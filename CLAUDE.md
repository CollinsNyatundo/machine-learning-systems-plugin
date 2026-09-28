# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A searchable reference derived from the CC BY-NC-SA 4.0 textbook *Machine Learning Systems* (Vijay Janapa Reddi). It is content plus one small FastMCP server, not an MLOps platform. The content is extracted upstream material: report textbook errors upstream (`harvard-edge/cs249r_book`), not here. Derivative work must keep the CC BY-NC-SA 4.0 license.

## Commands

```bash
pip install -r requirements-dev.txt        # fastmcp==2.14.7, pytest==8.4.2
pytest -q                                  # full suite (CI: Python 3.11 and 3.12)
pytest -q tests/test_mcp_server.py::test_get_chapter_rejects_parent_directory_escape   # single test
python -m compileall -q mcp_server.py      # second CI check
fastmcp run mcp_server.py:mcp              # stdio
fastmcp run mcp_server.py:mcp --transport http   # HTTP, port 8000
```

`tests/conftest.py` puts the repo root on `sys.path`, so tests `import mcp_server` directly.

## Architecture

Everything served comes from `skills/machine-learning-systems/chapters/`, resolved once as `CHAPTERS_DIR` in `mcp_server.py` (relative to the file, with fallbacks to cwd and `~/.gemini/config/plugins/...`). Despite the name, that directory holds all content:

- `ch*.md`, `appA-E.md` are Vol 1. `v2_*.md` files are Vol 2. Volume is inferred from the `v2_` filename prefix.
- `glossary.md`, `patterns.md`, `cheatsheet.md`, `SKILL.md` are generated indexes/manifests living beside the chapters. `_load_chapter_index` explicitly skips these four names, so adding a new non-chapter `.md` there requires updating that exclusion set.

`mcp_server.py` (single file) has three layers:
1. **Loaders**: `@lru_cache`d parsers (`_load_chapter_index`, `_load_glossary_entries`, `_load_patterns_index`). Glossary and patterns are parsed from Markdown by splitting on `\n---\n` and reading `### ` headings plus `**Source:**` / `**Full heading:**` / `**Chapter:**` lines. Changing the format of `glossary.md` or `patterns.md` breaks these parsers. Because of `lru_cache`, tests that swap `CHAPTERS_DIR` must clear the caches.
2. **Resources**: `ml-systems://index|glossary|patterns|cheatsheet|skill`.
3. **Tools and prompts**: `search_chapters`, `get_definition`, `get_artifact`, `get_chapter`, `get_formula`, `list_artifacts`, `get_cheatsheet_section`. Prompts: `study_chapter`, `compare_volumes`, `design_review`, `exam_prep`.

`get_chapter` is the security-sensitive path: it rejects anything where `Path(file).name != file` or the suffix is not `.md`, then resolves and checks `is_relative_to(CHAPTERS_DIR)` (this also blocks symlink escape). The chapter index must not expose absolute paths. Existing tests cover both properties; keep them passing.

## Known inconsistencies

- `README.md` lists tool names (`search`, `list_chapters`, `list_patterns`) that do not exist. The code and `plugin.json` use the names above. Treat the code as authoritative.
- `plugin.json` is the plugin manifest (`"skills": "./skills/"`, MCP tool/resource/prompt lists). Update its lists when adding or renaming server tools, resources or prompts.
- `INTEGRATIONS.md` has per-client setup examples. Its HTTP examples need auth and transport hardening before exposure beyond localhost.

## Other

- `docs/books/` holds the source PDFs. `docs/plans/` and `docs/solutions/` record past extraction fixes (for example math-placeholder resolution) and are useful context when chapter Markdown looks corrupted.
