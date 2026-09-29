import asyncio
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from fastmcp import Client  # noqa: E402
from fastmcp.exceptions import ToolError  # noqa: E402

import mcp_server  # noqa: E402
from mlsys_index import Corpus  # noqa: E402


def _run(coro):
    return asyncio.run(coro)


class Caller:
    """Calls tools/resources/prompts through a real in-process MCP client (schema validation included)."""

    def tool(self, name: str, **args):
        async def go():
            async with Client(mcp_server.mcp) as client:
                result = await client.call_tool(name, args)
                return result.data if result.data is not None else json.loads(result.content[0].text)

        return _run(go())

    def tool_error(self, name: str, **args) -> str:
        async def go():
            async with Client(mcp_server.mcp) as client:
                try:
                    await client.call_tool(name, args)
                except Exception as exc:  # ToolError surfaces as a client-side exception
                    return str(exc)
                return ""

        message = _run(go())
        assert message, f"{name}({args}) was expected to fail"
        return message

    def resource(self, uri: str) -> str:
        async def go():
            async with Client(mcp_server.mcp) as client:
                return (await client.read_resource(uri))[0].text

        return _run(go())

    def prompt(self, name: str, **args) -> str:
        async def go():
            async with Client(mcp_server.mcp) as client:
                return (await client.get_prompt(name, args)).messages[0].content.text

        return _run(go())

    def names(self) -> dict[str, set[str]]:
        async def go():
            async with Client(mcp_server.mcp) as client:
                return {
                    "tools": {t.name for t in await client.list_tools()},
                    "resources": {str(r.uri) for r in await client.list_resources()},
                    "prompts": {p.name for p in await client.list_prompts()},
                }

        return _run(go())


@pytest.fixture(scope="session")
def corpus() -> Corpus:
    c = Corpus()
    mcp_server.reset_corpus(c)
    return c


@pytest.fixture(scope="session")
def call(corpus) -> Caller:  # noqa: ARG001 - ensures the shared corpus is installed
    return Caller()


@pytest.fixture
def tiny_corpus(tmp_path):
    """A minimal synthetic skill directory; swaps the shared index and restores it afterwards."""
    skill = tmp_path / "machine-learning-systems"
    chapters = skill / "chapters"
    chapters.mkdir(parents=True)
    (chapters / "ch01.md").write_text(
        "# Chapter 1: Basics\n\n## 1.1 Intro\n\nThe roofline model bounds performance.\n\n"
        "## Definition 1.1: Widget\n\nA widget is a small thing. 1. Significance: it matters.\n\n"
        "## Napkin Math 1.2: Cost of widgets\n\nCosts \\(\\$5\\) each.\n",
        encoding="utf-8",
    )
    (chapters / "v2_ch01.md").write_text(
        "# Chapter 1: Fleets\n\n## Checkpoint 1.1: Fleet check\n\nFleet widgets scale out.\n", encoding="utf-8"
    )
    (skill / "cheatsheet.md").write_text("# Cheat\n\n## 1. Key Numbers\n\nH100 has 989 TFLOPs.\n", encoding="utf-8")
    (skill / "SKILL.md").write_text("---\nname: t\n---\n# T\n", encoding="utf-8")
    (skill / "glossary.md").write_text("# G\n", encoding="utf-8")
    (skill / "patterns.md").write_text("# P\n", encoding="utf-8")
    previous = mcp_server._corpus
    mcp_server.reset_corpus(Corpus(skill))
    yield skill
    mcp_server.reset_corpus(previous)
