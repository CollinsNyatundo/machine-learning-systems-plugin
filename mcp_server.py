#!/usr/bin/env python3
"""
Machine Learning Systems — MCP Server
Exposes the complete textbook (44 chapters, 111 definitions, 820 artifacts)
as MCP tools, resources, and prompts.

Usage:
    pip install fastmcp
    fastmcp run mcp_server.py:mcp                    # stdio (for Hermes install)
    fastmcp run mcp_server.py:mcp --transport http   # HTTP on port 8000
    fastmcp install claude-code mcp_server.py
    fastmcp install cursor mcp_server.py
    fastmcp install claude-desktop mcp_server.py
"""

from __future__ import annotations
from pathlib import Path
import json
import re
from functools import lru_cache
from fastmcp import FastMCP

# ── Configuration ──────────────────────────────────────────────
# Option 1: Relative to this file (for repo usage)
CHAPTERS_DIR = Path(__file__).parent / "skills" / "machine-learning-systems" / "chapters"

# Option 2: Absolute path (uncomment and adjust for installed plugin)
# CHAPTERS_DIR = Path.home() / ".gemini" / "config" / "plugins" / "machine-learning-systems" / "skills" / "machine-learning-systems" / "chapters"

# Verify path exists
if not CHAPTERS_DIR.exists():
    # Try common locations
    for fallback in [
        Path.cwd() / "skills" / "machine-learning-systems" / "chapters",
        Path.cwd() / "chapters",
        Path.home() / ".gemini" / "config" / "plugins" / "machine-learning-systems" / "skills" / "machine-learning-systems" / "chapters",
    ]:
        if fallback.exists():
            CHAPTERS_DIR = fallback
            break

mcp = FastMCP("Machine Learning Systems")

# ── Helpers ────────────────────────────────────────────────────

@lru_cache(maxsize=1)
def _load_chapter_index() -> list[dict]:
    """Load metadata for all chapter files."""
    chapters = []
    for md in sorted(CHAPTERS_DIR.glob("*.md")):
        if md.name in {"SKILL.md", "glossary.md", "patterns.md", "cheatsheet.md"}:
            continue
        text = md.read_text(encoding="utf-8")
        title = text.split("\n")[0].replace("# ", "") if text.startswith("# ") else md.stem
        vol = "Vol 2" if md.name.startswith("v2_") else "Vol 1"
        chapters.append({
            "file": md.name,
            "title": title,
            "volume": vol,
            "size_kb": md.stat().st_size // 1024,
            "path": str(md)
        })
    return chapters

@lru_cache(maxsize=1)
def _load_glossary_entries() -> list[dict]:
    """Parse glossary.md into structured entries."""
    text = (CHAPTERS_DIR / "glossary.md").read_text(encoding="utf-8")
    entries = []
    parts = text.split("\n---\n")
    for part in parts[1:]:  # skip header
        lines = part.strip().split("\n")
        if not lines:
            continue
        term = lines[0].replace("### ", "").strip()
        heading = None
        source = None
        content = ""
        for line in lines[1:]:
            if line.startswith("**Full heading:**"):
                heading = line.replace("**Full heading:**", "").strip()
            elif line.startswith("**Source:**"):
                source = line.replace("**Source:**", "").strip().replace("`", "")
            elif line and not line.startswith("**") and not heading:
                content += line + " "
        entries.append({
            "term": term,
            "heading": heading,
            "source": source,
            "content": content.strip()
        })
    return entries

@lru_cache(maxsize=1)
def _load_patterns_index() -> list[dict]:
    """Parse patterns.md into structured artifacts."""
    text = (CHAPTERS_DIR / "patterns.md").read_text(encoding="utf-8")
    artifacts = []
    parts = text.split("\n---\n")
    for part in parts[1:]:  # skip header
        lines = part.strip().split("\n")
        if not lines:
            continue
        name = lines[0].replace("### ", "").strip()
        source = None
        version = None
        chapter = None
        content = ""
        for line in lines[1:]:
            if line.startswith("**Source:**"):
                source = line.replace("**Source:**", "").strip().replace("`", "")
            elif line.startswith("**Full heading:**"):
                version = line.replace("**Full heading:**", "").strip()
            elif line.startswith("**Chapter:**"):
                chapter = line.replace("**Chapter:**", "").strip()
            elif line and not line.startswith("**") and not line.startswith("---"):
                content += line + " "
        artifacts.append({
            "name": name,
            "source": source,
            "version": version,
            "chapter": chapter,
            "content": content.strip()
        })
    return artifacts

# ── Resources ──────────────────────────────────────────────────

@mcp.resource("ml-systems://index")
def chapter_index() -> str:
    """Complete chapter listing with metadata (44 chapters)."""
    chapters = _load_chapter_index()
    vol1 = [c for c in chapters if c["volume"] == "Vol 1"]
    vol2 = [c for c in chapters if c["volume"] == "Vol 2"]
    return json.dumps({
        "total_chapters": len(chapters),
        "vol1_count": len(vol1),
        "vol2_count": len(vol2),
        "vol1": vol1,
        "vol2": vol2
    }, indent=2)

@mcp.resource("ml-systems://glossary")
def glossary() -> str:
    """All 111 definitions, alphabetical, with Vol 1/Vol 2 disambiguation."""
    return (CHAPTERS_DIR / "glossary.md").read_text(encoding="utf-8")

@mcp.resource("ml-systems://patterns")
def patterns() -> str:
    """All 820 named artifacts across 8 categories."""
    return (CHAPTERS_DIR / "patterns.md").read_text(encoding="utf-8")

@mcp.resource("ml-systems://cheatsheet")
def cheatsheet() -> str:
    """Key formulas, quantitative rules of thumb, hardware constants."""
    return (CHAPTERS_DIR / "cheatsheet.md").read_text(encoding="utf-8")

@mcp.resource("ml-systems://skill")
def skill_manifest() -> str:
    """Plugin SKILL.md manifest."""
    return (CHAPTERS_DIR / "SKILL.md").read_text(encoding="utf-8")

# ── Tools ──────────────────────────────────────────────────────

@mcp.tool
def search_chapters(query: str, volume: str = "both", limit: int = 10) -> str:
    """
    Search chapter content by keyword with context.
    
    Args:
        query: Search term (case-insensitive, searches full text)
        volume: "1" | "2" | "both" (default: both)
        limit: Max results (default: 10)
    
    Returns:
        JSON with matching sections including file, line number, and context.
    """
    results = []
    vol_prefix = None
    if volume == "1":
        vol_prefix = ("ch", "app")
    elif volume == "2":
        vol_prefix = ("v2_ch", "v2_app")
    
    for md in sorted(CHAPTERS_DIR.glob("*.md")):
        if md.name in {"SKILL.md", "glossary.md", "patterns.md", "cheatsheet.md"}:
            continue
        if vol_prefix and not md.name.startswith(vol_prefix):
            continue
        
        text = md.read_text(encoding="utf-8")
        lines = text.split("\n")
        query_lower = query.lower()
        
        for i, line in enumerate(lines):
            if query_lower in line.lower():
                start = max(0, i - 2)
                end = min(len(lines), i + 3)
                context = "\n".join(lines[start:end])
                results.append({
                    "file": md.name,
                    "line": i + 1,
                    "context": context[:500]
                })
                if len(results) >= limit:
                    break
        if len(results) >= limit:
            break
    
    return json.dumps({
        "query": query,
        "volume_filter": volume,
        "results": results,
        "count": len(results)
    }, indent=2)

@mcp.tool
def get_definition(term: str) -> str:
    """
    Get a glossary definition by term (fuzzy, case-insensitive).
    
    Args:
        term: Term to look up (e.g., "MFU", "Arithmetic Intensity", "Iron Law")
    
    Returns:
        Full definition entry or error with suggestions.
    """
    entries = _load_glossary_entries()
    term_lower = term.lower()
    
    # Exact match first
    for entry in entries:
        if entry["term"].lower() == term_lower:
            return json.dumps(entry, indent=2)
    
    # Partial match
    matches = [e for e in entries if term_lower in e["term"].lower()]
    if matches:
        return json.dumps({"matches": matches}, indent=2)
    
    # Fuzzy: search in content
    content_matches = [e for e in entries if term_lower in e["content"].lower()]
    if content_matches:
        return json.dumps({"content_matches": content_matches[:5]}, indent=2)
    
    return json.dumps({
        "error": f"Definition not found: {term}",
        "suggestion": "Try search_chapters for broader search",
        "total_entries": len(entries)
    }, indent=2)

@mcp.tool
def get_artifact(artifact_type: str, identifier: str) -> str:
    """
    Get a specific artifact from patterns.md.
    
    Args:
        artifact_type: One of: napkin_math, checkpoint, systems_perspective, 
                       principle, war_story, lighthouse, example, definition
        identifier: Partial name or number (e.g., "1.1", "MFU", "Ridge Point")
    
    Returns:
        Full artifact entry or error.
    """
    artifacts = _load_patterns_index()
    type_lower = artifact_type.lower().replace("_", " ")
    id_lower = identifier.lower()
    
    matches = []
    for a in artifacts:
        name_lower = a["name"].lower()
        content_lower = a["content"].lower()
        
        # Match type in name or version
        if type_lower in name_lower or (a["version"] and type_lower in a["version"].lower()):
            if id_lower in name_lower or id_lower in content_lower or id_lower in (a["version"] or "").lower():
                matches.append(a)
    
    if matches:
        return json.dumps({"matches": matches}, indent=2)
    
    return json.dumps({
        "error": f"Artifact not found: {artifact_type} ~ {identifier}",
        "suggestion": "Use list_artifacts to browse available artifacts"
    }, indent=2)

@mcp.tool
def get_chapter(file: str) -> str:
    """
    Get full chapter content by filename.
    
    Args:
        file: Chapter filename (e.g., "ch04.md", "v2_ch06.md", "appE.md", "v2_appC.md")
    
    Returns:
        Full chapter markdown or error.
    """
    path = CHAPTERS_DIR / file
    if not path.exists():
        # List available files
        available = [c["file"] for c in _load_chapter_index()]
        return json.dumps({
            "error": f"Chapter not found: {file}",
            "available": available
        }, indent=2)
    return path.read_text(encoding="utf-8")

@mcp.tool
def get_formula(formula_name: str) -> str:
    """
    Get a specific formula from cheatsheet.md.
    
    Args:
        formula_name: Formula identifier (e.g., "Iron Law", "MFU", "Ridge Point", "Young-Daly", "KL")
    
    Returns:
        Formula with context or error.
    """
    cheatsheet = (CHAPTERS_DIR / "cheatsheet.md").read_text(encoding="utf-8")
    lines = cheatsheet.split("\n")
    name_lower = formula_name.lower()
    
    for i, line in enumerate(lines):
        if name_lower in line.lower():
            start = max(0, i - 1)
            end = min(len(lines), i + 3)
            return "\n".join(lines[start:end])
    
    # Also check table rows
    for row in re.findall(r"^\|.*?\|.*?\|", cheatsheet, re.MULTILINE):
        if name_lower in row.lower():
            return row
    
    return json.dumps({
        "error": f"Formula not found: {formula_name}",
        "suggestion": "Try 'Iron Law', 'MFU', 'Ridge Point', 'Young-Daly', 'KL Divergence', 'Arithmetic Intensity'"
    }, indent=2)

@mcp.tool
def list_artifacts(artifact_type: str = "all", volume: str = "both", limit: int = 100) -> str:
    """
    List all artifacts of a given type, optionally filtered by volume.
    
    Args:
        artifact_type: "all" | "napkin_math" | "checkpoint" | "systems_perspective" | 
                       "principle" | "war_story" | "lighthouse" | "example" | "definition"
        volume: "1" | "2" | "both"
        limit: Max results
    
    Returns:
        JSON list of artifact names.
    """
    artifacts = _load_patterns_index()
    type_lower = artifact_type.lower().replace("_", " ") if artifact_type != "all" else None
    vol_filter = None
    if volume == "1":
        vol_filter = "(Vol 1)"
    elif volume == "2":
        vol_filter = "(Vol 2)"
    
    results = []
    for a in artifacts:
        name = a["name"]
        version = a["version"] or ""
        
        if type_lower and type_lower not in name.lower() and type_lower not in version.lower():
            continue
        if vol_filter and vol_filter not in name and vol_filter not in version:
            continue
        
        results.append({
            "name": name,
            "source": a["source"],
            "chapter": a["chapter"]
        })
        if len(results) >= limit:
            break
    
    return json.dumps({
        "type": artifact_type,
        "volume": volume,
        "count": len(results),
        "artifacts": results
    }, indent=2)

@mcp.tool
def get_cheatsheet_section(section: str) -> str:
    """
    Get a section from cheatsheet.md.
    
    Args:
        section: "key_numbers" | "formulas" | "rules" | "links"
    
    Returns:
        Relevant cheatsheet section.
    """
    cheatsheet = (CHAPTERS_DIR / "cheatsheet.md").read_text(encoding="utf-8")
    sections = {
        "key_numbers": "## Key Numbers",
        "formulas": "## Key Formulas",
        "rules": "## Rules of Thumb",
        "links": "## Quick Links"
    }
    
    if section not in sections:
        return json.dumps({
            "error": f"Unknown section: {section}",
            "available": list(sections.keys())
        }, indent=2)
    
    header = sections[section]
    start = cheatsheet.find(header)
    if start == -1:
        return json.dumps({"error": f"Section not found: {header}"}, indent=2)
    
    # Find next ## header
    next_header = cheatsheet.find("\n## ", start + 1)
    if next_header == -1:
        content = cheatsheet[start:]
    else:
        content = cheatsheet[start:next_header]
    
    return content.strip()

# ── Prompts ────────────────────────────────────────────────────

@mcp.prompt
def study_chapter(chapter: str) -> str:
    """
    Generate a structured study prompt for a chapter.
    
    Args:
        chapter: Chapter file name (e.g., "ch04.md", "v2_ch06.md")
    """
    return f"""You are studying Chapter: {chapter} from "Machine Learning Systems" by Vijay Janapa Reddi (Harvard SEAS, CS 249r).

Please provide a comprehensive study guide with:

1. **Core Concepts** — 3-5 key takeaways from this chapter
2. **Quantitative Invariants** — All formulas, laws, ridge points, MFU calculations, arithmetic intensity boundaries
3. **Systems Perspectives** — Architectural insights, trade-offs, design principles
4. **Napkin Math** — Every worked example with numbers and units
5. **Checkpoints** — All self-check questions from the chapter
6. **Cross-References** — How this connects to other chapters (Vol 1 ↔ Vol 2)
7. **Key Definitions** — All formal definitions introduced

Format as a structured study guide with clear sections. Use the chapter content as the authoritative source. Be specific with numbers, formulas, and quantitative claims."""

@mcp.prompt
def compare_volumes(topic: str) -> str:
    """
    Compare how a topic is treated in Vol 1 (single-machine) vs Vol 2 (fleet scale).
    
    Args:
        topic: Topic to compare (e.g., "MFU", "Checkpointing", "Data Loading", "Network Fabrics", "Model Serving")
    """
    return f"""Compare the treatment of "{topic}" across both volumes of "Machine Learning Systems" by Vijay Janapa Reddi:

**Vol 1 (Foundations)** — Single-machine perspective
**Vol 2 (Scale)** — Fleet/distributed perspective

For each volume, extract and compare:
- Key definitions and formulas
- Systems perspectives / architectural insights  
- Quantitative constraints (Iron Law terms: D_vol, BW, R_peak, L_lat, O)
- Napkin math / worked examples
- Checkpoints (self-check questions)
- Principles / invariants

Synthesize:
1. What fundamentally changes at scale?
2. What invariants remain the same?
3. What new constraints emerge in Vol 2?
4. How do the quantitative trade-offs shift?

Provide specific numbers, formulas, and quantitative comparisons where possible."""

@mcp.prompt
def design_review(system_description: str) -> str:
    """
    Use ML Systems principles to review a system design.
    
    Args:
        system_description: Description of the ML system to review
    """
    return f"""You are a Machine Learning Systems expert (per "Machine Learning Systems" by Vijay Janapa Reddi, Harvard SEAS). Review this system design:

{system_description}

Apply the **D·A·M Taxonomy** (Data, Algorithm, Machine) and the **Iron Law of ML Systems**:
T = D_vol/BW + O/(R_peak·η_hw) + L_lat

Analyze across three axes:

### 1. Data Axis (D_vol, BW)
- Data volume and movement patterns
- Bandwidth requirements (memory, network, storage)
- Data gravity, training-serving skew, feature store needs
- Pipeline architecture (ETL/ELT, freshness, correctness)

### 2. Algorithm Axis (O, Arithmetic Intensity)
- Total operations (O) and compute intensity
- Ridge point analysis: AI = FLOPs/Byte vs R_peak/BW
- Critical batch size, MFU targets
- Model architecture efficiency

### 3. Machine Axis (R_peak, η_hw, L_lat)
- Hardware selection and peak throughput
- Memory wall vs compute wall
- Latency budget decomposition (L_lat)
- Hardware utilization (MFU = Achieved/Peak)

### Scaling Analysis
- **Bisection bandwidth** for distributed operations
- **Checkpoint overhead** (Young-Daly: τ_opt = √(2·T_write·MTBF))
- **MFU ceiling** and utilization gaps
- **Fault tolerance** (GPU MTBF, fleet reliability)

### Output Required
1. **Bottleneck identification** — Which axis dominates? Quantify.
2. **Scaling limits** — At what scale does this break? (GPU count, data volume, model size)
3. **Quantitative risks** — MTBF, checkpoint storm, ridge point, MFU gap
4. **Specific mitigations** — Overlap, compression, sparsity, topology, scheduling
5. **Napkin math** — Back-of-envelope estimates for key metrics

Provide specific numbers, formulas, and quantitative claims wherever possible. Reference the textbook's worked examples and principles."""

@mcp.prompt
def exam_prep(chapters: str = "all") -> str:
    """
    Generate exam preparation materials.
    
    Args:
        chapters: Comma-separated chapter files, or "all", "vol1", "vol2"
    """
    return f"""Generate comprehensive exam preparation materials for Machine Learning Systems (CS 249r), covering: {chapters}.

Include for each chapter:
1. **Key Definitions** — All formal definitions
2. **Core Formulas** — Every quantitative relationship
3. **Napkin Math** — All worked examples with step-by-step
4. **Checkpoints** — All self-check questions + answers
5. **Systems Perspectives** — Architectural insights
6. **Principles** — Invariants and laws
7. **Cross-Chapter Links** — How concepts connect

Format as a structured study packet with:
- One-page formula sheet
- Concept map (D·A·M taxonomy connections)
- Practice problems with solutions
- Common pitfalls and misconceptions

Focus on quantitative reasoning — this exam tests systems thinking with numbers, not memorization."""

# ── Run ────────────────────────────────────────────────────────
if __name__ == "__main__":
    mcp.run()