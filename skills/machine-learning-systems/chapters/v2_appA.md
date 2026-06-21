# Appendix A: Single-Machine Foundations — The D·A·M Taxonomy (Vol 2)

The **D·A·M (Data, Algorithm, Machine)** taxonomy is the diagnostic baseline for every ML systems analysis. Before
scaling to distributed fleets, before purchasing new hardware, before restructuring training pipelines—identify which of
these three axes is the binding constraint. Optimization effort directed at a non-bottleneck axis yields minimal
improvement and poor cost efficiency.

This appendix provides a compact reference for single-machine performance analysis, from arithmetic intensity theory to
bottleneck diagnostic tooling. It is the single-machine foundation for the fleet-scale **C³ Taxonomy** presented in
Appendix E.

---

---

## Section-by-Section Preserve-and-Extend

## Single-Machine Foundations (D·A·M)

## Purpose

Before engineering the fleet, we must master the single machine. Where do you look first when a single node fails: the
data path, the algorithm, or the machine?

This appendix provides a compact diagnostic frameworkData·Algorithm·Machine(D·A·M) -and shows how to map single-machine
symptoms and measurements to the term of the iron law that dominates. It serves as a foundational checklist before
fleet-scale optimization.

In production, 'it is slow' and 'it is wrong' are rarely informative symptoms. A serving stack can miss its latency
Service Level Objective (SLO) because the GPU is idle (data starvation), because the model is doing unnecessary work
(algorithmic overhead), or because the accelerator is genuinely saturated (machine-bound). The 𝐶 3 Taxonomy (Appendix E)
extends these diagnostics to the distributed fleet, but it relies on a firm foundation of single-node performance.
Without understanding the D·A·M taxonomy, teams often optimize the wrong thing-buying faster GPUs to fix a slow input
pipeline, or rewriting kernels when the model is simply too large for the latency budget.

## How to Use This Appendix

This appendix is designed as a reference for single-node performance. Start with the scorecard-style metrics, form a
hypothesis about which axis dominates, and then pick the tool that can confirm (or falsify) that hypothesis.

When training is slow on a single GPU, check utilization, data wait time, and MFU, then map each to its Data, Algorithm,
or Machine axis. When serving misses a latency target, identify whether the regime is latency-bound (overhead),
memory-bound (weight/KV movement), or compute-bound. When cost is exploding, use the D·A·M rubric to ensure that effort
targets the dominant term, not a nonbottleneck.

<!-- image -->

## Learning Objectives

- Classify single-machine bottlenecks by dominant Data, Algorithm, or Machine axis while recognizing mixed causes
- Map optimization techniques to their D·A·M intersection zone to understand which axes they span
- Apply the iron law equation to quantitatively diagnose performance problems
- Distinguish between memory-bound and compute-bound workloads using Arithmetic Intensity
- Select appropriate profiling tools and optimization strategies for each D·A·M axis
- Evaluate system health using the D·A·M Scorecard metrics (I/O Overhead, Active Params, MFU)

The Data · Algorithm · Machine (D·A·M) taxonomy is the primary diagnostic framework for ML systems engineering. It
formalizes the interdependence between information flow, mathematical

<!-- image -->

A

1 MECE (Mutually Exclusive, Collectively Exhaustive) : A classification principle from management consulting
(popularized by McKinsey) requiring that categories do not overlap and together cover every possibility. Applied to
systems engineering, it is useful as an idealized decomposition, but D·A·M bottlenecks often overlap in practice: a
kernel can be simultaneously memory-bound, synchronization-heavy, and poorly matched to available hardware.

2 Arithmetic Intensity: The ratio of floating-point operations to bytes transferred (FLOPs/byte). It determines whether
a workload is memory-bound or computebound by comparison against the hardware's ridge point ( 𝑅 peak / BW).

logic, and physical execution. When performance stalls or behavior degrades, ask: where is the flow blocked? This
taxonomy helps practitioners decompose bottlenecks across three diagnostic axes 1, while recognizing that real systems
can involve mixed causes or interactions between axes.

## A.1 Diagnostic Summary

T he taxonomy maps directly to the Iron Law of ML Systems, introduced in Section 1.5.2. Table A.1 summarizes the role,
primary physical constraint, and core optimization pathway for each axis.

Table A.1: D·A·M Axis Reference: Each axis maps to a distinct physical constraint and a high-leverage optimization
strategy. Start diagnosis here: identify which constraint is binding, then follow the optimization lever.

| Axis          | Role                   | Physical Constraint   | High-Leverage Optimization   |
|---------------|------------------------|-----------------------|------------------------------|
| Data (D)      | Information (The Fuel) | Bandwidth (BW)        | I/O Pipeline Optimization    |
| Algorithm (A) | Logic (The Blueprint)  | Operations ( )        | Model Compression            |
| Machine (M)   | Physics (The Engine)   | 𝑂 Throughput ( peak ) | Hardware Acceleration        |

## A.2 Iron Law Mapping

𝑅

The performance of any ML task is governed by the distribution of work across the D·A·M axes. The iron law mapping
reveals which component's variables dominate the execution time:

Algorithm and Machine share the compute term and are separated by which variable the engineer controls. Reducing the
total operations ( 𝑂 ) is an Algorithm lever, while improving the hardware's peak throughput ( 𝑅 peak ) or utilization (
𝜂 hw ) is a Machine lever. A.2.1 D·A·M coordination: From sum to max

\[ T_{\text{pipelined}} = \max\left(\frac{D_{\text{vol}}}{\text{BW}},\;\frac{O}{R_{\text{peak}}\cdot\eta_{\text{hw}}}\right) + L_{\text{lat}} \]

The additive iron law represents sequential execution -the worst case where Data, Algorithm, and Machine take turns.
Skilled systems engineering transforms the sum into a max:

The systems engineer's job is to make these components run in parallel, not in series. Table A.2 summarizes key D·A·M
Coordination techniques:

\[
\max\left(\frac{D_{\text{vol}}}{\text{BW}}, \frac{O}{R_{\text{peak}} \eta_{\text{hw}}}\right) + L_{\text{lat}}
\]

Table A.2: D·A·M Overlap Techniques: Each technique allows one D·A·M axis to execute while another is in flight,
converting the iron law's additive terms into overlapped terms.

| Technique           | D·A·M Axes Overlapped      | Implementation                                                                                  |
|---------------------|----------------------------|-------------------------------------------------------------------------------------------------|
| Prefetching         | DoverlapsM                 | DataLoader with prefetch_factor, pin_memory=True                                               |
| CUDAStreams         | DoverlapsM                 | Separate streams for H2D transfer and compute                                                   |
| Async Gradient Sync | M(communication) overlapsA | Overlap gradient AllReduce with remaining backward computation as gradient buckets become ready |
| Double Buffering    | DoverlapsM                 | Fill buffer N+1 while computing on bufferN                                                      |

## A.3 Arithmetic Intensity Boundary

- If arithmetic intensity is below the ridge point (about 295 FLOPs/byte on H100): The workload is likely memory bound
(Data/Machine boundary).
- The boundary between Data (memory bound) and Machine (compute bound) is not arbitrary; it is defined mathematically by
Arithmetic Intensity 2 ( 𝐼 ) of the workload. · If GPU utilization < 80 percent: The workload is likely data bound (or
CPU bound). The accelerator is starving. · If GPU utilization > 95 percent: The workload is likely machine bound. The
accelerator is fully saturated. · If batch size is 1: The workload is likely latency bound (algorithm overhead
dominates).

## A.3.1 Bottleneck diagnostic

Once the bottleneck is identified, Table A.3 shows which optimizations help and which ones are wasted:

Table A.3: What Works vs. What Is Wasted: Optimizing the wrong term yields limited improvement and poor cost efficiency.
Amemory-bound model will not speed up from more peak FLOP/s alone; it needs higher arithmetic intensity, less data
movement, or a faster memory subsystem.

| If the workload is…   | Dominant Term       | Optimization That Works                                                 | Optimization That is Wasted                        |
|-----------------------|---------------------|-------------------------------------------------------------------------|----------------------------------------------------|
| Memory- Bound         | 𝐷 vol / BW          | Quantization, pruning, batching, kernel fusion, higher memory bandwidth | More peak FLOP/s alone                             |
| Compute- Bound        | 𝑂/(𝑅 peak ⋅𝜂 hw ) 𝐿 | Better kernels, Tensor Cores, faster GPU, lower precision               | More memory bandwidth (already saturated)          |
| Latency-Bound         | lat                 | Batching requests, kernel fusion, async dispatch                        | Neither compute nor bandwidth (overhead dominates) |

## A.4 Tooling Map

Use Table A.4 to select the right profiling tool when diagnosing a bottleneck along a particular D·A·M axis:

Table A.4: D·A·M Tooling Map: Profiling utilities for diagnosing bottlenecks along each D·A·M axis.

| Axis      | Key Metric                    | Primary Tool          | Secondary Tool                 |
|-----------|-------------------------------|-----------------------|--------------------------------|
| Data      | Batch Load Time               | tqdm (iterations/sec) | iotop, dstat (Disk I/O)       |
| Algorithm | FLOPs, Model Depth            | PyTorch Profiler      | DeepSpeed Flops Profiler       |
| Machine   | GPU Utilization, SM Occupancy | nvidia-smi            | Nsight Compute, Nsight Systems |

## A.5 D·A·M Scorecard

The efficiency ratios in Table A.5 grade a system's performance against its theoretical limit. This 'Report Card' is
anchored by MFU 3 -theratio of achieved model FLOPs to the hardware's theoretical peak FLOPs.

Table A.5: The D·A·M Efficiency Rubric: Use these three numbers to characterize single-machine maturity.

Peak FLOPs

<

>

| Axis        | Metric                       | Definition                                               | Failing Grade       | Passing Grade         |
|-------------|------------------------------|----------------------------------------------------------|---------------------|-----------------------|
| Data        | I/O Overhead                 | Data Wait Time Total Step Time                           | > 10 percent        | 1 percent             |
| Algo- rithm | Compression/Spar- sity Ratio | Effective or active parameters Dense baseline parameters | Workload- dependent | < Workload- dependent |
| Machine     | MFU                          | Achieved FLOPs                                           | 30 percent          | 50 percent            |

3 MFU (Model FLOPs Utilization) : Measures only useful model computation, excluding overhead like gradient
synchronization and memory management.

| Axis   | Metric   | Definition   | Failing Grade   | Passing Grade   |
|--------|----------|--------------|-----------------|-----------------|

## A.6 Scaling the Taxonomy: From Node to Fleet

The D·A·M taxonomy is the diagnostic baseline for a single machine. However, as we move from a single node to the
Machine Learning Fleet, each axis undergoes a qualitative transformation. Understanding these 'tie-ins' is essential for
transitioning from local optimization to fleet-scale engineering.

## The evolution of constraints

| Axis          | Node-Level Focus (D·A·M)   | Fleet-Scale Transformation                                                                                                  |
|---------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Data (D)      | I/O Bandwidth (Disk/PCIe)  | The communication wall: The bottleneck shifts from local storage to the Bisection Bandwidth of the network fabric.         |
| Algorithm (A) | Model Depth/Ops Count      | The parallelism strategy: The logic now includes how we partition the math across 𝑁 devices (3D Parallelism).              |
| Machine (M)   | Peak TFLOPS/HBM            | The power and reliability wall: The constraint is no longer just silicon speed, but Watts per rack and cluster-wide MTBF . |

1. Computation ( 𝐶 1 ) inherits the Algorithm and Machine axes, but adds the loss of Scaling Efficiency .

(M) Bridging to 𝐶 3 While D·A·M diagnoses the components of a single node, the 𝐶 3 Taxonomy (Appendix E) diagnoses the
interactions of the fleet.

3. Coordination ( 𝐶 3 ) is the 'at scale' tie-in that has no single-node equivalent. It represents the Coordination Tax
-the time spent on synchronization, checkpoints, and failure recovery that only emerges at fleet scale.
2. Communication ( 𝐶 2 ) inherits the Data axis, but is governed by the speed of light and network topology rather than
just local I/O.

This progression ensures that single-node efficiency (high MFU) is never traded off for fleet-scale inefficiency (low
scaling efficiency). We optimize the node to serve the fleet.

## A.7 Summary

The D·A·M taxonomy provides the diagnostic baseline for every ML systems analysis. By isolating the bottleneck to Data,
Algorithm, or Machine, practitioners ensure that optimization efforts target the binding constraint. This single-node
discipline is the prerequisite for the fleet-scale engineering addressed in the rest of this volume.

## Key Takeaways: Single-machine diagnostic heuristics

- Identify the dominant axis (Data, Algorithm, or Machine) before proposing any optimization.
- Profile Arithmetic Intensity to quantitatively distinguish between Data-bound and Machine-bound regimes.
- Use the iron law to transform vague symptoms into specific term-based bottlenecks.
- Grade with the D·A·M Scorecard to standardize 'good' performance before moving to fleet scale.

