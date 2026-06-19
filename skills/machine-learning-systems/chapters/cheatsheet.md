# Cheatsheet — Machine Learning Systems

> Quick-reference formulas, rules of thumb, and key numbers from the textbook.
> Source: Extracted from **Napkin Math**, **Checkpoint**, and **Systems Perspective** artifacts across 44 chapters.

## Key Numbers (2024–2025)

| Metric | Value | Context | Source |
|--------|-------|---------|--------|
| H100 FP16 TFLOPS | 989 TFLOPS | Peak tensor core throughput | ch11, v2_ch01 |
| H100 Memory BW | 3.35 TB/s | HBM3 bandwidth | ch11, v2_ch01 |
| NVLink BW | 900 GB/s | NVLink 4.0 per link | v2_ch02 |
| NDR InfiniBand BW | 50 GB/s/port | 400 Gb/s per port | v2_ch03 |
| GPU Annual Failure | 8% | ~1/13 annual failure rate | v2_ch01 |
| MTBF (25K GPUs) | 4.4 hours | Per Young-Daly model | v2_ch08 |
| NVLink-to-InfiniBand | 18× ratio | 900 GB/s → 50 GB/s | v2_ch02 |
| Label cost ratio | 1000–3000× vs compute | Human labeling dominates | ch04, ch09 |
| H100 Ridge Point | 295 FLOP/byte | R_peak / BW = 989/3.35 | appD |
| A100 Ridge Point | 153 FLOP/byte | R_peak / BW = 312/2.0 | appD |
| V100 Ridge Point | 139 FLOP/byte | R_peak / BW = 125/0.9 | appD |
| Critical batch (RN50) | B ≈ 8,192 | Beyond = diminishing returns | ch08 |

## Key Formulas

| Formula | Description | Source |
|---------|-------------|--------|
| $$T = \frac{D_{\text{vol}}}{\text{BW}} + \frac{O}{R_{\text{peak}} \cdot \eta_{\text{hw}}} + L_{\text{lat}}$$ | Iron Law: total execution time | appA, ch01 |
| $$\text{AI} = \frac{\text{FLOPs}}{\text{Bytes Transferred}}$$ | Arithmetic Intensity (FLOP/byte) | ch11, appD |
| $$\text{MFU} = \frac{\text{Achieved Model FLOP/s}}{\text{Peak Hardware FLOP/s}}$$ | Model FLOPs Utilization | ch11, v2_ch01 |
| $$R = \frac{R_{\text{peak}}}{\text{BW}}$$ | Ridge Point (compute per byte) | appD |
| $$\tau_{\text{opt}} = \sqrt{2 \cdot T_{\text{write}} \cdot \text{MTBF}}$$ | Young-Daly optimal checkpoint interval | v2_ch08, appD |
| \[ \text{AllReduce Bandwidth} = \frac{2(N-1)}{N} \times \text{Link BW} \] | Ring AllReduce effective bandwidth | v2_ch07 |
| $$D_{KL}(P \parallel Q) = \sum_i P(i) \log \frac{P(i)}{Q(i)}$$ | KL divergence for drift detection | appB |
| $$\text{Mixed-precision Adam: } 16 \text{ bytes/param}$$ | 2B weight + 2B grad + 12B optimizer | appE |
| $$T_{\text{train}} \approx \frac{6PD}{N \cdot X \cdot U}$$ | Training time (6P = 2FWD + 4BWD) | appD |

## Rules of Thumb

| Rule | Description | Source |
|------|-------------|--------|
| 10× Rule | NVLink (900 GB/s) → InfiniBand (50 GB/s) = 18× bandwidth cliff | v2_ch02 |
| 1000× Rule | Labeling costs 1,000–3,000× compute | ch04, ch09 |
| 80/20 Rule | 80% effort on 20% of features (long tail) | ch04 |
| 355 Years | GPT-3 training on single V100 | v2_ch06 |
| 4% Fairness Tax | Demographic parity costs ~4% accuracy | v2_ch15 |
| 50–1000× | SHAP explainability overhead vs inference | v2_ch15 |
| 4.4 hrs MTBF | 25K GPUs at 8% annual failure | v2_ch01, v2_ch08 |
| 2× INT8 speedup | INT8 Tensor Cores 2× FP16 throughput | ch10, ch11 |
| 2× Pruning gain | 50% sparsity halves parameter count | ch10 |
| Ridge Point | If AI < Ridge Point → memory-bound; else compute-bound | appD |
| Checkpoint overhead | Keep checkpoint I/O < 5–10% of training time | v2_ch08 |
| Data gravity | Move compute to data, not data to compute | ch04 |

## Quick Links

- **Vol 1 (21 files):** `chapters/ch01.md` – `ch16.md`, `appA.md`–`appE.md`
- **Vol 2 (23 files):** `chapters/v2_ch01.md` – `v2_ch18.md`, `v2_appA.md`–`v2_appF.md`
- **Full Glossary:** `glossary.md` (112 definitions)
- **All Patterns:** `patterns.md` (820 artifacts)
- **Total Artifacts:** 820+

---

*Generated from 44 chapter files via deterministic extraction.*