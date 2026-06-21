# Appendix D: Reliability Foundations (Vol 2)

Appendix D provides the quantitative frameworks, statistical models, and heuristics required to design resilient,
fault-tolerant ML fleets. At scale, component failure is a continuous background condition that must be engineered
around, no different from heat dissipation or power delivery.

---

## Section-by-Section Preserve-and-Extend

## Reliability Foundations

## Purpose

\_** How do we reason about failure as a statistical certainty, and what does the math tell us about staying alive at
scale?\_

This appendix collects the reference calculations for reasoning quantitatively about failure, recovery, and availability
at scale. It provides the mathematical tools behind the fault tolerance strategies in Chapter 8, the fleet orchestration
policies in Chapter 9, and the operational practices in Chapter 13.

Individual accelerators fail rarely-but fleets are large, and probability is relentless. Scale a cluster to tens of
thousands of GPUs and the expected time between failures drops from years to hours. Scale further and failures arrive
faster than any human operator can respond. The math is straightforward, the implications are profound: at fleet scale,
failure is not an exceptional event to be debugged but a continuous physical condition to be engineered around, no
different from heat dissipation or power delivery.

## How to Use This Appendix

This appendix is designed as a reference, intended for moving from intuition ('failures happen more often at scale') to
quantitative engineering decisions ('how often should one checkpoint?' or 'how many spare nodes are needed?').

- 'How often will something fail?' -Start with Section D.1 and the MTBF cascade in Section D.1.2.
- 'How often should I checkpoint?' -Use the Young-Daly model in Section D.2.1 and the worked example in Section D.2.3.
- 'How much time do I lose to recovery?' -See the recovery anatomy in Section D.3.1 and the goodput analysis in Section
D.3.2.
- 'Should I use redundancy or checkpointing?' -Compare strategies in Section D.4.1 and availability stacking in Section
D.4.2.

## D.1 Failure Probability at Scale

<!-- image -->

## LIGHTBULB Why this matters

Consider a training run on a 10,000-GPU cluster running for three weeks. What is the probability that at least one GPU
fails during that time? The answer-effectively 100 percentdetermines whether the system needs fault tolerance as a core
design requirement or merely a nice-to-have. The calculations in this section make that determination precise.

I ndividual hardware components are remarkably reliable. A data center-grade GPU operates for tens of thousands of hours
before failing. The physics of large-scale systems, however, works against reliability: every additional component is
another opportunity for failure, and the aggregate failure rate scales linearly with component count. This section
develops the arithmetic that transforms component-level reliability into system-level failure predictions.

<!-- image -->

D

## D.1.1 Component failure rates

Reliability engineers characterize components using two complementary metrics. The Failure in Time (FIT) rate counts
failures per 10 9 device-hours of operation-a unit chosen because individual components fail so rarely that
failures-per-hour would produce inconveniently small numbers. The reciprocal quantity, Mean Time To Failure (MTTF) ,
gives the average lifetime in hours:

Table D.1 lists reference FIT rates and MTTF values for components found in a typical GPU training node, grounded in
large-fleet and warehouse-scale experience (Kokolis et al. 2025; Zu et al. 2024; Barroso et al. 2019). These values
assume the steady-state 'useful life' phase of the bathtub curve, where the failure rate is approximately
constant-neither dominated by infant mortality (early life) nor wear-out (end of life).

\( \text{MTTF} = \frac{10^9}{\text{FIT}} \)

Table D.1: Component Failure Rates: Order-of-magnitude reference FIT/MTTF in the steady-state useful-life phase.
Informed by large-GPU research-cluster analysis Kokolis et al. (2025), TPUv4 supercomputer resiliency and operations Zu
et al. (2024), and warehouse-scale machine design Barroso et al. (2019).

| Component     |   FIT Rate |   MTTF (hours) |   MTTF (years) | Typical Failure Mode        |
|---------------|------------|----------------|----------------|-----------------------------|
| GPU           |     20,000 |       50,000.0 |            5.7 | Die defect, thermal fatigue |
| HBM           |      5,000 |        200,000 |           22.8 | Bit-flip accumulation, TSV  |
| NIC           |      6,666 |        150,000 |           17.1 | Transceiver degradation     |
| PSU           |     10,000 |        100,000 |           11.4 | Capacitor aging             |
| PCIe Switch   |      5,000 |        200,000 |           22.8 | Solder joint, ESD damage    |
| Optical Cable |     20,000 |         50,000 |            5.7 | Fiber bend, connector wear  |
| ToR Switch    |      3,333 |        300,000 |           34.2 | ASIC failure, fan bearing   |

Each component in isolation appears highly reliable-a GPU lasts 5.7 years on average. The trouble begins when we ask how
a node behaves with many such components operating simultaneously.

## D.1.2 The MTBF cascade

Acompute node is a series system: if any component fails, the node fails. For independent components with constant
failure rates, the node-level failure rate is the sum of individual rates:

Think of each component as a ticking clock counting down to failure. A node with 8 GPUs, 2 NICs, and 2 PSUs has 12
independent clocks-the node fails when the fi rst clock reaches zero. More clocks mean a shorter expected wait. For a
cluster of 𝑁 identical nodes, the same logic applies one level up:

\( \text{MTBF}_{\text{cluster}} = \frac{\text{MTBF}_{\text{node}}}{N} \)

MTBFcluster = MTBFnode 𝑁 (D.3) This is the MTBF cascade: reliability degrades linearly with component count at each
level, and the levels compound. A node with 5,172-hour MTBF sounds reliable. A cluster of 1,250 such nodes has an MTBF
of just 4.14 hours-a failure every few hours is the expected steady state.

Table D.2 shows how cluster MTBF shrinks as fleet size grows.

Table D.2: Cluster MTBF by Scale: As cluster size grows, the aggregate MTBF shrinks proportionally. At 10,000 GPUs,
failures occur every few hours; at 100,000 GPUs, they occur continuously. Node configuration: 8 GPUs, 2 NICs, 2 PSUs per
node.

|   Cluster GPUs |   Nodes | Cluster MTBF   |   Expected Failures/Day |
|----------------|---------|----------------|-------------------------|
|            256 |      32 | 161.6 hours    |                     0.1 |
|          1,024 |     128 | 40.4 hours     |                     0.6 |
|          2,048 |     256 | 20.2 hours     |                     1.2 |
|          8,192 |   1,024 | 5.1 hours      |                     4.8 |
|         10,000 |   1,250 | 4.1 hours      |                     5.8 |
|        100,000 |  12,500 | 25 minutes     |                    58.0 |

The table makes a visceral point: the transition from 'hundreds of GPUs' to 'tens of thousands' is not merely a
quantitative change but a qualitative one. At 256 GPUs, a full day may pass between failures. At 10,000 GPUs, the
cluster expects multiple failures per shift. At 100,000 GPUs, failures are a continuous background condition-the system
is never fully healthy.

## D.1.3 Probability of failure during a job

Knowing the MTBF tells us the average time between failures, but training jobs have fixed durations. The question
practitioners ask is: what is the probability that my job will be interrupted at least once?

𝑃(≥ 1 failure ) = 1-𝑒 -𝑇 job / MTBF (D.4) When 𝑇 job ≫ MTBF, this probability approaches 1 rapidly. Table D.3 shows the
concrete numbers for various cluster sizes and job durations.

Under the exponential failure model (constant failure rate), the probability of at least one failure during a job of
duration 𝑇 job is:

Table D.3: Probability of At Least One Failure: For large clusters and multi-day jobs, failure is a near-certainty. Any
system operating in the bottom-right region of this table must treat fault tolerance as a core design requirement, not
an optimization.

|   Cluster GPUs | 1 Day (24 h)   | 1 Week (168 h)   | 30 Days (720 h)   |
|----------------|----------------|------------------|-------------------|
|            256 | 13.8%          | 64.6%            | 98.8%             |
|          1,024 | 44.8%          | 98.4%            | > 99.9%           |
|          2,048 | 69.5%          | > 99.9%          | > 99.9%           |
|          8,192 | 99.1%          | > 99.9%          | > 99.9%           |
|         10,000 | 99.7%          | > 99.9%          | > 99.9%           |
|        100,000 | > 99.9%        | > 99.9%          | > 99.9%           |

The message is stark: for any cluster above a few thousand GPUs running jobs longer than a day, the probability of
experiencing at least one failure is effectively 100 percent. This is why Chapter 8 treats fault tolerance not as a
defensive measure but as a fundamental architectural requirement.

The inevitability of failure during long training jobs leads directly to the next question: if we will lose progress,
how do we minimize how much?

The exponential failure model assumes a constant failure rate, which holds during the steady-state useful-life phase.
During burn-in (first few hundred hours) and wear-out (approaching end-of-life), failure rates are higher. In practice,
fleet operators observe that newly deployed nodes exhibit 2-3 × higher failure rates in their first week, making burn-in
testing essential before admitting nodes to production clusters.

## D.2 Checkpoint Optimization

<!-- image -->

## LIGHTBULB Why this matters

Every checkpoint saves progress but costs time. Checkpoint too rarely and a failure destroys hours of training.
Checkpoint too frequently and the overhead of writing checkpoints itself becomes the bottleneck. The Young-Daly formula
gives the mathematically optimal balance point, and it depends on just two measurable quantities: how long a checkpoint
takes to write and how often failures occur.

D.2.1 The Young-Daly model The optimal checkpoint interval balances two competing costs. Writing a checkpoint takes time
𝛿 (the checkpoint cost ), during which no useful training occurs. The longer the interval between checkpoints, however,
the more work is lost when a failure strikes-on average, half the interval. The Young-Daly formula minimizes the
expected total overhead:

The formula assumes that failures follow an exponential distribution (memoryless property) and that checkpoint cost 𝛿 is
small compared to MTBF cluster . Both assumptions hold well for production training clusters: the exponential model fits
observed failure data, and modern checkpointing systems write to fast parallel storage in tens of seconds, while MTBF is
measured in hours.

𝜏 opt =√2×𝛿× MTBFcluster (D.5) where 𝛿 is the checkpoint write time in seconds and MTBF cluster is the cluster MTBF in
seconds. The intuition is geometric-mean-like: when checkpoints are cheap relative to the MTBF ( 𝛿 ≪ MTBFcluster, the
common case), the optimal interval sits between the two time scales. If checkpoints took zero time, the optimal cadence
is every step. If the system never failed, no checkpoints would be required. The square root interpolates between these
extremes.

D.2.2 Checkpoint sizing Checkpoint size determines the write time 𝛿 that feeds into the Young-Daly formula. For common
mixed-precision training checkpoints with the Adaptive Moment Estimation (Adam) optimizer, each parameter requires
approximately 14 bytes of persistent state:

- 2 bytes for BF16 model weights
- 4 bytes for FP32 master weights
- 4 bytes for FP32 first moment (Adam )
- 4 bytes for FP32 second moment (Adam )

𝑚

\(m\)

𝑣

Table D.4: Checkpoint Sizes for Mixed-Precision Adam Training: Each parameter requires about 14 bytes of persistent
checkpoint state (model weights + FP32 master weights + optimizer moments); gradients are normally transient and
recomputed after restore rather than serialized as durable checkpoint state. Write times assume 100 GB/s aggregate
storage bandwidth.

=𝑁

×14

| Model Size   |   Checkpoint Size (GB) | Write Time at 100 GB/s   |
|--------------|------------------------|--------------------------|
| 7B           |                     98 | 0.98 s                   |
| 13B          |                    182 | 1.8 s                    |
| 70B          |                    980 | 9.8 s                    |
| 175B         |                  2,450 | 24.5 s                   |

As Table D.4 shows, at frontier scale (175B+ parameters), checkpoint sizes reach the terabyte range. This makes
checkpoint write time a significant cost that directly affects the Young-Daly optimal interval. The checkpoint
strategies in Chapter 8 discuss techniques for reducing 𝛿 -asynchronous checkpointing, incremental deltas, and
distributed storage-all of which improve the Young-Daly result by shrinking the numerator under the square root.

## D.2.3 Worked example: Optimal checkpoint interval

<!-- image -->

## Example 22.1: Young-Daly: 175B model on a 10,000-GPU cluster

Setup. Consider training a 175B-parameter model on a 10,000-GPU cluster. The cluster MTBF is 4.14 hours (Table D.2). The
checkpoint size is 2,450 GB, and the parallel storage system writes at 100 GB/s. Step 1: Checkpoint write time ( 𝛿 ).

Step 2: Apply the Young-Daly formula. 𝜏 opt =√2×24.5 s ×4.14 h ×3,600 s/h =14.2 min Interpretation. The optimal
checkpoint interval is approximately 14.2 minutes. The overhead from checkpointing alone is opt 2.9 percent of training
time.

\( \frac{\delta}{\tau} \approx \)

𝛿/𝜏 ≈ Implication. If the cluster were doubled to 20,000 GPUs, the MTBF would halve, and the optimal interval would
shrink to 10.1 minutes-checkpointing more frequently because failures happen more often. This illustrates the
fundamental tension at scale: larger clusters are faster but demand more frequent interruption to protect progress.

The boundary conditions of the Young-Daly formula merit attention. When 𝛿 approaches MTBFcluster (checkpoint cost
approaches MTBF), checkpoint and rework overheads become so large that checkpoint/restart alone may fail to maintain
useful forward progress. In such cases, redundancy or elastic training becomes necessary, as discussed in Section D.4.1.

## D.3 Recovery Budgets

<!-- image -->

## LIGHTBULB Why this matters

When a failure occurs, the system does not instantly resume training. Detection, rescheduling, reloading state, and
replaying lost work each consume time. Understanding this recovery anatomy reveals which phase dominates and where to
invest engineering effort.

## D.3.1 The anatomy of recovery time

Recovery is not a single event but a pipeline of phases, each with its own time budget:

Table D.5: Recovery Time Breakdown: Each phase contributes to the total time between failure and full-speed resumption.
For the 10K-GPU, 175B-model scenario, replay dominates because it recomputes work lost since the last checkpoint.

\[ T_{\text{recovery}} = T_{\text{detect}} + T_{\text{reschedule}} + T_{\text{reload}} + T_{\text{replay}} \tag{D.7} \]

| Phase          | Typical Duration   | What Happens                                    |
|----------------|--------------------|-------------------------------------------------|
| 𝑇 detect 𝑇     | 30 s               | Heartbeat timeout expires; failure is confirmed |
| reschedule 𝑇   | 60 s               | Replacement node allocated from spare pool      |
| reload         | 24.5 s             | Checkpoint read from storage into GPU memory    |
| 𝑇 replay       | ~7.1 min           | Recompute training steps since last checkpoint  |
| Total recovery | ~9.0 min           | System fully productive again                   |

𝑇

As Table D.5 illustrates, the key insight is that 𝑇 replay typically dominates, and it is directly controlled by the
checkpoint interval: on average, half the interval must be replayed. This creates a reinforcing loop with the Young-Daly
formula-shorter intervals mean less replay but more checkpoint overhead, and the formula finds the minimum of this sum.

The other phases offer engineering optimization targets. 𝑇 detect can be reduced with more aggressive heartbeat
intervals (at the cost of false positives). 𝑇 reschedule depends on having hot spare nodes preallocated, a fleet
orchestration decision covered in Chapter 9. 𝑇 reload scales with checkpoint size and storage bandwidth, motivating the
checkpoint compression and sharding techniques discussed in Chapter 8.

## D.3.2 Goodput vs. rawput

Not all time spent on a training cluster produces useful progress. Rawput is the total number of training steps executed
(including steps that will be discarded after a failure). Goodput is the number of training steps that actually
contribute to the final model:

- The gap between rawput and goodput comes from three sources: 1. Checkpoint overhead ( ∼ 5 percent): Training pauses
during each checkpoint write. 2. Recovery overhead ( ∼ 5 percent): Time lost to detection, rescheduling, reloading, and
replay after each failure.

\(\frac{1}{T_{\text{wall}}}\)

3. Wasted work: Training steps computed between the last checkpoint and the failure, which must be discarded and
recomputed.

At a 10,000-GPU scale, published reports from Meta, Google, and others consistently show 10-25 percent total overhead
from failures and checkpointing combined. This means that a cluster nominally capable of completing a training run in 30
days actually requires 33-38 days of wall-clock time. The fleet orchestration strategies in Chapter 9 and Chapter 13
focus on narrowing this gapevery percentage point of overhead recovered translates directly to dollars saved and
training time shortened.

<!-- image -->

## Systems Perspective 22.1: The hidden cost of scale

Acommon misconception is that doubling cluster size halves training time. In practice, doubling from 5,000 to 10,000
GPUs halves the MTBF, roughly doubling the failure-related overhead. The effective speedup is less than 2 × , and at
extreme scale, adding more GPUs can actually increase wall-clock time if the fault tolerance mechanisms cannot keep
pace. This is the reliability analogue of Amdahl's Law: the serial overhead of recovery bounds the benefit of
parallelism.

## D.4 Strategy Selection

<!-- image -->

## LIGHTBULB Why this matters

Checkpoint/restart is not the only fault tolerance strategy. For serving workloads where downtime is measured in lost
revenue, redundancy provides a fundamentally different tradeoff. For elastic training, the system can shrink around
failures rather than stopping. Choosing the right strategy depends on the workload's tolerance for latency, cost, and
complexity.

## D.4.1 Checkpoint/restart vs. redundancy vs. elastic training

The three canonical strategies represent different points in the trade-off space between cost, complexity, and recovery
speed.

Checkpoint/restart periodically saves full system state and rolls back to the last checkpoint after failure. It is the
workhorse of large-scale training: conceptually simple, well-understood, and effective when MTBF is much larger than
checkpoint cost. The weakness is that recovery requires stopping all workers and replaying lost computation.

Elastic training allows the training job to continue with fewer workers when a failure occurs, rather than stopping
entirely. Workers are added back when replacement nodes become available. This minimizes wall-clock interruption but
requires frameworks that support dynamic world-size changes (for example, TorchElastic), and it introduces complexity in
learning rate adjustment and gradient normalization. Table D.6 summarizes the trade-offs.

Redundancy maintains duplicate copies of state or computation. If one replica fails, another immediately takes over.
This is the dominant strategy for inference serving, where even seconds of downtime are unacceptable. The cost is 2-3 ×
the compute resources, which is prohibitive for training but justified for revenue-critical serving.

Table D.6: Fault Tolerance Strategy Comparison: Each strategy excels in a different regime. Real-world systems often
combine strategies: checkpoint/restart for training with redundancy for the metadata service and checkpoint storage
layer.

| Criterion         | Checkpoint/Restart           | Redundancy                 | Elastic Training               |
|-------------------|------------------------------|----------------------------|--------------------------------|
| Recovery latency  | Minutes (replay)             | Milliseconds (failover)    | Seconds (reconfigure)          |
| Resource overhead | ~3-13 percent (storage + IO) | 100-200 percent (replicas) | ~5-10 percent (spare capacity) |
| Workload fit      | Training (batch)             | Serving (online)           | Training (long-running)        |
| Implementation    | Simple                       | Moderate                   | Complex                        |
| State management  | Periodic snapshots           | Continuous replication     | Distributed with resharding    |
| Failure mode      | Job pauses, replays          | Transparent to user        | Throughput dip, continues      |

## D.4.2 The availability stacking formula

𝐴

For serving workloads, availability is typically expressed as a percentage: 99 percent ('two nines'), 99.9 percent
('three nines'), and so on. Redundancy improves availability by running 𝑘 independent replicas. The system is
unavailable only when all replicas are simultaneously down: 𝐴 system =1-(1-𝐴) 𝑘 (D.8) where is the availability of a
single replica and is the number of replicas.

Table D.7: Availability Stacking with Independent Replicas: Starting from a single-replica availability of 99 percent,
each additional replica dramatically reduces expected downtime. Assumes replica failures are independent. Replicas 𝑘 1

𝑘

|   Replicas | System Availability   |   Nines | Downtime per Year   |
|------------|-----------------------|---------|---------------------|
|          1 | 99.00%                |     2.0 | 87.6 hours          |
|          2 | 99.9900%              |     4.0 | 53 minutes          |
|          3 | 99.9999%              |     6.0 | 1 minutes           |

As Table D.7 shows, the power of stacking is dramatic: two replicas of a 99 percent-available system yield 99.99 percent
availability, reducing annual downtime from roughly 87 hours to under an hour. This is why inference serving systems
almost universally deploy multiple replicas behind a load balancer-the cost of an extra replica is small compared to the
business value of four-nines availability.

The independence assumption is critical, however. Correlated failures-power outages affecting an entire rack, software
bugs triggered by a specific input, or network partitions isolating a failure domain-defeat availability stacking. This
is why Chapter 8 emphasizes failure domain isolation: replicas must be placed in different racks, different power zones,
and ideally different data centers to ensure that their failure modes are truly independent.

## D.5 Fallacies and Pitfalls

Pitfall: Checkpointing as frequently as possible to minimize lost work. More frequent checkpoints reduce the expected
replay time after a failure, but each checkpoint incurs a fixed write cost 𝛿 . Checkpointing every minute when 𝛿 is 30
seconds means spending 50 percent of training time just writing checkpoints. The Young-Daly formula (Equation D.5) gives
the mathematically optimal balance; deviating in either direction increases total overhead.

Fallacy: If each GPU is 99.99 percent reliable, a 10,000-GPU cluster is also 99.99 percent reliable. Reliability does
not compose by averaging-it compounds by multiplication. A system of 𝑁 serial components, each with availability 𝐴, has
aggregate availability 𝐴 𝑁 . For 𝐴 = 0.9999 and 𝑁 = 10,000: 0.9999 10,000 ≈0.37 . The cluster is down 63 percent of the
time. Individual component reliability is necessary but nowhere near sufficient; system-level fault tolerance must be
designed explicitly.

Fallacy: Adding more GPUs always speeds up training.

Pitfall: Treating failures as independent when they share infrastructure. The availability stacking formula 𝐴 system
=1-(1-𝐴) 𝑘 assumes independent failures. In practice, correlated failures-a power distribution unit taking out an entire
rack, a firmware bug affecting all GPUs of the same generation, or a network partition isolating a failure domain-are
the dominant source of multi-replica outages. The correlation, not the individual failure rate, determines whether
redundancy actually delivers the expected availability.

Beyond the well-known communication overhead of distributed training, each additional GPU increases the aggregate
failure rate. At extreme scale, the time lost to failures and recovery can exceed the time saved by additional
parallelism. This is the reliability version of diminishing returns: there exists a cluster size beyond which adding
GPUs increases wall-clock time rather than decreasing it.

Pitfall: Ignoring recovery time when planning training budgets.

A training run scheduled for 30 days on a 10,000-GPU cluster will require 33-38 days of wallclock time after accounting
for failures and checkpointing overhead. Budgeting only for the raw compute time leads to missed deadlines, cost
overruns, and pressure to cut corners on checkpoint frequency-which makes the problem worse.

## Summary

- Key Takeaways: Failure as a physical constraint
- Failure rate scales linearly with component count. Asingle GPU fails once per 5.7 years; a 10,000-GPU cluster
experiences a failure every 4.14 hours. At fleet scale, failure is a continuous background condition, not an exceptional
event.
- The MTBF cascade compounds through system levels. Node MTBF is determined by the weakest component type; cluster MTBF
divides by node count. Table D.2 provides the reference numbers for capacity planning.
- Job failure probability approaches certainty quickly. For clusters above a few thousand GPUs running multi-day jobs,
the probability of at least one failure exceeds 99 percent. Fault tolerance is not optional at this scale-it is a
prerequisite for completing any training run. · The Young-Daly formula 𝜏 opt = √ 2𝛿𝑀 optimizes checkpoint frequency. It
balances the cost of writing checkpoints against the cost of lost work, requiring only two measurable inputs: checkpoint
write time and cluster MTBF.
- Recovery has four phases: Detection, rescheduling, reloading, and replay. Replay typically dominates and is controlled
by the checkpoint interval. Each phase offers distinct optimization opportunities.
- Strategy selection depends on workload type. Checkpoint/restart suits batch training. Redundancy suits
latency-sensitive serving. Elastic training bridges the two but adds complexity.

- Availability stacks exponentially with independent replicas but collapses under correlated failures. Failure domain
isolation is the prerequisite that makes redundancy effective.

