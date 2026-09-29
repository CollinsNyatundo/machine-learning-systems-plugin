# Client Integrations

The server (`mcp_server.py`) speaks MCP over stdio by default. It needs Python 3.12+ and the packages in `requirements.txt`, so create a virtual environment inside the clone first:

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt      # Windows: .venv\Scripts\pip
```

## One command

```bash
python scripts/install.py --dry-run     # show what would change
python scripts/install.py               # every detected client
python scripts/install.py --client cursor --client claude-code
python scripts/install.py --uninstall
```

The script uses the clone's `.venv` interpreter, saves a timestamped `.bak-*` copy of each config file it edits, and only adds or removes its own `ml-systems` entry. Supported clients: `claude-code` (via the `claude` CLI), `claude-desktop`, `cursor`, `gemini` and `antigravity`. Restart the client afterwards.

## Manual configuration

Every JSON-configured client takes the same entry under a top-level `mcpServers` object. Use absolute paths.

```json
{
  "mcpServers": {
    "ml-systems": {
      "command": "/path/to/machine-learning-systems-plugin/.venv/bin/python",
      "args": ["/path/to/machine-learning-systems-plugin/mcp_server.py"]
    }
  }
}
```

On Windows use `...\.venv\Scripts\python.exe`.

| Client | Config file |
|---|---|
| Claude Code | `claude mcp add --scope user ml-systems -- <python> <path>/mcp_server.py` |
| Claude Desktop | Windows `%APPDATA%\Claude\claude_desktop_config.json`, macOS `~/Library/Application Support/Claude/claude_desktop_config.json`, Linux `~/.config/Claude/claude_desktop_config.json` |
| Cursor | `~/.cursor/mcp.json` |
| Gemini CLI | `~/.gemini/settings.json` |
| Antigravity | `~/.gemini/config/mcp_config.json` |

For other MCP clients, use their documented stdio configuration with the same command and args. `fastmcp install <client> mcp_server.py` also works for the clients FastMCP supports; check `fastmcp install --help` for your version.

### Antigravity / Gemini plugin directory

Clone the whole repository (the server sits beside `skills/`, not inside it) to `~/.gemini/config/plugins/machine-learning-systems`. To update later: `git pull` inside that directory, then reinstall requirements if `requirements.txt` changed.

## Environment

| Variable | Purpose |
|---|---|
| `ML_SYSTEMS_DIR` | Path to a `skills/machine-learning-systems` directory (containing `chapters/`). Default: next to `mcp_server.py`. |

## HTTP transport

```bash
.venv/bin/fastmcp run mcp_server.py:mcp --transport http --port 8000
```

The HTTP server has no authentication. Bind it only to localhost, or put it behind an authenticating reverse proxy with TLS before exposing it to a network. stdio (the default) runs as a child process of the client with your user's permissions and is not a sandbox.

## Tool reference

| Tool | Arguments | Notes |
|---|---|---|
| `search_chapters` | `query`, `volume` (`1`/`2`/`both`), `limit` (1-25), `verbose` | BM25 ranking, AND then OR fallback |
| `get_definition` | `term`, `limit` (1-10), `verbose` | exact match returns full text |
| `get_artifact` | `artifact_type`, `identifier`, `verbose` | number like `18.2`, or title words |
| `list_artifacts` | `artifact_type`, `volume`, `limit` (1-200), `offset` | titles only |
| `get_chapter` | `file`, `section`, `offset`, `max_chars` (500-100000) | pages; `next_offset` continues |
| `get_formula` | `formula_name`, `limit` (1-5) | cheatsheet search |
| `get_cheatsheet_section` | `section` (`list` for headings) | |

Artifact types: `definition`, `napkin_math`, `systems_perspective`, `checkpoint`, `example`, `lighthouse`, `war_story`, `principle`.

Prompts: `study_chapter(chapter)`, `compare_volumes(topic)`, `design_review(system_description)`, `exam_prep(chapters)`.
