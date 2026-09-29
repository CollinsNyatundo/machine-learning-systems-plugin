# Machine Learning Systems Reference Plugin

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](LICENSE)
[![CI](https://github.com/CollinsNyatundo/machine-learning-systems-plugin/actions/workflows/ci.yml/badge.svg)](https://github.com/CollinsNyatundo/machine-learning-systems-plugin/actions/workflows/ci.yml)

A searchable study and reference package derived from Vijay Janapa Reddi's open textbook, [Machine Learning Systems](https://mlsysbook.ai/). It exposes the material as Markdown and through a small FastMCP server.

This repository is an independently organized derivative reference. It is not the original textbook, an official Harvard project, or an operational MLOps platform.

## Contents

- 44 chapter and appendix files across two volumes (Volume 2 has no Chapter 4 in this collection)
- Formal definitions, worked examples, checkpoints, principles, war stories and reference workloads, indexed from the chapter headings
- A formulas-and-constants cheatsheet
- Generated `glossary.md` and `patterns.md` catalogs
- FastMCP tools, resources and prompts for BM25-ranked search and retrieval

Live counts are available from the `ml-systems://index` resource.

## Quick start

Requires Python 3.12 or newer.

```bash
git clone https://github.com/CollinsNyatundo/machine-learning-systems-plugin.git
cd machine-learning-systems-plugin
python -m venv .venv
.venv/bin/pip install -r requirements.txt      # Windows: .venv\Scripts\pip
.venv/bin/fastmcp run mcp_server.py:mcp        # stdio; add --transport http for port 8000
```

To register the server with your AI clients in one step:

```bash
python scripts/install.py --dry-run    # preview
python scripts/install.py              # Claude Code, Claude Desktop, Cursor, Gemini CLI, Antigravity (those detected)
```

The installer backs up each config it edits and changes only its own `ml-systems` entry. See [INTEGRATIONS.md](INTEGRATIONS.md) for manual configuration and security notes. Set `ML_SYSTEMS_DIR` to use a `skills/machine-learning-systems` directory elsewhere.

## MCP surface

| Type | Name | Purpose |
|---|---|---|
| Tool | `search_chapters` | BM25-ranked search; compact snippets with file and heading |
| Tool | `get_definition` | Formal definition by term (exact, partial, then ranked) |
| Tool | `get_artifact` | Napkin math, checkpoints, principles, etc. by number or title |
| Tool | `list_artifacts` | Paged artifact titles, filterable by type and volume |
| Tool | `get_chapter` | Chapter text in pages, or one section; first page includes an outline |
| Tool | `get_formula` | Formulas and constants from the cheatsheet |
| Tool | `get_cheatsheet_section` | A cheatsheet section by heading, or the list of headings |
| Resource | `ml-systems://index` | Chapter metadata and live counts |
| Resource | `ml-systems://glossary` | Generated glossary |
| Resource | `ml-systems://patterns` | Compact artifact catalog (titles) |
| Resource | `ml-systems://cheatsheet` | Quick reference |
| Resource | `ml-systems://skill` | Plugin manifest (`SKILL.md`) |
| Prompt | `study_chapter`, `compare_volumes`, `design_review`, `exam_prep` | Structured study and review prompts |

Tools return compact structured results by default and accept `verbose` (or paging arguments) for more. Every tool is read-only.

## Content policy and maintenance

Chapters are the single source of truth. `glossary.md` and `patterns.md` are generated.

- Math uses `\( ... \)` (inline) and `\[ ... \]` (display) only. Bare `$` and `$$` are not allowed; literal dollar amounts are written `\$`.
- After editing chapters: `python scripts/fix_content.py` (normalizes delimiters and strips extraction artifacts), then `python scripts/build_indexes.py`, then `python scripts/validate_content.py`.

Known gaps in the extracted text: many Volume 1 and Volume 2 passages still contain raw Unicode math glyphs (for example `𝜏 opt`) instead of LaTeX; `v2_ch03.md` is titled Chapter 3 but its headings are numbered 4.x; chapter files begin with an extracted table of contents, and 21 of them also carry a verbatim "Full Slice Content" extraction after the condensed text, so some topics appear twice in search results. The original PDFs, when you have them, belong in `docs/books/` (ignored by git).

## Verify

```bash
pip install -r requirements-dev.txt
pytest -q
python scripts/validate_content.py
python scripts/build_indexes.py --check
```

## Provenance

The chapter Markdown was extracted and reorganized from the CC BY-NC-SA 4.0 source material. Repository-specific changes include the directory layout, indexes, search server, metadata, and tests. Corrections to the textbook itself should be reported to the [upstream project](https://github.com/harvard-edge/cs249r_book).

## License

The source and this derivative are licensed under [CC BY-NC-SA 4.0](LICENSE). You must provide attribution, restrict use to non-commercial purposes, and distribute adaptations under the same license.
