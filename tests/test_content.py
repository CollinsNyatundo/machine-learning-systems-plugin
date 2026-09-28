"""Content-policy tests: math delimiters, extraction artifacts, generated files, fixer."""

import build_indexes
import fix_content
import validate_content
from mlsys_index import Corpus


def codes(text: str) -> set[str]:
    return {i.code for i in validate_content.validate_markdown("t.md", text)}


# ── the shipped corpus obeys the policy ────────────────────────


def test_corpus_passes_validator():
    issues = validate_content.validate_all()
    assert not issues, "\n".join(str(i) for i in issues[:20])


def test_generated_files_are_current():
    corpus = Corpus()
    for name, builder in (("glossary.md", build_indexes.build_glossary), ("patterns.md", build_indexes.build_patterns)):
        on_disk = (corpus.skill_dir / name).read_text(encoding="utf-8").replace("\r\n", "\n")
        assert on_disk == builder(corpus), f"{name} is stale: run python scripts/build_indexes.py"


def test_no_duplicate_reference_files_in_chapters():
    chapters = Corpus().chapters_dir
    for name in ("glossary.md", "patterns.md", "cheatsheet.md"):
        assert not (chapters / name).exists(), f"{name} must live one level up"


# ── validator detects each problem ─────────────────────────────


def test_validator_flags_bare_dollars():
    assert "bare-dollar" in codes("Costs $5 and $x$ math.")
    assert "bare-dollar" in codes("$$x$$")


def test_validator_accepts_escaped_prices_and_delimited_math():
    assert not codes(r"Costs \$5 and \(x^2\) and \[ y \]" + "\n")


def test_validator_ignores_code_fences():
    assert "bare-dollar" not in codes("```\necho $HOME\n```\n")


def test_validator_flags_unbalanced_math():
    assert "math-unbalanced" in codes(r"open \( never closed")
    assert "math-unbalanced" in codes("\\[ open\n")


def test_validator_flags_artifacts():
    assert "image-stub" in codes("<!-- image -->\n")
    assert "placeholder" in codes("[Formula not decoded]\n")
    assert "pipeline-heading" in codes("## Section-by-Section Preserve-and-Extend\n")
    assert "double-rule" in codes("a\n\n---\n\n---\n\nb\n")


def test_validator_flags_table_without_separator_but_accepts_alignment_rows():
    assert "table-separator" in codes("| a | b |\n| 1 | 2 |\n")
    assert "table-separator" not in codes("| a | b |\n| :-: | :--- |\n| 1 | 2 |\n")


def test_validator_flags_broken_links(tmp_path):
    (tmp_path / "chapters").mkdir()
    (tmp_path / "SKILL.md").write_text("[x](chapters/missing.md)\n", encoding="utf-8")
    (tmp_path / "glossary.md").write_text("", encoding="utf-8")
    (tmp_path / "patterns.md").write_text("", encoding="utf-8")
    assert [i.code for i in validate_content.validate_links(tmp_path)] == ["broken-link"]


# ── fixer ──────────────────────────────────────────────────────


def test_fixer_converts_inline_and_display_math():
    fixed = fix_content.fix_text("Let $x^2$ be, and $$y = 1$$ holds.\n")
    assert r"\(x^2\)" in fixed and r"\[y = 1\]" in fixed and "$" not in fixed


def test_fixer_escapes_prices_but_not_math():
    fixed = fix_content.fix_text("Costs $3,000 - $5,000 and $224 \\times 224$ pixels.\n")
    assert r"\$3,000 - \$5,000" in fixed
    assert r"\(224 \times 224\)" in fixed


def test_fixer_handles_multiline_display_and_unwrapped_pair():
    fixed = fix_content.fix_text("$$\na = b\n$$\n\\( $z$ \\)\n")
    assert "$" not in fixed and r"\(z\)" in fixed


def test_fixer_leaves_code_fences_mostly_alone():
    assert "echo $HOME" in fix_content.fix_text("```\necho $HOME\n```\n")


def test_fixer_strips_artifacts_and_is_idempotent():
    src = "## Section-by-Section Preserve-and-Extend\n\n# T\n\n<!-- image -->\n\ntext\n\n---\n\n---\n\nmore $9\n"
    once = fix_content.fix_text(src)
    assert not codes(once)
    assert fix_content.fix_text(once) == once


def test_fixer_recovers_from_unbalanced_display_block():
    fixed = fix_content.fix_text("\\[ never closed\n\nprice $5 here\n")
    assert r"\$5" in fixed
