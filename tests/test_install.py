import json

import pytest

import install


@pytest.fixture
def fake_clients(tmp_path, monkeypatch):
    paths = {
        "cursor": tmp_path / ".cursor" / "mcp.json",
        "gemini": tmp_path / ".gemini" / "settings.json",
    }
    monkeypatch.setattr(install, "JSON_CLIENTS", paths)
    return paths


PY = "/venv/bin/python"


def test_creates_config_with_only_our_entry(fake_clients):
    msg = install.configure_json("cursor", "ml-systems", PY, dry_run=False, uninstall=False)
    assert "configured" in msg
    data = json.loads(fake_clients["cursor"].read_text(encoding="utf-8"))
    assert data == {"mcpServers": {"ml-systems": {"command": PY, "args": [str(install.SERVER)]}}}


def test_preserves_other_settings_and_backs_up(fake_clients):
    path = fake_clients["gemini"]
    path.parent.mkdir(parents=True)
    original = {"theme": "dark", "mcpServers": {"other": {"command": "x", "env": {"TOKEN": "secret"}}}}
    path.write_text(json.dumps(original), encoding="utf-8")
    install.configure_json("gemini", "ml-systems", PY, dry_run=False, uninstall=False)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["theme"] == "dark" and data["mcpServers"]["other"] == original["mcpServers"]["other"]
    assert "ml-systems" in data["mcpServers"]
    backups = list(path.parent.glob("settings.json.bak-*"))
    assert len(backups) == 1 and json.loads(backups[0].read_text(encoding="utf-8")) == original


def test_dry_run_writes_nothing(fake_clients):
    msg = install.configure_json("cursor", "ml-systems", PY, dry_run=True, uninstall=False)
    assert msg.startswith("would") and not fake_clients["cursor"].exists()


def test_idempotent(fake_clients):
    install.configure_json("cursor", "ml-systems", PY, False, False)
    assert "already configured" in install.configure_json("cursor", "ml-systems", PY, False, False)
    assert len(list(fake_clients["cursor"].parent.glob("*.bak-*"))) == 0


def test_uninstall_removes_only_our_entry(fake_clients):
    path = fake_clients["cursor"]
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps({"mcpServers": {"keep": {"command": "k"}, "ml-systems": {"command": "m"}}}), encoding="utf-8")
    install.configure_json("cursor", "ml-systems", PY, False, uninstall=True)
    assert json.loads(path.read_text(encoding="utf-8"))["mcpServers"] == {"keep": {"command": "k"}}
    assert "nothing to remove" in install.configure_json("cursor", "ml-systems", PY, False, uninstall=True)


def test_invalid_json_is_left_untouched(fake_clients):
    path = fake_clients["cursor"]
    path.parent.mkdir(parents=True)
    path.write_text("{ not json", encoding="utf-8")
    assert "not valid JSON" in install.configure_json("cursor", "ml-systems", PY, False, False)
    assert path.read_text(encoding="utf-8") == "{ not json"


def test_claude_code_dry_run_shows_command():
    msg = install.configure_claude_code("ml-systems", PY, dry_run=True, uninstall=False)
    assert msg.startswith("would run: claude mcp add") and "mcp_server.py" in msg
