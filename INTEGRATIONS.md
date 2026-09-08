# Machine Learning Systems Plugin — Integration Guide

This plugin provides the complete "Machine Learning Systems" textbook (Vol 1 & 2) as 44 chapter files + 4 top-level references. Here's how to integrate it with every major AI coding assistant and platform.

---

## 🔌 Universal Integration: MCP (Model Context Protocol)

**MCP is the single best integration path** — it works with **all** platforms below. Build one MCP server, use everywhere.

### Quick Start (Any MCP Client)

```bash
# 1. Install FastMCP
pip install fastmcp

# 2. Create the MCP server (see mcp_server.py below)
# 3. Test locally
fastmcp run mcp_server.py:mcp --transport http --port 8000

# 4. Install into your client
fastmcp install claude-code mcp_server.py
fastmcp install cursor mcp_server.py
fastmcp install claude-desktop mcp_server.py
```

---

## 📋 Platform-Specific Integration

### 1. Hermes Agent (Native MCP Client) ⭐ Native
**Best for**: Always-on agents, background tasks, Hermes TUI/CLI

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  ml-systems:
    command: "uvx"
    args: ["fastmcp", "run", "/path/to/mcp_server.py:mcp"]
    # OR HTTP:
    # url: "http://localhost:8000/mcp"
    timeout: 180
```

Tools auto-discovered: `mcp_ml_systems_search_chapters`, `mcp_ml_systems_get_definition`, etc.

### 2. Claude Code ⭐ Recommended
**Best for**: Local development, PR reviews, refactoring

```bash
# One-time setup
fastmcp install claude-code /path/to/mcp_server.py

# Or manual config (~/.claude/mcp_config.json):
{
  "mcpServers": {
    "ml-systems": {
      "command": "fastmcp",
      "args": ["run", "/path/to/mcp_server.py:mcp"]
    }
  }
}
```

Then in Claude Code: `/mcp` to list tools, use `mcp__ml-systems__search_chapters`

### 3. Cursor ⭐ Recommended
**Best for**: IDE-integrated coding, inline completions

```bash
fastmcp install cursor /path/to/mcp_server.py -e .
```

Available in Cursor Chat (`@ml-systems`) and Cmd+K with `mcp_ml_systems_*` tools.

### 4. Gemini CLI ⭐ Primary Target
**Best for**: Google ecosystem, large context windows

```bash
# Native plugin (current)
cp -r skills/machine-learning-systems ~/.gemini/config/plugins/

# Or via MCP (for tool-use):
# ~/.gemini/config.yaml
mcp_servers:
  ml-systems:
    command: "fastmcp"
    args: ["run", "/path/to/mcp_server.py:mcp"]
```

### 5. OpenCode
**Best for**: Open-source alternative, MCP-first

```json
// ~/.config/opencode/mcp.json
{
  "mcpServers": {
    "ml-systems": {
      "command": "fastmcp",
      "args": ["run", "/path/to/mcp_server.py:mcp"]
    }
  }
}
```

### 6. Continue.dev
**Best for**: VS Code/JetBrains IDE integration

```json
// ~/.continue/config.json
{
  "mcpServers": {
    "ml-systems": {
      "command": "fastmcp",
      "args": ["run", "/path/to/mcp_server.py:mcp"]
    }
  }
}
```

### 7. Aider
**Best for**: Terminal-based AI pair programming

```bash
# Aider reads .aider.mcp.json or env
export AIDER_MCP_ML_SYSTEMS="fastmcp run /path/to/mcp_server.py:mcp"
```

### 8. Sourcegraph Cody
**Best for**: Enterprise code search + context

```json
// ~/.cody/mcp.json
{
  "mcpServers": {
    "ml-systems": {
      "command": "fastmcp",
      "args": ["run", "/path/to/mcp_server.py:mcp"]
    }
  }
}
```

### 9. Neovim (via `mcphub.nvim` or `mcp.nvim`)
**Best for**: Terminal-first editing

```lua
-- lazy.nvim
{
  "ravitemer/mcphub.nvim",
  config = function()
    require("mcphub").setup({
      servers = {
        ml_systems = {
          cmd = "fastmcp",
          args = {"run", "/path/to/mcp_server.py:mcp"},
        }
      }
    })
  end
}
```

### 10. Zed Editor
**Best for**: High-performance collaborative editing

```json
// ~/.config/zed/settings.json
{
  "mcp_servers": {
    "ml-systems": {
      "command": "fastmcp",
      "args": ["run", "/path/to/mcp_server.py:mcp"]
    }
  }
}
```

### 11. GitHub Copilot (VS Code)
**Best for**: GitHub-integrated workflows

```json
// .vscode/mcp.json (workspace) or ~/.vscode/mcp.json (user)
{
  "servers": {
    "ml-systems": {
      "command": "fastmcp",
      "args": ["run", "/path/to/mcp_server.py:mcp"]
    }
  }
}
```

### 12. Local Models (Ollama / LM Studio / vLLM)
**Best for**: Offline/private development

Any model with **tool-use support** can call the MCP server via HTTP:

```bash
# Start server
fastmcp run mcp_server.py:mcp --transport http --port 8000

# In your model's tool config:
{
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "search_chapters",
        "description": "Search ML Systems textbook chapters",
        "parameters": { ... }
      }
    }
  ]
}
```

---

## 🏗 The MCP Server Implementation

Create `/path/to/mcp_server.py`:

```python
#!/usr/bin/env python3
"""
Machine Learning Systems — MCP Server
Exposes the reference corpus (44 chapter files, 111 definitions, 816 indexed artifacts)
as MCP tools, resources, and prompts.
"""

from pathlib import Path
import json
from fastmcp import FastMCP

# ── Configuration ──────────────────────────────────────────────
CHAPTERS_DIR = Path(__file__).parent / "chapters"  # Adjust to plugin path
# CHAPTERS_DIR = Path.home() / ".gemini/config/plugins/machine-learning-systems/skills/machine-learning-systems/chapters"

mcp = FastMCP("Machine Learning Systems")

# ── Load Chapter Index ────────────────────────────────────────
@mcp.resource("ml-systems://index")
def chapter_index() -> str:
    """Complete chapter listing with metadata."""
    chapters = []
    for md in sorted(CHAPTERS_DIR.glob("*.md")):
        if md.name in {"SKILL.md", "glossary.md", "patterns.md", "cheatsheet.md"}:
            continue
        text = md.read_text()
        title = text.split("\n")[0].replace("# ", "") if text.startswith("# ") else md.stem
        vol = "Vol 2" if md.name.startswith("v2_") else "Vol 1"
        chapters.append({
            "file": md.name,
            "title": title,
            "volume": vol,
            "size_kb": md.stat().st_size // 1024
        })
    return json.dumps({"chapters": chapters, "total": len(chapters)}, indent=2)

@mcp.resource("ml-systems://glossary")
def glossary() -> str:
    """All 111 definitions."""
    return (CHAPTERS_DIR / "glossary.md").read_text()

@mcp.resource("ml-systems://patterns")
def patterns() -> str:
    """All 816 indexed artifacts across 8 categories."""
    return (CHAPTERS_DIR / "patterns.md").read_text()

@mcp.resource("ml-systems://cheatsheet")
def cheatsheet() -> str:
    """Key formulas, numbers, rules of thumb."""
    return (CHAPTERS_DIR / "cheatsheet.md").read_text()

# ── Tools ─────────────────────────────────────────────────────

@mcp.tool
def search_chapters(query: str, volume: str = "both", limit: int = 10) -> str:
    """Search chapter content by keyword. Returns matching sections with context."""
    results = []
    for md in sorted(CHAPTERS_DIR.glob("*.md")):
        if md.name in {"SKILL.md", "glossary.md", "patterns.md", "cheatsheet.md"}:
            continue
        if volume != "both":
            vol_prefix = "v2_" if volume == "2" else "ch"
            if not md.name.startswith(vol_prefix) and not (volume == "1" and md.name.startswith("app")):
                continue
        
        text = md.read_text()
        lines = text.split("\n")
        for i, line in enumerate(lines):
            if query.lower() in line.lower():
                context = "\n".join(lines[max(0,i-2):i+3])
                results.append({
                    "file": md.name,
                    "line": i + 1,
                    "context": context[:500]
                })
                if len(results) >= limit:
                    break
        if len(results) >= limit:
            break
    return json.dumps({"query": query, "results": results}, indent=2)

@mcp.tool
def get_definition(term: str) -> str:
    """Get a glossary definition by term (case-insensitive, fuzzy match)."""
    glossary_text = (CHAPTERS_DIR / "glossary.md").read_text()
    entries = glossary_text.split("\n---\n")
    term_lower = term.lower()
    for entry in entries:
        if f"### {term}" in entry or term_lower in entry.lower().split("### ")[1].split("\n")[0].lower():
            return entry.strip()
    return json.dumps({"error": f"Definition not found: {term}", "suggestion": "Use search_chapters for broader search"})

@mcp.tool
def get_artifact(artifact_type: str, identifier: str) -> str:
    """Get a specific artifact from patterns.md (napkin_math, checkpoint, systems_perspective, principle, war_story, lighthouse, example, definition)."""
    patterns_text = (CHAPTERS_DIR / "patterns.md").read_text()
    # Simple search by type and identifier
    sections = patterns_text.split("\n---\n")
    for section in sections:
        if artifact_type.lower().replace("_", " ") in section.lower() and identifier.lower() in section.lower():
            return section.strip()
    return json.dumps({"error": f"Artifact not found: {artifact_type} {identifier}"})

@mcp.tool
def get_chapter(file: str) -> str:
    """Get full chapter content by filename (e.g., 'ch04.md', 'v2_ch06.md')."""
    path = CHAPTERS_DIR / file
    if not path.exists():
        return json.dumps({"error": f"Chapter not found: {file}"})
    return path.read_text()

@mcp.tool
def get_formula(formula_name: str) -> str:
    """Get a specific formula from cheatsheet.md."""
    cheatsheet = (CHAPTERS_DIR / "cheatsheet.md").read_text()
    if formula_name.lower() in cheatsheet.lower():
        # Extract relevant table row
        lines = cheatsheet.split("\n")
        for i, line in enumerate(lines):
            if formula_name.lower() in line.lower():
                return "\n".join(lines[max(0,i-1):i+2])
    return json.dumps({"error": f"Formula not found: {formula_name}"})

@mcp.tool
def list_artifacts(artifact_type: str = "all", volume: str = "both") -> str:
    """List all artifacts of a given type, optionally filtered by volume."""
    patterns_text = (CHAPTERS_DIR / "patterns.md").read_text()
    sections = patterns_text.split("\n---\n")
    results = []
    for section in sections:
        if artifact_type != "all" and artifact_type.lower().replace("_", " ") not in section.lower():
            continue
        if volume != "both":
            vol_marker = "Vol 2" if volume == "2" else "Vol 1"
            if vol_marker not in section:
                continue
        # Extract the artifact heading
        lines = section.strip().split("\n")
        if lines:
            results.append(lines[0].replace("### ", "").strip())
            if len(results) >= 100:
                break
    return json.dumps({"type": artifact_type, "volume": volume, "count": len(results), "artifacts": results})

# ── Prompts ───────────────────────────────────────────────────

@mcp.prompt
def study_chapter(chapter: str) -> str:
    """Generate a structured study prompt for a chapter."""
    return f"""You are studying Chapter: {chapter} from "Machine Learning Systems" by Vijay Janapa Reddi.

Please provide:
1. **Core Concepts** — 3-5 key takeaways
2. **Quantitative Invariants** — Formulas, laws, ridge points, MFU calculations
3. **Systems Perspectives** — Architectural insights, trade-offs
4. **Napkin Math** — Worked examples with numbers
5. **Checkpoints** — Self-check questions from the chapter
6. **Cross-References** — How this connects to other chapters (Vol 1 ↔ Vol 2)

Format as a study guide with clear sections. Use the chapter content as source."""

@mcp.prompt
def compare_volumes(topic: str) -> str:
    """Compare how a topic is treated in Vol 1 (single-machine) vs Vol 2 (fleet scale)."""
    return f"""Compare the treatment of "{topic}" across both volumes of "Machine Learning Systems":

**Vol 1 (Foundations)** — Single-machine perspective
**Vol 2 (Scale)** — Fleet/distributed perspective

For each volume:
- Key definitions and formulas
- Systems perspectives / architectural insights
- Quantitative constraints (Iron Law terms: D_vol, BW, R_peak, L_lat, O)
- Napkin math examples
- How the scaling changes the problem

Synthesize: What fundamentally changes at scale? What invariants remain?"""

@mcp.prompt
def design_review(system_description: str) -> str:
    """Use ML Systems principles to review a system design."""
    return f"""You are a Machine Learning Systems expert (per Vijay Janapa Reddi's textbook). Review this system design:

{system_description}

Apply the **D·A·M Taxonomy** (Data, Algorithm, Machine) and **Iron Law**:
T = D_vol/BW + O/(R_peak·η_hw) + L_lat

Check for:
1. **Data axis** — D_vol, BW, data gravity, training-serving skew
2. **Algorithm axis** — O (ops), arithmetic intensity, critical batch size
3. **Machine axis** — R_peak, ridge point, memory wall, MFU target

Identify:
- Bottlenecks (which axis dominates?)
- Scaling limits (bisection BW, MFU ceiling, checkpoint overhead)
- Quantitative risks (MTBF, Young-Daly, ridge point)
- Mitigations (overlap, compression, sparsity, topology)

Provide specific numbers where possible."""

# ── Run ───────────────────────────────────────────────────────
if __name__ == "__main__":
    mcp.run()
```

---

## 🚀 Quick Install Commands

```bash
# Clone the plugin
git clone https://github.com/CollinsNyatundo/machine-learning-systems-plugin.git
cd machine-learning-systems-plugin

# Create MCP server (copy the Python code above to mcp_server.py)
# Adjust CHAPTERS_DIR path in the script

# Test
pip install fastmcp
fastmcp run mcp_server.py:mcp --transport http --port 8000

# Install everywhere
fastmcp install claude-code mcp_server.py
fastmcp install cursor mcp_server.py
fastmcp install claude-desktop mcp_server.py

# Hermes (add to ~/.hermes/config.yaml)
# mcp_servers:
#   ml-systems:
#     url: "http://localhost:8000/mcp"
```

---

## 📊 Tool Reference

| Tool | Description | Returns |
|------|-------------|---------|
| `search_chapters(query, volume, limit)` | Full-text search across chapters | JSON with file, line, context |
| `get_definition(term)` | Glossary lookup (111 terms) | Full definition entry |
| `get_artifact(type, identifier)` | Patterns.md artifact | Full artifact entry |
| `get_chapter(file)` | Complete chapter text | Full markdown |
| `get_formula(name)` | Cheatsheet formula | Formula + context |
| `list_artifacts(type, volume)` | Catalog of artifacts | JSON list |

| Resource | URI | Content |
|----------|-----|---------|
| Chapter Index | `ml-systems://index` | All 44 chapters metadata |
| Glossary | `ml-systems://glossary` | 111 definitions |
| Patterns | `ml-systems://patterns` | 816 indexed artifacts |
| Cheatsheet | `ml-systems://cheatsheet` | Formulas, rules |

| Prompt | Use Case |
|--------|----------|
| `study_chapter(chapter)` | Structured study guide |
| `compare_volumes(topic)` | Vol 1 vs Vol 2 analysis |
| `design_review(description)` | D·A·M + Iron Law review |

---

## 🔒 Security Notes

- **No credentials needed** — plugin is read-only reference
- **Local filesystem only** — MCP server reads plugin directory
- **No network calls** — unless you deploy HTTP endpoint
- **Sand boxed** — each client runs server in isolated env

---

## 🎯 Recommended Setup by Use Case

| Use Case | Best Integration |
|----------|------------------|
| **Daily coding + ML sys questions** | Hermes (native) + Cursor (IDE) |
| **Code review / PR analysis** | Claude Code |
| **Research / deep study** | Gemini CLI (large context) + prompts |
| **Offline / air-gapped** | Local model + HTTP MCP server |
| **Team sharing** | HTTP MCP server + Cursor/Claude Code |
| **CI/CD integration** | `design_review` prompt in pipeline |

---

## 📚 Source Attribution

The reference content is adapted from **"Machine Learning Systems"** by **Professor Vijay Janapa Reddi** (Harvard SEAS), course **CS 249r**, at **[mlsysbook.ai](https://mlsysbook.ai/)**. This redistributed/adapted package, including its plugin and MCP integration, is licensed under CC BY-NC-SA 4.0; third-party dependencies retain their own licenses.
