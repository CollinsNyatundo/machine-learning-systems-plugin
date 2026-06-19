# Appendix B: Data Foundations

## Material Covered in This Chapter

- Purpose
- How to Use This Appendix
- B.1 Data Engineering Foundations
- B.1.1 Napkin math: The physics of data gravity
- B.1.2 The cost of serialization
- B.1.3 Row vs. columnar formats
- Systems Perspective 18.1: The accelerator starvation problem
- Row-Oriented (CSV)
- B.1.4 The algebra of data
- B.2 Probability and Statistics
- Systems Perspective 18.2: Why statistics matters for systems
- B.2.1 Distributions and the long tail
- B.2.2 Measuring drift (divergence)
- Napkin Math 18.2: Worked example: KL divergence for drift detection
- B.2.3 Information theory for systems
- B.2.4 Logits and numerical stability
- Napkin Math 18.3: Worked example: Log-sum-exp in action
- Checkpoint 18.1: Check your understanding
- B.3 Fallacies and Pitfalls
- B.4 Summary
- Key Takeaways: Data as a physical constraint

---

## Section-by-Section Preserve-and-Extend

# Appendix B: Data Foundations

This appendix serves as a systems engineering reference for data pipelines and statistical monitoring in production
Machine Learning (ML) systems. In high-scale ML, data is not merely an abstract collection of values; it is a physical
entity with volume, inertia, and serialization costs that must be transported through disks, networks, CPUs, and
accelerator memories.

---

## B.1 Data Engineering Foundations

System performance is heavily determined by how data is stored, parsed, and accessed. When training or serving models,
the physical limits of hardware bandwidth and memory hierarchy define the boundaries of throughput.

### B.1.1 Napkin Math: The Physics of Data Gravity
**Data Gravity** describes the phenomenon where large datasets become functionally stationary because the time and
energy required to transfer them across networks exceed the cost of shipping the computation to the data.

The network transfer time \(T\) for a dataset of volume \(V\) over network bandwidth \(BW\) (ignoring latency for large
payloads) is calculated as:

\[T = \frac{V}{BW}\]

#### Table B.1: The Cost of Inertia (Transfer Latency Across Media)
At petabyte scales, standard network connections are highly impractical. Shipping physical storage media (e.g., AWS
Snowmobile trucks) becomes the only viable path to move data within a reasonable timeframe.

| Data Volume | 1 Gbps (Standard WAN) | 10 Gbps (High-End WAN) | 100 Gbps (Direct Connect) | Snowmobile (Truck) |
| :--- | :--- | :--- | :--- | :--- |
| **1 TB** | 2.2 Hours | 13 Minutes | 1.2 Minutes | N/A |
| **100 TB** | 9 Days | 22.2 Hours | 2.2 Hours | N/A |
| **1 PB** | 3 Months | 9 Days | 22.2 Hours | 2 Days |

---

### B.1.2 The Cost of Serialization
The **serialization tax** represents the CPU compute overhead spent converting in-memory data structures into a byte
stream (and vice versa). Parsing text-based formats like CSV or JSON is highly CPU-intensive, often leading to
**accelerator starvation** where high-performance GPUs/TPUs idle while waiting for the CPU to decode input strings.

#### Table B.2: Serialization & Decode Overhead
Zero-copy and columnar binary formats are significantly faster because they map directly to internal memory layouts,
eliminating CPU parsing loops.

| Format | Decoding Speed (MB/s) | Relative CPU Decode Cost | Suitability |
| :--- | :--- | :--- | :--- |
| **CSV / JSON** | \(\sim 100 \text{ MB/s}\) | High | Debugging & Inspection Only |
| **Protobuf** | \(\sim 300 \text{ MB/s}\) | Medium | Remote Procedure Calls (RPC) & Messaging |
| **Parquet / Arrow** | \(> 1,000 \text{ MB/s}\) | Low | High-Scale ML Training & Vectorized Analytics |

---

### B.1.3 Row-Oriented vs. Columnar Formats
The layout of data on physical media fundamentally changes access patterns:

* **Row-Oriented (e.g., CSV, JSON)**: Packs data record-by-record. Reading a single column requires scanning every byte
of the entire table. This layout is write-efficient (fast appends) but highly inefficient for feature extraction.
* **Column-Oriented (e.g., Parquet, Arrow)**: Packs data column-by-column. This enables **projection pushdown** (reading
only the blocks of memory containing the requested features) and **vectorized processing** via Single Instruction,
Multiple Data (SIMD) hardware operations.

```
Row-Oriented Layout (Record-by-Record):
[Row 1: ID, Age, Label] -> [Row 2: ID, Age, Label] -> [Row 3: ID, Age, Label]

Columnar-Oriented Layout (Feature-by-Feature):
[IDs: Row 1, 2, 3] -> [Ages: Row 1, 2, 3] -> [Labels: Row 1, 2, 3]
```

> [!IMPORTANT]
> **Systems Perspective: The Accelerator Starvation Problem**
> If your data pipeline uses row-oriented layouts combined with slow text deserialization, the input data rate falls
below the execution capacity of the accelerator. This makes the system I/O-bound, rendering expensive GPU optimizations
useless.

---

### B.1.4 The Algebra of Data (SQL Primitives)
Feature engineering pipelines are built on relational primitives. Their computational complexity and system overhead are
characterized as follows:

1. **Selection (\(\sigma\))**: Filtering rows based on a predicate (e.g., `WHERE age > 30`).
   * **System Cost**: \(O(\log N)\) if index structures exist; \(O(N)\) for full-table scans.
2. **Projection (\(\pi\))**: Selecting subset columns (features).
   * **System Cost**: Practically free in columnar layouts (only loads targeted blocks). In row-oriented formats, it
wastes significant disk/network bandwidth. For instance, reading a \(1 \text{ KB}\) row to extract a \(4\text{-byte}\)
column wastes \(99.6\%\) of I/O bandwidth.
3. **Join (\(\bowtie\))**: Combining data tables on keys. Joins represent the most expensive distributed operation.
   * **Shuffle Join**: Both tables are partitioned and exchanged across the network using the join key.
     * **System Cost**: High network saturation. Joining two \(1 \text{ TB}\) tables requires moving approximately \(2
\text{ TB}\) of data over network interfaces.
   * **Broadcast Join**: The smaller table is fully replicated and sent to all compute nodes.
     * **System Cost**: Low network traffic, but the broadcasted table must fit entirely within the RAM of each worker
node.

---

## B.2 Probability and Statistics

Statistics provide the mathematical basis for detecting silent data errors, measuring tail latencies, and maintaining
numerical stability in neural network layers.

> [!NOTE]
> **Systems Perspective: Why Statistics Matters for Systems**
> Average-based metrics (like mean latency or mean values) fail to represent the operational state of distributed
systems. Tail events (P99/P99.9) dominate user experience, and distribution drift can silently degrade model accuracy
long before simple statistical aggregates show anomalies.

### B.2.1 Distributions and the Long Tail
System latencies exhibit lognormal or power-law distributions rather than Gaussian (normal) distributions. While a P99
latency indicates that \(1\%\) of single requests are slow, the cumulative probability of a user experiencing a slow
request over a session of \(N\) independent requests is given by:

\[P(\text{Slow}) = 1 - (1 - p)^N\]

where \(p = 0.01\) for P99.

#### Napkin Math 18.1: The Session-Level Latency Experience
For a user session involving \(N = 100\) requests (typical for a single web application session or chatbot
conversation), the probability of hitting at least one P99 latency spike is:

\[P(\text{Slow}) = 1 - (0.99)^{100} \approx 1 - 0.366 = 63.4\%\]

For high-volume users, the tail latency spike effectively becomes their median experience. This dictates that production
systems must optimize for high percentiles (\(P99.9\) or \(P99.99\)).

---

### B.2.2 Measuring Distribution Drift (Divergence)
Evaluating changes in incoming production data (serving distribution \(Q\)) relative to baseline training data
(reference distribution \(P\)) requires measuring the distance between their probability density functions.

#### Kullback-Leibler (KL) Divergence
KL divergence (relative entropy) measures the expected information loss when approximating \(P\) using \(Q\):

\[D_{KL}(P \parallel Q) = \sum_{i} P_i \ln \left(\frac{P_i}{Q_i}\right)\]

KL divergence is asymmetric: \(D_{KL}(P \parallel Q) \neq D_{KL}(Q \parallel P)\).

#### Population Stability Index (PSI)
To establish a symmetric metric that is easier to threshold for system alerts, practitioners use the Population
Stability Index (PSI), which combines both directions of KL divergence:

\[\text{PSI} = \sum_{i} (P_i - Q_i) \ln \left(\frac{P_i}{Q_i}\right) = D_{KL}(P \parallel Q) + D_{KL}(Q \parallel P)\]

* **PSI < 0.1**: Minimal shift.
* **0.1 \(\le\) PSI \(\le\) 0.2**: Moderate shift; monitor closely.
* **PSI > 0.2**: Significant shift; triggers an automated alert for model retraining.

#### Napkin Math 18.2: Worked Example of Drift Detection
Consider a sentiment classifier's class labels:

* **Training Distribution (\(P\))**: \([0.60 \text{ Positive}, 0.30 \text{ Negative}, 0.10 \text{ Neutral}]\)
* **Serving Distribution (\(Q\))**: \([0.45 \text{ Positive}, 0.40 \text{ Negative}, 0.15 \text{ Neutral}]\)

Step-by-step calculations:

1. **Calculate \(D_{KL}(P \parallel Q)\)**:
   \[
   \begin{aligned}
   D_{KL}(P \parallel Q) &= 0.60 \ln\left(\frac{0.60}{0.45}\right) + 0.30 \ln\left(\frac{0.30}{0.40}\right) + 0.10
\ln\left(\frac{0.10}{0.15}\right) \\
   &= 0.60(0.2877) + 0.30(-0.2877) + 0.10(-0.4055) \\
   &= 0.1726 - 0.0863 - 0.0405 \\
   &= 0.0458 \text{ nats}
   \end{aligned}
   \]

2. **Calculate \(D_{KL}(Q \parallel P)\)**:
   \[
   \begin{aligned}
   D_{KL}(Q \parallel P) &= 0.45 \ln\left(\frac{0.45}{0.60}\right) + 0.40 \ln\left(\frac{0.40}{0.30}\right) + 0.15
\ln\left(\frac{0.15}{0.10}\right) \\
   &= 0.45(-0.2877) + 0.40(0.2877) + 0.15(0.4055) \\
   &= -0.1295 + 0.1151 + 0.0608 \\
   &= 0.0464 \text{ nats}
   \end{aligned}
   \]

3. **Calculate PSI**:
   \[
   \begin{aligned}
   \text{PSI} &= (0.60 - 0.45)\ln\left(\frac{0.60}{0.45}\right) + (0.30 - 0.40)\ln\left(\frac{0.30}{0.40}\right) + (0.10
- 0.15)\ln\left(\frac{0.10}{0.15}\right) \\
   &= (0.15)(0.2877) + (-0.10)(-0.2877) + (-0.05)(-0.4055) \\
   &= 0.0432 + 0.0288 + 0.0203 \\
   &= 0.0923 \text{ (or } 0.092 \text{ rounded)}
   \end{aligned}
   \]

*Result*: Since \(\text{PSI} = 0.092 < 0.2\), the drift is observable but does not cross the retraining trigger
threshold.

---

### B.2.3 Information Theory for Systems
Information theory provides a formal vocabulary for reasoning about limits on data compression and dataset quality.

* **Entropy (\(H\))**: Quantifies the average uncertainty or information content contained within a distribution. For a
discrete random variable \(X\):
  \[H(X) = -\sum_{i} p(x_i) \log_b p(x_i)\]
  Using log base-2 gives bits; natural logarithms give nats. It defines the theoretical minimum code length for
loss-free data representation.
* **Information Density**: The proportion of useful signal relative to overall storage size.
* **Signal-to-Noise Ratio (SNR)**: The ratio of structured signal to random variance. Low SNR datasets hit a hard
information-theoretic barrier where adding further compute during model training yields no accuracy improvement.

---

### B.2.4 Logits and Numerical Stability
Deep neural networks output raw, unnormalized values called **logits** (\(z\)). Converting these to probability
distributions is done using the Softmax function:

\[p_i = \frac{e^{z_i}}{\sum_{j} e^{z_j}}\]

#### The Overflow Problem
When logits \(z_i\) take on large values (e.g., \(z_i = 100\)), direct exponentiation \(e^{z_i}\) causes numerical
overflow in standard computing formats:
* **FP16** overflows at \(x \approx 11.1\) (max value \(65,504\)).
* **FP32** overflows at \(x \approx 88.7\) (max value \(\approx 3.4 \times 10^{38}\)).
* **BF16** overflows at \(x \approx 88.7\) (max value \(\approx 3.4 \times 10^{38}\)).

This results in `NaN` outputs during standard backpropagation or inference.

#### The Log-Sum-Exp Solution
To resolve this, calculations are computed in log-space using the **Log-Sum-Exp identity**:

\[\ln \left( \sum_{j} e^{z_j} \right) = a + \ln \left( \sum_{j} e^{z_j - a} \right)\]

where \(a = \max_j(z_j)\). Subtraction of the maximum value shifts the exponents such that all \(z_j - a \le 0\),
forcing the exponentials to lie within the stable interval \([0, 1]\).

#### Napkin Math 18.3: Log-Sum-Exp in Action
Given a three-class classification model returning logits:

\[z = [100, 101, 102]\]

1. **Naive Softmax Approach**:
   * Exponents: \(e^{100} \approx 2.7 \times 10^{43}\), \(e^{101} \approx 7.3 \times 10^{43}\), \(e^{102} \approx 2.0
\times 10^{44}\).
   * *Outcome*: These numbers exceed the float limit of FP32 (\(3.4 \times 10^{38}\)) and immediately trigger overflow
failures.
2. **Log-Sum-Exp Approach**:
   * Find maximum value: \(a = 102\).
   * Shift logits: \(z - a = [-2, -1, 0]\).
   * Exponentiate shifted values: \(e^{-2} \approx 0.135\), \(e^{-1} \approx 0.368\), \(e^0 = 1.0\).
   * Sum of shifted exponents: \(\sum e^{z_j - a} = 0.135 + 0.368 + 1.0 = 1.503\).
   * Log-Sum-Exp value: \(\text{LogSumExp}(z) = 102 + \ln(1.503) \approx 102.408\).
   * Normalized Softmax values:
     \[p_i = e^{z_i - \text{LogSumExp}(z)}\]
     * \(p_1 = e^{100 - 102.408} = e^{-2.408} \approx 0.090\)
     * \(p_2 = e^{101 - 102.408} = e^{-1.408} \approx 0.245\)
     * \(p_3 = e^{102 - 102.408} = e^{-0.408} \approx 0.665\)
   * *Outcome*: Safe evaluation with all numbers bounded within standard formats.

---

## B.3 Fallacies and Pitfalls

* **Fallacy: Moving petabyte-scale data to the cloud is purely a bandwidth issue.**
  * *Reality*: Data gravity goes beyond transmission speeds. It impacts pipelines, validation constraints, and network
topology. Moving petabytes of data can take weeks or months. Computing must be placed adjacent to the data source.
* **Pitfall: Ignoring serialization costs during engine development.**
  * *Reality*: Over-optimizing accelerator kernels while reading dataset features in slow JSON/CSV files leads to severe
I/O bottlenecks. Upgrading to Parquet or Arrow provides up to a \(10\text{-}100\times\) decode speedup on the CPU.
* **Fallacy: Average latency is an adequate representation of service performance.**
  * *Reality*: Due to long-tailed distributions, P99 latency determines session quality. If a user issues multiple
requests per session, the probability of them hitting at least one degraded response is high.
* **Pitfall: Monitoring model accuracy rather than input distributions.**
  * *Reality*: A model can maintain average accuracy metrics even when processing drifted data. When accuracy drop-off
becomes visible, the system drift has typically been occurring for weeks. Proactive input monitoring using PSI is
necessary.

---

## B.4 Checkpoint Solutions & Explanations

### Question 1
*A training pipeline reads \(500\text{ GB}\) of CSV data over a \(10\text{ Gbps}\) link. Estimate the transfer time. Now
estimate how long it would take if the data were stored as Parquet and only \(20\%\) of columns were needed—what changes
and why?*

#### Solution
1. **CSV Transfer Time**:
   * Volume: \(500 \text{ GB} = 500 \times 10^9 \text{ Bytes} = 4,000 \times 10^9 \text{ bits}\) (since \(1\text{ Byte}
= 8\text{ bits}\)).
   * Bandwidth: \(10 \text{ Gbps} = 10 \times 10^9 \text{ bits/second}\).
   * Transfer Time:
     \[T = \frac{4000 \times 10^9 \text{ bits}}{10 \times 10^9 \text{ bits/s}} = 400 \text{ seconds} \approx 6.67 \text{ minutes}\]
2. **Parquet with Projection Pushdown**:
   * Columnar storage permits reading only the needed \(20\%\) of data.
   * New volume to transfer: \(500 \text{ GB} \times 0.20 = 100 \text{ GB}\).
   * Transfer Time:
     \[T = \frac{100 \times 8 \times 10^9 \text{ bits}}{10 \times 10^9 \text{ bits/s}} = 80 \text{ seconds} \approx 1.33 \text{ minutes}\]
   * *Rationale*: Changing to Parquet reduces physical network payload sizes via projection pushdown, cutting transfer
times by \(5\times\) and lowering CPU deserialization tax.

---

### Question 2
*Your model's average latency is \(50\text{ ms}\), but P99 is \(800\text{ ms}\). If a typical user session involves
fifty requests, what is the probability that a user experiences at least one P99 spike? Does "average latency"
adequately describe user experience?*

#### Solution
1. **Probability Calculation**:
   * Probability of experiencing at least one P99 latency event in \(N = 50\) requests:
     \[P(\text{Slow}) = 1 - (1 - 0.01)^{50} = 1 - (0.99)^{50}\]
   * Calculating the exponent:
     \[(0.99)^{50} \approx 0.605\]
   * Probability:
     \[P(\text{Slow}) = 1 - 0.605 = 0.395 \text{ or } 39.5\%\]
2. **System Analysis**:
   * Average latency (\(50\text{ ms}\)) is an inadequate representation of user experience. Approximately \(39.5\%\) of
users will experience a latency spike of \(800\text{ ms}\) during their session, showing that system performance is
governed by tail distribution behaviors.

---

### Question 3
*Explain why KL divergence is asymmetric and why this matters when choosing a drift metric for production monitoring.
When would you prefer PSI over raw KL divergence?*

#### Solution
1. **Asymmetry**:
   * KL divergence measures relative entropy based on a reference distribution:
     \[D_{KL}(P \parallel Q) = \sum P_i \ln\left(\frac{P_i}{Q_i}\right) \quad \text{vs.} \quad D_{KL}(Q \parallel P) = \sum Q_i \ln\left(\frac{Q_i}{P_i}\right)\]
   * The weighting term (coefficient outside the log) is either the training likelihood (\(P_i\)) or the serving
likelihood (\(Q_i\)). Consequently, a shift in low-density training areas has a different impact than a shift in
high-density areas.
2. **Monitoring Application**:
   * Asymmetry introduces ambiguity in automated monitoring rules since the alert output depends on which distribution
is labeled as the base reference.
3. **Preferring PSI**:
   * PSI is symmetric (\(D_{KL}(P \parallel Q) + D_{KL}(Q \parallel P)\)). This makes it easier to set stable,
direction-independent threshold values (such as the standard alert threshold of \(0.2\)) for production logging systems.

---

### Question 4
*Provide clear system definitions and units for: Entropy, Logits, and Log-Sum-Exp.*

#### Solution
1. **Entropy (\(H\))**:
   * *Definition*: The average uncertainty or information content contained within a probability distribution. It
determines the minimum lossless compression limit.
   * *Units*: **bits** (when log base-2 is used) or **nats** (when natural logarithms are used).
2. **Logits**:
   * *Definition*: The raw, unnormalized score outputs from the final linear layer of a deep neural network before
activation functions are applied.
   * *Units*: **Dimensionless scale factor** (representing logarithmic odds relative to other classes).
3. **Log-Sum-Exp**:
   * *Definition*: A mathematically equivalent identity that computes the logarithm of the sum of exponentials in a
numerically stable manner by shifting the logits by their maximum value.
   * *Units*: **Dimensionless log-scale value**.

---

## B.5 Key Takeaways: Data as a Physical Constraint

* **Physical Inertia**: Data transfer latency scales linearly with dataset size, rendering petabyte-scale data
effectively stationary. Distributed designs must process data locally where it is collected.
* **Algebraic Operations**: Selecting, projecting, and joining data have differing compute costs. Joins are highly
expensive and require selecting between shuffle joins (network bound) and broadcast joins (RAM bound).
* **Format Dependency**: Deserialization is a core pipeline bottleneck. Moving from row-oriented text formats (CSV,
JSON) to columnar binary formats (Parquet, Arrow) reduces decoding overhead on the CPU, preventing accelerator
starvation.
* **The Tail Governs Performance**: Standard averages do not represent operational user experience. P99 latency shapes
user session satisfaction, necessitating percentiles monitoring.
* **Distribution Monitoring**: Tracking drift requires comparing complete distributions rather than summary means.
Symmetric PSI metrics catch feature shifts before they degrade model accuracy.
* **Numerical Stability**: Implementations must utilize log-space identities like the Log-Sum-Exp trick to avoid
arithmetic overflows during softmax layers when working in FP16/FP32 precision.

---

## Full Slice Content (Docling Extract, Preserved Verbatim)

> Each section below preserves the source slice content as extracted by docling. Image placeholders are removed; tables,
equations, code blocks, named artifacts, and footnotes are kept intact.

## Purpose

What makes 'data' a first-class systems constraint, and how do we measure when it is silently breaking our models?

This appendix collects the reference calculations and statistical tools for reasoning about the data path as a systems
engineer. It focuses on what matters in practice: data gravity napkin math, format and serialization costs, the
algebraic primitives that create pipeline blowups (especially joins), and drift metrics that compare full distributions
rather than means.

In ML systems, data is not an abstract dataset-it is physical volume that must move through disks, networks, CPUs, and
accelerator memory. Many expensive training runs are limited not by FLOP/s, but by I/O bandwidth, serialization
overhead, and avoidable scans of irrelevant bytes. In production, the more dangerous failure mode is quieter:
distributions drift, tails dominate user experience, and accuracy degrades long before average metrics look suspicious.

## How to Use This Appendix

This appendix is designed as a reference . Reach for it when debugging 'slow training,' 'low accelerator utilization,'
or 'production accuracy drift' calls for the quickest path from symptom to measurement. Conventions used here follow the
book-wide notation (for example, we reserve 𝐵 for batch size and use BW for bandwidth). · When data will not move: Start
with Table B.1 and the transfer-time equation in Section B.1.

- When the accelerator is starving: Use Table B.2 and the layout discussion in Section B.1.3.
- When pipelines explode in cost: Use the primitives in Section B.1.4, especially join-induced shuffles.
- When 'average looks fine' but users complain: Use Section B.2.1 and session-level tail probability.
- When accuracy drifts silently: Use Section B.2.2 to compare full distributions.

This appendix covers the principles of data engineering and statistical monitoring that keep ML systems healthy. From
storage formats that determine I/O throughput to drift metrics that detect silent failures, these foundations connect
directly to the data pipelines in Chapter 4 and the operational monitoring in Chapter 14.

## B.1 Data Engineering Foundations

U nderstanding hardware constraints is only half the battle; we must also shape our data to fit them. Data engineering
applies the principles of the memory hierarchy to storage formats and pipeline design, ensuring that the accelerator
never starves. This process begins with recognizing that data is physical-it has volume, it takes time to move, and it
requires energy to parse.

## B.1.1 Napkin math: The physics of data gravity

Data gravity 1 is not a metaphor; it is a calculation of transfer time. Unlike compute, which gets faster every year,
the speed of light is fixed and network bandwidth is a finite resource. When datasets

1 Data Gravity: Coined by Dave McCrory in 2010 to describe how large datasets attract services and applications toward
them, much as massive bodies attract smaller ones in physics. The analogy is apt: the 'escape velocity' required to move
a petabyte-scale dataset is often measured in weeks.

Serialization: From Latin serialis (forming a series). The process of converting in-memory data structures into a byte
stream for storage or transmission, and the reverse ( deserialization ). In MLpipelines, the choice of serialization
format can dominate end-to-end training time; Chapter 4 covers pipeline design strategies that minimize this overhead.

grow large enough, they effectively become stationary-moving them costs more time and energy than moving the computation
to where the data already lives. The transfer time for moving a dataset is simply 𝑇 = Data Volume / Bandwidth (for the
large volumes here, latency is negligible; the full equation appears in Section D.3.4). Table B.1 illustrates the
sobering reality:

Table B.1: The Cost of Inertia: Why we 'ship compute to data' rather than 'ship data to compute.' At 1 PB, the network
is often not a viable option.

| Data Volume   | 1 Gbps (Standard WAN)   | 10 Gbps (High-End WAN)   | 100 Gbps (Direct Connect)   | Snowmobile (Truck)   |
|---------------|-------------------------|--------------------------|-----------------------------|----------------------|
| 1 TB          | 2.2 Hours               | 13 Minutes               | 1 Minutes                   | N/A                  |
| 100 TB        | 9 Days                  | 22.2 Hours               | 2.2 Hours                   | N/A                  |
| 1 PB          | 3 Months                | 9 Days                   | 22.2 Hours                  | 2 Days               |

## B.1.2 The cost of serialization

Even after data arrives at the machine, we face one final hurdle: the serialization tax. 2 As Table B.2 shows, many
engineers meticulously optimize their accelerator kernels while ignoring the CPU overhead of decoding data. Parsing
text-based formats like JavaScript Object Notation (JSON) or CSV is extremely CPU-intensive, often leaving the
accelerator idling while the CPU struggles to convert strings into floating-point numbers.

Table B.2: Serialization Overhead: Zero-copy formats like Arrow are 10-100 × faster than row-based text formats because
they align directly with internal memory structures.

| Format        | Decoding Speed (MB/s)   | Relative CPU Decode Cost   | Suitability         |
|---------------|-------------------------|----------------------------|---------------------|
| CSV/JSON      | ~100 MB/s               | High                       | Debugging only      |
| Protobuf      | ~300 MB/s               | Medium                     | RPC/Messages        |
| Parquet/Arrow | > 1,000 MB/s            | Low                        | High-Scale Training |

## B.1.3 Row vs. columnar formats

The choice of file format determines the 'physics' of how the data is read.

Column-Oriented (Parquet, Arrow) : Data is stored column-by-column. To read the age column, the disk head seeks to that
column's block and reads it sequentially. This enables projection pushdown (reading only the bytes required) and
vectorized processing (single instruction, multiple data (SIMD) operations on columns). Compare the two arrangements
side by side in Figure B.1 to see why columnar access avoids scanning unnecessary bytes.

Row-Oriented (CSV, JSON) : Data is stored record-by-record. Reading just the age column requires scanning every byte of
every row. This is efficient for writing (appending a log) but inefficient for analytics (training on specific
features).

This layout difference has direct consequences for ML pipelines where accelerator utilization depends on data loading
speed.

## Systems Perspective 18.1: The accelerator starvation problem

The choice of file format determines whether a system is I/O bound or compute bound. As Table B.2 shows, the
serialization tax compounds with storage layout: row-oriented formats force full-row scans while columnar formats enable
projection pushdown, reading only the bytes the model needs. The result is that the 'Data Movement' term in the iron law
can silently become the bottleneck that leaves expensive accelerators idling.

## Row-Oriented (CSV)

Figure B.1: Storage Layouts: Row-oriented formats pack data together by record (good for transactions). Column-oriented
formats pack data by feature (good for analytics).

## B.1.4 The algebra of data

- Feature engineering is built on three Structured Query Language (SQL) primitives. Understanding their computational
cost prevents pipeline bottlenecks. 1. Selection ( 𝜎 ) : Filtering rows (for example, WHERE age > 30 ). · Cost: Cheap (
𝑂( log 𝑁) ) if indexed; expensive ( 𝑂(𝑁) ) if full scan. 2. Projection ( 𝜋 ) : Selecting columns (for example, SELECT
age ). · Cost: Free in columnar formats (only read relevant blocks). In row formats, the entire 1 KB row must be read
just to extract the 4-byte integer, wasting 99.6 percent of I/O bandwidth. 3. Join ( ⋈ ) : Combining tables. The most
expensive operation. · Shuffle Join: Both tables are partitioned by key and exchanged over the network.
- -Cost: Massive network traffic. Joining two 1 TB tables requires moving ~2 TB over the network.
- Broadcast Join: One small table is sent to all workers.
- -Cost: Minimal network, but the small table must fi t in RAM.

Understanding data formats, serialization costs, and algebraic primitives tells us how to move data efficiently. Even a
perfectly engineered pipeline, however, can silently fail if the data it carries changes character over time. Detecting
that change-and quantifying how much it matters-requires a different set of tools: probability and statistics.

## B.2 Probability and Statistics

Once data is flowing through our pipelines, we need mathematical tools to ensure its quality and consistency.
Probability and statistics provide the language for monitoring system health, detecting the silent failures of data
drift, and managing uncertainty.

## Systems Perspective 18.2: Why statistics matters for systems

Your monitoring dashboard says average latency is fine, but users are complaining. Why? Because systems live in the
'long tail.' Statistics gives us the tools to measure uncertainty, detect drift, and handle numerical stability-three
capabilities that separate robust production systems from fragile ones.

3 KL Divergence: Named after Solomon Kullback and Richard Leibler, who introduced it in 1951. Also called relative
entropy, it quantifies the expected extra information needed to encode samples from 𝑃 using a code optimized for 𝑄 .
With natural logarithms, as in the example above, the unit is nats; with base-2 logarithms, the unit is bits. In
production ML, KL divergence is the theoretical backbone of many driftdetection metrics.

## B.2.1 Distributions and the long tail

In systems, the mean is often misleading. Latency distributions are almost always long-tailed (lognormal or power law).
A 'P99' (99th percentile) latency of 500 ms means 1 percent of requests experience that tail latency; with many requests
per session, the fraction of users who see at least one slow request can be much higher. At scale (1M users), even a 1
percent affected-user rate would be 10,000 unhappy people.

Computed: P(Slow) = 63.4 percent. For a heavy user ( 𝑁 is large), the 'tail' latency becomes their median experience.
This is why Google and Amazon optimize for P99.9 or P99.99.

Napkin Math 18.1: The median experience If a user session involves 𝑁 = 100 requests (common for a web page load or chat
session), the probability of experiencing at least one P99 latency spike is: 𝑃( Slow ) = 1 - (0.99) 100 ≈ 1-0.366 =
63.4%

## B.2.2 Measuring drift (divergence)

Because distributions have long tails where the most dangerous failures hide, simple metrics like 'mean shift' are
insufficient. We need tools that compare the entire shape of the distribution. Detecting drift between serving data ( 𝑄
) and training data ( 𝑃 ) requires measuring the 'distance' between their distributions. KL divergence 3 measures how
much information is lost if we approximate 𝑃 with 𝑄 (Kullback and Leibler 1951):

## Napkin Math 18.2: Worked example: KL divergence for drift detection

<!-- formula-not-decoded -->

Scenario: Asentiment classifier was trained on data where 60 percent of reviews were positive, 30 percent negative, and
10 percent neutral. After deployment, the serving distribution shifts to 45 percent positive, 40 percent negative, and
15 percent neutral. Training distribution 𝑃: [0.60, 0.30, 0.10]. Serving distribution 𝑄: [0.45, 0.40, 0.15]. 𝐷 𝐾𝐿 (𝑃||𝑄)
= 0.60 log 0.60 0.45 +0.30 log 0.30 0.40 +0.10 log 0.10 0.15 = 0.60 × 0.288 + 0.30 × (-0.288) + 0.10 × (-0.405) = 0.173
+ (-0.086) + (-0.041) = 0.046 nats 𝐷 𝐾𝐿 (𝑄||𝑃) = 0.45 log 0.45 0.60 +0.40 log 0.40 0.30 +0.15 log 0.15 0.10
=0.45×(-0.288)+0.40×(0.288)+0.15×(0.405) = -0.129+0.115+0.061 = 0.046 nats Notice the asymmetry: 𝐷 KL (𝑃||𝑄) ≠ 𝐷 KL
(𝑄||𝑃) . The Population Stability Index (PSI) symmetrizes this:

Because KL divergence is asymmetric ( 𝐷 KL (𝑃||𝑄) ≠ 𝐷 KL (𝑄||𝑃) ), practitioners often use PSI, a symmetric metric
derived from KL divergence that is easier to threshold. A PSI > 0.2 typically triggers an alert for retraining.

PSI = ∑(𝑃 𝑖 -𝑄 𝑖 ) log 𝑃 𝑖 𝑄 𝑖 = (0.15)(0.288) + (-0.10)(-0.288) + (-0.05)(-0.405) = 0.043 + 0.029+0.020 = 0.092 Since
PSI = 0.092 < 0.2, this drift is noticeable but does not yet trigger a retraining alert. However, monitoring should
increase in frequency.

Both KL divergence and PSI are grounded in a deeper framework-information theory-which provides the units and bounds
that make these metrics principled rather than ad hoc.

## B.2.3 Information theory for systems

In the information roofline model (Appendix A), we treat data quality as a physical constraint similar to bandwidth.
Information theory provides the units for this constraint. Three concepts are central:

Entropy ( 𝐻 ) 4 is the average information content (uncertainty) in a distribution, defined as 𝐻(𝑋)= -∑𝑝(𝑥) log 𝑝(𝑥) .
The log base sets the unit: natural logs give nats, while log 2 gives bits. A uniform distribution has maximum entropy
(maximum uncertainty). This connects directly to KL divergence above: 𝐷 KL measures excess information needed when using
the wrong distribution. Information Density is the amount of useful signal per unit of storage. High-quality data has
high information density; noisy data has low density.

Signal-to-Noise Ratio (SNR) is the ratio of useful information to irrelevant variance. In ML, training on low-SNR data
is like trying to learn a pattern from static-the system hits the information roofline where adding more compute yields
no improvement.

## B.2.4 Logits and numerical stability

Neural networks output logits 5 (unnormalized scores), not probabilities. We convert them using Softmax:

The problem is that if 𝑧 𝑖 is large (for example, 100), the exponential 𝑒 𝑧 𝑖 overflows common training and inference
formats such as FP32, BF16, and FP16. FP64 can represent this specific value, but production ML kernels rarely use FP64
for softmax. The solution is to compute in log-space: the 'LogSum-Exp' trick allows us to compute log (∑𝑒 𝑧 𝑗 ) without
ever calculating the massive exponentials directly, preserving numerical precision. 6 The following example shows why
this trick matters in practice, even for modest logit values:

<!-- formula-not-decoded -->

## Napkin Math 18.3: Worked example: Log-sum-exp in action

(-1) ≈ 0.368

The setup: Athree-class classifier outputs logits . Without the trick (naive softmax) : exp (100) ≈ 2.7 ×10 43, exp (101) ≈ 7.3×10 43, exp (102) ≈ 2.0×10 44 These numbers are representable in FP64 but overflow FP32 (max ≈3.4×10 38 ). With FP16 (max ≈65,504 ), even 𝑒 12 overflows. In practice, logits of magnitude 100 are not unusual in deep networks, and FP16/BF16 is the standard training precision-so naive softmax fails routinely. With the trick: Subtract 𝑎 = max (𝑧) = 102: 𝑧 -𝑎 = [-2,-1,0] exp (-2) ≈ 0.135, exp, exp Sum = 1.503. LogSumExp = 102 log . Softmax: [0.135/1.503, 0.368/1.503, 1.0/1.503] = [0.090, 0.245, 0.665] The exponentiated shifted values and the resulting softmax probabilities are in [0,1] -no overflow risk, even in FP16.

𝑧 = [100,101,102]

(0) = 1.0

+

(1.503) = 102.408

## Checkpoint 18.1: Check your understanding

1. Atraining pipeline reads 500 GB of CSV data over a 10 Gbps link. Estimate the transfer time. Now estimate how long it
would take if the data were stored as Parquet and only 20 percent of columns were needed-what changes and why?
2. Your model's average latency is 50 ms, but P99 is 800 ms. If a typical user session involves fifty requests, what is
the probability that a user experiences at least one P99 spike? Does 'average latency' adequately describe user
experience?
3. Explain why KL divergence is asymmetric and why this matters when choosing a drift metric for production monitoring.
When would you prefer PSI over raw KL divergence?
4. 4 Entropy: From Greek entropia (transformation). Shannon borrowed the term from thermodynamics in 1948 to quantify
information content. In systems terms, entropy quantifies the theoretical minimum code length needed to encode a message
from a source, measured in bits when using log 2 and nats when using natural logs, directly relevant to compression
ratios and data pipeline sizing.
5. 5 Logit: From log + unit, coined by Joseph Berkson in 1944. The logit function is the inverse of the logistic
(sigmoid) function: logit (𝑝) = log (𝑝/(1 - 𝑝)) . In deep learning, 'logits' refers more loosely to the raw,
unnormalized output of the final linear layer before any activation function is applied.
6. 6 Log-Sum-Exp: Implemented as torch.logsumexp in PyTorch and scipy.special.logsumexp in SciPy. It relies on the
identity log (∑𝑒 𝑥 𝑖 ) = 𝑎 + log (∑𝑒 𝑥 𝑖 -𝑎 ) , where 𝑎 = max (𝑥 𝑖 ) . Shifted values 𝑥 𝑖 - 𝑎 are ≤ 0, ensuring
exponentials never overflow.

The tools in this section-tail-aware metrics, drift divergences, information-theoretic bounds, and numerical stability
tricks-give us the vocabulary to diagnose data-related failures quantitatively rather than anecdotally. The fallacies
that follow highlight the most common ways these tools are ignored.

## B.3 Fallacies and Pitfalls

Fallacy: Moving a petabyte to the cloud is just a bandwidth problem.

Pitfall: Ignoring data serialization cost. Engineers meticulously optimize accelerator kernels while leaving data
loading as JSON or CSV. As Table B.2 shows, text-based formats can be 10-100 × slower to decode than columnar binary
formats, making the CPU-not the accelerator-the bottleneck (Section B.1). Fallacy: Average latency is a good summary of
system performance.

Transfer time is only the beginning. Data gravity encompasses not just transfer duration but also the re-engineering of
pipelines, re-validation of data quality, and synchronization of dependent services. Organizations that plan only for
bandwidth discover that the true cost is measured in engineering months, not network hours.

The mean hides the tail. At scale, the P99 latency becomes the median user experience because each session involves many
requests. Monitoring only the mean creates a dangerous blind spot where thousands of users suffer degraded service while
dashboards show green.

A model's accuracy can remain stable even as the input distribution drifts, because the model memorizes enough of the
old distribution to maintain aggregate metrics. By the time accuracy visibly degrades, the drift has often been
accumulating for weeks. Monitoring input distributions with metrics like PSI catches drift earlier and allows proactive
retraining.

Pitfall: Monitoring accuracy instead of input distributions.

These pitfalls share a common root: treating data as a solved problem rather than a continuous engineering discipline.
The following summary distills the core principles that guard against each one.

## B.4 Summary

## Key Takeaways: Data as a physical constraint

- Data has physical inertia: transfer time scales linearly with volume and inversely with bandwidth, making
petabyte-scale datasets effectively immovable. Design pipelines around data locality rather than data movement.
- The three algebraic primitives-selection, projection, and join-have radically different I/O costs. Joins in particular
can amplify network traffic by orders of magnitude; choosing between shuffle and broadcast joins depends on relative
table sizes.
- Serialization format is a first-order performance decision. Columnar binary formats (Parquet, Arrow) can be 10-100 ×
faster to decode than text formats (CSV, JSON), directly determining whether accelerators starve or stay fed.
- Average metrics lie. Long-tailed distributions mean that the P99 latency becomes the typical user experience at scale,
and monitoring only the mean creates dangerous blind spots.
- Drift detection requires comparing full distributions, not summary statistics. KL divergence and the symmetric
PSI/Jeffreys divergence provide principled measures of distribution shift that catch problems before accuracy metrics
react.
- Numerical stability is not optional. The log-sum-exp trick and log-space computation prevent overflow in softmax and
loss calculations, making them essential building blocks of any training or inference pipeline.
