# Time-Sharing Think-Time Experiment

Historical question:

> Why can many interactive users share one expensive CPU even when each person feels continuously connected to the machine?

The key asymmetry is that human interaction is bursty.

A user may think for seconds and then demand only a short burst of CPU time.

## What the script models

Each modeled user produces repeated requests consisting of:

```text
human think interval
-> short CPU burst
```

The script reports:

- how little CPU one reserved interactive user would consume;
- aggregate offered CPU load from many such users;
- response time in a tiny round-robin queue model;
- observed CPU utilization in the synthetic workload.

Default assumptions:

```text
20 users
10 seconds between requests
0.05 CPU seconds per request
0.02-second scheduling quantum
```

These are **hypothetical teaching values**, not CTSS measurements.

## Run

```bash
python experiments/time-sharing/time_sharing.py
```

Increase the user population:

```bash
python experiments/time-sharing/time_sharing.py --users 100
```

Make workloads more CPU-heavy:

```bash
python experiments/time-sharing/time_sharing.py \
  --users 40 \
  --think 3 \
  --cpu 0.2 \
  --quantum 0.05
```

Watch the system cross from spare capacity into queueing pressure.

## Why this is historically useful

A single interactive user may occupy a terminal for minutes while requiring only fractions of a second of computation during that period.

If the machine is reserved exclusively for that person, the CPU can spend most of its time idle.

If many independent users are multiplexed, their short requests can fill one another's think time.

This helps explain the economic opening for time-sharing.

It does **not** explain the whole system.

Time-sharing also requires mechanisms such as:

- timer interrupts;
- memory protection;
- relocation;
- context switching;
- secondary storage;
- terminal communications;
- buffering;
- scheduling policy;
- accounting and identity.

The companion CTSS case study is:

[`../../case-studies/ctss/from-batch-to-conversation.md`](../../case-studies/ctss/from-batch-to-conversation.md)

## What this does **not** model

It does not reproduce:

- CTSS's scheduler;
- IBM 7094 timing;
- swapping/drum/disk latency;
- terminal I/O service time;
- context-switch overhead;
- memory pressure;
- priority classes;
- actual user populations;
- correlated users;
- long-running batch jobs;
- device contention.

Requests are deterministically staggered for reproducibility. Real user activity is much messier.

## Interpretation rule

The experiment demonstrates only one structural fact:

> intermittent human demand can leave enough gaps for a shared processor to serve many users.

It does not establish that any particular historical time-sharing installation had a given capacity or response time.
