# Appendix B: Fleet Foundations (Vol 2)

Appendix B provides the quantitative reference numbers, physical scaling laws, and thermodynamic constraints that govern
machine learning fleets at scale. Designing and analyzing distributed training and serving systems requires
understanding how communication, computation, and coordination overheads scale.

---

## Section-by-Section Preserve-and-Extend

## Fleet Foundations

## Purpose

What reference numbers and physical laws should every fleet-scale ML engineer carry into distributed system design
decisions?

This appendix collects the reference numbers and compact models for fleet-scale reasoning. It begins with a comparison
of the three system paradigms that underpin this book, then provides the 'numbers every fleet engineer should
know'-organized around the three axes of Communication, Computation, and Coordination (C 3 ). It concludes with the
scaling physics and thermal constraints that govern cluster design.

Designing a system for a single machine requires knowledge of memory hierarchy latencies, roofline ridge points, and
precision trade-offs. The moment a training job spans two machines, however, a new set of numbers takes over. Network
latency replaces cache latency as the dominant concern. Component failure rates compound from negligible to inevitable.
Communication overhead erodes the scaling efficiency that justifies buying more accelerators in the first place.

## How to Use This Appendix

This appendix is designed as a reference. When a fleet-scale design question arises, use it to turn a vague symptom into
a specific constraint and then choose the lever that can actually move.

- 'How fast can I communicate between nodes?' : Start with the Communication Numbers in Section B.2 for the bandwidth
and latency hierarchy.
- 'How many GPUs do I actually need?' : Use the Scaling Physics in Section B.3 to understand why doubling GPUs does not
halve training time.
- 'How often will my cluster fail?' : Check the scaling physics in Section B.3 for MTBF tables and failure probability
calculations.
- 'Is my cluster power-limited or compute-limited?' : See Thermal and Power Physics in Section B.4 for power density and
cooling constraints.
- 'What does a typical overhead budget look like?' : The Coordination Numbers include the four overhead categories that
erode goodput.

## B.1 The Three System Paradigms

M achine learning infrastructure at scale inherits design DNA from two distinct computing lineages-and then breaks the
assumptions of both. Understanding where ML systems borrow from High-Performance Computing (HPC) and where they borrow
from Warehouse-Scale Computing (WSC) is essential for choosing the right design trade-offs. A system architect who
treats ML training as 'just HPC' will build infrastructure that cannot tolerate failures. One who treats it as 'just web
services' will build infrastructure that cannot sustain the tight coupling that synchronous training demands.

## High-performance computing

HPC systems descend from the supercomputer tradition. Their design philosophy is to maximize FLOPs per second on tightly
coupled simulations-weather modeling, molecular dynamics, nuclear physics. Every node matters: they use specialized
interconnects (InfiniBand), low-latency fabrics, and homogeneous hardware. Fault tolerance follows the
checkpoint/restart model: if one node fails, the entire job stops, rolls back to the last checkpoint, and restarts from
scratch. Scheduling is batch-oriented (Slurm), with jobs requesting rigid resource shapes ('512 nodes for 24 hours').
Nodes are pets -individually important, individually tracked.

## Warehouse-scale computing

WSC systems descend from the web services tradition. Their design philosophy is to maximize queries per second across
loosely coupled services-search, email, social media. Hardware is commodity Ethernet, varying generations coexist, and
nodes are heterogeneous. Fault tolerance follows the redundancy model: if one node fails, the load balancer reroutes
traffic to another replica. The user never notices. Scheduling is dynamic (Kubernetes, Borg), with elastic bin-packing.
Nodes are cattle -interchangeable and expendable.

## The ML fleet: A hybrid architecture

ML systems require the computational throughput of HPC (to train massive models with synchronous gradient updates) but
must operate at the scale and unreliability of WSC (thousands of accelerators running for weeks). This creates a hybrid
that borrows selectively from both traditions.

Table B.1 summarizes the design trade-offs across the three paradigms. The key insight is that ML fleets cannot simply
adopt either HPC or WSC patterns wholesale; they must selectively combine elements from each based on the workload
phase.

Training workloads are synchronous and bandwidth-hungry like HPC, but long-running and failure-tolerant like WSC.
Inference workloads are latency-sensitive like WSC, but computationally heavy like HPC. The network is a fusion: TCP/IP
for control planes, InfiniBand or NVLink for data planes. Fault tolerance uses elastic strategies-training jobs can
shrink, expand, pause, or resume without full restarts. Scheduling combines gang allocation (all-or-nothing for
training) with dynamic preemption and replacement.

Table B.1: Three System Paradigms: MLfleets inherit design DNA from both HPC and WSC but break assumptions of each.
Training resembles HPC (tight coupling), inference resembles WSC (elastic serving), and fault tolerance is a hybrid of
both.

| Dimension   | HPC (Supercomputer)                                                           | WSC(Web Cloud)        | MLFleet (AI Cluster)                   |
|-------------|-------------------------------------------------------------------------------|-----------------------|----------------------------------------|
| Philosophy  | Maximize FLOPs/s Tight (MPI) Stateful (RAM) Latency-optimized Compute (FLOPs) | Maximize QPS Loose    | Maximize Model Quality per Dollar/Watt |
| Coupling    |                                                                               | (RPC/HTTP)            | Hybrid (NCCL + RPC)                    |
| State       |                                                                               | Stateless (DB-backed) | Semi-Stateful (Checkpoints + KV Cache) |
| Network     |                                                                               | Bandwidth-optimized   | Bisection-bandwidth critical           |
| Bottleneck  |                                                                               | I/O (Disk/Net)        | Memory bandwidth (HBM)                 |
| Fault model | Checkpoint/Restart                                                            | Redundancy/Replicas   | Elastic shrink/expand                  |
| Scheduling  | Batch (Slurm)                                                                 | Orchestration (K8s)   | Gang + preemption                      |
| Node model  | Pets (tracked)                                                                | Cattle (expendable)   | Pets during job, cattle between jobs   |

## Foundations recap

- The following provides a compact reference for the key foundational ideas that reappear throughout the distributed
systems chapters. · The iron law ( 𝑇 ≈ 𝐷 vol / BW +𝑂/(𝑅 peak ⋅ 𝜂 hw ) +𝐿 lat ): Performance is bounded by data movement
or compute. At fleet scale, the data movement term expands to include inter-node communication, not just memory
bandwidth.
- Amdahl's Law: Caps strong-scaling speedup at 1/𝑠 . At fleet scale, the 'serial fraction' includes not just sequential
code but also synchronization barriers, collective communication, and pipeline bubbles.
- Roofline Model: Distinguishes compute-bound from memory-bound workloads using arithmetic intensity. At fleet scale, a
third ceiling appears: network-bound workloads whose performance is limited by inter-node bandwidth.

- Training state rule: about 14 bytes per parameter for common mixed-precision Adam checkpoint state (BF16 weights, FP32
master weights, and Adam moments), before framework metadata and implementation-specific extras. At fleet scale, this
determines how model state is partitioned across nodes (ZeRO, tensor parallelism, pipeline parallelism). · Little's Law
( 𝑁 req =𝜆𝑇 lat ): Sizes inference infrastructure. At fleet scale, it determines how many serving replicas are needed
behind a load balancer.

The transition from single-machine to fleet-scale reasoning requires extending these models with new dimensions: network
topology, failure probability, and coordination overhead. The numbers in the next section provide the quantitative
foundation for that extension.

## B.2 Numbers Every Fleet Engineer Should Know

Just as single-machine analysis depends on a set of core numbers, fleet-scale engineering is governed by a set of
predictable ratios and scaling behaviors. The single-machine numbers still apply within each node, but a new set of
numbers governs the spaces between nodes. While absolute values evolve with hardware generations, the ratios between
communication tiers and the scaling behavior of failure rates remain remarkably stable. Memorize the ratios and scaling
trends; use the specific numbers as sanity checks.

## Systems Perspective 20.1: Node-level numbers for fleet reasoning

Fleet reasoning depends on a few node-level numbers that directly affect fleet design: about 14 bytes per parameter for
common Adam checkpoint state, with larger footprints when gradients, activations, metadata, or extra optimizer buffers
are included; NVLink vs. HBM bandwidth (intra-node parallelism placement); peak FLOPS and HBM capacity (MFU and
effective FLOPS, batch and model sharding). Table B.2 and the communication numbers in the preceding section give
inter-node and current-generation values; the memory hierarchy and roofline ridge points within a node provide the
necessary baseline.

## Key Takeaways: Three fleet numbers that matter most

- If only three numbers stick from this section, they should be these: 1. 18 × gap: NVLink bandwidth within a node is
~18 × faster than InfiniBand between nodes. This ratio determines where parallelism boundaries belong-model parallelism
within a node, data parallelism across nodes.
3. ~19.2 percent effective utilization: After MFU, scaling efficiency, and overhead losses compound, a 1,024-GPU cluster
delivers roughly 19.2 percent of its peak FLOPS as useful training work.
2. MTBF scales as 1/𝑁: Acluster's mean time between failures is the single-component MTBF divided by the number of
components. At 100,000 GPUs, expect a failure every 30 minutes.

Quick reference-Table B.2 condenses the fleet-scale numbers into one place. Use it for back-ofenvelope checks; use the
detailed tables in each subsection when designing or debugging.

Table B.2: Numbers Every Fleet Engineer Should Know (Quick Reference) : One-page summary of the fleet-scale reference
numbers in this section. See Table B.3 and Table B.4 for Communication, Table B.5 for Computation, and Table B.6 for
Coordination.

| Category                | Number                                                         | Use                                                   |
|-------------------------|----------------------------------------------------------------|-------------------------------------------------------|
| Communi- cation         | NVLink ~18 × IBNDR                                             | Parallelism boundary (in-node vs. cross-node)         |
| Communi- cation         | IB NDR~50 GB/s, ~5 μs one-way                                  | Inter-node bandwidth and latency                      |
| Computa- tion           | MFU30-50%, η ~50% @ 1K, ~35% @ 8K                              | Effective FLOPS and scaling sanity checks             |
| Coordina- tion          | MTBF 8K: ~366 min; 100K: ~30 min                               | Failure expectation and checkpoint cadence            |
| Coordina- tion          | 175B checkpoint ~2450 GB (14 B/param common Adam state)        | Recovery and storage sizing                           |
| Coordina- tion          | Goodput ~77% after overheads                                   | Wall-clock utilization                                |
| Power& sustainabil- ity | AI rack ~70 kW; air limit ~30kW                                | Cooling feasibility (liquid required above air limit) |
| Power& sustainabil- ity | PUE liquid ~1.06, typical ~1.40; H100700W->10KGPUs≈7MWIT × PUE | Facility load and carbon (see Section B.4)            |

## The invariants: Ratios that will not change

These relationships are governed by physics or architecture-they will still be true in 2035.

## Network hierarchy ratio

The bandwidth gap between intra-node and inter-node communication is an architectural invariant. Chip-to-chip links
(NVLink, ICI) connect through short, wide, dedicated paths on a shared substrate. Inter-node links (InfiniBand,
Ethernet) must traverse cables, switches, and protocol stacks. This structural difference guarantees that intra-node
bandwidth will always be an order of magnitude higher than inter-node bandwidth.

Currently, NVLink 4.0 provides 18 × more bandwidth than InfiniBand NDR. Even as both technologies improve, the ratio
persists because both are constrained by the same physics: signaling rates, lane counts, and connector density. This
ratio is the single most important number for parallelism strategy: any operation requiring more bandwidth than the
inter-node link can provide must be confined within a single node.

## Failure scaling law

For independent components, each with mean time to failure MTTF, the cluster MTBF is: MTBFcluster = MTTFcomponent 𝑁
(B.1) This is pure arithmetic, not an approximation. Doubling the cluster size halves the time between failures. At
100,000 GPUs with a 50,000-hour per-GPU MTTF, the cluster experiences a GPU failure every 30 minutes. No fault tolerance
strategy can avoid this-the question is how quickly the system recovers.

𝑁

AllReduce overhead scaling The bandwidth-optimal Ring AllReduce algorithm transfers 2(𝑁 -1)𝑀/𝑁 bytes per participant,
where 𝑀 is the message size and 𝑁 is the number of participants. As 𝑁 grows large, this approaches 2𝑀 per GPU, so the
per-GPU bandwidth term is nearly independent of the number of GPUs; aggregate cluster traffic still grows with the
number of participants. This is why Ring AllReduce scales well in the bandwidth term. The latency term, however, grows
as 2(𝑁 -1)×𝛼, making latency the bottleneck for small messages on large rings. This trade-off motivates hierarchical
AllReduce strategies that use Ring AllReduce within nodes and Tree AllReduce across nodes.

## Communication numbers

Communication defines the boundaries of parallelism. These tables quantify the bandwidth and latency at each tier of the
network hierarchy, from the fastest intra-node links to the slowest wide-area connections. The key question for any
distributed ML operation is: which tier of the network hierarchy does this communication cross?

Table B.3: Communication Bandwidth Hierarchy: Bandwidth drops by roughly 18 × crossing from intra-node (NVLink) to
inter-node (InfiniBand). This ratio determines parallelism placement.

Table B.3 shows the bandwidth available at each tier. Note the order-of-magnitude drops as communication crosses node
boundaries.

| Interconnect      | Bandwidth   | Typical Role                                |
|-------------------|-------------|---------------------------------------------|
| NVLink 4.0 (H100) | 900 GB/s    | Tensor/pipeline parallelism within a node   |
| TPU v5p ICI       | 1,200 GB/s  | Intra-pod model parallelism (Google)        |
| PCIe Gen5 x16     | 64 GB/s     | CPU-GPU data transfer, NIC attachment       |
| IB GXDR(1.6 Tbps) | 200 GB/s    | Next-gen inter-node (2026+)                 |
| IB XDR (800 Gbps) | 100 GB/s    | Inter-node standard (2025+)                 |
| IB NDR(400 Gbps)  | 50 GB/s     | Current inter-node standard for AI clusters |
| IB HDR(200 Gbps)  | 25 GB/s     | Previous-gen inter-node                     |
| RoCE v2 (100 GbE) | 12.5 GB/s   | Budget clusters, inference fleets           |

Table B.4 shows the one-way latency at each tier. For collective operations on small messages, latency-not bandwidth-is
the bottleneck.

Table B.4: Communication Latency Hierarchy: Latency determines whether synchronous training is feasible. TCP/IP is
roughly 10 × slower than InfiniBand NDR, making it unsuitable for gradient synchronization in large clusters.
Interconnect

| Interconnect      | One-Way Latency   | Implication                           |
|-------------------|-------------------|---------------------------------------|
| InfiniBandNDR     | ~5 𝜇 s 𝜇          | Low enough for synchronous AllReduce  |
| InfiniBandHDR     | ~7 s 𝜇            | Adequate for most training topologies |
| RoCE v2           | ~10 s 𝜇           | Acceptable for data parallelism       |
| TCP/IP (Ethernet) | ~50 s             | Too slow for synchronous training     |
| Cross-data-center | ~40,000 s (40 ms) | Physics floor; async training only    |

## Computation numbers

𝜇

Raw peak FLOPS are a necessary but misleading metric for fleet capacity planning. Two multiplicative losses-Model FLOPS
Utilization (MFU) and scaling efficiency-reduce effective throughput dramatically. Understanding these losses transforms
fleet sizing from guesswork into engineering.

Model FLOPS Utilization (MFU) measures what fraction of peak FLOPS a training workload actually achieves. Well-optimized
large-model training on current hardware achieves 30-50 percent MFU. The gap comes from memory stalls, kernel launch
overhead, pipeline bubbles, and suboptimal operator fusion. MFU below 30 percent signals optimization opportunities; MFU
above 50 percent indicates excellent hardware utilization. Scaling efficiency ( 𝜂 hw ) measures how much useful
computation survives as accelerators are added. Table B.5 shows the empirical ranges for well-optimized distributed
training.

Table B.5: Scaling Efficiency by Cluster Size: Efficiency degrades roughly as the logarithm of cluster size. These
ranges assume well-optimized data parallelism with gradient compression. Poorly optimized systems can lose 2-3 × more.
Cluster Size 𝜂 32 GPUs Near-linear scaling; communication is negligible

| Cluster Size   | Scaling Efficiency ( hw )   | Implication                                      |
|----------------|-----------------------------|--------------------------------------------------|
| 32 GPUs        | ~90%                        | Near-linear scaling; communication is negligible |

𝜂

| Cluster Size   | Scaling Efficiency ( hw )   | Implication                                           |
|----------------|-----------------------------|-------------------------------------------------------|
| 256 GPUs       | ~70%                        | Communication starts to erode throughput              |
| 1,024 GPUs     | ~50%                        | Significant overhead; optimization critical           |
| 8,192 GPUs     | ~35%                        | Fleet-scale regime; 65 percent of compute is overhead |

## Coordination numbers

At fleet scale, coordination-failure recovery, checkpointing, and maintenance-consumes a measurable fraction of
wall-clock time. These numbers quantify the costs of keeping a large cluster running.

## Failure rates by cluster size

Table B.6 shows how cluster MTBF shrinks with scale, using a per-GPU MTTF of 50,000 hours (~5.7 years). The failure
probability column shows the likelihood of at least one GPU failure during a 24-hour training window.

Table B.6: MTBF and Failure Probability by Cluster Size: GPU-only failure model with per-GPU MTTF of 50,000 hours. Real
clusters also include NIC, PSU, cable, and switch failures, making these estimates conservative. The probability column
uses 𝑃(≥1) = 1-𝑒 -𝑇/ MTBF for 𝑇 = 24 hours. Cluster Size

| Cluster Size   | MTBF (GPU-only)   |   Minutes | P(failure) in 24 hours   |
|----------------|-------------------|-----------|--------------------------|
| 256 GPUs       | 195.3 hours       |    11,719 | 12%                      |
| 2,048 GPUs     | 24.4 hours        |     1,465 | 63%                      |
| 8,192 GPUs     | 6.1 hours         |       366 | 98%                      |
| 100,000 GPUs   | 0.50 hours        |        30 | 100%                     |

The key takeaway: at 8,192 GPUs and above, failure is not a risk-it is a certainty within any training run longer than a
few hours. Fault tolerance is not optional at fleet scale; it is a prerequisite for completing any training job. Chapter
8 covers the mechanisms in detail.

## Checkpoint sizes

Checkpointing is the primary recovery mechanism, and its cost depends on the model size. Table B.7 shows checkpoint
sizes for common mixed-precision Adam training checkpoints (14 bytes per parameter: 2B for BF16 weights and 12B for FP32
master weights + momentum + variance). Gradients are normally transient and recomputed after restore rather than
serialized as durable checkpoint state.

Table B.7: Checkpoint Sizes by Model Scale: Uses 14 bytes/parameter for common mixed-precision Adam checkpoint state.
Write time assumes 100 GB/s aggregate storage bandwidth. Asynchronous checkpointing (Chapter 8) can overlap writes with
training, reducing the visible overhead.

| Model Size      | Checkpoint Size   | Write Time @ 100 GB/s   |
|-----------------|-------------------|-------------------------|
| 7B parameters   | 98 GB             | ~1 second               |
| 70B parameters  | 980 GB            | ~10 seconds             |
| 175B parameters | 2,450 GB          | ~25 seconds             |
| 1T parameters   | 14 TB             | ~2.3 minutes            |

## Overhead budgets

As Table B.8 shows, at fleet scale, four categories of overhead consume wall-clock time that is not spent on useful
training:

Table B.8: Overhead Budgets for Fleet-Scale Training: These are fractions of wall-clock time. At 10,000+ GPUs, failure
recovery dominates. The compound effect is additive: total goodput ratio ≈1.0-(0.05+0.03+0.10+0.05) = 0.77 ≈ 77% .
Overhead Category

| Overhead Category   | Typical Budget   | Lever                                    |
|---------------------|------------------|------------------------------------------|
| Pipeline bubbles    | ~5%              | Increase microbatches per pipeline stage |
| Checkpointing       | ~3%              | Async checkpointing, faster storage      |
| Failure recovery    | ~10%             | Faster detection, elastic rescheduling   |
| Maintenance windows | ~5%              | Rolling upgrades, live migration         |

## Power and sustainability numbers

Fleet-scale capacity planning and sustainability reporting require a few power numbers that every fleet engineer should
know. At fleet scale, the critical numbers are rack power density, PUE, and the air-cooling limit -they determine where
construction is feasible and what the facility load will be.

| Quantity               | Typical value   | Use                                              |
|------------------------|-----------------|--------------------------------------------------|
| Traditional rack       | 12kW            | Baseline for non-AI data centers                 |
| AI rack (current gen)  | 70kW            | Liquid cooling required                          |
| AI rack (high-density) | 100kW           | Direct-to-chip liquid                            |
| Air cooling limit      | ~30 kWper rack  | Physics ceiling; above this, liquid is mandatory |
| PUE (liquid-cooled AI) | ~1.06           | Best case: facility load ≈ IT load               |
| PUE (best air-cooled)  | ~1.12           | Hyperscale best practice                         |
| PUE (industry average) | ~1.40           | Sanity check for cost/carbon                     |
| H100 TDP               | 700 Wper GPU    | IT load: 10K GPUs 700W=7MW                       |

## Current hardware reference (c. 2024-2025)

H100 TDP Rule of thumb: IT load (MW) = (number of GPUs × TDP per GPU)/ 10 6; facility load = IT load × PUE . A
10,000-GPU H100 cluster at 700 W each is 7 MW IT; at PUE 1.4 that is 9.8 MW facility draw. For carbon and cost, see
Section B.4 and Chapter 16.

Table B.9: Fleet-Scale Hardware Reference (c. 2025-2026) : Per-accelerator specifications for the current and emerging
generations. The B200, MI300X, and Tensor Processing Unit (TPU) v6 (Trillium) represent the frontier of fleet-scale
compute density and memory bandwidth.

×

These numbers reflect the current generation of fleet-scale hardware. Use them for back-of-envelope calculations, but
expect them to improve ~2 × every 2-3 years.

| Spec             | NVIDIA B200             | AMDMI300X                | Google TPU v6           |
|------------------|-------------------------|--------------------------|-------------------------|
| BF16/FP16 Peak   | 2,250 TFLOPS            | 1,307 TFLOPS             | 918 TFLOPS              |
| Memory Bandwidth | 8.00 TB/s               | 5.30 TB/s                | 1.60 TB/s               |
| HBMCapacity      | 192 GB                  | 192 GB                   | 32 GB                   |
| Intra-Node Link  | 1,800 GB/s (NVLink 5.0) | ~890 GB/s (Infinity Fab) | ~2,000 GB/s (estimated) |
| TDP              | 1,000W                  | 750W                     | ~600 W(estimated)       |

As Table B.9 summarizes, a DGX H100 SuperPOD contains 32 DGX H100 nodes (256 H100 GPUs). Meta announced two 24,576-H100
data-center-scale clusters built on the Grand Teton hardware platform. Google's TPU v5p pods scale to 8,960 chips. The
largest announced clusters (as of 2025) exceed 100,000 accelerators.

## B.3 Scaling Physics

The numbers in the previous section describe what the hardware can do. Scaling physics describes what happens
whenmoreofit is brought to bear. Three models govern fleet-scale reasoning: Amdahl's Law extended to fleet overhead, the
communication-computation ratio, and weak scaling behavior.

<!-- image -->

LIGHTBULB Why this matters Atraining job provisioned with 4,096 GPUs achieves only 2.5 × the throughput of a 1,024-GPU
run. Is this expected? Scaling physics provides the diagnostic tools to determine whether the system is performing as
physics allows or whether there is an engineering problem to fix.

## B.3.1 Amdahl's Law at fleet scale

- Pipeline bubbles: The warmup and cooldown phases of pipeline parallelism leave stages idle.

Amdahl's Law establishes that the maximum speedup of a parallel system is limited by its serial fraction 𝑠 . At fleet
scale, the 'serial fraction' is not just sequential code-it includes every operation that forces all 𝑁 GPUs to wait: ·
AllReduce synchronization: All GPUs must complete their gradient computation before any can proceed.

- Checkpoint writes: Even asynchronous checkpoints contend for storage bandwidth.
- Python-level overhead: Single-threaded operations in the training loop (data loading, metric logging).

×

To see the fleet-scale implications, consider a training workload where 10 percent of wall-clock time is spent in
synchronization, communication, and other serial overhead. Amdahl's Law gives the following speedups: · With 32 GPUs:
7.8 × speedup (good efficiency) · With 256 GPUs: 9.7 speedup (diminishing returns begin) · With 1,024 GPUs: 9.9 speedup
(approaching the ceiling) · With 8,192 GPUs: 10.0 × speedup (nearly at the Amdahl limit) · With 𝑁 →∞ : capped at 10 ×
With just 10 percent serial overhead, no amount of hardware can deliver more than 10 × speedup on this fixed workload.
This is why fleet-scale training does not simply add more GPUs to the same problem-it scales the problem (weak scaling)
to keep the serial fraction small relative to the total work.

×

## Exclamation The compound overhead trap

The 10 percent serial fraction above is optimistic. In practice, fleet-scale serial overhead accumulates from multiple
sources: 5 percent pipeline bubbles + 3 percent checkpointing + 10 percent failure recovery + 5 percent maintenance.
These are not all strictly serial in the Amdahl sense-some overlap with computation-but they illustrate how quickly
small per-category overheads compound into significant throughput loss.

## B.3.2 The communication-computation ratio

The fundamental question for any distributed training strategy is: does the computation between synchronization points
take long enough to hide the communication? The communication-computation ratio ( 𝜌 ) answers this directly:

\(\rho\)

When 𝜌 < 1, computation dominates and communication can be overlapped. When 𝜌 > 1, the system is communication-bound
-GPUs spend more time waiting for data than computing on it. Table B.10 shows the ratio for three representative
scenarios. The contrast between them reveals why parallelism strategy must match the workload.

Table B.10: Communication-Computation Ratio ( 𝜌 ) : When 𝜌 ≪ 1, communication can be fully overlapped with computation.
When 𝜌 ≫ 1, the system is communication-bound and GPUs sit idle waiting for data. Tensor parallelism within a node
benefits from NVLink's high bandwidth, keeping 𝜌 small. Scenario 𝑇 𝑇 𝜌 Data parallel, 7B

| Scenario                            | comm                              | comp              |       |
|-------------------------------------|-----------------------------------|-------------------|-------|
| Data parallel, 7B model, 256 GPUs   | 560.4 ms (AllReduce over IB NDR)  | ~5.0 s (fwd+bwd)  |  0.11 |
| Data parallel, 350M model, 256 GPUs | 30.4 ms (AllReduce over IB NDR)   | ~10 ms (fwd+bwd)  |   3.0 |
| Tensor parallel, 8 GPUs (NVLink)    | ~0.02 ms (activation over NVLink) | ~1 ms (one layer) | 0.018 |

GPUs (NVLink) The 7B model on 256 GPUs achieves 𝜌 = 0.11-communication takes about 11 percent as long as computation,
which can be partially overlapped. The 350M model on the same cluster has 𝜌 = 3.0-communication dominates, making this
configuration communication-bound. The solution is either to use fewer GPUs (reduce 𝑁 in the AllReduce) or to increase
the computation per step (larger batch size, gradient accumulation).

Tensor parallelism within a node achieves 𝜌 = 0.018, confirming that NVLink bandwidth is sufficient to keep intra-node
parallelism compute-bound. This is the quantitative reason why tensor parallelism is confined within nodes while data
parallelism spans across them.

## B.3.3 Weak scaling at fleet scale

Amdahl's Law paints a pessimistic picture because it assumes a fixed problem size. In practice, fleet-scale training
often follows weak scaling: the problem size (tokens, data, model parameters) grows proportionally with the number of
GPUs. Gustafson's Law captures this more optimistic view.

<!-- image -->

The key insight for fleet-scale ML is that weak scaling is not just a mathematical convenience-it reflects reality.
Engineers do not use 8,192 GPUs to train a 7B model faster; they use them to train a 70B or 700B model in reasonable
time. As models and training batches grow, engineers often increase the compute performed between synchronization
points. For dense Transformers, compute is commonly estimated as about 6 × parameters × tokens, while gradient
communication scales with parameter bytes, so the communication-computation ratio 𝜌 depends on batch size, sequence
length, accumulation, and parallelism layout rather than on parameter count alone.

## Systems Perspective 20.2: The compound loss of fleet utilization

A1,024-GPU H100 cluster has a peak aggregate throughput of 1,012,736 TFLOPS. After the three multiplicative losses, the
effective throughput is: Effective = Peak × MFU ×𝜂 scaling × Goodput Ratio =1,012,736×0.50×0.50×0.77 ≈ 194,952 TFLOPS
The cluster delivers 19.2 percent of its peak FLOPS as useful training work. The remaining 81 percent is consumed by
hardware underutilization (50 percent MFU), communication overhead (50 percent scaling efficiency), and operational
losses (77 percent goodput ratio).

This is not a failure of engineering-it is the physics of fleet-scale computation. Every additional GPU adds less
marginal useful work, but the total throughput still far exceeds what a smaller cluster could achieve. The goal is not
to reach 100 percent utilization; the goal is to deliver trained models faster than any smaller configuration could.

## B.4 Thermal and Power Physics

Compute performance ultimately converts to heat, and heat must be removed. At fleet scale, thermal and power constraints
are not secondary concerns-they determine where construction is feasible, how densely accelerators can be packed, and
what the operating costs will be. A cluster that is architecturally sound but thermally infeasible cannot be built.

<!-- image -->

Why this matters

Acluster design calling for 10,000 H100 GPUs at 700 W each-7 MW of IT load-and a PUE of 1.4 puts the facility load at
9.8 MW total. This is the electrical load of a small town. Before optimizing software, the physics of power delivery and
heat removal must be feasible.

## B.4.1 Power density wall

The shift from traditional data center workloads to AI training has created a power density crisis . Table B.11
quantifies the gap.

Table B.11: Power Density: Traditional vs. AI Workloads: AI racks consume roughly 5.8 × the power of traditional racks.
Air cooling physically cannot remove heat fast enough above ~30 kW per rack, making liquid cooling mandatory for modern
AI clusters.

| Configuration             | Power per Rack   | Cooling Implication                       |
|---------------------------|------------------|-------------------------------------------|
| Traditional data center   | 12kW             | Standard air cooling sufficient           |
| AI cluster (current gen)  | 70kW             | Liquid cooling required                   |
| AI cluster (high-density) | 100kW            | Direct-to-chip liquid cooling required    |
| Air cooling limit         | ~30kW            | Physics ceiling for forced-air convection |

The 5.8 × increase in rack power density between traditional and AI workloads is not merely an engineering challenge-it
represents a fundamental constraint on facility design. Existing data centers built for 12 kW racks cannot simply be
'retrofitted' with AI hardware. The electrical distribution, cooling infrastructure, and floor loading must all be
redesigned. This is why new AI-focused data centers are being built from the ground up with liquid cooling as the
baseline assumption.

## B.4.2 The energy hierarchy at scale

Power Usage Effectiveness (PUE) measures how efficiently a data center converts electrical power into useful IT
computation. A PUE of 1.0 would mean every watt goes to computing; values above 1.0 represent overhead for cooling,
power conversion, lighting, and other facility systems.

Table B.12 compares PUE across data center generations and cooling technologies.

Table B.12: Power Usage Effectiveness (PUE) : Lower is better. Liquid cooling achieves PUE near 1.0 because it removes
heat directly from the chip without the intermediate step of heating air. The gap between legacy (1.58) and
liquid-cooled (1.06) represents about a 33 percent reduction in total facility power at fixed IT load; the non-IT
overhead drops from 0.58 MW to 0.06 MWper MW of IT load.

| Data Center Type             |   PUE | Overhead per MWofIT Load      |
|------------------------------|-------|-------------------------------|
| Liquid-cooled AI data center |  1.06 | 60 kWcooling + infrastructure |
| Best-in-class air-cooled     |  1.12 | 120 kWoverhead                |
| Industry average             |  1.40 | 400 kWoverhead                |
| Legacy enterprise            |  1.58 | 580 kWoverhead                |

For fleet-scale cost calculations, PUE directly multiplies the electricity bill. A 10 MW IT load in a legacy data center
(PUE 1.58) requires 15.8 MW total, while the same load in a liquid-cooled facility

(PUE 1.06) requires only 10.6 MW-a savings of 5.2 MW. At typical commercial electricity rates, this difference
translates to millions of dollars per year. Chapter 16 covers the full sustainability implications.

## B.5 Fallacies and Pitfalls

<!-- image -->

Exclamation-Triangle Fallacy: Adding more GPUs always makes training faster Amdahl's Law caps speedup at 1/𝑠 for a fixed
workload. At 10 percent serial overhead, no fleet larger than ~10 × the baseline delivers meaningful additional speedup.
Beyond the Amdahl limit, every additional GPU contributes nearly zero marginal throughput while increasing failure
probability and communication overhead. The solution is weak scaling: grow the problem to match the hardware.

<!-- image -->

## Exclamation-Triangle Fallacy: InfiniBand is just fast Ethernet

InfiniBand and Ethernet differ architecturally, not just in speed. InfiniBand provides kernelbypass (RDMA),
hardware-managed flow control, and credit-based congestion avoidance. Ethernet relies on software-managed TCP/IP stacks
with orders-of-magnitude higher latency. RoCE (RDMA over Converged Ethernet) bridges some of this gap, but requires
lossless Ethernet configuration (PFC, ECN) that introduces its own failure modes. The choice between InfiniBand and
Ethernet is a system architecture decision, not a bandwidth selection.

<!-- image -->

## Exclamation-Triangle Pitfall: Ignoring failure probability at scale

Asingle GPU with a 50,000-hour MTTF seems extremely reliable-that is nearly 6 years. At 8,192 GPUs, however, the cluster
MTBF drops to 6.1 hours (366 minutes). The probability of at least one failure in a 24-hour training window is 98
percent. Designing a training system without automated failure recovery at this scale guarantees that every long-running
job will fail and require manual intervention.

<!-- image -->

## Exclamation-Triangle Pitfall: Optimizing MFU without considering scaling efficiency

Ateam achieves 50 percent MFU on a single node-excellent performance. They scale to 1,024 GPUs and expect 512 ×
throughput (512 GPU-equivalents of useful work). Scaling efficiency at 1,024 GPUs, however, is ~50 percent, so actual
throughput is only 256 GPU-equivalentshalf the expected value. MFU and scaling efficiency are independent multiplicative
factors; optimizing one without measuring the other leads to incorrect capacity estimates.

<!-- image -->

## Exclamation-Triangle Fallacy: Air cooling is sufficient for AI workloads

Air cooling physically cannot remove heat fast enough above ~30 kW per rack. Currentgeneration AI racks consume 70-100
kW, well beyond this limit. Attempting to air-cool an AI cluster leads to thermal throttling, reduced clock speeds, and
ultimately component failure. Liquid cooling is not an optimization for AI clusters-it is a physical requirement.

## Summary

- Key Takeaways: Fleet scale changes every constraint
- Three paradigms, one hybrid: ML fleets combine HPC's tight coupling (for training) with WSC's elastic fault tolerance
(for inference), creating a new architectural paradigm that cannot adopt either predecessor's patterns wholesale.
- Failure is certain at scale: Cluster MTBF scales as 1/𝑁 . At 8,192 GPUs, expect a failure every 366 minutes. Fault
tolerance is not optional-it is a prerequisite for completing any fleet-scale training job.
- The 18 × bandwidth gap: NVLink provides ~18 × more bandwidth than InfiniBand. This invariant ratio determines
parallelism placement: tensor parallelism within nodes, data parallelism across nodes.
- Compound utilization loss: After MFU (~50 percent), scaling efficiency (~50 percent), and operational overhead (~77
percent goodput) compound, a 1,024-GPU cluster delivers ~19.2 percent of peak FLOPS as useful work.
- Communication-computation ratio ( 𝜌 ) governs scaling strategy: When 𝜌 > 1, GPUs are idle waiting for data-reduce
parallelism or increase computation per step. When 𝜌 ≪ 1, communication can be fully overlapped.
- Power density demands liquid cooling: AI racks consume 5.8 × the power of traditional racks. Air cooling fails above
~30 kW per rack, making liquid cooling a physical requirement for modern AI clusters.
- Weak scaling is the fleet-scale paradigm: Engineers do not use more GPUs to solve the same problem faster (strong
scaling); they use more GPUs to solve larger problems in reasonable time. This keeps the serial fraction small and
utilization high.

