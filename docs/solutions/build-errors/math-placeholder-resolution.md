---
title: Resolution of Mathematical Placeholders and LaTeX Delimiters
date: 2026-06-21
problem_type: build_errors
track: bug
component: chapters
tags: [math, latex, placeholders, build-errors]
symptoms:
  - Unresolved mathematical placeholders (<!-- formula-not-decoded -->)
  - Unbalanced LaTeX delimiters (inline vs block)
  - Raw dollar sign wrappers ($ and $$) causing compilation errors
root_cause: PDF-to-Markdown conversion failures resulting in truncated or omitted math formulas and muddled delimiters.
resolution_type: automation
---

# Resolution of Mathematical Placeholders and LaTeX Delimiters

## Problem
The textbook chapters contained 354 unresolved mathematical placeholders (`<!-- formula-not-decoded -->`), raw dollar signs (`$` and `$$`), and unbalanced LaTeX math delimiters, which prevented clean rendering and compilation of equations.

## Symptoms
- Observable `<!-- formula-not-decoded -->` comment lines in rendered text.
- Equations failing to parse or compile.
- Mixed inline and block math delimiters (e.g., `\(` matched with `$`).

## What Didn't Work
- **Sequential LLM Chat Queries**: Querying the LLM sequentially within the main chat session led to severe token bloat, slowing down the work and hitting context limits.
- **Naïve OCR / Direct Translation**: Directly passing raw text to the model without standardizing unicode mappings caused failures in resolving Greek symbols (e.g., `𝑂` or `\α`), resulting in validation check failures and slower Claude fallbacks.

## Solution
We moved the math formula translation and replacement out of the main chat context into a background execution pipeline:
1. **Consolidated Mapping Extraction**: Extracted all placeholders, their surrounding markdown lines, and matched PDF page text into batch JSON input files.
2. **Background Resolution Pipeline**:
   - Programmatically queried `llama-3.1-8b-instant` for fast, zero-thinking formula correction.
   - Enforced strict validation: rejected responses containing raw `$` or mismatched delimiters.
   - Automatically normalized Unicode math script and Greek symbols using Python regex mappings (e.g., `α` -> `\alpha`, `\α` -> `\alpha`) to bypass manual correction needs.
   - Used a high-quality fallback (`nemotron-3-super-120b-a12b` via proxy) only for failed validations.
3. **Pristine Math Substitution**: Applied all 354 formulas back to their respective markdown files, adapting to shifted line numbers using local search windowing.

## Why This Works
- **Token Efficiency**: Keeps the main chat conversation clean of long sequential LLM calls.
- **Strict Validation**: Rejects incorrect formulas before they are written to disk.
- **Robust Substitution**: Resolves shifts in source files dynamically.

## Prevention
- **Delimiter Rules**: Restrict inline math to `\(` and `\)`, and block math to `\[` and `\]`. Never use raw `$` or `$$`.
- **Validation Script**: Run the recursive `verify_markdown.py` validator before committing changes:
  ```bash
  python scratch/verify_markdown.py
  ```
