import json

import mcp_server


def test_get_chapter_rejects_parent_directory_escape():
    result = json.loads(mcp_server.get_chapter.fn("../README"))
    assert result["error"].startswith("Invalid chapter filename")


def test_get_chapter_rejects_symlink_escape(tmp_path, monkeypatch):
    chapters = tmp_path / "chapters"
    chapters.mkdir()
    outside = tmp_path / "private.md"
    outside.write_text("private", encoding="utf-8")
    (chapters / "escape.md").symlink_to(outside)
    monkeypatch.setattr(mcp_server, "CHAPTERS_DIR", chapters)

    result = json.loads(mcp_server.get_chapter.fn("escape.md"))
    assert result["error"].startswith("Chapter not found")


def test_chapter_index_does_not_disclose_absolute_paths():
    mcp_server._load_chapter_index.cache_clear()
    payload = json.loads(mcp_server.chapter_index.fn())
    chapters = payload["vol1"] + payload["vol2"]
    assert payload["total_chapters"] == 44
    assert all("path" not in chapter for chapter in chapters)


def test_patterns_parser_indexes_every_artifact_record():
    mcp_server._load_patterns_index.cache_clear()
    patterns = mcp_server._load_patterns_index()
    assert len(patterns) == 816
    assert all(item["name"] and item["source"] and item["chapter"] for item in patterns)
