#!/usr/bin/env python3
"""Register the ML Systems MCP server with your AI clients.

Standard library only. Writes a single `mcpServers` entry (default name
"ml-systems") into each client's JSON config, after saving a timestamped
backup. Other entries in those files are never modified or printed.

    python scripts/install.py --dry-run           # show what would change
    python scripts/install.py                     # configure every detected client
    python scripts/install.py --client cursor     # just one (repeatable)
    python scripts/install.py --uninstall         # remove the entry

Clients: claude-code, claude-desktop, cursor, gemini, antigravity.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SERVER = REPO / "mcp_server.py"


def _claude_desktop_config() -> Path:
    if sys.platform == "win32":
        return Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming")) / "Claude" / "claude_desktop_config.json"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    return Path.home() / ".config" / "Claude" / "claude_desktop_config.json"


# client -> JSON config file holding a top-level "mcpServers" object
JSON_CLIENTS: dict[str, Path] = {
    "claude-desktop": _claude_desktop_config(),
    "cursor": Path.home() / ".cursor" / "mcp.json",
    "gemini": Path.home() / ".gemini" / "settings.json",
    "antigravity": Path.home() / ".gemini" / "config" / "mcp_config.json",
}
ALL_CLIENTS = ["claude-code", *JSON_CLIENTS]


def server_python() -> str:
    """Interpreter to launch the server: the repo's .venv if present, else this one."""
    for rel in (".venv/Scripts/python.exe", ".venv/bin/python"):
        candidate = REPO / rel
        if candidate.exists():
            return str(candidate)
    return sys.executable


def has_fastmcp(python: str) -> bool:
    return subprocess.run([python, "-c", "import fastmcp"], capture_output=True).returncode == 0


def entry(python: str) -> dict:
    return {"command": python, "args": [str(SERVER)]}


def detected(client: str) -> bool:
    if client == "claude-code":
        return shutil.which("claude") is not None
    path = JSON_CLIENTS[client]
    return path.exists() or path.parent.exists()


def configure_json(client: str, name: str, python: str, dry_run: bool, uninstall: bool) -> str:
    path = JSON_CLIENTS[client]
    data: dict = {}
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8") or "{}")
        except json.JSONDecodeError as exc:
            return f"skipped: {path} is not valid JSON ({exc.msg}); fix it or edit by hand"
    servers = data.setdefault("mcpServers", {})
    if uninstall:
        if name not in servers:
            return f"nothing to remove in {path}"
        del servers[name]
    else:
        if servers.get(name) == entry(python):
            return f"already configured in {path}"
        servers[name] = entry(python)
    if dry_run:
        return f"would {'remove' if uninstall else 'write'} '{name}' in {path}"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        shutil.copy2(path, path.with_name(f"{path.name}.bak-{time.strftime('%Y%m%d-%H%M%S')}"))
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return f"{'removed' if uninstall else 'configured'} '{name}' in {path}"


def configure_claude_code(name: str, python: str, dry_run: bool, uninstall: bool) -> str:
    if uninstall:
        cmd = ["claude", "mcp", "remove", "--scope", "user", name]
    else:
        cmd = ["claude", "mcp", "add", "--scope", "user", name, "--", python, str(SERVER)]
    shown = " ".join(f'"{c}"' if " " in c else c for c in cmd)
    if dry_run:
        return f"would run: {shown}"
    if shutil.which("claude") is None:
        return f"claude CLI not found; run manually: {shown}"
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return f"failed ({(result.stderr or result.stdout).strip()[:200]}); run manually: {shown}"
    return f"{'removed' if uninstall else 'configured'} '{name}' via claude CLI"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--client", action="append", choices=ALL_CLIENTS, help="client to configure (repeatable); default: all detected")
    parser.add_argument("--name", default="ml-systems", help="server name in client configs")
    parser.add_argument("--dry-run", action="store_true", help="show changes without writing")
    parser.add_argument("--uninstall", action="store_true", help="remove the server entry")
    args = parser.parse_args()

    python = server_python()
    if not args.uninstall and not has_fastmcp(python):
        print(f"warning: {python} cannot import fastmcp. Create a venv and run: pip install -r requirements.txt")
    print(f"server: {python} {SERVER}")

    clients = args.client or [c for c in ALL_CLIENTS if detected(c)]
    if not clients:
        print("no supported clients detected; use --client to force one")
        return 1
    for client in clients:
        if client == "claude-code":
            message = configure_claude_code(args.name, python, args.dry_run, args.uninstall)
        else:
            message = configure_json(client, args.name, python, args.dry_run, args.uninstall)
        print(f"{client:15} {message}")
    if not args.dry_run and not args.uninstall:
        print("restart your client(s) to pick up the server")
    return 0


if __name__ == "__main__":
    sys.exit(main())
