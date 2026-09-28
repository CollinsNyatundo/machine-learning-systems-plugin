"""In-memory index over the Machine Learning Systems reference corpus.

The chapters under ``skills/machine-learning-systems/chapters/`` are the single
source of truth. Everything else (definitions, artifacts, search, cheatsheet
rows) is derived from them at first use and held in an in-memory SQLite
database (FTS5 with BM25 ranking), so tool calls never re-read or re-parse
files.
"""

from __future__ import annotations

import os
import re
import sqlite3
import threading
from dataclasses import dataclass
from pathlib import Path

SKILL_NAME = "machine-learning-systems"
REPO_ROOT = Path(__file__).resolve().parent

# Artifact kinds recognised from chapter headings, e.g. "## Napkin Math 18.2: Title".
ARTIFACT_KINDS: dict[str, str] = {
    "Definition": "definition",
    "Napkin Math": "napkin_math",
    "Systems Perspective": "systems_perspective",
    "Checkpoint": "checkpoint",
    "Example": "example",
    "Lighthouse": "lighthouse",
    "War Story": "war_story",
    "Principle": "principle",
}
KIND_LABELS = {v: k for k, v in ARTIFACT_KINDS.items()}

HEADING_RE = re.compile(r"^(#{1,6})\s+(\S.*?)\s*$")
ARTIFACT_RE = re.compile(
    r"^(?P<label>" + "|".join(re.escape(k) for k in ARTIFACT_KINDS) + r")"
    r"(?:\s+(?P<num>[A-Z]?\d+(?:\.\d+)*))?\s*(?::\s*(?P<title>.*))?$"
)
MAX_CHUNK_CHARS = 2500


class CorpusError(RuntimeError):
    """The reference corpus is missing or unreadable."""


def locate_skill_dir() -> Path:
    """Find ``skills/machine-learning-systems`` (the dir holding ``chapters/``).

    Order: ``ML_SYSTEMS_DIR`` env var, next to this file, the current directory,
    then the Gemini/Antigravity plugin location.
    """
    candidates: list[Path] = []
    override = os.environ.get("ML_SYSTEMS_DIR")
    if override:
        candidates.append(Path(override).expanduser())
    candidates += [
        REPO_ROOT / "skills" / SKILL_NAME,
        Path.cwd() / "skills" / SKILL_NAME,
        Path.home() / ".gemini" / "config" / "plugins" / SKILL_NAME / "skills" / SKILL_NAME,
    ]
    for candidate in candidates:
        if (candidate / "chapters").is_dir():
            return candidate
    tried = ", ".join(str(c) for c in candidates)
    raise CorpusError(f"Could not find the '{SKILL_NAME}' chapters directory. Tried: {tried}. Set ML_SYSTEMS_DIR.")


def volume_of(filename: str) -> int:
    return 2 if filename.startswith("v2_") else 1


def normalize_volume(volume: str | int | None) -> int | None:
    """Return 1, 2, or None for both. Raises ValueError for anything else."""
    text = str(volume if volume is not None else "both").strip().lower()
    text = re.sub(r"^(vol(ume)?)[\s_-]*", "", text)
    if text in {"both", "all", "", "any", "*"}:
        return None
    if text in {"1", "2"}:
        return int(text)
    raise ValueError(f"Invalid volume {volume!r}; use '1', '2' or 'both'.")


def normalize_kind(kind: str | None) -> str | None:
    """Map 'Napkin Math', 'napkin-math', 'napkin_math' -> 'napkin_math'; 'all' -> None."""
    text = re.sub(r"[\s\-]+", "_", str(kind or "all").strip().lower())
    if text in {"all", "", "any", "*"}:
        return None
    if text not in KIND_LABELS:
        singular = text[:-3] + "y" if text.endswith("ies") else text.removesuffix("s")
        text = {"perspective": "systems_perspective", "story": "war_story"}.get(singular, singular)
    if text not in KIND_LABELS:
        raise ValueError(f"Unknown artifact type {kind!r}; choose one of: all, {', '.join(sorted(KIND_LABELS))}.")
    return text


def fts_query(text: str, mode: str = "and") -> str | None:
    """Turn free text into a safe FTS5 query (quoted tokens, prefix on the last)."""
    tokens = re.findall(r"[A-Za-z0-9_]+", text.lower())
    if not tokens:
        return None
    quoted = [f'"{t}"' for t in tokens]
    quoted[-1] += "*"
    return (" OR " if mode == "or" else " ").join(quoted)


@dataclass(frozen=True)
class Section:
    level: int
    heading: str
    start: int  # line index of the heading
    end: int  # exclusive line index


def split_sections(lines: list[str]) -> list[Section]:
    """Headings outside code fences, each with the line span it owns."""
    heads: list[tuple[int, int, str]] = []
    in_fence = False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if m:
            heads.append((i, len(m.group(1)), m.group(2)))
    sections = []
    for idx, (start, level, heading) in enumerate(heads):
        end = len(lines)
        for nstart, nlevel, _ in heads[idx + 1 :]:
            if nlevel <= level:
                end = nstart
                break
        sections.append(Section(level, heading, start, end))
    return sections


def clean_text(text: str) -> str:
    return re.sub(r"[ \t]+", " ", re.sub(r"\n{3,}", "\n\n", text)).strip()


def summarize(text: str, limit: int) -> str:
    """Whitespace-flattened excerpt of at most ~limit chars that never ends inside a math span."""
    flat = re.sub(r"\s+", " ", text).strip()
    if len(flat) <= limit:
        return flat
    cut = flat[:limit].rsplit(" ", 1)[0]
    for opener, closer in ((r"\(", r"\)"), (r"\[", r"\]")):
        if cut.count(opener) > cut.count(closer):
            cut = cut[: cut.rfind(opener)].rstrip()
    return cut + "…"


class Corpus:
    """Parsed chapters plus an in-memory FTS5 index. Build once, read many."""

    def __init__(self, skill_dir: Path | None = None) -> None:
        self.skill_dir = (skill_dir or locate_skill_dir()).resolve()
        self.chapters_dir = self.skill_dir / "chapters"
        if not self.chapters_dir.is_dir():
            raise CorpusError(f"Chapters directory not found: {self.chapters_dir}")
        self._lock = threading.RLock()
        self.db = sqlite3.connect(":memory:", check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.chapters: dict[str, dict] = {}
        self._lines: dict[str, list[str]] = {}
        self._sections: dict[str, list[Section]] = {}
        self._build()

    # ── build ────────────────────────────────────────────────────
    def _build(self) -> None:
        try:
            self.db.execute("CREATE VIRTUAL TABLE _probe USING fts5(x)")
            self.db.execute("DROP TABLE _probe")
        except sqlite3.OperationalError as exc:  # pragma: no cover - depends on the SQLite build
            raise CorpusError("This Python's SQLite lacks FTS5, which the search index requires.") from exc

        self.db.executescript(
            """
            CREATE TABLE artifacts(
                id INTEGER PRIMARY KEY, kind TEXT, num TEXT, title TEXT, file TEXT,
                volume INTEGER, chapter TEXT, body TEXT);
            CREATE VIRTUAL TABLE artifact_fts USING fts5(title, body, tokenize='porter unicode61');
            CREATE VIRTUAL TABLE chunk_fts USING fts5(
                heading, body, file UNINDEXED, volume UNINDEXED, tokenize='porter unicode61');
            CREATE TABLE cheat(id INTEGER PRIMARY KEY, section TEXT, text TEXT);
            CREATE VIRTUAL TABLE cheat_fts USING fts5(section, text, tokenize='porter unicode61');
            """
        )
        root = self.chapters_dir.resolve()
        paths = sorted(
            p for p in self.chapters_dir.glob("*.md")
            if p.name != "SKILL.md" and p.is_file() and p.resolve().is_relative_to(root)  # refuse symlink escapes
        )
        for path in paths:
            self._index_chapter(path)
        self._index_cheatsheet()
        self.db.commit()

    def _index_chapter(self, path: Path) -> None:
        name = path.name
        text = path.read_text(encoding="utf-8")
        lines = text.split("\n")
        sections = split_sections(lines)
        title = next((s.heading for s in sections if s.level == 1), path.stem)
        self._lines[name] = lines
        self._sections[name] = sections
        self.chapters[name] = {
            "file": name,
            "title": title,
            "volume": volume_of(name),
            "size_kb": max(1, round(len(text.encode("utf-8")) / 1024)),
            "sections": sum(1 for s in sections if s.level == 2),
        }

        # Search chunks: each section's own text (up to its first child heading).
        for idx, sec in enumerate(sections):
            own_end = sections[idx + 1].start if idx + 1 < len(sections) else len(lines)
            own_end = min(own_end, sec.end)
            body = clean_text("\n".join(lines[sec.start + 1 : own_end]))
            ancestors, floor = [], sec.level
            for prev in reversed(sections[:idx]):
                if prev.level < floor:
                    ancestors.append(prev.heading)
                    floor = prev.level
            heading_path = " > ".join([*reversed(ancestors[:2]), sec.heading])
            for chunk in self._chunk(body):
                self.db.execute(
                    "INSERT INTO chunk_fts(heading, body, file, volume) VALUES (?,?,?,?)",
                    (heading_path, chunk, name, volume_of(name)),
                )

        # Artifacts: headings such as "Definition 5.2: Backpropagation".
        for sec in sections:
            if sec.level not in (2, 3):
                continue
            m = ARTIFACT_RE.match(sec.heading)
            if not m:
                continue
            kind = ARTIFACT_KINDS[m.group("label")]
            body = clean_text("\n".join(lines[sec.start + 1 : sec.end]))
            art_title = (m.group("title") or "").strip() or sec.heading
            cur = self.db.execute(
                "INSERT INTO artifacts(kind,num,title,file,volume,chapter,body) VALUES (?,?,?,?,?,?,?)",
                (kind, m.group("num") or "", art_title, name, volume_of(name), title, body),
            )
            self.db.execute(
                "INSERT INTO artifact_fts(rowid,title,body) VALUES (?,?,?)", (cur.lastrowid, art_title, body)
            )

    @staticmethod
    def _chunk(body: str) -> list[str]:
        if not body:
            return []
        if len(body) <= MAX_CHUNK_CHARS:
            return [body]
        chunks, current = [], ""
        for para in body.split("\n\n"):
            while len(para) > MAX_CHUNK_CHARS:
                cut = para.rfind(" ", 0, MAX_CHUNK_CHARS) or MAX_CHUNK_CHARS
                chunks.append((current + "\n\n" + para[:cut]).strip())
                current, para = "", para[cut:].lstrip()
            if len(current) + len(para) + 2 > MAX_CHUNK_CHARS and current:
                chunks.append(current.strip())
                current = ""
            current = (current + "\n\n" + para).strip()
        if current:
            chunks.append(current)
        return [c for c in chunks if c]

    def _index_cheatsheet(self) -> None:
        self.cheat_sections: list[dict] = []
        path = self.skill_dir / "cheatsheet.md"
        if not path.is_file():
            return
        lines = path.read_text(encoding="utf-8").split("\n")
        sections = split_sections(lines)
        for sec in sections:
            if sec.level < 2:
                continue
            own_end = next((s.start for s in sections if s.start > sec.start), len(lines))
            own_end = min(own_end, sec.end)
            body = "\n".join(lines[sec.start + 1 : own_end]).strip()
            full = "\n".join(lines[sec.start : sec.end]).strip()
            self.cheat_sections.append({"level": sec.level, "heading": sec.heading, "text": full})
            if body:
                cur = self.db.execute("INSERT INTO cheat(section,text) VALUES (?,?)", (sec.heading, body))
                self.db.execute(
                    "INSERT INTO cheat_fts(rowid,section,text) VALUES (?,?,?)", (cur.lastrowid, sec.heading, body)
                )

    # ── queries ──────────────────────────────────────────────────
    def query(self, sql: str, params: tuple = ()) -> list[sqlite3.Row]:
        with self._lock:
            return self.db.execute(sql, params).fetchall()

    def search(self, text: str, volume: int | None, limit: int, snippet_chars: int) -> list[dict]:
        """BM25-ranked chunk search: AND semantics first, OR fallback."""
        for mode in ("and", "or"):
            match = fts_query(text, mode)
            if match is None:
                return []
            sql = (
                "SELECT file, volume, heading, bm25(chunk_fts, 6.0, 1.0) AS score, "
                "snippet(chunk_fts, 1, '[', ']', ' … ', ?) AS snip "
                "FROM chunk_fts WHERE chunk_fts MATCH ?"
            )
            params: list = [max(8, min(64, snippet_chars // 6)), match]
            if volume is not None:
                sql += " AND volume = ?"
                params.append(volume)
            sql += " ORDER BY score LIMIT ?"
            params.append(limit * 3)
            rows = self.query(sql, tuple(params))
            if rows:
                break
        results, seen = [], set()
        for row in rows:
            key = (row["file"], row["heading"], row["snip"][:60])
            if key in seen:
                continue
            seen.add(key)
            results.append(
                {
                    "file": row["file"],
                    "chapter": self.chapters[row["file"]]["title"],
                    "volume": row["volume"],
                    "heading": row["heading"],
                    "score": round(-row["score"], 3),
                    "snippet": row["snip"],
                }
            )
            if len(results) >= limit:
                break
        return results

    def artifact_rows(self, kind: str | None, volume: int | None) -> list[sqlite3.Row]:
        sql, params = "SELECT * FROM artifacts WHERE 1=1", []
        if kind:
            sql += " AND kind = ?"
            params.append(kind)
        if volume is not None:
            sql += " AND volume = ?"
            params.append(volume)
        return self.query(sql + " ORDER BY volume, file, id", tuple(params))

    def definitions(self) -> list[sqlite3.Row]:
        return self.artifact_rows("definition", None)

    def chapter_lines(self, filename: str) -> list[str]:
        return self._lines[filename]

    def chapter_sections(self, filename: str) -> list[Section]:
        return self._sections[filename]
