# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A searchable reference derived from the CC BY-NC-SA 4.0 textbook *Machine Learning Systems* (Vijay Janapa Reddi): Markdown content plus a small FastMCP server. It is also deployed as a global Antigravity/Gemini plugin at `~/.gemini/config/plugins/machine-learning-systems` (a separate git clone; do not edit it from here, users `git pull`). Textbook errors belong upstream (`harvard-edge/cs249r_book`). Derivatives must keep the CC BY-NC-SA 4.0 license.

## Environment and commands

Python 3.12+ in a repo-local venv. Never install packages globally.

```bash
uv venv --python 3.12 .venv
uv pip install --python .venv/Scripts/python.exe -r requirements-dev.txt   # fastmcp==2.14.7 is pinned
.venv/Scripts/python.exe -m pytest -q                       # all tests (CI: 3.12/3.13, Ubuntu + Windows)
.venv/Scripts/python.exe -m pytest -q tests/test_mcp_server.py::test_get_definition_exact   # one test
.venv/Scripts/python.exe scripts/validate_content.py        # content policy; must print "0 issue(s)"
.venv/Scripts/python.exe scripts/build_indexes.py --check   # glossary/patterns up to date
.venv/Scripts/python.exe scripts/install.py --dry-run       # preview MCP client registration
.venv/Scripts/fastmcp run mcp_server.py:mcp                 # stdio server
```

## Architecture

`skills/machine-learning-systems/chapters/*.md` (44 files: `ch*`/`app*` = Vol 1, `v2_*` = Vol 2) is the single source of truth. Everything else derives from it:

- `mlsys_index.py`: `Corpus` parses chapters once into an in-memory SQLite database (FTS5 + BM25). Chapters are split at headings (code fences respected). "Artifacts" (Definition, Napkin Math, Systems Perspective, Checkpoint, Example, Lighthouse, War Story, Principle) are recognised from headings like `## Napkin Math 18.2: Title`. The cheatsheet is indexed by section. `locate_skill_dir()` honours `ML_SYSTEMS_DIR`. Files that resolve outside `chapters/` (symlink escape) are not indexed.
- `mcp_server.py`: thin tools/resources/prompts over a lazily built shared `Corpus` (`get_corpus()`; tests swap it with `reset_corpus()`). Tools validate input, raise `ToolError` on bad arguments, return compact dicts, page long text, and are read-only. Chapter access is a whitelist lookup of indexed file names, so there is no path parsing to escape. FastMCP 2.14 masks prompt exceptions, so prompts return an explanatory string for bad input.
- `skills/machine-learning-systems/glossary.md` and `patterns.md` are **generated** by `scripts/build_indexes.py` from the chapters. Never hand-edit them; a test fails if they are stale. `cheatsheet.md` and `SKILL.md` are hand-written (SKILL.md links must be relative and are validated).
- `plugin.json` lists the server's tools/resources/prompts; a test asserts it matches the live server, so update both together.

## Content policy

Math is `\( ... \)` inline and `\[ ... \]` display only. Bare `$`/`$$` are forbidden outside code fences; literal prices are `\$`. Workflow after editing chapters: `scripts/fix_content.py` (idempotent normalizer), then `scripts/build_indexes.py`, then `scripts/validate_content.py`. `tests/test_content.py` enforces all of it.

Known, documented gaps (not bugs to silently "fix"): raw Unicode math glyphs remain in many passages; Vol 2 has no chapter 4 and `v2_ch03.md` uses 4.x numbering; 21 chapters include a verbatim "Full Slice Content" section after the condensed text; `docs/books/` PDFs are git-ignored originals.
