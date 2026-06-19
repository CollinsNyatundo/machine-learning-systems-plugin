---
name: machine-learning-systems
version: 1.0.0
description: Full chapter content from "Machine Learning Systems" textbook (Vol 1 & 2)
author: [your handle]
license: MIT
chapters: 44
artifacts: 667
entryPoints:
  gemini: chapters/
  mcp: mcp-server.py
keywords: [machine-learning, systems, textbook, reference, mlops, distributed-systems]
---

# Machine Learning Systems Plugin

This plugin provides the complete text of the **"Machine Learning Systems"** textbook 
(Part 1: Foundations, Part 2: Distribution, Part 3: Serving, Part 4: Governance) 
as **44 chapter files** (21 Vol1 + 23 Vol2) with **667+ named artifacts**.

## Contents

### Vol 1 — Foundations (21 chapters)
- **ch01.md** — Introduction to ML Systems
- **ch02.md** — Compute Infrastructure  
- **ch03.md** — Neural Computation
- **ch04.md** — Data Engineering & Pipeline Architecture
- **ch05.md** — Network Architectures
- **ch06.md** — ML Frameworks
- **ch07.md** — Model Training
- **ch08.md** — Data Selection & Efficient Training
- **ch09.md** — Model Compression
- **ch10.md** — Benchmarking & Profiling
- **ch11.md** — Hardware Acceleration
- **ch12.md** — ML Operations
- **ch13.md** — Model Serving
- **ch14.md** — Responsible Engineering
- **ch15.md** — Sustainable AI
- **ch16.md** — Conclusion
- **appA.md** — D·A·M Taxonomy
- **appB.md** — Data Foundations
- **appC.md** — Algorithm Foundations
- **appD.md** — Machine Foundations
- **appE.md** — System Assumptions

### Vol 2 — Distribution, Serving & Governance (23 chapters)
- **v2_ch01.md** — Introduction to ML Systems (Fleet Scale)
- **v2_ch02.md** — Compute Infrastructure (Fleet Scale)
- **v2_ch03.md** — Network Fabrics
- **v2_ch05.md** — Data Storage — The Fuel Line
- **v2_ch06.md** — Distributed Training Systems
- **v2_ch07.md** — Collective Communication
- **v2_ch08.md** — Fault Tolerance and Reliability
- **v2_ch09.md** — Fleet Orchestration
- **v2_ch10.md** — Performance Engineering
- **v2_ch11.md** — Inference at Scale
- **v2_ch12.md** — Edge Intelligence
- **v2_ch13.md** — ML Operations at Scale
- **v2_ch14.md** — Security & Privacy
- **v2_ch15.md** — Robust AI
- **v2_ch16.md** — Sustainable AI
- **v2_ch17.md** — Responsible Engineering
- **v2_ch18.md** — Conclusion
- **v2_appA.md** — Single-Machine Foundations
- **v2_appB.md** — Fleet Foundations
- **v2_appC.md** — Communication Foundations
- **v2_appD.md** — Reliability Foundations
- **v2_appE.md** — The C³ Taxonomy
- **v2_appF.md** — System Assumptions

## Named Artifacts (667+ total)
| Type | Count |
|------|-------|
| Definitions | 112 |
| Napkin Math | 181 |
| Checkpoints | 101 |
| Systems Perspectives | 108 |
| Examples | 54 |
| War Stories | 41 |
| Lighthouses | 52 |
| Principles | 18 |

## Installation

See [INSTALL.md](INSTALL.md) for platform-specific instructions:
- **Gemini CLI** — Copy to `~/.gemini/config/plugins/machine-learning-systems/`
- **Cursor / Windsurf** — Copy to `.cursor/plugins/` or reference in `.cursorrules`
- **MCP Server** — Run `python scripts/mcp-server.py` and configure
- **Manual** — Copy `chapters/` to your reference directory

## Cross-References
- **Full Glossary** → [glossary.md](glossary.md)
- **Patterns & Principles** → [patterns.md](patterns.md) 
- **Quick Formulas** → [cheatsheet.md](cheatsheet.md)

---

*Regenerated from 44 chapter files with deterministic merge from docling-extracted slices.*