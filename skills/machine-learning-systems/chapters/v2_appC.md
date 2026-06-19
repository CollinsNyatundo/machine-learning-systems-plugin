# Appendix C: Communication Foundations (Vol 2)

Appendix C compiles the communication cost models, collective operation complexities, pipeline bubble metrics, and
compression trade-offs that govern distributed machine learning. When network communication stalls limit scaling, these
models allow practitioners to diagnose bottlenecks.

---

## Section-by-Section Preserve-and-Extend

## Communication Foundations

## Purpose

\_** What communication primitives bind the fleet together, and how do we predict their cost before running a single
experiment?\_

This appendix collects the communication cost models that answer those questions quantitatively. It starts with the
foundational 𝛼 -𝛽 model-the 'Roofline for networks'-then derives the cost of every collective operation used in
distributed training, analyzes pipeline bubble overhead, and closes with the economics of gradient compression. These
models support the distributed strategies in Chapter 6, the collective algorithms in Chapter 7, the fault tolerance
mechanisms in Chapter 8, and the performance analysis in Chapter 10.

Distributed ML training spends a surprising fraction of wall time not computing, but communicating. A large distributed
training run may dedicate a substantial fraction of every iteration to synchronizing gradients, redistributing
activations, or shuffling expert tokens. When that communication overhead is the bottleneck, no amount of faster
arithmetic will help. The question shifts from 'how many FLOPs?' to 'how many bytes, across what topology, at what
latency?'

## How to Use This Appendix

This appendix is designed as a reference. Reach for it when translating a distributed training symptom ('AllReduce is
slow,' 'pipeline bubbles are killing throughput,' 'should we compress gradients?') into a quantitative diagnosis.

- When AllReduce is slow: Use Section C.2 to compute the expected time and compare ring vs. tree costs.

Conventions used here follow the book-wide notation. We use 𝛼 for per-message startup latency, 𝛽 for link bandwidth in
bytes per second, 𝑁 for the number of participating GPUs, and 𝑀 for total message size in bytes.

- When choosing ring vs. tree: Use Section C.3 and the crossover analysis to match algorithm to message size.
- When pipeline bubbles dominate: Use Section C.4 to compute bubble fraction and determine the required microbatch
count.
- When gradient compression is proposed: Use Section C.5 to run the break-even calculation before committing engineering
effort. C.1 The 𝛼 -𝛽 Communication Model Systems Perspective 21.1: Why this matters

<!-- image -->

Estimating how long a gradient synchronization will take across 256 GPUs must happen before committing to a cluster
topology. The 𝛼 -𝛽 model is the 'Roofline for networks': it gives a first-order prediction of transfer time from just
two hardware parameters and the message size.

𝛼

𝛽

<!-- formula-not-decoded -->

E very point-to-point transfer on a network follows the same fundamental pattern: the sender pays a fixed startup cost
to initiate the message, then transmits the payload at a rate determined by the link's bandwidth. This two-parameter
model captures the essential physics of network communication. The 𝛼 -𝛽 model predicts the time to transfer a message of
𝑀 bytes:

Table C.1: 𝛼 -𝛽 Parameters by Interconnect: Startup latency and sustained bandwidth for interconnects used in ML
clusters. NVLink and PCIe operate within a node; InfiniBand and RoCE operate between nodes. TCP latency is dominated by
kernel software stack overhead. Interconnect 𝛼 𝛽 NVLink 4.0 (H100)

where: · 𝛼 is the startup latency (seconds)-the fixed cost of initiating a message, including software overhead, NIC
processing, and routing setup · 𝛽 is the link bandwidth (bytes/second)-the sustained data rate after startup · 𝑀 is the
message size (bytes) The model decomposes every transfer into exactly two costs: a per-message tax ( 𝛼 ) paid regardless
of size, and a per-byte tax ( 𝑀/𝛽 ) that scales linearly with the payload. This decomposition drives all the algorithm
selection decisions in Section C.3. Table C.1 lists the 𝛼 and 𝛽 values for interconnects commonly found in ML training
clusters. These numbers are the starting point for every communication cost estimate in this appendix.

| Interconnect             | (Latency)   | (Bandwidth)   | Typical Role                     |
|--------------------------|-------------|---------------|----------------------------------|
| NVLink 4.0 (H100)        | 500 ns      | 900 GB/s      | Intra-node GPU-to-GPU            |
| PCIe Gen5                | 1000 ns 𝜇   | 64 GB/s       | CPU-GPU, NIC-GPU                 |
| InfiniBand NDR(400 Gbps) | 5 s         | 50 GB/s       | Inter-node (high-end clusters)   |
| InfiniBand HDR(200 Gbps) | 7 𝜇 s       | 25 GB/s       | Inter-node (previous generation) |
| RoCE v2 (100 GbE)        | 10 𝜇 s      | 12.5 GB/s     | Inter-node (Ethernet clusters)   |
| TCP/IP (Ethernet)        | 50 𝜇 s      | Varies        | Control plane, non-RDMA fallback |

C.1.1 Latency-dominated vs. bandwidth-dominated regimes The 𝛼 -𝛽 model reveals two distinct operating regimes. For small
messages, the startup latency 𝛼 dominates-the link spends most of its time starting transfers, not sustaining them. For
large messages, the bandwidth term 𝑀/𝛽 dominates, and the startup cost becomes negligible. The crossover message size 𝑀
cross is the point where both terms contribute equally: 𝑀 cross =𝛼×𝛽 (C.2) Below 𝑀 cross, communication is
latency-dominated: sending more small messages wastes time on repeated startups. Above 𝑀 cross, communication is
bandwidth-dominated: the link is fully utilized, and the only way to go faster is higher bandwidth.

<!-- image -->

<!-- formula-not-decoded -->

Interpretation: Messages smaller than 250 KB are latency-dominated on IB NDR. Gradient tensors from a single layer of a
large model are typically 10-100 MB-well above this threshold. Control messages, heartbeats, and barrier
synchronizations, however, are well below it.

C.1.2 The LogGP model extension The 𝛼 -𝛽 model assumes a message is a single, atomic transfer. In practice, networks
pipeline messages: a sender can inject a new packet before the previous one has been fully received. The LogGP model
(Alexandrov et al. 1995) extends LogP with a long-message gap parameter: · 𝑔 (gap) : The minimum interval between
consecutive message injections at the sender. This models the NIC's injection rate limit. · 𝑜 (overhead) : The CPU time
consumed by the processor to initiate or complete a message, during which it cannot do useful compute. For a long
message of 𝑘 bytes, LogGP models transfer time as approximately: 𝑇 long ≈𝑜 𝑠 +𝐿+(𝑘-1)𝐺+𝑜 𝑟 where 𝐺 is the gap per byte
for long messages and 𝑔 controls the minimum interval between consecutive message injections. Informal alpha-beta-style
approximations can be useful for ML profiling, but the standard LogGP model keeps these gap parameters distinct from a
simple bandwidth term.

Implication: This is why NCCL and Gloo batch small gradient tensors into larger 'buckets' before launching AllReduce.
Sending each tensor individually would pay the 5 𝜇 s startup cost hundreds of times per iteration instead of a handful.

In most ML training scenarios, the 𝛼 -𝛽 modelissufficient because gradient tensors are large enough that pipelining
effects are secondary to raw bandwidth. The LogGP model becomes important when analyzing the overhead of many small
control messages or when modeling the interaction between communication and computation overlap-situations that arise in
fine-grained pipeline parallelism and asynchronous gradient updates.

The 𝛼 -𝛽 model describes point-to-point transfers. Collective operations-where all GPUs participate-compose multiple
point-to-point transfers, and their cost formulas derive directly from the model above.

## C.2 Collective Operation Complexity

<!-- image -->

## Systems Perspective 21.2: Why this matters

Every distributed training step ends with a collective synchronization. The cost of that collective-not the cost of the
matrix multiplies-often determines whether scaling from 8 GPUs to 256 is feasible. Understanding the exact complexity of
each collective reveals which parallelism strategy (data, tensor, pipeline, expert) will dominate wall time at a given
scale.

Collective operations move data between all 𝑁 GPUs simultaneously. Each collective has a characteristic bandwidth term
(how much data flows) and latency term (how many sequential message steps are required). The formulas below use the
bandwidth-optimal ring algorithm unless otherwise noted; Section C.3 discusses when other algorithms are preferable.

## C.2.1 AllReduce

AllReduce is the workhorse of data-parallel training: every GPU starts with a local gradient tensor of size 𝑀 bytes and
ends with the globally reduced (summed) result. The ring algorithm decomposes AllReduce into a ReduceScatter phase
followed by an AllGather phase. Ring AllReduce

<!-- formula-not-decoded -->

The factor 2(𝑁 -1)/𝑁 in the bandwidth term approaches 2 as 𝑁 grows-each byte effectively traverses the ring twice (once
for reduce-scatter, once for all-gather). The latency term grows linearly with 𝑁, which makes the ring algorithm
expensive in latency for large GPU counts. Tree AllReduce

<!-- image -->

Ring AllReduce:

𝑇 tree =2 log 2 𝑁⋅ 𝑀 𝛽 +2 log 2 𝑁⋅𝛼 (C.4) The tree algorithm trades bandwidth efficiency for latency efficiency: the
latency term grows as log 2 𝑁 instead of 𝑁, but the bandwidth term sends the full message 𝑀 at each tree level instead
of 𝑀/𝑁 chunks. Napkin Math 21.2: Worked example: Ring vs. tree AllReduce Setup: 256 H100 GPUs connected via InfiniBand
NDR ( 𝛼 = 5 𝜇 s, 𝛽 = 50 GB/s). The gradient tensor is 1 GB (a 500M-parameter model in FP16). Question: How long does
AllReduce take with ring vs. tree?

𝑇

ring 42.4 ms Tree AllReduce: 𝑇 tree ≈ 320.1 ms Interpretation: For this 1 GB message, ring AllReduce takes 42.4 ms while
tree takes 320.1 ms-the ring is significantly faster because it distributes the bandwidth load across all links. The
tree's logarithmic latency advantage is negligible compared to its bandwidth penalty for large messages.

≈

Implication: For the large gradient tensors typical of data-parallel training, ring (or ring-based) algorithms dominate.
Tree algorithms are useful only for small messages or when latency-not bandwidth-is the bottleneck.

C.2.2 AllGather AllGather is the complement of ReduceScatter: each GPU starts with a 𝑀/𝑁 -sized shard and ends with the
complete 𝑀 -byte tensor. It is the core communication primitive in Fully Sharded Data Parallelism (FSDP) for
reconstructing parameters before each forward pass, and in tensor parallelism for reassembling split activations.

Ring AllGather

AllGather is exactly half the cost of AllReduce (one ring pass instead of two) because it does not include a reduction
step.

C.2.3 ReduceScatter ReduceScatter is the dual of AllGather: each GPU starts with a full 𝑀 -byte tensor and ends with a
𝑀/𝑁 -sized shard that contains the globally reduced values for that shard. It is the gradient synchronization primitive
in FSDP and ZeRO, replacing the full AllReduce with a cheaper operation when each GPU only needs its own parameter
shard's gradient.

<!-- formula-not-decoded -->

Ring ReduceScatter 𝑇 reducescatter = 𝑁 -1 𝑁 ⋅ 𝑀 𝛽 +(𝑁 -1)⋅𝛼 (C.6) The symmetry is not a coincidence: ring AllReduce
decomposes into one ReduceScatter followed by one AllGather, and the costs add up exactly to Equation C.3.

C.2.4 AllToAll AllToAll is the most general collective: each GPU sends a distinct 𝑀/𝑁 -sized chunk to every other GPU,
and receives a distinct chunk from each. It is the routing primitive for Mixture-of-Experts (MoE) architectures, where
tokens must be dispatched to the correct expert and the results gathered back.

Ring AllToAll

Although the formula matches AllGather and ReduceScatter in form, the communication pattern is fundamentally different:
AllToAll is a personalized exchange (each GPU sends different data to each peer), which makes it harder to overlap with
computation and more sensitive to network congestion.

<!-- formula-not-decoded -->

C.2.5 Broadcast Broadcast sends a single 𝑀 -byte tensor from one root GPU to all 𝑁 -1 others. It is used for
distributing initial model weights, updated learning rates, and configuration changes during training. Tree Broadcast

Broadcast is inherently asymmetric (one sender, many receivers), which makes a tree topology natural. In an unsegmented
tree broadcast, the full 𝑀 -byte payload is forwarded at each tree level, so both the latency and bandwidth terms appear
along the log 2 𝑁 -level critical path. Segmented or scatter-allgather broadcast variants can reduce the bandwidth term,
but they require a different algorithm-specific model.

<!-- formula-not-decoded -->

## Collective complexity summary

Table C.2 provides a compact reference for comparing the cost structure of each collective operation.

Table C.2: Collective Operation Cost Summary: Bandwidth and latency terms for ring and tree algorithms. The bandwidth
term determines cost for large messages (gradients, parameters); the latency term determines cost for small messages
(scalars, barriers). 𝑁 = GPU count, 𝑀 = total message size in bytes. Operation

| Operation            | Bandwidth Term        | Latency Term    | Primary Use Case                 |
|----------------------|-----------------------|-----------------|----------------------------------|
| AllReduce (Ring)     | 𝑁-1 𝑀                 | 2(𝑁 -1)⋅𝛼 2 𝑁⋅𝛼 | Data-parallel gradient sync      |
| AllReduce (Tree)     | 2⋅ 𝑁 ⋅ 𝛽 2 log 𝑁⋅ 𝑀 𝛽 | log 2 (𝑁 -1)⋅𝛼  | Small-message sync               |
| AllGather (Ring)     | 2 𝑁-1 𝑁 ⋅ 𝑀 𝛽         |                 | FSDP parameter reconstruction    |
| ReduceScatter (Ring) | 𝑁-1 𝑁 ⋅ 𝑀 𝛽           | (𝑁 -1)⋅𝛼        | FSDP/ZeRO gradient sharding      |
| AllToAll (Ring)      | 𝑁-1 𝑁 ⋅ 𝑀 𝛽 𝑁⋅        | (𝑁 -1)⋅𝛼 𝑁⋅𝛼    | MoE expert routing               |
| Broadcast (Tree)     | log 2 𝑀 𝛽             | log 2           | Weight distribution, config sync |

Two patterns emerge from this table. First, bandwidth-optimal ring algorithms all share the (𝑁 -1)/𝑁 factor, which
approaches 1 for large 𝑁 . Per-rank communication therefore approaches a constant multiple of 𝑀: about 2𝑀 for AllReduce
and about 𝑀 for AllGather, ReduceScatter, or AllToAll. Aggregate traffic still scales with the number of ranks. Second,
the latency term grows linearly with 𝑁 for ring algorithms but logarithmically for tree algorithms, creating the
algorithm selection trade-off analyzed next.

## C.3 Algorithm Selection

<!-- image -->

Systems Perspective 21.3: Why this matters

NCCL automatically selects a collective algorithm based on message size and GPU topology, but understanding why it
chooses ring for large messages and tree for small ones helps diagnose when the auto-selection is suboptimal-and how to
structure communication to stay in the efficient regime.

C.3.1 Ring vs. tree vs. recursive halving-doubling The ring algorithm minimizes bandwidth usage but pays a latency cost
that grows linearly with 𝑁 . The tree algorithm minimizes latency but wastes bandwidth because it sends the full message
at each level. Recursive halving-doubling splits the difference: it uses halving (like a tree) for the reduce phase and
doubling for the gather phase, achieving near-optimal bandwidth with 𝑂( log 𝑁) latency steps. The decision boundary
between ring and tree depends on message size: · 𝑀≫𝑀 cross (large gradients): Use ring . The bandwidth term dominates,
and ring's (𝑁 -1)/𝑁 factor is optimal.

- 𝑀 ≪𝑀 cross (barriers, scalars): Use tree . The latency term dominates, and tree's log 2 𝑁 steps are far fewer than
ring's 2(𝑁 -1) . · 𝑀 ≈𝑀 cross (medium tensors): Use recursive halving-doubling for balanced performance, or test
empirically. Table C.3 provides guidance for choosing the right algorithm.

Table C.3: Algorithm Selection Guide: Strengths and weaknesses of ring, tree, and recursive halving-doubling for
different message sizes and GPU counts. 𝑀 cross =𝛼×𝛽 is the crossover message size from Equation C.2. Regime Ring

𝑁

𝑁

𝑁 = 2

𝑁 = 2

| Regime                           | Ring                                       | Tree                               | Recursive Halving-Doubling                           |
|----------------------------------|--------------------------------------------|------------------------------------|------------------------------------------------------|
| Large messages ( 𝑀>10×𝑀 cross )  | Best-optimal bandwidth utilization 2(𝑁 -1) | Poor-sends 𝑀 at every tree level 𝑁 | Good-near-optimal bandwidth, 𝑂( log 𝑁) latency 𝑂( 𝑁) |
| Small messages ( 𝑀<𝑀 cross /10 ) | Poor- startup costs dominate               | Best- log 2 startup costs          | Good- log startup costs                              |
| Medium messages ( 𝑀≈𝑀 cross )    | Acceptable                                 | Acceptable                         | Best-balances both terms                             |
| Power-of-2                       | Works for any                              | Best when                          | Requires                                             |

## C.3.2 Hierarchical AllReduce

Modern clusters have a two-level topology: GPUs within a node are connected by NVLink (900 GB/s), while nodes are
connected by InfiniBand (50 GB/s). Hierarchical AllReduce exploits this asymmetry in three phases:

2. Inter-node AllReduce (InfiniBand): The per-node results are all-reduced across nodes. Only 𝑁/8 nodes participate, so the ring has 𝑁/8 steps instead of 𝑁 . 3. Intra-node broadcast (NVLink): Each node broadcasts the global result to its 8 local GPUs. The hierarchical approach reduces the inter-node ring size from 𝑁 to 𝑁/8, cutting the latency term by 8 × and confining the bandwidth-hungry phases to the fast intra-node links. NCCL selects among topology-aware algorithms such as Ring, Tree, CollNet variants, NVLS/NVLSTree, and PAT based on the collective, message size, topology, architecture, and version; hierarchical communication is common on multi-node systems but is not a universal default.

1. Intra-node reduce (NVLink): Each node reduces its 8 local GPUs to a single result using NVLink's 900 GB/s bandwidth.
This is fast because NVLink is 18 × faster than InfiniBand NDR.

Understanding the cost structure of collectives enables reasoning about data-parallel overhead. Pipeline parallelism,
however, introduces a different kind of overhead: idle time caused by the sequential dependency between pipeline stages.
The next section quantifies that cost.

𝑘

𝑘

## C.4 Pipeline Arithmetic

<!-- image -->

Systems Perspective 21.4: Why this matters

Pipeline parallelism splits a model across multiple GPUs so that each GPU holds only a fraction of the layers. The
trade-off is bubble time: idle cycles where GPUs wait for activations or gradients from upstream or downstream stages.
Quantifying the bubble fraction reveals whether pipeline parallelism is worth the complexity at a given scale.

C.4.1 Bubble fraction In a pipeline with 𝑃 stages and 𝑀 microbatches, the bubble fraction is the proportion of total
GPU-time spent idle:

The key insight: the bubble fraction depends on the ratio of stages to microbatches. Adding more microbatches (for a
fixed number of stages) amortizes the pipeline fill and drain across more useful work. Rule of thumb: Keeping bubble
overhead below 20 percent requires 𝑀 ≥4(𝑃 -1) , which means 𝑀 ≥4𝑃 for practical purposes. Table C.4 shows how bubble
fraction varies with pipeline depth and microbatch count.

𝑏 = 𝑃 -1 𝑃 -1+𝑀 (C.9) This formula applies to both GPipe (where all forward passes complete before any backward pass
begins) and 1F1B (one-forward-one-backward interleaving). The 1F1B schedule has the same asymptotic bubble fraction but
uses less peak memory because it retires microbatches earlier.

Table C.4: Pipeline Bubble Fraction: Percentage of GPU-time lost to pipeline bubbles for various stage counts and
microbatch counts. Values below 20 percent (the typical target) require 𝑀≥4𝑃 . Pipeline Stages ( ) = 8

𝑃

| Pipeline Stages ( 𝑃 ) 𝑃   | = 8     | = 16    | = 32   | = 64   |
|---------------------------|---------|---------|--------|--------|
| = 4                       | 𝑀 27.3% | 𝑀 15.8% | 𝑀 8.6% | 𝑀 4.5% |
| = 8                       | 46.7%   | 30.4%   | 17.9%  | 9.9%   |

C.4.2 Interleaved scheduling Interleaved scheduling (used in Megatron-LM) assigns 𝑉 virtual stages to each physical GPU
instead of one. Each GPU processes 𝑉 nonconsecutive chunks of the model, which means the pipeline has 𝑃 ×𝑉 virtual
stages but the bubble overhead uses the original 𝑃:

Interleaved scheduling highlights a recurring theme in distributed ML: communication granularity is a tunable knob.
Smaller, more frequent transfers improve overlap and reduce idle time, but increase the aggregate latency overhead. The
same trade-off appears in gradient compression, which is the final cost model in this appendix.

𝑏 interleaved = 𝑃 -1 𝑃 -1+𝑀 ×𝑉 (C.10) The denominator grows by a factor of 𝑉 compared to Equation C.9. For 𝑃 = 8, 𝑀 =
16, and 𝑉 = 4, the bubble fraction drops from 30.4 percent to 9.9 percent-a dramatic improvement that comes at the cost
of more frequent, smaller communication between stages.

## C.5 Compression Economics

<!-- image -->

Systems Perspective 21.5: Why this matters Gradient compression promises to reduce communication volume by 10-1000 × ,
making AllReduce nearly free. Compression, however, has overhead (encoding and decoding time), and it only helps if that
overhead is smaller than the communication time it saves. A quick break-even analysis prevents wasted effort on
compression schemes that will not actually speed up training.

C.5.1 The compression equation Gradient compression replaces the original 𝑀 -byte gradient with a compressed
representation of size 𝑀/𝐶, where 𝐶 is the compression ratio. The total time with compression is:

Compression is beneficial when compressed comm, which yields the break-even condition: 𝑇 encode +𝑇 decode <𝑇 comm (𝑀)-𝑇
comm ( 𝑀 𝐶 ) (C.12) In the bandwidth-dominated regime ( 𝑀 ≫𝑀 cross ), the communication time scales linearly with
message size, and the right-hand side simplifies to approximately 𝑇 comm (𝑀)×(1-1/𝐶) . For high compression ratios ( 𝐶
≫1 ), this approaches 𝑇 comm (𝑀) -meaning compression is worthwhile as long as the codec overhead is less than the
uncompressed communication time.

<!-- formula-not-decoded -->

## Napkin Math 21.3: Worked example: Is top-k compression worth it?

<!-- image -->

## Calculation:

Setup: Ring AllReduce of a 1 GB gradient across 256 H100 GPUs on InfiniBand NDR, taking 42.4 ms uncompressed. A Top-k
sparsification scheme achieves 64 × compression with 2.0 ms total encode + decode overhead. Question: Does compression
reduce the total AllReduce time?

- Uncompressed AllReduce: 42.4 ms

· Compressed communication: 0.7 ms · Total with compression: 2.7 ms · Speedup: 15.9 × Interpretation: Compression
delivers a 15.9 × speedup in communication time. The 2.0 ms codec overhead is a small fraction of the 42.4 ms saved.

Implication: At this scale (256 GPUs, 1 GB gradients), gradient compression is clearly profitable. However, the
convergence impact must be validated: Top-k sparsification discards information, and the model may require more
iterations to reach the same accuracy, potentially negating the per-iteration speedup.

Table C.5 shows how the break-even codec overhead varies with compression ratio and uncompressed AllReduce time. Higher
compression ratios tolerate larger codec overheads.

Table C.5: Compression Break-Even Thresholds: Maximum tolerable codec overhead (encode + decode) for compression to
reduce total time, computed as 𝑇 comm (𝑀)×(1-1/𝐶) . At high compression ratios, nearly the entire uncompressed AllReduce
time is available as codec budget. Compression Ratio

| Compression Ratio ( )   | AllReduce = 10 ms (Max Codec Overhead)   | AllReduce = 40 ms (Max Codec Overhead)   | AllReduce = 100 ms (Max Codec Overhead)   |
|-------------------------|------------------------------------------|------------------------------------------|-------------------------------------------|

𝐶

×

| Compression Ratio ( 𝐶 ) ×   | AllReduce = 10 ms (Max Codec Overhead)   | AllReduce = 40 ms (Max Codec Overhead)   | AllReduce = 100 ms (Max Codec Overhead)   |
|-----------------------------|------------------------------------------|------------------------------------------|-------------------------------------------|
| 16                          | 9.4 ms                                   | 37.5 ms                                  | 93.8 ms                                   |
| 64                          | 9.8 ms                                   | 39.4 ms                                  | 98.4 ms                                   |
| × 256                       | 9.96 ms                                  | 39.8 ms                                  | 99.6 ms                                   |

## C.6 Fallacies and Pitfalls

×

Fallacy: Doubling network bandwidth halves AllReduce time. For ring AllReduce, the bandwidth term is 2(𝑁 -1)/𝑁 ⋅𝑀/𝛽,
which does scale inversely with 𝛽 . The latency term 2(𝑁 -1)⋅𝛼, however, is independent of bandwidth. At 256 GPUs with
small messages, the latency term can dominate, and doubling bandwidth yields negligible improvement. Always check the
current regime before investing in faster interconnects.

Within a node, GPUs communicate through NVLink or NVSwitch, which provides all-to-all connectivity-not a ring. The
actual intra-node AllReduce uses a different algorithm (often a singlestep reduce through the NVSwitch crossbar) with
much lower latency than the ring formula predicts. The ring formula applies to inter-node communication where the ring
topology matches the physical network.

Pitfall: Using the ring AllReduce formula for intra-node communication.

Fallacy: Pipeline parallelism eliminates communication overhead.

Fallacy: AllReduce, AllGather, and ReduceScatter have the same performance characteristics because they have the same
ring complexity.

Pipeline parallelism replaces AllReduce with point-to-point activation transfers between adjacent stages, which are
indeed cheaper. It introduces, however, bubble overhead that is mathematically unavoidable: with 𝑃 stages, at least (𝑃
-1)/(𝑃 -1+𝑀) of GPU-time is idle. For deep pipelines ( 𝑃 ≥ 8 ), this overhead requires 𝑀 ≥32 microbatches to stay below
20 percent-a constraint that affects batch size, memory, and convergence. Pitfall: Evaluating gradient compression by
communication speedup alone. Acompression scheme that achieves 100 × communication speedup is worthless if it degrades
model quality enough to require 2 × more training iterations. The correct metric is time-to-accuracy, not
time-per-iteration. Always validate compression on the target convergence benchmark, not just on a communication
microbenchmark.

While the bandwidth and latency formulas are identical for ring-based implementations, the operations have different
memory access patterns and computation requirements. ReduceScatter performs a reduction (addition) on the received data,
AllGather only copies, and AllToAll routes distinct chunks to distinct destinations. These differences affect how well
each operation overlaps with computation and how sensitive it is to memory bandwidth contention on the GPU.

## Summary

- Key Takeaways: Communication costs are predictable · The 𝛼 -𝛽 model ( 𝑇 =𝛼+𝑀/𝛽 ) decomposes every network transfer
into a fixed startup cost and a payload-proportional bandwidth cost. The crossover message size 𝑀 cross =𝛼×𝛽 determines
which cost dominates.
- Algorithm selection depends on message size relative to 𝑀 cross: ring for large messages (gradients), tree for small
messages (barriers), and hierarchical two-level schemes for multi-node clusters.
- Ring-based collectives (AllReduce, AllGather, ReduceScatter, AllToAll) achieve bandwidth-optimal communication with a
(𝑁 -1)/𝑁 factor, but their latency term grows linearly with GPU count. Tree-based algorithms trade bandwidth for
logarithmic latency scaling.

- Pipeline bubble fraction 𝑏 = (𝑃 - 1)/(𝑃 - 1 + 𝑀) is the fundamental overhead of pipeline parallelism. The practical
rule 𝑀 ≥ 4𝑃 keeps bubbles below 20 percent, and interleaved scheduling with 𝑉 virtual stages reduces bubbles by a factor
of 𝑉 .
- Every communication cost model in this appendix derives from two hardware parameters ( 𝛼 and 𝛽 ) and two workload
parameters ( 𝑀 and 𝑁 ). Measuring these four numbers for a cluster yields a complete first-order prediction of
distributed training overhead.
- Gradient compression is profitable when the codec overhead (encode + decode) is less than the communication time
saved. At high compression ratios in the bandwidthdominated regime, nearly the entire uncompressed AllReduce time is
available as overhead budget-but convergence impact must always be validated.

