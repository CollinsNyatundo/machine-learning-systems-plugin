# Plan: Fix Machine Learning Systems Extraction Issues

This implementation plan details the steps to address the formatting, duplication, syntax, and placeholder issues identified in the *Machine Learning Systems* textbook markdown files and reference documents.

## User Review Required

> [!IMPORTANT]
> 1. **Reference Consolidation & Duplication Removal**: We will consolidate the reference files to avoid duplication in the repository. We will **migrate the large, comprehensive content** from `chapters/glossary.md` and `chapters/patterns.md` to the root directory (`skills/machine-learning-systems/`), overwriting the scanty root-level files. The duplicate copies inside `chapters/` will then be deleted, and `mcp_server.py` will be modified to load them from the root plugin directory. This ensures a single comprehensive source of truth.
> 2. **Chapter 3 Section Renumbering**: We propose to renumber all sections and definitions in `skills/machine-learning-systems/chapters/v2_ch03.md` from `4.x` to `3.x` to match the chapter number (`# Chapter 3: Network Fabrics`) and the filename `v2_ch03.md`, updating references in glossary and patterns accordingly.
> 3. **Mathematical Formula Restoration**: The restoration of 365 mathematical placeholders will be performed using a semi-automated pipeline that extracts text from the PDF pages, aligns them with placeholders, and replaces them with correct LaTeX formatting.

## Open Questions

> [!NOTE]
> None. The scope of work is fully defined by the assessment report.

## Proposed Changes

### Component: Core Plugin Configuration & Reference Consolidation

#### [MODIFY] [mcp_server.py](mcp_server.py)
- Change paths of `glossary.md`, `patterns.md`, and `cheatsheet.md` to point to the parent of `CHAPTERS_DIR` (e.g. `CHAPTERS_DIR.parent / "glossary.md"`).

#### [MODIFY] [SKILL.md](skills/machine-learning-systems/SKILL.md)
- Ensure all links to `glossary.md`, `patterns.md`, and `cheatsheet.md` point to the root plugin directory.

#### [DELETE] [glossary.md](skills/machine-learning-systems/chapters/glossary.md)
- Remove duplicate copy of the large glossary file in chapters folder after migrating it to root.

#### [DELETE] [patterns.md](skills/machine-learning-systems/chapters/patterns.md)
- Remove duplicate copy of the large patterns file in chapters folder after migrating it to root.

#### [DELETE] [cheatsheet.md](skills/machine-learning-systems/chapters/cheatsheet.md)
- Remove the scanty chapter-level cheatsheet file, as the root cheatsheet is already the detailed, equation-rich source of truth.

---

### Component: Chapter Content & Reference Corrections

#### [NEW] [glossary.md](skills/machine-learning-systems/glossary.md)
- Replace the root `glossary.md` with the large comprehensive version from `chapters/glossary.md` after applying fixes:
  - Clean broken metadata links: convert `[ch05.md • **Chapter:**...](ch05.md • **Chapter:**...)` to `[ch05.md • **Chapter:**...](chapters/ch05.md)`.
  - Fix unbalanced LaTeX block math `\[` delimiters.

#### [NEW] [patterns.md](skills/machine-learning-systems/patterns.md)
- Replace the root `patterns.md` with the large comprehensive version from `chapters/patterns.md` after applying fixes:
  - Update relative chapter links to point to the `chapters/` folder (e.g. `[appB.md](chapters/appB.md)`).
  - Fix unbalanced block math `\[` and inline math `\(` delimiters.

#### [MODIFY] [v2_ch03.md](skills/machine-learning-systems/chapters/v2_ch03.md)
- Renumber all `4.x` headings to `3.x` for consistency with the Chapter 3 title.
- Update `Definition 4.x` to `Definition 3.x` within the file.

#### [MODIFY] [v2_ch10.md](skills/machine-learning-systems/chapters/v2_ch10.md)
- Correct the spatial displacement of the Speculative Decoding sidebar. Place the sidebar definition cleanly inside a blockquote at the beginning of the chapter, and format the chapter title as `# Chapter 10: Performance Engineering`.

#### [MODIFY] [v2_appA.md](skills/machine-learning-systems/chapters/v2_appA.md)
- Correct the title typo from `(DAM)` to `(D·A·M)`.

#### [MODIFY] [ch13.md](skills/machine-learning-systems/chapters/ch13.md)
- Strip raw dollar math wrappers `\(\$` and replace with standard LaTeX delimiters.

#### [MODIFY] all chapter files with placeholders
- Run the placeholder resolution script to restore the 365 mathematical equations from PDF text.

---

## Verification Plan

### Automated Tests
- Run `verify_markdown.py` recursively to check for:
  - Out-of-bounds placeholders
  - Unbalanced LaTeX delimiters
  - Dollar math wrappers
  - HTML comments
- Verify that `mcp_server.py` starts correctly and that the resources `index`, `glossary`, `patterns`, and `cheatsheet` return the correct consolidated files.

### Manual Verification
- View the modified chapter files (like `v2_ch03.md`, `v2_ch10.md`, `ch13.md`) and the consolidated reference files (`glossary.md`, `patterns.md`) to verify layout, links, and mathematical rendering.
