---
name: machine-learning-systems
description: "Study and reference guide for Machine Learning Systems design, patterns, architectures, and quantitative invariants (Volume 1 & 2). Includes MCP server for universal AI assistant integration."
---

# Machine Learning Systems Engineering

Welcome to the **Machine Learning Systems** engineering reference guide. This guide is compiled directly from the comprehensive study of *Machine Learning Systems (Volume 1 & Volume 2)*. It is designed to help AI and systems engineers design, optimize, benchmark, deploy, and monitor production-grade machine learning systems.

---

## Core Systems Engineering Philosophy

The defining insight of ML systems engineering is that **constraints drive architecture**. 
Unlike traditional software engineering, ML systems are fundamentally shaped by the physical limits of hardware, network, and data:
* **The light barrier** sets an absolute floor on network latency, demanding edge processing for real-time safety.
* **The power wall** limits the thermal dissipation of chips, dictating battery budgets for mobile and edge nodes.
* **The memory wall** makes moving data (memory bandwidth) far more expensive in latency and energy than executing compute (FLOPs).

Hence, ML engineering is not about making models smaller, but about designing systems that balance these constraints to maximize the **Return on Compute (RoC)**.

---

## MCP Server

The repository root holds a FastMCP server (`mcp_server.py`) that indexes these chapters in memory and serves them to any MCP client. Setup and per-client configuration are in `INTEGRATIONS.md`.

| Type | Names |
|------|-------|
| **Tools** | `search_chapters`, `get_definition`, `get_artifact`, `get_chapter`, `get_formula`, `list_artifacts`, `get_cheatsheet_section` |
| **Resources** | `ml-systems://index`, `ml-systems://glossary`, `ml-systems://patterns`, `ml-systems://cheatsheet`, `ml-systems://skill` |
| **Prompts** | `study_chapter`, `compare_volumes`, `design_review`, `exam_prep` |

Tools return compact results by default. Pass `verbose=true` for longer text, and page long chapters with `get_chapter(file, section=..., offset=...)`.

---

## Global Navigation

### Supporting Reference Materials
* [Glossary of Terms & Quantitative Invariants](glossary.md)
* [Architectural Design Patterns Directory](patterns.md)
* [Equations, Napkin Math Constants & Roofline Cheatsheet](cheatsheet.md)

---

## Volume 1: Single-Machine & Local Foundations

### Part I: Foundations
* [Chapter 1: Introduction to ML Systems](chapters/ch01.md)
* [Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)](chapters/ch02.md)
* [Chapter 3: The ML Development Lifecycle](chapters/ch03.md)
* [Chapter 4: Data Engineering & Pipeline Architecture](chapters/ch04.md)

### Part II: Development & Training
* [Chapter 5: Neural Computation & Training Mechanics](chapters/ch05.md)
* [Chapter 6: Network Architectures (CNNs, Transformers, RecSys)](chapters/ch06.md)
* [Chapter 7: ML Frameworks (TF, PyTorch, JAX)](chapters/ch07.md)
* [Chapter 8: Staged Model Training & Parallelism](chapters/ch08.md)

### Part III: Optimize & Accelerate
* [Chapter 9: Data Selection & Active Learning](chapters/ch09.md)
* [Chapter 10: Model Compression (Pruning, Quantization, Distillation)](chapters/ch10.md)
* [Chapter 11: Hardware Acceleration, Compilers & SoCs](chapters/ch11.md)
* [Chapter 12: Benchmarking Systems & Power Measurement](chapters/ch12.md)

### Part IV: Deploy & Operationalize
* [Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)](chapters/ch13.md)
* [Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)](chapters/ch14.md)
* [Chapter 15: Responsible Engineering & Compliance](chapters/ch15.md)
* [Chapter 16: Conclusion & Thirteen Quantitative Invariants](chapters/ch16.md)

### Appendices (Volume 1)
* [Appendix A: The D·A·M Taxonomy](chapters/appA.md)
* [Appendix B: Data Foundations](chapters/appB.md)
* [Appendix C: Algorithm Foundations](chapters/appC.md)
* [Appendix D: Machine Foundations](chapters/appD.md)
* [Appendix E: System Assumptions](chapters/appE.md)

---

## Volume 2: Distributed Infrastructure & Fleet Scaling

### Part V: The Fleet & Physical Substrate
> Volume 2's own table of contents has no distinct Chapter 3 — numbering runs 1, 2, 4, 5. (A stray "Chapter 3" row in the source ToC duplicates Chapter 4's title with no body content of its own.)

* [Chapter 1: Introduction to ML Systems](chapters/v2_ch01.md)
* [Chapter 2: Compute Infrastructure](chapters/v2_ch02.md)
* [Chapter 4: Network Fabrics](chapters/v2_ch04.md)
* [Chapter 5: Data Storage](chapters/v2_ch05.md)

### Part VI: Distributed Compute & Distribution Logic
* [Chapter 6: Distributed Training Systems](chapters/v2_ch06.md)
* [Chapter 7: Collective Communication](chapters/v2_ch07.md)
* [Chapter 8: Fault Tolerance and Reliability](chapters/v2_ch08.md)
* [Chapter 9: Fleet Orchestration](chapters/v2_ch09.md)

### Part VII: Serving at Scale
* [Chapter 10: Performance Engineering](chapters/v2_ch10.md)
* [Chapter 11: Inference at Scale](chapters/v2_ch11.md)
* [Chapter 12: Edge Intelligence](chapters/v2_ch12.md)
* [Chapter 13: ML Operations at Scale](chapters/v2_ch13.md)

### Part VIII: Governance & Safety
* [Chapter 14: Security & Privacy](chapters/v2_ch14.md)
* [Chapter 15: Robust AI](chapters/v2_ch15.md)
* [Chapter 16: Sustainable AI](chapters/v2_ch16.md)
* [Chapter 17: Responsible Engineering](chapters/v2_ch17.md)
* [Chapter 18: Conclusion](chapters/v2_ch18.md)

### Appendices (Volume 2)
* [Appendix A: Single-Machine Foundations](chapters/v2_appA.md)
* [Appendix B: Fleet Foundations](chapters/v2_appB.md)
* [Appendix C: Communication Foundations](chapters/v2_appC.md)
* [Appendix D: Reliability Foundations](chapters/v2_appD.md)
* [Appendix E: The C³ Taxonomy](chapters/v2_appE.md)
* [Appendix F: System Assumptions](chapters/v2_appF.md)

---

## Installation

Clone the whole repository (the MCP server sits beside `skills/`, not inside it):

```bash
git clone https://github.com/CollinsNyatundo/machine-learning-systems-plugin.git
cd machine-learning-systems-plugin
python -m venv .venv && .venv/bin/pip install -r requirements.txt   # Windows: .venv\Scripts\pip
python scripts/install.py --dry-run    # preview MCP client configuration
```

For Gemini/Antigravity, place the clone at `~/.gemini/config/plugins/machine-learning-systems`.

---

## Source Attribution

| Component | License | Attribution |
|-----------|---------|-------------|
| **Source Textbook** | CC BY-NC-SA 4.0 | "Machine Learning Systems" by Vijay Janapa Reddi, Harvard SEAS — [mlsysbook.ai](https://mlsysbook.ai/) |
| **Course Material** | Educational | CS 249r: Machine Learning Systems, Harvard |
| **Plugin & MCP Server** | CC BY-NC-SA 4.0 | Attribution required; noncommercial use; adaptations use the same license |
| **FastMCP** | MIT | MCP server framework — [gofastmcp.com](https://gofastmcp.com) |

---

*Derived from "Machine Learning Systems" through document extraction and repository-specific indexing. Consult the upstream textbook when exact source fidelity matters.*
