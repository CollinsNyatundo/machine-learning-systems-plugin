# Machine Learning Systems Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Plugin Version](https://img.shields.io/badge/version-1.1.0-blue.svg)]()
[![Chapters](https://img.shields.io/badge/chapters-44-brightgreen.svg)]()
[![Artifacts](https://img.shields.io/badge/named_artifacts-820-orange.svg)]()

A comprehensive study and reference plugin for **"Machine Learning Systems"** — the open-source textbook by **Professor Vijay Janapa Reddi** ([Harvard SEAS](https://vijay.seas.harvard.edu/)), covering the principles and practices of engineering artificially intelligent systems.

Based on the [CS 249r course](https://github.com/harvard-edge/cs249r_book) and the official textbook at **[mlsysbook.ai](https://mlsysbook.ai/)**.

---

## 📚 About the Source Material

| Volume | Title | Focus | Chapters |
|--------|-------|-------|----------|
| **Vol 1** | Introduction to Machine Learning Systems | Foundations, single-machine ML, data engineering, training, serving | 16 + 5 appendices |
| **Vol 2** | Machine Learning Systems at Scale | Distributed training, fleet orchestration, inference at scale, governance | 18 + 6 appendices |

**Author**: Professor Vijay Janapa Reddi, Harvard John A. Paulson School of Engineering and Applied Sciences  
**Course**: CS 249r — Machine Learning Systems  
**License**: The textbook is open-source (CC BY-NC-SA 4.0). This plugin is MIT-licensed for the extracted reference format.

---

## 📦 What's Included

### 44 Chapter Files (Complete Textbook Content)
```
Vol 1 — Foundations (21 files)
├── ch01.md  — Introduction to ML Systems
├── ch02.md  — Compute Infrastructure
├── ch03.md  — Neural Computation
├── ch04.md  — Data Engineering & Pipeline Architecture
├── ch05.md  — Network Architectures
├── ch06.md  — ML Frameworks
├── ch07.md  — Model Training
├── ch08.md  — Data Selection & Efficient Training
├── ch09.md  — Model Compression
├── ch10.md  — Benchmarking & Profiling
├── ch11.md  — Hardware Acceleration
├── ch12.md  — ML Operations
├── ch13.md  — Model Serving
├── ch14.md  — Responsible Engineering
├── ch15.md  — Sustainable AI
├── ch16.md  — Conclusion
├── appA.md  — D·A·M Taxonomy
├── appB.md  — Data Foundations
├── appC.md  — Algorithm Foundations
├── appD.md  — Machine Foundations
└── appE.md  — System Assumptions

Vol 2 — Distribution, Serving & Governance (23 files)
├── v2_ch01.md  — Introduction to ML Systems (Fleet Scale)
├── v2_ch02.md  — Compute Infrastructure (Fleet Scale)
├── v2_ch03.md  — Network Fabrics
├── v2_ch05.md  — Data Storage — The Fuel Line
├── v2_ch06.md  — Distributed Training Systems
├── v2_ch07.md  — Collective Communication
├── v2_ch08.md  — Fault Tolerance and Reliability
├── v2_ch09.md  — Fleet Orchestration
├── v2_ch10.md  — Performance Engineering
├── v2_ch11.md  — Inference at Scale
├── v2_ch12.md  — Edge Intelligence
├── v2_ch13.md  — ML Operations at Scale
├── v2_ch14.md  — Security & Privacy
├── v2_ch15.md  — Robust AI
├── v2_ch16.md  — Sustainable AI
├── v2_ch17.md  — Responsible Engineering
├── v2_ch18.md  — Conclusion
├── v2_appA.md  — Single-Machine Foundations
├── v2_appB.md  — Fleet Foundations
├── v2_appC.md  — Communication Foundations
├── v2_appD.md  — Reliability Foundations
├── v2_appE.md  — The C³ Taxonomy
└── v2_appF.md  — System Assumptions
```

> **Note**: The source textbook Vol 2 has no chapter 3 content (skips from ch03 to ch04). This plugin combines both ch03 and ch04 into 1 (ch03).

### 4 Top-Level Reference Files
| File | Description |
|------|-------------|
| `SKILL.md` | Plugin manifest with chapter index, artifact counts, installation guide |
| `glossary.md` | **111 definitions** — alphabetical, disambiguated Vol 1/Vol 2 |
| `patterns.md` | **820 named artifacts** across 8 categories (see below) |
| `cheatsheet.md` | Key formulas, quantitative rules of thumb, hardware constants |

### 820 Named Artifacts (Extracted & Categorized)
| Category | Count | Description |
|----------|-------|-------------|
| 🧮 Napkin Math | 192 | Worked quantitative examples |
| ✅ Checkpoints | 130 | Self-check questions |
| 🔭 Systems Perspectives | 114 | Architectural insights |
| ⚖️ Principles | 50 | Invariants & laws |
| 💥 War Stories | 41 | Production failures |
| 🏮 Lighthouses | 60 | Reference workloads |
| 📋 Examples | 87 | Applied cases |
| 📖 Definitions | 142 | Formal definitions |
| **Total** | **820** | |

---

## 🚀 Installation

### Gemini CLI (Primary Target)
```bash
# Clone or download this repo
git clone https://github.com/CollinsNyatundo/machine-learning-systems-plugin.git

# Install to Gemini CLI plugins directory
cp -r machine-learning-systems-plugin/skills/machine-learning-systems \
      ~/.gemini/config/plugins/

# Verify
ls ~/.gemini/config/plugins/machine-learning-systems/skills/machine-learning-systems/chapters/
```

### Cursor / Windsurf
```bash
cp -r machine-learning-systems-plugin/skills/machine-learning-systems \
      .cursor/plugins/
```

### MCP Server (Programmatic Access)
```bash
# If MCP server script is added (future)
python machine-learning-systems-plugin/skills/machine-learning-systems/scripts/mcp-server.py
```

### Manual / Any Editor
```bash
# Just copy the chapters folder anywhere
cp -r machine-learning-systems-plugin/skills/machine-learning-systems/chapters \
      ~/my-ml-reference/
```

---

## 🔍 Usage

### In Gemini CLI
```
# List available skills
/skills

# The plugin provides these skills automatically:
# - machine-learning-systems (full textbook reference)
# - Individual chapter skills via chapter-naming
```

### As Reference Documentation
- **Search**: Use `Ctrl+F` in any `.md` file
- **Cross-references**: Patterns/glossary link back to source chapters
- **Formulas**: Cheatsheet has LaTeX-rendered equations
- **Definitions**: Glossary is alphabetical with Vol 1/Vol 2 disambiguation

### Key Formulas Available (Cheatsheet)
- **Iron Law**: `T = D_vol/BW + O/(R_peak·η_hw) + L_lat`
- **Arithmetic Intensity**: `AI = FLOPs / Bytes`
- **MFU**: `Achieved FLOP/s / Peak FLOP/s`
- **Ridge Point**: `R = R_peak / BW`
- **Young-Daly**: `τ_opt = √(2·T_write·MTBF)`
- **KL Divergence**: `D_KL(P∥Q) = Σ P(i) log(P(i)/Q(i))`

---

## 🛠 How This Was Built

1. **Source Extraction**: Docling PDF → markdown slices (via Antigravity / docling-serve)
2. **Deterministic Merge**: Python script `merge_vol1_chapters.py` — no LLM in the loop
   - Preserves every named artifact (Definition, Napkin Math, Checkpoint, etc.)
   - Maintains all tables, equations, code blocks, H2/H3 hierarchy
   - Prepends original summary section ("Section-by-Section Preserve-and-Extend")
3. **Parity Audit**: `audit_vol1_rebuild.py` verifies 100% artifact coverage
4. **Top-Level Regeneration**: Patterns, glossary, cheatsheet extracted from final chapters
5. **Math Placeholder & LaTeX Resolution**: Resolved 354 mathematical comment placeholders (`<!-- formula-not-decoded -->`) and raw dollar-sign math wrappers using a background validation pipeline. Enforced strict math delimiters (`\(` and `\)` for inline, `\[` and `\]` for display) and normalized Greek/Unicode characters across all 44 chapters.
6. **Quality**: 113% average byte ratio (plugin ≥ slice), 0 missing artifacts

**Artifacts preserved**: `/tmp/merge_vol1_chapters.py`, `/tmp/audit_vol1_rebuild.py`, `/tmp/backup_vol1/`

---

## 📖 Attribution & License

| Component | License | Attribution |
|-----------|---------|-------------|
| **Source Textbook** | CC BY-NC-SA 4.0 | "Machine Learning Systems" by Vijay Janapa Reddi, Harvard SEAS — [mlsysbook.ai](https://mlsysbook.ai/) |
| **Course Material** | Educational | CS 249r: Machine Learning Systems, Harvard |
| **This Plugin** | MIT | Plugin format, extraction scripts, top-level indices — free to use, modify, distribute |
| **Docling** | Apache 2.0 | PDF → markdown conversion — [ds4sd/docling](https://github.com/docling-project/docling) |

### Proper Citation
```
@book{reddi2024mlsystems,
  title = {Machine Learning Systems},
  author = {Reddi, Vijay Janapa},
  institution = {Harvard John A. Paulson School of Engineering and Applied Sciences},
  course = {CS 249r},
  year = {2024},
  url = {https://mlsysbook.ai/},
  note = {Open-source textbook, CC BY-NC-SA 4.0}
}

@software{mls_plugin_2025,
  title = {Machine Learning Systems Plugin for Gemini CLI / Cursor / MCP},
  author = {Nyatundo, Collins},
  url = {https://github.com/CollinsNyatundo/machine-learning-systems-plugin},
  license = {MIT},
  note = {Deterministic extraction from docling slices, 820 artifacts, 44 chapters}
}
```

---

## 🤝 Contributing

1. **Source corrections**: Report to upstream textbook at [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book)
2. **Plugin improvements**: PRs welcome for:
   - Additional top-level indices (timeline, concept map, etc.)
   - MCP server implementation
   - Better cross-references between Vol 1 ↔ Vol 2
   - Search/index tooling

---

## 🙏 Acknowledgments

- **Prof. Vijay Janapa Reddi** — for writing and open-sourcing this exceptional textbook
- **Harvard EDGE / CS 249r team** — for the course and materials
- **Docling Project** — for best-in-class PDF understanding
- **Antigravity** — for the deterministic rebuild pipeline
- **Nous Research / Hermes** — for the agent framework used to build this

---

## 📞 Support

- **Plugin issues**: [GitHub Issues](https://github.com/CollinsNyatundo/machine-learning-systems-plugin/issues)
- **Textbook questions**: [mlsysbook.ai](https://mlsysbook.ai/) or [CS 249r discussions](https://github.com/harvard-edge/cs249r_book/discussions)
- **Author**: Collins Nyatundo ([@CollinsNyatundo](https://github.com/CollinsNyatundo))

---

*Generated from the complete "Machine Learning Systems" textbook via deterministic docling extraction. Every definition, formula, worked example, and architectural insight preserved from source.*
