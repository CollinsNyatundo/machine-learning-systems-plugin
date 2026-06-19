# Appendix E: The C³ Taxonomy — Fleet-Scale Bottleneck Diagnosis (Vol 2)

The **C³ (Computation, Communication, Coordination)** taxonomy is the diagnostic framework for identifying, isolating,
and optimizing bottlenecks in distributed machine learning fleets. Where the single-machine **D·A·M taxonomy** (Appendix
A) diagnoses bottlenecks within a single node—data starvation, algorithmic overhead, hardware saturation—the C³ taxonomy
diagnoses bottlenecks *across* the distributed fleet.

**The core diagnostic question:** When the fleet is slow, where do you look first—Computation, Communication, or
Coordination?

In a distributed training cluster, "it is slow" is even less informative than on a single machine. A 4,096-GPU job can
miss its throughput target because individual accelerators are underutilized (**Computation**), because gradient
synchronization saturates the network fabric (**Communication**), or because checkpoint overhead and failure recovery
consume too much wall-clock time (**Coordination**). Without a taxonomy, teams buy more GPUs when they should be
upgrading interconnects, or optimize kernels when the real problem is pipeline bubble overhead.

---

---

## Section-by-Section Preserve-and-Extend

## The C 3 Taxonomy Purpose

In a distributed training cluster, 'it is slow' is even less informative than on a single machine. A4,096-GPU job can
miss its throughput target because individual accelerators are underutilized (computation), because gradient
synchronization saturates the network fabric (communication), or because checkpoint overhead and failure recovery
consume too much wall-clock time (coordination). Without a taxonomy, teams buy more GPUs when they should be upgrading
interconnects, or optimize kernels when the real problem is pipeline bubble overhead.

When the fleet is slow, where do you look first: Computation, Communication, or Coordination?

This appendix provides a compact diagnostic frameworkComputation, Communication, Coordination (C 3 ) -and shows how to
map fleet-scale symptoms and measurements to the term of the Fleet Law that dominates. It is the fleet-scale extension
of the Single-Machine Foundations (Appendix A), projecting the same diagnostic philosophy from a single machine to the
distributed fleet. It serves as a 'first response' checklist before committing to deeper fleet-scale optimization.

## How to Use This Appendix

When training throughput is low, check MFU, communication fraction, and goodput ratio, then map each to its Computation,
Communication, or Coordination axis. When scaling efficiency drops below expectations, use the Fleet Law decomposition
to identify which term grew. When cost is exploding, use the C 3 scorecard to ensure that effort targets the dominant
term, not a nonbottleneck.

This appendix is designed as a reference. Start with the diagnostic summary table, form a hypothesis about which C 3
axis dominates, and then pick the tool that can confirm (or falsify) that hypothesis.

The C 3 Taxonomy is the diagnostic framework for fleet-scale ML systems engineering. Where the Single-Machine
Foundations (Appendix A) diagnose bottlenecks within a single node-data starvation, algorithmic overhead, or hardware
saturation-the C 3 taxonomy diagnoses bottlenecks across the distributed fleet. Most fleet-scale performance problems
can be diagnosed by identifying the dominant axis: Computation (are the accelerators doing useful math?), Communication
(is the network moving data fast enough?), or Coordination (is the system spending too much time on synchronization,
failure recovery, and scheduling?). Many production bottlenecks sit at intersections between these axes. E.1 From D·A·M
to C 3 T he C 3 taxonomy does not replace D·A·M-it extends it. When a workload moves from one machine to a fleet, each
D·A·M axis acquires new failure modes that the single-machine framework cannot capture. Table E.1 shows how the
transition works.

Table E.1: D·A·M to C 3 Mapping: Each D·A·M axis maps to a C 3 counterpart, but Coordination ( 𝐶 3 ) is genuinely new-it
captures overhead that is negligible on a single machine but can consume 40 percent of wall-clock time at fleet scale.


| D·A·M Axis      | Single-Machine Concern        | C 3 Extension           | What Changes at Fleet Scale                                                                                    |
|-----------------|-------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------|
| Data (D)        | I/O bandwidth, disk to GPU    | Communica- tion ( 𝐶 2 ) | Data moves across network, not just memory hierarchy                                                           |
| Algorithm (A)   | FLOPs, model depth, ops count | Computation ( 𝐶 1 )     | Per-GPU utilization (MFU) still matters, but scaling efficiency erodes it 𝑁×                                   |
| Machine (M)     | Peak FLOPS, hardware limits 𝐿 | Computation ( 𝐶 1 )     | Fleet peak = single-GPU peak, but compound losses reduce effective FLOPS                                       |
| (no equivalent) | (overhead term lat )          | Coordination ( )        | New axis: barriers, checkpoints, failure recovery, scheduling-negligible on one machine, dominant at 10K+ GPUs |

𝐶

The most important row in Table E.1 is the last one. On a single machine, the overhead term ( 𝐿 lat ) in the iron law is
typically small-kernel launch latency, Python dispatch, synchronization barriers. At fleet scale, Coordination becomes
an axis in its own right: checkpoint writes, failure detection and recovery, pipeline bubble overhead, scheduler
preemptions, and maintenance windows collectively consume a significant fraction of wall time. Coordination is the axis
that this book exists to address.

E.2 Diagnostic Summary Table E.2 provides the main reference table for fleet-scale diagnosis. Each C 3 axis maps to a
physical constraint, observable symptoms, measurable metrics, and engineering levers.

Table E.2: C 3 Diagnostic Summary: Each axis maps to a distinct physical constraint and a high-leverage optimization
strategy. Start diagnosis here: identify which constraint binds, then follow the optimization pointer to the relevant
chapter. C 3 Axis


| C Axis                    | Physical Constraint                           | Symptoms                                                                        | Key Metric                                                                       | High-Leverage Optimization                                                             |
|---------------------------|-----------------------------------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Com- puta- tion ( 𝐶 1 )   | Arithmetic throughput ( 𝑅 peak ×𝜂 hw )        | Low MFU, GPU utilization below 80 percent, poor per-GPU performance             | MFU(Model FLOPS Utilization)                                                     | Kernel optimization, mixed precision, operator fusion (Chapter 10)                     |
| Com- muni- cation ( 𝐶 2 ) | Network bandwidth (BW net )                   | High AllReduce time, low scaling efficiency, communication > 30 percent of step | Scaling efficiency ( 𝜂 scaling ), communication fraction ( 𝑇 comm /𝑇 step ) 𝑇 /𝑇 | Gradient compression, overlap compute/communication, topology optimization (Chapter 7) |
| Coor- dina- tion ( )      | Synchronization overhead and failure recovery | Low goodput ratio, frequent restarts, large pipeline bubbles, scheduler churn   | Goodput ratio ( useful wall )                                                    | Async checkpointing, elastic training, faster failure detection (Chapter 8)            |

## E.3 The Fleet Law

𝐶

The Fleet Law, introduced in Section 1.5, decomposes every distributed training step into three irreducible time
components:

𝑇 step =𝑇 Computation +𝑇 Communication +𝑇 Coordination This equation is the fleet-scale counterpart of the iron law.
Where the iron law decomposes single-machine execution into data movement, compute, and overhead, the Fleet Law
decomposes distributed execution into local arithmetic, network data transfer, and synchronization logic. The diagnostic
strategy is identical: measure each term, identify which dominates, and direct engineering effort at the dominant term.

## E.3.1 Component decomposition

Each Fleet Law term maps to specific measurable activities:

- 𝑇 Computation: Forward pass, backward pass, optimizer step-all local arithmetic on each GPU. Governed by MFU and
per-GPU kernel efficiency. Improvements come from better kernels, mixed precision, and operator fusion.
- 𝑇 Coordination: Synchronization barriers, checkpoint writes, failure detection and recovery, pipeline bubble idle
time, scheduler preemptions, and maintenance windows. Governed by cluster reliability and orchestration software.
Improvements come from asynchronous checkpointing, elastic training, and faster failure detection.
- 𝑇 Communication: AllReduce of gradients, AllGather of parameters (in FSDP/ZeRO), activation transfers in
tensor/pipeline parallelism. Governed by network bandwidth and collective algorithm choice. Improvements come from
gradient compression, hierarchical collectives, and compute-communication overlap.

The fleet's efficiency follows directly:

When 𝑓 compute drops below 0.5, the fleet spends more time on communication and coordination than on useful arithmetic.
This compute-time fraction is not total fleet efficiency; useful fleet efficiency also depends on MFU, scaling
efficiency, and goodput. The C 3 taxonomy identifies which noncompute term is responsible.

<!-- formula-not-decoded -->

E.4 Intersection Landscape Like D·A·M, the C 3 axes interact at their boundaries. Production bottlenecks often sit at an
intersection where two axes compound.

Engineering at this intersection focuses on overlap strategies: launching AllReduce during the backward pass, using CUDA
streams to pipeline local computation with network transfers, and increasing the computation per synchronization point
(larger microbatches, gradient accumulation). Chapter 6 and Chapter 7 cover these techniques in depth.

E.4.1 Computation ∩ communication This intersection governs whether the system can hide communication behind
computation. The communication-computation ratio ( 𝜌 = 𝑇 comm /𝑇 comp ) is the key metric (Appendix B). When 𝜌 < 1,
computation takes longer than communication and the network transfer can be overlapped-the system is compute-bound and
healthy. When 𝜌 > 1, GPUs finish their local work before the network delivers the next round of data, and the system is
communication-bound.

E.4.2 Communication ∩ coordination This intersection captures the synchronization cost embedded in communication. Every
AllReduce is both a data transfer (Communication) and a synchronization barrier (Coordination)-all participants must
reach the barrier before any can proceed. The cost of stragglers manifests here: if one GPU is 10 percent slower, every
other GPU waits, converting a Communication operation into a Coordination bottleneck.

E.4.3 Computation ∩ coordination This intersection captures the idle compute caused by coordination overhead. Pipeline
bubbles are the canonical example: during warmup and cooldown phases of pipeline parallelism, some stages are idle while
others compute. Checkpoint writes that block the training loop convert coordination overhead into wasted compute
capacity. Failure recovery that requires rolling back and recomputing work transforms a coordination event into a
computation penalty.

Engineering at this intersection focuses on reducing barrier sensitivity: asynchronous gradient methods that decouple
communication from synchronization, hierarchical AllReduce that limits the blast radius of stragglers, and straggler
detection with proactive mitigation. Chapter 8 addresses straggler management.

Engineering at this intersection focuses on minimizing idle time: increasing microbatches to shrink the pipeline bubble
fraction, using asynchronous checkpointing to overlap writes with compute, and reducing the blast radius of failures so
that recomputation is bounded. Chapter 6 covers pipeline scheduling; Chapter 8 covers recovery strategies.

## E.5 Rules of Thumb

In the middle of a production incident, fast heuristics narrow the search space before a profiler is needed. These
thresholds provide that first line of defense.

Table E.3 provides threshold-based triage for each C 3 axis.

## E.5.1 The C 3 traffic light

Table E.3: C 3 Traffic Light: Quick triage thresholds for fleet-scale diagnosis. Green means the axis is healthy; yellow
means it deserves investigation; red means it is the likely bottleneck. These thresholds assume well-optimized
large-model training on current-generation hardware. C 3 Axis

| C Axis          | Green (Healthy)            | Yellow (Investigate)        | Red (Bottleneck)           |
|-----------------|----------------------------|-----------------------------|----------------------------|
| Computa- tion   | MFU > 50 percent           | MFU30-50 percent            | MFU < 30 percent           |
| Communi- cation | Commfraction < 20 percent  | Comm fraction 20-40 percent | Comm fraction > 40 percent |
| Coordina- tion  | Goodput ratio > 90 percent | Goodput ratio 75-90 percent | Goodput ratio < 75 percent |

## E.5.2 The bottleneck diagnostic table

Once the bottleneck axis is identified, Table E.4 shows which optimizations help and which ones are wasted.

Table E.4: What Works vs. What Is Wasted at Fleet Scale: Optimizing a nondominant C 3 axis yields limited improvement
and often worsens cost efficiency. A communication-bound fleet will gain little from faster GPUs until AllReduce and
other communication bottlenecks are addressed.

E.6 C 3 Case Studies Theoretical constraints manifest as confusing symptoms in production. These scenarios illustrate
how to apply the C 3 taxonomy to fleet-scale performance problems.

| If the fleet is…       | Dominant Term   | Optimization That Works                                                                  | Optimization That is Wasted                                                                               |
|------------------------|-----------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Computation- bound     | 𝑇 Computation   | Better kernels, mixed precision, operator fusion, next-gen accelerators                  | More network bandwidth (GPUs are not waiting on the network)                                              |
| Communication- bound 𝑇 | Communication   | Gradient compression, compute-comm overlap, hierarchical collectives, InfiniBand upgrade | Faster GPUs (they will just idle faster while waiting for the network)                                    |
| Coordination- bound 𝑇  | Coordination    | Async checkpointing, elastic training, faster failure detection, fewer pipeline stages   | Neither faster GPUs nor faster network (the time is lost to overhead, not to data movement or arithmetic) |

## E.6.1 Case 1: The underutilized fleet (Computation)

## Symptom

You provision 4,096 H100 GPUs for a large language model training run. The training loop runs without errors, but the
PyTorch Profiler shows MFU of only 15 percent. The network profiler shows communication accounts for less than 10
percent of step time. The cluster is running but barely working.

## Diagnosis

The Computation axis is the bottleneck. With 15 percent MFU, 85 percent of the fleet's arithmetic capacity sits idle on
every step. This is not a communication or coordination problem-the network is fast enough and the system is stable. The
system is not feeding work to the GPUs efficiently.

## The fix

This is a per-GPU efficiency problem that happens to be multiplied across 4,096 accelerators. Target the Computation
axis:

- Mixed precision: Ensure BF16/FP8 Tensor Cores are engaged. A common culprit is FP32 fallback in normalization layers
or loss computation.
- Operator fusion: Use torch.compile or similar just-in-time (JIT) compilation to fuse elementwise operations and reduce
kernel launch overhead.

· Batch size tuning: If per-GPU batch size is too small, the matrix multiplications have insufficient arithmetic
intensity to saturate the Tensor Cores. Raising MFU from 15 percent to 50 percent on the same hardware delivers 50/15 =
3.3 × more useful work-the equivalent of tripling the fleet without buying a single GPU.

## E.6.2 Case 2: The communication wall (Communication)

Symptom A 512-GPU data-parallel training run achieves 45 percent MFU on each individual GPU-good per-device efficiency.
Yet scaling from 64 to 512 GPUs yields only 4 × speedup instead of the expected 8 × . NCCL profiling reveals that
AllReduce consumes 55 percent of every training step. Diagnosis

The Communication axis dominates. Each GPU computes efficiently (MFU is healthy), but more than half the step time is
spent synchronizing gradients across the network. The system is communicationbound: adding more GPUs will make it worse,
not better, because AllReduce time grows with participant count while per-GPU computation stays constant.

## The fix

Target the Communication axis without touching the per-GPU computation:

- Compute-communication overlap: Launch AllReduce during the backward pass rather than waiting until it completes.
Modern frameworks (FSDP, DeepSpeed) support this natively.
- Hierarchical collectives: Use intra-node NVLink for the first reduction stage, then inter-node InfiniBand only for
cross-node aggregation, reducing cross-node traffic by 8 × .
- Gradient compression: Apply TopK sparsification or quantization to reduce the bytes crossing the network by 10-100 × .

If communication were eliminated entirely, throughput would increase by 2.2 × (Amdahl's Law applied to the 45 percent
compute fraction). Realistically, reducing communication from 55 percent to 20 percent of step time would recover most
of the lost scaling.

## E.6.3 Case 3: The coordination tax (Coordination)

## Symptom

A10,000-GPU training run shows 40 percent MFU per device and communication accounts for only 15 percent of step
time-both healthy. The job's goodput ratio (useful training steps/wall-clock time), however, is only 60 percent. The
remaining 40 percent of wall time is consumed by checkpoint writes, failure recovery restarts, pipeline bubble idle
time, 17 percent scheduler preemptions, and maintenance windows.

## Diagnosis

The Coordination axis dominates. Per-GPU computation and inter-node communication are both efficient, but 40 percent of
wall time is consumed by nonproductive overhead: 10 percent failure recovery (at 10,000 GPUs, failures occur every few
hours), 5 percent pipeline bubbles, 3 percent checkpoint writes, and 5 percent maintenance windows. Neither faster GPUs
nor faster networks will help-coordination, not computation or communication, consumes the time.

## The fix

Target the Coordination axis:

- Asynchronous checkpointing: Overlap checkpoint writes with the next training step, reducing visible checkpoint
overhead from 3 percent to near zero.
- Elastic training: When a node fails, shrink the job and continue rather than halting all 10,000 GPUs for recovery.
This converts the 10 percent failure recovery cost into a smaller throughput reduction.
- Pipeline schedule optimization: Switch from GPipe to an interleaved 1F1B schedule to reduce bubble fraction, or
increase microbatch count per pipeline flush.
- Faster failure detection: Reduceheartbeat timeout from 30 seconds to 5 seconds with hardwarelevel health monitoring,
cutting the idle time between failure occurrence and recovery initiation.

## E.7 Production Troubleshooting

Table E.5 provides a diagnostic matrix for common fleet-scale failure modes.

Table E.5: C 3 Troubleshooting Matrix: Root cause identification and remediation for common fleet-scale bottlenecks.
Each row connects a user-visible symptom to the C 3 axis most likely responsible, reducing the search space before
reaching for a profiler. Symptom 3

| Symptom                                    | C Axis          | Diagnostic Question                                                          | Measurement                                      | Action                                                                 |
|--------------------------------------------|-----------------|------------------------------------------------------------------------------|--------------------------------------------------|------------------------------------------------------------------------|
| Low MFUdespite fast network                | Compu- tation   | Are Tensor Cores engaged? Is batch size sufficient for arithmetic intensity? | Per-GPU kernel trace (Nsight/PyTorch Profiler) 𝜌 | Enable mixed precision, increase per-GPU batch size                    |
| Throughput plateaus when adding GPUs       | Commu- nication | Does AllReduce time grow faster than computation shrinks?                    | NCCL trace, ratio                                | Gradient compression, hierarchical collectives, overlap                |
| Frequent job restarts                      | Coordi- nation  | What is the cluster MTBF? Is detection fast enough?                          | Failure logs, MTBF calculation                   | Elastic training, faster detection, smaller blast radius               |
| High GPU-hours but slow progress           | Coordi- nation  | What fraction of GPU-hours produce useful training steps?                    | Goodput ratio ( 𝑇 useful /𝑇 wall )               | Async checkpointing, reduce pipeline stages, eliminate scheduler churn |
| Scaling efficiency drops with cluster size | Comm/Co- ord    | Is the bottleneck network bandwidth or synchronization barriers?             | Separate 𝑇 comm from 𝑇 coord                     | If comm: compress or overlap. If coord: async methods                  |
| Stragglers slow entire job                 | Comm ∩ Coord    | Is one node consistently last to reach the AllReduce barrier?                | Per-node step time histogram                     | Straggler detection + replacement, bounded staleness, backup workers   |

E.8 Tooling Map Engineers must measure abstract C 3 axes with concrete profiling tools. Table E.6 maps each axis to the
utilities that confirm or falsify a hypothesis.

Table E.6: C 3 Tooling Map: Profiling utilities for diagnosing fleet-scale bottlenecks. Start with the primary tool for
quick triage; use secondary tools for deep-dive analysis. Computation tools operate per-GPU; Communication tools operate
at the network layer; Coordination tools operate at the cluster/job level. C 3 Axis Key Metric

E.9 C 3 Scorecard The C 3 Scorecard grades fleet efficiency against known thresholds, extending the Single-Machine
Scorecard (Appendix A) to the distributed environment. Table E.7 defines the three metrics that characterize fleet
health.

Table E.7: The C 3 Efficiency Rubric: Use these three numbers to characterize fleet health. A fleet that passes all
three thresholds has exhausted its easy optimizations; further gains require architectural changes, hardware upgrades,
or larger problem sizes to improve the scaling regime. C 3 Axis Metric

| C Axis          | Key Metric                   | Primary Tool                                   | Secondary Tool                                            |
|-----------------|------------------------------|------------------------------------------------|-----------------------------------------------------------|
| Computation     | MFU, kernel utilization      | PyTorch Profiler (TensorBoard plugin)          | Nsight Compute (per-kernel roofline analysis)             |
| Communica- tion | AllReduce time, 𝜌 ratio      | NCCL debug logs ( NCCL_DEBUG=INFO )            | Nsight Systems (timeline), ibstat / perfquery (IB)        |
| Coordination    | Goodput ratio, restart count | Cluster scheduler logs (Slurm, K8s event logs) | Custom goodput dashboards (for example, Google MLGoodput) |

## E.10 Scaling Laws Through the C 3 Lens E.10.1 Why scaling laws assume perfect C 3

| C Axis            | Metric                           | Definition                                                       | Failing Grade   | Passing Grade   |
|-------------------|----------------------------------|------------------------------------------------------------------|-----------------|-----------------|
| Com- puta- tion   | MFU                              | Achieved Model FLOPs Peak                                        | < 30 percent    | > 50 percent    |
| Com- muni- cation | Scaling Efficiency ( 𝜂 scaling ) | 𝑇 1 𝑁×𝑇𝑁                                                         | < 35 percent    | > 70 percent    |
| Coordi- nation    | Goodput Ratio                    | 𝑇 useful 𝑇 wall or useful steps/sec ideal or allocated steps/sec | < 75 percent    | > 90 percent    |

Scaling laws-Kaplan, Chinchilla, and their successors-predict model quality as a function of algorithmic training
compute. They usually abstract away systems efficiency: wall-clock time, accelerator peak FLOPS, MFU, communication
overhead, and scheduler losses enter later when teams provision hardware to deliver the target compute budget. In C 3
terms, scaling-law FLOPs must be converted into raw fleet capacity after MFU, communication, and goodput losses.

<!-- image -->

<!-- formula-not-decoded -->

The gap between scaling-law predictions and observed training outcomes is, in large part, a C 3 gap. A team that budgets
10 24 FLOPs for training will actually deliver far fewer effective FLOPs to the model, because each FLOP must survive
three multiplicative losses: per-GPU utilization (MFU), inter-node scaling efficiency ( 𝜂 scaling ), and operational
goodput. E.10.2 The effective FLOPS concept The Effective FLOPS delivered by a fleet compound three independent C 3
losses:

Each factor maps to one C 3 axis. MFU captures per-GPU computation efficiency. Scaling efficiency captures communication
overhead as GPUs are added. Goodput ratio captures coordination losses from checkpoints, failures, pipeline bubbles, and
maintenance.

## Systems Perspective 23.1: The C³ tax on a 100,000-GPU cluster

Consider a 100,000-GPU H100 cluster with 98,900 PFLOPS of peak aggregate throughput. After the three C 3 losses:

This is not a failure of engineering-it is the physics of fleet-scale computation. The C 3 taxonomy quantifies where the
losses occur so that optimization effort targets the dominant term.

Effective =98,900×0.50×0.35×0.60 ≈ 10,384 PFLOPS The fleet delivers 10.5 percent of its peak capacity as useful training
work. The C 3 tax -the ratio of peak to effective-is 9.5 × : achieving a given effective compute budget requires 9.5 ×
the raw hardware. Broken down by axis: Computation consumes a 50 percent factor (MFU), Communication consumes a 35
percent factor (using the 8,192-GPU scaling-efficiency reference as an illustrative proxy), and Coordination consumes a
60 percent factor (goodput ratio after pipeline bubbles, checkpoints, failures, scheduler preemptions, and maintenance).

E.11 Summary The C 3 taxonomy provides a systematic framework for diagnosing fleet-scale bottlenecks. Each axis maps to
a distinct physical constraint: arithmetic throughput and MFU bound Computation; network bandwidth and collective
algorithm efficiency bound Communication; and synchronization overhead, failure recovery, and operational losses bound
Coordination. The Fleet Law quantifies these constraints, enabling systematic diagnosis. Use the C 3 Traffic Light for
quick triage, the Bottleneck Diagnostic Table to choose the right lever, and the C 3 Scorecard to grade fleet health.

- Every fleet-scale bottleneck has a dominant C 3 axis: Computation, Communication, or Coordination, with many real
bottlenecks spanning intersections. Identify the dominant axis before optimizing. > >

## Key Takeaways: Where to look first at fleet scale

<!-- image -->

- Measure the C 3 Scorecard (MFU 50 percent, Scaling Efficiency 70 percent, Goodput Ratio > 90 percent) before investing
in optimizations. · The C 3 tax is multiplicative: Peak FLOPS × MFU × Scaling Efficiency × Goodput Ratio = Effective
FLOPS. At 100,000 GPUs, expect only ~10.5 percent of peak.
- Optimizing the wrong C 3 axis yields limited improvement. Faster GPUs cannot fix a communication-bound fleet by
themselves; faster networks cannot fix coordination overhead.
- Coordination is the new axis: On a single machine, overhead is negligible. At fleet scale, checkpoints, failures,
pipeline bubbles, and scheduling consume 40 percent or more of wall time.

E.12 Exercises Exercise 1: C 3 classification A512-GPU training job shows 45 percent MFU per device, but NCCL logs
reveal that AllReduce consumes 55 percent of each training step. Which C 3 axis is the bottleneck? Name two specific
optimizations and explain why each targets the correct axis.

Answer: The bottleneck is Communication ( 𝐶 2 ). Per-GPU MFU of 45 percent is healthy (above the 30 percent threshold),
so Computation is not the problem. The 55 percent communication fraction far exceeds the 40 percent red-line threshold.
Two optimizations: (1) Gradient compression (for example, TopK sparsification) directly reduces the bytes crossing the
network, shrinking 𝑇 Communication while leaving 𝑇 Computation unchanged. (2) Compute-communication overlap launches the
AllReduce during the backward pass rather than waiting until it completes, converting the sequential sum 𝑇 comp +𝑇 comm
into the overlapped max (𝑇 comp, 𝑇 comm ) -both target the Communication axis.

Exercise 2: Fleet law decomposition Atraining step on a 1,024-GPU cluster takes 200 ms. Profiling reveals: forward +
backward pass = 100 ms, AllReduce = 60 ms, pipeline bubble + checkpoint = 40 ms. Calculate 𝜂 fleet . Which C 3 axis
would you optimize first, and why? Answer: Fleet efficiency is:

The fleet spends exactly half its time on useful computation. Breaking down the noncompute time: Communication accounts
for 60/200 = 30 percent and Coordination accounts for 40/200 = 20 percent. Both are in the 'yellow' zone of the traffic
light, but Communication (30 percent) is the larger contributor. Optimize Communication first: overlapping AllReduce
with the backward pass could reduce the visible 60 ms to near zero (if computation is longer), pushing 𝜂 fleet toward
100/140 = 0.71. Tackle the 40 ms coordination overhead only after addressing communication.

Exercise 4: Anti-pattern detection Acolleague proposes upgrading the cluster's InfiniBand from HDR(200 Gbps) to NDR (400
Gbps) because 'training is too slow.' Before approving the network upgrade, what three C 3 diagnostic questions would
you ask? Map each to its C 3 axis. Answer: Before upgrading the network, ask:

<!-- formula-not-decoded -->

Exercise 3: Effective FLOPS calculation Ateam provisions 2,048 H100 GPUs. The cluster achieves 50 percent MFU, 50
percent scaling efficiency, and 85 percent goodput ratio. Calculate the effective FLOPs as a fraction of peak. If a
scaling law predicts that 10 24 FLOPs of training compute will reach a target loss, how many raw peak FLOPs must be
provisioned to account for the C 3 tax? Answer: Effective fraction: Effective fraction =0.50×0.50×0.85 = 21.2% The C 3
tax is 1/0.212 ≈ 4.7× . Delivering 10 24 effective FLOPs therefore requires provisioning 4.7 ×10 24 raw peak FLOPs. This
is the practical cost of the C 3 gap: scaling-law compute budgets must be inflated by the C 3 tax to account for
real-world fleet overhead.

1. 'What is the current MFU?' -Computation ( 𝐶 1 ) . If MFU is below 30 percent, the GPUs themselves are underutilized.
Faster interconnects cannot help if the GPUs are not doing useful work to begin with. Fix kernel efficiency first.
3. 'Cancompute-communicationoverlapbeenabledbeforeupgradinghardware?' -Communication ( 𝐶 2 ) . If AllReduce currently
runs sequentially after the backward pass, enabling overlap (a software change) may eliminate the communication
bottleneck entirely-at zero hardware cost. Consider the network upgrade only after enabling overlap and confirming that
communication still dominates.
2. 'Whatfraction of step time is spent in AllReduce vs. noncommunication overhead?' -Communication ( 𝐶 2 ) vs.
Coordination ( 𝐶 3 ) . If AllReduce consumes $>$40 percent of step time, the network upgrade is justified. If, however,
most noncompute time is checkpoint writes and failure recovery (Coordination), doubling network bandwidth will have no
impact on the dominant overhead.

