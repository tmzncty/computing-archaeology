# Batch economics experiment

This dependency-free Python model accompanies [`docs/interaction/why-batch-processing-made-sense.md`](../../docs/interaction/why-batch-processing-made-sense.md).

## Historical question

Why might an installation deliberately remove programmers from direct console access and submit work in batches?

One important answer is **machine occupancy**. If every short job requires a long machine-side setup by its programmer, an expensive computer can spend most of its scheduled time waiting for people rather than computing.

## Run

```bash
python experiments/batch-economics/batch_economics.py
```

The defaults are intentionally hypothetical:

```text
20 jobs
30 s useful computation per job
120 s direct machine-side setup per job
240 s setup once for the batch
3 s standardized transition between batch jobs
```

Change the assumptions:

```bash
python experiments/batch-economics/batch_economics.py \
  --jobs 50 \
  --compute 10 \
  --direct-setup 180 \
  --batch-setup 300 \
  --transition 2
```

## Model

The direct strategy pays:

```text
setup + compute
```

for every job while the central machine is occupied.

The batch strategy pays one larger batch setup, then a small standardized transition between jobs:

```text
batch setup + compute jobs + transitions
```

The program reports:

- useful compute seconds;
- total central-machine occupancy;
- compute utilization;
- jobs per hour.

## Why response time is deliberately absent

A batch system can increase installation throughput while making the owner of one particular job wait longer for an answer. That is the central tradeoff described in the article.

This script therefore ends by warning that throughput and interactive latency are different objective functions.

A more elaborate future model could add:

- submission queues;
- card-to-tape and tape-to-print stations;
- multiple operators;
- job priorities;
- failures and restart costs;
- human think time;
- time-sharing as a competing strategy.

## What it demonstrates

- repeated machine-side setup can dominate short computations;
- moving preparation off the critical path can improve utilization;
- standardized job transitions can make many small jobs economical;
- “faster for the installation” does not imply “faster feedback for the user.”

## What it does **not** demonstrate

The default numbers are **not historical measurements of an IBM 704, GM Research, or North American Aviation installation**.

The model does not reproduce GM-NAA I/O, an actual 704 monitor, real card/tape speeds, operator staffing, or historical queue policies. It is an explanatory cost model only.

For historical workflow evidence, see Robert L. Patrick's CHM oral history and retrospective cited in the article:

- https://archive.computerhistory.org/resources/text/Oral_History/Patrick_Robert/Patrick_Robert.oral_history_transcript.2006.102657941.pdf
- https://softwarepreservation.computerhistory.org/os/gm.html
