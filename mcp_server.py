#!/usr/bin/env python3
"""
Machine Learning Systems - MCP server.

Exposes the reference collection (chapters, definitions, indexed artifacts,
cheatsheet) as MCP tools, resources and prompts. All content is indexed once
in memory (see ``mlsys_index.py``); tools return compact structured results by
default and take ``verbose=True`` for fuller text.

Usage:
    pip install -r requirements.txt
    fastmcp run mcp_server.py:mcp                    # stdio
    fastmcp run mcp_server.py:mcp --transport http   # HTTP on port 8000

Set ML_SYSTEMS_DIR to point at a different ``skills/machine-learning-systems`` directory.
"""

from __future__ import annotations

import json
import re
import threading
from typing import Annotated

from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from pydantic import Field

from mlsys_index import (
    KIND_LABELS,
    Corpus,
    CorpusError,
    fts_query,
    normalize_kind,
    normalize_volume,
    summarize,
)

mcp = FastMCP("Machine Learning Systems")

READ_ONLY = {"readOnlyHint": True, "idempotentHint": True, "openWorldHint": False}

DEFAULT_CHAPTER_CHARS = 20_000
MAX_CHAPTER_CHARS = 100_000
MAX_SEARCH_RESULTS = 25

# ── Corpus access ──────────────────────────────────────────────

_corpus: Corpus | None = None
_corpus_lock = threading.Lock()


def get_corpus() -> Corpus:
    """Build the index on first use; later calls reuse it."""
    global _corpus
    if _corpus is None:
        with _corpus_lock:
            if _corpus is None:
                try:
                    _corpus = Corpus()
                except CorpusError as exc:
                    raise ToolError(str(exc)) from exc
    return _corpus


def reset_corpus(corpus: Corpus | None = None) -> None:
    """Swap (or clear) the shared index. Used by tests and after content edits."""
    global _corpus
    with _corpus_lock:
        _corpus = corpus


def _volume(value: str | int | None) -> int | None:
    try:
        return normalize_volume(value)
    except ValueError as exc:
        raise ToolError(str(exc)) from exc


def _kind(value: str | None) -> str | None:
    try:
        return normalize_kind(value)
    except ValueError as exc:
        raise ToolError(str(exc)) from exc


def _require_text(name: str, value: str, max_len: int = 200) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ToolError(f"'{name}' must be a non-empty string.")
    return value.strip()[:max_len]


def _clamp(value: int, low: int, high: int) -> int:
    return max(low, min(high, int(value)))


def _resolve_chapter(corpus: Corpus, file: str) -> str:
    """Map 'ch05', 'ch05.md' or 'v2_ch06' to an indexed chapter file name (whitelist lookup)."""
    name = _require_text("file", file, 100)
    for candidate in (name, f"{name}.md"):
        if candidate in corpus.chapters:
            return candidate
        lowered = {k.lower(): k for k in corpus.chapters}
        if candidate.lower() in lowered:
            return lowered[candidate.lower()]
    raise ToolError(f"Chapter not found: {file!r}. Available: {', '.join(corpus.chapters)}")


# ── Resources ──────────────────────────────────────────────────


@mcp.resource("ml-systems://index", mime_type="application/json")
def chapter_index() -> str:
    """Chapter listing with metadata and live corpus counts."""
    corpus = get_corpus()
    chapters = list(corpus.chapters.values())
    by_kind = {kind: 0 for kind in KIND_LABELS}
    for row in corpus.artifact_rows(None, None):
        by_kind[row["kind"]] += 1
    return json.dumps(
        {
            "total_chapters": len(chapters),
            "definitions": by_kind["definition"],
            "artifacts": sum(by_kind.values()),
            "artifacts_by_type": by_kind,
            "volume_1": [c for c in chapters if c["volume"] == 1],
            "volume_2": [c for c in chapters if c["volume"] == 2],
        },
        indent=2,
        ensure_ascii=False,
    )


@mcp.resource("ml-systems://glossary")
def glossary() -> str:
    """Glossary (generated from the chapters' formal definitions)."""
    return _read_reference("glossary.md")


@mcp.resource("ml-systems://patterns", mime_type="application/json")
def patterns() -> str:
    """Compact catalog of indexed artifacts (titles only). Use get_artifact for text."""
    corpus = get_corpus()
    catalog: dict[str, list[dict]] = {kind: [] for kind in KIND_LABELS}
    for row in corpus.artifact_rows(None, None):
        catalog[row["kind"]].append(
            {"id": row["num"], "title": row["title"], "file": row["file"], "volume": row["volume"]}
        )
    return json.dumps(catalog, indent=1, ensure_ascii=False)


@mcp.resource("ml-systems://cheatsheet")
def cheatsheet() -> str:
    """Formulas and hardware numbers quick reference."""
    return _read_reference("cheatsheet.md")


@mcp.resource("ml-systems://skill")
def skill_manifest() -> str:
    """Plugin SKILL.md manifest."""
    return _read_reference("SKILL.md")


def _read_reference(name: str) -> str:
    path = get_corpus().skill_dir / name
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ToolError(f"Reference file unavailable: {name}") from exc


# ── Tools ──────────────────────────────────────────────────────


@mcp.tool(annotations=READ_ONLY)
def search_chapters(
    query: Annotated[str, Field(description="Words to search for, e.g. 'roofline arithmetic intensity'")],
    volume: Annotated[str, Field(description="'1', '2' or 'both'")] = "both",
    limit: Annotated[int, Field(description=f"Max results (1-{MAX_SEARCH_RESULTS})")] = 10,
    verbose: Annotated[bool, Field(description="Longer snippets")] = False,
) -> dict:
    """BM25-ranked full-text search over all chapters. Returns compact snippets with file and heading."""
    text = _require_text("query", query, 300)
    vol = _volume(volume)
    limit = _clamp(limit, 1, MAX_SEARCH_RESULTS)
    results = get_corpus().search(text, vol, limit, 600 if verbose else 240)
    return {"query": text, "volume": vol or "both", "count": len(results), "results": results}


@mcp.tool(annotations=READ_ONLY)
def get_definition(
    term: Annotated[str, Field(description="Term to look up, e.g. 'Backpropagation' or 'Iron Law'")],
    limit: Annotated[int, Field(description="Max matches (1-10)")] = 5,
    verbose: Annotated[bool, Field(description="Full definition text for every match")] = False,
) -> dict:
    """Look up a formal definition. An exact term match returns its full text."""
    text = _require_text("term", term)
    limit = _clamp(limit, 1, 10)
    corpus = get_corpus()
    defs = corpus.definitions()
    lowered = text.lower()

    exact = [r for r in defs if r["title"].lower() == lowered]
    partial = [r for r in defs if r not in exact and lowered in r["title"].lower()]
    ranked = exact + partial
    if len(ranked) < limit:
        match = fts_query(text, "and") or fts_query(text, "or")
        if match:
            ids = {r["id"] for r in ranked}
            for row in corpus.query(
                "SELECT a.* FROM artifact_fts f JOIN artifacts a ON a.id = f.rowid "
                "WHERE artifact_fts MATCH ? AND a.kind = 'definition' ORDER BY bm25(artifact_fts, 8.0, 1.0) LIMIT ?",
                (match, limit),
            ):
                if row["id"] not in ids:
                    ranked.append(row)
    if not ranked:
        raise ToolError(f"No definition found for {term!r}. Try search_chapters.")

    matches = []
    for i, r in enumerate(ranked[:limit]):
        full = verbose or (i == 0 and len(exact) == 1)
        matches.append(
            {
                "term": r["title"],
                "definition_id": r["num"],
                "volume": r["volume"],
                "source": r["file"],
                "chapter": r["chapter"],
                "definition": summarize(r["body"], 4000 if full else 300),
                "exact": r in exact,
            }
        )
    return {"query": text, "count": len(matches), "matches": matches}


@mcp.tool(annotations=READ_ONLY)
def get_artifact(
    artifact_type: Annotated[
        str, Field(description="napkin_math, systems_perspective, checkpoint, example, lighthouse, war_story, principle, definition")
    ],
    identifier: Annotated[str, Field(description="Number like '18.2' or words from the title")],
    verbose: Annotated[bool, Field(description="Longer text (default is a short excerpt)")] = False,
) -> dict:
    """Fetch artifacts by type and number or title (content is not searched; use search_chapters for that)."""
    kind = _kind(artifact_type)
    if kind is None:
        raise ToolError("artifact_type is required (not 'all').")
    ident = _require_text("identifier", identifier)
    rows = get_corpus().artifact_rows(kind, None)
    number = re.fullmatch(r"[A-Za-z]?\d+(?:\.\d+)*", ident)
    if number:
        hits = [r for r in rows if r["num"] == ident]
    else:
        words = [w for w in re.findall(r"\w+", ident.lower())]
        hits = [r for r in rows if all(w in r["title"].lower() for w in words)]
    if not hits:
        raise ToolError(f"No {KIND_LABELS[kind]} matching {identifier!r}. Use list_artifacts to browse.")
    cap = 6000 if verbose else 1200
    return {
        "type": kind,
        "count": len(hits),
        "artifacts": [
            {
                "id": r["num"],
                "title": r["title"],
                "source": r["file"],
                "volume": r["volume"],
                "chapter": r["chapter"],
                "text": summarize(r["body"], cap),
                "truncated": len(re.sub(r"\s+", " ", r["body"])) > cap,
            }
            for r in hits[:5]
        ],
    }


@mcp.tool(annotations=READ_ONLY)
def get_chapter(
    file: Annotated[str, Field(description="Chapter file, e.g. 'ch04', 'ch04.md', 'v2_ch06', 'appE'")],
    section: Annotated[str | None, Field(description="Return only the section whose heading contains this text")] = None,
    offset: Annotated[int, Field(description="Character offset to continue from (use next_offset)")] = 0,
    max_chars: Annotated[int, Field(description=f"Page size, up to {MAX_CHAPTER_CHARS}")] = DEFAULT_CHAPTER_CHARS,
) -> dict:
    """Read a chapter in pages. The first page (no section) also returns a heading outline for navigation."""
    corpus = get_corpus()
    name = _resolve_chapter(corpus, file)
    lines = corpus.chapter_lines(name)
    sections = corpus.chapter_sections(name)
    offset = max(0, int(offset))
    max_chars = _clamp(max_chars, 500, MAX_CHAPTER_CHARS)

    heading = None
    if section:
        needle = section.strip().lower()
        found = next((s for s in sections if needle in s.heading.lower()), None)
        if found is None:
            outline = [s.heading for s in sections if s.level == 2][:60]
            raise ToolError(f"Section {section!r} not found in {name}. Level-2 headings: {outline}")
        heading = found.heading
        text = "\n".join(lines[found.start : found.end])
    else:
        text = "\n".join(lines)

    page = text[offset : offset + max_chars]
    end = offset + len(page)
    result: dict = {
        "file": name,
        "title": corpus.chapters[name]["title"],
        "section": heading,
        "total_chars": len(text),
        "offset": offset,
        "returned_chars": len(page),
        "truncated": end < len(text),
        "next_offset": end if end < len(text) else None,
        "content": page,
    }
    if not section and offset == 0:
        result["outline"] = [s.heading for s in sections if s.level == 2][:80]
    return result


@mcp.tool(annotations=READ_ONLY)
def get_formula(
    formula_name: Annotated[str, Field(description="Formula or constant, e.g. 'roofline', 'KV cache', 'H100'")],
    limit: Annotated[int, Field(description="Max matching cheatsheet sections (1-5)")] = 3,
) -> dict:
    """Find formulas and constants in the cheatsheet (ranked). Returns the matching sections."""
    text = _require_text("formula_name", formula_name)
    limit = _clamp(limit, 1, 5)
    corpus = get_corpus()
    hits: list = []
    for mode in ("and", "or"):
        match = fts_query(text, mode)
        if match:
            hits = corpus.query(
                "SELECT section, text FROM cheat_fts WHERE cheat_fts MATCH ? ORDER BY bm25(cheat_fts, 4.0, 1.0) LIMIT ?",
                (match, limit),
            )
        if hits:
            break
    if not hits:
        raise ToolError(f"No cheatsheet entry matches {formula_name!r}. Use get_cheatsheet_section to list sections.")
    return {
        "query": text,
        "count": len(hits),
        "results": [{"section": h["section"], "text": summarize_block(h["text"], 2500)} for h in hits],
    }


@mcp.tool(annotations=READ_ONLY)
def list_artifacts(
    artifact_type: Annotated[str, Field(description="'all' or one type such as napkin_math, checkpoint, war_story")] = "all",
    volume: Annotated[str, Field(description="'1', '2' or 'both'")] = "both",
    limit: Annotated[int, Field(description="Page size (1-200)")] = 50,
    offset: Annotated[int, Field(description="Skip this many entries")] = 0,
) -> dict:
    """List artifact titles (no body text). Page with limit/offset; fetch text via get_artifact."""
    kind, vol = _kind(artifact_type), _volume(volume)
    limit, offset = _clamp(limit, 1, 200), max(0, int(offset))
    rows = get_corpus().artifact_rows(kind, vol)
    page = rows[offset : offset + limit]
    return {
        "total": len(rows),
        "offset": offset,
        "count": len(page),
        "next_offset": offset + limit if offset + limit < len(rows) else None,
        "artifacts": [
            {"type": r["kind"], "id": r["num"], "title": r["title"], "source": r["file"], "volume": r["volume"]}
            for r in page
        ],
    }


@mcp.tool(annotations=READ_ONLY)
def get_cheatsheet_section(
    section: Annotated[str, Field(description="Part of a section heading, e.g. 'roofline'. Use 'list' to see all headings.")],
) -> dict:
    """Return a cheatsheet section by heading text, or list the headings."""
    text = _require_text("section", section)
    sections = get_corpus().cheat_sections
    headings = [s["heading"] for s in sections]
    if text.lower() in {"list", "all", "*"}:
        return {"sections": headings}
    words = re.findall(r"\w+", text.lower())
    hits = [s for s in sections if all(w in s["heading"].lower() for w in words)]
    if not hits:
        raise ToolError(f"No cheatsheet section matches {section!r}. Available: {headings}")
    return {"sections": [{"heading": s["heading"], "text": s["text"]} for s in hits[:3]]}


def summarize_block(text: str, limit: int) -> str:
    """Trim multi-line text (keeps line breaks, unlike summarize)."""
    return text if len(text) <= limit else text[:limit].rsplit("\n", 1)[0] + "\n…"


# ── Prompts ────────────────────────────────────────────────────

IRON_LAW = r"\( T = \frac{D_{\text{vol}}}{BW} + \frac{O}{R_{\text{peak}} \cdot \eta_{\text{hw}}} + L_{\text{lat}} \)"


@mcp.prompt
def study_chapter(chapter: str) -> str:
    """Generate a structured study prompt for one chapter (e.g. "ch04", "v2_ch06")."""
    corpus = get_corpus()
    try:
        name = _resolve_chapter(corpus, chapter)
    except ToolError as exc:  # FastMCP masks prompt exceptions, so answer with a usable message instead
        return str(exc)
    info = corpus.chapters[name]
    outline = "\n".join(f"- {s.heading}" for s in corpus.chapter_sections(name) if s.level == 2 and s.heading)[:3000]
    return f"""You are studying {info['title']} ({name}, Volume {info['volume']}) from "Machine Learning Systems" by Vijay Janapa Reddi (Harvard SEAS, CS 249r).

Read the chapter with the get_chapter tool (page through it with next_offset, or pass section=...). Section outline:
{outline}

Produce a study guide with:
1. **Core Concepts** - 3-5 key takeaways
2. **Quantitative Invariants** - formulas, laws, ridge points, MFU, arithmetic-intensity boundaries
3. **Systems Perspectives** - trade-offs and design principles
4. **Napkin Math** - each worked example with numbers and units
5. **Checkpoints** - the chapter's self-check questions
6. **Cross-References** - links to other chapters (Vol 1 and Vol 2)
7. **Key Definitions** - use get_definition for exact wording

Treat the chapter text as the authoritative source and be specific with numbers."""


@mcp.prompt
def compare_volumes(topic: str) -> str:
    """Compare how a topic is treated in Vol 1 (single machine) and Vol 2 (fleet scale)."""
    topic = _require_text("topic", topic)
    return f"""Compare the treatment of "{topic}" across both volumes of "Machine Learning Systems" by Vijay Janapa Reddi.

Use search_chapters(query="{topic}", volume="1") and volume="2", then get_chapter(section=...) for the best hits.

**Vol 1 (Foundations)** - single-machine perspective
**Vol 2 (Scale)** - fleet / distributed perspective

For each volume extract: key definitions and formulas, systems perspectives, quantitative constraints (Iron Law terms), napkin math, checkpoints, principles.

Then synthesize:
1. What fundamentally changes at scale?
2. What invariants stay the same?
3. What new constraints emerge in Vol 2?
4. How do the quantitative trade-offs shift?

Give specific numbers and formulas."""


@mcp.prompt
def design_review(system_description: str) -> str:
    """Review an ML system design using the D-A-M taxonomy and the Iron Law."""
    system_description = _require_text("system_description", system_description, 8000)
    return f"""You are a Machine Learning Systems expert (per "Machine Learning Systems" by Vijay Janapa Reddi, Harvard SEAS). Review this system design:

{system_description}

Apply the **D·A·M taxonomy** (Data, Algorithm, Machine) and the **Iron Law of ML Systems**:
{IRON_LAW}

Analyze three axes:

### 1. Data (\\(D_{{\\text{{vol}}}}\\), \\(BW\\))
- Data volume and movement, bandwidth needs (memory, network, storage)
- Data gravity, training-serving skew, feature stores, pipeline freshness and correctness

### 2. Algorithm (\\(O\\), arithmetic intensity)
- Total operations and compute intensity
- Ridge point: intensity = FLOPs/Byte versus \\(R_{{\\text{{peak}}}}/BW\\)
- Critical batch size, MFU targets, architecture efficiency

### 3. Machine (\\(R_{{\\text{{peak}}}}\\), \\(\\eta_{{\\text{{hw}}}}\\), \\(L_{{\\text{{lat}}}}\\))
- Hardware selection, memory wall vs compute wall
- Latency budget decomposition, utilization (MFU = achieved / peak)

### Scaling analysis
- Bisection bandwidth for distributed operations
- Checkpoint overhead (Young-Daly optimal interval)
- MFU ceiling and utilization gaps
- Fault tolerance (GPU MTBF, fleet reliability)

### Output required
1. **Bottleneck identification** - which axis dominates, quantified
2. **Scaling limits** - where the design breaks (GPU count, data volume, model size)
3. **Quantitative risks** - MTBF, checkpoint storms, ridge point, MFU gap
4. **Mitigations** - overlap, compression, sparsity, topology, scheduling
5. **Napkin math** - back-of-envelope estimates for key metrics

Ground claims in the textbook: use search_chapters, get_definition and get_formula."""


@mcp.prompt
def exam_prep(chapters: str = "all") -> str:
    """Generate exam preparation materials. `chapters`: "all", "vol1", "vol2", or comma-separated chapter files."""
    corpus = get_corpus()
    spec = chapters.strip().lower()
    if spec in {"all", "", "*"}:
        names = list(corpus.chapters)
    elif spec in {"vol1", "vol 1", "1"}:
        names = [n for n, c in corpus.chapters.items() if c["volume"] == 1]
    elif spec in {"vol2", "vol 2", "2"}:
        names = [n for n, c in corpus.chapters.items() if c["volume"] == 2]
    else:
        try:
            names = [_resolve_chapter(corpus, part) for part in spec.split(",") if part.strip()]
        except ToolError as exc:
            return str(exc)
    listing = ", ".join(names)
    return f"""Generate exam preparation materials for Machine Learning Systems (CS 249r) covering: {listing}.

For each chapter (use get_chapter, get_definition, list_artifacts, get_artifact):
1. **Key Definitions**
2. **Core Formulas** - every quantitative relationship
3. **Napkin Math** - worked examples, step by step
4. **Checkpoints** - self-check questions with answers
5. **Systems Perspectives** and **Principles**
6. **Cross-Chapter Links**

Package as a study packet with a one-page formula sheet, a concept map (D·A·M connections), practice problems with solutions, and common pitfalls.

Focus on quantitative reasoning: the exam tests systems thinking with numbers, not memorization."""


# ── Run ────────────────────────────────────────────────────────
if __name__ == "__main__":
    mcp.run()
