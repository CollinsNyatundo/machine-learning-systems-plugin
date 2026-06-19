# Architectural Design Patterns for ML Systems

This directory compiles production-proven architectural and engineering design patterns for machine learning pipelines, training infrastructure, optimization workflows, and serving engines.

---

## Serving & Inference Patterns

### 1. Continuous Batching (Iteration-Level Scheduling)
* **Problem**: Standard batching groups requests and waits for all of them to finish generating before returning outputs. In LLM generation, sequence lengths vary widely, meaning short requests are held hostage by the longest sequence, leading to accelerator underutilization.
* **Solution**: Schedule at the iteration level rather than request level. Once a token is generated for a sequence, evaluate if a new request can join the batch or if a finished request can exit.
* **Diagram**:
  ```
  Traditional: [Req 1 (3 tokens), Req 2 (5 tokens)] -> Runs for 5 iterations, Req 1 sits idle.
  Continuous:  [Req 1, Req 2] -> Iteration 3: Req 1 finishes -> Req 3 injected immediately.
  ```

### 2. Virtual Memory for KV Cache (PagedAttention)
* **Problem**: The Key-Value (KV) cache grows dynamically with sequence length. Pre-allocating contiguous memory blocks for the maximum context length causes massive memory fragmentation and limits serving capacity (up to 60-80% memory waste).
* **Solution**: Divide the KV cache into fixed-size physical pages. Use a lookup table (Page Table) to map logical KV cache pages to non-contiguous physical pages.
* **Impact**: Decreases memory waste to near 0%, allowing batch size increases of 2-4x on the same hardware.

### 3. Hybrid Edge-Cloud Serving
* **Problem**: Edge devices provide zero-latency local execution but lack the compute capacity for large, highly accurate models. Cloud servers offer full capacity but introduce network latency and privacy risks.
* **Solution**: Implement a cascade model. A lightweight model runs locally on the edge. If the local prediction confidence is below a defined threshold \(\theta\), the request (or intermediate feature representations) is routed to a larger cloud model for final inference.
* **Formula**:
  \[\text{Final Prediction} = \begin{cases} f_{\text{edge}}(x) & \text{if } \text{confidence}(f_{\text{edge}}(x)) \ge \theta \\ f_{\text{cloud}}(x) & \text{otherwise} \end{cases}\]

---

## Training & Scaling Patterns

### 4. Gradient Accumulation
* **Problem**: Training with large batch sizes is critical for model convergence, but accelerator memory limits the physical batch size that can fit on-chip.
* **Solution**: Split a logical batch size \(B\) into \(N\) mini-batches of size \(b\), where \(B = N \times b\). Run forward and backward passes sequentially for each mini-batch, accumulating gradients without updating weights. Run the optimizer update step only after all \(N\) steps.
* **Benefits**: Simulates large batch sizes without extra memory, trading sequential compute time for size scalability.

### 5. Pipeline Parallelism (GPipe)
* **Problem**: Extremely large models exceed the memory of a single accelerator chip, requiring partition across multiple chips. Serialized layer processing creates massive processor idle time ("bubbles").
* **Solution**: Partition the model's layers sequentially across a 1D chain of accelerators. Divide the training batch into micro-batches and pipeline them through the chips.
* **Bubble Ratio**:
  \[\text{Idle Fraction} \approx \frac{K - 1}{M + K - 1}\]
  where \(K\) is the number of accelerator stages and \(M\) is the number of micro-batches. Larger \(M\) relative to \(K\) reduces the bubble but increases activation storage requirements.

---

## Data & MLOps Patterns

### 6. Active Learning Loop (Data Selection)
* **Problem**: Labeling raw data is expensive and time-consuming. Randomly labeling data leads to diminishing returns and suboptimal RoC.
* **Solution**: Build a closed loop. Train a baseline model. Run inference on unlabeled pools. Use an acquisition function (e.g., entropy, variance, or margin sampling) to select the samples with the highest model uncertainty. Route only these samples to human labelers.
* **Loop**:
  ```
  [Unlabeled Pool] -> [Inference & Uncertainty Filter] -> [Labeling Pipeline] -> [Training Set] -> [Model Retrain]
  ```

### 7. Dual Feature Serving (Online-Offline Consistency)
* **Problem**: Training-serving skew occurs when features used during training differ in calculation logic from features computed at serving time.
* **Solution**: Use a Feature Store with unified ingestion pipelines:
  * **Offline Store (Parquet/BigQuery)**: Stores historical feature versions for batch training.
  * **Online Store (Redis/Spanner)**: Stores low-latency key-value lookups of the latest feature values.
  A single feature definition script compiles feature logic for both destinations.

---

## Distributed Training & Infrastructure Patterns

### 8. Zero Redundancy Memory Partitioning (ZeRO / FSDP)
* **Problem**: Storing weights, gradients, and optimizer states (Adam requires 14 bytes/parameter) for large models exhausts GPU memory. Replicating model states across all data-parallel ranks restricts the model size that can fit on-chip.
* **Solution**: Instead of replicating model states, shard them across data-parallel ranks. Reconstruct the required state on-demand during the forward and backward passes using collective operations:
  * **ZeRO-1**: Shards optimizer states (saves $\approx 4\times$ memory).
  * **ZeRO-2**: Shards optimizer states and gradients (saves $\approx 8\times$ memory).
  * **ZeRO-3 (FSDP)**: Shards parameters, optimizer states, and gradients (memory footprint scales as $\frac{\text{Model Size}}{N}$).
* **Impact**: Enables training trillion-parameter models without complex model parallelism partitions.

### 9. Asynchronous Double Buffering (Compute-Communication Overlap)
* **Problem**: Synchronous collective operations (e.g., waiting for AllReduce to complete after the backward pass) stall compute engines (GPUs/TPUs), leaving them idle and reducing MFU.
* **Solution**: Overlap communication with computation. During training, partition the gradient tensor into smaller buckets. As soon as a bucket's gradients are computed during the backward pass, launch an asynchronous AllReduce collective on a separate network stream while the GPU continues backpropagating earlier layers.
* **Impact**: Eliminates visible communication latency, converting sequential step time $T_{\text{comp}} + T_{\text{comm}}$ to $\max(T_{\text{comp}}, T_{\text{comm}})$.

---

## Distributed Serving Patterns

### 10. Speculative Decoding Cascade
* **Problem**: Autoregressive decode in LLM serving is memory-bandwidth-bound (moving parameters from HBM to SRAM for every single generated token), leading to low GPU FLOPs utilization (often $<5\%$ MFU).
* **Solution**: Use a draft model / target model cascade. A lightweight draft model ($M_{\text{draft}}$, e.g., 1.5B parameters) generates $K$ candidate tokens quickly. A larger target model ($M_{\text{target}}$, e.g., 70B parameters) evaluates all $K$ candidates in a single parallel forward pass (compute-bound).
* **Impact**: Achieves $2\text{--}3\times$ latency reduction for serving large models. The number of accepted tokens determines the overall speedup.

### 11. Prefill-Decode Phase Splitting (Splitwise)
* **Problem**: The prefill phase of LLM serving (processing prompt tokens) is highly compute-bound and utilizes GPU Tensor Cores efficiently, while the decode phase (generating tokens one-by-one) is memory-bandwidth-bound. Mixing both phases on the same GPU causes scheduling interference and memory fragmentation.
* **Solution**: Partition the serving cluster into dedicated prefill nodes and decode nodes. Prefill nodes process incoming prompts, construct the initial Key-Value (KV) cache, and transfer the KV cache tensors to decode nodes, which handle token generation.
* **Impact**: Optimizes hardware mapping. Prefill nodes run on compute-heavy GPUs, while decode nodes run on high-bandwidth-memory nodes.

---

## Governance & Sustainability Patterns

### 12. SISA Sharding for Machine Unlearning
* **Problem**: Complying with deletion requests (e.g., GDPR "Right to be Forgotten") requires removing a user's data from a model's weights. Retraining a model from scratch is computationally prohibitive.
* **Solution**: Apply the Sharded, Isolated, Sliced, and Aggregated (SISA) pattern:
  * Divide the dataset into $S$ independent shards.
  * Train an isolated sub-model on each shard.
  * Within each shard, slice the data and train incrementally.
  * Aggregate sub-model predictions at serving time.
  When a deletion request is received, only the single affected shard's sub-model must be retrained from the checkpoint before the target user's slice, saving up to $99\%$ of retraining compute.

### 13. Carbon-Aware Spatial-Temporal Scheduling
* **Problem**: Running large training runs on coal-heavy grids emits hundreds of tonnes of $CO_2$.
* **Solution**: Implement spatial-temporal scheduling:
  * **Temporal scheduling**: Pause non-urgent training jobs and resume when local grid carbon intensity drops (e.g., peak solar/wind hours).
  * **Spatial scheduling**: Route training tasks to datacenters located in low-carbon regions (e.g., hydro-dominant grids in Quebec or Norway).
* **Impact**: Lowers carbon emissions by up to $80\times$ without altering training code.

