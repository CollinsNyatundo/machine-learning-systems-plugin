# Glossary — Machine Learning Systems

> Curated from 44 chapters, **111 definitions**. Sorted alphabetically by term.

Each entry links to its source chapter. Use `Ctrl+F` to search.

## #

### ## B

**Full heading:** Definition 5.2 (Vol 1)

**Source:** `ch05.md • **Chapter:** Chapter 5: Neural Computation & Training Mechanics`

## B  ### Backpropagation    Backpropagation Backpropagation is the efficient application of the Chain Rule to a computational graph to solve the Credit Assignment Problem . 1. Significance (quantitative) : It propagates error signals from output to input, computing the gradient of the loss with respect to every parameter in one backward traversal of the computation graph. 2. Distinction (durable) : Unlike Numerical Differentiation (which requires one perturbed forward pass per parameter), Backpropagation is a Global Gradie

**Location:** [ch05.md • **Chapter:** Chapter 5: Neural Computation & Training Mechanics](ch05.md • **Chapter:** Chapter 5: Neural Computation & Training Mechanics)

---

### ## C

**Full heading:** Definition 5.5 (Vol 2)

**Source:** `v2_ch05.md • **Chapter:** Chapter 5: Data Storage — The Fuel Line`

## C  ### Checkpoint storm    Checkpoint storm - Checkpoint Storm is a burst of synchronized network and storage traffic that occurs when all nodes in a training fleet save model state simultaneously. 1. Significance (quantitative) : The storm magnitude scales as 𝑇 write = 𝑁 × per-node-shard / BWfabric . For a 70B-parameter model in FP16 (140 GB of weights) trained across 1,000 nodes with vanilla data parallelism (every node holding its own complete copy), a naive checkpoint generates 140 TB of simultaneous writes; at 100 GB

**Location:** [v2_ch05.md • **Chapter:** Chapter 5: Data Storage — The Fuel Line](v2_ch05.md • **Chapter:** Chapter 5: Data Storage — The Fuel Line)

---

### ## D

**Full heading:** Definition 4.4 (Vol 1)

**Source:** `ch04.md • **Chapter:** Chapter 4: Data Engineering & Pipeline Architecture`

## D  ### Data Debt    Data Debt Data Debt is the compound interest of implicit coupling and missing documentation across the data stack. 1. **Significance (Quantitative)**: It manifests as silent degradation, where the cost of maintenance scales superlinearly with system age due to unmanaged dependencies and distribution shifts: \[ \mathcal{D}(P_t \parallel P_0) \] 2. **Distinction (Durable)**: Unlike technical debt in code, which manifests as slower development velocity, data debt manifests as lower model accuracy e

**Location:** [ch04.md • **Chapter:** Chapter 4: Data Engineering & Pipeline Architecture](ch04.md • **Chapter:** Chapter 4: Data Engineering & Pipeline Architecture)

---

### ## E

**Full heading:** Definition 2.3 (Vol 1)

**Source:** `ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)`

## E  ### Edge ML    Edge ML - Edge Machine Learning is the deployment paradigm optimized for Latency Determinism and Data Locality by locating computation physically adjacent to data sources. 1. Significance (quantitative) : It circumvents the Distance Penalty (𝐿 lat ) of the cloud, trading elastic scale for a fixed Local Compute Capacity (𝑅 peak ) . 2. Distinction (durable) : Unlike Cloud ML, which prioritizes Throughput, Edge ML prioritizes Determinism and privacy. Unlike TinyML, Edge ML may still use workstation

**Location:** [ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)](ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML))

---

### ## F

**Full heading:** Definition 4.6 (Vol 2)

**Source:** `v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics`

## F  ### Fat    Fat-tree Fat-Tree is a hierarchical network topology in which the number of parallel paths-and therefore aggregate cross-sectional capacity-increases at each switch tier toward the spine, providing full bisection bandwidth and multiple equal-cost routes between any two nodes (Al-Fares et al. 2008). 1. Significance (quantitative) : Ak-ary fat-tree built from radix𝑘 switches supports 𝑘 2 /2 hosts in a two-tier (pod) configuration and 𝑘 3 /4 hosts in a three-tier configuration with full bisection b

**Location:** [v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics](v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics)

---

### ## G

**Full heading:** Definition 5.4 (Vol 2)

**Source:** `v2_ch05.md • **Chapter:** Chapter 5: Data Storage — The Fuel Line`

## G  ### GPU Direct Storage    GPU Direct Storage GPU Direct Storage (GDS) is a technology that enables a direct DMA path between NVMe storage devices and GPU memory, bypassing the host CPU and system DRAM. 2. Distinction (durable) : Unlike Traditional I/O, where every byte must be processed by the CPU and stored in kernel buffers, GDS provides Direct Memory Access between the storage controller and the accelerator. 1. Significance (quantitative) : It eliminates the 'Bounce Buffer' through system memory, reducing data loading

**Location:** [v2_ch05.md • **Chapter:** Chapter 5: Data Storage — The Fuel Line](v2_ch05.md • **Chapter:** Chapter 5: Data Storage — The Fuel Line)

---

### ## H

**Full heading:** Definition 11.1 (Vol 1)

**Source:** `ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs`

## H  ### Hardware Acceleration    Hardware Acceleration **Hardware Acceleration** is the practice of replacing general-purpose processor logic with domain-specific silicon optimized for a narrow class of operations, trading programmability for compute density (\(R_{\text{peak}}\)) and energy efficiency (\(\eta_{\text{hw}}\)) gains that regular, data-parallel workloads like matrix multiplication can exploit. * **Throughput Scaling:** An NVIDIA A100 GPU delivers 312 TFLOPS of BF16 tensor compute, compared to 1–2 TFLOPS on server-c

**Location:** [ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs](ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs)

---

### ## I

**Full heading:** Definition 4.9 (Vol 2)

**Source:** `v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics`

## I  ### Incast    Incast Incast is a many-to-one traffic pattern in which a large number of senders simultaneously transmit data to a single receiver port, concentrating line-rate traffic from multiple sources into a single switch queue and causing buffer overflow even when the rest of the fabric is uncongested. 1. Significance (quantitative) : In the reduce phase of AllReduce, every participating GPU simultaneously sends gradients toward the same aggregation points. With 256 senders each at 50 GB/s targeting one

**Location:** [v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics](v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics)

---

### ## K

**Full heading:** Definition 11.2 (Vol 2)

**Source:** `v2_ch11.md • **Chapter:** Chapter 11: Inference at Scale (Vol 2)`

## K  ### KV cache    KV cache - KV Cache is a memory buffer that stores previously computed Key and Value attention vectors to avoid redundant computation during autoregressive generation. 1. Significance (quantitative) : It reduces per-token computation from 𝑂(𝑡 2 ) to 𝑂(𝑡) , making generation feasible for long sequences. However, it grows linearly with sequence length and batch size, often exceeding the memory footprint of the model weights and becoming the primary constraint on Concurrent Capacity . 2. Distinctio

**Location:** [v2_ch11.md • **Chapter:** Chapter 11: Inference at Scale (Vol 2)](v2_ch11.md • **Chapter:** Chapter 11: Inference at Scale (Vol 2))

---

### ## L

**Full heading:** Definition 13.2 (Vol 1)

**Source:** `ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)`

## L  ### Latency budget    Latency budget Latency Budget is the time capital allocated to a request, strictly bounded by the end-to-end service level objective (SLO) . 7 gRPC (gRPC Remote Procedure Call) : Evolved from Google's internal Stubby framework, gRPC was designed to minimize the overhead of the billions of interservice calls made per second. It achieves this by pairing HTTP/2 for persistent connection multiplexing with Protobuf for efficient binary serialization, directly addressing the handshake and parsing late

**Location:** [ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)](ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory))

---

### ## M

**Full heading:** Definition 11.3 (Vol 1)

**Source:** `ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs`

## M  ### Machine Learning Accelerator    Machine Learning Accelerator An **ML Accelerator** is a domain-specific processor whose silicon is designed primarily for the dense matrix operations and regular data flow of neural networks, achieving high peak throughput (\(R_{\text{peak}}\)) and memory bandwidth utilization by dedicating die area to arithmetic units rather than general-purpose control logic. | Era | Bottleneck Target | Architecture Examples | Characteristics | | :--- | :--- | :--- | :--- | | **1980s** | Precision (Scalar FP)

**Location:** [ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs](ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs)

---

### ## N

**Full heading:** Definition 2.7 (Vol 2)

**Source:** `v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure`

## N  ### Node    Node Node is a physical server chassis that aggregates multiple accelerators-typically 8-through a high-speed intra-node interconnect (NVLink or ICI), creating the fundamental boundary between high-bandwidth local communication and the order-of-magnitude slower inter-node network fabric. 2. Distinction (durable) : Unlike a single accelerator (which provides fast HBM bandwidth but limited capacity), a node aggregates 8 × the HBM capacity and 8 × the compute of a single chip - enough to place larg

**Location:** [v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure](v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure)

---

### ## O

**Full heading:** Definition 12.1 (Vol 2)

**Source:** `v2_ch12.md • **Chapter:** Chapter 12: Edge Intelligence (Vol 2)`

## O  ### On-device learning    On-device learning On-Device Learning is the local training or adaptation of machine learning models directly on deployed hardware without requiring server connectivity. 1. Significance (quantitative) : It enables Hyper-Personalization andautonomousoperation under severe resource constraints. Within the iron law, on-device learning must maximize Energy Efficiency (𝜂 hw ) because every gradient update consumes limited battery power and must compete with other system tasks for Peak Throughput (𝑅 p

**Location:** [v2_ch12.md • **Chapter:** Chapter 12: Edge Intelligence (Vol 2)](v2_ch12.md • **Chapter:** Chapter 12: Edge Intelligence (Vol 2))

---

### ## P

**Full heading:** Definition 5.1 (Vol 2)

**Source:** `v2_ch05.md • **Chapter:** Chapter 5: Data Storage — The Fuel Line`

## P  ### Parallel file system    Parallel file system Parallel File System (PFS) is a distributed storage architecture that stripes data across many storage servers to provide aggregate throughput exceeding the capacity of any single device. 1. Significance (quantitative) : APFS aggregates BW io linearly with the number of storage servers (Object Storage Servers). A Lustre cluster with 20 OSS nodes each delivering 10 GB/s provides 200 GB/s aggregate, versus a single NAS server capped at 10 GB/s, enabling a training job to load

**Location:** [v2_ch05.md • **Chapter:** Chapter 5: Data Storage — The Fuel Line](v2_ch05.md • **Chapter:** Chapter 5: Data Storage — The Fuel Line)

---

### ## Q

**Full heading:** Definition 10.3 (Vol 1)

**Source:** `ch10.md • **Chapter:** Chapter 10: Model Compression (Pruning, Quantization, Distillation)`

## Q  ### Quantization    Quantization - Quantization is the reduction of Information Fidelity by mapping high-precision continuous values to a lower-precision discrete set. 1. Significance (quantitative) : It reduces the Memory Bandwidth ( BW ) and energy consumption by 4 × (FP32 to INT8) or more, exploiting the inherent robustness of neural networks to low-precision arithmetic. 2. Distinction (durable) : Unlike Pruning, which reduces the Count of parameters, Quantization reduces the Bit-Depth of every parameter and act

**Location:** [ch10.md • **Chapter:** Chapter 10: Model Compression (Pruning, Quantization, Distillation)](ch10.md • **Chapter:** Chapter 10: Model Compression (Pruning, Quantization, Distillation))

---

### ## R

**Full heading:** Definition 2.9 (Vol 2)

**Source:** `v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure`

## R  ### Rack    Rack Rack is the physical infrastructure unit-a standardized 42U enclosure-that houses multiple compute nodes, a Top-of-Rack (ToR) switch (the first network aggregation point connecting all nodes in the rack to the broader cluster fabric), power distribution units, and cooling distribution manifolds, defining the granularity at which power and cooling capacity must be provisioned. 1. Significance (quantitative) : AI rack power density has grown dramatically: a rack of 4 DGXH100nodes contains 32

**Location:** [v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure](v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure)

---

### ## S

**Full heading:** Definition 14.1 (Vol 2)

**Source:** `v2_ch14.md • **Chapter:** Chapter 14: Security & Privacy (Vol 2)`

## S  ### Security    Security Security is the set of system properties (confidentiality, integrity, and availability) that protect an ML system's data, model weights, and inference pipeline from intentional adversarial actions, spanning both the infrastructure layer (network intrusion, credential theft) and the algorithmic layer (model extraction, prompt injection, adversarial examples). 1. Significance (quantitative) : Security failures operate on both surfaces simultaneously. At the infrastructure layer, a stolen

**Location:** [v2_ch14.md • **Chapter:** Chapter 14: Security & Privacy (Vol 2)](v2_ch14.md • **Chapter:** Chapter 14: Security & Privacy (Vol 2))

---

### ## T

**Full heading:** Definition 14.2 (Vol 1)

**Source:** `ch14.md • **Chapter:** Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)`

## T  ### Technical debt in ML    Technical debt in ML Technical Debt in Machine Learning is the high interest rate paid on System Complexity and Implicit Dependencies . 1. Significance (quantitative) : It arises because ML systems have all the maintenance problems of traditional code plus new ML-specific drivers: Entanglement (changing one feature affects everything), Correction Cascades, and Undeclared Consumers . 2. Distinction (durable) : Unlike software technical debt (which manifests as lower productivity), ML technical de

**Location:** [ch14.md • **Chapter:** Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)](ch14.md • **Chapter:** Chapter 14: ML Operations (MLOps, Drift, Edge Fleets))

---

### ## W

**Full heading:** Definition 2.11 (Vol 2)

**Source:** `v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure`

## W  ### Warehouse    Warehouse-scale computer (WSC) Warehouse-Scale Computer (WSC) is a building-scale computing system in which thousands of servers are operated as a single coherent machine-with the network fabric serving as the system bus, distributed storage as the disk subsystem, and a cluster orchestrator as the operating system-enabling training workloads that would be physically impossible on any single machine. 1. Significance (quantitative) : AWSCof 10,000 H100 GPUs delivers approximately 3.12 ExaFLOP/s BF

**Location:** [v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure](v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure)

---

## A

### AI Engineering

**Full heading:** Definition 1.3 (Vol 1)

**Source:** `ch01.md • **Chapter:** Chapter 1: Introduction to ML Systems`

AI Engineering AI Engineering is the engineering discipline of designing, deploying, and maintaining systems whose outputs are inherently probabilistic (stochastic) to meet deterministic reliability targets by simultaneously satisfying constraints on all three D·A·M axes (Data quality, Algorithm correctness, Machine efficiency) in production. 1. Significance (quantitative) : MLResearch typically optimizes only the Algorithm axis ( 𝑂 and convergence). AI Engineering jointly optimizes all three: i

**Location:** [ch01.md • **Chapter:** Chapter 1: Introduction to ML Systems](ch01.md • **Chapter:** Chapter 1: Introduction to ML Systems)

---

### AI Memory Wall

**Full heading:** Definition 11.4 (Vol 1)

**Source:** `ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs`

AI Memory Wall The **AI Memory Wall** is the performance constraint that arises when arithmetic throughput (\(R_{\text{peak}}\)) outpaces memory bandwidth (\(\text{BW}\)). It dictates that system performance is bounded by the energy and latency cost of data movement rather than FLOP capacity, representing the point where the data volume term (\(\frac{D_{\text{vol}}}{\text{BW}}\)) in the Iron Law of ML dominates total execution time.

**Location:** [ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs](ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs)

---

### Algorithmic fairness

**Full heading:** Definition 17.2 (Vol 2)

**Source:** `v2_ch17.md • **Chapter:** Chapter 17: Responsible Engineering (Vol 2)`

Algorithmic fairness Algorithmic Fairness is the measurable property that a model's error distribution or outcomes are invariant (or bounded in variation) across protected demographic groups. 1. Significance (quantitative) : It transforms fairness from an intuition into a MultiObjective Optimization problem. Within the iron law, achieving fairness often requires trading off total accuracy ( Accuracy ) for Group-Specific Calibration, ensuring that the system's benefits and harms are distributed e

**Location:** [v2_ch17.md • **Chapter:** Chapter 17: Responsible Engineering (Vol 2)](v2_ch17.md • **Chapter:** Chapter 17: Responsible Engineering (Vol 2))

---

### Arithmetic Intensity

**Full heading:** Definition 11.5 (Vol 1)

**Source:** `ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs`

Arithmetic Intensity **Arithmetic Intensity (AI)** is the ratio of floating-point operations to bytes of memory traffic for a given computation (FLOP/byte), determining whether the workload is limited by compute throughput (\(R_{\text{peak}}\)) or memory bandwidth (\(\text{BW}\)) on a given accelerator. \[ \text{AI} = \frac{\text{FLOPs}}{\text{Bytes Transferred}} \]

**Location:** [ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs](ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs)

---

### Attention Mechanism

**Full heading:** Definition 6.5 (Vol 1)

**Source:** `ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys)`

Attention Mechanism An **attention mechanism** is a sequence-processing operation that computes a weighted sum of value vectors, where the weights are dynamically calculated via similarity scores between a query vector and a set of key vectors. * **Direct Connectivity:** Information flows between any two positions in $O(1)$ depth, eliminating the $O(N)$ sequential path length of RNNs. * **Quadratic Wall:** Materializing the $N \times N$ attention weight matrix requires $O(N^2)$ memory and comput

**Location:** [ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys)](ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys))

---

## B

### Bandwidth hierarchy

**Full heading:** Definition 2.8 (Vol 2)

**Source:** `v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure`

Bandwidth hierarchy Bandwidth Hierarchy is the physical ordering of data transfer rates across system boundaries, from on-chip SRAM (fastest) to the wide-area network (slowest). 1. Significance (quantitative) : It dictates the Scaling Ceiling for distributed training. At each physical boundary (die edge, package edge, chassis, rack), the Effective Bandwidth ( BW ) drops by approximately one order of magnitude while latency (𝐿 lat ) increases. 2. Distinction (durable) : Unlike Idealized Networkin

**Location:** [v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure](v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure)

---

### Batch processing

**Full heading:** Definition 8.3 (Vol 1)

**Source:** `ch08.md • **Chapter:** Chapter 8: Staged Model Training & Parallelism`

Batch processing 1. Significance (quantitative) : Throughput increases with batch size up to the critical batch size, beyond which additional examples provide diminishing gradient quality without proportional convergence benefit. For ResNet-50 on ImageNet, empirical studies find the critical batch size near 𝐵≈8,192: at this batch size, throughput approaches 𝑅 peak while validation accuracy is preserved; larger batches require learning rate scaling (linear rule: lr ∝𝐵 ) to compensate for reduced

**Location:** [ch08.md • **Chapter:** Chapter 8: Staged Model Training & Parallelism](ch08.md • **Chapter:** Chapter 8: Staged Model Training & Parallelism)

---

### Bisection bandwidth

**Full heading:** Definition 4.4 (Vol 2)

**Source:** `v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics`

Bisection bandwidth Bisection Bandwidth is a network topology metric defined as the minimum aggregate link capacity crossing any partition that divides the cluster into two equal halves, representing the worst-case throughput ceiling for all-to-all communication patterns such as AllReduce. 1. Significance (quantitative) : Bisection bandwidth directly sets the BW ceiling in the iron law for global synchronization. A 1,024-GPU fat-tree with 400 Gb/s (50 GB/s) links at 1:1 subscription provides 512

**Location:** [v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics](v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics)

---

### Block

**Full heading:** Definition 10.2 (Vol 2)

**Source:** `v2_ch10.md • **Chapter:** Chapter 10: Performance Engineering (Vol 2)`

Block-wise quantization 1. Significance (quantitative) : With block size 𝐵 block =64 and 𝑏 = 4 bits, weights compress from 16 bits to 4 bits-a 4 × memory reduction-while each FP16 scale adds 16/64 = 0.25 bits per weight. This yields an effective bit-width of 4.25 bits per weight: 6.25 percent overhead relative to the INT4 payload, or about 1.6 percent of the original FP16 weight size. Block-wise Quantization is a quantization scheme that partitions a weight tensor into nonoverlapping groups of 𝐵

**Location:** [v2_ch10.md • **Chapter:** Chapter 10: Performance Engineering (Vol 2)](v2_ch10.md • **Chapter:** Chapter 10: Performance Engineering (Vol 2))

---

## C

### Checkpointing

**Full heading:** Definition 8.1 (Vol 2)

**Source:** `v2_ch08.md • **Chapter:** Chapter 8: Fault Tolerance and Reliability (Vol 2)`

Checkpointing Checkpointing is the periodic serialization of the complete training state (parameters, optimizer state, and data loader position) to persistent storage. 1. Significance (quantitative) : It minimizes the Lost Work after a system failure. Within the iron-law framework formalized in Section 10.1.1, checkpointing creates an I/O Overhead that reduces the total training throughput (𝜂 hw ) , with the optimal interval (𝜏 opt ) governed by the Young-Daly Formula (𝜏 opt =√2⋅𝑇 write ⋅ MTBF )

**Location:** [v2_ch08.md • **Chapter:** Chapter 8: Fault Tolerance and Reliability (Vol 2)](v2_ch08.md • **Chapter:** Chapter 8: Fault Tolerance and Reliability (Vol 2))

---

### Cloud ML

**Full heading:** Definition 2.2 (Vol 1)

**Source:** `ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)`

Cloud ML - Cloud Machine Learning is the deployment paradigm that optimizes for Resource Elasticity by decoupling computational capacity from physical location. 1. Significance (quantitative) : It enables systems to scale resources (𝑅 peak ) proportional to workload variance, allowing for bursts of peta-flops that would be economically unfeasible to maintain locally. 3. Common pitfall: Afrequent misconception is that cloud ML is 'unlimited compute.' In reality, it is constrained by the distance

**Location:** [ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)](ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML))

---

### Cold start

**Full heading:** Definition 13.4 (Vol 1)

**Source:** `ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)`

Cold start Cold Start is the initialization latency incurred when instantiating a new model replica. 1. Significance (quantitative) : It represents the fixed cost of state hydration (loading weights, compiling graphs), which can take seconds or minutes, effectively blocking the system's ability to scale elastically in response to traffic bursts. 2. Distinction (durable) : Unlike inference latency (𝐿 lat ) , which is a per-request cost, cold start is a per-replica cost that occurs only during dep

**Location:** [ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)](ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory))

---

### Collective operation

**Full heading:** Definition 7.3 (Vol 2)

**Source:** `v2_ch07.md • **Chapter:** Chapter 7: Collective Communication`

Collective operation Collective Operation is a distributed communication pattern in which all processes in a group participate simultaneously to aggregate, broadcast, or redistribute data-with the correctness guarantee that every participant receives the same result regardless of message ordering or arrival time. 1. Significance (quantitative) : The right collective algorithm determines whether communication scales with cluster size or remains constant. Ring AllReduce achieves bandwidthoptimal 2

**Location:** [v2_ch07.md • **Chapter:** Chapter 7: Collective Communication](v2_ch07.md • **Chapter:** Chapter 7: Collective Communication)

---

### Compute Infrastructure

**Full heading:** Definition 2.5 (Vol 2)

**Source:** `v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure`

Model FLOPs utilization (MFU) Model FLOPs Utilization (MFU) is the ratio of a model's theoretical FLOP count per training step-calculated from architecture parameters alone-to the product of hardware peak throughput and elapsed wall-clock time, measuring what fraction of the hardware's theoretical capacity is doing useful model computation rather than overhead. 2. Distinction (durable) : Unlike hardware utilization (the fraction of clock cycles during which the GPU reports being 'busy'), MFU cou

**Location:** [v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure](v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure)

---

### Concept drift

**Full heading:** Definition 15.2 (Vol 2)

**Source:** `v2_ch15.md • **Chapter:** Chapter 15: Robust AI`

Concept drift Concept Drift is the subtype of distribution shift (see Section 15.4.1) in which the statistical relationship 𝑃(𝑌 |𝑋) changes over time, meaning the decision boundary itself becomes incorrect rather than merely the input distribution. Its sibling is data drift (see Section 13.4), in which 𝑃(𝑋) changes while 𝑃(𝑌 |𝑋) remains stable. Figure 15.9: Types of Distribution Shift: Comparison of covariate shift ( 𝑃(𝑋) changes), label shift ( 𝑃(𝑦) changes), and concept drift ( 𝑃(𝑦|𝑥) changes)

**Location:** [v2_ch15.md • **Chapter:** Chapter 15: Robust AI](v2_ch15.md • **Chapter:** Chapter 15: Robust AI)

---

### Consistency Imperative

**Full heading:** Definition 4.2 (Vol 2)

**Source:** `v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics`

Remote direct memory access (RDMA) Remote Direct Memory Access (RDMA) is a networking technology that allows one machine to read or write the memory of another machine directly, bypassing the operating system kernel and CPU of both endpoints by offloading transport processing to the network interface card. 1. Significance (quantitative) : RDMAreduces end-to-end message latency from the 50-100 μs typical of kernel TCP to approximately 1-2 μs, cutting the 𝐿 lat term in the iron law by 25-50 × . Fo

**Location:** [v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics](v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics)

---

### Continuous batching

**Full heading:** Definition 11.1 (Vol 2)

**Source:** `v2_ch11.md • **Chapter:** Chapter 11: Inference at Scale (Vol 2)`

Continuous batching - Continuous Batching is a serving strategy that decouples batch membership from iteration boundaries, allowing new requests to enter and completed ones to exit at every decode step. 1. Significance (quantitative) : It maximizes the system throughput (𝜂 hw ) by eliminating the padding waste and head-of-line blocking inherent in static batching. It ensures the GPU remains saturated even when requests have widely varying sequence lengths. 2. Distinction (durable) : Unlike stati

**Location:** [v2_ch11.md • **Chapter:** Chapter 11: Inference at Scale (Vol 2)](v2_ch11.md • **Chapter:** Chapter 11: Inference at Scale (Vol 2))

---

### Convolutional Neural Network (CNN)

**Full heading:** Definition 6.3 (Vol 1)

**Source:** `ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys)`

Convolutional Neural Network (CNN) A **CNN** is a neural network architecture defined by translation equivariance and spatial locality, restricting receptive fields to local spatial neighborhoods and sharing weights across all grid positions. * **Translation Equivariance:** A function $f$ is equivariant to translation $T$ if shifting the input results in an equivalent shift in the output: \[ f(T_v(x)) = T_v(f(x)) \] * **Translation Invariance:** Shifting the input does not alter the output: \[ f

**Location:** [ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys)](ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys))

---

## D

### Data drift

**Full heading:** Definition 14.3 (Vol 1)

**Source:** `ch14.md • **Chapter:** Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)`

Data drift 1. Significance (quantitative) : It represents a violation of the i.i.d. assumption (independent and identically distributed), causing accuracy to erode monotonically with the distributional divergence (𝒟(𝑃 𝑡 ‖𝑃 0 )) , empirically modeled as Accuracy (𝑡) ≈ Accuracy 0 -𝜆⋅𝒟(𝑃 𝑡 ‖𝑃 0 ) with 𝜆 fit per deployment. Because 𝑃(𝑌 |𝑋) is unchanged, retraining on fresh 𝑃(𝑋) data can recover performance (when the new input distribution overlaps the original support), unlike concept drift, where t

**Location:** [ch14.md • **Chapter:** Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)](ch14.md • **Chapter:** Chapter 14: ML Operations (MLOps, Drift, Edge Fleets))

---

### Data Engineering (Vol 1)

**Full heading:** Definition 4.1 (Vol 1)

**Source:** `ch04.md • **Chapter:** Chapter 4: Data Engineering & Pipeline Architecture`

Data Engineering Data Engineering is the infrastructure layer that manages the lifecycle of data from source to model, encompassing acquisition, transformation, storage, and governance. 1. **Significance (Quantitative)**: Its critical function is ensuring *Training-Serving Consistency* and preventing *Silent Degradation* by decoupling the model from raw data volatility. Within the iron law, it governs the Data Volume (\(D_{\text{vol}}\)) and ensures that it remains representative of the target d

**Location:** [ch04.md • **Chapter:** Chapter 4: Data Engineering & Pipeline Architecture](ch04.md • **Chapter:** Chapter 4: Data Engineering & Pipeline Architecture)

---

### Data Engineering (Vol 2)

**Full heading:** Definition 4.1 (Vol 2)

**Source:** `v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics`

PAM4 signaling PAM4 Signaling is an electrical modulation scheme that uses four distinct voltage levels to encode two bits per symbol period, doubling the data rate achievable over a given physical medium without requiring a higher symbol rate. 1. Significance (quantitative) : PAM4 enables 400 Gb/s and 800 Gb/s link speeds that sustain the BW required for large-scale gradient synchronization. However, the reduced gap between voltage levels increases susceptibility to noise, requiring Forward Err

**Location:** [v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics](v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics)

---

### Data parallelism

**Full heading:** Definition 6.2 (Vol 2)

**Source:** `v2_ch06.md • **Chapter:** Chapter 6: Distributed Training Systems`

Data parallelism Data Parallelism is a distributed training strategy in which each worker holds a complete replica of the model and processes an independent shard of the minibatch, then synchronizes gradient updates via AllReduce so all replicas apply identical parameter changes each step. 2. Distinction (durable) : Unlike model parallelism, where parameters are partitioned so no single worker holds the full model, data parallelism requires every worker to have 1. Significance (quantitative) : W

**Location:** [v2_ch06.md • **Chapter:** Chapter 6: Distributed Training Systems](v2_ch06.md • **Chapter:** Chapter 6: Distributed Training Systems)

---

### Data poisoning

**Full heading:** Definition 15.4 (Vol 2)

**Source:** `v2_ch15.md • **Chapter:** Chapter 15: Robust AI`

Data poisoning Data Poisoning is the corruption of training data to compromise model behavior at inference time, either by injecting malicious samples or modifying existing labels. 1. Significance (quantitative) : It undermines the foundational assumption of Data Integrity . Even a small fraction of poisoned samples (for example, <1 percent) can create Backdoors or systematic biases that remain latent until triggered by specific inputs during serving. 2. Distinction (durable) : Unlike Adversaria

**Location:** [v2_ch15.md • **Chapter:** Chapter 15: Robust AI](v2_ch15.md • **Chapter:** Chapter 15: Robust AI)

---

### Data selection

**Full heading:** Definition 9.1 (Vol 1)

**Source:** `ch09.md • **Chapter:** Chapter 9: Data Selection & Active Learning`

Data selection Data Selection is the process of maximizing the Information-Compute Ratio of a training dataset. 2. Distinction (durable) : Unlike data engineering, which focuses on the cleanliness and consistency of data, data selection focuses on the informativeness and diversity of the samples. 1. Significance (quantitative) : It identifies the smallest subset of data sufficient to define the decision boundary, reducing the total operations (𝑂) of the iron law by eliminating redundant or noisy

**Location:** [ch09.md • **Chapter:** Chapter 9: Data Selection & Active Learning](ch09.md • **Chapter:** Chapter 9: Data Selection & Active Learning)

---

### Deep Learning

**Full heading:** Definition 5.1 (Vol 1)

**Source:** `ch05.md • **Chapter:** Chapter 5: Neural Computation & Training Mechanics`

Deep Learning **Deep Learning** is the computational paradigm of Hierarchical Feature Learning from raw data. 1. **Quantitative Significance**: By stacking nonlinear transformations, it replaces manual Feature Engineering with **Architecture Engineering**, enabling models to scale performance with both Data Volume (\(D_{\text{vol}}\)) and Peak Compute (\(R_{\text{peak}}\)). 2. **Durable Distinction**: Unlike Shallow Learning, which learns a single feature transformation, Deep Learning learns a H

**Location:** [ch05.md • **Chapter:** Chapter 5: Neural Computation & Training Mechanics](ch05.md • **Chapter:** Chapter 5: Neural Computation & Training Mechanics)

---

### Demographic parity

**Full heading:** Definition 17.3 (Vol 2)

**Source:** `v2_ch17.md • **Chapter:** Chapter 17: Responsible Engineering (Vol 2)`

Demographic parity 1. Significance (quantitative) : It is the simplest and most restrictive fairness metric. It requires the model to produce Equal Outcomes across groups, regardless of the underlying base-rate differences in the dataset. Demographic Parity is the fairness constraint where a model's positive prediction rate is independent of group membership (𝑃( 𝑌 = 1 ∣ 𝐴 = 𝑎) = 𝑃( 𝑌 = 1 ∣ 𝐴 = 𝑏)) . ̂ ̂ 2. Distinction (durable) : Unlike Equalized Odds (which focuses on error rates like False Pos

**Location:** [v2_ch17.md • **Chapter:** Chapter 17: Responsible Engineering (Vol 2)](v2_ch17.md • **Chapter:** Chapter 17: Responsible Engineering (Vol 2))

---

### Distributed training

**Full heading:** Definition 6.1 (Vol 2)

**Source:** `v2_ch06.md • **Chapter:** Chapter 6: Distributed Training Systems`

Distributed training Distributed Training is a training methodology that partitions the optimization loop across multiple compute nodes-distributing either data, model layers, or individual tensor operationsand coordinates their outputs through synchronized communication primitives to produce a single coherent model. 1. Significance (quantitative) : Distributed training becomes necessary when a model's memory requirement exceeds a single accelerator's capacity. GPT-3 (175B parameters) requires a

**Location:** [v2_ch06.md • **Chapter:** Chapter 6: Distributed Training Systems](v2_ch06.md • **Chapter:** Chapter 6: Distributed Training Systems)

---

### Dynamic batching

**Full heading:** Definition 13.5 (Vol 1)

**Source:** `ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)`

Dynamic batching Dynamic Batching is the runtime optimization of trading Latency for Throughput under stochastic arrival patterns. 2. Distinction (durable) : Unlike Static Batching, which is fixed during training, Dynamic Batching adaptively adjusts the batch size at Inference Time based on real-time traffic volume. 1. Significance (quantitative) : By buffering requests into a Batching Window, the scheduler amortizes fixed overheads (𝐿 lat ) across multiple inputs, pushing the system away from t

**Location:** [ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)](ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory))

---

### D·A·M Taxonomy

**Full heading:** Definition 1.2 (Vol 1)

**Source:** `ch01.md • **Chapter:** Chapter 1: Introduction to ML Systems`

The D·A·M taxonomy 1. Significance (quantitative) : The diagnostic power is concrete. A ResNet-50 inference run at batch size one is memory-bandwidth-bound (Machine axis): the A100's 2 terabytes per second bandwidth moves 25 megabytes of weights per forward pass in 12.5 μs, while the 4 GFLOP compute finishes in 2 μs. This 6 × gap means hardware upgrades to 𝑅 peak yield no improvement until the bandwidth bottleneck is resolved first. The D·A·M Taxonomy is a diagnostic framework that classifies an

**Location:** [ch01.md • **Chapter:** Chapter 1: Introduction to ML Systems](ch01.md • **Chapter:** Chapter 1: Introduction to ML Systems)

---

## E

### Elastic training

**Full heading:** Definition 9.2 (Vol 2)

**Source:** `v2_ch09.md • **Chapter:** Chapter 9: Fleet Orchestration (Vol 2)`

Elastic training - Elastic Training is the capability of a distributed training job to dynamically adjust its worker count during execution without requiring a full restart. 1. Significance (quantitative) : It maximizes the System Duty Cycle (𝜂 hw ) by allowing training to continue through node failures and by absorbing idle capacity in the cluster. It requires Learning Rate Recalibration and gradient accumulation adjustment to maintain mathematical consistency as the global batch size changes.

**Location:** [v2_ch09.md • **Chapter:** Chapter 9: Fleet Orchestration (Vol 2)](v2_ch09.md • **Chapter:** Chapter 9: Fleet Orchestration (Vol 2))

---

## F

### Feature Store (Vol 1)

**Full heading:** Definition 4.3 (Vol 1)

**Source:** `ch04.md • **Chapter:** Chapter 4: Data Engineering & Pipeline Architecture`

Feature Store A Feature Store is the architectural layer that centralizes the management of machine learning features, decoupling feature computation from consumption. 1. **Significance (Quantitative)**: It enforces point-in-time correctness, ensuring that historical data used for training (\(x_{t-\Delta}\)) is computed with identical logic to the real-time data served at inference (\(x_t\)), eliminating training-serving skew by design. 2. **Distinction (Durable)**: Unlike a general-purpose data

**Location:** [ch04.md • **Chapter:** Chapter 4: Data Engineering & Pipeline Architecture](ch04.md • **Chapter:** Chapter 4: Data Engineering & Pipeline Architecture)

---

### Feature Store (Vol 2)

**Full heading:** Definition 4.3 (Vol 2)

**Source:** `v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics`

α-β model (Hockney Model) 1. Significance (quantitative) : Topology choice directly shifts 𝛼 and 𝛽 . An InfiniBand HDR link has 𝛼 ≈ 1𝜇 s and 𝛽 ≈ 25 GB/s, yielding 𝑛 ∗ ≈25 KB: messages smaller than 25 KB are latency-bound and benefit from topology designs that minimize hop count; messages larger than 25 KB are bandwidth-bound and benefit from fat-tree bisection bandwidth. In a ring topology, the worst-case path traverses ⌊𝑁/2⌋ hops, so effective startup latency scales as 𝛼 ring ≈⌊𝑁/2⌋⋅𝛼 hop: for

**Location:** [v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics](v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics)

---

### Federated learning

**Full heading:** Definition 12.2 (Vol 2)

**Source:** `v2_ch12.md • **Chapter:** Chapter 12: Edge Intelligence (Vol 2)`

Federated learning Federated Learning is a decentralized training paradigm where distributed devices collaboratively train a shared model using local data while exchanging only model updates (gradients or weights). 1. Significance (quantitative) : It transforms the constraint of Data Locality into a privacy feature. Within the iron law, federated learning is constrained by the Wide-Area Bandwidth (BW) and the extreme Heterogeneity of the Fleet, where device-specific efficiency (𝜂 hw ) and availa

**Location:** [v2_ch12.md • **Chapter:** Chapter 12: Edge Intelligence (Vol 2)](v2_ch12.md • **Chapter:** Chapter 12: Edge Intelligence (Vol 2))

---

### FinOps for ML

**Full heading:** Definition 13.1 (Vol 2)

**Source:** `v2_ch13.md • **Chapter:** Chapter 13: ML Operations at Scale`

FinOps for ML FinOps for ML is the practice of treating compute cost as a first-class engineering constraintmeasured in real-time per experiment and model, and optimized jointly with model accuracy and latency-rather than accounting for it retrospectively through annual budget reconciliation. 1. Significance (quantitative) : MLcompute costs scale steeply with experimentation volume. A team running 1,000 GPU-hours/day at $3/GPU-hour spends $3,000/day$1.1M/year-on training alone. With per-experime

**Location:** [v2_ch13.md • **Chapter:** Chapter 13: ML Operations at Scale](v2_ch13.md • **Chapter:** Chapter 13: ML Operations at Scale)

---

## G

### Graceful degradation

**Full heading:** Definition 8.3 (Vol 2)

**Source:** `v2_ch08.md • **Chapter:** Chapter 8: Fault Tolerance and Reliability (Vol 2)`

Graceful degradation Graceful Degradation is a fault tolerance strategy in which a system responds to resource exhaustion or component failure by deliberately reducing service quality-falling back to a smaller model, serving cached results, or returning partial outputs-rather than failing completely, maintaining measurable availability at reduced capability. 1. Significance (quantitative) : Graceful degradation converts total outage risk into a controlled quality reduction. A recommendation syst

**Location:** [v2_ch08.md • **Chapter:** Chapter 8: Fault Tolerance and Reliability (Vol 2)](v2_ch08.md • **Chapter:** Chapter 8: Fault Tolerance and Reliability (Vol 2))

---

### Gradient descent

**Full heading:** Definition 5.3 (Vol 1)

**Source:** `ch05.md • **Chapter:** Chapter 5: Neural Computation & Training Mechanics`

Gradient descent Gradient Descent is the iterative algorithm that navigates the Loss Landscape by updating parameters in the direction of the negative gradient. 3. Common pitfall: Afrequent misconception is that Gradient Descent always finds the Global Minimum . In reality, it is a Local Optimizer that can become stuck in plateaus or local optima in nonconvex landscapes. 1. Significance (quantitative) : It transforms the Learning Problem into an Optimization Problem, trading computational cycles

**Location:** [ch05.md • **Chapter:** Chapter 5: Neural Computation & Training Mechanics](ch05.md • **Chapter:** Chapter 5: Neural Computation & Training Mechanics)

---

### Gradient synchronization

**Full heading:** Definition 7.1 (Vol 2)

**Source:** `v2_ch07.md • **Chapter:** Chapter 7: Collective Communication`

Gradient synchronization Gradient Synchronization is the collective communication protocol executed at each training step in which every worker transmits its locally computed gradient tensor to all other workers, receives their gradients, and computes an aggregate update that all workers apply identically to their model copies. 1. Significance (quantitative) : A70B-parameter model in BF16 generates 140 GB of gradient data per worker per step. Synchronizing across 1,000 GPUs via ring AllReduce at

**Location:** [v2_ch07.md • **Chapter:** Chapter 7: Collective Communication](v2_ch07.md • **Chapter:** Chapter 7: Collective Communication)

---

## H

### Hardware-Software Co

**Full heading:** Definition 11.2 (Vol 1)

**Source:** `ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs`

Hardware-Software Co-Design **Hardware-Software Co-design** is a development methodology that intentionally violates traditional hardware-software abstraction layers, allowing algorithmic constraints to inform silicon design and hardware capabilities to directly shape algorithm formulation. * **Quantized Operations:** Algorithmic quantization (e.g., INT8/INT4) only achieves speedups because accelerators are physically built to execute multiple low-precision operations in the same die area as a s

**Location:** [ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs](ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs)

---

### Hierarchy

**Full heading:** Definition 2.13 (Vol 2)

**Source:** `v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure`

Hierarchy-aware parallelism Hierarchy-Aware Parallelism is the strategy of mapping different parallel execution modes to the physical bandwidth tiers of the cluster. 1. Significance (quantitative) : It ensures that high-frequency synchronization (for example, Tensor Parallelism) stays on the fastest links (NVLink), while lower-frequency tasks (for example, Data Parallelism) use slower tiers (InfiniBand). This alignment maximizes the System Efficiency (𝜂 hw ) by minimizing communication stalls (𝐿

**Location:** [v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure](v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure)

---

### Hybrid ML

**Full heading:** Definition 2.7 (Vol 1)

**Source:** `ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)`

Hybrid ML Hybrid Machine Learning is the architectural strategy of Hierarchical Distribution across cloud and edge resources. 3. Common pitfall: A frequent misconception is that Hybrid ML is just 'running two models.' In reality, it is a Unified Data Fabric where the state must be synchronized across disparate hardware to ensure consistency. 1. Significance (quantitative) : It partitions the ML workload across the latency-compute Pareto frontier, minimizing the Distance Penalty (𝐿 lat ) for reac

**Location:** [ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)](ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML))

---

## I

### Inductive Bias

**Full heading:** Definition 6.1 (Vol 1)

**Source:** `ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys)`

Inductive Bias An **inductive bias** is a structural constraint built into a model architecture that restricts the hypothesis space, enabling generalization from finite data by encoding domain-specific assumptions (such as spatial locality or sequential ordering) directly into the computational graph. * **Quantitative Significance:** Inductive bias directly reduces the required data volume ($D_{\text{vol}}$) for generalization. For a $224 \times 224$ image, a $3 \times 3$ convolutional kernel re

**Location:** [ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys)](ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys))

---

### Iron Law

**Full heading:** Definition 2.1 (Vol 2)

**Source:** `v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure`

High bandwidth memory (HBM) HighBandwidthMemory(HBM) is a 3D-stacked DRAM architecture in which multiple memory dies are vertically bonded and connected to the processor through thousands of ThroughSilicon Vias (TSVs) on a shared silicon interposer, eliminating the centimeter-scale PCB traces of conventional DRAM and replacing them with micrometer-scale vertical paths. - 3 HBM (High Bandwidth Memory) : Standardized by JEDEC in 2013 as a joint development between AMD and SK Hynix, originally for

**Location:** [v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure](v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure)

---

### It is the primary diagnostic for whether hardware investment

**Full heading:** Definition 10.3 (Vol 2)

**Source:** `v2_ch10.md • **Chapter:** Chapter 10: Performance Engineering (Vol 2)`

Model FLOPs utilization (MFU) 1. Significance (quantitative) : At fleet scale, MFU aggregates across all nodes: communication overhead, load imbalance, and pipeline bubbles each compound the utilization loss, so fleet MFU is consistently below single-node MFU. It is the primary diagnostic for whether hardware investment is translating into model progress, and a 1 percent improvement in MFU across a 10,000-GPU cluster reduces cost by the equivalent of 100 GPUs. Model FLOPs Utilization (MFU) is th

**Location:** [v2_ch10.md • **Chapter:** Chapter 10: Performance Engineering (Vol 2)](v2_ch10.md • **Chapter:** Chapter 10: Performance Engineering (Vol 2))

---

## L

### LLM performance metrics

**Full heading:** Definition 13.6 (Vol 1)

**Source:** `ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)`

LLM performance metrics LLM Performance Metrics are the two-dimensional measurements of latency for streaming autoregressive generation. 25 Autoregressive: From Greek auto(self) and Latin regressus (a going back)-the output 'regresses' on itself. George Udny Yule introduced autoregressive models in 1927 for analyzing sunspot cycles. In language modeling, each output token conditions on all previously generated tokens, creating a serial dependency that prevents the parallelism exploited during tr

**Location:** [ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)](ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory))

---

## M

### Machine learning benchmarking

**Full heading:** Definition 12.1 (Vol 1)

**Source:** `ch12.md • **Chapter:** Chapter 12: Benchmarking Systems & Power Measurement`

Machine learning benchmarking Machine Learning Benchmarking is the empirical measurement of a system's end-to-end performance on representative ML workloads, designed to decouple marketed peak specifications from the sustained throughput and latency achievable under realistic operating conditions. 1. Significance (quantitative) : The gap between peak and sustained performance is large and structurally unavoidable. An A100 GPU delivers 312 TFLOPS BF16 at peak, but production transformer training

**Location:** [ch12.md • **Chapter:** Chapter 12: Benchmarking Systems & Power Measurement](ch12.md • **Chapter:** Chapter 12: Benchmarking Systems & Power Measurement)

---

### Machine learning fleet

**Full heading:** Definition 1.1 (Vol 2)

**Source:** `v2_ch01.md • **Chapter:** Chapter 1: Introduction to ML Systems`

Machine learning fleet Machine Learning Fleet is a distributed system of thousands of interconnected accelerators, storage arrays, and network fabrics designed to operate as a single coherent computer. 2. Distinction (durable) : Unlike Traditional Clusters (for example, Spark, MapReduce) that manage independent, asynchronous jobs, an ML Fleet operates under Synchronous Tight Coupling, requiring near-perfect reliability to maintain throughput. 1. Significance (quantitative) : It coordinates synch

**Location:** [v2_ch01.md • **Chapter:** Chapter 1: Introduction to ML Systems](v2_ch01.md • **Chapter:** Chapter 1: Introduction to ML Systems)

---

### Machine learning frameworks

**Full heading:** Definition 7.1 (Vol 1)

**Source:** `ch07.md • **Chapter:** Chapter 7: ML Frameworks (TF, PyTorch, JAX)`

Machine learning frameworks Machine Learning Frameworks are software systems that translate high-level mathematical model definitions into hardware-optimized execution plans by managing the computational graph, automatic differentiation, kernel dispatch, and memory allocation across the hardware hierarchy. 2. Distinction (durable) : Unlike a numerical library such as NumPy, which executes each operation immediately (eager evaluation), an ML framework can defer execution to analyze the full compu

**Location:** [ch07.md • **Chapter:** Chapter 7: ML Frameworks (TF, PyTorch, JAX)](ch07.md • **Chapter:** Chapter 7: ML Frameworks (TF, PyTorch, JAX))

---

### Machine learning lifecycle

**Full heading:** Definition 3.1 (Vol 1)

**Source:** `ch03.md • **Chapter:** Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)`

Machine learning lifecycle Machine Learning Lifecycle is the continuous engineering discipline of managing System Entropy across the Data, Algorithm, and Machine axes. 1. Significance (quantitative) : It transforms the linear software 'release' into a continuous loop of monitoring, retraining, and redeployment to maintain the system's Duty Cycle (𝜂 hw ) . 2. Distinction (durable) : Unlike a traditional software lifecycle, which degrades primarily through code modification, the ML lifecycle recog

**Location:** [ch03.md • **Chapter:** Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)](ch03.md • **Chapter:** Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration))

---

### Machine learning system benchmarks

**Full heading:** Definition 12.2 (Vol 1)

**Source:** `ch12.md • **Chapter:** Chapter 12: Benchmarking Systems & Power Measurement`

Machine learning system benchmarks Machine Learning System Benchmarks are standardized evaluation protocols that hold the workload and quality target constant while varying the hardware-software stack, measuring 𝜂 hw =𝑅 sustained /𝑅 peak and 𝐿 lat to isolate infrastructure efficiency from algorithmic improvements. 2. Distinction (durable) : Unlike algorithmic benchmarks (which vary model architectures and training procedures to improve convergence accuracy), system benchmarks hold the algorithm

**Location:** [ch12.md • **Chapter:** Chapter 12: Benchmarking Systems & Power Measurement](ch12.md • **Chapter:** Chapter 12: Benchmarking Systems & Power Measurement)

---

### Machine learning systems

**Full heading:** Definition 1.1 (Vol 1)

**Source:** `ch01.md • **Chapter:** Chapter 1: Introduction to ML Systems`

Machine learning systems Machine Learning Systems are software systems whose core behavior is determined by parameters learned from data rather than explicitly programmed rules, making performance a function of data quality, algorithm choice, and hardware capacity simultaneously. 2. Distinction (durable) : Unlike traditional software, whose correctness degrades only when code changes, an ML system's accuracy degrades when the world changes. Model weights are fixed after deployment, but the distr

**Location:** [ch01.md • **Chapter:** Chapter 1: Introduction to ML Systems](ch01.md • **Chapter:** Chapter 1: Introduction to ML Systems)

---

### Mapping in AI Acceleration

**Full heading:** Definition 11.6 (Vol 1)

**Source:** `ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs`

Mapping in AI Acceleration **Mapping in AI Acceleration** is the process of binding the Logical Computation Graph to the Physical Hardware Topology by deciding which operations execute on which processing elements, which data resides in which memory tier, and in what temporal order. Mapping defines three axes of execution: 1. **Computation placement:** Assigning operations to physical processing elements (PEs) to balance load and minimize stalls. 2. **Memory allocation:** Specifying where weight

**Location:** [ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs](ch11.md • **Chapter:** Chapter 11: Hardware Acceleration, Compilers & SoCs)

---

### MLOps

**Full heading:** Definition 14.1 (Vol 1)

**Source:** `ch14.md • **Chapter:** Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)`

MLOps Machine Learning Operations (MLOps) is the engineering discipline that closes the feedback loop between model behavior and data reality by automating retraining, validation, and deployment in response to measurable production drift (Kreuzberger et al. 2023). 1. Significance (quantitative) : The cost of not closing this loop shows up in reported production deployments: recommendation models without drift monitoring can lose on the order of 10-20 percent absolute accuracy within six months a

**Location:** [ch14.md • **Chapter:** Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)](ch14.md • **Chapter:** Chapter 14: ML Operations (MLOps, Drift, Edge Fleets))

---

### MLsystems TCO

**Full heading:** Definition 13.2 (Vol 2)

**Source:** `v2_ch13.md • **Chapter:** Chapter 13: ML Operations at Scale`

MLsystems TCO Total Cost of Ownership (TCO) for ML Systems is the complete economic accounting of developing, deploying, and operating machine learning capabilities across their full lifecycle. 1. Significance (quantitative) : It captures the Cost Inversion of scale: while training costs are a one-time 'upfront' operation (𝑂) , the cumulative Inference TCO grows linearly with user adoption and time, often exceeding development costs by 5 × to 10 × over a 3-year period. 3. Common pitfall: Afreque

**Location:** [v2_ch13.md • **Chapter:** Chapter 13: ML Operations at Scale](v2_ch13.md • **Chapter:** Chapter 13: ML Operations at Scale)

---

### MLtraining benchmarks

**Full heading:** Definition 12.3 (Vol 1)

**Source:** `ch12.md • **Chapter:** Chapter 12: Benchmarking Systems & Power Measurement`

MLtraining benchmarks MLTraining Benchmarks measure the Rate of Convergence per unit of resource (time, energy, cost). 1. Significance (quantitative) : They validate the system's ability to sustain high arithmetic intensity across distributed accelerators while managing the communication overhead (𝐿 lat ) of gradient synchronization. 2. Distinction (durable) : Unlike inference benchmarks, which focus on input-output latency, training benchmarks focus on throughput (𝜂 hw ) and total training time

**Location:** [ch12.md • **Chapter:** Chapter 12: Benchmarking Systems & Power Measurement](ch12.md • **Chapter:** Chapter 12: Benchmarking Systems & Power Measurement)

---

### Mobile ML

**Full heading:** Definition 2.5 (Vol 1)

**Source:** `ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)`

Mobile ML Mobile Machine Learning is the deployment paradigm bounded by Thermal Design Power (TDP) and battery energy. 1. Significance (quantitative) : It is constrained by the heat dissipation capacity of passive cooling (typically 2-3 W), requiring architectures that prioritize sustained energy efficiency over peak throughput (𝑅 peak ) . 3. Common pitfall: A frequent misconception is that mobile ML performance is a fixed value. In reality, it is a Time-Varying Constraint: performance often dro

**Location:** [ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)](ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML))

---

### Model compression

**Full heading:** Definition 10.1 (Vol 1)

**Source:** `ch10.md • **Chapter:** Chapter 10: Model Compression (Pruning, Quantization, Distillation)`

Model compression Model Compression is a family of techniques that reduce a trained model's computational cost and memory footprint by eliminating redundant parameters (pruning), reducing numerical precision (quantization), or transferring learned behavior into a smaller architecture (distillation), while preserving as much predictive accuracy as possible. 1. Significance (quantitative) : Compression directly reduces both iron law terms. INT8 quantization of a 175B-parameter large language model

**Location:** [ch10.md • **Chapter:** Chapter 10: Model Compression (Pruning, Quantization, Distillation)](ch10.md • **Chapter:** Chapter 10: Model Compression (Pruning, Quantization, Distillation))

---

### Model FLOPs Utilization (MFU)

**Full heading:** Definition 8.4 (Vol 1)

**Source:** `ch08.md • **Chapter:** Chapter 8: Staged Model Training & Parallelism`

Model FLOPs Utilization (MFU) **Model FLOPs Utilization (MFU)** is the hardware-agnostic efficiency metric defined as the ratio of useful model computations performed per step to the peak theoretical hardware capability: \[ \text{MFU} = \frac{C_{\text{model}}}{R_{\text{peak}} \cdot T_{\text{step}}} \] Where \(C_{\text{model}}\) is the theoretical FLOP count per training step based on the model parameters (excluding activation recomputation and padding), \(R_{\text{peak}}\) is the peak accelerato

**Location:** [ch08.md • **Chapter:** Chapter 8: Staged Model Training & Parallelism](ch08.md • **Chapter:** Chapter 8: Staged Model Training & Parallelism)

---

### Model serving

**Full heading:** Definition 13.1 (Vol 1)

**Source:** `ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)`

Model serving Model Serving is the operational phase that provides model predictions to end-users or downstream systems under strict latency constraints. 1 Jevons Paradox: William Stanley Jevons observed in 1865 that efficiency improvements in coal-powered steam engines increased total coal consumption by making steam power economically viable for applications previously too costly. The same dynamic governs AI inference: each 10 × cost reduction opens application classes that were economically i

**Location:** [ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)](ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory))

---

### Model validation

**Full heading:** Definition 3.2 (Vol 1)

**Source:** `ch03.md • **Chapter:** Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)`

Model validation Model Validation is the rigorous verification that a model meets business constraints-service level agreement (SLA), fairness, and cost-on production-representative data. 1. Significance (quantitative) : It moves beyond 'test set accuracy' to test for robustness against distribution shift (𝐷 vol ) and efficiency against hardware limits (𝑅 peak, BW ) . 2. Distinction (durable) : Unlike model evaluation, which measures performance on a static test set, model validation confirms th

**Location:** [ch03.md • **Chapter:** Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)](ch03.md • **Chapter:** Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration))

---

### Multilayer Perceptron (MLP)

**Full heading:** Definition 6.2 (Vol 1)

**Source:** `ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys)`

Multilayer Perceptron (MLP) An **MLP** is a feed-forward neural network architecture that applies fully connected layers in sequence, where every neuron in layer $l-1$ connects to every neuron in layer $l$, encoding no structural assumptions about the input domain. * **Universal Approximation Theorem (UAT):** A sufficiently wide single-hidden-layer MLP with non-linear activation functions can approximate any continuous function on a compact domain. * **Manifold Hypothesis:** High-dimensional rea

**Location:** [ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys)](ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys))

---

## N

### Non

**Full heading:** Definition 4.5 (Vol 2)

**Source:** `v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics`

Non-blocking fabric Non-blocking Fabric is a network topology in which any permutation of input-output port pairs can communicate simultaneously at full line rate without internal contention, achieved by ensuring that uplink capacity at every switch tier equals or exceeds downlink capacity. 1. Significance (quantitative) : In ML fleets, a non-blocking fabric ensures that AllReduce traffic from any accelerator subset does not compete for shared links, preserving the full BW term of the iron law.

**Location:** [v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics](v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics)

---

## O

### Online Learning

**Full heading:** Definition 2.6 (Vol 2)

**Source:** `v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure`

Thermal design power (TDP) Thermal Design Power (TDP) is the maximum sustained thermal load in watts that a chip's cooling system must continuously remove for the processor to operate at its rated clock frequencydefining both the cooling infrastructure requirement and the performance ceiling for the accelerator. 1. Significance (quantitative) : The H100 SXM5 operates at 700 W TDP. When a liquid cooling system can only sustain 500 W of heat removal (inadequate cooling), the GPU firmware reduces c

**Location:** [v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure](v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure)

---

### Overfitting

**Full heading:** Definition 5.4 (Vol 1)

**Source:** `ch05.md • **Chapter:** Chapter 5: Neural Computation & Training Mechanics`

Overfitting Overfitting is the failure of Generalization caused by memorizing Noise instead of Signal . 2. Distinction (durable) : Unlike Underfitting (where the model is too simple), Overfitting is a Symmetry Breaking problem: the model becomes too specialized to the specific training sample. 1. Significance (quantitative) : It occurs when a model's Capacity exceeds the information content of the training data (𝐷) , allowing it to satisfy the training objective without learning the underlying d

**Location:** [ch05.md • **Chapter:** Chapter 5: Neural Computation & Training Mechanics](ch05.md • **Chapter:** Chapter 5: Neural Computation & Training Mechanics)

---

## P

### Pipeline bubble

**Full heading:** Definition 2.4 (Vol 2)

**Source:** `v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure`

Pipeline bubble - Pipeline Bubble is the idle time in pipeline-parallel training caused by stages waiting for inputs from upstream workers during the fill and drain phases of a micro-batch cycle. 1. Significance (quantitative) : It represents a direct loss in System Efficiency (𝜂 hw ) . For a model with 𝑝 pipeline stages and 𝑚 micro-batches, the bubble fraction is approximately (𝑝 -1)/𝑚, dictating the maximum theoretical utilization of the cluster. 3. Common pitfall: Afrequent misconception is t

**Location:** [v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure](v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure)

---

### Pipeline parallelism

**Full heading:** Definition 6.5 (Vol 2)

**Source:** `v2_ch06.md • **Chapter:** Chapter 6: Distributed Training Systems`

Pipeline parallelism Pipeline Parallelism is a model parallelism technique that partitions a neural network's layers into sequential stages assigned to different devices, passing activations forward and gradients backward between stages while overlapping computation across stages using micro-batches to maintain throughput. 1. Significance (quantitative) : Inter-stage communication transmits only the activation tensor at each stage boundary, sized as microbatch × seq\_len × hidden ×2 bytes at BF1

**Location:** [v2_ch06.md • **Chapter:** Chapter 6: Distributed Training Systems](v2_ch06.md • **Chapter:** Chapter 6: Distributed Training Systems)

---

### Power Usage Effectiveness (PUE)

**Full heading:** Definition 2.10 (Vol 2)

**Source:** `v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure`

Power usage effectiveness (PUE) 1. Significance (quantitative) : It measures the Infrastructure Overhead of the data center. A PUE of 1.0 is the theoretical ideal; a PUE of 1.10 means that for every 100 watts of computation, an additional 10 watts are required for cooling and power distribution. Power Usage Effectiveness (PUE) is the ratio of total facility power consumption to the power consumed specifically by IT equipment ( 𝑃 facility /𝑃 IT ). 2. Distinction (durable) : Unlike Computing Effic

**Location:** [v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure](v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure)

---

### Prefill and decode phases

**Full heading:** Definition 11.5 (Vol 2)

**Source:** `v2_ch11.md • **Chapter:** Chapter 11: Inference at Scale (Vol 2)`

Prefill and decode phases Prefill and Decode Phases are the two distinct computational regimes of transformer-based LLM inference. 2. Distinction (durable) : Unlike Single-Pass Inference (for example, ImageNet), where the resource bottleneck is constant, LLM inference switches between these regimes at every request, requiring Iteration-Level Scheduling to maintain utilization. 1. Significance (quantitative) : The Prefill Phase (processing the prompt) is ComputeBound (𝑅 peak ) with high arithmeti

**Location:** [v2_ch11.md • **Chapter:** Chapter 11: Inference at Scale (Vol 2)](v2_ch11.md • **Chapter:** Chapter 11: Inference at Scale (Vol 2))

---

### Priority flow control

**Full heading:** Definition 4.8 (Vol 2)

**Source:** `v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics`

Priority flow control Priority Flow Control (PFC) is a link-layer mechanism that prevents switch buffer overflow by sending PAUSE frames to an upstream sender when a port's queue depth crosses a configured threshold, throttling injection on a per-priority basis without dropping packets. 1. Significance (quantitative) : PFC is the foundation for lossless Ethernet required by RoCEv2 RDMA. A PFC PAUSE frame must reach the upstream sender within one roundtrip time (roughly 1-5 μs at switch-to-switch

**Location:** [v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics](v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics)

---

### Priority inversion

**Full heading:** Definition 9.1 (Vol 2)

**Source:** `v2_ch09.md • **Chapter:** Chapter 9: Fleet Orchestration (Vol 2)`

Priority inversion Priority Inversion is a scheduling pathology in which a high-priority task is forced to wait for a lower-priority task to release a shared resource. 1. Significance (quantitative) : It reduces the progress rate of the entire fleet to that of the lowest-priority job. In ML clusters, this typically occurs when a low-priority job holding GPUs is starved of auxiliary resources (for example, BW for checkpointing), preventing it from finishing and releasing the accelerators needed b

**Location:** [v2_ch09.md • **Chapter:** Chapter 9: Fleet Orchestration (Vol 2)](v2_ch09.md • **Chapter:** Chapter 9: Fleet Orchestration (Vol 2))

---

### Privacy

**Full heading:** Definition 14.2 (Vol 2)

**Source:** `v2_ch14.md • **Chapter:** Chapter 14: Security & Privacy (Vol 2)`

Privacy Privacy is the protection of sensitive information from unauthorized disclosure, inference, and misuse across the ML lifecycle. 1. Significance (quantitative) : It limits the exposure risk of training data and user inputs. Privacy-preserving techniques (for example, differential privacy) typically introduce a utility-privacy trade-off: increasing privacy adds 'noise' to the gradients, which can increase the total operations (𝑂) required to reach a target accuracy. 2. Distinction (durable

**Location:** [v2_ch14.md • **Chapter:** Chapter 14: Security & Privacy (Vol 2)](v2_ch14.md • **Chapter:** Chapter 14: Security & Privacy (Vol 2))

---

### Pruning

**Full heading:** Definition 10.2 (Vol 1)

**Source:** `ch10.md • **Chapter:** Chapter 10: Model Compression (Pruning, Quantization, Distillation)`

Pruning Pruning is the sparsification of the Parameter Space by removing weights that contribute minimal information to the loss landscape. 2. Distinction (durable) : Unlike Quantization, which reduces the Precision of every weight, Pruning reduces the Count of weights by identifying and eliminating redundancy. 1. Significance (quantitative) : It converts dense matrices into sparse structures, reducing the Memory Footprint and the total Data Volume (𝐷 vol ) by as much as 10 × without significant

**Location:** [ch10.md • **Chapter:** Chapter 10: Model Compression (Pruning, Quantization, Distillation)](ch10.md • **Chapter:** Chapter 10: Model Compression (Pruning, Quantization, Distillation))

---

## R

### RAID

**Full heading:** Definition 4.7 (Vol 2)

**Source:** `v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics`

Bulk synchronous parallel (BSP) Bulk Synchronous Parallel (BSP) is a parallel execution model in which every worker completes a local computation phase, exchanges data with all other workers, and then waits at a global barrier before any worker begins the next phase-making the slowest participant the pacing constraint for the entire cluster. 1. Significance (quantitative) : BSP makes system efficiency 𝜂 scaling directly proportional to the slowest worker: if one GPU in a 1,024-GPU cluster runs 1

**Location:** [v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics](v2_ch03.md • **Chapter:** Chapter 3: Network Fabrics)

---

### Recurrent Neural Network (RNN)

**Full heading:** Definition 6.4 (Vol 1)

**Source:** `ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys)`

Recurrent Neural Network (RNN) An **RNN** is a sequence-processing architecture that updates a hidden state vector $h_t$ at each time step $t$ according to $h_t = f(h_{t-1}, x_t)$, propagating temporal context with constant $O(1)$ inference memory scaling. * **Sequential Bottleneck:** The sequential dependency $h_{t-1} \to h_t$ prevents parallel execution across the sequence (time) dimension during both training and inference. * **Vanishing/Exploding Gradients:** Backpropagation Through Time (BP

**Location:** [ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys)](ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys))

---

### Responsible AI

**Full heading:** Definition 17.1 (Vol 2)

**Source:** `v2_ch17.md • **Chapter:** Chapter 17: Responsible Engineering (Vol 2)`

Responsible AI Responsible AI is the practice of designing, auditing, and operating ML systems to measurable fairness, safety, privacy, and accountability standards-translating ethical principles into verifiable system properties that constrain model training, deployment decisions, and operational monitoring. 1. Significance (quantitative) : Responsible AI constraints impose real costs: fairness-aware training algorithms add 5-15 percent to training time; real-time bias monitoring adds 10-20 ms

**Location:** [v2_ch17.md • **Chapter:** Chapter 17: Responsible Engineering (Vol 2)](v2_ch17.md • **Chapter:** Chapter 17: Responsible Engineering (Vol 2))

---

### Responsible AI engineering

**Full heading:** Definition 15.2 (Vol 1)

**Source:** `ch15.md • **Chapter:** Chapter 15: Responsible Engineering & Compliance`

Responsible AI engineering Responsible AI Engineering is the engineering discipline of designing, deploying, and maintaining systems with probabilistic outputs by operationalizing societal and regulatory requirements as testable constraints on the D·A·M axes, bounding which values of 𝐷 vol, 𝑂, and 𝑅 peak ⋅ 𝜂 hw are permissible. 1. Significance (quantitative) : Each D·A·M axis acquires concrete governance constraints: the Data axis is bounded by privacy regulations such as the General Data Protec

**Location:** [ch15.md • **Chapter:** Chapter 15: Responsible Engineering & Compliance](ch15.md • **Chapter:** Chapter 15: Responsible Engineering & Compliance)

---

### Ridge point

**Full heading:** Definition 2.2 (Vol 2)

**Source:** `v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure`

Ridge point Achievable FLOPS = min (𝑅 peak, BW ×𝐼) (2.1) Equation 2.1 has a direct physical interpretation. If the workload's arithmetic intensity is low (it needs many bytes per operation), then performance is limited by how fast memory can deliver those bytes. The achievable FLOPS grows linearly with 𝐼, tracing a sloped line on a log-log plot. If the arithmetic intensity is high (each byte fuels many operations), then performance plateaus at the hardware's peak compute rate, regardless of furt

**Location:** [v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure](v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure)

---

### Robust AI

**Full heading:** Definition 15.1 (Vol 2)

**Source:** `v2_ch15.md • **Chapter:** Chapter 15: Robust AI`

Robust AI Robust AI is the measurable systems property that a model's predictions remain valid-within specified error bounds-under distribution shift, adversarial perturbation, and hardware or software faults, as opposed to the average-case accuracy achieved under ideal i.i.d. conditions. 1. Significance (quantitative) : Robustness is quantified by worst-case guarantees: a certified robust classifier guarantees accuracy above a threshold for all inputs within an ℓ ∞ ball of radius 𝜀 around any t

**Location:** [v2_ch15.md • **Chapter:** Chapter 15: Robust AI](v2_ch15.md • **Chapter:** Chapter 15: Robust AI)

---

## S

### SLO vs. SLA

**Full heading:** Definition 12.5 (Vol 1)

**Source:** `ch12.md • **Chapter:** Chapter 12: Benchmarking Systems & Power Measurement`

SLO vs. SLA SLOs and SLAs are performance commitment specifications: a Service Level Objective (SLO) is the internal engineering target that the team optimizes toward, while a Service Level Agreement (SLA) is the external contractual threshold whose breach triggers financial penalties. 1. Significance (quantitative) : SLOs directly constrain the 𝐿 lat term in the iron law by setting a hard latency ceiling that the serving system must satisfy at a given percentile. A typical production setup sets

**Location:** [ch12.md • **Chapter:** Chapter 12: Benchmarking Systems & Power Measurement](ch12.md • **Chapter:** Chapter 12: Benchmarking Systems & Power Measurement)

---

### Small file problem

**Full heading:** Definition 5.2 (Vol 2)

**Source:** `v2_ch05.md • **Chapter:** Chapter 5: Data Storage — The Fuel Line`

Small file problem - Small File Problem is a pathological I/O pattern where millions of individually small files overwhelm the metadata server of a storage system. 1. Significance (quantitative) : It reduces effective I/O Bandwidth ( BWio ) to a fraction of its theoretical rating because each file requires its own metadata operations ( open, stat, close ). With 10,000 workers simultaneously accessing small files, the metadata server becomes a Serialization Point that idles the entire cluster. 3.

**Location:** [v2_ch05.md • **Chapter:** Chapter 5: Data Storage — The Fuel Line](v2_ch05.md • **Chapter:** Chapter 5: Data Storage — The Fuel Line)

---

### Speculative decoding

**Full heading:** Definition 11.4 (Vol 2)

**Source:** `v2_ch11.md • **Chapter:** Chapter 11: Inference at Scale (Vol 2)`

Speculative decoding Speculative Decoding is a latency optimization that uses a smaller Draft Model to predict multiple future tokens, which are then verified in parallel by the full Target Model in a single forward pass. 2. Distinction (durable) : Unlike standard autoregressive decoding (one token at a time), speculative decoding enables batch-of-tokens verification, increasing the arithmetic intensity of the target model's forward pass. 1. Significance (quantitative) : It breaks the sequential

**Location:** [v2_ch11.md • **Chapter:** Chapter 11: Inference at Scale (Vol 2)](v2_ch11.md • **Chapter:** Chapter 11: Inference at Scale (Vol 2))

---

### Straggler

**Full heading:** Definition 8.2 (Vol 2)

**Source:** `v2_ch08.md • **Chapter:** Chapter 8: Fault Tolerance and Reliability (Vol 2)`

Straggler - Straggler is a worker in a distributed training job that processes tasks significantly slower than its peers, creating a synchronization bottleneck. 1. Significance (quantitative) : In a synchronous system (BSP), cluster throughput ( 𝜂 hw ) is bounded by the speed of the Slowest Rank . Asingle 10 percent performance drop on one node can reduce the effective compute capacity of thousands of nodes by 10 percent. 2. Distinction (durable) : Unlike a Hardware Failure (where the node stops

**Location:** [v2_ch08.md • **Chapter:** Chapter 8: Fault Tolerance and Reliability (Vol 2)](v2_ch08.md • **Chapter:** Chapter 8: Fault Tolerance and Reliability (Vol 2))

---

### Sustainable AI

**Full heading:** Definition 16.1 (Vol 2)

**Source:** `v2_ch16.md • **Chapter:** Chapter 16: Sustainable AI`

Sustainable AI Sustainable AI is the systems engineering practice of measuring and optimizing the full environmental cost of ML systems (energy, water, and embodied carbon across training, inference, and hardware manufacturing) and incorporating those costs as explicit constraints in architecture decisions alongside performance and accuracy objectives (Lannelongue et al. 2021). 1. Significance (quantitative) : Training GPT-3 consumed approximately 1,287 MWh of energy (Li 2020), equivalent to rou

**Location:** [v2_ch16.md • **Chapter:** Chapter 16: Sustainable AI](v2_ch16.md • **Chapter:** Chapter 16: Sustainable AI)

---

## T

### Tensor core

**Full heading:** Definition 2.3 (Vol 2)

**Source:** `v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure`

Tensor core Tensor Core is a specialized mixed-precision hardware unit that performs a fused matrixmultiply-accumulate (MMA) operation 𝐷=𝐴×𝐵+𝐶 on small tiles (for example, 16×8×16 in BF16) within a single clock cycle, delivering dramatically higher throughput than generalpurpose CUDA cores by trading programmability for fixed-function matrix arithmetic. 1. Significance (quantitative) : Tensor Cores provide the bulk of the H100's 312 TFLOPS BF16 peak-roughly 8 × the ~40 TFLOPS delivered by CUDA (

**Location:** [v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure](v2_ch02.md • **Chapter:** Chapter 2: Compute Infrastructure)

---

### Tensor parallelism

**Full heading:** Definition 6.6 (Vol 2)

**Source:** `v2_ch06.md • **Chapter:** Chapter 6: Distributed Training Systems`

Tensor parallelism Tensor Parallelism is a model parallelism technique that partitions individual tensor operations-primarily matrix multiplications-across multiple devices using column-parallel or row-parallel weight splits, typically requiring two AllReduce operations per transformer layer in Megatron-style transformer blocks to sum partial results from all participating devices. 1. Significance (quantitative) : Megatron-LM style tensor parallelism places two AllReduce operations per transform

**Location:** [v2_ch06.md • **Chapter:** Chapter 6: Distributed Training Systems](v2_ch06.md • **Chapter:** Chapter 6: Distributed Training Systems)

---

### The Consistency Imperative

**Full heading:** Definition 4.2 (Vol 1)

**Source:** `ch04.md • **Chapter:** Chapter 4: Data Engineering & Pipeline Architecture`

The Consistency Imperative The Consistency Imperative is the axiom that Transformation Logic must be immutable across training and serving environments. 1. **Significance (Quantitative)**: It predicts that performance degradation is proportional to the Kullback-Leibler (KL) Divergence: \[ \mathcal{D}_{\text{KL}}(T \parallel T') \] between the training transformation (\(T\)) and the serving transformation (\(T'\)). 2. **Distinction (Durable)**: Unlike Data Quality, which focuses on the cleanlines

**Location:** [ch04.md • **Chapter:** Chapter 4: Data Engineering & Pipeline Architecture](ch04.md • **Chapter:** Chapter 4: Data Engineering & Pipeline Architecture)

---

### The constraint propagation principle

**Full heading:** Definition 3.3 (Vol 1)

**Source:** `ch03.md • **Chapter:** Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)`

The constraint propagation principle 1. Significance (quantitative) : It dictates that system design must proceed end-to-end. Within the iron law, a constraint on 𝑅 peak at deployment (Stage 5) propagates backward to redefine the Stage 1 requirements and the downstream data volume (𝐷 vol ) and algorithm complexity (𝑂) that those requirements permit. The Constraint Propagation Principle states that constraints discovered late in the lifecycle ( 𝑁 ) incur an exponential cost relative to catching t

**Location:** [ch03.md • **Chapter:** Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)](ch03.md • **Chapter:** Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration))

---

### The data locality invariant

**Full heading:** Definition 2.4 (Vol 1)

**Source:** `ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)`

The data locality invariant 1. Significance (quantitative) : It defines the Locality Crossover, the point where adding cloud compute (increasing 𝑅 peak ) yields zero benefit because the 'Pipe' ( BWnet ) is too narrow for the 'Volume' (𝐷 vol ) . The Data Locality Invariant states that a workload necessitates local processing whenever the transmission delay (𝐷 vol / BWnet ) dominates the remote response time: Data Locality ⟺ 𝐷 vol BWnet >𝐿 net + 𝑂 𝑅 peak, remote 2. Distinction (durable) : Unlike T

**Location:** [ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)](ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML))

---

### The iron law

**Full heading:** Definition 2.1 (Vol 1)

**Source:** `ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)`

The iron law [Formula not decoded] 1. Significance (quantitative) : It defines the Physical Ceiling for any system by quantifying the relationship between data volume (𝐷 vol ) , compute capacity (𝑅 peak ) , and communication overhead (𝐿 lat ) . The iron law is the fundamental physical constraint governing all machine learning performance, expressed as the total time 𝑇 required for a workload: 5 Workload Archetype: A classification of ML workloads by their dominant iron law bottleneck rather than

**Location:** [ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)](ch02.md • **Chapter:** Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML))

---

### The Iron Law of Training Performance

**Full heading:** Definition 8.2 (Vol 1)

**Source:** `ch08.md • **Chapter:** Chapter 8: Staged Model Training & Parallelism`

The Iron Law of Training Performance The **Iron Law of Training Performance** models the wall-clock execution time of an iterative optimization run by assuming that data transfer and communication latency are fully overlapped with computation: \[ T_{\text{train}} \approx \frac{O}{R_{\text{peak}} \cdot \eta_{\text{hw}}} \] Where: * \(T_{\text{train}}\) is the training wall-clock time (seconds). * \(O\) is the total number of floating-point operations (FLOPs) required. * \(R_{\text{peak}}\) is the

**Location:** [ch08.md • **Chapter:** Chapter 8: Staged Model Training & Parallelism](ch08.md • **Chapter:** Chapter 8: Staged Model Training & Parallelism)

---

### Training

**Full heading:** Definition 13.3 (Vol 1)

**Source:** `ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)`

Training-serving skew Training-Serving Skew is the distributional divergence between the training and inference environments caused by inconsistent logic or state. 3. Common pitfall: Afrequent misconception is that skew is 'found' by looking for errors. In reality, it is invisible to exceptions: the system runs perfectly and the latency is low, but the predictions are statistically wrong. 1. Significance (quantitative) : It violates the consistency imperative, causing silent accuracy degradation

**Location:** [ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)](ch13.md • **Chapter:** Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory))

---

### Training Systems

**Full heading:** Definition 8.1 (Vol 1)

**Source:** `ch08.md • **Chapter:** Chapter 8: Staged Model Training & Parallelism`

Training Systems **Machine Learning Training Systems** are software-hardware systems that execute the iterative optimization loop—forward pass, loss computation, backward pass, and parameter update—to minimize a loss function over a training dataset. * **Quantitative Significance:** The memory cost of training is typically \(6 \times\) the inference memory footprint per parameter when using the Adaptive Moment Estimation (Adam) optimizer. For a \(7\text{B}\) parameter model: \[ \text{VRAM}_{\tex

**Location:** [ch08.md • **Chapter:** Chapter 8: Staged Model Training & Parallelism](ch08.md • **Chapter:** Chapter 8: Staged Model Training & Parallelism)

---

### Transformer

**Full heading:** Definition 6.6 (Vol 1)

**Source:** `ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys)`

Transformer A **Transformer** is an architectural paradigm for parallel sequence processing that replaces recurrence entirely with global self-attention and point-wise fully connected networks, decoupling sequence length from computational depth during training. * **Autoregressive Generation:** Generation is performed token-by-token. For each new token, the model evaluates a single forward pass, resulting in a low-intensity, memory-bandwidth-bound execution profile. * **KV Cache:** To prevent re

**Location:** [ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys)](ch06.md • **Chapter:** Chapter 6: Network Architectures (CNNs, Transformers, RecSys))

---
