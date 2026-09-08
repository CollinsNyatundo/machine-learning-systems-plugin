# Machine Learning Systems Reference Plugin

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](LICENSE)
[![CI](https://github.com/CollinsNyatundo/machine-learning-systems-plugin/actions/workflows/ci.yml/badge.svg)](https://github.com/CollinsNyatundo/machine-learning-systems-plugin/actions/workflows/ci.yml)

A searchable study and reference package derived from Vijay Janapa Reddi's open textbook, [Machine Learning Systems](https://mlsysbook.ai/). It exposes the material as Markdown and through a small FastMCP server.

This repository is an independently organized derivative reference. It is not the original textbook, an official Harvard project, or an operational MLOps platform.

## Contents

- 44 chapter and appendix files across two volumes
- 111 glossary entries
- 816 indexed learning artifacts
- A formulas-and-concepts cheatsheet
- FastMCP resources and tools for search and retrieval

## Run locally

```bash
git clone https://github.com/CollinsNyatundo/machine-learning-systems-plugin.git
cd machine-learning-systems-plugin
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python mcp_server.py
```

FastMCP can also install the server into supported clients:

```bash
fastmcp install claude-desktop mcp_server.py
fastmcp install cursor mcp_server.py
fastmcp install claude-code mcp_server.py
```

Client support and syntax change over time; consult the client's current documentation. See [INTEGRATIONS.md](INTEGRATIONS.md) for configuration examples. Its HTTP examples require authentication, transport security, and network hardening before exposure outside a trusted machine.

## MCP surface

| Type | Name | Purpose |
|---|---|---|
| Resource | `ml-systems://index` | Chapter metadata |
| Resource | `ml-systems://chapter/{id}` | Chapter text |
| Resource | `ml-systems://glossary` | Glossary |
| Resource | `ml-systems://patterns` | Indexed artifacts |
| Resource | `ml-systems://cheatsheet` | Quick reference |
| Tool | `search` | Search the reference corpus |
| Tool | `get_chapter` | Retrieve one chapter safely |
| Tool | `list_chapters` | List chapter metadata |
| Tool | `list_patterns` | Filter indexed artifacts |

## Verify

```bash
pip install -r requirements-dev.txt
pytest -q
python -m compileall -q mcp_server.py
```

## Provenance

The chapter Markdown was extracted and reorganized from the CC BY-NC-SA 4.0 source material. Repository-specific changes include the directory layout, indexes, search server, metadata, and tests. Corrections to the textbook itself should be reported to the [upstream project](https://github.com/harvard-edge/cs249r_book).

## License

The source and this derivative are licensed under [CC BY-NC-SA 4.0](LICENSE). You must provide attribution, restrict use to non-commercial purposes, and distribute adaptations under the same license.
