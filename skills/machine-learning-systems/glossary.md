# Machine Learning Systems Glossary

A comprehensive reference for core definitions, paradigms, metrics, and hardware concepts in machine learning systems engineering.

---

## Core Economic & Performance Metrics

### Return on Compute (RoC)
The primary economic invariant of machine learning systems engineering. It measures the utility or accuracy gained per unit of compute resource spent:
\[\text{RoC} = \frac{\Delta \text{Model Accuracy}}{\text{Total FLOPs spent on Training/Inference}}\]
Maximizing RoC is the ultimate goal when trading off model size, accuracy, and operational cost.

### Arithmetic Intensity
The ratio of floating-point operations (compute) performed per byte of data transferred from high-bandwidth memory (HBM) or memory systems:
\[I = \frac{\text{FLOPs}}{\text{Bytes Transferred}}\]
* **Compute-Bound**: When a workload's arithmetic intensity exceeds the hardware's device balance (Roofline threshold), execution speed is limited by the processor's compute speed.
* **Memory-Bound**: When arithmetic intensity is below the device balance, execution speed is limited by memory bandwidth.

### The Iron Law of ML Systems
The system capacity constraints that state model performance degration and energy correlates with model size and precision:
* **The Degradation Equation**: Models lose performance or accuracy when compressed beyond their overparameterization boundary.
* **The Energy Corollary**: Power consumption scales with memory traffic; moving data consumes significantly more energy than computing on it.

---

## Data Engineering Terms

### Data Gravity
The concept that data accumulates over time, attracting applications and compute resources closer to it due to the high latency and cost of transferring large datasets over networks.

### Data Cascade
Sequential and compounded errors in downstream model behavior caused by underlying data quality issues, labeling errors, or collection biases in upstream data pipelines.

### Feature Store
A centralized data management layer that registers, transforms, serves, and monitors features for both offline training (batch) and online inference (low latency).

---

## Model Optimization & Compression

### Quantization
The process of mapping continuous high-precision values (e.g., FP32) to lower-precision, discrete values (e.g., FP16, BF16, INT8, INT4) to reduce memory footprint and latency:
* **Post-Training Quantization (PTQ)**: Quantizing weights and activations after model training using a small calibration dataset.
* **Quantization-Aware Training (QAT)**: Simulating quantization noise during the forward pass of training so the optimizer can adapt weights to maintain accuracy.

### Pruning
The removal of redundant weight parameters or connections from a neural network:
* **Unstructured Pruning**: Removing individual weights based on magnitude. Results in sparse tensors that are difficult to accelerate on dense GPUs without custom kernel support.
* **Structured Pruning**: Removing entire channels, attention heads, or layers. Directly speeds up execution on standard hardware but may cause larger accuracy drops.

### Knowledge Distillation
A compression technique where a smaller student network is trained to replicate the soft output probabilities (logits) or internal representations of a larger, highly accurate teacher network.

---

## Serving & Infrastructure

### Continuous Batching
An iteration-level serving technique where incoming requests are dynamically inserted into the running batch at the token level, rather than waiting for the entire batch to finish generating. This dramatically improves throughput for LLM serving.

### PagedAttention
An algorithm that manages Key-Value (KV) cache memory by allocating it in non-contiguous virtual pages (similar to page tables in operating systems), preventing fragmentation and memory waste.

### Roofline Model
A visual performance model that charts execution speed (FLOPs/sec) against arithmetic intensity (FLOPs/byte) to determine whether a workload is compute-bound or memory-bound on a given hardware accelerator.

### Accelerator Bubble
Idle clock cycles on accelerators (GPUs/TPUs) caused by synchronization barriers, serialized data ingestion pipelines, or pipeline stalls in model-parallel training.

---

## Distributed ML & Fleet Infrastructure

### 3D Parallelism
The combination of three orthogonal parallelism strategies to train massive models: Data Parallelism (DP) for scaling throughput, Tensor Parallelism (TP) for splitting individual layers within a node, and Pipeline Parallelism (PP) for partitioning layers across nodes.

### ZeRO (Zero Redundancy Optimizer)
A memory optimization paradigm that eliminates memory redundancy in data-parallel training by sharding optimizer states (ZeRO-1), gradients (ZeRO-2), and model parameters (ZeRO-3) across ranks rather than replicating them.

### FSDP (Fully Sharded Data Parallel)
An implementation of ZeRO-3 in PyTorch that shards model parameters, gradients, and optimizer states across data-parallel ranks, reconstructing them dynamically during the forward and backward passes using AllGather and ReduceScatter collective operations.

### Clos Topology (Fat-Tree)
A non-blocking, multi-stage network switch architecture that provides maximum bisection bandwidth across a cluster, ensuring that any GPU can communicate with any other GPU at full link speed without switch congestion.

### Hockney Model
A network communication cost model that predicts the time to transfer $M$ bytes between two ranks using startup latency ($\alpha$) and link bandwidth ($\beta$):
\[T(M) = \alpha + \frac{M}{\beta}\]

### RDMA (Remote Direct Memory Access)
A networking technology that allows direct data transfer between the memories of two nodes (e.g., GPU to GPU) without involving the host operating system or CPU, minimizing latency and processing overhead.

### GPUDirect RDMA
An NVIDIA technology that enables direct data transfer between GPU memory and network adapters (NICs) over PCIe, bypassing host system memory and host CPU entirely.

### Priority Flow Control (PFC)
A link-level flow control mechanism in Converged Ethernet (RoCE) that applies pause frames to individual traffic priorities to prevent packet drops and buffer overflows, enabling a lossless fabric.

### DCQCN (Data Center Quantized Congestion Notification)
A congestion control protocol designed for RoCE v2 fabrics that uses Explicit Congestion Notification (ECN) and congestion marking to throttle sender rates, preventing PFC-induced pause storms and head-of-line blocking.

---

## Governance & Responsible Engineering

### SISA (Sharded, Isolated, Sliced, and Aggregated)
A framework for machine unlearning that shards training data into isolated chunks and trains sub-models incrementally. When a user requests data deletion, only the affected shard's sub-model must be retrained, reducing re-training compute costs by $90\text{--}99\%$.

### Differential Privacy (DP-SGD)
A mathematically rigorous privacy framework that limits the leakage of individual training records by clipping gradients and adding calibrated noise during training, bounding the privacy budget ($\epsilon$).

### RLHF (Reinforcement Learning from Human Feedback)
An alignment paradigm that fine-tunes LLMs to match human preferences. It trains a reward model on pairwise comparisons and uses Reinforcement Learning (PPO or DPO) to optimize the LLM output.

### The Responsibility Tax (Alignment Tax)
The additional system resource costs—increased training FLOPS, larger memory footprints, higher serving latencies, or degraded base-model benchmark accuracies—paid to enforce safety, privacy, explainability, or fairness constraints.

