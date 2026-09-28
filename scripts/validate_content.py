#!/usr/bin/env python3
"""Validate the Markdown corpus against the plugin's content policy.

Checks (outside fenced code blocks unless noted):
  bare-dollar        unescaped ``$`` (math must use ``\\( \\)`` / ``\\[ \\]``; prices use ``\\$``)
  math-unbalanced    ``\\(``/``\\)`` or ``\\[``/``\\]`` counts differ within a file
  image-stub         leftover ``<!-- image -->``
  placeholder        ``[Formula not decoded]``
  pipeline-heading   ``Section-by-Section Preserve-and-Extend`` extraction heading
  table-separator    table header row not followed by a ``|---|`` row
  double-rule        two ``---`` rules separated only by blank lines
  broken-link        relative link in SKILL.md/glossary.md/patterns.md to a missing file
  skill-title        SKILL.md chapter link text differs from the chapter's H1

Usage: python scripts/validate_content.py [--skill-dir DIR]   (exit 1 on any issue)
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1] / "skills" / "machine-learning-systems"

BARE_DOLLAR = re.compile(r"(?<!\\)\$")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
TABLE_SEP = re.compile(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")
LINK = re.compile(r"\]\((?!https?:|#|mailto:)([^)\s]+)\)")
SKILL_CHAPTER_LINK = re.compile(r"\[(?P<text>[^\]]+)\]\((?P<path>chapters/[^)]+\.md)\)")


@dataclass(frozen=True)
class Issue:
    file: str
    line: int
    code: str
    message: str

    def __str__(self) -> str:
        return f"{self.file}:{self.line}: [{self.code}] {self.message}"


def _outside_fences(lines: list[str]):
    in_fence = False
    for no, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        yield no, line, in_fence


def validate_markdown(name: str, text: str) -> list[Issue]:
    issues: list[Issue] = []
    lines = text.split("\n")
    opens = closes = dopens = dcloses = 0
    for no, line, fenced in _outside_fences(lines):
        if "<!-- image -->" in line:
            issues.append(Issue(name, no, "image-stub", "leftover image stub"))
        if "Preserve-and-Extend" in line:
            issues.append(Issue(name, no, "pipeline-heading", "extraction pipeline heading"))
        if fenced:
            continue
        if "[Formula not decoded]" in line:
            issues.append(Issue(name, no, "placeholder", "[Formula not decoded]"))
        if BARE_DOLLAR.search(line):
            issues.append(Issue(name, no, "bare-dollar", line.strip()[:100]))
        opens += line.count(r"\(")
        closes += line.count(r"\)")
        dopens += line.count(r"\[")
        dcloses += line.count(r"\]")

    if opens != closes:
        issues.append(Issue(name, 0, "math-unbalanced", rf"\( count {opens} != \) count {closes}"))
    if dopens != dcloses:
        issues.append(Issue(name, 0, "math-unbalanced", rf"\[ count {dopens} != \] count {dcloses}"))

    fenced_flags = {no: fenced for no, _, fenced in _outside_fences(lines)}
    for i, line in enumerate(lines[:-1]):
        if fenced_flags.get(i + 1):
            continue
        if TABLE_ROW.match(line) and not TABLE_ROW.match(lines[i - 1] if i else "") and not TABLE_SEP.match(lines[i + 1]):
            issues.append(Issue(name, i + 1, "table-separator", "table header without separator row"))
    for m in re.finditer(r"(?m)^---[ \t]*\n(?:[ \t]*\n)+---[ \t]*$", text):
        issues.append(Issue(name, text.count("\n", 0, m.start()) + 1, "double-rule", "duplicate horizontal rule"))
    return issues


def validate_links(skill_dir: Path) -> list[Issue]:
    issues: list[Issue] = []
    for name in ("SKILL.md", "glossary.md", "patterns.md"):
        path = skill_dir / name
        if not path.exists():
            issues.append(Issue(name, 0, "broken-link", "file missing"))
            continue
        for no, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
            for m in LINK.finditer(line):
                target = m.group(1).split("#")[0]
                if target and not (skill_dir / target).exists():
                    issues.append(Issue(name, no, "broken-link", target))
    return issues


def validate_skill_titles(skill_dir: Path) -> list[Issue]:
    issues: list[Issue] = []
    skill = skill_dir / "SKILL.md"
    if not skill.exists():
        return issues
    for no, line in enumerate(skill.read_text(encoding="utf-8").split("\n"), 1):
        m = SKILL_CHAPTER_LINK.search(line)
        target = skill_dir / m.group("path") if m else None
        if not m or not target.exists() or not m.group("text").startswith(("Chapter ", "Appendix ")):
            continue
        h1 = next((l[2:].strip() for l in target.read_text(encoding="utf-8").split("\n") if l.startswith("# ")), "")
        first = re.split(r"\s+[—-]\s+", h1)[0]
        if not first.lower().startswith(m.group("text").lower()[:24]) and m.group("text").split(":")[0] not in h1:
            issues.append(Issue("SKILL.md", no, "skill-title", f"link text {m.group('text')!r} vs H1 {h1!r}"))
    return issues


def validate_all(skill_dir: Path = SKILL_DIR) -> list[Issue]:
    issues: list[Issue] = []
    files = sorted((skill_dir / "chapters").glob("*.md")) + [skill_dir / n for n in ("glossary.md", "patterns.md", "cheatsheet.md", "SKILL.md")]
    for path in files:
        if path.exists():
            issues += validate_markdown(path.name, path.read_text(encoding="utf-8"))
    issues += validate_links(skill_dir)
    issues += validate_skill_titles(skill_dir)
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--skill-dir", type=Path, default=SKILL_DIR)
    args = parser.parse_args()
    issues = validate_all(args.skill_dir)
    for issue in issues:
        print(issue)
    counts: dict[str, int] = {}
    for issue in issues:
        counts[issue.code] = counts.get(issue.code, 0) + 1
    print(f"{len(issues)} issue(s)" + (": " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())) if counts else ""))
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
