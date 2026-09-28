#!/usr/bin/env python3
"""Regenerate glossary.md and patterns.md from the chapters.

Both files are derived data: never edit them by hand. Run after changing any
chapter, then commit the result.

Usage:
    python scripts/build_indexes.py           # rewrite the two files
    python scripts/build_indexes.py --check   # exit 1 if they are out of date
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mlsys_index import KIND_LABELS, Corpus, summarize  # noqa: E402

KIND_HEADINGS = {
    "napkin_math": "Napkin Math (Worked Examples)",
    "checkpoint": "Checkpoints (Self-Check Questions)",
    "systems_perspective": "Systems Perspectives (Architectural Insights)",
    "principle": "Principles (Invariants and Laws)",
    "war_story": "War Stories (Production Failures)",
    "lighthouse": "Lighthouses (Reference Workloads)",
    "example": "Examples (Applied Cases)",
    "definition": "Definitions",
}
GLOSSARY_SUMMARY_CHARS = 500
PATTERN_SUMMARY_CHARS = 200


def _initial(term: str) -> str:
    ch = term.strip()[:1].upper()
    return ch if ch.isalpha() else "#"


def build_glossary(corpus: Corpus) -> str:
    rows = sorted(corpus.definitions(), key=lambda r: (r["title"].lower(), r["volume"]))
    out = [
        "# Glossary — Machine Learning Systems",
        "",
        f"> Generated from the formal definitions in {len(corpus.chapters)} chapters ({len(rows)} entries), "
        "sorted alphabetically. Do not edit by hand: run `python scripts/build_indexes.py`.",
        "",
        "Entries are excerpts. Use the `get_definition` tool or open the source chapter for the full text.",
        "",
    ]
    letter = None
    for r in rows:
        if _initial(r["title"]) != letter:
            letter = _initial(r["title"])
            out += [f"## {letter}", ""]
        out += [
            f"### {r['title']}",
            "",
            f"**Definition {r['num']}** (Vol {r['volume']}) · [{r['file']}](chapters/{r['file']}) · {r['chapter']}",
            "",
            summarize(r["body"], GLOSSARY_SUMMARY_CHARS),
            "",
        ]
    return "\n".join(out).rstrip() + "\n"


def build_patterns(corpus: Corpus) -> str:
    rows = corpus.artifact_rows(None, None)
    out = [
        "# Patterns & Principles — Machine Learning Systems",
        "",
        f"> Generated catalog of {len(rows)} indexed artifacts across {len(corpus.chapters)} chapters. "
        "Do not edit by hand: run `python scripts/build_indexes.py`.",
        "",
        "Each entry is a short excerpt. Use `get_artifact` or open the source chapter for the full text.",
        "",
    ]
    for kind in KIND_LABELS:
        group = [r for r in rows if r["kind"] == kind]
        if not group:
            continue
        out += [f"## {KIND_HEADINGS[kind]}", "", f"*{len(group)} entries, in reading order*", ""]
        for r in group:
            label = f"{KIND_LABELS[kind]} {r['num']}".strip()
            out += [
                f"### {label}: {r['title']}",
                "",
                f"[{r['file']}](chapters/{r['file']}) · Vol {r['volume']} · {r['chapter']}",
                "",
                summarize(r["body"], PATTERN_SUMMARY_CHARS),
                "",
            ]
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="fail if generated files differ from disk")
    args = parser.parse_args()

    corpus = Corpus()
    outputs = {"glossary.md": build_glossary(corpus), "patterns.md": build_patterns(corpus)}
    stale = []
    for name, text in outputs.items():
        path = corpus.skill_dir / name
        current = path.read_text(encoding="utf-8").replace("\r\n", "\n") if path.exists() else None
        if current != text:
            stale.append(name)
            if not args.check:
                path.write_text(text, encoding="utf-8", newline="\n")
    if args.check:
        print("out of date: " + ", ".join(stale) if stale else "generated files are up to date")
        return 1 if stale else 0
    print("wrote: " + ", ".join(stale) if stale else "no changes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
