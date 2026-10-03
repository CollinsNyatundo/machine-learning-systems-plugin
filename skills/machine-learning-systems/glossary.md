# Glossary — Machine Learning Systems

> Generated from the formal definitions in 44 chapters (132 entries), sorted alphabetically. Do not edit by hand: run `python scripts/build_indexes.py`.

Entries are excerpts. Use the `get_definition` tool or open the source chapter for the full text.

## A

### Adversarial attack

**Definition 15.3** (Vol 2) · [v2_ch15.md](chapters/v2_ch15.md) · Chapter 15: Robust AI

Adversarial Attack is a deliberate, mathematically crafted perturbation to model inputs designed to cause misclassification while remaining imperceptible to humans. 1. Significance (quantitative) : It reveals that high-dimensional decision boundaries have Counterintuitive Vulnerabilities . The perturbation magnitude required for misclassifi- 17 Human vs. Machine Perception: First highlighted by Szegedy et al. (2013), neural networks learn statistical correlations in pixel space rather than the…

### AI Engineering

**Definition 1.3** (Vol 1) · [ch01.md](chapters/ch01.md) · Chapter 1: Introduction to ML Systems

AI Engineering is the engineering discipline of designing, deploying, and maintaining systems whose outputs are inherently probabilistic (stochastic) to meet deterministic reliability targets by simultaneously satisfying constraints on all three D·A·M axes (Data quality, Algorithm correctness, Machine efficiency) in production. 1. Significance (quantitative) : MLResearch typically optimizes only the Algorithm axis ( 𝑂 and convergence). AI Engineering jointly optimizes all three: it bounds 𝐷 vol…

### AI Memory Wall

**Definition 11.4** (Vol 1) · [ch11.md](chapters/ch11.md) · Chapter 11: Hardware Acceleration, Compilers & SoCs

The **AI Memory Wall** is the performance constraint that arises when arithmetic throughput (\(R_{\text{peak}}\)) outpaces memory bandwidth (\(\text{BW}\)). It dictates that system performance is bounded by the energy and latency cost of data movement rather than FLOP capacity, representing the point where the data volume term (\(\frac{D_{\text{vol}}}{\text{BW}}\)) in the Iron Law of ML dominates total execution time.

### AI memory wall

**Definition 11.4** (Vol 1) · [ch11.md](chapters/ch11.md) · Chapter 11: Hardware Acceleration, Compilers & SoCs

2. Distinction (durable) : Unlike a general-purpose memory wall, which affects all computing, the AI memory wall is driven by the massive model state and activation storage required by deep learning. 2. The AI Memory Wall is the performance constraint that arises when arithmetic throughput (𝑅 peak ) outpaces memory bandwidth ( BW ) . 1. Significance (quantitative) : It dictates that system performance is no longer bounded by FLOPs, but by the energy and latency cost of moving data. Within the…

### Algorithmic fairness

**Definition 17.2** (Vol 2) · [v2_ch17.md](chapters/v2_ch17.md) · Chapter 17: Responsible Engineering (Vol 2)

Algorithmic Fairness is the measurable property that a model's error distribution or outcomes are invariant (or bounded in variation) across protected demographic groups. 1. Significance (quantitative) : It transforms fairness from an intuition into a MultiObjective Optimization problem. Within the iron law, achieving fairness often requires trading off total accuracy ( Accuracy ) for Group-Specific Calibration, ensuring that the system's benefits and harms are distributed equitably. 2.…

### Arithmetic Intensity

**Definition 11.5** (Vol 1) · [ch11.md](chapters/ch11.md) · Chapter 11: Hardware Acceleration, Compilers & SoCs

**Arithmetic Intensity (AI)** is the ratio of floating-point operations to bytes of memory traffic for a given computation (FLOP/byte), determining whether the workload is limited by compute throughput (\(R_{\text{peak}}\)) or memory bandwidth (\(\text{BW}\)) on a given accelerator. \[ \text{AI} = \frac{\text{FLOPs}}{\text{Bytes Transferred}} \]

### Arithmetic intensity

**Definition 11.5** (Vol 1) · [ch11.md](chapters/ch11.md) · Chapter 11: Hardware Acceleration, Compilers & SoCs

1. Significance (quantitative) : The intensity threshold separating memory-bound from compute-bound regimes is the roofline ridge point: 𝑅 peak / BW. For an A100 (312 TFLOPS BF16, 2 TB/s), the ridge point is 312×10 12 /(2×10 12 ) = 156 FLOP/byte. A large matrixmultiply achieves about 100-200 FLOP/byte (compute bound); a pointwise ReLU achieves about 0.5 FLOP/byte (memory bound)-placing these two operations in completely different optimization regimes on the same hardware. Arithmetic Intensity…

### Attention Mechanism

**Definition 6.5** (Vol 1) · [ch06.md](chapters/ch06.md) · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

An **attention mechanism** is a sequence-processing operation that computes a weighted sum of value vectors, where the weights are dynamically calculated via similarity scores between a query vector and a set of key vectors. * **Direct Connectivity:** Information flows between any two positions in \(O(1)\) depth, eliminating the \(O(N)\) sequential path length of RNNs. * **Quadratic Wall:** Materializing the \(N \times N\) attention weight matrix requires \(O(N^2)\) memory and compute, creating…

### Attention mechanisms

**Definition 6.5** (Vol 1) · [ch06.md](chapters/ch06.md) · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Attention Mechanisms are neural network operations that compute a weighted sum of value vectors, where the weights are derived from learned similarity scores between a query vector and a set of key vectors, enabling dynamic, content-dependent information routing between any two positions in a sequence. 2. Distinction (durable) : Unlike RNNs, which compress all prior context into a single fixed-size state vector, attention mechanisms retain token representations and compute relevance scores…

## B

### Backpropagation

**Definition 5.2** (Vol 1) · [ch05.md](chapters/ch05.md) · Chapter 5: Neural Computation & Training Mechanics

Backpropagation is the efficient application of the Chain Rule to a computational graph to solve the Credit Assignment Problem . 1. Significance (quantitative) : It propagates error signals from output to input, computing the gradient of the loss with respect to every parameter in one backward traversal of the computation graph. 2. Distinction (durable) : Unlike Numerical Differentiation (which requires one perturbed forward pass per parameter), Backpropagation is a Global Gradient Computation…

### Bandwidth hierarchy

**Definition 2.8** (Vol 2) · [v2_ch02.md](chapters/v2_ch02.md) · Chapter 2: Compute Infrastructure

Bandwidth Hierarchy is the physical ordering of data transfer rates across system boundaries, from on-chip SRAM (fastest) to the wide-area network (slowest). 1. Significance (quantitative) : It dictates the Scaling Ceiling for distributed training. At each physical boundary (die edge, package edge, chassis, rack), the Effective Bandwidth ( BW ) drops by approximately one order of magnitude while latency (𝐿 lat ) increases. 2. Distinction (durable) : Unlike Idealized Networking Models, the…

### Batch processing

**Definition 8.3** (Vol 1) · [ch08.md](chapters/ch08.md) · Chapter 8: Staged Model Training & Parallelism

1. Significance (quantitative) : Throughput increases with batch size up to the critical batch size, beyond which additional examples provide diminishing gradient quality without proportional convergence benefit. For ResNet-50 on ImageNet, empirical studies find the critical batch size near 𝐵≈8,192: at this batch size, throughput approaches 𝑅 peak while validation accuracy is preserved; larger batches require learning rate scaling (linear rule: lr ∝𝐵 ) to compensate for reduced update…

### Bisection bandwidth

**Definition 4.4** (Vol 2) · [v2_ch04.md](chapters/v2_ch04.md) · Chapter 4: Network Fabrics

Bisection Bandwidth is a network topology metric defined as the minimum aggregate link capacity crossing any partition that divides the cluster into two equal halves, representing the worst-case throughput ceiling for all-to-all communication patterns such as AllReduce. 1. Significance (quantitative) : Bisection bandwidth directly sets the BW ceiling in the iron law for global synchronization. A 1,024-GPU fat-tree with 400 Gb/s (50 GB/s) links at 1:1 subscription provides 512 × 50 GB/s = 25.6…

### Block-wise quantization

**Definition 10.2** (Vol 2) · [v2_ch10.md](chapters/v2_ch10.md) · Chapter 10: Performance Engineering (Vol 2)

1. Significance (quantitative) : With block size 𝐵 block =64 and 𝑏 = 4 bits, weights compress from 16 bits to 4 bits-a 4 × memory reduction-while each FP16 scale adds 16/64 = 0.25 bits per weight. This yields an effective bit-width of 4.25 bits per weight: 6.25 percent overhead relative to the INT4 payload, or about 1.6 percent of the original FP16 weight size. Block-wise Quantization is a quantization scheme that partitions a weight tensor into nonoverlapping groups of 𝐵 block elements and…

### Bulk synchronous parallel (BSP)

**Definition 4.7** (Vol 2) · [v2_ch04.md](chapters/v2_ch04.md) · Chapter 4: Network Fabrics

Bulk Synchronous Parallel (BSP) is a parallel execution model in which every worker completes a local computation phase, exchanges data with all other workers, and then waits at a global barrier before any worker begins the next phase-making the slowest participant the pacing constraint for the entire cluster. 1. Significance (quantitative) : BSP makes system efficiency 𝜂 scaling directly proportional to the slowest worker: if one GPU in a 1,024-GPU cluster runs 10 percent slower due to thermal…

## C

### Checkpoint storm

**Definition 5.5** (Vol 2) · [v2_ch05.md](chapters/v2_ch05.md) · Chapter 5: Data Storage — The Fuel Line

- Checkpoint Storm is a burst of synchronized network and storage traffic that occurs when all nodes in a training fleet save model state simultaneously. 1. Significance (quantitative) : The storm magnitude scales as 𝑇 write = 𝑁 × per-node-shard / BWfabric . For a 70B-parameter model in FP16 (140 GB of weights) trained across 1,000 nodes with vanilla data parallelism (every node holding its own complete copy), a naive checkpoint generates 140 TB of simultaneous writes; at 100 GB/s fabric…

### Checkpointing

**Definition 8.1** (Vol 2) · [v2_ch08.md](chapters/v2_ch08.md) · Chapter 8: Fault Tolerance and Reliability (Vol 2)

Checkpointing is the periodic serialization of the complete training state (parameters, optimizer state, and data loader position) to persistent storage. 1. Significance (quantitative) : It minimizes the Lost Work after a system failure. Within the iron-law framework formalized in Section 10.1.1, checkpointing creates an I/O Overhead that reduces the total training throughput (𝜂 hw ) , with the optimal interval (𝜏 opt ) governed by the Young-Daly Formula (𝜏 opt =√2⋅𝑇 write ⋅ MTBF ) . 2.…

### Cloud ML

**Definition 2.2** (Vol 1) · [ch02.md](chapters/ch02.md) · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

- Cloud Machine Learning is the deployment paradigm that optimizes for Resource Elasticity by decoupling computational capacity from physical location. 1. Significance (quantitative) : It enables systems to scale resources (𝑅 peak ) proportional to workload variance, allowing for bursts of peta-flops that would be economically unfeasible to maintain locally. 3. Common pitfall: Afrequent misconception is that cloud ML is 'unlimited compute.' In reality, it is constrained by the distance penalty…

### Cold start

**Definition 13.4** (Vol 1) · [ch13.md](chapters/ch13.md) · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Cold Start is the initialization latency incurred when instantiating a new model replica. 1. Significance (quantitative) : It represents the fixed cost of state hydration (loading weights, compiling graphs), which can take seconds or minutes, effectively blocking the system's ability to scale elastically in response to traffic bursts. 2. Distinction (durable) : Unlike inference latency (𝐿 lat ) , which is a per-request cost, cold start is a per-replica cost that occurs only during deployment or…

### Collective operation

**Definition 7.3** (Vol 2) · [v2_ch07.md](chapters/v2_ch07.md) · Chapter 7: Collective Communication

Collective Operation is a distributed communication pattern in which all processes in a group participate simultaneously to aggregate, broadcast, or redistribute data-with the correctness guarantee that every participant receives the same result regardless of message ordering or arrival time. 1. Significance (quantitative) : The right collective algorithm determines whether communication scales with cluster size or remains constant. Ring AllReduce achieves bandwidthoptimal 2(𝑁 -1)/𝑁 ×𝑛/𝛽 per…

### Concept drift

**Definition 15.2** (Vol 2) · [v2_ch15.md](chapters/v2_ch15.md) · Chapter 15: Robust AI

Concept Drift is the subtype of distribution shift (see Section 15.4.1) in which the statistical relationship 𝑃(𝑌 |𝑋) changes over time, meaning the decision boundary itself becomes incorrect rather than merely the input distribution. Its sibling is data drift (see Section 13.4), in which 𝑃(𝑋) changes while 𝑃(𝑌 |𝑋) remains stable. Figure 15.9: Types of Distribution Shift: Comparison of covariate shift ( 𝑃(𝑋) changes), label shift ( 𝑃(𝑦) changes), and concept drift ( 𝑃(𝑦|𝑥) changes).…

### Continuous batching

**Definition 11.1** (Vol 2) · [v2_ch11.md](chapters/v2_ch11.md) · Chapter 11: Inference at Scale (Vol 2)

- Continuous Batching is a serving strategy that decouples batch membership from iteration boundaries, allowing new requests to enter and completed ones to exit at every decode step. 1. Significance (quantitative) : It maximizes the system throughput (𝜂 hw ) by eliminating the padding waste and head-of-line blocking inherent in static batching. It ensures the GPU remains saturated even when requests have widely varying sequence lengths. 2. Distinction (durable) : Unlike static or dynamic…

### Convolutional Neural Network (CNN)

**Definition 6.3** (Vol 1) · [ch06.md](chapters/ch06.md) · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

A **CNN** is a neural network architecture defined by translation equivariance and spatial locality, restricting receptive fields to local spatial neighborhoods and sharing weights across all grid positions. * **Translation Equivariance:** A function \(f\) is equivariant to translation \(T\) if shifting the input results in an equivalent shift in the output: \[ f(T_v(x)) = T_v(f(x)) \] * **Translation Invariance:** Shifting the input does not alter the output: \[ f(T_v(x)) = f(x) \] Global…

### Convolutional neural networks

**Definition 6.3** (Vol 1) · [ch06.md](chapters/ch06.md) · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Convolutional Neural Networks (CNNs) are architectures defined by Translation Equivariance and Spatial Locality . 2. Distinction (durable) : Unlike MLPs, which have Global Connectivity, CNNs restrict connections to spatially adjacent regions, reflecting the insight that proximity correlates with feature relevance. 1. Significance (quantitative) : They exploit weight sharing to decouple parameter count from input size, enabling 𝑂(1) scaling for high-dimensional grid data (for example, images)…

## D

### Data Debt

**Definition 4.4** (Vol 1) · [ch04.md](chapters/ch04.md) · Chapter 4: Data Engineering & Pipeline Architecture

Data Debt is the compound interest of implicit coupling and missing documentation across the data stack. 1. **Significance (Quantitative)**: It manifests as silent degradation, where the cost of maintenance scales superlinearly with system age due to unmanaged dependencies and distribution shifts: \[ \mathcal{D}(P_t \parallel P_0) \] 2. **Distinction (Durable)**: Unlike technical debt in code, which manifests as slower development velocity, data debt manifests as lower model accuracy even when…

### Data debt

**Definition 4.4** (Vol 1) · [ch04.md](chapters/ch04.md) · Chapter 4: Data Engineering & Pipeline Architecture

Data Debt is the compound interest of implicit coupling and missing documentation across the data stack. 1. Significance (quantitative) : It manifests as silent degradation, where the cost of maintenance scales superlinearly with system age due to unmanaged dependencies and distribution shifts (𝒟(𝑃 𝑡 ‖𝑃 0 )) . 2. Distinction (durable) : Unlike technical debt in code, which manifests as slower development, data debt manifests as lower accuracy even when the code is perfectly maintained. 3.…

### Data drift

**Definition 14.3** (Vol 1) · [ch14.md](chapters/ch14.md) · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

1. Significance (quantitative) : It represents a violation of the i.i.d. assumption (independent and identically distributed), causing accuracy to erode monotonically with the distributional divergence (𝒟(𝑃 𝑡 ‖𝑃 0 )) , empirically modeled as Accuracy (𝑡) ≈ Accuracy 0 -𝜆⋅𝒟(𝑃 𝑡 ‖𝑃 0 ) with 𝜆 fit per deployment. Because 𝑃(𝑌 |𝑋) is unchanged, retraining on fresh 𝑃(𝑋) data can recover performance (when the new input distribution overlaps the original support), unlike concept drift, where the label…

### Data Engineering

**Definition 4.1** (Vol 1) · [ch04.md](chapters/ch04.md) · Chapter 4: Data Engineering & Pipeline Architecture

Data Engineering is the infrastructure layer that manages the lifecycle of data from source to model, encompassing acquisition, transformation, storage, and governance. 1. **Significance (Quantitative)**: Its critical function is ensuring *Training-Serving Consistency* and preventing *Silent Degradation* by decoupling the model from raw data volatility. Within the iron law, it governs the Data Volume (\(D_{\text{vol}}\)) and ensures that it remains representative of the target distribution. 2.…

### Data engineering

**Definition 4.1** (Vol 1) · [ch04.md](chapters/ch04.md) · Chapter 4: Data Engineering & Pipeline Architecture

Data Engineering is the infrastructure layer that manages the lifecycle of data from source to model, encompassing acquisition, transformation, storage, and governance. 1. Significance (quantitative) : Its critical function is ensuring Training-Serving Consistency, preventing Silent Degradation by decoupling the model from the volatility of raw data. Within the iron law, it governs the Data Volume (𝐷 vol ) and ensures that it remains representative of the target distribution. 2. Distinction…

### Data parallelism

**Definition 6.2** (Vol 2) · [v2_ch06.md](chapters/v2_ch06.md) · Chapter 6: Distributed Training Systems

Data Parallelism is a distributed training strategy in which each worker holds a complete replica of the model and processes an independent shard of the minibatch, then synchronizes gradient updates via AllReduce so all replicas apply identical parameter changes each step. 2. Distinction (durable) : Unlike model parallelism, where parameters are partitioned so no single worker holds the full model, data parallelism requires every worker to have 1. Significance (quantitative) : With 𝑁 workers…

### Data poisoning

**Definition 15.4** (Vol 2) · [v2_ch15.md](chapters/v2_ch15.md) · Chapter 15: Robust AI

Data Poisoning is the corruption of training data to compromise model behavior at inference time, either by injecting malicious samples or modifying existing labels. 1. Significance (quantitative) : It undermines the foundational assumption of Data Integrity . Even a small fraction of poisoned samples (for example, <1 percent) can create Backdoors or systematic biases that remain latent until triggered by specific inputs during serving. 2. Distinction (durable) : Unlike Adversarial Attacks…

### Data selection

**Definition 9.1** (Vol 1) · [ch09.md](chapters/ch09.md) · Chapter 9: Data Selection & Active Learning

Data Selection is the process of maximizing the Information-Compute Ratio of a training dataset. 2. Distinction (durable) : Unlike data engineering, which focuses on the cleanliness and consistency of data, data selection focuses on the informativeness and diversity of the samples. 1. Significance (quantitative) : It identifies the smallest subset of data sufficient to define the decision boundary, reducing the total operations (𝑂) of the iron law by eliminating redundant or noisy samples (𝐷…

### Deep Learning

**Definition 5.1** (Vol 1) · [ch05.md](chapters/ch05.md) · Chapter 5: Neural Computation & Training Mechanics

**Deep Learning** is the computational paradigm of Hierarchical Feature Learning from raw data. 1. **Quantitative Significance**: By stacking nonlinear transformations, it replaces manual Feature Engineering with **Architecture Engineering**, enabling models to scale performance with both Data Volume (\(D_{\text{vol}}\)) and Peak Compute (\(R_{\text{peak}}\)). 2. **Durable Distinction**: Unlike Shallow Learning, which learns a single feature transformation, Deep Learning learns a Hierarchy of…

### Deep learning

**Definition 5.1** (Vol 1) · [ch05.md](chapters/ch05.md) · Chapter 5: Neural Computation & Training Mechanics

Deep Learning is the computational paradigm of Hierarchical Feature Learning from raw data. 1. Significance (quantitative) : By stacking nonlinear transformations, it replaces manual Feature Engineering with Architecture Engineering, enabling models to scale with both Data Volume (𝐷 vol ) and Compute (𝑅 peak ) . 2. Distinction (durable) : Unlike Shallow Learning, which learns a single transformation, Deep Learning learns a Hierarchy of Abstractions that can be fine-tuned for different tasks. 3.…

### Demographic parity

**Definition 17.3** (Vol 2) · [v2_ch17.md](chapters/v2_ch17.md) · Chapter 17: Responsible Engineering (Vol 2)

1. Significance (quantitative) : It is the simplest and most restrictive fairness metric. It requires the model to produce Equal Outcomes across groups, regardless of the underlying base-rate differences in the dataset. Demographic Parity is the fairness constraint where a model's positive prediction rate is independent of group membership (𝑃( 𝑌 = 1 ∣ 𝐴 = 𝑎) = 𝑃( 𝑌 = 1 ∣ 𝐴 = 𝑏)) . ̂ ̂ 2. Distinction (durable) : Unlike Equalized Odds (which focuses on error rates like False Positives),…

### Distributed training

**Definition 6.1** (Vol 2) · [v2_ch06.md](chapters/v2_ch06.md) · Chapter 6: Distributed Training Systems

Distributed Training is a training methodology that partitions the optimization loop across multiple compute nodes-distributing either data, model layers, or individual tensor operationsand coordinates their outputs through synchronized communication primitives to produce a single coherent model. 1. Significance (quantitative) : Distributed training becomes necessary when a model's memory requirement exceeds a single accelerator's capacity. GPT-3 (175B parameters) requires approximately 350 GB…

### Dynamic batching

**Definition 13.5** (Vol 1) · [ch13.md](chapters/ch13.md) · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Dynamic Batching is the runtime optimization of trading Latency for Throughput under stochastic arrival patterns. 2. Distinction (durable) : Unlike Static Batching, which is fixed during training, Dynamic Batching adaptively adjusts the batch size at Inference Time based on real-time traffic volume. 1. Significance (quantitative) : By buffering requests into a Batching Window, the scheduler amortizes fixed overheads (𝐿 lat ) across multiple inputs, pushing the system away from the memory-bound…

## E

### Edge ML

**Definition 2.3** (Vol 1) · [ch02.md](chapters/ch02.md) · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

- Edge Machine Learning is the deployment paradigm optimized for Latency Determinism and Data Locality by locating computation physically adjacent to data sources. 1. Significance (quantitative) : It circumvents the Distance Penalty (𝐿 lat ) of the cloud, trading elastic scale for a fixed Local Compute Capacity (𝑅 peak ) . 2. Distinction (durable) : Unlike Cloud ML, which prioritizes Throughput, Edge ML prioritizes Determinism and privacy. Unlike TinyML, Edge ML may still use workstationclass…

### Elastic training

**Definition 9.2** (Vol 2) · [v2_ch09.md](chapters/v2_ch09.md) · Chapter 9: Fleet Orchestration (Vol 2)

- Elastic Training is the capability of a distributed training job to dynamically adjust its worker count during execution without requiring a full restart. 1. Significance (quantitative) : It maximizes the System Duty Cycle (𝜂 hw ) by allowing training to continue through node failures and by absorbing idle capacity in the cluster. It requires Learning Rate Recalibration and gradient accumulation adjustment to maintain mathematical consistency as the global batch size changes. 2. Distinction…

## F

### Fat-tree

**Definition 4.6** (Vol 2) · [v2_ch04.md](chapters/v2_ch04.md) · Chapter 4: Network Fabrics

Fat-Tree is a hierarchical network topology in which the number of parallel paths-and therefore aggregate cross-sectional capacity-increases at each switch tier toward the spine, providing full bisection bandwidth and multiple equal-cost routes between any two nodes (Al-Fares et al. 2008). 1. Significance (quantitative) : Ak-ary fat-tree built from radix𝑘 switches supports 𝑘 2 /2 hosts in a two-tier (pod) configuration and 𝑘 3 /4 hosts in a three-tier configuration with full bisection…

### Feature Store

**Definition 4.3** (Vol 1) · [ch04.md](chapters/ch04.md) · Chapter 4: Data Engineering & Pipeline Architecture

A Feature Store is the architectural layer that centralizes the management of machine learning features, decoupling feature computation from consumption. 1. **Significance (Quantitative)**: It enforces point-in-time correctness, ensuring that historical data used for training (\(x_{t-\Delta}\)) is computed with identical logic to the real-time data served at inference (\(x_t\)), eliminating training-serving skew by design. 2. **Distinction (Durable)**: Unlike a general-purpose database, a…

### Feature store

**Definition 4.3** (Vol 1) · [ch04.md](chapters/ch04.md) · Chapter 4: Data Engineering & Pipeline Architecture

Feature Store is the architectural layer that centralizes the management of machine learning features, decoupling feature computation from consumption. 2. Distinction (durable) : Unlike a general-purpose database, a feature store is designed for dual storage modes: an offline store (columnar/batch) for training and an online store (key-value/low-latency) for serving. 1. Significance (quantitative) : It enforces point-in-time correctness, ensuring that historical data used for training (𝑥 𝑡-Δ )…

### Federated learning

**Definition 12.2** (Vol 2) · [v2_ch12.md](chapters/v2_ch12.md) · Chapter 12: Edge Intelligence (Vol 2)

Federated Learning is a decentralized training paradigm where distributed devices collaboratively train a shared model using local data while exchanging only model updates (gradients or weights). 1. Significance (quantitative) : It transforms the constraint of Data Locality into a privacy feature. Within the iron law, federated learning is constrained by the Wide-Area Bandwidth (BW) and the extreme Heterogeneity of the Fleet, where device-specific efficiency (𝜂 hw ) and availability can vary by…

### FinOps for ML

**Definition 13.1** (Vol 2) · [v2_ch13.md](chapters/v2_ch13.md) · Chapter 13: ML Operations at Scale

FinOps for ML is the practice of treating compute cost as a first-class engineering constraintmeasured in real-time per experiment and model, and optimized jointly with model accuracy and latency-rather than accounting for it retrospectively through annual budget reconciliation. 1. Significance (quantitative) : MLcompute costs scale steeply with experimentation volume. A team running 1,000 GPU-hours/day at \$3/GPU-hour spends \$3,000/day\$1.1M/year-on training alone. With per-experiment cost…

## G

### GPU Direct Storage

**Definition 5.4** (Vol 2) · [v2_ch05.md](chapters/v2_ch05.md) · Chapter 5: Data Storage — The Fuel Line

GPU Direct Storage (GDS) is a technology that enables a direct DMA path between NVMe storage devices and GPU memory, bypassing the host CPU and system DRAM. 2. Distinction (durable) : Unlike Traditional I/O, where every byte must be processed by the CPU and stored in kernel buffers, GDS provides Direct Memory Access between the storage controller and the accelerator. 1. Significance (quantitative) : It eliminates the 'Bounce Buffer' through system memory, reducing data loading latency (𝐿 lat )…

### Graceful degradation

**Definition 8.3** (Vol 2) · [v2_ch08.md](chapters/v2_ch08.md) · Chapter 8: Fault Tolerance and Reliability (Vol 2)

Graceful Degradation is a fault tolerance strategy in which a system responds to resource exhaustion or component failure by deliberately reducing service quality-falling back to a smaller model, serving cached results, or returning partial outputs-rather than failing completely, maintaining measurable availability at reduced capability. 1. Significance (quantitative) : Graceful degradation converts total outage risk into a controlled quality reduction. A recommendation system that falls back…

### Gradient descent

**Definition 5.3** (Vol 1) · [ch05.md](chapters/ch05.md) · Chapter 5: Neural Computation & Training Mechanics

Gradient Descent is the iterative algorithm that navigates the Loss Landscape by updating parameters in the direction of the negative gradient. 3. Common pitfall: Afrequent misconception is that Gradient Descent always finds the Global Minimum . In reality, it is a Local Optimizer that can become stuck in plateaus or local optima in nonconvex landscapes. 1. Significance (quantitative) : It transforms the Learning Problem into an Optimization Problem, trading computational cycles ( 𝑂 ) for error…

### Gradient synchronization

**Definition 7.1** (Vol 2) · [v2_ch07.md](chapters/v2_ch07.md) · Chapter 7: Collective Communication

Gradient Synchronization is the collective communication protocol executed at each training step in which every worker transmits its locally computed gradient tensor to all other workers, receives their gradients, and computes an aggregate update that all workers apply identically to their model copies. 1. Significance (quantitative) : A70B-parameter model in BF16 generates 140 GB of gradient data per worker per step. Synchronizing across 1,000 GPUs via ring AllReduce at 50 GB/s per link…

## H

### Hardware Acceleration

**Definition 11.1** (Vol 1) · [ch11.md](chapters/ch11.md) · Chapter 11: Hardware Acceleration, Compilers & SoCs

**Hardware Acceleration** is the practice of replacing general-purpose processor logic with domain-specific silicon optimized for a narrow class of operations, trading programmability for compute density (\(R_{\text{peak}}\)) and energy efficiency (\(\eta_{\text{hw}}\)) gains that regular, data-parallel workloads like matrix multiplication can exploit. * **Throughput Scaling:** An NVIDIA A100 GPU delivers 312 TFLOPS of BF16 tensor compute, compared to 1–2 TFLOPS on server-class CPUs without…

### Hardware acceleration

**Definition 11.1** (Vol 1) · [ch11.md](chapters/ch11.md) · Chapter 11: Hardware Acceleration, Compilers & SoCs

Hardware Acceleration is the practice of replacing general-purpose processor logic with domain-specific silicon optimized for a narrow class of operations, trading programmability for the compute density (𝑅 peak ) and energy efficiency (𝜂 hw ) gains that regular, data-parallel workloads like matrix multiplication can exploit. 2. Distinction (durable) : Unlike a general-purpose CPU, which is optimized to minimize latency for any single instruction in an arbitrary serial program, an accelerator…

### Hardware-Software Co-Design

**Definition 11.2** (Vol 1) · [ch11.md](chapters/ch11.md) · Chapter 11: Hardware Acceleration, Compilers & SoCs

**Hardware-Software Co-design** is a development methodology that intentionally violates traditional hardware-software abstraction layers, allowing algorithmic constraints to inform silicon design and hardware capabilities to directly shape algorithm formulation. * **Quantized Operations:** Algorithmic quantization (e.g., INT8/INT4) only achieves speedups because accelerators are physically built to execute multiple low-precision operations in the same die area as a single FP32 operation (e.g.,…

### Hardware-software co-design

**Definition 11.2** (Vol 1) · [ch11.md](chapters/ch11.md) · Chapter 11: Hardware Acceleration, Compilers & SoCs

Hardware-Software Co-design is a development methodology that intentionally violates traditional hardware-software abstraction layers, allowing algorithm constraints to inform silicon design and hardware capabilities to directly shape algorithm formulation. 1. Significance (quantitative) : Co-design unlocks gains unavailable to either layer acting alone. INT8 quantization delivers 2-4 × throughput improvement not because 8-bit arithmetic is faster in the abstract, but because NVIDIA Tensor…

### Hierarchy-aware parallelism

**Definition 2.13** (Vol 2) · [v2_ch02.md](chapters/v2_ch02.md) · Chapter 2: Compute Infrastructure

Hierarchy-Aware Parallelism is the strategy of mapping different parallel execution modes to the physical bandwidth tiers of the cluster. 1. Significance (quantitative) : It ensures that high-frequency synchronization (for example, Tensor Parallelism) stays on the fastest links (NVLink), while lower-frequency tasks (for example, Data Parallelism) use slower tiers (InfiniBand). This alignment maximizes the System Efficiency (𝜂 hw ) by minimizing communication stalls (𝐿 lat ) . 2. Distinction…

### High bandwidth memory (HBM)

**Definition 2.1** (Vol 2) · [v2_ch02.md](chapters/v2_ch02.md) · Chapter 2: Compute Infrastructure

HighBandwidthMemory(HBM) is a 3D-stacked DRAM architecture in which multiple memory dies are vertically bonded and connected to the processor through thousands of ThroughSilicon Vias (TSVs) on a shared silicon interposer, eliminating the centimeter-scale PCB traces of conventional DRAM and replacing them with micrometer-scale vertical paths. - 3 HBM (High Bandwidth Memory) : Standardized by JEDEC in 2013 as a joint development between AMD and SK Hynix, originally for graphics cards. ML…

### Hybrid ML

**Definition ** (Vol 1) · [ch02.md](chapters/ch02.md) · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Hybrid ML is the architectural strategy of hierarchically distributing machine learning tasks across cloud, edge, mobile, and tiny devices. It optimizes the latency-compute Pareto frontier by executing time-sensitive tasks locally while offloading compute-intensive processing to the cloud.

### Hybrid ML

**Definition 2.7** (Vol 1) · [ch02.md](chapters/ch02.md) · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Hybrid Machine Learning is the architectural strategy of Hierarchical Distribution across cloud and edge resources. 3. Common pitfall: A frequent misconception is that Hybrid ML is just 'running two models.' In reality, it is a Unified Data Fabric where the state must be synchronized across disparate hardware to ensure consistency. 1. Significance (quantitative) : It partitions the ML workload across the latency-compute Pareto frontier, minimizing the Distance Penalty (𝐿 lat ) for reactive…

## I

### Incast

**Definition 4.9** (Vol 2) · [v2_ch04.md](chapters/v2_ch04.md) · Chapter 4: Network Fabrics

Incast is a many-to-one traffic pattern in which a large number of senders simultaneously transmit data to a single receiver port, concentrating line-rate traffic from multiple sources into a single switch queue and causing buffer overflow even when the rest of the fabric is uncongested. 1. Significance (quantitative) : In the reduce phase of AllReduce, every participating GPU simultaneously sends gradients toward the same aggregation points. With 256 senders each at 50 GB/s targeting one…

### Inductive Bias

**Definition 6.1** (Vol 1) · [ch06.md](chapters/ch06.md) · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

An **inductive bias** is a structural constraint built into a model architecture that restricts the hypothesis space, enabling generalization from finite data by encoding domain-specific assumptions (such as spatial locality or sequential ordering) directly into the computational graph. * **Quantitative Significance:** Inductive bias directly reduces the required data volume (\(D_{\text{vol}}\)) for generalization. For a \(224 \times 224\) image, a \(3 \times 3\) convolutional kernel reduces…

### Inductive bias

**Definition 6.1** (Vol 1) · [ch06.md](chapters/ch06.md) · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Inductive Bias is a structural constraint built into a model architecture that restricts the hypothesis space, enabling generalization from finite data by encoding domain-specific assumptions (such as spatial locality or sequential ordering) directly into the computational graph. 2. Distinction (durable) : Unlike Regularization (which penalizes hypothesis complexity at training time via L1/L2 terms), Inductive Bias eliminates entire hypothesis classes at architecture design time-a CNN cannot…

## K

### KV cache

**Definition 11.2** (Vol 2) · [v2_ch11.md](chapters/v2_ch11.md) · Chapter 11: Inference at Scale (Vol 2)

- KV Cache is a memory buffer that stores previously computed Key and Value attention vectors to avoid redundant computation during autoregressive generation. 1. Significance (quantitative) : It reduces per-token computation from 𝑂(𝑡 2 ) to 𝑂(𝑡) , making generation feasible for long sequences. However, it grows linearly with sequence length and batch size, often exceeding the memory footprint of the model weights and becoming the primary constraint on Concurrent Capacity . 2. Distinction…

## L

### Latency budget

**Definition 13.2** (Vol 1) · [ch13.md](chapters/ch13.md) · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Latency Budget is the time capital allocated to a request, strictly bounded by the end-to-end service level objective (SLO) . 7 gRPC (gRPC Remote Procedure Call) : Evolved from Google's internal Stubby framework, gRPC was designed to minimize the overhead of the billions of interservice calls made per second. It achieves this by pairing HTTP/2 for persistent connection multiplexing with Protobuf for efficient binary serialization, directly addressing the handshake and parsing latencies inherent…

### LLM performance metrics

**Definition 13.6** (Vol 1) · [ch13.md](chapters/ch13.md) · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

LLM Performance Metrics are the two-dimensional measurements of latency for streaming autoregressive generation. 25 Autoregressive: From Greek auto(self) and Latin regressus (a going back)-the output 'regresses' on itself. George Udny Yule introduced autoregressive models in 1927 for analyzing sunspot cycles. In language modeling, each output token conditions on all previously generated tokens, creating a serial dependency that prevents the parallelism exploited during training. This serial…

## M

### Machine Learning Accelerator

**Definition 11.3** (Vol 1) · [ch11.md](chapters/ch11.md) · Chapter 11: Hardware Acceleration, Compilers & SoCs

An **ML Accelerator** is a domain-specific processor whose silicon is designed primarily for the dense matrix operations and regular data flow of neural networks, achieving high peak throughput (\(R_{\text{peak}}\)) and memory bandwidth utilization by dedicating die area to arithmetic units rather than general-purpose control logic. | Era | Bottleneck Target | Architecture Examples | Characteristics | | :--- | :--- | :--- | :--- | | **1980s** | Precision (Scalar FP) | FPU (Intel 8087), DSP |…

### Machine learning benchmarking

**Definition 12.1** (Vol 1) · [ch12.md](chapters/ch12.md) · Chapter 12: Benchmarking Systems & Power Measurement

Machine Learning Benchmarking is the empirical measurement of a system's end-to-end performance on representative ML workloads, designed to decouple marketed peak specifications from the sustained throughput and latency achievable under realistic operating conditions. 1. Significance (quantitative) : The gap between peak and sustained performance is large and structurally unavoidable. An A100 GPU delivers 312 TFLOPS BF16 at peak, but production transformer training runs typically sustain 90-155…

### Machine learning fleet

**Definition 1.1** (Vol 2) · [v2_ch01.md](chapters/v2_ch01.md) · Chapter 1: Introduction to ML Systems

Machine Learning Fleet is a distributed system of thousands of interconnected accelerators, storage arrays, and network fabrics designed to operate as a single coherent computer. 2. Distinction (durable) : Unlike Traditional Clusters (for example, Spark, MapReduce) that manage independent, asynchronous jobs, an ML Fleet operates under Synchronous Tight Coupling, requiring near-perfect reliability to maintain throughput. 1. Significance (quantitative) : It coordinates synchronous state across…

### Machine learning frameworks

**Definition 7.1** (Vol 1) · [ch07.md](chapters/ch07.md) · Chapter 7: ML Frameworks (TF, PyTorch, JAX)

Machine Learning Frameworks are software systems that translate high-level mathematical model definitions into hardware-optimized execution plans by managing the computational graph, automatic differentiation, kernel dispatch, and memory allocation across the hardware hierarchy. 2. Distinction (durable) : Unlike a numerical library such as NumPy, which executes each operation immediately (eager evaluation), an ML framework can defer execution to analyze the full computational graph and apply…

### Machine learning lifecycle

**Definition 3.1** (Vol 1) · [ch03.md](chapters/ch03.md) · Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)

Machine Learning Lifecycle is the continuous engineering discipline of managing System Entropy across the Data, Algorithm, and Machine axes. 1. Significance (quantitative) : It transforms the linear software 'release' into a continuous loop of monitoring, retraining, and redeployment to maintain the system's Duty Cycle (𝜂 hw ) . 2. Distinction (durable) : Unlike a traditional software lifecycle, which degrades primarily through code modification, the ML lifecycle recognizes that models degrade…

### Machine learning system benchmarks

**Definition 12.2** (Vol 1) · [ch12.md](chapters/ch12.md) · Chapter 12: Benchmarking Systems & Power Measurement

Machine Learning System Benchmarks are standardized evaluation protocols that hold the workload and quality target constant while varying the hardware-software stack, measuring 𝜂 hw =𝑅 sustained /𝑅 peak and 𝐿 lat to isolate infrastructure efficiency from algorithmic improvements. 2. Distinction (durable) : Unlike algorithmic benchmarks (which vary model architectures and training procedures to improve convergence accuracy), system benchmarks hold the algorithm fixed and vary the implementation…

### Machine learning systems

**Definition 1.1** (Vol 1) · [ch01.md](chapters/ch01.md) · Chapter 1: Introduction to ML Systems

Machine Learning Systems are software systems whose core behavior is determined by parameters learned from data rather than explicitly programmed rules, making performance a function of data quality, algorithm choice, and hardware capacity simultaneously. 2. Distinction (durable) : Unlike traditional software, whose correctness degrades only when code changes, an ML system's accuracy degrades when the world changes. Model weights are fixed after deployment, but the distribution of inputs…

### Mapping in AI Acceleration

**Definition 11.6** (Vol 1) · [ch11.md](chapters/ch11.md) · Chapter 11: Hardware Acceleration, Compilers & SoCs

**Mapping in AI Acceleration** is the process of binding the Logical Computation Graph to the Physical Hardware Topology by deciding which operations execute on which processing elements, which data resides in which memory tier, and in what temporal order. Mapping defines three axes of execution: 1. **Computation placement:** Assigning operations to physical processing elements (PEs) to balance load and minimize stalls. 2. **Memory allocation:** Specifying where weight and activation tensors…

### Mapping in AI acceleration

**Definition 11.6** (Vol 1) · [ch11.md](chapters/ch11.md) · Chapter 11: Hardware Acceleration, Compilers & SoCs

Mapping in AI Acceleration is the process of binding the Logical Computation Graph to the Physical Hardware Topology by deciding which operations execute on which processing elements, which data resides in which memory tier, and in what temporal order. 2. Distinction (durable) : Unlike Traditional Compilation (which targets a linear instruction stream on a von Neumann processor), Mapping targets a Dataflow Architecture where 1. Significance (quantitative) : Within the D·A·M taxonomy, mapping is…

### MLaccelerator

**Definition 11.3** (Vol 1) · [ch11.md](chapters/ch11.md) · Chapter 11: Hardware Acceleration, Compilers & SoCs

Machine Learning Accelerators are domain-specific processors whose silicon is designed primarily for the dense matrix operations and regular data flow of neural networks, achieving high 𝑅 peak and memory bandwidth utilization for these workloads by devoting die area to arithmetic units rather than to general-purpose control logic. 2. Distinction (durable) : Unlike a general-purpose CPU, which executes complex, branchdependent serial programs efficiently by minimizing per-instruction latency, an…

### MLOps

**Definition 14.1** (Vol 1) · [ch14.md](chapters/ch14.md) · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Machine Learning Operations (MLOps) is the engineering discipline that closes the feedback loop between model behavior and data reality by automating retraining, validation, and deployment in response to measurable production drift (Kreuzberger et al. 2023). 1. Significance (quantitative) : The cost of not closing this loop shows up in reported production deployments: recommendation models without drift monitoring can lose on the order of 10-20 percent absolute accuracy within six months as…

### MLsystems TCO

**Definition 13.2** (Vol 2) · [v2_ch13.md](chapters/v2_ch13.md) · Chapter 13: ML Operations at Scale

Total Cost of Ownership (TCO) for ML Systems is the complete economic accounting of developing, deploying, and operating machine learning capabilities across their full lifecycle. 1. Significance (quantitative) : It captures the Cost Inversion of scale: while training costs are a one-time 'upfront' operation (𝑂) , the cumulative Inference TCO grows linearly with user adoption and time, often exceeding development costs by 5 × to 10 × over a 3-year period. 3. Common pitfall: Afrequent…

### MLtraining benchmarks

**Definition 12.3** (Vol 1) · [ch12.md](chapters/ch12.md) · Chapter 12: Benchmarking Systems & Power Measurement

MLTraining Benchmarks measure the Rate of Convergence per unit of resource (time, energy, cost). 1. Significance (quantitative) : They validate the system's ability to sustain high arithmetic intensity across distributed accelerators while managing the communication overhead (𝐿 lat ) of gradient synchronization. 2. Distinction (durable) : Unlike inference benchmarks, which focus on input-output latency, training benchmarks focus on throughput (𝜂 hw ) and total training time (𝑇 train ) . 3.…

### Mobile ML

**Definition 2.5** (Vol 1) · [ch02.md](chapters/ch02.md) · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Mobile Machine Learning is the deployment paradigm bounded by Thermal Design Power (TDP) and battery energy. 1. Significance (quantitative) : It is constrained by the heat dissipation capacity of passive cooling (typically 2-3 W), requiring architectures that prioritize sustained energy efficiency over peak throughput (𝑅 peak ) . 3. Common pitfall: A frequent misconception is that mobile ML performance is a fixed value. In reality, it is a Time-Varying Constraint: performance often drops as the…

### Model compression

**Definition 10.1** (Vol 1) · [ch10.md](chapters/ch10.md) · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

Model Compression is a family of techniques that reduce a trained model's computational cost and memory footprint by eliminating redundant parameters (pruning), reducing numerical precision (quantization), or transferring learned behavior into a smaller architecture (distillation), while preserving as much predictive accuracy as possible. 1. Significance (quantitative) : Compression directly reduces both iron law terms. INT8 quantization of a 175B-parameter large language model (LLM) cuts…

### Model FLOPs Utilization (MFU)

**Definition 8.4** (Vol 1) · [ch08.md](chapters/ch08.md) · Chapter 8: Staged Model Training & Parallelism

**Model FLOPs Utilization (MFU)** is the hardware-agnostic efficiency metric defined as the ratio of useful model computations performed per step to the peak theoretical hardware capability: \[ \text{MFU} = \frac{C_{\text{model}}}{R_{\text{peak}} \cdot T_{\text{step}}} \] Where \(C_{\text{model}}\) is the theoretical FLOP count per training step based on the model parameters (excluding activation recomputation and padding), \(R_{\text{peak}}\) is the peak accelerator FLOP rate, and…

### Model FLOPs utilization (MFU)

**Definition 2.5** (Vol 2) · [v2_ch02.md](chapters/v2_ch02.md) · Chapter 2: Compute Infrastructure

Model FLOPs Utilization (MFU) is the ratio of a model's theoretical FLOP count per training step-calculated from architecture parameters alone-to the product of hardware peak throughput and elapsed wall-clock time, measuring what fraction of the hardware's theoretical capacity is doing useful model computation rather than overhead. 2. Distinction (durable) : Unlike hardware utilization (the fraction of clock cycles during which the GPU reports being 'busy'), MFU counts only cycles spent on…

### Model FLOPs utilization (MFU)

**Definition 10.3** (Vol 2) · [v2_ch10.md](chapters/v2_ch10.md) · Chapter 10: Performance Engineering (Vol 2)

1. Significance (quantitative) : At fleet scale, MFU aggregates across all nodes: communication overhead, load imbalance, and pipeline bubbles each compound the utilization loss, so fleet MFU is consistently below single-node MFU. It is the primary diagnostic for whether hardware investment is translating into model progress, and a 1 percent improvement in MFU across a 10,000-GPU cluster reduces cost by the equivalent of 100 GPUs. Model FLOPs Utilization (MFU) is the fraction of the hardware's…

### Model serving

**Definition 13.1** (Vol 1) · [ch13.md](chapters/ch13.md) · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Model Serving is the operational phase that provides model predictions to end-users or downstream systems under strict latency constraints. 1 Jevons Paradox: William Stanley Jevons observed in 1865 that efficiency improvements in coal-powered steam engines increased total coal consumption by making steam power economically viable for applications previously too costly. The same dynamic governs AI inference: each 10 × cost reduction opens application classes that were economically infeasible at…

### Model validation

**Definition 3.2** (Vol 1) · [ch03.md](chapters/ch03.md) · Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)

Model Validation is the rigorous verification that a model meets business constraints-service level agreement (SLA), fairness, and cost-on production-representative data. 1. Significance (quantitative) : It moves beyond 'test set accuracy' to test for robustness against distribution shift (𝐷 vol ) and efficiency against hardware limits (𝑅 peak, BW ) . 2. Distinction (durable) : Unlike model evaluation, which measures performance on a static test set, model validation confirms that the model…

### Multilayer Perceptron (MLP)

**Definition 6.2** (Vol 1) · [ch06.md](chapters/ch06.md) · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

An **MLP** is a feed-forward neural network architecture that applies fully connected layers in sequence, where every neuron in layer \(l-1\) connects to every neuron in layer \(l\), encoding no structural assumptions about the input domain. * **Universal Approximation Theorem (UAT):** A sufficiently wide single-hidden-layer MLP with non-linear activation functions can approximate any continuous function on a compact domain. * **Manifold Hypothesis:** High-dimensional real-world data (e.g.,…

### Multilayer perceptrons

**Definition 6.2** (Vol 1) · [ch06.md](chapters/ch06.md) · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Multilayer Perceptrons are feed-forward neural network architectures that apply fully connected layers in sequence, where every neuron in one layer connects to every neuron in the next, encoding no structural assumption about the input domain. 1. Significance (quantitative) : The lack of structural prior incurs 𝑂(𝑑 2 ) parameter scaling per layer (where 𝑑 is layer width): a single layer mapping 1,024 inputs to 1,024 outputs requires 1,048,576 parameters and 2 MB of weight memory in FP16. A 3×3…

## N

### Node

**Definition 2.7** (Vol 2) · [v2_ch02.md](chapters/v2_ch02.md) · Chapter 2: Compute Infrastructure

Node is a physical server chassis that aggregates multiple accelerators-typically 8-through a high-speed intra-node interconnect (NVLink or ICI), creating the fundamental boundary between high-bandwidth local communication and the order-of-magnitude slower inter-node network fabric. 2. Distinction (durable) : Unlike a single accelerator (which provides fast HBM bandwidth but limited capacity), a node aggregates 8 × the HBM capacity and 8 × the compute of a single chip - enough to place large…

### Non-blocking fabric

**Definition 4.5** (Vol 2) · [v2_ch04.md](chapters/v2_ch04.md) · Chapter 4: Network Fabrics

Non-blocking Fabric is a network topology in which any permutation of input-output port pairs can communicate simultaneously at full line rate without internal contention, achieved by ensuring that uplink capacity at every switch tier equals or exceeds downlink capacity. 1. Significance (quantitative) : In ML fleets, a non-blocking fabric ensures that AllReduce traffic from any accelerator subset does not compete for shared links, preserving the full BW term of the iron law. A 2:1…

## O

### On-device learning

**Definition 12.1** (Vol 2) · [v2_ch12.md](chapters/v2_ch12.md) · Chapter 12: Edge Intelligence (Vol 2)

On-Device Learning is the local training or adaptation of machine learning models directly on deployed hardware without requiring server connectivity. 1. Significance (quantitative) : It enables Hyper-Personalization andautonomousoperation under severe resource constraints. Within the iron law, on-device learning must maximize Energy Efficiency (𝜂 hw ) because every gradient update consumes limited battery power and must compete with other system tasks for Peak Throughput (𝑅 peak ) . 2.…

### Overfitting

**Definition 5.4** (Vol 1) · [ch05.md](chapters/ch05.md) · Chapter 5: Neural Computation & Training Mechanics

Overfitting is the failure of Generalization caused by memorizing Noise instead of Signal . 2. Distinction (durable) : Unlike Underfitting (where the model is too simple), Overfitting is a Symmetry Breaking problem: the model becomes too specialized to the specific training sample. 1. Significance (quantitative) : It occurs when a model's Capacity exceeds the information content of the training data (𝐷) , allowing it to satisfy the training objective without learning the underlying…

## P

### PAM4 signaling

**Definition 4.1** (Vol 2) · [v2_ch04.md](chapters/v2_ch04.md) · Chapter 4: Network Fabrics

PAM4 Signaling is an electrical modulation scheme that uses four distinct voltage levels to encode two bits per symbol period, doubling the data rate achievable over a given physical medium without requiring a higher symbol rate. 1. Significance (quantitative) : PAM4 enables 400 Gb/s and 800 Gb/s link speeds that sustain the BW required for large-scale gradient synchronization. However, the reduced gap between voltage levels increases susceptibility to noise, requiring Forward Error Correction…

### Parallel file system

**Definition 5.1** (Vol 2) · [v2_ch05.md](chapters/v2_ch05.md) · Chapter 5: Data Storage — The Fuel Line

Parallel File System (PFS) is a distributed storage architecture that stripes data across many storage servers to provide aggregate throughput exceeding the capacity of any single device. 1. Significance (quantitative) : APFS aggregates BW io linearly with the number of storage servers (Object Storage Servers). A Lustre cluster with 20 OSS nodes each delivering 10 GB/s provides 200 GB/s aggregate, versus a single NAS server capped at 10 GB/s, enabling a training job to load a 10 GB striped…

### Pipeline bubble

**Definition 2.4** (Vol 2) · [v2_ch02.md](chapters/v2_ch02.md) · Chapter 2: Compute Infrastructure

- Pipeline Bubble is the idle time in pipeline-parallel training caused by stages waiting for inputs from upstream workers during the fill and drain phases of a micro-batch cycle. 1. Significance (quantitative) : It represents a direct loss in System Efficiency (𝜂 hw ) . For a model with 𝑝 pipeline stages and 𝑚 micro-batches, the bubble fraction is approximately (𝑝 -1)/𝑚, dictating the maximum theoretical utilization of the cluster. 3. Common pitfall: Afrequent misconception is that bubbles can…

### Pipeline parallelism

**Definition 6.5** (Vol 2) · [v2_ch06.md](chapters/v2_ch06.md) · Chapter 6: Distributed Training Systems

Pipeline Parallelism is a model parallelism technique that partitions a neural network's layers into sequential stages assigned to different devices, passing activations forward and gradients backward between stages while overlapping computation across stages using micro-batches to maintain throughput. 1. Significance (quantitative) : Inter-stage communication transmits only the activation tensor at each stage boundary, sized as microbatch × seq\_len × hidden ×2 bytes at BF16. For a hidden…

### Power usage effectiveness (PUE)

**Definition 2.10** (Vol 2) · [v2_ch02.md](chapters/v2_ch02.md) · Chapter 2: Compute Infrastructure

1. Significance (quantitative) : It measures the Infrastructure Overhead of the data center. A PUE of 1.0 is the theoretical ideal; a PUE of 1.10 means that for every 100 watts of computation, an additional 10 watts are required for cooling and power distribution. Power Usage Effectiveness (PUE) is the ratio of total facility power consumption to the power consumed specifically by IT equipment ( 𝑃 facility /𝑃 IT ). 2. Distinction (durable) : Unlike Computing Efficiency (which focuses on FLOPs…

### Prefill and decode phases

**Definition 11.5** (Vol 2) · [v2_ch11.md](chapters/v2_ch11.md) · Chapter 11: Inference at Scale (Vol 2)

Prefill and Decode Phases are the two distinct computational regimes of transformer-based LLM inference. 2. Distinction (durable) : Unlike Single-Pass Inference (for example, ImageNet), where the resource bottleneck is constant, LLM inference switches between these regimes at every request, requiring Iteration-Level Scheduling to maintain utilization. 1. Significance (quantitative) : The Prefill Phase (processing the prompt) is ComputeBound (𝑅 peak ) with high arithmetic intensity, while the…

### Priority flow control

**Definition 4.8** (Vol 2) · [v2_ch04.md](chapters/v2_ch04.md) · Chapter 4: Network Fabrics

Priority Flow Control (PFC) is a link-layer mechanism that prevents switch buffer overflow by sending PAUSE frames to an upstream sender when a port's queue depth crosses a configured threshold, throttling injection on a per-priority basis without dropping packets. 1. Significance (quantitative) : PFC is the foundation for lossless Ethernet required by RoCEv2 RDMA. A PFC PAUSE frame must reach the upstream sender within one roundtrip time (roughly 1-5 μs at switch-to-switch distances) before…

### Priority inversion

**Definition 9.1** (Vol 2) · [v2_ch09.md](chapters/v2_ch09.md) · Chapter 9: Fleet Orchestration (Vol 2)

Priority Inversion is a scheduling pathology in which a high-priority task is forced to wait for a lower-priority task to release a shared resource. 1. Significance (quantitative) : It reduces the progress rate of the entire fleet to that of the lowest-priority job. In ML clusters, this typically occurs when a low-priority job holding GPUs is starved of auxiliary resources (for example, BW for checkpointing), preventing it from finishing and releasing the accelerators needed by high-priority…

### Privacy

**Definition 14.2** (Vol 2) · [v2_ch14.md](chapters/v2_ch14.md) · Chapter 14: Security & Privacy (Vol 2)

Privacy is the protection of sensitive information from unauthorized disclosure, inference, and misuse across the ML lifecycle. 1. Significance (quantitative) : It limits the exposure risk of training data and user inputs. Privacy-preserving techniques (for example, differential privacy) typically introduce a utility-privacy trade-off: increasing privacy adds 'noise' to the gradients, which can increase the total operations (𝑂) required to reach a target accuracy. 2. Distinction (durable) :…

### Pruning

**Definition 10.2** (Vol 1) · [ch10.md](chapters/ch10.md) · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

Pruning is the sparsification of the Parameter Space by removing weights that contribute minimal information to the loss landscape. 2. Distinction (durable) : Unlike Quantization, which reduces the Precision of every weight, Pruning reduces the Count of weights by identifying and eliminating redundancy. 1. Significance (quantitative) : It converts dense matrices into sparse structures, reducing the Memory Footprint and the total Data Volume (𝐷 vol ) by as much as 10 × without significant…

## Q

### Quantization

**Definition 10.3** (Vol 1) · [ch10.md](chapters/ch10.md) · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

- Quantization is the reduction of Information Fidelity by mapping high-precision continuous values to a lower-precision discrete set. 1. Significance (quantitative) : It reduces the Memory Bandwidth ( BW ) and energy consumption by 4 × (FP32 to INT8) or more, exploiting the inherent robustness of neural networks to low-precision arithmetic. 2. Distinction (durable) : Unlike Pruning, which reduces the Count of parameters, Quantization reduces the Bit-Depth of every parameter and activation in…

## R

### Rack

**Definition 2.9** (Vol 2) · [v2_ch02.md](chapters/v2_ch02.md) · Chapter 2: Compute Infrastructure

Rack is the physical infrastructure unit-a standardized 42U enclosure-that houses multiple compute nodes, a Top-of-Rack (ToR) switch (the first network aggregation point connecting all nodes in the rack to the broader cluster fabric), power distribution units, and cooling distribution manifolds, defining the granularity at which power and cooling capacity must be provisioned. 1. Significance (quantitative) : AI rack power density has grown dramatically: a rack of 4 DGXH100nodes contains 32 GPUs…

### Recurrent Neural Network (RNN)

**Definition 6.4** (Vol 1) · [ch06.md](chapters/ch06.md) · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

An **RNN** is a sequence-processing architecture that updates a hidden state vector \(h_t\) at each time step \(t\) according to \(h_t = f(h_{t-1}, x_t)\), propagating temporal context with constant \(O(1)\) inference memory scaling. * **Sequential Bottleneck:** The sequential dependency \(h_{t-1} \to h_t\) prevents parallel execution across the sequence (time) dimension during both training and inference. * **Vanishing/Exploding Gradients:** Backpropagation Through Time (BPTT) computes…

### Recurrent neural networks

**Definition 6.4** (Vol 1) · [ch06.md](chapters/ch06.md) · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

1. Significance (quantitative) : The fixed-size state provides 𝑂(1) inference memory regardless of sequence length-processing a 10,000-token sequence requires the same memory as a 10-token sequence-but the sequential update rule creates a sequential bottleneck where all 𝑇 steps must execute in order, directly contributing to the 𝐿 lat term of the iron law and making RNNs unable to exploit GPU parallelism across the time dimension during training. Recurrent Neural Networks (RNNs) are…

### Remote direct memory access (RDMA)

**Definition 4.2** (Vol 2) · [v2_ch04.md](chapters/v2_ch04.md) · Chapter 4: Network Fabrics

Remote Direct Memory Access (RDMA) is a networking technology that allows one machine to read or write the memory of another machine directly, bypassing the operating system kernel and CPU of both endpoints by offloading transport processing to the network interface card. 1. Significance (quantitative) : RDMAreduces end-to-end message latency from the 50-100 μs typical of kernel TCP to approximately 1-2 μs, cutting the 𝐿 lat term in the iron law by 25-50 × . For a 175B-parameter model…

### Responsible AI

**Definition 17.1** (Vol 2) · [v2_ch17.md](chapters/v2_ch17.md) · Chapter 17: Responsible Engineering (Vol 2)

Responsible AI is the practice of designing, auditing, and operating ML systems to measurable fairness, safety, privacy, and accountability standards-translating ethical principles into verifiable system properties that constrain model training, deployment decisions, and operational monitoring. 1. Significance (quantitative) : Responsible AI constraints impose real costs: fairness-aware training algorithms add 5-15 percent to training time; real-time bias monitoring adds 10-20 ms per inference;…

### Responsible AI engineering

**Definition 15.2** (Vol 1) · [ch15.md](chapters/ch15.md) · Chapter 15: Responsible Engineering & Compliance

Responsible AI Engineering is the engineering discipline of designing, deploying, and maintaining systems with probabilistic outputs by operationalizing societal and regulatory requirements as testable constraints on the D·A·M axes, bounding which values of 𝐷 vol, 𝑂, and 𝑅 peak ⋅ 𝜂 hw are permissible. 1. Significance (quantitative) : Each D·A·M axis acquires concrete governance constraints: the Data axis is bounded by privacy regulations such as the General Data Protection Regulation (GDPR),…

### Ridge point

**Definition 2.2** (Vol 2) · [v2_ch02.md](chapters/v2_ch02.md) · Chapter 2: Compute Infrastructure

Achievable FLOPS = min (𝑅 peak, BW ×𝐼) (2.1) Equation 2.1 has a direct physical interpretation. If the workload's arithmetic intensity is low (it needs many bytes per operation), then performance is limited by how fast memory can deliver those bytes. The achievable FLOPS grows linearly with 𝐼, tracing a sloped line on a log-log plot. If the arithmetic intensity is high (each byte fuels many operations), then performance plateaus at the hardware's peak compute rate, regardless of further…

### Robust AI

**Definition 15.1** (Vol 2) · [v2_ch15.md](chapters/v2_ch15.md) · Chapter 15: Robust AI

Robust AI is the measurable systems property that a model's predictions remain valid-within specified error bounds-under distribution shift, adversarial perturbation, and hardware or software faults, as opposed to the average-case accuracy achieved under ideal i.i.d. conditions. 1. Significance (quantitative) : Robustness is quantified by worst-case guarantees: a certified robust classifier guarantees accuracy above a threshold for all inputs within an ℓ ∞ ball of radius 𝜀 around any test…

## S

### Security

**Definition 14.1** (Vol 2) · [v2_ch14.md](chapters/v2_ch14.md) · Chapter 14: Security & Privacy (Vol 2)

Security is the set of system properties (confidentiality, integrity, and availability) that protect an ML system's data, model weights, and inference pipeline from intentional adversarial actions, spanning both the infrastructure layer (network intrusion, credential theft) and the algorithmic layer (model extraction, prompt injection, adversarial examples). 1. Significance (quantitative) : Security failures operate on both surfaces simultaneously. At the infrastructure layer, a stolen…

### SLO vs. SLA

**Definition 12.5** (Vol 1) · [ch12.md](chapters/ch12.md) · Chapter 12: Benchmarking Systems & Power Measurement

SLOs and SLAs are performance commitment specifications: a Service Level Objective (SLO) is the internal engineering target that the team optimizes toward, while a Service Level Agreement (SLA) is the external contractual threshold whose breach triggers financial penalties. 1. Significance (quantitative) : SLOs directly constrain the 𝐿 lat term in the iron law by setting a hard latency ceiling that the serving system must satisfy at a given percentile. A typical production setup sets the SLO at…

### Small file problem

**Definition 5.2** (Vol 2) · [v2_ch05.md](chapters/v2_ch05.md) · Chapter 5: Data Storage — The Fuel Line

- Small File Problem is a pathological I/O pattern where millions of individually small files overwhelm the metadata server of a storage system. 1. Significance (quantitative) : It reduces effective I/O Bandwidth ( BWio ) to a fraction of its theoretical rating because each file requires its own metadata operations ( open, stat, close ). With 10,000 workers simultaneously accessing small files, the metadata server becomes a Serialization Point that idles the entire cluster. 3. Common pitfall:…

### Speculative decoding

**Definition 11.4** (Vol 2) · [v2_ch11.md](chapters/v2_ch11.md) · Chapter 11: Inference at Scale (Vol 2)

Speculative Decoding is a latency optimization that uses a smaller Draft Model to predict multiple future tokens, which are then verified in parallel by the full Target Model in a single forward pass. 2. Distinction (durable) : Unlike standard autoregressive decoding (one token at a time), speculative decoding enables batch-of-tokens verification, increasing the arithmetic intensity of the target model's forward pass. 1. Significance (quantitative) : It breaks the sequential bottleneck of…

### Straggler

**Definition 8.2** (Vol 2) · [v2_ch08.md](chapters/v2_ch08.md) · Chapter 8: Fault Tolerance and Reliability (Vol 2)

- Straggler is a worker in a distributed training job that processes tasks significantly slower than its peers, creating a synchronization bottleneck. 1. Significance (quantitative) : In a synchronous system (BSP), cluster throughput ( 𝜂 hw ) is bounded by the speed of the Slowest Rank . Asingle 10 percent performance drop on one node can reduce the effective compute capacity of thousands of nodes by 10 percent. 2. Distinction (durable) : Unlike a Hardware Failure (where the node stops), a…

### Sustainable AI

**Definition 16.1** (Vol 2) · [v2_ch16.md](chapters/v2_ch16.md) · Chapter 16: Sustainable AI

Sustainable AI is the systems engineering practice of measuring and optimizing the full environmental cost of ML systems (energy, water, and embodied carbon across training, inference, and hardware manufacturing) and incorporating those costs as explicit constraints in architecture decisions alongside performance and accuracy objectives (Lannelongue et al. 2021). 1. Significance (quantitative) : Training GPT-3 consumed approximately 1,287 MWh of energy (Li 2020), equivalent to roughly 122 U.S.…

## T

### Technical debt in ML

**Definition 14.2** (Vol 1) · [ch14.md](chapters/ch14.md) · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Technical Debt in Machine Learning is the high interest rate paid on System Complexity and Implicit Dependencies . 1. Significance (quantitative) : It arises because ML systems have all the maintenance problems of traditional code plus new ML-specific drivers: Entanglement (changing one feature affects everything), Correction Cascades, and Undeclared Consumers . 2. Distinction (durable) : Unlike software technical debt (which manifests as lower productivity), ML technical debt manifests as…

### Tensor core

**Definition 2.3** (Vol 2) · [v2_ch02.md](chapters/v2_ch02.md) · Chapter 2: Compute Infrastructure

Tensor Core is a specialized mixed-precision hardware unit that performs a fused matrixmultiply-accumulate (MMA) operation 𝐷=𝐴×𝐵+𝐶 on small tiles (for example, 16×8×16 in BF16) within a single clock cycle, delivering dramatically higher throughput than generalpurpose CUDA cores by trading programmability for fixed-function matrix arithmetic. 1. Significance (quantitative) : Tensor Cores provide the bulk of the H100's 312 TFLOPS BF16 peak-roughly 8 × the ~40 TFLOPS delivered by CUDA (vector)…

### Tensor parallelism

**Definition 6.6** (Vol 2) · [v2_ch06.md](chapters/v2_ch06.md) · Chapter 6: Distributed Training Systems

Tensor Parallelism is a model parallelism technique that partitions individual tensor operations-primarily matrix multiplications-across multiple devices using column-parallel or row-parallel weight splits, typically requiring two AllReduce operations per transformer layer in Megatron-style transformer blocks to sum partial results from all participating devices. 1. Significance (quantitative) : Megatron-LM style tensor parallelism places two AllReduce operations per transformer block-one after…

### The Consistency Imperative

**Definition 4.2** (Vol 1) · [ch04.md](chapters/ch04.md) · Chapter 4: Data Engineering & Pipeline Architecture

The Consistency Imperative is the axiom that Transformation Logic must be immutable across training and serving environments. 1. **Significance (Quantitative)**: It predicts that performance degradation is proportional to the Kullback-Leibler (KL) Divergence: \[ \mathcal{D}_{\text{KL}}(T \parallel T') \] between the training transformation (\(T\)) and the serving transformation (\(T'\)). 2. **Distinction (Durable)**: Unlike Data Quality, which focuses on the cleanliness of a single record, the…

### The consistency imperative

**Definition 4.2** (Vol 1) · [ch04.md](chapters/ch04.md) · Chapter 4: Data Engineering & Pipeline Architecture

The Consistency Imperative is the axiom that Transformation Logic must be immutable across training and serving environments. 2. Distinction (durable) : Unlike Data Quality, which focuses on the Cleanliness of a single record, the consistency imperative focuses on the Alignment of the entire transformation pipeline. 1. Significance (quantitative) : It predicts that performance degradation is proportional to the KL Divergence (𝒟 KL (𝑇 ∥ 𝑇 ′ )) between the training transformation (𝑇) and the…

### The constraint propagation principle

**Definition 3.3** (Vol 1) · [ch03.md](chapters/ch03.md) · Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)

1. Significance (quantitative) : It dictates that system design must proceed end-to-end. Within the iron law, a constraint on 𝑅 peak at deployment (Stage 5) propagates backward to redefine the Stage 1 requirements and the downstream data volume (𝐷 vol ) and algorithm complexity (𝑂) that those requirements permit. The Constraint Propagation Principle states that constraints discovered late in the lifecycle ( 𝑁 ) incur an exponential cost relative to catching them during Stage 1 problem…

### The data locality invariant

**Definition 2.4** (Vol 1) · [ch02.md](chapters/ch02.md) · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

1. Significance (quantitative) : It defines the Locality Crossover, the point where adding cloud compute (increasing 𝑅 peak ) yields zero benefit because the 'Pipe' ( BWnet ) is too narrow for the 'Volume' (𝐷 vol ) . The Data Locality Invariant states that a workload necessitates local processing whenever the transmission delay (𝐷 vol / BWnet ) dominates the remote response time: Data Locality ⟺ 𝐷 vol BWnet >𝐿 net + 𝑂 𝑅 peak, remote 2. Distinction (durable) : Unlike The iron law, which…

### The D·A·M taxonomy

**Definition 1.2** (Vol 1) · [ch01.md](chapters/ch01.md) · Chapter 1: Introduction to ML Systems

1. Significance (quantitative) : The diagnostic power is concrete. A ResNet-50 inference run at batch size one is memory-bandwidth-bound (Machine axis): the A100's 2 terabytes per second bandwidth moves 25 megabytes of weights per forward pass in 12.5 μs, while the 4 GFLOP compute finishes in 2 μs. This 6 × gap means hardware upgrades to 𝑅 peak yield no improvement until the bandwidth bottleneck is resolved first. The D·A·M Taxonomy is a diagnostic framework that classifies any machine learning…

### The iron law

**Definition 2.1** (Vol 1) · [ch02.md](chapters/ch02.md) · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

\[ T_{\text{bottleneck}} = \max\left( \frac{D_{\text{vol}}}{\text{BW}}, \frac{O}{R_{\text{peak}} \cdot \eta_{\text{hw}}}, T_{\text{network}} \right) + L_{\text{lat}} \] 1. Significance (quantitative) : It defines the Physical Ceiling for any system by quantifying the relationship between data volume (𝐷 vol ) , compute capacity (𝑅 peak ) , and communication overhead (𝐿 lat ) . The iron law is the fundamental physical constraint governing all machine learning performance, expressed as the total…

### The Iron Law of Training Performance

**Definition 8.2** (Vol 1) · [ch08.md](chapters/ch08.md) · Chapter 8: Staged Model Training & Parallelism

The **Iron Law of Training Performance** models the wall-clock execution time of an iterative optimization run by assuming that data transfer and communication latency are fully overlapped with computation: \[ T_{\text{train}} \approx \frac{O}{R_{\text{peak}} \cdot \eta_{\text{hw}}} \] Where: * \(T_{\text{train}}\) is the training wall-clock time (seconds). * \(O\) is the total number of floating-point operations (FLOPs) required. * \(R_{\text{peak}}\) is the peak theoretical hardware…

### The iron law of training performance

**Definition 8.2** (Vol 1) · [ch08.md](chapters/ch08.md) · Chapter 8: Staged Model Training & Parallelism

The Iron Law of Training Performance is the simplified form of the general iron law that isolates the computational bottleneck of iterative optimization: The simplification is valid when the pipeline is correctly staged: at training scale with large batches, data movement (𝐷 vol / BW ) is overlapped with compute via prefetching pipelines, and communication overhead (𝐿 lat ) is absorbed by gradient overlap strategies, leaving hardware utilization as the dominant remaining lever. When pipelines…

### Thermal design power (TDP)

**Definition 2.6** (Vol 2) · [v2_ch02.md](chapters/v2_ch02.md) · Chapter 2: Compute Infrastructure

Thermal Design Power (TDP) is the maximum sustained thermal load in watts that a chip's cooling system must continuously remove for the processor to operate at its rated clock frequencydefining both the cooling infrastructure requirement and the performance ceiling for the accelerator. 1. Significance (quantitative) : The H100 SXM5 operates at 700 W TDP. When a liquid cooling system can only sustain 500 W of heat removal (inadequate cooling), the GPU firmware reduces clock frequency via thermal…

### Training Systems

**Definition 8.1** (Vol 1) · [ch08.md](chapters/ch08.md) · Chapter 8: Staged Model Training & Parallelism

**Machine Learning Training Systems** are software-hardware systems that execute the iterative optimization loop—forward pass, loss computation, backward pass, and parameter update—to minimize a loss function over a training dataset. * **Quantitative Significance:** The memory cost of training is typically \(6 \times\) the inference memory footprint per parameter when using the Adaptive Moment Estimation (Adam) optimizer. For a \(7\text{B}\) parameter model:…

### Training systems

**Definition 8.1** (Vol 1) · [ch08.md](chapters/ch08.md) · Chapter 8: Staged Model Training & Parallelism

Machine Learning Training Systems are software-hardware systems that execute the iterative optimization loop-forward pass, loss computation, backward pass, and parameter update-to minimize a loss function over a training dataset. 1. Significance (quantitative) : Training memory cost is 6 × the inference memory cost per parameter when using the Adaptive Moment Estimation (Adam) optimizer: a 7Bparameter model requires 14 GB (FP16 weights) + 14 GB (FP16 gradients) + 56 GB (Adam first and second…

### Training-serving skew

**Definition 13.3** (Vol 1) · [ch13.md](chapters/ch13.md) · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Training-Serving Skew is the distributional divergence between the training and inference environments caused by inconsistent logic or state. 3. Common pitfall: Afrequent misconception is that skew is 'found' by looking for errors. In reality, it is invisible to exceptions: the system runs perfectly and the latency is low, but the predictions are statistically wrong. 1. Significance (quantitative) : It violates the consistency imperative, causing silent accuracy degradation proportional to the…

### Transformer

**Definition 6.6** (Vol 1) · [ch06.md](chapters/ch06.md) · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

A **Transformer** is an architectural paradigm for parallel sequence processing that replaces recurrence entirely with global self-attention and point-wise fully connected networks, decoupling sequence length from computational depth during training. * **Autoregressive Generation:** Generation is performed token-by-token. For each new token, the model evaluates a single forward pass, resulting in a low-intensity, memory-bandwidth-bound execution profile. * **KV Cache:** To prevent redundant…

### Transformers

**Definition 6.6** (Vol 1) · [ch06.md](chapters/ch06.md) · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Transformers are the architectural paradigm of Parallel Sequence Processing that eliminates recurrence in favor of global self-attention. 1. Significance (quantitative) : They decouple Sequence Length from Compute Depth, enabling massive parallelization (maximizing 𝜂 hw ) at the cost of Quadratic Attention Memory ( 𝑂(𝑁 2 ) ). 2. Distinction (durable) : Unlike RNNs, which have a Sequential Bottleneck ( 𝑂(𝑁) depth), transformers provide direct, 𝑂(1) depth connections between all sequence…

## W

### Warehouse-scale computer (WSC)

**Definition 2.11** (Vol 2) · [v2_ch02.md](chapters/v2_ch02.md) · Chapter 2: Compute Infrastructure

Warehouse-Scale Computer (WSC) is a building-scale computing system in which thousands of servers are operated as a single coherent machine-with the network fabric serving as the system bus, distributed storage as the disk subsystem, and a cluster orchestrator as the operating system-enabling training workloads that would be physically impossible on any single machine. 1. Significance (quantitative) : AWSCof 10,000 H100 GPUs delivers approximately 3.12 ExaFLOP/s BF16 peak-enabling frontier…

## Α

### α-β model (Hockney Model)

**Definition 4.3** (Vol 2) · [v2_ch04.md](chapters/v2_ch04.md) · Chapter 4: Network Fabrics

1. Significance (quantitative) : Topology choice directly shifts 𝛼 and 𝛽 . An InfiniBand HDR link has 𝛼 ≈ 1𝜇 s and 𝛽 ≈ 25 GB/s, yielding 𝑛 ∗ ≈25 KB: messages smaller than 25 KB are latency-bound and benefit from topology designs that minimize hop count; messages larger than 25 KB are bandwidth-bound and benefit from fat-tree bisection bandwidth. In a ring topology, the worst-case path traverses ⌊𝑁/2⌋ hops, so effective startup latency scales as 𝛼 ring ≈⌊𝑁/2⌋⋅𝛼 hop: for a 64-node ring, 𝛼 ring…
