"""Behavioral tests for every MCP tool, resource and prompt."""

import json
import os

import pytest

import mcp_server
from mlsys_index import Corpus, CorpusError, locate_skill_dir, normalize_kind, normalize_volume, summarize

# ── security / path handling ───────────────────────────────────


@pytest.mark.parametrize("bad", ["../README.md", "..\\README.md", "ch01.md/../../x", "/etc/passwd", "ch99", "glossary", "SKILL"])
def test_get_chapter_rejects_paths_outside_the_chapter_list(call, bad):
    assert "Chapter not found" in call.tool_error("get_chapter", file=bad)


def test_get_chapter_rejects_empty_file(call):
    assert "non-empty" in call.tool_error("get_chapter", file="  ")


def test_symlink_escape_is_not_indexed(tmp_path):
    outside = tmp_path / "secret.md"
    outside.write_text("# Secret\n", encoding="utf-8")
    skill = tmp_path / "s"
    (skill / "chapters").mkdir(parents=True)
    (skill / "chapters" / "ch01.md").write_text("# Chapter 1\n", encoding="utf-8")
    try:
        os.symlink(outside, skill / "chapters" / "ch02.md")
    except (OSError, NotImplementedError):
        pytest.skip("symlinks not permitted on this machine")
    assert set(Corpus(skill).chapters) == {"ch01.md"}


def test_index_does_not_disclose_absolute_paths(call):
    text = call.resource("ml-systems://index")
    assert "C:\\" not in text and "/home/" not in text and "\"path\"" not in text


def test_missing_corpus_gives_clear_error(tmp_path, monkeypatch):
    monkeypatch.setenv("ML_SYSTEMS_DIR", str(tmp_path / "nope"))
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("mlsys_index.REPO_ROOT", tmp_path)
    monkeypatch.setattr("pathlib.Path.home", lambda: tmp_path)
    with pytest.raises(CorpusError, match="ML_SYSTEMS_DIR"):
        locate_skill_dir()


def test_env_override_selects_directory(tiny_corpus, monkeypatch):
    monkeypatch.setenv("ML_SYSTEMS_DIR", str(tiny_corpus))
    assert locate_skill_dir() == tiny_corpus


# ── helpers ────────────────────────────────────────────────────


def test_normalize_volume():
    assert normalize_volume("both") is None and normalize_volume(None) is None
    assert normalize_volume("1") == 1 and normalize_volume("Vol 2") == 2 and normalize_volume(2) == 2
    with pytest.raises(ValueError):
        normalize_volume("3")


def test_normalize_kind():
    assert normalize_kind("Napkin Math") == "napkin_math"
    assert normalize_kind("war stories") == "war_story"
    assert normalize_kind("all") is None
    with pytest.raises(ValueError):
        normalize_kind("nonsense")


def test_summarize_never_cuts_inside_math():
    text = "word " * 10 + r"\( a + b + c + d \) tail"
    cut = summarize(text, 60)
    assert cut.count(r"\(") == cut.count(r"\)")


# ── search_chapters ────────────────────────────────────────────


def test_search_is_ranked_and_compact(call):
    result = call.tool("search_chapters", query="roofline model arithmetic intensity", limit=5)
    assert 1 <= result["count"] <= 5
    scores = [r["score"] for r in result["results"]]
    assert scores == sorted(scores, reverse=True)
    assert all({"file", "heading", "snippet", "volume"} <= r.keys() for r in result["results"])
    assert len(json.dumps(result)) < 8_000


def test_search_volume_filter(call):
    for vol in (1, 2):
        hits = call.tool("search_chapters", query="checkpoint", volume=str(vol), limit=10)["results"]
        assert hits and all(h["volume"] == vol for h in hits)


def test_search_limit_is_clamped(call):
    assert call.tool("search_chapters", query="memory", limit=10_000)["count"] <= 25
    assert call.tool("search_chapters", query="memory", limit=-5)["count"] == 1


def test_search_verbose_returns_longer_snippets(call):
    short = call.tool("search_chapters", query="memory bandwidth", limit=3)["results"]
    long = call.tool("search_chapters", query="memory bandwidth", limit=3, verbose=True)["results"]
    assert sum(len(r["snippet"]) for r in long) >= sum(len(r["snippet"]) for r in short)


@pytest.mark.parametrize("query", ["", "   ", "!!! ???"])
def test_search_rejects_or_handles_unusable_queries(call, query):
    if query.strip() and any(c.isalnum() for c in query):
        return
    if not query.strip():
        assert "non-empty" in call.tool_error("search_chapters", query=query)
    else:
        assert call.tool("search_chapters", query=query)["count"] == 0


def test_search_rejects_bad_volume(call):
    assert "Invalid volume" in call.tool_error("search_chapters", query="gpu", volume="3")


def test_search_handles_fts_syntax_characters(call):
    call.tool("search_chapters", query='"unbalanced OR (roofline* NEAR')


def test_search_tiny_corpus(tiny_corpus, call):
    result = call.tool("search_chapters", query="roofline")
    assert result["results"][0]["file"] == "ch01.md"


# ── get_definition ─────────────────────────────────────────────


def test_definitions_have_real_terms_and_content(corpus):
    defs = corpus.definitions()
    assert len(defs) > 100
    for row in defs:
        assert row["title"] and not row["title"].startswith("#"), row["title"]
        assert len(row["body"]) > 40, row["title"]


def test_get_definition_exact(call):
    result = call.tool("get_definition", term="Backpropagation")
    first = result["matches"][0]
    assert first["exact"] and first["term"] == "Backpropagation"
    assert "Chain Rule" in first["definition"]


def test_get_definition_case_insensitive_and_partial(call):
    result = call.tool("get_definition", term="iron law")
    assert result["count"] >= 1 and "iron law" in result["matches"][0]["term"].lower()


def test_get_definition_unknown_and_empty(call):
    assert "No definition found" in call.tool_error("get_definition", term="zzzqqqxxx")
    assert "non-empty" in call.tool_error("get_definition", term="")


def test_get_definition_payload_is_bounded(call):
    assert len(json.dumps(call.tool("get_definition", term="a", limit=10))) < 40_000


# ── get_artifact / list_artifacts ──────────────────────────────


def test_get_artifact_by_number(call):
    result = call.tool("get_artifact", artifact_type="napkin_math", identifier="18.2")
    assert result["count"] >= 1 and result["artifacts"][0]["id"] == "18.2"


def test_get_artifact_by_title_words_and_plural_type(call):
    result = call.tool("get_artifact", artifact_type="war stories", identifier="checkpoint")
    assert result["type"] == "war_story"


def test_get_artifact_does_not_match_body_text(call):
    assert "No " in call.tool_error("get_artifact", artifact_type="checkpoint", identifier="zzzqqqxxx")


def test_get_artifact_validation(call):
    assert "Unknown artifact type" in call.tool_error("get_artifact", artifact_type="bogus", identifier="1")
    assert "required" in call.tool_error("get_artifact", artifact_type="all", identifier="1")


def test_get_artifact_is_compact_and_verbose_is_longer(call):
    small = call.tool("get_artifact", artifact_type="napkin_math", identifier="energy")
    big = call.tool("get_artifact", artifact_type="napkin_math", identifier="energy", verbose=True)
    assert len(json.dumps(small)) < 15_000
    assert len(json.dumps(big)) >= len(json.dumps(small))


@pytest.mark.parametrize("volume", ["1", "2"])
def test_list_artifacts_volume_filter_returns_results(call, volume):
    result = call.tool("list_artifacts", volume=volume, limit=200)
    assert result["total"] > 0
    assert all(a["volume"] == int(volume) for a in result["artifacts"])


def test_list_artifacts_pagination_and_no_body(call):
    first = call.tool("list_artifacts", artifact_type="checkpoint", limit=5)
    assert first["count"] == 5 and first["next_offset"] == 5
    second = call.tool("list_artifacts", artifact_type="checkpoint", limit=5, offset=5)
    assert first["artifacts"] != second["artifacts"]
    assert all("text" not in a and "body" not in a for a in first["artifacts"])
    assert len(json.dumps(call.tool("list_artifacts", limit=200))) < 40_000


def test_list_artifacts_bad_arguments(call):
    assert "Unknown artifact type" in call.tool_error("list_artifacts", artifact_type="zzz")
    assert "Invalid volume" in call.tool_error("list_artifacts", volume="x")


def test_list_artifacts_offset_beyond_end(call):
    result = call.tool("list_artifacts", offset=10**6)
    assert result["count"] == 0 and result["next_offset"] is None


# ── get_chapter ────────────────────────────────────────────────


def test_get_chapter_paging_round_trip(call, corpus):
    name = "appA.md"
    full = "\n".join(corpus.chapter_lines(name))
    got, offset, pages = "", 0, 0
    while offset is not None and pages < 200:
        page = call.tool("get_chapter", file=name, offset=offset, max_chars=20_000)
        got += page["content"]
        offset = page["next_offset"]
        pages += 1
    assert got == full


def test_get_chapter_name_forms(call):
    for form in ("ch04", "ch04.md", "CH04", "v2_ch06"):
        assert call.tool("get_chapter", file=form, max_chars=500)["file"].lower().startswith(form.lower()[:4])


def test_get_chapter_first_page_has_outline(call):
    page = call.tool("get_chapter", file="ch05", max_chars=500)
    assert page["outline"] and page["truncated"] and page["next_offset"] == 500


def test_get_chapter_section(call):
    result = call.tool("get_chapter", file="ch05", section="Backpropagation", max_chars=2000)
    assert "ackpropagation" in result["section"] and "outline" not in result


def test_get_chapter_unknown_section(call):
    assert "not found" in call.tool_error("get_chapter", file="ch05", section="zzzqqqxxx")


def test_get_chapter_clamps_page_size(call):
    page = call.tool("get_chapter", file="ch05", max_chars=10**9)
    assert page["returned_chars"] <= 100_000
    assert call.tool("get_chapter", file="ch05", offset=-5, max_chars=600)["offset"] == 0


def test_every_chapter_is_readable(call, corpus):
    assert len(corpus.chapters) == 44
    for name in corpus.chapters:
        assert call.tool("get_chapter", file=name, max_chars=500)["total_chars"] > 500


# ── get_formula / get_cheatsheet_section ───────────────────────


def test_get_formula(call):
    result = call.tool("get_formula", formula_name="roofline")
    assert "roofline" in result["results"][0]["section"].lower()
    assert "$" not in result["results"][0]["text"]


def test_get_formula_errors(call):
    assert "No cheatsheet entry" in call.tool_error("get_formula", formula_name="zzzqqqxxx")
    assert "non-empty" in call.tool_error("get_formula", formula_name="")


def test_cheatsheet_list_and_section(call):
    headings = call.tool("get_cheatsheet_section", section="list")["sections"]
    assert len(headings) >= 5
    hw = call.tool("get_cheatsheet_section", section="hardware")["sections"]
    assert hw and "H100" in hw[0]["text"]
    assert "No cheatsheet section" in call.tool_error("get_cheatsheet_section", section="zzz")


def test_cheatsheet_tiny_corpus(tiny_corpus, call):
    assert "989" in call.tool("get_formula", formula_name="H100")["results"][0]["text"]
    assert call.tool("get_cheatsheet_section", section="numbers")["sections"][0]["heading"] == "1. Key Numbers"


# ── resources / prompts / manifest ─────────────────────────────


def test_index_counts_are_live(call, corpus):
    data = json.loads(call.resource("ml-systems://index"))
    assert data["total_chapters"] == len(corpus.chapters)
    assert data["definitions"] == len(corpus.definitions())
    assert data["artifacts"] == sum(data["artifacts_by_type"].values())
    assert len(data["volume_1"]) + len(data["volume_2"]) == data["total_chapters"]


def test_resources_are_non_empty(call):
    for uri in ("ml-systems://glossary", "ml-systems://cheatsheet", "ml-systems://skill", "ml-systems://patterns"):
        assert len(call.resource(uri)) > 200, uri
    assert json.loads(call.resource("ml-systems://patterns"))["napkin_math"]


def test_skill_resource_is_the_current_manifest(call):
    text = call.resource("ml-systems://skill")
    assert "CC BY-NC-SA" in text and "[your handle]" not in text and "license: MIT" not in text


def test_prompts_render_and_validate(call):
    assert "Chapter 4" in call.prompt("study_chapter", chapter="ch04")
    assert "Roofline" in call.prompt("compare_volumes", topic="Roofline") or "roofline" in call.prompt("compare_volumes", topic="Roofline").lower()
    assert "Iron Law" in call.prompt("design_review", system_description="A GPU inference service")
    assert "ch01.md" in call.prompt("exam_prep", chapters="ch01")
    assert "v2_ch01.md" in call.prompt("exam_prep", chapters="vol2")
    assert "Chapter not found" in call.prompt("study_chapter", chapter="nope")
    assert "Available: appA.md" in call.prompt("exam_prep", chapters="ch01,nope")


def test_plugin_manifest_matches_server(call):
    import pathlib

    manifest = json.loads((pathlib.Path(__file__).parents[1] / "plugin.json").read_text(encoding="utf-8"))
    live = call.names()
    assert set(manifest["mcp"]["tools"]) == live["tools"]
    assert set(manifest["mcp"]["resources"]) == live["resources"]
    assert set(manifest["mcp"]["prompts"]) == live["prompts"]


def test_tools_are_marked_read_only(call):
    import asyncio

    from fastmcp import Client

    async def go():
        async with Client(mcp_server.mcp) as client:
            return await client.list_tools()

    for tool in asyncio.run(go()):
        assert tool.annotations and tool.annotations.readOnlyHint is True, tool.name
