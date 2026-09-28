# Patterns & Principles — Machine Learning Systems

> Generated catalog of 702 indexed artifacts across 44 chapters. Do not edit by hand: run `python scripts/build_indexes.py`.

Each entry is a short excerpt. Use `get_artifact` or open the source chapter for the full text.

## Definitions

*132 entries, in reading order*

### Definition 1.1: Machine learning systems

[ch01.md](chapters/ch01.md) · Vol 1 · Chapter 1: Introduction to ML Systems

Machine Learning Systems are software systems whose core behavior is determined by parameters learned from data rather than explicitly programmed rules, making performance a function of data quality,…

### Definition 1.2: The D·A·M taxonomy

[ch01.md](chapters/ch01.md) · Vol 1 · Chapter 1: Introduction to ML Systems

1. Significance (quantitative) : The diagnostic power is concrete. A ResNet-50 inference run at batch size one is memory-bandwidth-bound (Machine axis): the A100's 2 terabytes per second bandwidth…

### Definition 1.3: AI Engineering

[ch01.md](chapters/ch01.md) · Vol 1 · Chapter 1: Introduction to ML Systems

AI Engineering is the engineering discipline of designing, deploying, and maintaining systems whose outputs are inherently probabilistic (stochastic) to meet deterministic reliability targets by…

### Definition: Hybrid ML

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Hybrid ML is the architectural strategy of hierarchically distributing machine learning tasks across cloud, edge, mobile, and tiny devices. It optimizes the latency-compute Pareto frontier by…

### Definition 2.1: The iron law

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

\[ T_{\text{bottleneck}} = \max\left( \frac{D_{\text{vol}}}{\text{BW}}, \frac{O}{R_{\text{peak}} \cdot \eta_{\text{hw}}}, T_{\text{network}} \right) + L_{\text{lat}} \] 1. Significance (quantitative)…

### Definition 2.2: Cloud ML

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

- Cloud Machine Learning is the deployment paradigm that optimizes for Resource Elasticity by decoupling computational capacity from physical location. 1. Significance (quantitative) : It enables…

### Definition 2.3: Edge ML

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

- Edge Machine Learning is the deployment paradigm optimized for Latency Determinism and Data Locality by locating computation physically adjacent to data sources. 1. Significance (quantitative) : It…

### Definition 2.4: The data locality invariant

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

1. Significance (quantitative) : It defines the Locality Crossover, the point where adding cloud compute (increasing 𝑅 peak ) yields zero benefit because the 'Pipe' ( BWnet ) is too narrow for the…

### Definition 2.5: Mobile ML

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Mobile Machine Learning is the deployment paradigm bounded by Thermal Design Power (TDP) and battery energy. 1. Significance (quantitative) : It is constrained by the heat dissipation capacity of…

### Definition 2.7: Hybrid ML

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Hybrid Machine Learning is the architectural strategy of Hierarchical Distribution across cloud and edge resources. 3. Common pitfall: A frequent misconception is that Hybrid ML is just 'running two…

### Definition 3.1: Machine learning lifecycle

[ch03.md](chapters/ch03.md) · Vol 1 · Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)

Machine Learning Lifecycle is the continuous engineering discipline of managing System Entropy across the Data, Algorithm, and Machine axes. 1. Significance (quantitative) : It transforms the linear…

### Definition 3.2: Model validation

[ch03.md](chapters/ch03.md) · Vol 1 · Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)

Model Validation is the rigorous verification that a model meets business constraints-service level agreement (SLA), fairness, and cost-on production-representative data. 1. Significance…

### Definition 3.3: The constraint propagation principle

[ch03.md](chapters/ch03.md) · Vol 1 · Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)

1. Significance (quantitative) : It dictates that system design must proceed end-to-end. Within the iron law, a constraint on 𝑅 peak at deployment (Stage 5) propagates backward to redefine the Stage…

### Definition 4.1: Data Engineering

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Data Engineering is the infrastructure layer that manages the lifecycle of data from source to model, encompassing acquisition, transformation, storage, and governance. 1. **Significance…

### Definition 4.2: The Consistency Imperative

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

The Consistency Imperative is the axiom that Transformation Logic must be immutable across training and serving environments. 1. **Significance (Quantitative)**: It predicts that performance…

### Definition 4.3: Feature Store

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

A Feature Store is the architectural layer that centralizes the management of machine learning features, decoupling feature computation from consumption. 1. **Significance (Quantitative)**: It…

### Definition 4.4: Data Debt

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Data Debt is the compound interest of implicit coupling and missing documentation across the data stack. 1. **Significance (Quantitative)**: It manifests as silent degradation, where the cost of…

### Definition 4.1: Data engineering

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Data Engineering is the infrastructure layer that manages the lifecycle of data from source to model, encompassing acquisition, transformation, storage, and governance. 1. Significance (quantitative)…

### Definition 4.2: The consistency imperative

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

The Consistency Imperative is the axiom that Transformation Logic must be immutable across training and serving environments. 2. Distinction (durable) : Unlike Data Quality, which focuses on the…

### Definition 4.3: Feature store

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Feature Store is the architectural layer that centralizes the management of machine learning features, decoupling feature computation from consumption. 2. Distinction (durable) : Unlike a…

### Definition 4.4: Data debt

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Data Debt is the compound interest of implicit coupling and missing documentation across the data stack. 1. Significance (quantitative) : It manifests as silent degradation, where the cost of…

### Definition 5.1: Deep Learning

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

**Deep Learning** is the computational paradigm of Hierarchical Feature Learning from raw data. 1. **Quantitative Significance**: By stacking nonlinear transformations, it replaces manual Feature…

### Definition 5.1: Deep learning

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

Deep Learning is the computational paradigm of Hierarchical Feature Learning from raw data. 1. Significance (quantitative) : By stacking nonlinear transformations, it replaces manual Feature…

### Definition 5.2: Backpropagation

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

Backpropagation is the efficient application of the Chain Rule to a computational graph to solve the Credit Assignment Problem . 1. Significance (quantitative) : It propagates error signals from…

### Definition 5.3: Gradient descent

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

Gradient Descent is the iterative algorithm that navigates the Loss Landscape by updating parameters in the direction of the negative gradient. 3. Common pitfall: Afrequent misconception is that…

### Definition 5.4: Overfitting

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

Overfitting is the failure of Generalization caused by memorizing Noise instead of Signal . 2. Distinction (durable) : Unlike Underfitting (where the model is too simple), Overfitting is a Symmetry…

### Definition 6.1: Inductive Bias

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

An **inductive bias** is a structural constraint built into a model architecture that restricts the hypothesis space, enabling generalization from finite data by encoding domain-specific assumptions…

### Definition 6.2: Multilayer Perceptron (MLP)

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

An **MLP** is a feed-forward neural network architecture that applies fully connected layers in sequence, where every neuron in layer \(l-1\) connects to every neuron in layer \(l\), encoding no…

### Definition 6.3: Convolutional Neural Network (CNN)

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

A **CNN** is a neural network architecture defined by translation equivariance and spatial locality, restricting receptive fields to local spatial neighborhoods and sharing weights across all grid…

### Definition 6.4: Recurrent Neural Network (RNN)

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

An **RNN** is a sequence-processing architecture that updates a hidden state vector \(h_t\) at each time step \(t\) according to \(h_t = f(h_{t-1}, x_t)\), propagating temporal context with constant…

### Definition 6.5: Attention Mechanism

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

An **attention mechanism** is a sequence-processing operation that computes a weighted sum of value vectors, where the weights are dynamically calculated via similarity scores between a query vector…

### Definition 6.6: Transformer

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

A **Transformer** is an architectural paradigm for parallel sequence processing that replaces recurrence entirely with global self-attention and point-wise fully connected networks, decoupling…

### Definition 6.1: Inductive bias

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Inductive Bias is a structural constraint built into a model architecture that restricts the hypothesis space, enabling generalization from finite data by encoding domain-specific assumptions (such…

### Definition 6.2: Multilayer perceptrons

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Multilayer Perceptrons are feed-forward neural network architectures that apply fully connected layers in sequence, where every neuron in one layer connects to every neuron in the next, encoding no…

### Definition 6.3: Convolutional neural networks

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Convolutional Neural Networks (CNNs) are architectures defined by Translation Equivariance and Spatial Locality . 2. Distinction (durable) : Unlike MLPs, which have Global Connectivity, CNNs restrict…

### Definition 6.4: Recurrent neural networks

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

1. Significance (quantitative) : The fixed-size state provides 𝑂(1) inference memory regardless of sequence length-processing a 10,000-token sequence requires the same memory as a 10-token…

### Definition 6.5: Attention mechanisms

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Attention Mechanisms are neural network operations that compute a weighted sum of value vectors, where the weights are derived from learned similarity scores between a query vector and a set of key…

### Definition 6.6: Transformers

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Transformers are the architectural paradigm of Parallel Sequence Processing that eliminates recurrence in favor of global self-attention. 1. Significance (quantitative) : They decouple Sequence…

### Definition 7.1: Machine learning frameworks

[ch07.md](chapters/ch07.md) · Vol 1 · Chapter 7: ML Frameworks (TF, PyTorch, JAX)

Machine Learning Frameworks are software systems that translate high-level mathematical model definitions into hardware-optimized execution plans by managing the computational graph, automatic…

### Definition 8.1: Training Systems

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

**Machine Learning Training Systems** are software-hardware systems that execute the iterative optimization loop—forward pass, loss computation, backward pass, and parameter update—to minimize a loss…

### Definition 8.2: The Iron Law of Training Performance

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

The **Iron Law of Training Performance** models the wall-clock execution time of an iterative optimization run by assuming that data transfer and communication latency are fully overlapped with…

### Definition 8.4: Model FLOPs Utilization (MFU)

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

**Model FLOPs Utilization (MFU)** is the hardware-agnostic efficiency metric defined as the ratio of useful model computations performed per step to the peak theoretical hardware capability: \[…

### Definition 8.1: Training systems

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Machine Learning Training Systems are software-hardware systems that execute the iterative optimization loop-forward pass, loss computation, backward pass, and parameter update-to minimize a loss…

### Definition 8.2: The iron law of training performance

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

The Iron Law of Training Performance is the simplified form of the general iron law that isolates the computational bottleneck of iterative optimization: The simplification is valid when the pipeline…

### Definition 8.3: Batch processing

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

1. Significance (quantitative) : Throughput increases with batch size up to the critical batch size, beyond which additional examples provide diminishing gradient quality without proportional…

### Definition 9.1: Data selection

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

Data Selection is the process of maximizing the Information-Compute Ratio of a training dataset. 2. Distinction (durable) : Unlike data engineering, which focuses on the cleanliness and consistency…

### Definition 10.1: Model compression

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

Model Compression is a family of techniques that reduce a trained model's computational cost and memory footprint by eliminating redundant parameters (pruning), reducing numerical precision…

### Definition 10.2: Pruning

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

Pruning is the sparsification of the Parameter Space by removing weights that contribute minimal information to the loss landscape. 2. Distinction (durable) : Unlike Quantization, which reduces the…

### Definition 10.3: Quantization

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

- Quantization is the reduction of Information Fidelity by mapping high-precision continuous values to a lower-precision discrete set. 1. Significance (quantitative) : It reduces the Memory Bandwidth…

### Definition 11.1: Hardware Acceleration

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

**Hardware Acceleration** is the practice of replacing general-purpose processor logic with domain-specific silicon optimized for a narrow class of operations, trading programmability for compute…

### Definition 11.2: Hardware-Software Co-Design

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

**Hardware-Software Co-design** is a development methodology that intentionally violates traditional hardware-software abstraction layers, allowing algorithmic constraints to inform silicon design…

### Definition 11.3: Machine Learning Accelerator

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

An **ML Accelerator** is a domain-specific processor whose silicon is designed primarily for the dense matrix operations and regular data flow of neural networks, achieving high peak throughput…

### Definition 11.4: AI Memory Wall

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

The **AI Memory Wall** is the performance constraint that arises when arithmetic throughput (\(R_{\text{peak}}\)) outpaces memory bandwidth (\(\text{BW}\)). It dictates that system performance is…

### Definition 11.5: Arithmetic Intensity

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

**Arithmetic Intensity (AI)** is the ratio of floating-point operations to bytes of memory traffic for a given computation (FLOP/byte), determining whether the workload is limited by compute…

### Definition 11.6: Mapping in AI Acceleration

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

**Mapping in AI Acceleration** is the process of binding the Logical Computation Graph to the Physical Hardware Topology by deciding which operations execute on which processing elements, which data…

### Definition 11.1: Hardware acceleration

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Hardware Acceleration is the practice of replacing general-purpose processor logic with domain-specific silicon optimized for a narrow class of operations, trading programmability for the compute…

### Definition 11.2: Hardware-software co-design

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Hardware-Software Co-design is a development methodology that intentionally violates traditional hardware-software abstraction layers, allowing algorithm constraints to inform silicon design and…

### Definition 11.3: MLaccelerator

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Machine Learning Accelerators are domain-specific processors whose silicon is designed primarily for the dense matrix operations and regular data flow of neural networks, achieving high 𝑅 peak and…

### Definition 11.4: AI memory wall

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

2. Distinction (durable) : Unlike a general-purpose memory wall, which affects all computing, the AI memory wall is driven by the massive model state and activation storage required by deep learning.…

### Definition 11.5: Arithmetic intensity

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

1. Significance (quantitative) : The intensity threshold separating memory-bound from compute-bound regimes is the roofline ridge point: 𝑅 peak / BW. For an A100 (312 TFLOPS BF16, 2 TB/s), the ridge…

### Definition 11.6: Mapping in AI acceleration

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Mapping in AI Acceleration is the process of binding the Logical Computation Graph to the Physical Hardware Topology by deciding which operations execute on which processing elements, which data…

### Definition 12.1: Machine learning benchmarking

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Machine Learning Benchmarking is the empirical measurement of a system's end-to-end performance on representative ML workloads, designed to decouple marketed peak specifications from the sustained…

### Definition 12.2: Machine learning system benchmarks

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Machine Learning System Benchmarks are standardized evaluation protocols that hold the workload and quality target constant while varying the hardware-software stack, measuring 𝜂 hw =𝑅 sustained /𝑅…

### Definition 12.3: MLtraining benchmarks

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

MLTraining Benchmarks measure the Rate of Convergence per unit of resource (time, energy, cost). 1. Significance (quantitative) : They validate the system's ability to sustain high arithmetic…

### Definition 12.5: SLO vs. SLA

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

SLOs and SLAs are performance commitment specifications: a Service Level Objective (SLO) is the internal engineering target that the team optimizes toward, while a Service Level Agreement (SLA) is…

### Definition 13.1: Model serving

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Model Serving is the operational phase that provides model predictions to end-users or downstream systems under strict latency constraints. 1 Jevons Paradox: William Stanley Jevons observed in 1865…

### Definition 13.2: Latency budget

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Latency Budget is the time capital allocated to a request, strictly bounded by the end-to-end service level objective (SLO) . 7 gRPC (gRPC Remote Procedure Call) : Evolved from Google's internal…

### Definition 13.3: Training-serving skew

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Training-Serving Skew is the distributional divergence between the training and inference environments caused by inconsistent logic or state. 3. Common pitfall: Afrequent misconception is that skew…

### Definition 13.4: Cold start

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Cold Start is the initialization latency incurred when instantiating a new model replica. 1. Significance (quantitative) : It represents the fixed cost of state hydration (loading weights, compiling…

### Definition 13.5: Dynamic batching

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Dynamic Batching is the runtime optimization of trading Latency for Throughput under stochastic arrival patterns. 2. Distinction (durable) : Unlike Static Batching, which is fixed during training,…

### Definition 13.6: LLM performance metrics

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

LLM Performance Metrics are the two-dimensional measurements of latency for streaming autoregressive generation. 25 Autoregressive: From Greek auto(self) and Latin regressus (a going back)-the output…

### Definition 14.1: MLOps

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Machine Learning Operations (MLOps) is the engineering discipline that closes the feedback loop between model behavior and data reality by automating retraining, validation, and deployment in…

### Definition 14.2: Technical debt in ML

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Technical Debt in Machine Learning is the high interest rate paid on System Complexity and Implicit Dependencies . 1. Significance (quantitative) : It arises because ML systems have all the…

### Definition 14.3: Data drift

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

1. Significance (quantitative) : It represents a violation of the i.i.d. assumption (independent and identically distributed), causing accuracy to erode monotonically with the distributional…

### Definition 15.2: Responsible AI engineering

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

Responsible AI Engineering is the engineering discipline of designing, deploying, and maintaining systems with probabilistic outputs by operationalizing societal and regulatory requirements as…

### Definition 1.1: Machine learning fleet

[v2_ch01.md](chapters/v2_ch01.md) · Vol 2 · Chapter 1: Introduction to ML Systems

Machine Learning Fleet is a distributed system of thousands of interconnected accelerators, storage arrays, and network fabrics designed to operate as a single coherent computer. 2. Distinction…

### Definition 2.1: High bandwidth memory (HBM)

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

HighBandwidthMemory(HBM) is a 3D-stacked DRAM architecture in which multiple memory dies are vertically bonded and connected to the processor through thousands of ThroughSilicon Vias (TSVs) on a…

### Definition 2.2: Ridge point

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Achievable FLOPS = min (𝑅 peak, BW ×𝐼) (2.1) Equation 2.1 has a direct physical interpretation. If the workload's arithmetic intensity is low (it needs many bytes per operation), then performance is…

### Definition 2.3: Tensor core

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Tensor Core is a specialized mixed-precision hardware unit that performs a fused matrixmultiply-accumulate (MMA) operation 𝐷=𝐴×𝐵+𝐶 on small tiles (for example, 16×8×16 in BF16) within a single clock…

### Definition 2.4: Pipeline bubble

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

- Pipeline Bubble is the idle time in pipeline-parallel training caused by stages waiting for inputs from upstream workers during the fill and drain phases of a micro-batch cycle. 1. Significance…

### Definition 2.5: Model FLOPs utilization (MFU)

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Model FLOPs Utilization (MFU) is the ratio of a model's theoretical FLOP count per training step-calculated from architecture parameters alone-to the product of hardware peak throughput and elapsed…

### Definition 2.6: Thermal design power (TDP)

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Thermal Design Power (TDP) is the maximum sustained thermal load in watts that a chip's cooling system must continuously remove for the processor to operate at its rated clock frequencydefining both…

### Definition 2.7: Node

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Node is a physical server chassis that aggregates multiple accelerators-typically 8-through a high-speed intra-node interconnect (NVLink or ICI), creating the fundamental boundary between…

### Definition 2.8: Bandwidth hierarchy

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Bandwidth Hierarchy is the physical ordering of data transfer rates across system boundaries, from on-chip SRAM (fastest) to the wide-area network (slowest). 1. Significance (quantitative) : It…

### Definition 2.9: Rack

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Rack is the physical infrastructure unit-a standardized 42U enclosure-that houses multiple compute nodes, a Top-of-Rack (ToR) switch (the first network aggregation point connecting all nodes in the…

### Definition 2.10: Power usage effectiveness (PUE)

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

1. Significance (quantitative) : It measures the Infrastructure Overhead of the data center. A PUE of 1.0 is the theoretical ideal; a PUE of 1.10 means that for every 100 watts of computation, an…

### Definition 2.11: Warehouse-scale computer (WSC)

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Warehouse-Scale Computer (WSC) is a building-scale computing system in which thousands of servers are operated as a single coherent machine-with the network fabric serving as the system bus,…

### Definition 2.13: Hierarchy-aware parallelism

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Hierarchy-Aware Parallelism is the strategy of mapping different parallel execution modes to the physical bandwidth tiers of the cluster. 1. Significance (quantitative) : It ensures that…

### Definition 4.1: PAM4 signaling

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

PAM4 Signaling is an electrical modulation scheme that uses four distinct voltage levels to encode two bits per symbol period, doubling the data rate achievable over a given physical medium without…

### Definition 4.2: Remote direct memory access (RDMA)

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Remote Direct Memory Access (RDMA) is a networking technology that allows one machine to read or write the memory of another machine directly, bypassing the operating system kernel and CPU of both…

### Definition 4.3: α-β model (Hockney Model)

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

1. Significance (quantitative) : Topology choice directly shifts 𝛼 and 𝛽 . An InfiniBand HDR link has 𝛼 ≈ 1𝜇 s and 𝛽 ≈ 25 GB/s, yielding 𝑛 ∗ ≈25 KB: messages smaller than 25 KB are latency-bound and…

### Definition 4.4: Bisection bandwidth

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Bisection Bandwidth is a network topology metric defined as the minimum aggregate link capacity crossing any partition that divides the cluster into two equal halves, representing the worst-case…

### Definition 4.5: Non-blocking fabric

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Non-blocking Fabric is a network topology in which any permutation of input-output port pairs can communicate simultaneously at full line rate without internal contention, achieved by ensuring that…

### Definition 4.6: Fat-tree

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Fat-Tree is a hierarchical network topology in which the number of parallel paths-and therefore aggregate cross-sectional capacity-increases at each switch tier toward the spine, providing full…

### Definition 4.7: Bulk synchronous parallel (BSP)

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Bulk Synchronous Parallel (BSP) is a parallel execution model in which every worker completes a local computation phase, exchanges data with all other workers, and then waits at a global barrier…

### Definition 4.8: Priority flow control

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Priority Flow Control (PFC) is a link-layer mechanism that prevents switch buffer overflow by sending PAUSE frames to an upstream sender when a port's queue depth crosses a configured threshold,…

### Definition 4.9: Incast

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Incast is a many-to-one traffic pattern in which a large number of senders simultaneously transmit data to a single receiver port, concentrating line-rate traffic from multiple sources into a single…

### Definition 5.1: Parallel file system

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

Parallel File System (PFS) is a distributed storage architecture that stripes data across many storage servers to provide aggregate throughput exceeding the capacity of any single device. 1.…

### Definition 5.2: Small file problem

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

- Small File Problem is a pathological I/O pattern where millions of individually small files overwhelm the metadata server of a storage system. 1. Significance (quantitative) : It reduces effective…

### Definition 5.4: GPU Direct Storage

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

GPU Direct Storage (GDS) is a technology that enables a direct DMA path between NVMe storage devices and GPU memory, bypassing the host CPU and system DRAM. 2. Distinction (durable) : Unlike…

### Definition 5.5: Checkpoint storm

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

- Checkpoint Storm is a burst of synchronized network and storage traffic that occurs when all nodes in a training fleet save model state simultaneously. 1. Significance (quantitative) : The storm…

### Definition 6.1: Distributed training

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Distributed Training is a training methodology that partitions the optimization loop across multiple compute nodes-distributing either data, model layers, or individual tensor operationsand…

### Definition 6.2: Data parallelism

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Data Parallelism is a distributed training strategy in which each worker holds a complete replica of the model and processes an independent shard of the minibatch, then synchronizes gradient updates…

### Definition 6.5: Pipeline parallelism

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Pipeline Parallelism is a model parallelism technique that partitions a neural network's layers into sequential stages assigned to different devices, passing activations forward and gradients…

### Definition 6.6: Tensor parallelism

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Tensor Parallelism is a model parallelism technique that partitions individual tensor operations-primarily matrix multiplications-across multiple devices using column-parallel or row-parallel weight…

### Definition 7.1: Gradient synchronization

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

Gradient Synchronization is the collective communication protocol executed at each training step in which every worker transmits its locally computed gradient tensor to all other workers, receives…

### Definition 7.3: Collective operation

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

Collective Operation is a distributed communication pattern in which all processes in a group participate simultaneously to aggregate, broadcast, or redistribute data-with the correctness guarantee…

### Definition 8.1: Checkpointing

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

Checkpointing is the periodic serialization of the complete training state (parameters, optimizer state, and data loader position) to persistent storage. 1. Significance (quantitative) : It minimizes…

### Definition 8.2: Straggler

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

- Straggler is a worker in a distributed training job that processes tasks significantly slower than its peers, creating a synchronization bottleneck. 1. Significance (quantitative) : In a…

### Definition 8.3: Graceful degradation

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

Graceful Degradation is a fault tolerance strategy in which a system responds to resource exhaustion or component failure by deliberately reducing service quality-falling back to a smaller model,…

### Definition 9.1: Priority inversion

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Priority Inversion is a scheduling pathology in which a high-priority task is forced to wait for a lower-priority task to release a shared resource. 1. Significance (quantitative) : It reduces the…

### Definition 9.2: Elastic training

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

- Elastic Training is the capability of a distributed training job to dynamically adjust its worker count during execution without requiring a full restart. 1. Significance (quantitative) : It…

### Definition 10.2: Block-wise quantization

[v2_ch10.md](chapters/v2_ch10.md) · Vol 2 · Chapter 10: Performance Engineering (Vol 2)

1. Significance (quantitative) : With block size 𝐵 block =64 and 𝑏 = 4 bits, weights compress from 16 bits to 4 bits-a 4 × memory reduction-while each FP16 scale adds 16/64 = 0.25 bits per weight.…

### Definition 10.3: Model FLOPs utilization (MFU)

[v2_ch10.md](chapters/v2_ch10.md) · Vol 2 · Chapter 10: Performance Engineering (Vol 2)

1. Significance (quantitative) : At fleet scale, MFU aggregates across all nodes: communication overhead, load imbalance, and pipeline bubbles each compound the utilization loss, so fleet MFU is…

### Definition 11.1: Continuous batching

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

- Continuous Batching is a serving strategy that decouples batch membership from iteration boundaries, allowing new requests to enter and completed ones to exit at every decode step. 1. Significance…

### Definition 11.2: KV cache

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

- KV Cache is a memory buffer that stores previously computed Key and Value attention vectors to avoid redundant computation during autoregressive generation. 1. Significance (quantitative) : It…

### Definition 11.4: Speculative decoding

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Speculative Decoding is a latency optimization that uses a smaller Draft Model to predict multiple future tokens, which are then verified in parallel by the full Target Model in a single forward…

### Definition 11.5: Prefill and decode phases

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Prefill and Decode Phases are the two distinct computational regimes of transformer-based LLM inference. 2. Distinction (durable) : Unlike Single-Pass Inference (for example, ImageNet), where the…

### Definition 12.1: On-device learning

[v2_ch12.md](chapters/v2_ch12.md) · Vol 2 · Chapter 12: Edge Intelligence (Vol 2)

On-Device Learning is the local training or adaptation of machine learning models directly on deployed hardware without requiring server connectivity. 1. Significance (quantitative) : It enables…

### Definition 12.2: Federated learning

[v2_ch12.md](chapters/v2_ch12.md) · Vol 2 · Chapter 12: Edge Intelligence (Vol 2)

Federated Learning is a decentralized training paradigm where distributed devices collaboratively train a shared model using local data while exchanging only model updates (gradients or weights). 1.…

### Definition 13.1: FinOps for ML

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

FinOps for ML is the practice of treating compute cost as a first-class engineering constraintmeasured in real-time per experiment and model, and optimized jointly with model accuracy and…

### Definition 13.2: MLsystems TCO

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Total Cost of Ownership (TCO) for ML Systems is the complete economic accounting of developing, deploying, and operating machine learning capabilities across their full lifecycle. 1. Significance…

### Definition 14.1: Security

[v2_ch14.md](chapters/v2_ch14.md) · Vol 2 · Chapter 14: Security & Privacy (Vol 2)

Security is the set of system properties (confidentiality, integrity, and availability) that protect an ML system's data, model weights, and inference pipeline from intentional adversarial actions,…

### Definition 14.2: Privacy

[v2_ch14.md](chapters/v2_ch14.md) · Vol 2 · Chapter 14: Security & Privacy (Vol 2)

Privacy is the protection of sensitive information from unauthorized disclosure, inference, and misuse across the ML lifecycle. 1. Significance (quantitative) : It limits the exposure risk of…

### Definition 15.1: Robust AI

[v2_ch15.md](chapters/v2_ch15.md) · Vol 2 · Chapter 15: Robust AI

Robust AI is the measurable systems property that a model's predictions remain valid-within specified error bounds-under distribution shift, adversarial perturbation, and hardware or software faults,…

### Definition 15.2: Concept drift

[v2_ch15.md](chapters/v2_ch15.md) · Vol 2 · Chapter 15: Robust AI

Concept Drift is the subtype of distribution shift (see Section 15.4.1) in which the statistical relationship 𝑃(𝑌 |𝑋) changes over time, meaning the decision boundary itself becomes incorrect rather…

### Definition 15.3: Adversarial attack

[v2_ch15.md](chapters/v2_ch15.md) · Vol 2 · Chapter 15: Robust AI

Adversarial Attack is a deliberate, mathematically crafted perturbation to model inputs designed to cause misclassification while remaining imperceptible to humans. 1. Significance (quantitative) :…

### Definition 15.4: Data poisoning

[v2_ch15.md](chapters/v2_ch15.md) · Vol 2 · Chapter 15: Robust AI

Data Poisoning is the corruption of training data to compromise model behavior at inference time, either by injecting malicious samples or modifying existing labels. 1. Significance (quantitative) :…

### Definition 16.1: Sustainable AI

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

Sustainable AI is the systems engineering practice of measuring and optimizing the full environmental cost of ML systems (energy, water, and embodied carbon across training, inference, and hardware…

### Definition 17.1: Responsible AI

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

Responsible AI is the practice of designing, auditing, and operating ML systems to measurable fairness, safety, privacy, and accountability standards-translating ethical principles into verifiable…

### Definition 17.2: Algorithmic fairness

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

Algorithmic Fairness is the measurable property that a model's error distribution or outcomes are invariant (or bounded in variation) across protected demographic groups. 1. Significance…

### Definition 17.3: Demographic parity

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

1. Significance (quantitative) : It is the simplest and most restrictive fairness metric. It requires the model to produce Equal Outcomes across groups, regardless of the underlying base-rate…

## Napkin Math (Worked Examples)

*186 entries, in reading order*

### Napkin Math 18.2: Worked example: KL divergence for drift detection

[appB.md](chapters/appB.md) · Vol 1 · Appendix B: Data Foundations

\[ \text{KL Divergence} = \sum_{i=1}^{3} P_i \log \frac{P_i}{Q_i} \] Scenario: Asentiment classifier was trained on data where 60 percent of reviews were positive, 30 percent negative, and 10 percent…

### Napkin Math 18.3: Worked example: Log-sum-exp in action

[appB.md](chapters/appB.md) · Vol 1 · Appendix B: Data Foundations

(-1) ≈ 0.368 The setup: Athree-class classifier outputs logits . Without the trick (naive softmax) : exp (100) ≈ 2.7 ×10 43, exp (101) ≈ 7.3×10 43, exp (102) ≈ 2.0×10 44 These numbers are…

### Napkin Math 20.1: The training time equation

[appD.md](chapters/appD.md) · Vol 1 · Appendix D: Machine Foundations

\[2\left(PD\right)\cdot \left(4PD\right) \] Just as classical architecture has an 'iron law' of performance, Large Language Model training has a fundamental governing equation. To estimate training…

### Napkin Math 21.1: Napkin math with these constants

[appE.md](chapters/appE.md) · Vol 1 · Appendix E: System Assumptions & Quantitative Constants

Theconstants in this appendix are not just for auditing-they are designed for quick calculations. Three examples illustrate the pattern. How much memory does training a 7B model require?…

### Napkin Math: Training GPT-3-scale Model

[ch01.md](chapters/ch01.md) · Vol 1 · Chapter 1: Introduction to ML Systems

* **Task:** Estimate training time for a model requiring \(O \approx 3.14 \times 10^{23}\) FLOPs on \(N = 1024\) GPUs. * **Hardware:** NVIDIA A100 (FP16 Tensor Core peak \(R_{\text{peak}} = 312\)…

### Napkin Math 1.1: Training GPT-3

[ch01.md](chapters/ch01.md) · Vol 1 · Chapter 1: Introduction to ML Systems

- Problem: What is the training time for a GPT-3 class model on a cluster of A100 GPUs? Variables: · Ops (𝑂) : ≈3.14×10 23 FLOPs (from paper). · Peak (𝑅 peak ) : 312 TFLOPS (A100 FP16 tensor core…

### Napkin Math 2.1: The Energy of Transmission

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

**Problem**: Determine whether a remote battery-powered sensor should transmit raw audio data to the cloud or process it locally. **Variables**: * Transmission energy (\(E_{\text{tx}}\)): \(100…

### Napkin Math 2.2: ResNet-50 Inference on Cloud vs. Mobile NPU

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

**Problem**: Compare whether batch-1 inference for ResNet-50 (4.1 GFLOPs, FP16 size = 51.2 MB, INT8 size = 25.6 MB) is compute or memory-bound on (a) a cloud GPU (NVIDIA A100) and (b) a mobile NPU.…

### Napkin Math 2.3: Autonomous Vehicle Emergency Braking Walkthrough

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

**Problem**: Select the appropriate deployment paradigm for a vision-based pedestrian detection system driving emergency braking. **Evaluation**: 1. **Privacy Gate**: Vehicle camera feeds do not…

### Napkin Math 2.1: The energy of transmission

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Problem: Should a battery-powered sensor process data locally (TinyML) or send it to the cloud?

### Napkin Math 2.2: ResNet-50 on cloud vs. mobile

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Problem: Is ResNet-50 inference compute bound or memory bound on (a) a high-end data center GPU (NVIDIA A100 class) and (b) a flagship mobile NPU (Apple/Qualcomm class)? Given (from Lighthouse…

### Napkin Math 2.3: The distance penalty

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Problem: Consider a real-time safety monitor for a robotic arm. The safety logic requires a 10 ms end-to-end response time to prevent injury. The model runs in a high-performance cloud data center…

### Napkin Math 2.4: Cloud vs. edge TCO

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Scenario: Avision system serving 1M daily inferences (ResNet-50 scale, 10ms latency, 100KB response). Cloud Implementation (illustrative public list pricing) | Cost Component | Calculation | Annual…

### Napkin Math 2.6: The bandwidth bottleneck

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

- Problem: Consider a quality control system for a factory floor with 100 cameras running at 30 FPS with 1080p resolution . Should the system stream to the cloud or process at the edge? Physics: 1.…

### Napkin Math 2.7: Napkin math: The locality crossover

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

- Problem: Should a drone's object avoidance system (4K, 60 FPS) offload to the cloud? Variables: · Data (𝐷 vol ) : 4K frame ≈ 25 MB. · Bandwidth ( BWnet ) : 100 Mbps home broadband (up). · Remote…

### Napkin Math 2.8: Edge inference sizing

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Scenario: A smart retail chain deploying person detection across 500 stores, each with 20 cameras at 15 FPS.

### Napkin Math 2.9: The battery tax

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Problem: Consider deploying a 'real-time' background object detector on a smartphone. The model consumes 2 Watts of continuous power when active. The phone has a standard 15 Watt-hour (Wh) battery.…

### Napkin Math 2.10: The thermal wall

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Problem: An unoptimized LLM requires 12 W peak compute. Can it be deployed on a mobile device?

### Napkin Math 2.11: Energy per inference

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Energy consumption spans eight orders of magnitude across deployment paradigms: | Paradigm | Example Workload | Energy/Inference | Battery Life (3.7V, 3000mAh) |…

### Napkin Math 2.12: Autonomous vehicle emergency braking

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Application: Vision-based pedestrian detection for emergency braking.

### Napkin Math 3.1: The iteration tax

[ch03.md](chapters/ch03.md) · Vol 1 · Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)

Problem: Adiabetic retinopathy (DR) screening system for rural clinics must choose between a large ensemble trained on high-resolution fundus images (training time: 1 week, accuracy: 95 percent) and…

### Napkin Math 3.2: Bandwidth vs. compute

[ch03.md](chapters/ch03.md) · Vol 1 · Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)

Problem: A rural clinic captures retinal images for DR screening. Can the clinic upload all images to the cloud for processing, or must it process them locally on edge hardware? Math: 1. Daily data:…

### Napkin Math 3.3: Cloud vs. edge deployment economics

[ch03.md](chapters/ch03.md) · Vol 1 · Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)

Problem: Aproduction model processes about 760,000 billable screening images per month across 500 clinics, assuming one processed image per patient after local selection and quality checks. Should…

### Napkin Math 4.1: The physics of data gravity

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Problem: A 1 PB training dataset resides in a US East data center, while a Tensor Processing Unit (TPU) pod is available in US West. Is it faster to move the data or to move the compute?

### Napkin Math 4.2: False positive targets

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Constraint: User tolerance is max one false wake-up per month.

### Napkin Math 4.3: Synthetic data generation

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Building synthetic datasets is one of the most cost-effective data engineering techniques. This exercise generates synthetic audio samples using pitch shifting, noise injection, and room impulse…

### Napkin Math 4.5: The cost of transformation placement

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Problem: Ateam processes 10 TB of raw clickstream data daily and must compute user session features for 3 ML models, each requiring different aggregation windows (1-hour, 24-hour, 7-day). Which is…

### Napkin Math 4.6: The coordination tax

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Problem: Mean normalization must be computed across 1 TB of features distributed across 100 nodes. Is it faster to (A) gather all data to one node and compute centrally, or (B) compute local means…

### Napkin Math 4.7: The active learning multiplier

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Problem: A 10M image dataset has a \$50K labeling budget. Random sampling achieves 85 percent accuracy with 100K images, while the target is 95 percent accuracy.

### Napkin Math 4.9: Format efficiency

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Storage formats determine how much 'waste' data must move to retrieve the signal needed for training, as captured in Equation 4.7: Effective Bandwidth = Physical Bandwidth ×𝜂 format (4.7) Scenario:…

### Napkin Math 5.2: Quick estimation for ML engineers

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

Detailed calculations are essential for design documents, but experienced engineers also develop rapid mental estimation skills. These 'napkin math' shortcuts enable quick feasibility checks before…

### Napkin Math 6.1: The quadratic bottleneck

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Problem: How much memory does the attention matrix of a single layer require at sequence length N = 100,000 (context window)?

### Napkin Math 6.2: The capacity wall

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Problem: Consider a recommendation system for a store with 100 Million items using an embedding size of 128 . How much memory does the item table alone require?

### Napkin Math 6.3: The energy cost of data movement

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

A core systems principle: moving data costs more than computing on it . A floating-point Revisit the preceding architectures through this energy lens: MLPs have low data reuse (each weight loaded…

### Napkin Math 8.1: GPT-2 attention layer computation

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Each GPT-2 layer performs attention computations that exemplify dense matrix multiplication demands. For one GPT-2 transformer layer (all heads combined) with batch\_size = 32, sequence\_length =…

### Napkin Math 8.2: GPT-2 GELU activation function

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Beyond the foundational activation functions covered in Chapter 5 (Sigmoid, Tanh, ReLU), modern architectures increasingly adopt smoother alternatives. GPT-2 uses a GELU activation (Hendrycks and…

### Napkin Math 8.3: GPT-2 optimizer memory requirements

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Arepresentative GPT-2 XL training configuration uses the Adam optimizer with the following hyperparameters: - β₁ = 0.9 (momentum decay) - β₂ = 0.999 (second moment decay) - Learning rate: Warmed up…

### Napkin Math 8.4: GPT-2 activation memory breakdown

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

For GPT-2 with batch\_size = 32, seq\_len = 1024, hidden\_dim = 1600, 48 layers: - Per-Layer Activation Memory. · Attention activations: batch × seq × hidden × 4 (Q, K, V, output) = 32 × 1024 × 1600…

### Napkin Math 8.5: The network wall

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

- Problem: Ateam is training a large model on eight GPUs. Is the network the bottleneck? Math: For a 7 B parameter model with FP16 gradients: 1. Gradient size: 7 ×10 9 ×2 bytes = 14 GB per step. 2.…

### Napkin Math 8.6: Estimating VRAM requirements

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Problem: Will a 7 B parameter model fit on a 24 GB GPU for training? Given: 7 B parameters, mixed-precision training (FP16 weights/gradients, FP32 optimizer), Adam optimizer, 24 GB GPU memory.

### Napkin Math 8.7: The utility bill

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Problem: Is it cheaper to rent an H100 or buy it for training Llama-2-70B? Math: 1. Workload: Llama-2-70B (70 B params, 2 T tokens). 2. Compute required: (6 ×70 ×10^9 ×2 ×10^{12} ≈8.4 ×10^{23})…

### Napkin Math 8.8: GPT-2 mixed precision training impact

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

GPT-2 training heavily relies on mixed-precision (FP16) to fit within accelerator memory constraints.

### Napkin Math 8.9: GPT-2 gradient accumulation strategy

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

GPT-2's training configuration demonstrates the essential role of gradient accumulation.

### Napkin Math 8.10: Data vs. model parallelism

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

- The physics of splitting: Howshould a model that is too big or too slow be split across multiple devices? Scenario: Training a model with parameters 𝑃 and batch size 𝐵 across 𝑁 GPUs. Data…

### Napkin Math 8.11: The carbon footprint of training

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Scaling the Utility Bill: Training large models is not just a compute challenge; it is a massive energy sink. We can quantify the environmental impact of scaling training using the energy corollary…

### Napkin Math 9.1: Computing ICR: Coresets

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

Scenario: Training our ResNet-50 Lighthouse model from Section 6.1.1 on ImageNet for one epoch. We compare random batch selection vs. EL2N-based coreset selection (EL2N, or Error L2-Norm, scores each…

### Napkin Math 9.2: The data quality multiplier

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

The physics of noise: The following analysis explains why one clean sample provides as much learning signal as 100 noisy ones. Math: Classical learning theory (for convex optimization with SGD) tells…

### Napkin Math 9.4: The selection inequality

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

Problem: An active learning system selects the best 10 percent of samples for training, and the selection algorithm requires running the full model on the unlabeled pool. Is this activelearning loop…

### Napkin Math 10.2: The quantization speedup

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

Problem: Adeployment scenario calls for running a 7 B parameter LLM on a device with 16 GB RAM. The weights are FP16 (2 bytes).

### Napkin Math 10.3: The bandwidth-compute trade-off

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

Reducing the Memory Pressure: Low-rank factorization illustrates a classic systems trade-off: trading computation for bandwidth reduction . Storing a 4096 by 4096 matrix requires 64 MB(at FP32).…

### Napkin Math 10.4: Quantization savings

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

Scenario: Deploying Llama 3 8 B (8 billion parameters). - Hardware Req: Requires 24 GB GPU (for example, A10G, 3090, 4090). - FP16 (Half Precision) · Size: 8 9 2 bytes (16-bit) = 16 GB ×10 × -…

### Napkin Math 10.5: The SIMD multiplier

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

Throughput physics: Why is INT8 faster than FP32 on the same processor? Mechanism: SIMD (Single Instruction, Multiple Data). A CPU or GPU core processes data in fixed-width vector registers (for…

### Napkin Math 11.1: The energy advantage of pulsing data

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

systolic arrays vs. Traditional Vector Units: The 'Systolic' (heartbeat) metaphor is not just about timing; it reflects a decisive energy efficiency advantage. We can quantify the energy advantage of…

### Napkin Math 11.2: The bandwidth taper

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

The single-machine stack is governed by an orders-of-magnitude bandwidth hierarchy. On an NVIDIA H100 node: - HBM3: 3.4 TB/s - NVLink 4.0: 900 GB/s - PCIe Gen5: 64 GB/s - Network (NDR) : 50 GB/s…

### Napkin Math 11.3: The speed of light limit

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Problem: Why is on-chip SRAM necessary instead of fetching all data from HBM? Physics: 1. Distance: On a large 700mm² chip, signals travel ~20mm. 2. Speed: Signals in silicon travel at (half speed of…

### Napkin Math 11.4: The utilization gap

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs



### Napkin Math 11.5: Transformer layer analysis

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

For a transformer with hidden\_dim = 768, batch = 32, seq = 512: - Attention QKV Projection: · FLOPs: 2 × 3 × 32 × 512 × 768 × 768 = 58 billion FLOPs · Bytes: (input + weights + output) = (32 × 512 ×…

### Napkin Math 11.6: Convolutional layer analysis

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Consider a Conv2D layer with input shape (batch=32, channels=128, height=56, width=56), output channels=256, kernel size 3×3 on an A100 GPU: Computational Requirements: · Output size: = 25.7 M…

### Napkin Math 11.7: Dense layer analysis

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Consider a fully connected layer: input (batch = 32, features = 2048) → output (batch = 32, features = 2048) on the same A100:

### Napkin Math 11.8: LayerNorm analysis

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

LayerNorm with input shape (batch = 32, seq = 512, hidden = 768): - Input: 12.6 M 2 = 25.2 MB - Computational Requirements: · Elements: 32×512×768 = 12.6 M · Operations per element: mean (1 ADD),…

### Napkin Math 11.9: Batch size and arithmetic intensity

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Increasing batch size improves AI for matrix operations by amortizing weight loading. Equation 11.6 formalizes this relationship for a dense layer (𝐵×𝑀)×(𝑀×𝑁) : - Batch = 1: AI ≈1 FLOP/byte (memory…

### Napkin Math 11.10: The throughput ceiling

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Problem: What is the maximum possible utilization of an NVIDIA A100 when running GPT-2 inference (batch size 1)?

### Napkin Math 11.11: The carbon ROI of specialized silicon

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Problem: Should an inference fleet run on generic CPUs or invest in specialized NPUs (Neural Processing Units)? Physics: Specialized hardware achieves higher arithmetic intensity while using fewer…

### Napkin Math 12.2: Goodhart's Law in action

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

The metric trap: Optimizing for a single metric often degrades others. Scenario: Ateam optimizes a translation model for BLEU score . - Original Model: BLEU = 28.0, Inference = 50 ms. - Optimized…

### Napkin Math 12.3: Roofline analysis for BERT inference

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Problem: BERT-Base must be deployed for inference on an A100 GPU. Management expects high GPU utilization. What performance should we predict, and how can we improve it? Step 1: Hardware limits. -…

### Napkin Math 12.4: Measuring the iron law terms

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

- From Theory to Trace: Howto map the iron law equation from Section 1.7 to a profiler timeline (like Nsight Systems or PyTorch Profiler). Measuring the data term ( 𝐷 vol BW ) · Signal: Look for the…

### Napkin Math 12.5: Interpreting a benchmark claim

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Problem: Avendor claims 'Our system achieves 10,000 images/second on ResNet-50.' Should this number be trusted for deployment planning?

### Napkin Math 12.6: Scaling efficiency calculation

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Problem: Ateam trains ResNet-50 on ImageNet. Single-GPU training takes 24 hours. With 8 GPUs, training takes 4 hours. Is this good scaling? Where did the efficiency go? Step 1: Define scaling…

### Napkin Math 12.7: Why INT8 saves energy

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Recall from Chapter 11 that moving data costs far more energy than computing on it (the energy-movement invariant formalized in Chapter 4). Understanding WHY quantization reduces energy consumption…

### Napkin Math 12.8: Amdahl's Law: Optimization ceiling

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

The latency breakdown reveals why aggressive model optimization often yields disappointing end-to-end results. Consider a vision pipeline where preprocessing (JPEG decode, resize, normalize) consumes…

### Napkin Math 13.1: The cost of latency

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Latency constraints directly dictate infrastructure costs. Consider a GPU server renting for USD 4/hour.

### Napkin Math 13.2: JSON vs. Protobuf serialization

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Consider a request payload containing 1,000 floating point numbers (for example, an embedding vector). - JSON: Uses ~9 KB on the wire. Requires ~50 μs to parse. - Protobuf: Uses ~4 KB on the wire.…

### Napkin Math 13.4: ResNet-50: Latency budget breakdown

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Atypical serving request for our ResNet-50 classifier shows the following latency distribution: | Phase | Operation | Time | Percentage |…

### Napkin Math 13.5: The quantitative approach to serving

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

DSAEfficiency: General-purpose CPUs achieve only 1-2 percent of peak performance at batch1 because instruction overhead dominates. DSAs like TPUs and Tensor Cores replace complex Amdahl's Law at Work…

### Napkin Math 13.6: ResNet-50 capacity planning

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Consider designing a ResNet-50 serving system with these requirements: - Target p99 latency: 50 ms - Peak expected traffic: 5,000 requests per second Step 4: Add headroom for variance. Production…

### Napkin Math 13.8: ResNet-50 batching efficiency

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Two fixed costs dominate at small batch sizes. Kernel launch overhead 20 is the time for the CPU to prepare and submit work to the GPU. Each layer in a neural network typically requires a separate…

### Napkin Math 13.11: The iron law of batching efficiency

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Iron law connection: In serving, we maximize throughput by amortizing the Latency Term (𝐿 lat ) , as shown in Equation 13.11:

### Napkin Math 13.14: The carbon cost of a chat

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Joules per Token: The Green Metric: As LLMs scale, energy efficiency becomes a first-class operational metric alongside latency. For an H100 GPU (700 W TDP), we can quantify the energy footprint of…

### Napkin Math 13.15: ResNet-50: Runtime comparison

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Performance comparison for ResNet-50 inference on V100 GPU (batch size 1): | Runtime | Latency | Speedup × | Notes | |-----------------|-----------|-------------|---------------------------| |…

### Napkin Math 13.16: ResNet-50: Precision trade-offs on V100

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

| Precision | Latency | Memory | Accuracy | Tensor Core Util. | Calibration | |-------------|-----------|----------|------------|---------------------|-----------------| | FP32 | 2.8 ms | 98MB |…

### Napkin Math 13.18: ResNet-50: Cost analysis

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Consider serving ResNet-50 on AWS infrastructure (US-East region, on-demand pricing in 2026): | Instance Type | Cost/Hour | Throughput | Cost per 1M Images |…

### Napkin Math 14.1: The compound cost of manual operations

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Problem: Why build automated pipelines when manual retraining is faster? Physics: Manual work accumulates Compound Interest . - Manual retrain: 4 engineering hours per week. - Pipeline build: 80…

### Napkin Math 14.2: The cost of silent failures

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Problem: Is building an automated drift detection system worth the engineering effort? Scenario: Consider a product recommendation engine generating \$50M/year in revenue. Failure: Adeployment bug…

### Napkin Math 14.3: The half-life of a model

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

- Problem: How often should the team retrain the model to maximize profit? Physics: Model accuracy 𝐴(𝑡) decays at rate 𝛾 due to data drift. · 𝑄: Daily Query Volume (Traffic). · 𝑉: Financial value per…

### Napkin Math 14.4: The drift detection delay

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Problem: Amodel has 95 percent baseline accuracy . The goal is to detect a 5 percent drop (to 90 percent) with 95 percent statistical confidence. The system handles 1 request per second (1 QPS) . How…

### Napkin Math 14.5: The economics of observability

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

The monitoring trade-off: 'Measure everything' is physically impossible at scale. Equation 14.11 shows that observability cost scales linearly with sampling frequency and metric cardinality: Cost ≈…

### Napkin Math 15.1: The alignment gap

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

Problem: Amodel optimizes a proxy metric (Clicks) because the true metric (User Satisfaction) is unobservable. How much can they diverge? Physics: Goodhart's Law states that optimizing a proxy…

### Napkin Math 15.2: The statistics of representation

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

Problem: An engineering team needs to verify that a FaceID model works for a minority group representing 1 percent of the user base. A worst-case binomial margin of error near 1 percentage point at…

### Napkin Math 15.3: The price of fairness

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

Problem: Stakeholders demand elimination of a 20 percent True Positive Rate (TPR) disparity in a hiring model. What is the 'Price of Fairness' in terms of hiring quality? Physics: TPRs can be…

### Napkin Math 15.4: The carbon cost of scale

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

Problem: Afoundation model is being trained at the scale of GPT-3, consuming 1,300 Megawatthours (MWh) of electricity. What is the environmental impact?

### Napkin Math 21.3: Worked example: Is top-k compression worth it?

[v2_appC.md](chapters/v2_appC.md) · Vol 2 · Appendix C: Communication Foundations (Vol 2)



### Napkin Math 24.1: Quick calculations with these constants

[v2_appF.md](chapters/v2_appF.md) · Vol 2 · Appendix F: System Assumptions (Vol 2)

The constants in this appendix are designed for quick distributed systems calculations. Three examples illustrate the pattern. How long does an AllReduce of a 70.0B model take? With BF16 parameters,…

### Napkin Math 1.2: The coordination and energy tax

[v2_ch01.md](chapters/v2_ch01.md) · Vol 2 · Chapter 1: Introduction to ML Systems

Problem: Calculate the scaling efficiency and energy cost of training GPT-3 (175B params) on a cluster connected by 100G Ethernet vs. 200G InfiniBand. Physics: To synchronize 175B parameters (FP16),…

### Napkin Math 2.1: The physics of token latency

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Scenario: Abandwidth-floor calculation for generating one token from Llama-3 70B (140 GB weights in FP16) at NVIDIA H100 memory bandwidth. The full FP16 model exceeds one H100's HBM capacity, so a…

### Napkin Math: The memory wall: H100 vs. H200

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

To understand why the 'memory wall' is the primary constraint for modern large language models (LLMs), we compare the NVIDIA H100 against its successor, the H200 . While both chips share the same…

### Napkin Math 2.2: The energy cost of data movement

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

The iron law of modern computing is that moving data costs significantly more energy than manipulating it. We can prove this by analyzing the energy hierarchy of a single operation at the 4nm process…

### Napkin Math 2.3: The physics of the staircase

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

≈ Problem: A10 GB buffer is synchronized across the fleet. How much does the physical 'Layer' of the fleet affect transfer time? Math: Transfer time is 𝑇 = Data / Bandwidth. 1. HBM(Intra-Chip) : 10…

### Napkin Math 2.4: The cost of crossing the cliff

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Scenario: Synchronizing a 1 GB gradient buffer during a training step. 1. Intra-Node (NVLink) : Bandwidth = 900 GB/s. intra GB GB/s 1 1 ms 2. Inter-Node (InfiniBand NDR) : Bandwidth = 50 GB/s. 𝑇…

### Napkin Math 2.6: The cooling tax

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

- Consider a 1,000-GPU cluster of H100s at 700 W TDP each. · IT Power: 1,000×700 W=700 kW · Air cooling (PUE 1.5) : Total facility power = 700 kW × 1.5 = 1,050 kW. Cooling overhead = 350 kW. · Liquid…

### Napkin Math 2.7: Training time for 175B

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

- We can derive the training time for our 175B model from first principles. 1. Total FLOPs: Using the approximation 6×𝑃 ×𝐷, where 𝑃 = 175×10 9 and 𝐷=300× 10 9 tokens: 3.15×10 23 FLOPs 2. Cluster…

### Napkin Math 2.8: Scaling efficiency for a 175B model

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Setup: Training a 175B model on a DGX H100 cluster with 400 Gbps InfiniBand per GPU. - 𝑇 ≈2.1 · AllReduce time for 350 GB of gradients using ring-AllReduce with overlap: 𝑇 comm ≈3.5 seconds (raw…

### Napkin Math 2.9: The 10,000-GPU cluster

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

- Consider a cluster of 1,250 DGX H100 nodes (10,000 GPUs) for training our 175B model. On-Premises (3-year lifecycle) : · Hardware CapEx: 1,250 nodes × \$350,000 = \$437.5M · Network CapEx: ~\$25M…

### Napkin Math 4.2: When does AllReduce become the bottleneck?

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Step 1: Compute time per iteration. Assume each GPU processes a synthetic microbatch requiring 5×10 13 FLOPs, chosen to produce an approximately 100 ms compute phase for this bottleneck example. At…

### Napkin Math 4.3: Bisection bandwidth: The cost of oversubscription

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Problem: Acluster designer is choosing between a 'Non-blocking' (1:1) fat-tree and a 'Costoptimized' (4:1) spine for a 1024-GPU cluster. How much slower will a 100 GB-per-GPU AllReduce be on the…

### Napkin Math 4.4: The rail-optimized dividend

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Problem: A team is synchronizing per-rank data-parallel gradients across 128 nodes. In a standard fat-tree, each message between same-rank GPUs traverses a Leaf switch and a Spine switch (2 hops). In…

### Napkin Math 4.5: The bisection bottleneck

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Problem: Acluster has 1,024 accelerators across 128 nodes. Each accelerator has 400 Gb/s (50 GB/s) network injection bandwidth. An AllReduce job requires full bisection bandwidth. Scenario A…

### Napkin Math 4.6: The probability of a PFC storm

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Problem: A4096-GPU RoCE cluster is in operation. If the probability of a single transceiver degrading and triggering PFC pauses is just 0.001% per day, what is the chance of a cluster-wide 'PFC…

### Napkin Math 4.7: Napkin math: The optical dividend

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Problem: Calculate the power savings of moving a 51.2 Tbps switch from pluggable transceivers to Co-Packaged Optics (CPO). 1. Pluggable Architecture: 128 ports × 20 W = 2.56 kW for optics alone. 2.…

### Napkin Math 5.1: The thundering herd: Shard contention

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

Problem: A dataset is split into 1000 shards on a shared file system. If 32 GPUs each pick a shard at random to start their next epoch, what is the probability that at least two GPUs 'collide' on the…

### Napkin Math 5.2: Text vs. image bandwidth

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

The bandwidth demand of a 2,048-GPU cluster depends entirely on the data modality. For text training, the demand is surprisingly low. With a typical batch size of 4,096 tokens per GPU and a 200 ms…

### Napkin Math 5.3: The ImageNet bottleneck analysis

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

Problem: AResNet-50 training job on ImageNet (1.28M images, ~150 KB average) targets 1,000 images/second. The question is whether to use individual JPEG files on an HDD or NVMe.

### Napkin Math 5.4: ROI of local NVMe caching

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

- Problem: A vision-model training pipeline runs each step in 800 ms. Fetching data from a shared Parallel File System adds 150 ms of I/O wait because of network congestion. How much does adding…

### Napkin Math 5.6: The CPU bypass dividend

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

Problem: Atraining node with 8 GPUs loads 150 KB images at 8,000 images/second per GPU (64,000 images/second total). Compare the CPU load under traditional I/O vs. GDS. Traditional path: Each image…

### Napkin Math 5.7: The egress tax

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

Problem: Ateam trains a vision model on a 50 TB image dataset stored in S3. Training runs for 20 epochs. The decision is whether to stream from S3 each epoch or stage to local NVMe.

### Napkin Math 5.8: The checkpoint storm

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

Problem: A 256-node cluster saves a 175B-parameter checkpoint every 10 minutes. Each checkpoint totals 1,750 GB. With ZeRO-3, each node saves roughly 7 GB. 1. Per-node write to local NVMe (4 drives…

### Napkin Math 5.9: The 175B model's storage footprint

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

Thecompletestorage picture for our running example, a 30-day training run of a 175B-parameter model on 256 nodes: | Category | Volume | Primary Tier |…

### Napkin Math 5.10: Napkin math: The synthetic tax

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

Problem: Calculate the storage amplification of a 1 TB synthetic dataset that requires cryptographic lineage and multi-model verification. 1. Raw Payload: 1 TB. 2. Provenance Overhead: 40 percent…

### Napkin Math 6.2: GPT-2 data parallel scaling

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

The following example demonstrates how data parallelism scales in practice, including efficiency degradation.

### Napkin Math 6.3: Gradient accumulation speedup

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Problem: AGPT-2 run on a commodity 10G network is communication-bound at 32 GPUs, costing \$3,021 for a fixed number of samples. Can a single 8-GPU node achieve the same effective batch size more…

### Napkin Math 6.4: ZeRO memory savings

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Scenario: Training a 7B parameter Llama 2 model using Mixed Precision (FP16). Baseline: Standard DDP (Replicated State) Per-Parameter Memory Cost: - Weights (FP16) : 2 bytes - Gradients (FP16) : 2…

### Napkin Math 6.5: FSDP communication analysis

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

FSDP introduces communication on the critical path that DDP avoids: 𝑀 × The choice between FSDP and DDP depends on model size and memory constraints. Use DDP when the model fits in GPU memory with…

### Napkin Math 6.6: Scaling from 8 to 64 workers

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Setup: Transformer model with 1.3B parameters, target perplexity 15.0, baseline training: 100K iterations on single GPU with 𝑏 = 32. 8 Workers (BSP) · Effective batch size: 256 - Learning rate: 8…

### Napkin Math 6.7: The memory wall of scale

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Problem: Training a 175 Billion parameter model (like GPT-3) on NVIDIA A100s (80 GB). Can Data Parallelism with ZeRO-3 handle this?

### Napkin Math 6.8: The cost of the pipeline bubble

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Problem: Afrontier-model training run uses pipeline parallelism across 8 nodes. To hide the sequential delay, the batch is split into 32 microbatches. What is the 'bubble tax'-the fraction of GPU…

### Napkin Math 6.9: Automated design space search (Tier 3 optimizer)

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Solution: Instead of trial and error, we invoke a Tier 3 Optimizer (like the ParallelismOptimizer in our physics engine) to find the mathematically optimal split. We configure the optimizer with the…

### Napkin Math 6.10: RLHF infrastructure budget: PPO vs. DPO

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Scenario: Aligning a 70B parameter policy model. Reference model: 70B (frozen). Reward model (PPO only): 13B (frozen). Value model (PPO only): 13B (training).

### Napkin Math 7.1: AllReduce cost for a 70B model

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

Problem: A70 billion parameter model trains with data parallelism across 64 GPUs connected by InfiniBand NDR (50 GB/s per port). Each GPU computes gradients in BF16 (2 bytes per parameter, standard…

### Napkin Math 7.3: Latency vs. bandwidth dominance

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

2 𝜇𝑠 Problem: Consider synchronizing a 1 MB buffer vs. a 1 GB buffer on InfiniBand NDR with 𝛼 = 2 𝜇 s and 𝛽 = 50 GB/s. How does the bottleneck shift? Case A: 1 MB Message · Bandwidth Time: 10 6…

### Napkin Math 7.4: Hiding communication behind computation

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

Problem: Atraining pipeline attempts to overlap gradient AllReduce with the next layer's backward pass. The backward pass takes 500 μs. The AllReduce has network latency 𝐿 lat =100 𝜇 s but processor…

### Napkin Math 7.5: AllToAll for MoE token routing

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

Problem: AMoEmodel processes a batch of 4096 tokens across 8 GPUs (512 tokens per GPU). Each token is a 2048-dimensional hidden state in BF16 (4 KB per token). The gating network assigns each token…

### Napkin Math 7.8: The hierarchical bandwidth multiplier

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

Problem: Acluster has 8 nodes, each with 8 GPUs (64 GPUs total). The system must AllReduce a 1 GB gradient buffer. Compare flat Ring AllReduce vs. Hierarchical AllReduce.

### Napkin Math 7.9: Three-level hierarchical bandwidth budget

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

Problem: A128-GPU cluster is arranged as 4 racks of 4 nodes of 8 GPUs. Cross-rack bandwidth is oversubscribed 2:1 (effective 25 GB/s). How much does 3-level hierarchical AllReduce reduce cross-rack…

### Napkin Math 7.10: Error feedback mechanism

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

𝑔 𝑣 | Step | True Gradient 𝑡 | Transmitted 𝑡 | Cumulative Transmitted | Cumulative True | |--------|-------------------|-----------------|--------------------------|-------------------| | 1 | 0.4 | 0…

### Napkin Math 7.12: Overlap budget for a 7B transformer

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

Problem: A32-layer transformer model (7B parameters) is trained on 64 GPUs. Each layer's backward pass takes 15 ms. The hierarchical AllReduce for each layer's gradients (~880 MB per layer) takes 26…

### Napkin Math 7.13: Napkin math: The overlap budget

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

- This analysis determines whether the communication cost of a 70B parameter model on 8 GPUs can be hidden behind computation. The physics determines the answer. 1. Gradient size: 70B params × 2…

### Napkin Math 8.1: The 9s of reliability

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

Problem: Acluster of 10,000 GPUs runs with each GPU at 99.99 percent availability (only 52 minutes of downtime per year). What is the probability that the entire cluster is up at the same instant? -…

### Napkin Math 8.2: Napkin math: The SDC certainty

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

Problem: Calculate the probability that at least one GPU in a 100,000-GPU fleet experiences a silent ALU error during a single 2-second training step. Systems insight: In a 100k-GPU fleet, a silent…

### Napkin Math 8.3: The Young-Daly optimal interval

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

× Problem: A10,000-GPU cluster has an MTBF of 3.69 hours. A full model checkpoint takes 21 seconds to write. What is the optimal checkpoint frequency? Math: Apply the Young-Daly formula: 𝜏 opt =√2⋅𝑇…

### Napkin Math 8.4: The recovery time budget

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

Consider our 175B parameter model training on 1,000 GPUs. The checkpoint size is approximately 2.1 TB (weights + Adam optimizer state). How much does a single failure event cost? 𝑇 - The budget (…

### Napkin Math 8.5: The straggler tax

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

Consider our 1,000-GPU cluster where a normal training iteration takes 1.0 second . Asingle GPU enters a thermally throttled state, clocking down to 50 percent speed, and now takes 2.0 seconds to…

### Napkin Math 9.1: The physics of deadlock

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Problem: A 1024-GPU cluster receives two frontier training jobs from separate teams, each requiring the full cluster. A naive scheduler (nongang) allocates 512 GPUs to Team A and 512 to Team B, then…

### Napkin Math 9.2: The queuing theory of GPU clusters

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

\[ W_q = \frac{\rho}{1 - \rho} \left( 1 + \frac{C_s^2}{2} \right) \] AGPUcluster can be modeled as an M/G/1 queue, where jobs arrive according to a Poisson process (𝜆) and service times follow a…

### Napkin Math 9.3: The topology placement impact

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

The physical location of GPUs on the network switch fabric dramatically impacts collective performance. Consider an AllReduce operation across 64 GPUs: · Random placement: Spread across many racks →…

### Napkin Math 9.4: The elastic scaling decision

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Consider a large language model training job with a target batch size that requires 512 A100s for peak efficiency. Three scheduling strategies are evaluated over a 24-hour window. Assumptions:…

### Napkin Math 9.5: The autoscaling lag

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Consider a serving fleet with 10 replicas, each capable of 5 queries per second (QPS) while meeting the 500 ms SLO. Total capacity: 50 QPS. Scenario: Traffic ramps from 40 QPS to 80 QPS linearly over…

### Napkin Math 9.6: GPU sharing ROI

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Consider a fleet serving 100 distinct 7B models (26 GB footprint each) and 10 distinct 175B models (350 GB footprint each). Strategy B - Mixed sharing (MPS for small, exclusive for large) : Pack 2…

### Napkin Math 9.7: The diurnal GPU shift

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Consider a fleet of 1,000 GPUs managed under two regimes: Scenario B - Dynamic Sharing: Serving claims GPUs strictly as needed (average 150). Training reclaims unused serving GPUs (average 250),…

### Napkin Math 9.8: The value of policy debugging

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Problem: Aplatform team manages a 1000-GPU cluster. Initial monitoring shows 60 percent average utilization. After a week of policy debugging (capability-based scheduling, topologyaware placement,…

### Napkin Math 10.3: The compilation dividend

[v2_ch10.md](chapters/v2_ch10.md) · Vol 2 · Chapter 10: Performance Engineering (Vol 2)

Problem: A13B parameter model is deployed for inference. Without compilation, the PyTorch eager mode processes 120 tokens/second on a single H100. The Nsight Systems trace reveals that 35 percent of…

### Napkin Math 10.4: The profiler detective

[v2_ch10.md](chapters/v2_ch10.md) · Vol 2 · Chapter 10: Performance Engineering (Vol 2)

Problem: A7B parameter LLM runs on a single H100 and shows 45 tokens/second during autoregressive generation at batch size 1. The pure FP16 weight-read roofline is higher, but after budgeting roughly…

### Napkin Math 10.5: The scaling tax

[v2_ch10.md](chapters/v2_ch10.md) · Vol 2 · Chapter 10: Performance Engineering (Vol 2)

Scenario: Training a 70B parameter model across a cluster of 128 H100 GPUs . - Local node baseline: Asingle 8-GPU node achieves 65.0 percent MFU . - Fleet performance: At 128 GPUs, the step time…

### Napkin Math 11.3: The batching efficiency curve

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

- Problem: An engineer optimizes two services: a Vision model (ResNet) and an LLM (70B). At what batch size does each hit the 'Knee' of its efficiency curve? Math: The knee occurs where the variable…

### Napkin Math 11.5: Napkin math: Scaling reasoning depth

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Problem: Calculate the latency impact of a model that uses 128 'Thinking Tokens' to solve a complex math proof vs. a standard answer. 1. Standard Response: 1 token answer = 100 ms. 2. Reasoning…

### Napkin Math 11.7: KV cache memory hierarchy

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Production systems use a memory hierarchy for KV cache: | Tier | Capacity | Latency | Use Case | |---------|------------|-----------|-------------------| | GPUHBM | 80 GB | 0 ms | Active sequences |…

### Napkin Math 11.8: MoE capacity planning

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Problem: A team deploys DeepSeek-V3 (671B total parameters, 37B active per token) for a chatbot application. The model uses FP8 weights (1 byte per parameter). The cluster has 8-GPU nodes, each with…

### Napkin Math 11.9: Interconnect technology comparison

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Communication overhead depends heavily on the interconnect technology: | Interconnect | Bandwidth | Latency | Use Case | |----------------|-------------|-----------|---------------| | NVLink (H100) |…

### Napkin Math 11.10: Quantifying noisy neighbor impact

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Consider an inference platform serving 10 tenants on shared H100 GPUs:

### Napkin Math 11.11: Cold start timeline for Llama-70B

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Bringing up a new replica for Llama-70B on H100: | Phase | Duration | Cumulative | |---------------------------|--------------|--------------| | Cloud API request | 5s | 5s | | GPU instance…

### Napkin Math 11.12: Reactive scaling response analysis

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Consider traffic spike from 1000 to 3000 QPS: Current state: 10 replicas, 100 QPS each, 70 percent utilization Target state: 30 replicas for 3000 QPS

### Napkin Math 12.1: NPU: The silicon dividend

[v2_ch12.md](chapters/v2_ch12.md) · Vol 2 · Chapter 12: Edge Intelligence (Vol 2)

Problem: AMobileNet classifier runs on both a generic mobile CPU and a specialized Neural Processing Unit (NPU). How much 'Silicon Dividend' does the NPU provide in terms of speed and battery life?…

### Napkin Math 12.2: Battery drain: The cost of edge learning

[v2_ch12.md](chapters/v2_ch12.md) · Vol 2 · Chapter 12: Edge Intelligence (Vol 2)

Problem: Ateam is designing a background fine-tuning job for a personalized voice assistant on a smartphone. The training job consumes 4.5 Watts and takes 30 minutes to complete. If the phone has a…

### Napkin Math 12.3: The hidden cost of personalization

[v2_ch12.md](chapters/v2_ch12.md) · Vol 2 · Chapter 12: Edge Intelligence (Vol 2)

Problem: Ateam is deploying a 10M parameter vision model to a smartphone with support for 10 different 'User Contexts' (Home, Office, Car, etc.). If a full fine-tuned model requires 40 MB, how much…

### Napkin Math 12.4: Model updates vs. raw data

[v2_ch12.md](chapters/v2_ch12.md) · Vol 2 · Chapter 12: Edge Intelligence (Vol 2)

Problem: Ateam is designing a federated camera-personalization system that learns from 195 MB of compressed user images per week. Should the system upload the raw images to the cloud for training, or…

### Napkin Math 13.1: The sharing dividend

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Problem: Aplatform team manages a fleet of 100 GPUs. Under dedicated per-team quotas, average idle time is 70% . Moving to a Multi-Tenant ML Platform that shares resources across 1 Feature Store: A…

### Napkin Math 13.2: The platform dividend

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Problem: An organization manages 50 models. A centralized ML Platform team costs \$120,000/month. If the platform saves each model team 20 hours of manual toil per month, is the platform investment…

### Napkin Math 13.3: The maintenance dividend

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Problem: A team spends 40 hours/month manually fixing 'broken plumbing' (stale data, failed scripts, manual monitoring). A one-month intensive cleanup (160 hours) is projected to reduce this to 8…

### Napkin Math 13.4: ROI of automation

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Problem: Ateam spends 10 hours of manual toil per model deployment. Investing 120 hours in a CI/CD pipeline is projected to reduce deployment toil to 0.5 hours. At 3 deploys per week, how long until…

### Napkin Math 13.5: The safety of staged rollouts

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Problem: Ateam is deploying a new ranking model. A 'Blue-Green' deployment (100 percent cutover) exposes all users to any potential bugs. A 'Canary' deployment starts at 5% traffic. By how much does…

### Napkin Math 13.7: The false alarm tax

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

The problem: Consider a system monitoring 100 models . Each model has 10 metrics (latency, accuracy, drift, and others). Alert thresholds are set at 3-sigma (99.7 percent specificity), and a control…

### Napkin Math 13.8: Time-to-detection: The monitoring lag

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Problem: A production model has a baseline accuracy of 95%. A data drift event causes accuracy to drop by 2%. If the service receives 1,000 requests per hour with labels, how long is needed to…

### Napkin Math 14.1: The cost of differential privacy

[v2_ch14.md](chapters/v2_ch14.md) · Vol 2 · Chapter 14: Security & Privacy (Vol 2)

Problem: Consider computing the average salary of 1000 employees while guaranteeing privacy budget 𝜖 = 1.0. The salaries range from \$0 to \$200,000. How much noise must the mechanism add? Math: 1.…

### Napkin Math 14.2: The tax of secure multi-tenancy

[v2_ch14.md](chapters/v2_ch14.md) · Vol 2 · Chapter 14: Security & Privacy (Vol 2)

Problem: A platform team hosts two models on a single H100 using Multi-Instance GPU (MIG) to provide hardware-level isolation. On a dedicated GPU, the model achieves 1,000 tokens per second. After…

### Napkin Math 14.3: Protecting a production API

[v2_ch14.md](chapters/v2_ch14.md) · Vol 2 · Chapter 14: Security & Privacy (Vol 2)

Consider a production API serving a ResNet-50 image classifier (1000 ImageNet classes) with 1M daily queries from 10K users.

### Napkin Math 14.4: The tax of trusted compute

[v2_ch14.md](chapters/v2_ch14.md) · Vol 2 · Chapter 14: Security & Privacy (Vol 2)

Problem: Ateam deploying a health-monitoring model compares three security levels: 1. Plaintext: Standard inference. 2. Encrypted Transport (AES) : Model/Data encrypted at rest/transit. 3. Encrypted…

### Napkin Math 15.2: Is the world changing?

[v2_ch15.md](chapters/v2_ch15.md) · Vol 2 · Chapter 15: Robust AI

Problem: A model monitors a critical input feature. The baseline mean was 0.5. Over the last 1,000 requests, the mean has shifted to 0.55. The engineering question is whether this is a random…

### Napkin Math 16.1: The carbon cost of training

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

Problem: Ateam trains a large model (GPT-3 size) consuming 1,287 MWh . How much CO2 is emitted, and how does that compare to a trans-Atlantic flight?

### Napkin Math 16.2: Automated carbon-aware scheduling (Tier 3 optimizer)

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

Problem: Ateam is planning a large training run requiring 10,000 MWh of energy, choosing between three regions with different electricity prices and carbon intensities. With an internal carbon tax of…

### Napkin Math 16.3: The geography of carbon

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

Problem: Ateam is choosing a data center for a 10,000 MWh training run. - Site A (Quebec) : Hydropower, 20 g CO 2 /kWh. · Site B (Poland) : Coal-heavy, 800 g CO 2 /kWh. How does the location affect a…

### Napkin Math 16.4: PUE: The cost of cooling

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

Problem: Ateam operates a 2.0 MW cluster. If the facility can be optimized from the industry average PUE (1.58) to state-of-the-art (1.10), how much energy and money does that save annually? Math:…

### Napkin Math 16.5: The energy of learning

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

Problem: Consider fine-tuning a small language model (1B parameters) on a user's smartphone overnight. Is this feasible within a 5 percent battery budget ?

### Napkin Math 17.1: The fairness tax

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

Problem: Consider a credit model with 85 percent accuracy . Group A (majority) has a 20 percent default rate. Group B (minority) has a 40 percent default rate due to systemic factors. If Demographic…

### Napkin Math 17.2: The fairness-efficiency frontier

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

Problem: Consider optimizing a hiring model. The 'unconstrained' model reaches 92% accuracy but exhibits a 15 percent disparity between demographic groups. Applying a fairness constraint (demographic…

### Napkin Math 17.3: The price of privacy

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

Training a next-word predictor on sensitive messages with DP-SGD (Differentially Private Stochastic Gradient Descent) to prevent data extraction. The privacy parameter 𝜖 is the privacy budget. Lower…

### Napkin Math 17.5: The automation bias paradox

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

Consider a radiology department deploying an AI assistant for tumor detection. 𝑆 =92% As AI reliability increases, human vigilance decreases-a phenomenon known as the paradox of reliability . · At 90…

### Napkin Math 17.6: The representation tax

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

Amedical imaging model trained on data from 5 major urban hospitals achieves 94 percent accuracy overall but only 78 percent on underrepresented populations (rural patients, elderly patients,…

### Napkin Math 18.2: The physics of better fabrics

[v2_ch18.md](chapters/v2_ch18.md) · Vol 2 · Chapter 18: Conclusion (Vol 2)

Problem: Modern GPU clusters are hitting the energy wall. Public optical I/O materials describe moving from roughly 6-10 pJ/bit long-reach electrical signaling toward below 5 pJ/bit optical…

## Systems Perspectives (Architectural Insights)

*111 entries, in reading order*

### Systems Perspective 18.1: The accelerator starvation problem

[appB.md](chapters/appB.md) · Vol 1 · Appendix B: Data Foundations

The choice of file format determines whether a system is I/O bound or compute bound. As Table B.2 shows, the serialization tax compounds with storage layout: row-oriented formats force full-row scans…

### Systems Perspective 18.2: Why statistics matters for systems

[appB.md](chapters/appB.md) · Vol 1 · Appendix B: Data Foundations

Your monitoring dashboard says average latency is fine, but users are complaining. Why? Because systems live in the 'long tail.' Statistics gives us the tools to measure uncertainty, detect drift,…

### Systems Perspective 19.1: Why this matters

[appC.md](chapters/appC.md) · Vol 1 · Appendix C: Algorithm Foundations

Many modern dense neural networks, especially transformers and large CNNs, spend much of their compute time in matrix multiplication or GEMM-like kernels. A single forward pass through a transformer…

### Systems Perspective 19.3: Why this matters

[appC.md](chapters/appC.md) · Vol 1 · Appendix C: Algorithm Foundations

Whentraining fails-loss goes to NaN, gradients explode, or memory runs out-understanding what backpropagation actually does is essential for diagnosing the problem. This section provides the mental…

### Systems Perspective 20.1: Anote on terminology: GPUs and accelerators

[appD.md](chapters/appD.md) · Vol 1 · Appendix D: Machine Foundations

Throughout this book, we often use 'accelerator' when discussing hardware acceleration. However, the principles-roofline analysis, memory hierarchies, numerical precision, and performance…

### Systems Perspective 20.2: Why this matters

[appD.md](chapters/appD.md) · Vol 1 · Appendix D: Machine Foundations

Consider a model that achieves good accuracy, but inference takes 200 ms when the SLA requires 50 ms. Performance analysis models provide a systematic method to diagnose whether the system is limited…

### Systems Perspective 20.3: Why this matters

[appD.md](chapters/appD.md) · Vol 1 · Appendix D: Machine Foundations

Aproduction model might run at 50 QPS in FP32 when the target is 200 QPS. Switching to INT8 could achieve this throughput, but accuracy may suffer. Understanding numerical formats enables a…

### Systems Perspective 20.4: The dynamic range wall

[appD.md](chapters/appD.md) · Vol 1 · Appendix D: Machine Foundations

The choice of numerical format is a direct application of the iron law of ML systems (Principle 3). Reducing precision from FP32 to BF16 or FP16 halves the Data Movement term in the denominator,…

### Systems Perspective 1.4: The iron law analogy

[ch01.md](chapters/ch01.md) · Vol 1 · Chapter 1: Introduction to ML Systems

We call this the 'iron law' by analogy to Patterson & Hennessy's Iron Law of Processor Performance (Patterson and Hennessy 2017). However, there are important differences. P&H's law is a…

### Systems Perspective 1.5: The efficiency paradox

[ch01.md](chapters/ch01.md) · Vol 1 · Chapter 1: Introduction to ML Systems

This apparent contradiction defines the economics of ML systems engineering. Efficiency gains enabled larger experiments, which demanded more compute, which motivated further efficiency research.…

### Systems Perspective 1.6: The engineering missions: Application scenarios

[ch01.md](chapters/ch01.md) · Vol 1 · Chapter 1: Introduction to ML Systems

The top of the hierarchy transforms abstract systems into concrete engineering missions. Each mission inherits one of the four System Archetypes introduced in the Engineering Crux (Section 1.5.1) and…

### Systems Perspective: Pattern Selection Guide

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

* **Train-Serve Split**: * *Choose when*: Training requires scales that inference does not; raw training data cannot be shared but model parameters are public. * *Avoid when*: The model requires…

### Systems Perspective 2.1: System balance across paradigms

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

The pipelined form of the iron law of ML systems from Section 1.7 states that execution time is bounded by the slowest resource, as Equation 2.6 formalizes: Here, 𝑂 represents total operations, 𝑅…

### Systems Perspective 2.2: The complexity tax

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Before committing to any ML deployment, weigh the Complexity Tax against simpler alternatives. Consider a classification problem solvable by either a Heuristic (if-then rules) or a Deep Learning…

### Systems Perspective 2.3: Pattern selection guide

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Train-Serve Split -Trade-off: Training cost vs. inference latency - Choose when: Training requires scale that inference does not; privacy matters for inference but not training - Avoid when: Model…

### Systems Perspective 3.1: The iron law of workflow

[ch03.md](chapters/ch03.md) · Vol 1 · Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)

The six lifecycle stages are not merely procedural steps; they are the engineering levers used to optimize the variables in the iron law of ML systems (𝑇 = 𝐷 vol BW + 𝑂 𝑅 peak ⋅𝜂 hw +𝐿 lat ) : -…

### Systems Perspective 4.1: The Energy-Movement Invariant

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Moving a bit of data dominates the energy budget, costing \(100\times\) to \(10,000\times\) more energy than performing a compute operation on it: | Operation | Energy (pJ) | Relative Cost | | :--- |…

### Systems Perspective 4.2: Key Data Engineering Numbers (2024 Estimates)

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

ML engineers must internalize these cost and time scales: | Operation | Cost / Metric | Context | | :--- | :--- | :--- | | **Crowdsourced image label** | \$0.01 - \$0.05 | Simple classification | |…

### Systems Perspective 4.1: The energy-movement invariant

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

The iron law in Section 1.7 and the memory-wall analysis in Section 11.4.1 imply a dataengineering invariant: moving a bit costs 100-10,000 × more energy than computing on it. While Chapter 10…

### Systems Perspective 4.2: Key data engineering numbers

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Just as systems engineers memorize latency numbers, ML engineers should internalize these data engineering constants: Costs (2024 estimates) | Operation | Cost | Notes |…

### Systems Perspective 5.2: The depth vs. width trade-off

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

However, depth introduces engineering challenges. Each additional layer: The theoretical power of depth comes from the exponential advantage: for certain function classes, a network with 𝐿 layers can…

### Systems Perspective 5.5: The memory cost of backprop

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

For deep networks, Activations dominate. Storing a batch of high-resolution images across 100 layers consumes gigabytes of HBM (High Bandwidth Memory). This Capacity Wall drives the need for systems…

### Systems Perspective 5.6: Batch size and hardware utilization

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

Thebatchsize trade-off: Larger batches improve hardware efficiency because matrix operations can process multiple examples with similar computational cost to processing one. However, each example in…

### Systems Perspective 6.1: Equivariance formalism

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Mathematical Formulation: For a convolutional layer with filter w and input x: Applying translation 𝑣 (shift by ) to the input: 𝑇 \(H(l)_{i,j,k} = \sum_{di} \sum_{dj} \sum_{c} W(l)_{di,dj,c,k}…

### Systems Perspective 7.1: The ML compiler

[ch07.md](chapters/ch07.md) · Vol 1 · Chapter 7: ML Frameworks (TF, PyTorch, JAX)

- In the context of the iron law (Section 1.7), a framework is a compiler for the silicon contract. The 'source code' is the model architecture (the 𝑂 term). The framework's job is to take this…

### Systems Perspective 7.7: The three problems in action

[ch07.md](chapters/ch07.md) · Vol 1 · Chapter 7: ML Frameworks (TF, PyTorch, JAX)

This trace reveals the three problems in concrete terms: - Execution: Eager mode enables line-by-line debugging but incurs dispatch overhead - Differentiation: Autograd tape records operations during…

### Systems Perspective 8.1: The 10 GB to 10 TB scale factor

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

- At 10 GB: The entire dataset often fits in system RAM. Data loading is a one-time 'startup cost,' and the disk bandwidth ( BW ) does not matter after the first few seconds. · At 10 TB: Data becomes…

### Systems Perspective 8.2: Why GPUs dominate training

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

The matrix operations described earlier directly explain modern training hardware architecture. GPUs dominate training for three reasons. First, matrix multiplication's independent element…

### Systems Perspective 8.3: Memory bandwidth bottlenecks

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Activation functions reveal a critical systems principle: not all operations are compute bound. While matrix multiplications saturate accelerator compute units, activation functions often become…

### Systems Perspective 8.4: Peak FLOPS vs. sustained performance

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Hardware vendors often market 'Peak TFLOPS,' but for a systems engineer, this number is often a theoretical limit that is rarely reached. The intensity gap reveals that most neural network…

### Systems Perspective 9.3: When to invest in data selection

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning



### Systems Perspective 10.2: The optimization composition problem

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

Unlike software functions that compose predictably, optimization techniques interact through shared physical resources: memory bandwidth, cache capacity, and arithmetic units. Pruning changes…

### Systems Perspective 11.1: Matching architecture to workload

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Thearchitects' dilemma: Systolic arrays must choose which data to keep stationary (in registers) to minimize movement. This choice hard-codes the hardware's preference for certain model types. |…

### Systems Perspective 11.2: The role of the compiler

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Developers rarely perform this complex mapping manually. Instead, a specialized compiler (like NVIDIA's NVCC or Google's XLA) takes the high-level model from the framework and automatically explores…

### Systems Perspective 11.3: The hidden optimization layer

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Most practitioners never interact directly with ML compilers, yet compiler quality often determines whether a model achieves 20 percent or 80 percent of hardware peak performance. Calling…

### Systems Perspective 11.4: When production differs from development

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Runtime behavior often surprises engineers who optimized their models in development environments. Common production surprises include: Training uses fixed batch sizes, but production inference may…

### Systems Perspective 12.1: Benchmarks as moving targets

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

In traditional systems (for example, SPEC CPU), the benchmark is a rigid specification . Asorting algorithm is correct if it sorts the list. Correctness is absolute and unchanging. In ML systems, the…

### Systems Perspective 12.2: Related efficiency metrics

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

While this chapter focuses on system-level benchmarking, comprehensive evaluation spans multiple dimensions covered elsewhere. For data selection metrics (PPD, DUE), see Chapter 9. For model…

### Systems Perspective 12.3: The fallacy of peak performance

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Dave Patterson often refers to peak performance as 'the performance the manufacturer guarantees you will not exceed.' For ML systems, this gap between peak and achieved performance is especially wide…

### Systems Perspective 12.4: Micro-benchmarking rules

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

To avoid measuring hardware artifacts instead of kernel performance, follow the Systems Detective's Rules: 1. The warm-up rule: Never measure the first ten to fifty iterations. Modern hardware uses…

### Systems Perspective 12.5: Edge benchmark reality check

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement



### Systems Perspective 12.6: The cost of comprehensive benchmarking

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

While benchmarking is essential for ML system development, it comes with substantial costs that limit participation to well-resourced organizations. Submitting to MLPerf can require months of…

### Systems Perspective 13.1: The serving inversion

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Applying the D·A·M taxonomy reveals how deployment inverts the engineering priorities: - Data (Information) : In training, the goal is Volume (shuffling billions of samples). In serving, the goal is…

### Systems Perspective 13.3: ResNet-50 across the serving spectrum

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

The same ResNet-50 architecture requires dramatically different serving strategies across deployment contexts:

### Systems Perspective 13.6: LLM serving: Beyond the fundamentals

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Language model serving introduces challenges beyond the batching and memory principles established here. The key-value cache that stores attention context scales with sequence length and batch size,…

### Systems Perspective 14.1: The operational mismatch

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Traditional monitoring tracks deterministic system health: server uptime, request latency, and request success rates. These signals suffice for deterministic software where correctness is binary. ML…

### Systems Perspective 14.2: The three critical interfaces

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Operationalizing machine learning requires coordinating three distinct system boundaries, each with unique constraints: Data-Model Interface: The handoff between data infrastructure and model…

### Systems Perspective 14.4: Iron law in production monitoring

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

- These utilization patterns map directly to the iron law of ML systems (Section 1.7). Monitoring reveals which term dominates: · Compute-bound (high GPU util, low memory BW util): Limited by 𝑂/(𝑅…

### Systems Perspective 15.1: The D·A·M taxonomy

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

When a system causes harm, use the D·A·M taxonomy to identify the root cause. Responsibility failures are rarely 'algorithm bugs'; they are structural flaws along one of the three axes: - Data…

### Systems Perspective 15.4: The carbon cost of compute

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

Quantifying Environmental Impact: To make carbon a first-class engineering metric, we must convert 'compute hours' into 'kg CO 2 eq'. Equation 15.2 captures this standard conversion: Carbon = Energy…

### Systems Perspective 16.1: The cost of a token

[ch16.md](chapters/ch16.md) · Vol 1 · Chapter 16: Conclusion & Thirteen Quantitative Invariants

We can apply the iron law (Principle 3) and Arithmetic Intensity (Principle 6) to a real-world problem: serving one token from a 70B parameter model (like Llama-2-70B) on an NVIDIA H100.

### Systems Perspective 16.2: Anew golden age

[ch16.md](chapters/ch16.md) · Vol 1 · Chapter 16: Conclusion & Thirteen Quantitative Invariants

Hennessy and Patterson (2019) declared a 'New Golden Age for Computer Architecture,' driven by the end of Dennard scaling, the slowdown of Moore's Law, and new opportunities from domain-specific…

### Systems Perspective 20.1: Node-level numbers for fleet reasoning

[v2_appB.md](chapters/v2_appB.md) · Vol 2 · Appendix B: Fleet Foundations (Vol 2)

Fleet reasoning depends on a few node-level numbers that directly affect fleet design: about 14 bytes per parameter for common Adam checkpoint state, with larger footprints when gradients,…

### Systems Perspective 20.2: The compound loss of fleet utilization

[v2_appB.md](chapters/v2_appB.md) · Vol 2 · Appendix B: Fleet Foundations (Vol 2)

A1,024-GPU H100 cluster has a peak aggregate throughput of 1,012,736 TFLOPS. After the three multiplicative losses, the effective throughput is: Effective = Peak × MFU ×𝜂 scaling × Goodput Ratio…

### Systems Perspective 21.2: Why this matters

[v2_appC.md](chapters/v2_appC.md) · Vol 2 · Appendix C: Communication Foundations (Vol 2)

Every distributed training step ends with a collective synchronization. The cost of that collective-not the cost of the matrix multiplies-often determines whether scaling from 8 GPUs to 256 is…

### Systems Perspective 22.1: The hidden cost of scale

[v2_appD.md](chapters/v2_appD.md) · Vol 2 · Appendix D: Reliability Foundations (Vol 2)

Acommon misconception is that doubling cluster size halves training time. In practice, doubling from 5,000 to 10,000 GPUs halves the MTBF, roughly doubling the failure-related overhead. The effective…

### Systems Perspective 23.1: The C³ tax on a 100,000-GPU cluster

[v2_appE.md](chapters/v2_appE.md) · Vol 2 · Appendix E: The C³ Taxonomy — Fleet-Scale Bottleneck Diagnosis (Vol 2)

Consider a 100,000-GPU H100 cluster with 98,900 PFLOPS of peak aggregate throughput. After the three C 3 losses: This is not a failure of engineering-it is the physics of fleet-scale computation. The…

### Systems Perspective 1.1: Transformer compute refresher

[v2_ch01.md](chapters/v2_ch01.md) · Vol 2 · Chapter 1: Introduction to ML Systems

Transformers process sequences using self-attention mechanisms that compute relationships between all token pairs. This architecture's computational cost scales quadratically with sequence length (…

### Systems Perspective 1.2: Amdahl's distributed pitfall

[v2_ch01.md](chapters/v2_ch01.md) · Vol 2 · Chapter 1: Introduction to ML Systems

The iron law of scale is a specialized form of Amdahl's Law. The maximum speedup of a distributed system is limited by its most tightly coupled component, usually the network synchronization. If a…

### Systems Perspective 2.1: The generality tax

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Amodern server CPU devotes roughly 30-40 percent of its die area to caches, 20-30 percent to control logic (branch predictors, reorder buffers, instruction decoders), and only 5-10 percent to…

### Systems Perspective 2.3: The end of Dennard scaling

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

For three decades, Dennard scaling allowed architects to increase transistor count without increasing power density, as smaller transistors required proportionally less voltage. That free lunch ended…

### Systems Perspective 2.4: Matching hardware to workload

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

The fundamental insight from the Roofline Model is that no single accelerator is optimal for all workloads . An H100 that delivers outstanding training throughput for a 175B LLM achieves less than 1…

### Systems Perspective 2.5: Beyond peak specifications

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

When evaluating accelerator options, the following metrics provide a more complete picture than peak TFLOPS alone: - Model FLOPS Utilization (MFU) : The ratio of achieved FLOPS during real training…

### Systems Perspective 2.6: Proactive vs. reactive maintenance

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Fleet operators have learned, often through costly experience, that proactive maintenance dramatically reduces the impact of hardware failures on training productivity. The three pillars of proactive…

### Systems Perspective 2.7: The infrastructure moat

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

The economics of ML infrastructure create a self-reinforcing advantage for organizations that can sustain high utilization. Building a 10,000-GPU cluster saves hundreds of millions over cloud rental,…

### Systems Perspective 4.1: The network as a gradient bus

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

In a single machine, the memory bus moves data between the processor and memory. In a distributed training cluster, the network fabric serves the analogous role: it is the Gradient Bus that moves…

### Systems Perspective 4.2: The cost of distance

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

In an ML fleet, distance is money. A 10,000-GPU cluster requires ~20,000 optical links at the spine layer alone. At \$500 each with 10 W per link, that represents \$10 million in cabling and 200 kW…

### Systems Perspective 4.3: InfiniBand vs. RoCE: The industry verdict

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

The coexistence of InfiniBand (NVIDIA DGX SuperPOD) and RoCE (Meta Grand Teton, Google) in production reflects a genuine trade-off rather than a clear winner. InfiniBand provides 30 to 50 percent…

### Systems Perspective 5.1: Fleet stack connection

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

In the Fleet Stack shown in Figure 1.13, Data Storage forms the third pillar of the infrastructure layer. The accelerator hierarchy consumes data, and the network fabric moves it between nodes. Data…

### Systems Perspective 5.2: The widening I/O wall

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

The I/O wall is not static: it is widening. Between 2016 and 2024, advertised accelerator Tensor Core throughput grew sharply, but exact ratios depend on whether the comparison holds precision fixed…

### Systems Perspective 5.3: The storage cost iceberg

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

The visible cost of storage (\$/GB/month) is the tip of the iceberg. Below the surface lie costs that often exceed the storage cost itself: - Egress fees: Cloud providers charge \$0.09/GB for data…

### Systems Perspective 5.4: The IOPS bottleneck in high-dimensional search

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

This architectural pattern shifts the primary storage bottleneck from sequential read bandwidth to random access memory IOPS . Vector databases must traverse high-dimensional graphs (such as HNSW) to…

### Systems Perspective 6.1: Fleet stack connection

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

In the Fleet Stack framework shown in Figure 1.13, Distributed Training represents the Distribution Layer. We are defining how to split the math. The actual execution of these split workloads happens…

### Systems Perspective 6.2: The Jeff Dean test

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Tensor parallelism across server racks connected by standard Ethernet will stall. The communication volume (proportional to Batch × Layers) requires the 600-900 GB/s bandwidth of NVLink. For…

### Systems Perspective 6.3: Distributed training complexity

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Although modern frameworks abstract away much of the complexity through sharded data parallelism and communication libraries, implementing distributed training efficiently remains a significant…

### Systems Perspective 6.4: Data parallelism at scale

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Data parallelism in production environments involves several operational considerations beyond the theoretical framework: - Communication efficiency: AllReduce operations for gradient synchronization…

### Systems Perspective 6.6: Debugging slow gradient synchronization

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Problem statement: An AllReduce of a 3 GB gradient tensor across 128 nodes (1,024 GPUs) takes 100 ms, while a hierarchical-AllReduce model that exploits NVLink within nodes and InfiniBand between…

### Systems Perspective 6.7: The energy tax of scale

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Distributed training is a race against energy as much as against time. In a single GPU, moving a byte from HBM to the cores costs roughly 1-2 pJ/bit . Moving that same byte across an NVLink…

### Systems Perspective 7.1: Fleet stack connection

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

Communication algorithms operate at the Distribution Layer of the fleet stack. The Infrastructure Layer below provides the raw bandwidth through NVLink, InfiniBand, and network topologies (covered in…

### Systems Perspective 7.2: AllToAll vs. AllReduce: Why scale differs

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

While AllReduce scales efficiently because it can be pipelined in a ring (where each node only talks to its neighbor), AllToAll is fundamentally harder to scale. This is why Expert Parallelism (MoE)…

### Systems Perspective 7.3: Debugging communication bottlenecks

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

Whenadistributed training job runs slower than expected, the communication library provides the first diagnostic signals. The following systematic approach isolates whether the bottleneck is in…

### Systems Perspective 8.1: Scale transforms failure

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

Asingle GPU with MTBF of 50,000 hours (5.7 years) fails rarely enough that manual intervention suffices. A 10,000-GPU cluster with the same per-GPU reliability has GPU-only system MTBF of 5 hours.…

### Systems Perspective 8.2: Three rules of failure at scale

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

1. At scale, failures are continuous, not exceptional. A 10,000-GPU cluster experiences failures every few hours. Systems must be designed expecting failure as normal operation. 2. Theoptimal…

### Systems Perspective 8.3: Checkpoint consistency models

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

The idealized protocol above assumes step 2 completes quickly. At scale, this barrier synchronization becomes the dominant checkpoint cost because there is almost always at least one slow worker in a…

### Systems Perspective 9.1: The economics of idle GPUs

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

The cost of poor scheduling compounds rapidly. Consider a 10,000-GPU cluster: - Operating cost: \$480,000/day (\$175M/year) - At 60 percent utilization: 6,000 GPUs productive, 4,000 idle =…

### Systems Perspective 9.2: Routing over synchrony

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

This necessitates Heterogeneous Gang Scheduling . The scheduler must atomically allocate a diverse constellation of resources-high-HBM nodes optimized for memory-bound inference generation, alongside…

### Systems Perspective 9.3: The convergence of HPC and cloud

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

The sharp distinction between HPC and cloud-native scheduling is rapidly blurring as both communities adopt features from the other. Kubernetes is evolving batch capabilities through the Volcano and…

### Systems Perspective 9.4: Topology placement impact

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Consider a 256-GPU training job using 3D parallelism: 8-way tensor parallel, 4-way pipeline parallel, 8-way data parallel.

### Systems Perspective 9.6: Spot vs. on-demand training

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Consider training a 70B parameter model requiring 512 GPUs for 14 days. On-demand: 512 GPUs × 336 hours × \$2.00/GPU-hour = \$344,064 Spot (65 percent discount, 5 percent checkpoint overhead, 1…

### Systems Perspective 9.7: The three utilization metrics

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

To debug cluster efficiency, measure utilization at three distinct layers. Allocated utilization is the percentage of physical GPUs reserved by the scheduler; low values indicate a lack of demand or…

### Systems Perspective 10.1: Fleet stack connection

[v2_ch10.md](chapters/v2_ch10.md) · Vol 2 · Chapter 10: Performance Engineering (Vol 2)

Performance Engineering is the Optimization Layer of the fleet stack. While Inference at Scale (Chapter 11) defines the serving architecture and scheduling policies, Performance Engineering optimizes…

### Systems Perspective 10.2: Analogy: The scholar's library

[v2_ch10.md](chapters/v2_ch10.md) · Vol 2 · Chapter 10: Performance Engineering (Vol 2)

The GPU memory hierarchy parallels a scholar researching in a library: - Registers (33 MB) are working memory: instant access, but capacity is small enough to hold only a few values at once. - Shared…

### Systems Perspective 10.3: Analogy: The short-order cook

[v2_ch10.md](chapters/v2_ch10.md) · Vol 2 · Chapter 10: Performance Engineering (Vol 2)

Imagine a kitchen where one chef chops vegetables, puts them in the fridge (HBM), then another chef takes them out to boil them, puts them back in the fridge, and a third chef takes them out to plate…

### Systems Perspective 10.4: Hardware-software co-design

[v2_ch10.md](chapters/v2_ch10.md) · Vol 2 · Chapter 10: Performance Engineering (Vol 2)

Graph compilation is the bridge between algorithmic intent and physical silicon constraints. A compiler like XLA or TensorRT does not merely 'reduce math operations'-it fundamentally reshapes the…

### Systems Perspective 11.1: Queuing theory and performance

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Queuing theory, developed by Agner Krarup Erlang in 1909 for telephone network analysis, remains foundational to systems performance engineering. The same mathematical framework that sized telephone…

### Systems Perspective 11.2: Analogy: The restaurant kitchen

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Imagine a restaurant where a waiter seats a table of four (a batch of 4 requests). In static batching, if three diners finish their meals in 20 minutes, but the fourth takes an hour, the waiter…

### Systems Perspective 11.3: Analogy: The inefficient hotel

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Imagine a hotel where every guest might stay anywhere from 1 to 10 days, but they do not know in advance. Under Contiguous Allocation, the hotel manager blocks out a 10-day suite for every guest just…

### Systems Perspective 11.4: Analogy: The executive and the assistant

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Imagine an executive (the large Target Model) writing an important letter. Normally, the executive types it out one word at a time, looking up complex information for every word (Autoregressive…

### Systems Perspective 11.5: The context switch of machine learning

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

This multi-tenant serving pattern shifts the fundamental performance constraint from compute throughput to SRAMcache trashing . As the continuous batching scheduler interleaves requests from…

### Systems Perspective 13.1: Fleet stack connection

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

We are now at the Management Layer of the fleet stack. While Parts I and II built the engine, and Part III deployed the service, this chapter provides the control plane: the dashboard, steering, and…

### Systems Perspective 13.2: The complexity explosion

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Managing 100 models is not 100 times the work of managing 1 model. It is fundamentally different due to dependencies, interactions, and organizational complexity. As Jeff Dean observes, the challenge…

### Systems Perspective 13.3: Training-serving skew

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Training-serving skew is the failure mode where subtle differences in feature processing logic between batch training and real-time inference pipelines cause silent accuracy degradation. At fleet…

### Systems Perspective 14.1: Fleet stack connection

[v2_ch14.md](chapters/v2_ch14.md) · Vol 2 · Chapter 14: Security & Privacy (Vol 2)

Part IV: The Responsible Fleet addresses the Governance Layer of the fleet stack. The fleet (Part I), the distributed logic (Part II), and the serving infrastructure (Part III) are operational. The…

### Systems Perspective 14.2: The privacy-utility trade-off

[v2_ch14.md](chapters/v2_ch14.md) · Vol 2 · Chapter 14: Security & Privacy (Vol 2)

Security and privacy are deeply interrelated but not interchangeable. A secure system helps maintain privacy by restricting unauthorized access to models and data. Privacy-preserving designs can…

### Systems Perspective 15.1: Fleet stack connection

[v2_ch15.md](chapters/v2_ch15.md) · Vol 2 · Chapter 15: Robust AI

Robust AI sits in the Governance Layer of the fleet stack. The previous chapter (Chapter 14) addressed malicious external threats; robustness addresses operational threats: distribution drift,…

### Systems Perspective 16.1: Fleet stack connection

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

Sustainability is the final component of the Governance Layer . Security protects against adversaries; Robustness protects against operational chaos; Sustainability protects against resource…

### Systems Perspective 16.2: Embodied carbon amortization

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

Ahidden cost emerges when renting a GPU for an hour: the fee does not cover electricity alone but also amortizes the carbon debt of manufacturing. Formula: Scenario: Training a model for 10 hours on…

### Systems Perspective 16.3: Hidden carbon cost of software

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

Beyond direct training and inference energy use, the entire software development ecosystem for AI has a significant, though difficult to measure, carbon footprint. The millions of continuous…

### Systems Perspective 16.5: Efficiency as sustainability

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

Every model optimization technique is simultaneously a sustainability tool. Pruning reduces computational complexity and energy consumption by eliminating unnecessary parameters. Quantization…

### Systems Perspective 17.1: From engineering to sociotechnical

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

The previous section focused on technical tools for solving well-defined problems: algorithms for detecting bias, methods for preserving privacy, and techniques for generating explanations. We now…

### Systems Perspective 18.1: Fleet stack connection

[v2_ch18.md](chapters/v2_ch18.md) · Vol 2 · Chapter 18: Conclusion (Vol 2)

The preceding chapters built the fleet stack layer by layer: from Infrastructure (Part I: The Fleet) to Distribution (Part II: Distributed ML), Serving (Part III: Deployment at Scale), and Governance…

## Checkpoints (Self-Check Questions)

*101 entries, in reading order*

### Checkpoint 17.1: D·A·M diagnosis check

[appA.md](chapters/appA.md) · Vol 1 · Appendix A: The D-A-M Taxonomy

1. A training job shows 95 percent accelerator utilization but loss has plateaued for two epochs. Which D·A·M axis should you investigate, and why? 2. Your colleague suggests adding more data loader…

### Checkpoint 18.1: Check your understanding

[appB.md](chapters/appB.md) · Vol 1 · Appendix B: Data Foundations

1. Atraining pipeline reads 500 GB of CSV data over a 10 Gbps link. Estimate the transfer time. Now estimate how long it would take if the data were stored as Parquet and only 20 percent of columns…

### Checkpoint 19.1: Training memory estimation

[appC.md](chapters/appC.md) · Vol 1 · Appendix C: Algorithm Foundations

1. Amodel has one billion parameters and is trained with Adam in mixed precision (FP16 weights, FP32 optimizer states). Without activations, how many GB of memory do the weights, gradients, and…

### Checkpoint 20.1: Check your understanding: Performance models

[appD.md](chapters/appD.md) · Vol 1 · Appendix D: Machine Foundations

1. Anew accelerator doubles compute throughput but keeps memory bandwidth the same. For a workload that is memory-bound on the current hardware, how much speedup do you expect? What about a…

### Checkpoint 1.1: The paradigm shift

[ch01.md](chapters/ch01.md) · Vol 1 · Chapter 1: Introduction to ML Systems

Before tracing the history of AI, verify your understanding of the paradigm shift in how we build software: - [ ] □ Can you distinguish Software 1.0 (explicit instructions) from Software 2.0…

### Checkpoint 2.1: Physical constraints and deployment

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Deployment choices are governed by physics, not just preference. Check your understanding: - □ Light barrier: Can you explain why the speed of light makes cloud ML impossible for <10 ms safety tasks?…

### Checkpoint 2.2: System design

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

The central trade-off is often Accuracy vs. Complexity .

### Checkpoint 3.1: MLvs. traditional DevOps

[ch03.md](chapters/ch03.md) · Vol 1 · Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)

MLOps is not merely DevOps for models. Ensure you grasp the key differences: - □ Failure Modes: Can you distinguish Silent Failure (degradation/drift) from Explicit Failure (crash/exception)? - □…

### Checkpoint 3.2: The workflow cycle

[ch03.md](chapters/ch03.md) · Vol 1 · Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)

The ML lifecycle is not a straight line; it is a spiral of continuous refinement.

### Checkpoint 3.3: The cost of late discovery

[ch03.md](chapters/ch03.md) · Vol 1 · Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)

Apply the constraint propagation principle to this scenario: A team discovers during monitoring (Stage 6) that their DR model fails for patients over 70 years old. This demographic requirement should…

### Checkpoint 4.1: The physics of data

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Data engineering is governed by physical costs. Check your intuition: - □ Do you understand data gravity: Why petabyte-scale datasets force compute to move to the data? - □ Can you explain the…

### Checkpoint 4.2: Four pillars framework

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

The four pillars provide a systems lens for every pipeline choice.

### Checkpoint 4.3: Defensive processing

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

The primary cause of ML system failure is not bad algorithms but training-serving skew. - □ The definition: Skew happens when the code processing data during training differs from the code processing…

### Checkpoint 5.1: Understanding deep learning's emergence

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

Before proceeding to the mathematical foundations, verify your understanding of why deep learning emerged: - □ Can you explain why rule-based programming fails for tasks like image recognition? - □…

### Checkpoint 5.2: Neural network architecture fundamentals

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

Before proceeding to network topology and training, verify your understanding of the foundational concepts we have covered:

### Checkpoint 5.3: Gradient flow

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

The forward pass is only half the story. Data vs. Signal - [ ] □ Forward Pass: Moves Data from input to output to generate predictions. - [ ] □ Backward Pass: Moves Error Signal from output to input…

### Checkpoint 5.4: Backpropagation

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

The 'Credit Assignment Problem' asks: which weight caused this error? Now that you have seen how backpropagation answers this question, verify your understanding:

### Checkpoint 5.5: Neural network learning process

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

You have now covered the complete training cycle, the mathematical machinery that enables neural networks to learn from data. Before moving to inference and deployment, verify your understanding:

### Checkpoint 5.6: Complete neural network system

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

Before examining how these concepts integrate in a real-world deployment, verify your understanding of the complete neural network lifecycle: Integration across phases: - □ Can you trace how…

### Checkpoint 6.1: Arithmetic intensity and architecture

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Match the architectural choice to its systems implication: - □ Weight Reuse (CNNs) : Increases arithmetic intensity by using the same weights across many inputs. - □ Large Embedding Tables (DLRM) :…

### Checkpoint 6.2: Spatial inductive bias

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

CNNs succeed because they match the structure of image data. Verify you understand how: - □ Can you explain parameter sharing: How using the same filter across the image reduces parameter count by…

### Checkpoint 6.3: Quadratic scaling intuition

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Modern AI scaling is defined by the cost of Attention. Verify your intuition: - □ Complexity: Do you understand why doubling the sequence length quadruples the memory required for the Attention…

### Checkpoint 6.4: DLRM and sparse scatter

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Recommendation systems stress a different part of the machine than CNNs or transformers. - □ Capacity-bound: Can you explain why embedding tables push DLRM into a memory capacity regime where 'FLOPs'…

### Checkpoint 7.1: Execution models

[ch07.md](chapters/ch07.md) · Vol 1 · Chapter 7: ML Frameworks (TF, PyTorch, JAX)

The choice of execution mode determines both developer velocity and model performance. Debuggability vs. Speed - [ ] □ Eager Mode (Python-First) : Why does executing ops one-by-one make debugging…

### Checkpoint 7.2: The systems cost of gradients

[ch07.md](chapters/ch07.md) · Vol 1 · Chapter 7: ML Frameworks (TF, PyTorch, JAX)

Training is inherently more expensive than inference because of Automatic Differentiation.

### Checkpoint 7.3: Hardware abstraction

[ch07.md](chapters/ch07.md) · Vol 1 · Chapter 7: ML Frameworks (TF, PyTorch, JAX)

The abstraction problem is the bridge between portable code and efficient execution . - □ Two dimensions: Can you distinguish data representation (layout, dtype, placement) from execution mapping…

### Checkpoint 8.2: The memory-compute trade-off

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Training large models requires managing the memory wall (the bandwidth bottleneck introduced in Chapter 5 and revisited in Section 7.3.1).

### Checkpoint 8.3: Scaling decisions

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Scaling trades compute bottlenecks for communication bottlenecks.

### Checkpoint 9.1: Data selection efficiency

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

The goal of data selection is to maximize the ICR.

### Checkpoint 9.2: The selection inequality

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

Data selection is not free. It introduces a new term to the iron law.

### Checkpoint 10.1: The efficiency frontier

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

Optimization is about trading one resource for another.

### Checkpoint 10.2: Structural optimization checkpoint

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

Test your understanding of the structural optimization techniques covered so far: - □ Can you explain the key difference between structured and unstructured pruning in terms of hardware efficiency?…

### Checkpoint 10.3: The quantization gate

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

Precision reduction is the most impactful deployment optimization.

### Checkpoint 10.4: Quantization and precision checkpoint

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

- Test your understanding of quantization before moving to architectural efficiency: □ Can you explain why INT8 quantization provides roughly 4 × memory reduction but potentially more than 4 × energy…

### Checkpoint 11.1: The parallelism gate

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Hardware speedups are capped by sequential bottlenecks. - Amdahl's Reality □ Serial Bottlenecks: Why does a 1,000 × faster GPU only speed up training by 5 × if data loading is slow? (Because Speedup…

### Checkpoint 11.2: The accelerator gate

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Hardware specialization is driven by energy physics. - □ Architectural response: Howdosystolic arrays (TPU) and Tensor Cores (GPU) minimize this cost? (They reuse data in registers for many…

### Checkpoint 11.3: Data movement and kernel fusion

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

At this point, you should be able to answer the first two questions from the roadmap: Whichdatastays local? The weight-stationary, output-stationary, and input-stationary patterns each make a…

### Checkpoint 11.4: Feasibility assessment: Can you run it?

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Before procuring hardware, validate feasibility by calculating these hard constraints:

### Checkpoint 12.1: Metric selection

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

The metric shapes the optimization.

### Checkpoint 12.2: Benchmarking methodology

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Bad benchmarks optimize the wrong things.

### Checkpoint 13.1: Queuing and SLO headroom

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

- Latency SLOs are not enforced by 'fast inference' alone; they are enforced by headroom . □ Little's Law: Can you use 𝑁 req =𝜆𝑇 lat to explain why rising queue depth implies rising latency even if…

### Checkpoint 13.2: Batching and traffic patterns

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Batching is the primary lever for serving economics, but the optimal strategy depends on context. □ Throughput-latency trade-off: Can you explain why batch size 32 achieves 6 × higher throughput than…

### Checkpoint 13.3: LLM serving fundamentals

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

LLM serving introduces constraints absent from traditional model serving. - □ TTFTvs. TPOT: Can you explain why these two metrics capture different user experience aspects (responsiveness vs.…

### Checkpoint 13.4: The optimization hierarchy

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Optimizing inference requires a layered approach.

### Checkpoint 14.1: The MLOps loop

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

MLOps is not linear; it is circular.

### Checkpoint 14.2: The monitoring stack

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

MLmonitoring is layered, not monolithic. Each layer reveals distinct failure modes that higher layers cannot diagnose:

### Checkpoint 15.1: Responsible design

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

Responsibility is a system property, not a model property.

### Checkpoint 15.3: Ethical deployment

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

Deployment is the point of no return.

### Checkpoint 15.4: Efficiency as responsibility

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

Total cost of ownership reveals where responsible optimization has the most leverage. - □ Inference dominance: Can you explain why a 20 percent inference latency reduction delivers more savings than…

### Checkpoint 16.1: Systems thinking

[ch16.md](chapters/ch16.md) · Vol 1 · Chapter 16: Conclusion & Thirteen Quantitative Invariants

An ML system is greater than the sum of its parts.

### Checkpoint 16.2: Applying the invariants

[ch16.md](chapters/ch16.md) · Vol 1 · Chapter 16: Conclusion & Thirteen Quantitative Invariants

Acolleague proposes quantizing your model from FP32 to INT8 to reduce serving costs. Trace the Invariants - □ Pareto Frontier (Principle 5): What accuracy are you trading for the bandwidth gain? - □…

### Checkpoint 1.1: The fleet mindset

[v2_ch01.md](chapters/v2_ch01.md) · Vol 2 · Chapter 1: Introduction to ML Systems

Verify your understanding of how MLfleets differ from traditional clusters: - □ Why does a single slow worker (straggler) have a disproportionate impact on a synchronous ML training job compared to a…

### Checkpoint 1.2: Applying scaling laws

[v2_ch01.md](chapters/v2_ch01.md) · Vol 2 · Chapter 1: Introduction to ML Systems

Verify your understanding of how scaling laws guide resource allocation: - □ Ateam has a fixed compute budget but limited training data. According to the 'Regimes' framework, should they train a…

### Checkpoint 1.3: The scale mandate

[v2_ch01.md](chapters/v2_ch01.md) · Vol 2 · Chapter 1: Introduction to ML Systems

- Before proceeding, verify your understanding of the 'Scale Mindset': □ Can you explain why scaling efficiency decreases as you add more nodes ( 𝑁 )? □ Do you understand the reliability gap: why a…

### Checkpoint 2.1: HBMand the memory wall

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Verify your understanding of 3D-stacked memory: - □ Why does HBM achieve higher bandwidth than DDR5 despite having a lower clock frequency? - □ What is the 'generality tax' of DDR memory, and how…

### Checkpoint 2.2: Roofline diagnosis

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Ateam is serving a 13B-parameter model at batch size 1 on an H100 and observing 25 ms per token. They propose upgrading to a B200 with 2.3 × the peak TFLOPS. Estimate the arithmetic intensity of…

### Checkpoint 2.3: Accelerator selection

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Your team needs to deploy a 70B-parameter model for both training and inference. Training will use batch size 2048 across 256 GPUs for 3 months. Inference will serve 10,000 requests per second at…

### Checkpoint 2.4: Power delivery physics

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Verify your understanding of the data center power path: - □ Why does synchronous ML training create more stress on the power grid than asyn- chronous web traffic? - □ What is the 'Power Ramp'…

### Checkpoint 2.5: Infrastructure physics

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Ateam is planning to deploy 256 H100 GPUs (32 nodes) in an existing air-cooled data center that has 250 kW of available power capacity and cooling rated for 200 kW at PUE 1.5. Can this facility…

### Checkpoint 2.6: TCO decision framework

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Your organization needs to train 10 models per year, each requiring 1,000 GPU-hours on H100s. You are evaluating whether to purchase a 128-GPU on-premises cluster or use cloud instances at…

### Checkpoint 2.7: Infrastructure planning exercise

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Your team needs to train a 70B-parameter model on 1 trillion tokens within 4 weeks. Using the following specifications: - H100 GPU: 1979 TFLOPS peak, assume 45 percent MFU · Compute budget: 9 12 23…

### Checkpoint 4.1: Protocol selection

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Consider a 2,048-GPU training cluster that will run both large language model training (gradient messages of several gigabytes) and reinforcement learning (frequent small control messages). 1. Which…

### Checkpoint 4.2: Fat-tree topologies

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Verify your understanding of hierarchical switch fabrics: - □ In a Radix-64 two-tier fat-tree, what is the maximum number of GPUs you can connect without core switches? - □ Why does a Non-blocking…

### Checkpoint 4.3: Rail-optimized networks

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Verify your understanding of workload-specific network design: - □ Which dimension of 3D Parallelism (TP, PP, or DP) is the primary beneficiary of a RailOptimized design? - □ Why does a…

### Checkpoint 4.4: Topology selection

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

The choice of network topology dictates the upper bound of training efficiency. Consider three workloads: 1. For a standard data-parallel job, bandwidth is dominated by AllReduce. Which topology…

### Checkpoint 4.5: Topology selection for your workload

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

You are designing the network for a new ML cluster that will run two primary workloads: (1) training a 175B-parameter language model using 3D parallelism (tensor, pipeline, and data parallelism), and…

### Checkpoint 4.6: Diagnosing a training slowdown

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Scenario: Your 175B model training job has been running for 3 days on 512 GPUs. You notice that the iteration time has gradually increased from 4.2 seconds to 4.8 seconds (a 14 percent slowdown). The…

### Checkpoint 5.1: Storage workload analysis

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

You are designing the storage subsystem for a new ML training cluster with 512 GPUs. The primary workload will train large language models on a 10 TB text dataset. 1. Based on the five inversions…

### Checkpoint 5.2: Parallel file system design

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

Consider a training cluster with 512 nodes, each running 8 GPUs. The training job requires 400 GB/s of aggregate read bandwidth. 1. If each Lustre OSS delivers 10 GB/s, how many OSS nodes are…

### Checkpoint 5.3: Data pipeline design

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

Atraining cluster runs 1,024 GPUs with 128-image batches (150 KB per image after compression, 150 ms per iteration). 1. Using Equation 5.1, calculate the required aggregate storage bandwidth at 90…

### Checkpoint 5.4: Checkpoint storage design

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

Atraining cluster of 1,024 nodes saves a 175B-parameter model checkpoint every 10 minutes. Each checkpoint is 1,750 GB total, distributed across all nodes. 1. What is the per-node checkpoint size? 2.…

### Checkpoint 6.1: Data parallelism mechanics

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Verify your understanding of how data parallelism distributes work: - □ In data parallelism, is the model state (weights) sharded or replicated across GPUs? - [ ] □ If you have 8 GPUs and a per-GPU…

### Checkpoint 6.2: Scaling decisions

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Given a 7B parameter model distributed across a cluster of 64 A100 GPUs (80 GB HBM each), what is the maximum useful batch size? To answer this, you must calculate the critical batch size (𝐵 crit )…

### Checkpoint 6.3: Model parallelism foundations

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Verify your understanding of model sharding: - □ Does Model Parallelism reduce the memory footprint per GPU for a given model? - □ In which phase-forward or backward-do sequential dependencies…

### Checkpoint 6.4: Hybrid 3D parallelism

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Verify your understanding of how parallelism strategies combine: - □ In a TP=8, PP=16, DP=128 configuration, which dimension is responsible for sharding layers within a single node? - □ How does…

### Checkpoint 7.1: Alpha-beta diagnostics

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

- Verify your understanding of network performance regimes: □ A message of 10 KB is being sent over a link where 𝛼 = 2𝜇𝑠 and 𝛽 = 10𝐺𝐵/𝑠 . Is this message Latency-Bound or Bandwidth-Bound ? □ If you…

### Checkpoint 7.2: Ring AllReduce mechanics

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

- Verify your understanding of bandwidth-optimal reduction: □ In a ring of 𝑁 GPUs, how many sequential steps are required to complete the full AllReduce? - □ True or False: In Ring AllReduce, every…

### Checkpoint 7.3: AllReduce algorithm selection

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

Verify your understanding of Ring vs. Tree AllReduce trade-offs: - □ Can you trace through the Scatter-Reduce phase of Ring AllReduce for 3 GPUs with a 3-element vector and verify that each GPU ends…

### Checkpoint 7.4: Gradient compression decisions

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

Verify your understanding of when and how to apply gradient compression: - □ Can you explain why 1-bit SGD without error feedback causes divergence, while 1-bit Adamwith warmup converges? What is…

### Checkpoint 8.2: Mapping failure domains

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

Verify your understanding of how failure domains nest and their operational impact: - □ If a rack switch fails, how many 8-GPU nodes are typically affected in a standard data center configuration? -…

### Checkpoint 8.3: Knowledge check

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

Question: Why might a software-based fault injection tool underestimate the resilience of a system compared to physical beam testing? Answer: Software tools often miss masking effects at the circuit…

### Checkpoint 9.1: Scheduling paradigm trade-offs

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

The following checkpoint reviews the core trade-offs before the chapter turns to topology-aware scheduling: - □ Can you explain why gang scheduling is essential for distributed training but not for…

### Checkpoint 9.2: Cost-aware scheduling trade-offs

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

The following checkpoint reviews cost-optimization mechanisms before the chapter turns to ML-specific schedulers: - □ Atraining job requires 512 GPUs for 14 days. Spot instances offer 65 percent…

### Checkpoint 9.3: Custom scheduler design space

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Consider the trade-offs between the four research schedulers examined above: - □ Tiresias eliminates runtime estimates. What information does it sacrifice, and when would this sacrifice hurt…

### Checkpoint 9.4: Multi-tenancy design decisions

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Consider a 2,000-GPU cluster shared between a research team (60 percent allocation) and a production team (40 percent allocation): - □ The research team is using only 30 percent of the cluster.…

### Checkpoint 10.1: The iron law of performance

[v2_ch10.md](chapters/v2_ch10.md) · Vol 2 · Chapter 10: Performance Engineering (Vol 2)

Verify your understanding of system-level performance diagnosis: - □ Aworkload is Memory-Bound . Will upgrading the GPU's clock frequency (increasing FLOPS) improve performance? - □ If you apply…

### Checkpoint 10.3: Optimization strategy

[v2_ch10.md](chapters/v2_ch10.md) · Vol 2 · Chapter 10: Performance Engineering (Vol 2)

Test your ability to design an optimization plan: - □ Given an LLM serving workload at batch size 1 that achieves 25 percent of peak bandwidth, can you identify the three most impactful optimizations…

### Checkpoint 11.1: Distribution strategy selection

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Verify your understanding of when to move from single-machine to distributed inference: - □ A 13B model (26 GB weights) fits on a single A100. If the throughput requirements double, should you use…

### Checkpoint 11.2: The serving hierarchy

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Verify your understanding of where specific optimizations sit within the serving hierarchy: - □ Which level of the hierarchy is responsible for managing KV cache fragmentation to increase concurrent…

### Checkpoint 11.3: Serving dimensions

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Verify your understanding of how workload constraints drive architectural choices: - □ Why is preemptive scheduling more critical for LLMs than for vision models? - □ For which workload type is…

### Checkpoint 11.4: Batching strategy trade-offs

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Verify your understanding of different batching mechanics: - □ Avision service has highly uniform input sizes and predictable traffic. Which is more appropriate: static batching or continuous…

### Checkpoint 12.2: Edge personalization

[v2_ch12.md](chapters/v2_ch12.md) · Vol 2 · Chapter 12: Edge Intelligence (Vol 2)

Verify your understanding of efficient on-device adaptation: - □ Why is Adapter Switching more storage-efficient than maintaining separate full-model copies for different user contexts? - □ How does…

### Checkpoint 12.3: Federated system design

[v2_ch12.md](chapters/v2_ch12.md) · Vol 2 · Chapter 12: Edge Intelligence (Vol 2)

Youare architecting a federated learning system for a fleet of 10 million mobile devices. The data is highly non-IID (users have distinct, clustered typing patterns), and the network environment is…

### Checkpoint 15.1: Knowledge check

[v2_ch15.md](chapters/v2_ch15.md) · Vol 2 · Chapter 15: Robust AI

Scenario: An attacker modifies the labels of a small subset of training data to cause a specific misclassification in a deployed model. Question: Is this an availability attack or a targeted attack?…

### Checkpoint 15.2: Defense selection

[v2_ch15.md](chapters/v2_ch15.md) · Vol 2 · Chapter 15: Robust AI

Given your threat model and compute budget, select the optimal defense strategy for the following scenarios: 1. Production image classifier (evasion) : Facing adversarial examples. Recommendation:…

### Checkpoint 16.3: Accounting for invisible carbon

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

You are auditing the carbon footprint of a Machine Learning platform. Classify the following emission sources into Scope 1 (Direct), Scope 2 (Indirect Energy), or Scope 3 (Value Chain): 1. Diesel…

### Checkpoint 16.4: The training-inference flip

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

Consider a vision model where training requires 2,000 GPU-hours at an average power draw of 300 W. Once deployed, the model serves 1 million requests per day, with each request taking 50 ms at an…

### Checkpoint 16.5: The efficiency trap (Jevons Paradox)

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

- Your team optimizes a translation service, reducing the computational cost per query by 50 percent (2 × efficiency gain). 1. If demand is inelastic (price change does not affect usage), how does…

### Checkpoint 16.6: Prioritizing decarbonization strategy

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

You are deploying a 70B LLM for a latency-sensitive application. Rank the following techniques by their potential to reduce total energy consumption, justifying your order using the principle that…

### Checkpoint 17.1: Exercise: Auditing a confusion matrix

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

Afraud detection model operates on two groups. - Group A (Majority) : TP, FP, FN, TN ( ). - Group B (Minority) : TP, FP, FN, TN ( ).

### Checkpoint 17.2: Fairness audit

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

You are deploying a hiring recommendation model. Before launch, determine the critical fairness metric: 1. Demographic parity: Requires equal acceptance rates across groups (for example, 50 percent…

## Examples (Applied Cases)

*56 entries, in reading order*

### Example 3.1: Auditing stage transitions

[ch03.md](chapters/ch03.md) · Vol 1 · Chapter 3: ML Workflow (Machine Learning Lifecycle & Systems Orchestration)

Scenario: Ateam claims to have completed Problem Definition for a medical imaging classifier. Before Data Collection begins, the stage transition must be audited against Table 3.1. Audit Checklist…

### Example 4.1: The Pipeline Jungle

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

A credit scoring model suddenly started rejecting all applicants from a specific region. An upstream team had changed the schema of the `zip_code` field from `integer` to `string` to handle…

### Example 4.2: Optimizing the KWS Design Space

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

*Scenario*: A KWS system with a target of \(98\%\) accuracy, \(<1\) false wake-up/month, a \$150K data budget, and a \(64\text{ KB}\) model size limit (always-on island). 1. **Constraint…

### Example 4.1: The pipeline jungle

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Failure: Acredit scoring model suddenly started rejecting all applicants from a specific region. Root cause: An upstream team changed the schema of the zip\_code fi eld from integer to string to…

### Example 4.2: Optimizing the KWS design space

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Scenario: AKWSsystem for a smart speaker has these constraints: - Target: 98 percent accuracy, < 1 false wake per month - Budget: \$150K total data engineering budget - Memory: 64 KB model size limit…

### Example 5.2: Building intuition: The XOR problem

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

(1,0) Consider a network learning the XOR function, a classic problem that requires nonlinearity. With inputs 𝑥 1 and 𝑥 2 that can be 0 or one, XOR outputs one when inputs differ and 0 when they are…

### Example 5.5: Tracing gradients: A worked backpropagation example

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

Setup: Consider a network with two inputs, a hidden layer of two neurons (ReLU activation), and one output neuron (no activation, for simplicity). Suppose the current weights and biases are:…

### Example 5.6: USPS digit recognition: By the numbers

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

Table 5.7: USPS LeNet Deployment Results: LeNet achieved lower error rates than human operators (1.0 percent vs. 2.5 percent) while processing digits 10-30 × faster-demonstrating that neural networks…

### Example 5.7: Then vs. now: USPS on modern HW

[ch05.md](chapters/ch05.md) · Vol 1 · Chapter 5: Neural Computation & Training Mechanics

The same neural network computation that required industrial-scale infrastructure in 1990 runs on pocket-sized devices today. Table 5.8 quantifies four decades of progress: Table 5.8: Hardware…

### Example 6.1: MNIST: Representation vs. learnability

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Consider classifying MNIST digits (784 input pixels, 10 output classes).

### Example 6.2: Concrete computation example

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

\[ \begin{bmatrix} 0.59 \\ -0.09 \\ 0.45 \end{bmatrix} = \begin{bmatrix} 0.8 & 0.2 & 0.9 & 0.1 \\ 0.3 & 0.8 & 0.4 & 0.2 \\ 0.2 & -0.3 & 0.6 & 0.7 \\ -0.2 & 0.1 & 0.4 & 0.6 \end{bmatrix}…

### Example 6.3: Equivariance: Feature detection

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Consider a image with a vertical edge at column 3: 7×7 Vertical edge detector filter:

### Example 6.4: Real-time wildlife monitoring

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Problem statement: Design an ML system to identify wildlife species from camera trap images in a national park. The system must process images locally (no cloud connectivity), operate on battery…

### Example 8.1: GPT-2 language model data pipeline

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Training language models like GPT-2 requires a specialized data pipeline optimized for text processing.

### Example 8.2: GPT-2 optimization on A100

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism



### Example 9.1: Coreset selection in practice

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

Context: Ateam has 1 million training images and wants to reduce to 100,000 (10 percent) for faster experimentation. Insight: Random sampling loses rare classes and edge cases. Instead, a coreset…

### Example 9.2: FixMatch on CIFAR-10

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

FixMatch (Sohn et al. 2020) combines pseudo-labeling with consistency regularization to achieve high label efficiency (Table 9.6). Table 9.6: FixMatch Label Efficiency on CIFAR-10: With 250 labels…

### Example 9.3: KWS data selection

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

Context: Our Keyword Spotting Lighthouse model from Section 6.1.1, a depthwise-separable convolutional neural network (CNN) known as DS-CNN, with 200 K parameters, represents the extreme end of data…

### Example 9.5: Worked example: Data echoing ROI

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

Scenario: Training ResNet-50 on ImageNet with heavy augmentation (RandAugment + MixUp).

### Example 9.6: Cost breakdown: ImageNet-scale training

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

| Cost Component | Calculation | Amount | |----------------------------------------|------------------|-----------------------| | Raw data (1.2M images) | Licensed dataset | \$50,000 | | Labels (1.2M…

### Example 10.1: The 4× MobileNet win

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

Context: Amobile app wants to add real-time 'Background Blur' to video calls. The feature requires a segmentation model running at 30 FPS. Bottleneck: The unoptimized MobileNetV3 (FP32), a…

### Example 10.2: BERT-Base mobile deployment pipeline

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

Consider deploying BERT-Base on mobile devices through three stages. Stage one applies structured architectural pruning: removing 30 percent of attention heads, trimming 40 percent of intermediate…

### Example 11.1: The TPUv1 vs. K80 efficiency shock

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

The comparison: In 2015, Google deployed its first Tensor Processing Unit (TPUv1) and compared it to the dominant GPU of the era, the NVIDIA K80. The shock: The TPUv1 was not just slightly faster; it…

### Example 12.1: Benchmarking a vision model for edge deployment

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Scenario: Ateam validates MobileNetV2 for a wildlife camera trap running on a Raspberry Pi 4.

### Example 13.2: ResNet-50: Image preprocessing skew

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

For ResNet-50 serving, common sources of skew include: Resize interpolation: Training uses PIL.BILINEAR while OpenCV defaults to cv2.INTER\_-LINEAR. These produce pixel-level differences that can…

### Example 13.3: Loading speed: Safetensors vs. Pickle

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Loading a 5 GB Stable Diffusion model: - Pickle ( torch.load ) : ~15 seconds. High CPU usage. - Safetensors: ~0.5 seconds. Near-zero CPU usage. By using mmap and formats like safetensors, loading…

### Example 13.4: The profiling loop

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

1. Capture: Run a warmup, then capture a trace of ten to fifty requests. 2. Visualize: Open the trace in a viewer (Chrome Tracing, Nsight). 3. Identify: Find the largest gap or the longest block. 4.…

### Example 14.1: Fraud detection retraining

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Consider a fraud detection model with the parameters in Table 14.9 that captures the high query volume and rapid drift rate characteristic of financial fraud detection: Table 14.9: Retraining…

### Example 14.2: Single-model monitoring budget

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Consider monitoring a single ML node (one production model) with: - one model with 3 deployment variants (production, canary, staging), each emitting 50 metrics - Metrics sampled every 15 seconds -…

### Example 14.3: Principle mapping guide

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

These case studies illustrate how each environment implements the five foundational MLOps principles: | Principle | Oura Ring | ClinAIOps |…

### Example 15.1: The COMPAS recidivism algorithm audit

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

Context: COMPAS is a risk assessment tool used in US courtrooms to predict re-offending. Judges use these scores to inform bail and sentencing decisions. Failure: AProPublica investigation (Angwin et…

### Example 22.1: Young-Daly: 175B model on a 10,000-GPU cluster

[v2_appD.md](chapters/v2_appD.md) · Vol 2 · Appendix D: Reliability Foundations (Vol 2)

Setup. Consider training a 175B-parameter model on a 10,000-GPU cluster. The cluster MTBF is 4.14 hours (Table D.2). The checkpoint size is 2,450 GB, and the parallel storage system writes at 100…

### Example 2.1: Roofline analysis: Training vs. inference

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Consider our 175B model on an H100 with 989 TFLOPS peak compute and 3.35 TB/s memory bandwidth. The ridge point is 295 FLOP/byte. Training (Forward Pass, Batch Size 2048) : The same weight tensor is…

### Example 8.1: Optimal checkpoint interval

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

Applying the Young-Daly formula to a real-world scenario illustrates its practical value. Scenario: Ateam is training Llama-3 on a cluster of 16,000 GPUs. - Checkpoint Cost (𝑇 write ) : It takes 2…

### Example 8.2: Debugging checkpoint overhead

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

A team training a 70B parameter model observes that checkpointing takes 10 minutes per checkpoint, far exceeding their expected 2-minute target. Training throughput has dropped 30 percent because the…

### Example 11.1: Dynamic batching for ResNet-50

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Consider a vision classification service with the following requirements: - Arrival rate: 5,000 QPS - Latency SLO: 50 ms P99 - Per-image inference time: 5 ms at batch=1, 25 ms at batch=32 - Number of…

### Example 11.2: Continuous batching in vLLM

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

vLLM implements continuous batching with several key mechanisms. Iteration-level scheduling evaluates at each decode step which sequences have generated end-of-sequence tokens (remove from batch),…

### Example 11.3: RecSys batching at Meta scale

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Consider Meta's recommendation infrastructure serving 10 million QPS across the platform:

### Example 11.4: Streaming speech recognition pipeline

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Consider a streaming speech-to-text system with 20 ms audio frames: Latency budget: 100 ms end-to-end (5 frames of delay) Pipeline stages: | Stage | Duration | Notes |…

### Example 11.5: Adaptive batching: Triton

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Triton Inference Server implements adaptive batching with three configurable parameters: 1. max\_batch\_size: Upper bound on batch size 2. batching\_timeout\_ms: Maximum time to wait for batch…

### Example 11.8: Prefix caching at scale

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Consider a chatbot service with a 2000-token system prompt and 1000 concurrent users:

### Example 11.9: Sarathi: Chunked prefill implementation

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

The Sarathi system (Agrawal et al. 2023) implements chunked prefill with the following design: Chunk sizing: Chunks are sized to complete in approximately the same time as one decode iteration…

### Example 11.10: Tensor parallelism for Llama-70B

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Consider serving Llama-70B with the following configuration: (Touvron, Martin, et al. 2023)

### Example 11.11: Expert parallelism for Mixtral-8x7B

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Mixtral-8x7B uses 8 experts per MoE layer with top-2 routing:

### Example 11.12: Heterogeneous GPU cluster

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)



### Example 11.13: Least-connections for LLM serving

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)



### Example 11.14: Consistent hashing for KV cache affinity

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Consider an LLM serving system where each user's conversation maintains KV cache state: Without affinity: - User sends message, routed to Server A, KV cache built - Next message routes to Server B…

### Example 11.16: Cascading failure prevention

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Consider a scenario where one server becomes slow (thermal throttling):

### Example 11.17: Bulkhead configuration for API tiers

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Atypical LLM API illustrates the three-tier bulkhead pattern. The enterprise tier runs on a dedicated GPU pool with hardware isolation and a 99.9 percent availability SLO - no other tenant's traffic…

### Example 11.18: Predictive scaling for traffic

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Achatbot service shows predictable daily patterns: | Time (UTC) | Typical QPS | Replicas Needed | |--------------|---------------|-------------------| | 00:00-06:00 | 500 | 5 | | 06:00-09:00 | 1500 |…

### Example 13.1: Feature freshness latency

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

The problem: A user clicks a 'Basketball' video. The time required for their feed to show more basketball content is the feature freshness latency. The formula is:

### Example 14.1: The privacy-accuracy tax

[v2_ch14.md](chapters/v2_ch14.md) · Vol 2 · Chapter 14: Security & Privacy (Vol 2)

Trade-off: Stronger privacy requires adding more noise to gradients during training. This noise acts like a 'tax' on model accuracy. Formula: For (𝜖,𝛿) -DP with gradient clipping 𝐶, the required…

### Example 16.2: Training emissions calculation

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

Consider training a 7 billion parameter model on 64 A100 GPUs for 14 days: Step 1: Compute energy. - GPU power: 400 W per A100 at typical training utilization - Training time: 14 days times 24 hours…

### Example 16.3: Battery life for TinyML

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

Consider deploying an anomaly detection model on a factory sensor node:

### Example 17.1: Calculating fairness metrics

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

Consider a simplified loan approval model evaluated on 200 applicants, evenly split between two demographic groups (Group A and Group B). The model makes predictions, and we later observe actual…

### Example 17.4: Conflicting values in practice

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

Consider a team building a mental health chatbot for adolescents that uses ML to detect crisis situations and recommend interventions. The system must balance multiple legitimate but incompatible…

## Lighthouses (Reference Workloads)

*55 entries, in reading order*

### Lighthouse 2.1: Five reference workloads

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Throughout this book, we use the five Lighthouse Models summarized in Table 1.5: concrete workloads that span the deployment spectrum and isolate distinct system bottlenecks. Chapter 6 provides full…

### Lighthouse 4.1: DLRM (recommendation lighthouse)

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Why it matters: Recommendation systems like Deep Learning Recommendation Model (DLRM) exemplify the scalability challenge of modern data engineering. They rely on highcardinality categorical features…

### Lighthouse 6.1: Canonical workloads

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

In computer architecture, the microprocessor without interlocked pipelined stages (MIPS) processor is often used to teach pipelining, not because it is the fastest chip today, but because it is the…

### Lighthouse 6.2: ResNet-50 (vision lighthouse)

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Why it matters: ResNet-50 is the gold standard benchmark for compute-bound vision workloads. Its architecture consists almost entirely of dense convolutional layers, making it highly regular and…

### Lighthouse 6.3: MobileNet (efficiency lighthouse)

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Why it matters: MobileNet represents latency-constrained edge workloads. Its depthwise separable convolutions trade channel mixing capacity for speed, making it the standard baseline for mobile apps,…

### Lighthouse 6.4: KWS (TinyML lighthouse)

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Why it matters: Keyword Spotting models (like DS-CNN) represent the power-constrained end of the spectrum. Used in always-on applications like Smart Doorbells (which often pair KWS with Wake Vision),…

### Lighthouse 6.5: GPT-2 XL (bandwidth lighthouse)

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Why it matters: GPT-2 XL exemplifies memory-bandwidth-bound workloads. During autoregressive inference, the model must load all 6.0 GB of FP32 weights from HBM for every generated token, while…

### Lighthouse 6.6: DLRM (recommendation lighthouse)

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Why it matters: DLRM exemplifies memory-capacity-bound workloads. Its massive embedding tables often exceed the memory of a single GPU, forcing model parallelism (sharding tables across devices). The…

### Lighthouse 7.1: Framework strategy by archetype

[ch07.md](chapters/ch07.md) · Vol 1 · Chapter 7: ML Frameworks (TF, PyTorch, JAX)

The optimal framework execution strategy depends on which iron law term dominates the workload. Table 7.5 aligns each archetype to its recommended execution strategy: Table 7.5: Framework Execution…

### Lighthouse 7.2: Lighthouse example: Smart Doorbell (TinyML)

[ch07.md](chapters/ch07.md) · Vol 1 · Chapter 7: ML Frameworks (TF, PyTorch, JAX)

The scenario: Deploying the Smart Doorbell's Keyword Spotting (KWS) model to an ARM Cortex-M4 microcontroller with 256 KB of RAM and 1 MB of Flash. The constraint: Astandard PyTorch runtime occupies…

### Lighthouse 8.1: Training GPT-2 XL (1.5B parameters)

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

GPT-2 XL serves as our representative lighthouse example for analyzing large-scale single-node training: * **Parameter Count:** \(1.5 \times 10^9\) (XL size), requiring \(\sim 3\text{ GB}\) in FP16…

### Lighthouse 8.1: Lighthouse example: Training GPT-2

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Whythismodel? GPT-2 (1.5B) serves as our primary case study for large-scale training because it sits at the 'sweet spot' of systems complexity. It is large enough to require distributed training and…

### Lighthouse 9.1: DLRM and embedding deduplication

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

Our DLRMLighthouse model from Section 6.1.1 presents a unique deduplication challenge. Recommendation systems are memory capacity-bound, with embedding tables consuming terabytes of storage for…

### Lighthouse 9.2: Mining for hard negatives

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

The 'Hard Negative' Problem: Our Smart Doorbell faces a classic data selection challenge. The vast majority of its video feed is empty (easy negatives) or clearly people (easy positives). The model…

### Lighthouse 9.3: MobileNet and aggressive augmentation

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

Our MobileNet Lighthouse model from Section 6.1.1 exemplifies how data augmentation compensates for model capacity constraints. MobileNet's depthwise separable convolutions reduce parameters by 8-9 ×…

### Lighthouse 9.4: Lighthouse data selection

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

Data selection principles apply to all five Lighthouse Models, though the priorities differ by bottleneck: | Lighthouse | Primary Bottleneck | Data Selection Priority |…

### Lighthouse 10.1: DLRM and embedding quantization

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

The memory capacity constraint: Our DLRM Lighthouse (Chapter 6) presents a unique compression challenge. Unlike ResNet or GPT, which are constrained by compute or bandwidth, DLRMis constrained by…

### Lighthouse 10.2: The TinyML quantization imperative

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

The energy and storage constraint: Our Smart Doorbell Lighthouse operates at the opposite extreme of the iron law from DLRM. The deployment table used a roughly 512 KB TinyML capacity where the…

### Lighthouse 10.3: Keyword spotting and extreme compression

[ch10.md](chapters/ch10.md) · Vol 1 · Chapter 10: Model Compression (Pruning, Quantization, Distillation)

The extreme constraint: Our Keyword Spotting (KWS) Lighthouse (Chapter 6) lives here. Running on a microcontroller with 256 KB of SRAM means 'standard' compression is not enough. For KWS, INT8…

### Lighthouse 11.1: Amdahl's Law on NVIDIA H100

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

* **ResNet-50 Inference (\(p = 0.95\)):** Assuming an H100 GPU delivers an \(S = 247\times\) speedup over a baseline CPU for matrix math: \[ \text{Speedup} = \frac{1}{(1-0.95) + \frac{0.95}{247}} =…

### Lighthouse 11.2: Life of a Tensor (Keyword Spotting Inference)

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Trace of a 31.2 KB tensor (16,000 samples \(\times\) FP16) through the memory hierarchy of an A100 GPU: 1. **DRAM (HBM):** Tensor starts here. Latency: \(\sim 100\) ns to \(300\) ns. Energy: \(\sim…

### Lighthouse 11.1: Amdahl's Law on H100

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

- ResNet-50 inference on NVIDIA H100: · H100 delivers S = 247 × speedup over CPU for matrix multiply (1,979 TOPS INT8 vs. ~8 TOPS on baseline CPU without AMX extensions) (Speedup = 1 / ((1-0.95) +…

### Lighthouse 11.2: Life of a tensor: The KWS journey

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Recall the one-second audio clip from Chapter 2. Here is its physical path through the hardware during inference: 1. DRAM(HBM) 2. : The tensor starts here. - Size: 16,000 samples 2 bytes (FP16) =…

### Lighthouse 11.3: The case for heterogeneous microcontrollers

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

The extreme edge: The Smart Doorbell (Wake Vision) pushes heterogeneity to its logical limit. Unlike a smartphone SoC with a multi-watt budget, a doorbell camera often runs on a microcontroller with…

### Lighthouse 12.1: MobileNet deployment validation

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Throughout this chapter, we validate the complete optimization pipeline using MobileNetV2 (introduced in Section 6.1.1) as our lighthouse example. MobileNetV2 refines v1's depthwise separable design…

### Lighthouse 12.2: MobileNet on EdgeTPU

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Completing our MobileNet lighthouse example, we validate the hardware acceleration claims from Chapter 11 using MLPerf Tiny scenarios. Note: The following values are illustrative, based on typical…

### Lighthouse 12.3: MobileNet INT8 compression

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Returning to our MobileNet lighthouse example, consider the complete validation protocol for INT8 quantization: Precompression baseline: MobileNetV2 achieves 71.8 percent top-1 accuracy on ImageNet…

### Lighthouse 13.1: Lighthouse example: DLRM serving

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

The scenario: Serving a Deep Learning Recommendation Model (DLRM) with a 10 ms P99 latency budget. The contrast: While ResNet-50's model stage is dominated by convolutional neural network (CNN)…

### Lighthouse 13.2: LLM serving latency targets

[ch13.md](chapters/ch13.md) · Vol 1 · Chapter 13: Model Serving Systems (LLMs, vLLM, Queuing Theory)

Aproduction-grade LLM service typically targets the following SLOs: - TTFT: < 500 ms (for a 1000-token prompt) - TPOT: < 50 ms (equivalent to ~20 tokens/second, faster than human reading speed) -…

### Lighthouse 14.1: Monitoring strategy by archetype

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

The dominant failure modes and monitoring priorities differ across workload archetypes. The following table summarizes how monitoring priorities differ across four representative archetypes. Table…

### Lighthouse 14.2: Uber Michelangelo feature store

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Uber's Michelangelo platform pioneered the feature store concept (Hermann and Balso 2017), addressing training-serving skew across thousands of ML models powering ride pricing, ETA prediction, and…

### Lighthouse 14.3: Google TFX production ML pipelines

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

TensorFlow Extended (TFX) emerged from Google's internal ML infrastructure, productionizing the same pipeline patterns that power Search, Ads, and YouTube recommendations. Origin: Before TFX, Google…

### Lighthouse 14.4: Netflix ML monitoring at scale

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Netflix operates hundreds of ML models powering recommendations, content optimization, and infrastructure management, processing billions of predictions daily across 200+ million subscribers. The…

### Lighthouse 14.5: Oura Ring: Principles summary

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Reproducibility: Versioned wearable and PSG datasets, preprocessing code, feature definitions, and hyperparameters make each model traceable to the exact evidence used to train and evaluate it.…

### Lighthouse 14.6: ClinAIOps: Principles summary

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Reproducibility: Every AI recommendation is logged with complete provenance: input data, model version, confidence scores, and clinician decision. Audit trails enable regulatory review and outcome…

### Lighthouse 15.1: Fairness concerns by archetype

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

The dominant fairness risks differ by workload archetype (introduced in Chapter 2), requiring different evaluation strategies. Table 15.5 maps each archetype to its primary risk and evaluation…

### Lighthouse 1.1: Lighthouse archetypes at scale

[v2_ch01.md](chapters/v2_ch01.md) · Vol 2 · Chapter 1: Introduction to ML Systems

Lighthouse Archetypes are canonical workloads that we track throughout the volume, examining their behavior when distributed across thousands of devices. The full roster with the C 3 taxonomy mapping…

### Lighthouse 2.1: Archetype B (DLRM at Scale): The capacity wall

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

While Archetype A (GPT-4) is primarily throughput-bound (demanding more TFLOPS), Archetype B (DLRM at Scale) -the Deep Learning Recommendation Model (DLRM) workload-is primarily capacity-bound. A 10…

### Lighthouse 4.1: Archetype A (GPT-4/Llama-3): The rail-optimized fleet

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Archetype A (GPT-4) is the primary driver for rail-optimized fabrics. Because it uses 3D Parallelism, it generates two distinct traffic patterns: (1) massive, bandwidth-hungry gradient averaging for…

### Lighthouse 5.1: Archetype B (DLRM at Scale): Feature store latency

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

While Archetype A (GPT-4) deals with static, versioned datasets of trillions of tokens, Archetype B (DLRM at Scale) -the Deep Learning Recommendation Model (DLRM) workload-deals with dynamic,…

### Lighthouse 6.1: Archetype B (DLRM at Scale): DLRM vs. LLM scaling

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

Archetype B (DLRM at Scale) and Archetype A (GPT-4/Llama-3) scale differently. - LLMs (Dense) : Scale via Tensor/Pipeline Parallelism. Constraint: Compute & Interconnect Bandwidth (NVLink). - DLRMs…

### Lighthouse 6.2: Archetype A (GPT-4/Llama-3): Physics of 3D parallelism

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

𝑃 Archetype A (GPT-4/Llama-3) is the primary driver for hybrid parallelism. Because the model parameters (𝑃) exceed the memory of any single accelerator (𝐶 mem,device ) , and the training dataset (𝐷)…

### Lighthouse 6.3: Distributed archetype spectrum

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

The 'optimal point' in the 3D Parallelism Cube shifts depending on the system's primary bottleneck: | Archetype | Primary Partitioning Strategy | The Logic |…

### Lighthouse 7.1: Communication archetype patterns

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

The 'Travel Manifest' for a gradient depends on the system's objective function and constraint regime. Each lighthouse archetype faces a distinct communication challenge, and the techniques developed…

### Lighthouse 10.1: Archetype C (Federated MobileNet): TinyML survival

[v2_ch10.md](chapters/v2_ch10.md) · Vol 2 · Chapter 10: Performance Engineering (Vol 2)

For Archetype C (Federated MobileNet) , quantization is a prerequisite for survival, not an optimization. On a microcontroller with only 512 KB of SRAM, an FP16 model is physically impossible to…

### Lighthouse 11.1: Archetype A (GPT-4/Llama-3): Throughput-latency

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Archetype A (GPT-4/Llama-3) (Section 1.6.1) relies on continuous batching to solve its primary efficiency paradox. The decode phase is memory-bandwidth bound, meaning the GPU compute cores are idle…

### Lighthouse 11.2: Blackwell: The FP4 inference frontier

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

The Blackwell (B200) architecture introduces native FP4 support, which doubles the effective memory bandwidth for the Decode Phase . Because the decode phase is strictly bandwidthbound, shrinking the…

### Lighthouse 11.3: Embedding sharding at Meta

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Meta's recommendation infrastructure demonstrates embedding sharding at extreme scale: Scale: Figure 11.19: Embedding Sharding Strategies: Row-wise sharding places complete embedding vectors on…

### Lighthouse 11.4: Archetype B (DLRM at Scale): The tail at scale

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Archetype B (DLRM at Scale) is the canonical victim of tail latency. Processing 10 million QPS means that a 1-in-10,000 latency spike happens 1,000 times every second. For Archetype B (DLRM at…

### Lighthouse 13.1: Archetype A (GPT-4/Llama-3): Cost of regression

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Archetype A (GPT-4/Llama-3) (Section 1.6.1) faces the 'Generalist's Dilemma.' Because the model serves millions of distinct use cases, a fine-tuning update to improve Python coding might silently…

### Lighthouse 13.2: Archetype B (DLRM at Scale): The staleness tax

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Archetype B (DLRM at Scale) -the Deep Learning Recommendation Model (DLRM) workload-is uniquely sensitive to freshness. Unlike Archetype A (GPT-4/Llama-3) (where grammar rules do not change),…

### Lighthouse 14.1: Archetype C (Federated MobileNet): The need for privacy

[v2_ch14.md](chapters/v2_ch14.md) · Vol 2 · Chapter 14: Security & Privacy (Vol 2)

Archetype C (Federated MobileNet) (Section 1.6.1) represents the class of systems where privacy is a hard constraint, not an optimization. For a fleet of health monitors processing cardiac data,…

### Lighthouse 14.2: Google Gboard federated learning

[v2_ch14.md](chapters/v2_ch14.md) · Vol 2 · Chapter 14: Security & Privacy (Vol 2)

Google's Gboard keyboard, illustrated in Figure 12.2 as a federated learning deployment, demonstrates how security mechanisms layer atop the FL protocol. From a privacy perspective, the system…

### Lighthouse 15.1: Archetype B (DLRM at Scale): Fake profile injection

[v2_ch15.md](chapters/v2_ch15.md) · Vol 2 · Chapter 15: Robust AI

Archetype B (DLRM at Scale) -the Deep Learning Recommendation Model (DLRM) workload-is uniquely vulnerable to a specific form of data poisoning: Fake Profile Injection . Because recommendation…

### Lighthouse 16.1: Archetype A (GPT-4/Llama-3): The energy wall

[v2_ch16.md](chapters/v2_ch16.md) · Vol 2 · Chapter 16: Sustainable AI

Archetype A (GPT-4) is the primary driver of the industry's exponential energy growth. A single 25,000-GPU cluster drawing 700 W per chip requires 17.5 MW of continuous power for training. The…

## War Stories (Production Failures)

*41 entries, in reading order*

### War Story 2.1: The Zillow Offers collapse (2021)

[ch02.md](chapters/ch02.md) · Vol 1 · Chapter 2: Deployment Paradigms (Cloud, Edge, Mobile, TinyML)

Context: Zillow, a real-estate marketplace, launched 'Zillow Offers' to buy homes directly using an algorithmic valuation model ('Zestimate'). Failure: The model was trained on historical data during…

### War Story 4.1: Microsoft Tay (2016)

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Context: Microsoft launched 'Tay,' an AI chatbot designed to learn from user interactions on Twitter in real-time. Failure: The data pipeline ingested user tweets directly into the model's retraining…

### War Story 6.1: The quadratic wall

[ch06.md](chapters/ch06.md) · Vol 1 · Chapter 6: Network Architectures (CNNs, Transformers, RecSys)

Context: When Google released BERT in 2018, it set new accuracy records across 11 NLP benchmarks. However, the engineering team strictly limited the input sequence length to 512 tokens, despite users…

### War Story 7.1: The silent gradient killer

[ch07.md](chapters/ch07.md) · Vol 1 · Chapter 7: ML Frameworks (TF, PyTorch, JAX)

Context: An ML engineer implemented a custom activation function in PyTorch. To save memory, they used an in-place operation such as x += 1 instead of x = x + 1 . Failure: In-place operations modify…

### War Story 8.1: The 3AM gradient explosion

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

The context: Ateam is training a 7B parameter large language model (LLM). The loss curve has been decreasing smoothly for four days. The engineers leave for the night. The failure: At 3:00 AM, the…

### War Story 8.2: The GIL-locked GPU

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Context: Aresearch lab purchased a \$100,000 GPU cluster to accelerate training. They wrote their data loading pipeline in standard Python, using a simple loop to read images, augment them, and feed…

### War Story 9.1: The test set leak

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

Context: For years, ImageNet and CIFAR-10 were the gold standards for computer vision. Researchers competed to squeeze every 0.1 percent accuracy gain, assuming higher scores meant better…

### War Story 9.2: The 99 percent sparsity trap

[ch09.md](chapters/ch09.md) · Vol 1 · Chapter 9: Data Selection & Active Learning

Context: Researchers at Google Brain investigated the impact of pruning on model performance. They pruned a ResNet model to 90 percent+ sparsity, removing the vast majority of weights. Failure: They…

### War Story 11.1: The 0 percent Tensor Core mystery

[ch11.md](chapters/ch11.md) · Vol 1 · Chapter 11: Hardware Acceleration, Compilers & SoCs

Consequence: Tensor Cores on A100s only trigger for specific precision formats (FP16, BF16, or TF32). By forcing FP32 accumulation in a way the hardware did not support for acceleration, the code…

### War Story 12.1: The tail latency death

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Context: Discord, a real-time chat platform, used Go for its core services. The system required low latency for millions of concurrent users. Failure: Engineers observed massive latency spikes every…

### War Story 12.2: The JSON serialization trap

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Context: Researchers at Berkeley developed Clipper, a low-latency model serving system. They benchmarked standard serving approaches using Python-based web servers. Failure: They found that for…

### War Story 14.1: The Knight Capital error (2012)

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Context: Knight Capital Group was a major market maker in US equities. In 2012, they deployed new software to seven of eight servers but missed the 8th. 13 Containerization for ML Deployment: Docker…

### War Story 14.2: The zombie feature

[ch14.md](chapters/ch14.md) · Vol 1 · Chapter 14: ML Operations (MLOps, Drift, Edge Fleets)

Context: Google engineers analyzed a large-scale ad-click prediction model that had been in production for years. Failure: They discovered a feature ('Feature X') that had been deprecated in the…

### War Story 15.1: The click-bait death spiral

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

Context: In 2018, Facebook's News Feed algorithm was optimized heavily for 'time spent' and 'clicks.' Failure: The model learned that sensationalist, divisive, and 'click-bait' content generated the…

### War Story 15.2: The proxy variable trap

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

Context: Optum, a healthcare services company, developed an algorithm to identify patients with complex health needs for enrollment in a high-risk care management program. Failure: The model used…

### War Story 15.3: The automation paradox

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

Context: Uber's Advanced Technologies Group (ATG) was testing self-driving cars in Arizona. The system was designed with a 'safety driver' to take over if the AI failed. Failure: The AI system…

### War Story 15.4: The Clever Hans effect

[ch15.md](chapters/ch15.md) · Vol 1 · Chapter 15: Responsible Engineering & Compliance

Context: Researchers at Mount Sinai Hospital trained a neural network to detect pneumonia in chest X-rays (Rajkomar et al. 2019). The model achieved superhuman accuracy on the test set. Failure: When…

### War Story 2.1: The TPU origin story

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

In 2013, Google engineers projected that if users spoke to their Android phones for just three minutes per day using voice search, the company would need to double its data center compute capacity to…

### War Story 2.2: The NVLink bandwidth surprise

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

Early users of multi-GPU nodes often attempted tensor parallelism over PCIe, expecting the 64 GB/s bandwidth to suffice. In practice, tensor parallelism requires AllReduce after every Transformer…

### War Story 2.3: The power ramp crash

[v2_ch02.md](chapters/v2_ch02.md) · Vol 2 · Chapter 2: Compute Infrastructure

In one of the early large-scale training deployments, a 512-GPU cluster experienced intermittent node failures during the first week of operation. The failures occurred at random intervals, with no…

### War Story 4.1: The PFC storm that froze a cluster (2022)

[v2_ch03.md](chapters/v2_ch03.md) · Vol 2 · Chapter 3: Network Fabrics

Context: Alarge RoCE-based training cluster connected over 4,096 GPUs through a standard 400 GbE fabric with Priority Flow Control enabled for lossless RDMA. Failure: Asingle malfunctioning…

### War Story 5.1: The invisible tax

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

Amajor cloud provider invested heavily in a 4,096-GPU cluster for a flagship large language model (LLM) training service. Despite top-tier hardware, the team struggled to exceed 68 percent Model…

### War Story 6.1: The linear scaling rule discovery

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

In 2017, Facebook AI Research shattered the 'batch size ceiling' by training ResNet-50 on ImageNet in just one hour using 256 GPUs. Prior to this, increasing batch size 𝐵 beyond a few hundred…

### War Story 6.2: Linear scaling warmup

[v2_ch06.md](chapters/v2_ch06.md) · Vol 2 · Chapter 6: Distributed Training Systems

𝜂 𝑡 =𝜂 base + 𝑡 𝑊 (𝑘⋅𝜂 base -𝜂 base ) for 𝑡 < 𝑊 The warmup period allows the model to reach a region of the loss landscape where large learning rates are stable. Typical warmup lengths are 5 epochs…

### War Story 7.1: NCCL topology discovery

[v2_ch07.md](chapters/v2_ch07.md) · Vol 2 · Chapter 7: Collective Communication

Asoftware library running deep inside a GPU must determine whether another GPU sits on a local NVLink switch or 100 meters away across an InfiniBand fabric. NVIDIA's Collective…

### War Story 8.1: The checkpoint storm

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

For the 2.1 TB Archetype A checkpoint above, 1,000 workers would each write roughly 2.1 GB of state. The same mechanism becomes catastrophic in embedding-heavy recommendation or trillion-parameter…

### War Story 8.2: The recommendation fallback

[v2_ch08.md](chapters/v2_ch08.md) · Vol 2 · Chapter 8: Fault Tolerance and Reliability (Vol 2)

Resilience is not always about restoring the primary system; sometimes it is about graceful degradation. During a major data center outage, a leading e-commerce platform's complex deep learning…

### War Story 9.1: The silent switch failure

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

A major research lab spent a week debugging a 30 percent performance regression in their flagship foundation model training run. The GPUs were healthy, the code was unchanged, and the job was placed…

### War Story 9.2: The spot market crash

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

A major AI lab configured their entire research fleet to use spot instances in a single cloud region to save costs. Two days before a top-tier conference deadline, a massive wave of lastminute…

### War Story 9.3: The scheduler that optimized the wrong metric

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Aplatform team at a major autonomous vehicle company deployed a custom scheduler designed to minimize average job completion time (JCT), a standard academic metric. The logic was sound: by…

### War Story 9.4: The quota hoarding incident

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

A computer vision team at a major logistics company reserved a block of 500 GPUs for a 'critical' urgent model refresh. Due to upstream data delays, the training jobs were postponed, but the team…

### War Story 10.2: Benchmark vs. reality: The hero run tax

[v2_ch10.md](chapters/v2_ch10.md) · Vol 2 · Chapter 10: Performance Engineering (Vol 2)

Industry benchmarks like MLPerf are often 'hero runs'-highly tuned configurations where logging is disabled, safety checks are bypassed, and the hardware is freshly rebooted. In production, achieved…

### War Story 11.1: The ChatGPT traffic spike

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

When ChatGPT scaled from zero to 100 million users in two months, the engineering challenge shifted from model quality to survival. The system faced an unprecedented 'cold start' problem:…

### War Story 11.2: The continuous batching revolution

[v2_ch11.md](chapters/v2_ch11.md) · Vol 2 · Chapter 11: Inference at Scale (Vol 2)

Before late 2022, LLM serving was plagued by the 'straggler problem.' Frameworks used static batching, meaning the GPU had to wait for the longest sequence in a batch to finish generation before…

### War Story 12.1: Apple's on-device keyboard learning

[v2_ch12.md](chapters/v2_ch12.md) · Vol 2 · Chapter 12: Edge Intelligence (Vol 2)

Apple's QuickType keyboard represents one of the largest deployments of federated learning in history. The system updates next-word prediction models across billions of devices without raw keystrokes…

### War Story 13.1: The silent model regression

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

In a famous incident at a major e-commerce platform, a product ranking model passed all offline validation gates but caused a 1.2 percent revenue drop in production. The culprit was a silent failure…

### War Story 13.2: The feature pipeline cascade

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Aplatform team once updated the normalization logic for a 'User Engagement Score' feature, switching from a 30-day z-score to a 7-day min-max scale to better capture trends. They updated the feature…

### War Story 14.1: The BERT model extraction

[v2_ch14.md](chapters/v2_ch14.md) · Vol 2 · Chapter 14: Security & Privacy (Vol 2)

Researchers demonstrated that proprietary models behind APIs are vulnerable to functional extraction. By querying a victim BERT-based API with just 2 million carefully crafted inputs (costing roughly…

### War Story 15.1: The stop sign attack

[v2_ch15.md](chapters/v2_ch15.md) · Vol 2 · Chapter 15: Robust AI

In a striking demonstration of physical adversarial examples, researchers fooled a state-of-theart object detector into classifying a Stop sign as a Speed Limit 45 sign using only black and white…

### War Story 17.1: Apple Card: The cost of missing explanations

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

In 2019, Apple and Goldman Sachs faced intense public scrutiny when prominent tech leaders, including Steve Wozniak, reported receiving credit limits 10 × lower than their spouses despite having…

### War Story 17.2: The algorithmic grading failure

[v2_ch17.md](chapters/v2_ch17.md) · Vol 2 · Chapter 17: Responsible Engineering (Vol 2)

In 2020, following the cancellation of A-level exams due to the COVID-19 pandemic, Ofqual (the qualifications regulator for England) deployed an algorithmic standardization model to assign grades.…

## Principles (Invariants and Laws)

*20 entries, in reading order*

### Principle 4: The Silicon Contract

[ch04.md](chapters/ch04.md) · Vol 1 · Chapter 4: Data Engineering & Pipeline Architecture

Invariant: Every model architecture and workload regime makes an implicit commitment to the hardware, a wager on which resource it will saturate first. - 𝐷 / · DLRM assumes massive embedding tables…

### Principle 5: The Pareto Frontier

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Invariant: Optimization is not a single-objective problem. It is a multi-dimensional search for the Pareto frontier-the boundary where no metric can be improved without degrading at least one other.…

### Principle 8: Amdahl's Law

[ch08.md](chapters/ch08.md) · Vol 1 · Chapter 8: Staged Model Training & Parallelism

Invariant: The maximum speedup of a system is limited by the fraction of the workload that cannot be accelerated (Amdahl 1967). where 𝑝 is the parallelizable fraction and 𝑠 is the speedup of that…

### Principle 9: The Verification Gap Invariant

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

> **Invariant:** In traditional software, verification checks whether \(f(x) = y\). In machine learning systems, verification checks statistical bounds: > \[ > \Pr(f(X) \approx Y) > 1 - \epsilon > \]…

### Principle 10: The Statistical Drift Invariant

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

> **Invariant:** Machine learning systems fail silently when the production data distribution drifts from the training data distribution. This accuracy decay is modeled as: > \[ > \text{Accuracy}(t)…

### Principle 11: The Training-Serving Skew Law Invariant

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

> **Invariant:** If the function computed during serving (\(f_{\text{serve}}\)) diverges from the function learned during training (\(f_{\text{train}}\)), the model's effective accuracy degrades…

### Principle 12: The Latency Budget Invariant

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

> **Invariant:** In interactive serving, systems must optimize throughput within a strict tail-latency constraint defined by a Service Level Objective (SLO). Latency is governed by: > \[ >…

### Principle 13: The Bias Feedback Invariant

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

> **Invariant:** When a model's outputs influence the distribution of its future inputs, prediction errors compound across decision cycles. For a self-reinforcing feedback loop, the disparity…

### Principle 10: The Statistical Drift Invariant

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Consider a credit scoring model trained on 2020 borrower behavior. Two years later, inflation rises, interest rates change, and lending policies shift. The system still produces scores, but the…

### Principle 13: The Bias Feedback Invariant

[ch12.md](chapters/ch12.md) · Vol 1 · Chapter 12: Benchmarking Systems & Power Measurement

Consider a loan approval model that denies credit at higher rates to applicants from historically underserved communities. Denied applicants cannot build credit history, which makes future…

### Principle 10: The Distributed Step Time Law (Iron Law of Scale)

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

\[ T_{\text{step}}(N) = \frac{T_{\text{compute}}}{N} + T_{\text{comm}}(N) - T_{\text{overlap}} \] Implication: Scaling is a race between parallelizable compute (which shrinks with 𝑁 under ideal…

### Principle 13: The Conservation of Overhead

[v2_ch05.md](chapters/v2_ch05.md) · Vol 2 · Chapter 5: Data Storage — The Fuel Line

Invariant: Overheadinadistributed ML system cannot be eliminated, only redistributed among Compute, Communication, and Coordination (the C 3 taxonomy). Reducing one necessarily increases at least one…

### Principle 14: The Autoregressive Bottleneck

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Invariant: In low-batch dense transformer decode, throughput is memory-bandwidth bound because the model weights must be streamed across the device for every generated token . Higher batch sizes…

### Principle 15: The Serving Cost Dominance Law

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Invariant: For high-traffic production models, cumulative inference cost can exceed the onetime training cost. Implication: Inference efficiency often becomes the dominant lifecycle optimization…

### Principle 16: The Power of Two Choices (P2C)

[v2_ch09.md](chapters/v2_ch09.md) · Vol 2 · Chapter 9: Fleet Orchestration (Vol 2)

Invariant: Under an idealized balls-into-bins model, querying just two random replicas and selecting the least-loaded one reduces the maximum load on any replica from Θ( log 𝑛/ loglog 𝑛) to Θ( loglog…

### Principle 17: The Information Leakage Invariant

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Invariant: Every model output potentially leaks information about its training data. Perfect privacy is mathematically impossible if the model remains useful. 𝐼( TrainingData; ModelOutput ) > 0…

### Principle 18: The Robustness Compute Penalty

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Implication: There is no 'free' robustness. Building secure models is computationally expensive. For many applications, it is more efficient to rely on external guardrails (input filtering, output…

### Principle 19: The Jevons Paradox of AI (Efficiency Trap)

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Invariant: Improvements in efficiency that lower the cost of a resource will tend to increase, rather than decrease, the total consumption of that resource. Efficiency ↑ ⟹ Cost ↓ ⟹ Demand ↑↑…

### Principle 20: The Fairness Impossibility Law

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Invariant: For nonperfect classifiers operating on groups with different base rates, Calibration, Equalized Odds, and Demographic Parity cannot be satisfied simultaneously. 𝑃(𝑌 = 1|𝐴 = 𝑎) ≠ 𝑃(𝑌 = 1|𝐴…

### Principle 21: The Sociotechnical Feedback Invariant

[v2_ch13.md](chapters/v2_ch13.md) · Vol 2 · Chapter 13: ML Operations at Scale

Implication: Systems require Closed-Loop Governance . Amodel that maximizes accuracy on static test data can still degrade the future data distribution it operates on, amplify incentives that bias…
