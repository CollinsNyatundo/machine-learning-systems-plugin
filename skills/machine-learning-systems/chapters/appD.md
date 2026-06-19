# Appendix D: Machine Foundations

## Material Covered in This Chapter

- Purpose
- How to Use This Appendix
- D.1 Numbers to Know
- Key Takeaways: Three numbers that matter most
- The invariants: Numbers that will not change
- Speed of light tax
- Energy hierarchy
- Scaling laws
- Latency budgets: The nonnegotiables
- Current hardware reference (c. 2024)
- Compute throughput
- Roofline ridge points
- Systems Perspective 20.1: Anote on terminology: GPUs and accelerators
- D.2 Physics of Computing
- Systems Perspective 20.2: Why this matters
- D.2.1 The roofline model
- LIGHTBULB Batch size controls arithmetic intensity
- D.2.1.1 Aconcrete example: The A100 analysis
- D.2.2 Dimensional analysis
- D.2.3 Amdahl's Law and Gustafson's Law
- D.2.3.1 Strong scaling (Amdahl's Law)
- D.2.3.2 Weak scaling (Gustafson's Law)
- Napkin Math 20.1: The training time equation
- Checkpoint 20.1: Check your understanding: Performance models
- D.3 Computer Architecture Essentials
- D.3.1 Latencies every programmer should know
- D.3.2 The AI hardware cheat sheet (modern reference)
- D.3.3 The memory hierarchy
- D.3.4 Bandwidth vs. latency
- · Bandwidth-Bound (1 GB Checkpoint) :
- D.4 Numerical Representations
- Systems Perspective 20.3: Why this matters
- D.4.1 Floating-point format comparison
- Systems Perspective 20.4: The dynamic range wall
- D.4.2 Integer quantization
- D.5 Fallacies and Pitfalls
- Further Reading

---

## Section-by-Section Preserve-and-Extend

# Appendix D: Machine Foundations

## Purpose & Overview
Every Machine Learning (ML) systems engineer must master the fundamental physical laws, hardware limits, and reference
numbers that govern performance. Performance bottlenecks—such as unexpected slow-downs, failure to meet Service Level
Agreements (SLAs), or poor parallel scaling—frequently masquerade as software bugs. In reality, they are the predictable
outcomes of physical constraints (latency, bandwidth, energy) and architecture limits (memory hierarchy, numerical
precision, and interconnects).

This appendix provides a rigorous quantitative reference for systems engineering, covering:
1. **Numbers to Know**: Latency, bandwidth, and energy constants.
2. **Physics of Computing**: The Roofline model, Dimensional Analysis, Amdahl's/Gustafson's laws, and Little's law.
3. **Computer Architecture Essentials**: Memory hierarchy, hardware specs (c. 2024), and bandwidth-latency bounds.
4. **Numerical Representations**: Floating-point formats (FP32, FP16, BF16, FP8) and integer quantization.
5. **Fallacies & Pitfalls**: Common systems engineering misconceptions.

---

## D.1 Numbers to Know

Ratios between performance categories remain stable across hardware generations. Memorizing these invariants enables
instant sanity-checks for feasibility.

### Three Numbers to Memorize
1. **~600x Energy Ratio**: DRAM access consumes \(\sim 581\times\) more energy than an FP16 FLOP. Moving data is the
primary energy cost in AI accelerators.
2. **16 Bytes/Parameter for Adam Training**:
   * Model weights: \(2\text{ bytes (FP16)}\)
   * Gradients: \(2\text{ bytes (FP16)}\)
   * Master weights: \(4\text{ bytes (FP32)}\)
   * Optimizer states (Adam): \(8\text{ bytes (FP32)}\) (4 bytes for momentum + 4 bytes for variance)
   * **Total**: \(16\text{ bytes per parameter}\). (e.g., a 7B parameter model requires \(112\text{ GB}\) of memory just
to initialize training).
3. **\(\sim 200\text{ km/ms}\) Speed of Light in Fiber**: Transmitting data over physical distance imposes a hard
latency floor (e.g., cross-country round-trip is \(\approx 40\text{ ms}\)).

### Reference Tables

#### Table D.1: Speed of Light Reference
No software optimization can reduce these fiber propagation delays.
| Distance | Round-Trip Latency | Implication |
| :--- | :--- | :--- |
| Same data center | \(\sim 1\text{ ms}\) | Distributed training is highly feasible |
| Cross-country (US) | \(\sim 40\text{ ms}\) | Edge deployments required for \(<100\text{ ms}\) applications |
| Cross-Atlantic | \(\sim 60\text{ ms}\) | Content Delivery Networks (CDNs) required for global users |
| Cross-Pacific | \(\sim 100\text{ ms}\) | Data locality is critical |

#### Table D.2: The Energy Wall
Quantifies energy costs at 45nm process (Horowitz 2014).
| Relationship | Ratio | Why It Is Stable |
| :--- | :--- | :--- |
| DRAM access vs. FP16 compute | \(\sim 581\times\) | Wire capacitance scales with physical distance |
| FP32 vs. INT8 energy | \(\sim 18\times\) | Bit width determines transistor switching energy |
| FP32 vs. FP16 energy | \(\sim 3.4\times\) | Narrower datapath reduces switching energy |
| L1 SRAM vs. register | \(\sim 50\times\) | Physical distance to ALU on-chip |

#### Table D.3: The Latency Hierarchy
| Relationship | Ratio | Why It Persists |
| :--- | :--- | :--- |
| Accelerator memory (HBM) vs. register | \(\sim 300\times\) slower | On-chip registers vs. off-chip HBM stack |
| SSD vs. register | \(\sim 100,000\times\) slower | Electrical charge trap vs. SRAM/Register switching |
| Network vs. local memory | \(\sim 16\times\) slower | Physical distance, packet switching overhead |
| Accelerator memory BW vs. CPU-Accelerator link | \(\sim 52\times\) faster | High-bandwidth 3D stacked memory prioritization |

#### Table D.4: Scaling Rules
Arithmetic scaling relations that are hardware-independent.
| Rule | Formula | Example (7B Parameter Model) |
| :--- | :--- | :--- |
| Inference memory (FP16) | \(2\text{ bytes} \times \text{parameters}\) | \(7\text{B parameters} \rightarrow 14\text{ GB}\) |
| Inference memory (INT8) | \(1\text{ byte} \times \text{parameters}\) | \(7\text{B parameters} \rightarrow 7\text{ GB}\) |
| Training memory (Adam) | \(16\text{ bytes} \times \text{parameters}\) | \(7\text{B parameters} \rightarrow 112\text{ GB}\) |
| Inference FLOPs (Transformer) | \(\sim 2\text{ FLOPs} \times \text{parameters per token}\) | \(7\text{B model} \rightarrow \sim 14\text{ GFLOPs/token}\) |
| Training FLOPs | \(\sim 6\text{ FLOPs} \times \text{parameters} \times \text{tokens}\) | 7B on 1T tokens \(\rightarrow 4.2 \times 10^{22}\) FLOPs |
| Data center vs. edge compute | \(\sim 19\times\) compute ratio | Driven by power budget limits (700W vs 5W) |

#### Table D.5: Latency Targets (SLA Budgets)
Non-negotiable constraints set by psychology or physical safety.
| Application | Budget | Constraint |
| :--- | :--- | :--- |
| Autonomous braking | \(<10\text{ ms}\) | At \(100\text{ km/h}\), \(10\text{ ms}\) corresponds to \(28\text{ cm}\) travel distance |
| Voice assistant | \(<100\text{ ms}\) | Human perception of instantaneous response |
| Web search | \(<200\text{ ms}\) | User patience/focus threshold |
| Video streaming | \(<1\text{ s}\) | Start-up buffer tolerance |
| Batch training | Hours to days | Optimized for throughput, not step latency |

---

## D.2 Physics of Computing

To diagnose bottlenecks, systems engineers construct analytical models of hardware and application scaling.

### D.2.1 The Roofline Model
The Roofline Model sets the maximum performance ceiling based on arithmetic intensity:
\[
\text{Arithmetic Intensity (AI)} = \frac{\text{Operations (FLOPs)}}{\text{Memory Moved (Bytes)}}
\]

The model divides hardware performance into two regimes:
1. **Memory-Bound**: Performance is limited by memory bandwidth.
   \[
   \text{Attainable Performance (TFLOPS)} = \text{Arithmetic Intensity} \times \text{Memory Bandwidth (TB/s)}
   \]
2. **Compute-Bound**: Performance is limited by peak compute capability.
   \[
   \text{Attainable Performance (TFLOPS)} = \text{Peak Compute}
   \]

The intersection of these two boundaries is the **Ridge Point**:
\[
\text{Ridge Point} = \frac{\text{Peak Compute (TFLOPS)}}{\text{Memory Bandwidth (TB/s)}}
\]

* **Workloads below the Ridge Point** are memory-bound. Optimization focus: memory layout, fusion, or quantization.
* **Workloads above the Ridge Point** are compute-bound. Optimization focus: compiler optimizations, ALU utilization.

#### Batch Size Controls Arithmetic Intensity
Consider matrix multiplication \(Y = XW\) where \(X \in \mathbb{R}^{B \times D_{in}}\) and \(W \in \mathbb{R}^{D_{in}
\times D_{out}}\):
* **Compute (FLOPs)**: \(2 \times B \times D_{in} \times D_{out}\) (Multiply-Add operations)
* **Memory Access (Bytes)**: Assuming weights are loaded once: \(D_{in} \times D_{out} \times \text{bytes\_precision}\)
* **Arithmetic Intensity**:
  \[
  \text{AI} = \frac{2 \times B \times D_{in} \times D_{out}}{D_{in} \times D_{out} \times \text{bytes\_precision}} =
\frac{2B}{\text{bytes\_precision}}
  \]

Increasing batch size \(B\) scales compute requirements linearly while keeping memory transfer for model weights
constant. This transitions memory-bound inference (\(B=1\)) to compute-bound inference (\(B \ge 64\)).

#### A100 Case Study
* **Hardware Specs**: NVIDIA A100 (FP16 Tensor Cores = 312 TFLOPS, HBM2e Bandwidth = 2.0 TB/s).
* **Ridge Point**: \(\frac{312\text{ TFLOPS}}{2.0\text{ TB/s}} = 156\text{ FLOP/byte}\) (referenced as 153 FLOP/byte
under nominal conditions).
* **GEMM (4096 \(\times\) 4096)**:
  * Arithmetic Intensity \(\approx 1365\text{ FLOP/byte}\).
  * Since \(1365 > 156\), it is **compute-bound** (highly efficient execution).
* **ReLU (Element-wise, 4096 \(\times\) 4096)**:
  * Arithmetic Intensity \(\approx 0.25\text{ op/byte}\).
  * Since \(0.25 \ll 156\), it is **memory-bound** (achieves \(\sim 0.16\%\) of peak compute). Operators must be fused
to avoid round-trips to DRAM.

### D.2.2 Dimensional Analysis
All systems equations must be checked for dimensional homogeneity. For example, the **Iron Law of ML Systems**:
\[
\text{Step Time} = \frac{\text{FLOPs}}{\text{Compute Throughput (FLOPs/s)}} + \frac{\text{Bytes}}{\text{Memory Bandwidth
(Bytes/s)}} + \text{Overhead}
\]

Confirming units:
\[
[\text{seconds}] = \frac{[\text{FLOPs}]}{\left[\frac{\text{FLOPs}}{\text{seconds}}\right]} +
\frac{[\text{Bytes}]}{\left[\frac{\text{Bytes}}{\text{seconds}}\right]} + [\text{seconds}]
\]
\[
[\text{seconds}] = [\text{seconds}] + [\text{seconds}] + [\text{seconds}]
\]

### D.2.3 Amdahl's Law and Gustafson's Law

#### Strong Scaling (Amdahl's Law)
Strong scaling models speedup on a **fixed-size problem** as you add more parallel processors:
\[
\text{Speedup}(n) = \frac{1}{s + \frac{1 - s}{n}}
\]
Where:
* \(s\) is the serial fraction of the workload (cannot be parallelized).
* \(n\) is the number of parallel processors (accelerators).

As \(n \to \infty\), speedup is strictly capped by the serial ceiling:
\[
\lim_{n \to \infty} \text{Speedup}(n) = \frac{1}{s}
\]

For instance, with \(5\%\) serial overhead (\(s=0.05\)):
* Max speedup = \(\frac{1}{0.05} = 20\times\), even if you deploy an infinite number of GPUs.

#### Weak Scaling (Gustafson's Law)
Weak scaling models speedup as the **problem size scales proportionally** with the number of processors:
\[
\text{Scaled Speedup}(n) = n - s(n - 1)
\]

Here, the parallel portion of the workload scales with \(n\), keeping execution time constant while throughput scales.
With \(5\%\) serial overhead (\(s=0.05\)) and \(n=1000\):
* Scaled Speedup = \(1000 - 0.05 \times (999) \approx 950\times\) (retains \(95\%\) efficiency). This explains why LLM
scaling focuses on weak scaling (training larger models on larger datasets).

### D.2.4 Little's Law
For capacity planning in queuing systems (like inference endpoints):
\[
N_{\text{req}} = \lambda \times T_{\text{lat}}
\]
Where:
* \(N_{\text{req}}\) = average concurrent requests in the system.
* \(\lambda\) = query arrival rate (queries per second, QPS).
* \(T_{\text{lat}}\) = average request latency (seconds).

#### Memory Capacity Sizing
* If sustaining \(1000\text{ QPS}\) at \(50\text{ ms}\) average latency:
  \[
  N_{\text{req}} = 1000 \times 0.05\text{ s} = 50\text{ concurrent requests}
  \]
* If each request requires \(1\text{ GB}\) of memory (activations + KV cache), the system needs \(50\text{ GB}\) minimum
memory.
* If physical accelerator capacity is \(24\text{ GB}\), concurrency is capped at \(24\), limiting the maximum throughput
to:
  \[
  \lambda_{\text{max}} = \frac{24}{0.05\text{ s}} = 480\text{ QPS}
  \]

### D.2.5 LLM Training Time Equation
To calculate the total wall-clock training time \(T\) of a Large Language Model:
\[
T = \frac{6 \times P \times D}{N \times X \times U}
\]
Where:
* \(P\) = number of model parameters.
* \(D\) = number of training tokens.
* \(6\) = multiplier for FLOPs per token (2 for forward pass, 4 for backward pass).
* \(N\) = number of accelerators.
* \(X\) = peak FLOP/s of a single accelerator.
* \(U\) = Model FLOPs Utilization (MFU), typically \(0.30\) to \(0.50\).

---

## D.3 Computer Architecture Essentials

Performance is dictated by the cost of data movement across the memory hierarchy.

### D.3.1 Latency and Bandwidth Hierarchy (c. 2024)

#### Table D.9: Detailed Latency Reference
Note the HBM-to-SRAM boundary gap (nearly two orders of magnitude).
| Component | Latency (ns) | Cycles (Approx.) | Relative Distance Analogy |
| :--- | :--- | :--- | :--- |
| Register | \(\sim 0.3\text{ ns}\) | 1 cycle | 10 seconds (Pencil on desk) |
| L1 Cache | \(\sim 1\text{ ns}\) | 3–4 cycles | 1 minute |
| L2 Cache | \(\sim 4\text{ ns}\) | 12 cycles | 4 minutes |
| HBM3 (GPU Memory) | \(\sim 300\text{ ns}\) | 1,000 cycles | 5 hours (Walk across office) |
| NVLink (GPU-GPU) | \(\sim 500\text{ ns}\) | 1,500 cycles | 8 hours |
| PCIe Gen5 (CPU-GPU) | \(\sim 1000\text{ ns}\) | 3,000 cycles | 1 day |
| CPUDRAM | \(\sim 100\text{ ns}\) | 300 cycles | 2 hours |
| InfiniBand (Network) | \(\sim 5000\text{ ns}\) | 15,000 cycles | 1 week (Flight to moon) |
| NVMe SSD (Storage) | \(\sim 100,000\text{ ns}\) | 300,000 cycles | 3 months |

#### Table D.10: Accelerator Specs Comparison (c. 2024)
Standard units of compute for hardware planning.
| Spec | NVIDIA H100 (SXM) | Google TPU v5p | System Impact |
| :--- | :--- | :--- | :--- |
| FP16/BF16 Peak | 989 TFLOPS | 459 TFLOPS | Peak compute ceiling |
| Memory Bandwidth | 3.35 TB/s | 2.76 TB/s | Memory bus width (pipe size) |
| HBM Capacity | 80 GB | 95 GB | Max model weights & KV cache |
| L2/SRAM Cache | 50 MB | \(\sim 100\text{ MB}\) | Bounds operator fusion scope |
| Interconnect Bandwidth | 900 GB/s (NVLink) | 1200 GB/s (ICI) | Bounds model-parallel scaling |

#### Table D.11: Physical Properties of the Memory Hierarchy
Detailed latency, bandwidth, and energy cost per 32-bit access.
| Layer | Technology | Latency | Bandwidth | Energy (per 32b) |
| :--- | :--- | :--- | :--- | :--- |
| Registers | Flip-Flops | \(\sim 0.3\text{ ns}\) | - | 0.01 pJ |
| L1 Cache | SRAM | \(\sim 1\text{ ns}\) | - | 0.5 pJ |
| L2 Cache | SRAM | \(\sim 4\text{ ns}\) | - | 2.0 pJ |
| Memory (Local) | HBM3 | \(\sim 300\text{ ns}\) | 3,350 GB/s | 640 pJ |
| Interconnect | NVLink 4.0 | \(\sim 500\text{ ns}\) | 900 GB/s | \(\sim 640\text{ pJ}\) |
| Host Link | PCIe Gen5 | \(\sim 1000\text{ ns}\) | 64 GB/s | \(\sim 640\text{ pJ}\) |
| System RAM | DDR5 | \(\sim 100\text{ ns}\) | 50 GB/s | \(\sim 640\text{ pJ}\) |
| Network (Fabric) | InfiniBand NDR | \(\sim 5000\text{ ns}\) | 50 GB/s | \(\sim 10,000\text{ pJ}\) |
| Storage (Local) | NVMe SSD | \(\sim 100,000\text{ ns}\) | 7.0 GB/s | \(\sim 5,000\text{ pJ}\) |

### D.3.2 Bandwidth vs. Latency Trade-offs
Total data transfer time is modeled as:
\[
T_{\text{transfer}} = T_{\text{latency}} + \frac{\text{Data Size}}{\text{Bandwidth}}
\]

* **Latency-Bound Regime**: When \(\text{Data Size}\) is small (e.g., \(1\text{ KB}\) packet on \(10\text{ Gbps}\)
network with \(10\text{ ms}\) ping):
  \[
  T_{\text{transfer}} = 10\text{ ms} + \frac{1\text{ KB}}{10\text{ Gbps}} \approx 10\text{ ms} + 0.8\text{ }\mu\text{s}
\approx 10\text{ ms}
  \]
  Bandwidth is irrelevant; propagation latency dominates.
* **Bandwidth-Bound Regime**: When \(\text{Data Size}\) is large (e.g., \(1\text{ GB}\) checkpoint on same link):
  \[
  T_{\text{transfer}} = 10\text{ ms} + \frac{1\text{ GB}}{10\text{ Gbps}} = 10\text{ ms} + 800\text{ ms} = 810\text{ ms}
  \]
  Latency is negligible; bandwidth dominates.

---

## D.4 Numerical Representations

Numerical format selection is a direct application of the Iron Law. Halving bit precision halves memory traffic,
doubling performance on memory-bound workloads.

### D.4.1 Floating-Point Formats

#### Table D.12: Precision Format Comparison
| Format | Bits | Exponent | Mantissa | Dynamic Range | Typical Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FP32** | 32 | 8 bits | 23 bits | \(\sim 10^{-38}\) to \(10^{38}\) | Standard training, reference weights |
| **FP16** | 16 | 5 bits | 10 bits | \(\sim 10^{-5}\) to \(6.5 \times 10^4\) | Inference, training (with loss scaling) |
| **BF16** | 16 | 8 bits | 7 bits | Same as FP32 | Preferred mixed-precision training |
| **FP8** | 8 | 4 or 5 bits | 3 or 2 bits | Varies (E4M3, E5M2) | Low-precision inference (H100+) |
| **INT8** | 8 | N/A | N/A | \(-128\) to \(127\) | Quantized edge/server inference |

#### Format Details
* **BF16 (Brain Float 16)**: Matches the 8-bit exponent of FP32, providing the same dynamic range. This prevents
underflow/overflow issues in training, removing the need for complex loss scaling.
* **FP16**: Employs a smaller exponent (5 bits) and larger mantissa (10 bits). The limited dynamic range requires **Loss
Scaling** (multiplying gradients by a large constant) to prevent values from collapsing to zero.
* **INT8**: Yields maximum execution efficiency on battery-constrained/edge platforms by leveraging simple, high-density
integer ALUs.

### D.4.2 Integer Quantization Methods
Mapping floating-point weights and activations to 8-bit integers relies on scaling.

#### Symmetric Quantization
Centers the mapping scale at zero. Best for symmetric distributions (e.g., weights).
\[
x_{\text{int}} = \text{round}\left( \frac{x}{\alpha} \times 127 \right)
\]
Where \(\alpha\) is the clipping threshold:
\[
\alpha = \max(|x|)
\]

#### Asymmetric Quantization
Accommodates asymmetric distributions (e.g., post-ReLU activations) by introducing a zero-point shift:
\[
x_{\text{int}} = \text{round}\left( \frac{x - x_{\text{min}}}{\alpha} \times 255 \right)
\]
Where \(\alpha\) is the dynamic range width:
\[
\alpha = x_{\text{max}} - x_{\text{min}}
\]

---

## D.5 Fallacies and Pitfalls

### Fallacy: "Doubling the number of accelerators halves training time"
* **Reality**: This assumes perfect linear strong scaling (\(100\%\) parallel efficiency). In practice, adding
accelerators:
  1. Increases communication overhead (collective operations like All-Reduce scale with network size).
  2. Reduces local batch sizes per device, pushing execution into memory-bound or latency-bound regimes.
  3. Limits speedup according to Amdahl's Law unless the total dataset/model size scales up concurrently (Gustafson's
Law / weak scaling).

### Fallacy: "Higher precision (FP32) is always better"
* **Reality**: Deep learning models are inherently noise-resilient. The excess precision of FP32 is spent modeling
stochastic variance rather than structural signal. Operating in FP32 wastes \(2\times\) memory bandwidth and energy
compared to BF16 without improving final convergence or validation metrics.

---

## D.6 Checkpoint Solutions

### Question 1: Compute and Memory Scaling
A new accelerator doubles compute throughput but keeps memory bandwidth the same. For a workload that is memory-bound on
the current hardware, how much speedup do you expect? What about a compute-bound workload?
* **Solution**:
  * **Memory-Bound Workload**: Expect **\(0\%\) speedup** (or negligible). Because performance is limited strictly by
the memory bus speed, doubling ALU capacity does not resolve the bottleneck of waiting for data.
  * **Compute-Bound Workload**: Expect **up to \(100\%\) speedup (\(2\times\))**. Since the processor is actively
computing rather than waiting for memory, doubling execution units directly halves compute time.

### Question 2: Parallel Limits
Your training pipeline has \(10\%\) serial overhead. Using Amdahl's Law, what is the maximum possible speedup regardless
of how many accelerators you add? Using Gustafson's Law with 256 accelerators, what is the scaled speedup?
* **Solution**:
  * **Amdahl's Law (Strong Scaling)**: Given \(s = 0.10\):
    \[
    \text{Max Speedup} = \lim_{n \to \infty} \frac{1}{s + \frac{1-s}{n}} = \frac{1}{0.10} = 10\times
    \]
  * **Gustafson's Law (Weak Scaling)**: Given \(s = 0.10\) and \(n = 256\):
    \[
    \text{Scaled Speedup}(256) = n - s(n-1) = 256 - 0.10(255) = 256 - 25.5 = 230.5\times
    \]

### Question 3: Little's Law Inference Planning
An inference service must handle \(500\text{ QPS}\) at \(100\text{ ms}\) latency. Using Little's Law, how many
concurrent requests must the system support? If each request needs \(2\text{ GB}\) of KV cache memory, what is the
minimum accelerator memory required?
* **Solution**:
  * **Concurrency (\(N_{\text{req}}\))**:
    \[
    N_{\text{req}} = \lambda \times T_{\text{lat}} = 500\text{ QPS} \times 0.1\text{ s} = 50\text{ concurrent requests}
    \]
  * **Memory Sizing**:
    \[
    \text{Memory Required} = 50\text{ concurrent requests} \times 2\text{ GB/request} = 100\text{ GB}
    \]

---

## Further Reading
* For details on hardware acceleration, see **Chapter 11**.
* For distributed training system design, see **Chapter 8**.
* For inference serving system design, see **Chapter 13**.
* For deep-learning compiler frameworks and custom kernel designs, see **Chapter 7**.

---

## Full Slice Content (Docling Extract, Preserved Verbatim)

> Each section below preserves the source slice content as extracted by docling. Image placeholders are removed; tables,
equations, code blocks, named artifacts, and footnotes are kept intact.

## Purpose

What reference numbers and physical laws should every ML systems engineer carry into design decisions?

This appendix collects the reference numbers and compact models that let you do quick, quantitative reasoning. It begins
with a quick-reference section of 'numbers to know,' then summarizes the tools used throughout the book: roofline
analysis, dimensional analysis, scaling laws, and precision trade-offs.

In ML systems, performance failures often masquerade as software problems: a training step 'mysteriously' slows down, a
serving stack misses its service level agreement (SLA), or an accelerator upgrade fails to deliver the expected speedup.
Many of these surprises are not bugs-they are the predictable consequences of physics (latency, bandwidth, energy) and
architecture (memory hierarchy, precision, parallel scaling).

## How to Use This Appendix

This appendix is designed as a reference. When diagnosing performance issues, use this appendix to translate a vague
symptom ('it's slow') into a specific constraint ('memory bound at batch size one') and then choose the lever that can
actually move. Conventions used here follow the book-wide notation (for example, 𝐵 is reserved for batch size and BW for
bandwidth). · Sanity-check feasibility: Start with Section D.1 for order-of-magnitude numbers.

- Diagnose the dominant ceiling: Use the Roofline Model in Section D.2.1 to decide whether the workload is compute bound
or memory bound.
- Reason about scaling limits: Use Amdahl's and Gustafson's Laws in Section D.2.3 to understand why adding accelerators
may not reduce time-to-train.
- Choose the right precision: Use Section D.4.1 to reason about FP32 vs. BF16/FP16 vs. INT8 as a systems trade-off.
- Cross-reference for depth: When you want the full narrative, jump back to Chapter 11, Chapter 8, and Chapter 13.

## D.1 Numbers to Know

J ust as Jeff Dean's 'Latency Numbers Every Programmer Should Know' 1 shaped a generation of systems engineers, these
reference numbers provide the order-of-magnitude intuition essential for ML systems design. While absolute values evolve
with hardware generations, the ratios betweencategories remain remarkably stable. Memorizetherelationships; use the
specific numbers as sanity checks.

## Key Takeaways: Three numbers that matter most

- The following three numbers are critical to memorize: 1. ~600 × energy ratio: DRAMaccess costs ~581 × more energy than
an FP16 FLOP. This is why arithmetic intensity is everything.

D

1 Jeff Dean: A Google Senior Fellow and one of the architects of Google's distributed systems infrastructure, including MapReduce, BigTable, and TensorFlow. His latency numbers, originally presented with Peter Norvig around 2010, became a canonical reference for systems engineers. The numbers have been updated over the years as hardware evolved, but the hierarchy of latencies remains remarkably stable. See Colin Scott's interactive visualization at https://colin-scott.github.io/ personal\_website/research/ interactive\_latency.html.

2 Energy hierarchy source: Energy numbers from Horowitz's classic 'Computing's Energy Problem' (ISSCC 2014, 45nm
process) (Horowitz 2014). While absolute values scale with process node, the ratios between memory access and compute
remain remarkably stable because wire capacitance (distance) dominates.

3 Training memory (Adam) : The 16 bytes/parameter rule assumes mixedprecision training with Adam. ZeRO optimization can
reduce per-accelerator memory by sharding optimizer states across accelerators, but the total memory across all
accelerators remains ~16 × parameters.

2. 16 bytes/parameter for training: Model weights (2B FP16) + gradients (2B FP16) + master weights (4B FP32) + optimizer
states for Adaptive Moment Estimation (Adam) at 8B. That totals 16 bytes per parameter, so a 7B model needs 112 GB just
to start training.
3. ~200 km/ms speed of light in fiber: Cross-country latency is ~40 ms. No optimization can reduce this-it is physics.

## The invariants: Numbers that will not change

These relationships are governed by physics or arithmetic-they will still be true in 2035.

## Speed of light tax

Table D.1 shows the irreducible latency floor for any distributed system.

Table D.1: Speed of Light Reference: Light in fiber travels ~200 km/ms. These latencies are physics-no optimization can
reduce them.

| Distance           | Round-Trip Latency   | Implication                   |
|--------------------|----------------------|-------------------------------|
| Same data center   | ~1 ms                | Distributed training feasible |
| Cross-country (US) | ~40 ms               | Edge needed for <100 ms apps  |
| Cross-Atlantic     | ~60 ms               | CDNrequired for global users  |
| Cross-Pacific      | ~100 ms              | Data locality is critical     |

## Energy hierarchy

Table D.2 quantifies the energy cost of data movement vs. computation-the fundamental reason why arithmetic intensity
dominates ML performance optimization. 2

Table D.2: The Energy Wall: Moving data costs ~580 more energy than computing on it. This ratio is physics, not
engineering.

×

×

| Relationship                | Ratio    | Why It is Stable                                          |
|-----------------------------|----------|-----------------------------------------------------------|
| DRAMaccess vs. FP16 compute | ~581 × × | Wire capacitance scales with distance                     |
| FP32 vs. INT8 energy        | ~18      | Bit width determines switching energy                     |
| FP32 vs. FP16 energy        | ~3.4 ×   | Narrower arithmetic reduces switching and datapath energy |
| L1 SRAM vs. register        | ~50      | Distance to ALU                                           |

Memory hierarchy Table D.3 shows how each level of the memory hierarchy costs roughly 10-100 × more latency than the one
above it.

Table D.3: The Latency Hierarchy: Each level costs roughly 10-100 more than the one above it.

| Relationship                                  | Ratio              | Why It Persists                   |
|-----------------------------------------------|--------------------|-----------------------------------|
| Accelerator memory (HBM) vs. register         | ~300 slower        | On-chip vs. off-chip              |
| SSD vs. register                              | × ~100000 × slower | Electrical vs. mechanical/flash   |
| Network vs. local memory                      | ~16 slower         | Speed of light + switching        |
| Accelerator memory BWvs. CPU฀Accelerator link | × ~52 faster       | Architectural investment priority |

## Scaling laws

×

Table D.4 collects the arithmetic relationships that govern memory and compute requirements for training and inference.
3

×

Table D.4: Scaling Rules: These are arithmetic, not hardware-specific. Training memory includes FP16 weights (2B), FP16
gradients (2B), FP32 master weights (4B), and Adam optimizer states (8B for momentum + variance).

| Rule                          | Formula                         | Example                        |
|-------------------------------|---------------------------------|--------------------------------|
| Inference memory (FP16)       | 2 bytes × parameters            | 7B params →14 GB               |
| Inference memory (INT8)       | 1 byte parameters               | 7B params→7GB                  |
| Training memory (Adam)        | × 16 bytes parameters           | 7B params →112 GB              |
| Inference FLOPs (transformer) | × ~2 × parameters per token × × | 7B model →~14 GFLOPs/token     |
| Training FLOPs                | ~6 parameters tokens            | 7B on 1T tokens→ 4×10 22 FLOPs |
| Data center vs. edge compute  | ~19                             | Compute per watt power budget  |

## Latency budgets: The nonnegotiables

×

×

These budgets are set by physics (safety) or psychology (human perception)-not by engineering choice. Unlike hardware
specs that improve each generation, these are constraints your system must meet (Table D.5).

Table D.5: Latency Targets: Miss these and the application fails, regardless of accuracy.

| Application        | Budget     | Constraint                           |
|--------------------|------------|--------------------------------------|
| Autonomous braking | <10 ms     | At 100 km/h, 10 ms = 28 cm of travel |
| Voice assistant    | <100 ms    | Human perception of 'instant'        |
| Web search         | <200 ms    | User patience threshold              |
| Video streaming    | <1 s       | Buffer tolerance                     |
| Batch training     | hours-days | Throughput dominates latency         |

## Current hardware reference (c. 2024)

Table D.6 captures the full latency and bandwidth hierarchy for current-generation hardware.

These numbers reflect the current generation. Use them for back-of-envelope calculations, but expect them to improve ~2
× every 2-3 years. Memory latency and bandwidth

Table D.6: Memory Hierarchy (c. 2024) : Specific values for current hardware.

| Level                | Latency    | Bandwidth   |
|----------------------|------------|-------------|
| Register             | ~0.3 ns    | -           |
| L1 Cache             | ~1 ns      | -           |
| L2 Cache             | ~4 ns      | -           |
| GPU HBM3             | ~300 ns    | 3.4 TB/s    |
| PCIe Gen5 (CPU฀GPU)  | ~1000 ns   | 64 GB/s     |
| CPUDRAM              | ~100 ns    | 50 GB/s     |
| InfiniBand (network) | ~5000 ns   | 50 GB/s     |
| NVMe SSD             | ~100000 ns | 7.0 GB/s    |

## Compute throughput

Table D.7 shows the raw throughput available at each tier of the deployment hierarchy.

Table D.7: Compute Reference (c. 2024) : Using the current FP16 and mobile INT8 constants, data-center peak throughput
is about 19 × the mobile reference; exact ratios depend on precision mode and workload. Platform

| Platform               | FP16/BF16   | INT8/FP8-class       | Power   |
|------------------------|-------------|----------------------|---------|
| Data center GPU (H100) | 989 TFLOPS  | 1979 TOPS (FP8 peak) | 700W    |
| Data center GPU (A100) | 312 TFLOPS  | 624 TOPS             | 400W    |
| Mobile NPU             | -           | 50 TOPS              | 3-5W    |

## Roofline ridge points

Table D.8 defines the arithmetic intensity thresholds that determine whether a workload is memory bound or compute
bound.

Table D.8: Arithmetic Intensity Thresholds (c. 2024) : Most inference workloads are <10 ops/byte-firmly memory bound.

| Accelerator   | Ridge Point   | Implication                  |
|---------------|---------------|------------------------------|
| A100 (FP16)   | 153 ops/byte  | Below →memory-bound          |
| H100 (FP16)   | 295 ops/byte  | Higher bar for compute-bound |

## Systems Perspective 20.1: Anote on terminology: GPUs and accelerators

Throughout this book, we often use 'accelerator' when discussing hardware acceleration. However, the principles-roofline
analysis, memory hierarchies, numerical precision, and performance modeling-apply equally to GPUs, Tensor Processing
Units (TPUs) , NPUs, custom ASICs, and other specialized AI accelerators. We use 'accelerator' as the universal term,
but readers should understand these concepts apply to GPUs unless we explicitly discuss vendor-specific features (for
example, CUDA, NVLink).

Knowing the numbers is only the first step. The real power comes from having compact models that tell you which number
matters for your specific bottleneck. The next section provides exactly these diagnostic tools-starting with the
Roofline Model, which translates raw hardware specs into actionable performance ceilings.

## D.2 Physics of Computing

Rawhardware specs-TFLOP/s, TB/s, watt budgets-are necessary but insufficient for performance reasoning. Without compact
analytical models, an engineer cannot distinguish a compute-bound workload from a memory-bound one, or predict whether
doubling GPUs will halve training time. The models in this section provide exactly these diagnostic tools.

## Systems Perspective 20.2: Why this matters

Consider a model that achieves good accuracy, but inference takes 200 ms when the SLA requires 50 ms. Performance
analysis models provide a systematic method to diagnose whether the system is limited by computation, memory bandwidth,
or other factors. Without these models, optimization relies on guesswork.

## D.2.1 The roofline model

The Roofline Model (Williams et al. 2009) answers a deceptively simple question: how fast can this workload possibly run
on this hardware? The answer depends on whether you run out of compute or memory bandwidth first.

Every operation has an arithmetic intensity: the ratio of computations performed to bytes moved from memory. Matrix
multiplication has high arithmetic intensity because each loaded element is reused many times. Element-wise operations
like rectified linear unit (ReLU) have low intensity because each operation loads a number, performs one computation,
and writes it back. As Figure D.1 illustrates, each workload is bounded by either memory bandwidth or compute
throughput, and its arithmetic intensity determines which ceiling it hits first.

Figure D.1: The Roofline Model: Performance ceiling for a hypothetical accelerator. The sloped line represents memory
bandwidth limits; the horizontal line represents peak compute. Every workload can be plotted on this diagram to
determine its optimization strategy.

The ridge point determines the hardware's balance. If a workload's intensity falls below this point, it is memory-bound
(sloped region). If above, it is compute-bound (flat region).

## LIGHTBULB Batch size controls arithmetic intensity

<!-- formula-not-decoded -->

For matrix multiplications, arithmetic intensity scales with the batch dimension. When you compute 𝑌 = 𝑋𝑊 where 𝑋 is
(𝐵×𝐷 in ) and 𝑊 is (𝐷 in ×𝐷 out ) : · FLOPs: 2×𝐵×𝐷 in ×𝐷 out (multiply-adds) · Bytes: Weights are loaded once: 𝐷 in ×𝐷
out × bytes precision Doubling the batch size 𝐵 doubles FLOPs while keeping weight loads constant-directly increasing
arithmetic intensity. This is why inference serving batches requests: batch size 1 is almost always memory bound, while
batch size 64+ can approach the compute ceiling.

## D.2.1.1 Aconcrete example: The A100 analysis

Consider an NVIDIA A100 GPU with FP16 Tensor Core performance of 312 TFLOP/s and HBM2e bandwidth of 2.0 TB/s. The ridge point is 312/2.0 = 153 FLOP/byte (the Tera prefixes cancel, yielding FLOP/byte).

General matrix multiply (GEMM) : For two square matrices of size 4096 by 4096, arithmetic intensity is approximately
1365 FLOP/byte. Since 1365 > 153, this operation is compute bound. You are using the hardware efficiently.

Consider two common operations:

ReLU (Element-wise) : For a square tensor of size 4096 by 4096, intensity is approximately 0.25 op/byte. Since 0.25 ฀
153, this operation is severely memory bound, achieving only about 0.16 percent of peak TFLOP/s. The hardware is mostly
waiting for data.

This explains why modern frameworks fuse operations: combining ReLU with the preceding MatMul avoids writing
intermediate results to memory, effectively increasing arithmetic intensity.

4 Gene Amdahl (1922-2015) : A legendary computer architect at IBM, where he was the chief architect of the System/360.
He later founded Amdahl Corporation to compete with IBM in the mainframe market.

5 John Gustafson: A computer scientist known for his work in parallel computing and for introducing the Unum (universal
number) format. His law was a direct response to the perceived 'limits' of Amdahl's Law when applied to massive scale.

## D.2.2 Dimensional analysis

The Roofline Model helps diagnose where a bottleneck lies. Before applying any performance equation, however, it must be
verified as physically meaningful. Dimensional analysis provides this sanity check: any valid equation must be
dimensionally homogeneous -every term must resolve to the same units. If they do not, the equation contains an error.

Consider the iron law of ML systems (Principle 3) introduced in Section 1.7:

We verify correctness by confirming that every term resolves to Time (seconds) :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The equation is physically consistent. Apply this technique to any systems equation: if the dimensions do not match, the
formula is wrong. 'FLOPs' and 'Bandwidth' cannot be traded directly because they have different units. Any such
trade-off must convert through Time, which is precisely what the iron law quantifies.

- Data Term: Bytes Bytes/s Bytes s Bytes s · Compute Term: FLOPs FLOPs/s = FLOPs × s FLOPs s · Overhead Term: Already in
seconds.

=

The fundamental limits of scaling across multiple devices are the subject of Section D.2.3.

## D.2.3 Amdahl's Law and Gustafson's Law

Parallelization is the primary tool for scaling ML, but its limits depend on how you scale. These two laws frame the
fundamental tension in parallel computing. Amdahl's Law is the pessimist's view, governing how much faster a fi xed task
can run (optimizing latency). Gustafson's Law is the optimist's view, governing how much more work we can do in the same
time (optimizing throughput).

## D.2.3.1 Strong scaling (Amdahl's Law)

Strong scaling answers the question: If I add more processors to a fixed-size problem, how much faster will it run?

As 𝑛 → ∞ , the term 1-𝑠 𝑛 →0, and the speedup converges to 1/𝑠 . To see Amdahl's Law in action, suppose 5 percent of a training step is serial overhead (for example, Python global interpreter lock (GIL), kernel launch latency) and 95 percent is parallelizable matrix math: · With 𝑛 = 1, speedup is 1. · With 8, speedup is 1/(0.05 + 0.95/8) ≈ 5.9 . · With, speedup is capped at 1/0.05 = 20 .

Amdahl's Law (Amdahl 1967) states that the speedup is limited by the serial portion of the task. 4 If a fraction 𝑠 of
your task is serial (cannot be parallelized) and 𝑝 = 1-𝑠 is parallelizable, the maximum speedup with 𝑛 processors is:
Speedup (𝑛) = 1 𝑠+ 1-𝑠 𝑛

𝑛 =

𝑛 → ∞

×

No matter how many accelerators are added, this fixed workload cannot run faster than 20 .

×

×

## D.2.3.2 Weak scaling (Gustafson's Law)

Weak scaling answers the question: If I add more processors, how much larger of a problem can I solve in the same amount
of time?

This is the reality of Large Language Models. Rather than using 1,000 accelerators to train a model on a small dataset
in milliseconds, they are used to train on a dataset 1,000 × larger in reasonable time. Gustafson's Law (Gustafson 1988)
models this 'scaled speedup': 5 Scaled Speedup (𝑛) = 𝑛-𝑠(𝑛-1) Here, the parallel part of the workload grows linearly
with 𝑛, while the serial part 𝑠 remains fixed. Using the same 5 percent serial overhead ( 𝑠 = 0.05), Gustafson's Law
tells a very different story: · With 𝑛 = 1, speedup is 1. · With 𝑛 = 8, Scaled Speedup is 8 -0.05 × (7) = 8 - 0.35 =
7.65 × . · With 𝑛 = 1000, Scaled Speedup is 1000 -0.05 × (999) ≈ 950 × . In weak scaling, efficiency remains high
because the useful work (training the model) scales up to dwarf the fixed overheads.

## Napkin Math 20.1: The training time equation

<!-- formula-not-decoded -->

Just as classical architecture has an 'iron law' of performance, Large Language Model training has a fundamental
governing equation. To estimate training time 𝑇:

- Where: · 6: The factor deriving from the forward pass ( 2𝑃𝐷 ) and backward pass ( 4𝑃𝐷 ) FLOPs per token. · 𝑃: Number
of model parameters. · 𝐷: Number of training tokens. · 𝑁: Number of accelerators (GPUs). · 𝑋: Peak FLOP/s of one
accelerator. · 𝑈: Model FLOPs Utilization (MFU), typically 30 percent-50 percent. Example: Training a 1B parameter model
on 20B tokens using 1 A100 (312 TFLOPS) at 40 percent utilization . Total FLOPs =6×1×10 9 ×2×10 10 =1.2×10 20 FLOPs
Throughput = 1×(3×10 14 )×0.40 ≈ 1.25×10 14 FLOP/s 𝑇 = 1.2×10 20 1.25×10 14 ≈961,538 seconds ≈16,026 minutes The
computed result: 961538 seconds (≈ 16026 minutes, or about 11 days).

## Checkpoint 20.1: Check your understanding: Performance models

1. Anew accelerator doubles compute throughput but keeps memory bandwidth the same. For a workload that is memory-bound
on the current hardware, how much speedup do you expect? What about a compute-bound workload?
2. Your training pipeline has 10 percent serial overhead. Using Amdahl's Law, what is the maximum possible speedup
regardless of how many accelerators you add? Using Gustafson's Law with 256 accelerators, what is the scaled speedup?
3. An inference service must handle 500 queries per second (QPS) at 100 ms latency. Using Little's Law, how many
concurrent requests must the system support? If each request needs 2 GB of KV cache memory, what is the minimum
accelerator memory required?

6 John Little: An Institute Professor at MIT and a pioneer in the field of operations research. His law, proved in 1961,
is fundamental to queuing theory and is used across fields from manufacturing to computer network analysis.

D.2.4 Little's Law For capacity planning in inference systems, Little's Law (Little 1961) relates concurrency ( 𝑁 req ),
arrival rate ( 𝜆 ), and latency ( 𝑇 lat ): 6 𝑁 req =𝜆×𝑇 lat To see this in practice, consider sustaining 1,000 queries
per second (QPS) with 50 ms average latency. The law tells us the system must support 1000 × 0.05 = 50 concurrent
requests. This directly determines how to size inference worker pools. If serving one request requires 1 GB of temporary
memory (KV cache, activations), handling 50 concurrent requests requires 50 GB of memory. If the accelerator only has 24
GB, the system is physically limited to 24 concurrent requests. Maximum throughput is capped at 𝐿/𝑊 = 24/0.05 = 480 QPS,
regardless of how many requests arrive.

These physics-based models-Roofline, Amdahl, Gustafson, and Little-diagnose where bottlenecks lie. Translating those
diagnoses into actionable optimizations, however, requires understanding the concrete hardware structures that impose
them: caches, memory buses, and interconnects.

## D.3 Computer Architecture Essentials

AGPUadvertises 1,000 TFLOP/s, yet your kernel achieves only 30 TFLOP/s. The missing 97 percent is not a software bug-it
is the cost of moving data through a memory hierarchy that spans five orders of magnitude in latency. While physics sets
theoretical performance bounds, computer architecture defines the machinery that determines how close a real workload
can get. The following discussion covers the latency, bandwidth, and energy trade-offs that shape system design.

## D.3.1 Latencies every programmer should know

The first step in systems intuition is understanding the cost of distance. Table D.9 quantifies how long the processor
waits for data from different levels of the memory hierarchy. If accessing a register is like picking up a pencil from
your desk, fetching from HBM is walking across the office, and fetching from disk is flying to the moon.

Table D.9: The Latency Hierarchy: Access times for modern AI hardware. Note the massive jump from SRAM (Cache) to HBM.
Any kernel that misses cache pays a heavy penalty.

| Component            | Latency (ns)   | Cycles (Approx)   | Relative 'Distance'   |
|----------------------|----------------|-------------------|-----------------------|
| Register             | ~0.3 ns        | 1 cycle           | 10 seconds            |
| L1 Cache             | ~1 ns          | 3-4 cycles        | 1 minute              |
| L2 Cache             | ~4 ns          | 12 cycles         | 4 minutes             |
| HBM3 (GPU Memory)    | ~300 ns        | 1,000 cycles      | 5 hours               |
| NVLink (GPU-GPU)     | ~500 ns        | 1,500 cycles      | 8 hours               |
| PCIe (CPU-GPU)       | ~1000 ns       | 3,000 cycles      | 1 day                 |
| InfiniBand (Network) | ~5000 ns       | 15,000 cycles     | 1 week                |
| SSD (NVMe)           | ~100000 ns     | 300,000 cycles    | 3 months              |

## D.3.2 The AI hardware cheat sheet (modern reference)

While latency tells us how long we wait for the fi rst byte, bandwidth tells us how many bytes follow. Table D.10
provides the constants for back-of-the-envelope 'Roofline' calculations. These represent the 'standard units of compute'
for the current era of machine learning.

Table D.10: Reference Specs: Key constants for quantitative analysis. Always check specific datasheets, but these serve
as standard units of compute.

𝑅

| Spec           | NVIDIA H100 (SXM)   | Google TPU v5p   | System Impact              |
|----------------|---------------------|------------------|----------------------------|
| FP16/BF16 Peak | 989 TFLOPS          | 459 TFLOPS       | The 'Speed Limit' ( peak ) |

| Spec             | NVIDIA H100 (SXM)   | Google TPU v5p                           | System Impact                        |
|------------------|---------------------|------------------------------------------|--------------------------------------|
| Memory Bandwidth | 3.35 TB/s           | 2.76 TB/s                                | The 'Width of the Pipe' (BW) 𝑃       |
| HBMCapacity      | 80 GB               | 95 GB                                    | Max Model Size ( )/Batch Size ( 𝐵 )  |
| L2/SRAM Cache    | 50MB                | ~100MB                                   | Critical for Operator Fusion         |
| Interconnect     | 900 GB/s (NVLink)   | 1200 GB/s (Inter-Chip Interconnect, ICI) | Determines Model Parallelism Scaling |

## D.3.3 The memory hierarchy

Computer systems use a hierarchy because no single technology provides both high capacity and low latency. Examine the
pyramid in Figure D.2 to see how each level balances this trade-off: every technique that keeps data higher in the
pyramid (registers/cache) directly improves performance.

The memory hierarchy is the fundamental physical constraint of machine learning systems. Table D.11 consolidates the
physical properties-latency, bandwidth, and energy-across the entire stack.

Figure D.2: The Memory Hierarchy: Performance depends on data proximity. Accessing HBM is roughly 1,000 × slower than
registers; accessing SSD is roughly 300,000 × slower.

Table D.11: Physical Properties of the Memory Hierarchy (c. 2024) : Consolidating latency, bandwidth, and energy across
the memory hierarchy. The hierarchy spans five orders of magnitude in latency and six orders of magnitude in energy per
access. For the ML engineer, this table defines the 'silicon contract': every optimization that moves data one layer
higher in the hierarchy delivers an order-of-magnitude dividend in performance.

| Layer            | Technology    | Latency    | Bandwidth   | Energy (per 32b)   |
|------------------|---------------|------------|-------------|--------------------|
| Registers        | Flip-Flops    | ~0.3 ns    | -           | 0.01 pJ            |
| L1 Cache         | SRAM          | ~1 ns      | -           | 0.5 pJ             |
| L2 Cache         | SRAM          | ~4 ns      | -           | 2.0 pJ             |
| Memory (Local)   | HBM3          | ~300 ns    | 3,350 GB/s  | 640 pJ             |
| Interconnect     | NVLink 4.0    | ~500 ns    | 900 GB/s    | ~640 pJ            |
| Host Link        | PCIe Gen5     | ~1000 ns   | 64 GB/s     | ~640 pJ            |
| SystemRAM        | DDR5          | ~100 ns    | 50 GB/s     | ~640 pJ            |
| Network (Fabric) | InfiniBandNDR | ~5000 ns   | 50 GB/s     | ~10,000 pJ         |
| Storage (Local)  | NVMe SSD      | ~100000 ns | 7.0 GB/s    | ~5,000 pJ          |

The hierarchy's energy costs reveal why data movement dominates modern system design.

Napkin Math 20.2: The high cost of data movement Fetching a 32-bit value from DRAM costs roughly 581 × moreenergy than
performing a floatingpoint operation on it (for example, ~640 pJ vs. ~1 pJ). This energy wall means that maximizing
arithmetic intensity (doing many ops per loaded byte) is the only way to be energy efficient.

## D.3.4 Bandwidth vs. latency

Bandwidth (throughput) and latency (delay) are distinct constraints. Total transfer time follows:

For small transfers (for example, single-token inference), latency dominates. For large transfers (for example, loading
weights), bandwidth dominates.

<!-- formula-not-decoded -->

Consider sending data over a 10 Gbps link with 10 ms ping (latency). The dominant bottleneck depends entirely on the
transfer size:

- Latency-Bound (1 KB Packet) :
- -Transmission: 1 KB/10 Gbps ≈ 0.8 μs.
- -Total Time ≈ 10 ms + 0.8 μs ≈ 10 ms.
- -Result: The bandwidth is irrelevant; the speed of light (ping) is the bottleneck.

## · Bandwidth-Bound (1 GB Checkpoint) :

- -Transmission: GB Gbps ms.
- -Total Time ms ms ms.
- -Result: The ping is negligible; the pipe size is the bottleneck.

1

/10

≈800

Architecture determines how fast data can move, but there is another lever that directly controls how much data must
move: the numerical precision of each value. Halving precision from FP32 to FP16 halves the bytes per parameter, which
doubles effective bandwidth for free-if the model can tolerate the reduced precision. Understanding these trade-offs
requires a closer look at how numbers are represented in hardware.

≈10

+800

=810

## D.4 Numerical Representations

While statistics helps us understand data distributions, numerical representations determine how we store the values
themselves. In ML systems, the choice of precision (FP32 vs. BF16 vs. INT8) is a direct trade-off between statistical
fidelity and hardware throughput.

## Systems Perspective 20.3: Why this matters

Aproduction model might run at 50 QPS in FP32 when the target is 200 QPS. Switching to INT8 could achieve this
throughput, but accuracy may suffer. Understanding numerical formats enables a quantitative evaluation of this
trade-off.

## D.4.1 Floating-point format comparison

IEEE 754 formats such as FP32 and FP16, together with AI-specific formats such as BF16 and FP8, define different
trade-offs between dynamic range (the span of representable values) and precision (the granularity of values within that
range). Table D.12 summarizes the key formats and their use cases, while Figure D.3 visualizes the bit allocations.

Table D.12: Numerical Format Comparison: Each format trades off precision, dynamic range, memory footprint, and compute
throughput. BF16 has emerged as the preferred training format because it matches FP32's range while using half the
memory.

| Format   |   Bits | Exponent   | Mantissa   | Dynamic Range       | Typical Use Case                               |
|----------|--------|------------|------------|---------------------|------------------------------------------------|
| FP32     |     32 | 8          | 23         | ∼10 -38 to 10 38 -5 | Training (full precision), reference inference |
| FP16     |     16 | 5          | 10         | ∼10 to 6.5×10 4     | Training with loss scaling, inference          |
| BF16     |     16 | 8          | 7          | Same as FP32        | Training (preferred), avoids loss scaling      |
| FP8      |      8 | 4 or 5     | 3 or 2     | Varies              | Inference on newest hardware (H100+)           |
| INT8     |      8 | N/A        | N/A        | -128 to 127         | Inference after quantization                   |

Figure D.3: Numerical Format Bit Layouts: Avisual comparison of bit allocations. Note how BF16 (Brain Float 16)
preserves the 8-bit exponent of FP32, ensuring the same dynamic range for training stability. FP16 trades range for
precision, often requiring loss scaling to prevent underflow.

Beyond bit width, the allocation of bits between exponent and mantissa determines what range of values each format can
represent.

## Systems Perspective 20.4: The dynamic range wall

The choice of numerical format is a direct application of the iron law of ML systems (Principle 3). Reducing precision
from FP32 to BF16 or FP16 halves the Data Movement term in the denominator, potentially doubling throughput on
memory-bound workloads. However, the type of 16-bit format determines the engineering complexity:

- Dynamic Range (The Exponent) : BF16 preserves the eight-bit exponent of FP32. This means it can represent the same
range of extremely large and extremely small values (gradients).
- Precision (The Mantissa) : FP16 has a larger 10-bit mantissa than BF16 (7 bits), offering higher precision for values
within its range. Its five-bit exponent, however, is a major constraint; gradients often 'vanish' to zero (underflow)
because the exponent cannot represent them. To solve this, FP16 training requires Loss Scaling, an operational overhead
where gradients are multiplied by a large constant to push them into the representable range.
- Energy Efficiency: INT8 operations are significantly more energy-efficient than floatingpoint equivalents because they
use simpler integer ALUs and require less silicon area. Moving to INT8 for inference is the primary lever for deploying
large language models (LLMs) on battery-constrained edge devices.

Among these formats, BF16 7 deserves special attention (Cloud 2019). By matching FP32's eightbit exponent while
truncating the mantissa to just 7 bits, BF16 preserves the full dynamic range needed for gradient representation. This
avoids the underflow problems that plague FP16 training, eliminating the need for complex loss scaling. Most modern
training uses BF16 for this reason-it is effectively a 'drop-in' half-precision replacement for FP32 that just works.

## D.4.2 Integer quantization

Quantization maps continuous floating-point values to discrete integers, typically INT8. The key challenge is choosing
how to map the floating-point range to integers. Two approaches dominate. Symmetric quantization centers the mapping at
zero: 𝑥 int = round ( 𝑥 𝛼 ×127) where 𝛼 is the scale factor (typically the maximum absolute value). This works well for
weight distributions centered around zero.

Withthefull toolkit assembled-reference numbers, performance models, architectural constraints, and numerical
trade-offs-the next section catalogs the most common ways engineers misapply these concepts. The following section
catalogs fallacies and pitfalls that violate the physical and architectural principles covered earlier.

Asymmetric quantization handles distributions that are not centered (common after ReLU, which produces only nonnegative
values) by shifting the range before scaling. If 𝑥 min is the minimum of the range and 𝛼 is the range width ( 𝑥 max -𝑥
min ): 𝑥 int = round ( 𝑥-𝑥 min 𝛼 ×255) The choice between symmetric and asymmetric quantization depends on your tensor's
distribution and has measurable accuracy implications.

## D.5 Fallacies and Pitfalls

Even experienced engineers fall into traps when reasoning about hardware performance. The following misconceptions
violate the physical and architectural principles covered in this appendix.

Exclamation-Triangle Fallacy: Doubling accelerators halves training time

Arelated misconception concerns numerical precision.

This assumes perfect strong scaling (Amdahl's Law). In practice, communication overhead (all-reduce) grows with 𝑁, and
batch size constraints may limit parallelism. At large scale, you often hit diminishing returns unless you also scale
the problem size (weak scaling).

Fallacy: Higher precision (FP32) is always better

With the common misconceptions addressed, use the reference numbers and models in this appendix as your first line of
defense whenever a system behaves unexpectedly. A quick back-ofenvelope calculation often reveals whether the culprit is
physics, architecture, or a genuine software bug.

For deep learning, FP32 often hurts performance without improving convergence. It consumes 2 × memory bandwidth and
energy compared to BF16. Since neural networks are resilient to noise, the extra mantissa bits in FP32 are often
modeling random variance rather than signal.

- Key Takeaways: Numbers every engineer should know · Energy dominates: Moving data costs ~600 × more energy than
computing on it. Arithmetic intensity-the ratio of compute to data movement-is the single most important metric for ML
workload performance.

- The Roofline Model reveals whether a workload is compute bound or memory bound. Most inference workloads fall below
the ridge point and are memory bound; batch size is the primary lever to shift toward compute-bound operation.
- Memory hierarchy spans five orders of magnitude in latency (register at ~0.3 ns to SSD at ~100,000 ns). Keeping data
close to compute is not an optimization-it is the optimization.
- Amdahl's Law caps strong-scaling speedup at 1/𝑠 (where 𝑠 is the serial fraction). Gustafson's Law shows that scaling
the problem alongside hardware yields near-linear throughput gains-the paradigm that makes large-scale training
feasible. · Little's Law ( 𝑁 req =𝜆𝑇 lat ) directly sizes inference infrastructure: concurrency, memory, and maximum
throughput are all linked by this simple identity.
- Physics is nonnegotiable: Speed of light sets latency floors, energy ratios set efficiency ceilings, and no amount of
software optimization can violate these constraints.
- Numerical precision is a systems lever, not just a modeling choice. BF16 matches FP32's dynamic range at half the
memory cost; INT8 quantization can deliver 2-4 × inference speedup with careful calibration.

## Further Reading

- Hardware acceleration: Chapter 11
- Training system design: Chapter 8
- Serving system design: Chapter 13
- Framework internals and kernels: Chapter 7
