# ML Systems Napkin Math & Hardware Cheatsheet

A quick-reference sheet for systems capacity planning, model size estimation, and hardware specifications.

---

## 1. Key Estimations & Equations

### Transformer Memory Footprint (Weights & Training)
For a model with \(P\) parameters:
* **Model Weights**:
  * FP32: \(4 \times P\) bytes
  * FP16 / BF16: \(2 \times P\) bytes
  * INT8 / FP8: \(1 \times P\) bytes
  * INT4: \(0.5 \times P\) bytes
* **Optimizer States (AdamW)**:
  * FP32 states + FP32 master weights: \(12 \times P\) bytes (mixed-precision training)
* **Gradients**:
  * FP32: \(4 \times P\) bytes
  * FP16 / BF16: \(2 \times P\) bytes
* **Total Training Memory (excl. activations)**:
  * Mixed-precision AdamW: \(\approx 16 \times P\) bytes (plus activation memory, model partitions, and workspace overhead)

### Training & Inference Compute (FLOPs)
For a model with \(P\) parameters processing \(T\) tokens:
* **Training (Forward + Backward Pass)**:
  * \(\text{Compute} \approx 6 \times P \times T\) FLOPs
* **Inference (Forward Pass Only)**:
  * \(\text{Compute} \approx 2 \times P \times T\) FLOPs

### LLM KV Cache Size
For a batch size \(B\), sequence length \(S\), layer count \(L\), hidden dimension size \(H\), and number of key-value heads \(H_{KV}\) (in multi-query/grouped-query attention):
\[\text{KV Cache Memory (Bytes)} = 2 \times B \times S \times L \times H \times \left(\frac{H_{KV}}{H_{\text{attn}}}\right) \times (\text{bytes per element})\]
Typically, for BF16, this is:
\[\text{KV Cache Size} = 4 \times B \times S \times L \times H_{KV} \times d_{\text{head}} \text{ bytes}\]
where \(d_{\text{head}} = H / H_{\text{attn}}\).

---

## 2. Hardware Specifications

| Hardware Accelerator | Peak FP16/BF16 Tensor Core Performance | Peak Memory Bandwidth | High-Bandwidth Memory (HBM) Capacity | Thermal Design Power (TDP) |
|----------------------|----------------------------------------|-----------------------|-------------------------------------|----------------------------|
| **NVIDIA A100 (SXM4)**| 312 TFLOPs                             | 2.0 TB/s (HBM2e)      | 80 GB                               | 400W                       |
| **NVIDIA H100 (SXM5)**| 989 TFLOPs                             | 3.35 TB/s (HBM3)      | 80 GB                               | 700W                       |
| **NVIDIA B200 (SXM)** | 2,250 TFLOPs                           | 8.00 TB/s (HBM3e)     | 192 GB                              | 1000W                      |
| **AMD MI300X**       | 1,307 TFLOPs                           | 5.30 TB/s (HBM3)      | 192 GB                              | 750W                       |
| **Google TPU v4**    | 275 TFLOPs                             | 1.2 TB/s (HBM2)       | 32 GB                               | \~300W                     |
| **Google TPU v5e**   | 197 TFLOPs (BF16)                      | 819 GB/s (HBM2)       | 16 GB                               | \~150W                     |
| **Google TPU v6**    | 918 TFLOPs (BF16)                      | 1.60 TB/s (HBM3)      | 32 GB                               | \~600W                     |

---

## 3. Napkin Math Constants (Energy & Latency)

### The Memory Access Tax (Energy Cost Ratio)
Data movement is the primary driver of energy consumption in deep learning hardware:
* **SRAM Access (On-Chip)**: \(\approx 1 \times\) base energy cost.
* **FP32 Multiply-Accumulate (MAC)**: \(\approx 5 \times\) SRAM access cost.
* **DRAM / HBM Access (Off-Chip)**: \(\approx 100 \times\) to \(200 \times\) compute cost!

### The Latency Cost of the Memory Wall
* **On-chip SRAM cache latency**: \(\approx 1 - 5\) ns
* **HBM / DRAM memory latency**: \(\approx 100 - 200\) ns (two orders of magnitude slower)
* **PCIe Gen 4 bus transfer speed**: 64 GB/s (system memory to GPU)
* **PCIe Gen 5 bus transfer speed**: 128 GB/s
* **NVLink 4 bandwidth**: 900 GB/s (peer GPU interconnect)
* **InfiniBand NDR port bandwidth**: 50 GB/s (inter-node interconnect)

---

## 4. Single-Machine Roofline Model

The execution performance \(P\) of a model on a device is bounded by:
\[P \le \min \left( P_{\text{peak}}, I \times B_{\text{mem}} \right)\]
where:
* \(P_{\text{peak}}\) is the peak compute performance of the hardware (FLOPs/sec).
* \(B_{\text{mem}}\) is the peak memory bandwidth of the hardware (Bytes/sec).
* \(I\) is the Arithmetic Intensity of the workload (FLOPs/Byte).

The **Device Balance** (turning point) is:
\[I_{\text{balance}} = \frac{P_{\text{peak}}}{B_{\text{mem}}}\]
For NVIDIA H100:
\[I_{\text{balance}} = \frac{989 \times 10^{12} \text{ FLOPs/s}}{3.35 \times 10^{12} \text{ Bytes/s}} \approx 295 \text{ FLOPs/Byte}\]
Workloads with \(I < 295\) are memory-bound; workloads with \(I > 295\) are compute-bound.

---

## 5. Distributed Systems & Fleet Equations

### Hockney Network Model (Latency-Bandwidth)
The time to transfer a message of \(M\) bytes between two nodes:
\[T(M) = \alpha + \frac{M}{\beta}\]
where \(\alpha\) is the startup latency (seconds) and \(\beta\) is the link bandwidth (bytes/sec).
The **Crossover Message Size** where latency and bandwidth contribute equally:
\[M_{\text{cross}} = \alpha \times \beta\]

### Collective Operation Complexity (Ring AllReduce)
The time to run a ring AllReduce across \(N\) ranks for a message of \(M\) bytes:
\[T_{\text{ring\_AllReduce}} = 2 \left( \frac{N-1}{N} \right) \frac{M}{\beta} + 2(N-1)\alpha\]
For large \(N\), the bandwidth term approaches \(\frac{2M}{\beta}\) per node.

### Cluster MTBF (Series Failure Model)
For a cluster of \(N\) nodes, where each node has a Mean Time Between Failures of \(\text{MTBF}_{\text{node}}\):
\[\text{MTBF}_{\text{cluster}} = \frac{\text{MTBF}_{\text{node}}}{N}\]
The probability of at least one failure during a job of duration \(T_{\text{job}}\) is:
\[P(\ge 1\text{ failure}) = 1 - e^{-\frac{T_{\text{job}}}{\text{MTBF}_{\text{cluster}}}}\]

### Young-Daly Checkpoint Interval
The mathematically optimal interval (\(\tau_{\text{opt}}\)) to save checkpoints, balancing write cost (\(\delta\)) and recomputation loss:
\[\tau_{\text{opt}} = \sqrt{2 \times \delta \times \text{MTBF}_{\text{cluster}}}\]

### Pipeline Bubble Fraction (GPipe & 1F1B)
The fraction of GPU compute time lost to bubbles for \(P\) pipeline stages and \(M\) microbatches:
\[b = \frac{P - 1}{P - 1 + M}\]
Keeping bubble overhead below \(20\%\) requires \(M \ge 4(P-1)\).
For interleaved scheduling with \(V\) virtual stages:
\[b_{\text{interleaved}} = \frac{P - 1}{P - 1 + M \times V}\]

### Availability Stacking
The aggregate availability \(A_{\text{system}}\) of \(k\) independent redundant replicas, each with availability \(A\):
\[A_{\text{system}} = 1 - (1 - A)^k\]

### Effective Fleet FLOPS (The M-S-G Law)
The useful compute throughput delivered by a fleet, accounting for Computation (MFU), Communication (\(\eta_{\text{scaling}}\)), and Coordination (Goodput Ratio):
\[\text{Effective FLOPS} = \text{Peak FLOPS} \times \text{MFU} \times \eta_{\text{scaling}} \times \text{Goodput Ratio}\]

### Tail Latency Compounding Law
The probability \(P_{\text{tail}}\) of a query experiencing a tail-latency delay when distributed across \(N\) independent servers, each with local tail probability \(p\):
\[P_{\text{tail}} = 1 - (1 - p)^N\]

