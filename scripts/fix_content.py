#!/usr/bin/env python3
"""Normalize chapter Markdown to the plugin's math/markup policy.

Policy: inline math is ``\\( ... \\)``, display math is ``\\[ ... \\]``.
Bare ``$`` / ``$$`` delimiters are not allowed; literal dollar signs (prices)
are written ``\\$``.

Also strips extraction artifacts (image stubs, pipeline headings, doubled
separators). Idempotent: running it twice changes nothing the second time.

Usage:
    python scripts/fix_content.py            # rewrite files in place
    python scripts/fix_content.py --check    # exit 1 if any file would change
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CHAPTERS_DIR = Path(__file__).resolve().parents[1] / "skills" / "machine-learning-systems" / "chapters"

IMAGE_STUB = re.compile(r"^[ \t]*<!--\s*image\s*-->[ \t]*\n?", re.MULTILINE)
INLINE_IMAGE_STUB = re.compile(r"[ \t]*<!--\s*image\s*-->[ \t]*")
PIPELINE_HEADING = re.compile(r"^## Section-by-Section Preserve-and-Extend[ \t]*\n(?:[ \t]*\n)*", re.MULTILINE)
DOUBLE_RULE = re.compile(r"(?m)^---[ \t]*\n(?:[ \t]*\n)+---[ \t]*$")
BROKEN_DISPLAY = re.compile(r"^\\\[ \$\$(?P<body>.*)\$\$ \\$")

# A `$...$` inline pair: opening `$` not escaped/followed by space, closing `$`
# not preceded by space and not followed by a digit (which would be a price).
INLINE_PAIR = re.compile(r"(?<![\\$])\$(?![\s$])(?P<body>[^$\n]{1,300}?)(?<![\s\\])\$(?![\d$])")
WRAPPED_INLINE = re.compile(r"\\\( \$(?P<body>[^$\n]+?)\$ \\\)")  # `\( $x$ \)` left by a partial conversion
DISPLAY_PAIR =re.compile(r"(?<!\\)\$\$(?P<body>.+?)(?<!\\)\$\$")
SKIP_SPANS = re.compile(r"\\\(.*?\\\)|`[^`\n]*`")


def _plain_math(match: re.Match) -> str:
    body = match.group("body").strip()
    return body.replace(r"\times", "×").replace("{", "").replace("}", "")


def _convert_line(line: str) -> str:
    """Convert `$`/`$$` math on one non-display, non-code line and escape prices."""
    line = DISPLAY_PAIR.sub(lambda m: r"\[" + m.group("body").strip() + r"\]", line)
    line = WRAPPED_INLINE.sub(lambda m: r"\(" + m.group("body").strip() + r"\)", line)

    out: list[str] = []
    pos = 0
    for span in SKIP_SPANS.finditer(line):
        out.append(_convert_text(line[pos:span.start()]))
        out.append(span.group(0))
        pos = span.end()
    out.append(_convert_text(line[pos:]))
    return "".join(out)


def _convert_text(text: str) -> str:
    text = INLINE_PAIR.sub(lambda m: r"\(" + m.group("body").strip() + r"\)", text)
    return re.sub(r"(?<!\\)\$", r"\\$", text)


def fix_text(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = PIPELINE_HEADING.sub("", text)
    text = IMAGE_STUB.sub("", text)
    text = INLINE_IMAGE_STUB.sub(" ", text)

    lines = text.split("\n")
    out: list[str] = []
    in_fence = False
    in_display = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            # code listings are literal text: LaTeX residue becomes plain characters
            out.append(INLINE_PAIR.sub(_plain_math, line))
            continue

        broken = BROKEN_DISPLAY.match(line)
        if broken:
            out.append(r"\[" + broken.group("body").strip() + r"\]")
            continue

        if in_display and (not stripped or stripped.startswith("#")):
            in_display = False  # display math never spans a blank line/heading; recover from unbalanced \[

        if in_display:
            body = line.replace("$$", "")
            if r"\]" in body:
                in_display = False
            out.append(body)
            continue

        if "$$" in line and len(re.findall(r"(?<!\\)\$\$", line)) == 1:
            # multi-line `$$` block opens here (or closes without opener)
            head, _, tail = line.partition("$$")
            out.append(head + r"\[" + tail)
            in_display = r"\]" not in tail
            continue

        if stripped.startswith(r"\[") and r"\]" not in line:
            in_display = True
            out.append(line)
            continue

        out.append(_convert_line(line))

    text = "\n".join(out)
    text = DOUBLE_RULE.sub("---", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="report files that would change; do not write")
    parser.add_argument("--dir", type=Path, default=CHAPTERS_DIR)
    args = parser.parse_args()

    changed = 0
    for path in sorted(args.dir.glob("*.md")):
        if path.name == "SKILL.md":
            continue
        original = path.read_text(encoding="utf-8")
        fixed = fix_text(original)
        if fixed != original.replace("\r\n", "\n"):
            changed += 1
            print(f"{'would change' if args.check else 'fixed'}: {path.name}")
            if not args.check:
                path.write_text(fixed, encoding="utf-8", newline="\n")
    print(f"{changed} file(s) {'need changes' if args.check else 'changed'}")
    return 1 if (args.check and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
