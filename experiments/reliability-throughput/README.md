# Reliability versus throughput experiment

This dependency-free Python model accompanies [`docs/electronic/why-vacuum-tubes.md`](../../docs/electronic/why-vacuum-tubes.md).

## Historical question

A fast switching technology can be less convenient to maintain than a slower one. Does that automatically make the fast machine less useful?

No. System value depends on both speed and availability.

This tiny model compares:

```text
nominal operation rate
× expected availability
= effective long-run throughput
```

Availability is estimated from two assumptions:

```text
MTBF / (MTBF + repair time)
```

## Run

```bash
python experiments/reliability-throughput/reliability_throughput.py
```

Try your own hypothetical systems:

```bash
python experiments/reliability-throughput/reliability_throughput.py \
  --a-speed 200 \
  --a-mtbf 200 \
  --a-repair 0.25 \
  --b-speed 10000 \
  --b-mtbf 6 \
  --b-repair 0.5
```

## Defaults are deliberately **not historical measurements**

The script labels its defaults hypothetical. They are chosen only to make the tradeoff easy to see.

Do not read:

```text
system A = a real relay computer
system B = ENIAC or Colossus
```

into the output.

Real machines require evidence for:

- what counts as a failure;
- failure distributions;
- preventive maintenance;
- degraded operation;
- diagnostic time;
- restart/recovery cost;
- component age;
- operating schedule;
- workload and operation definition.

A single MTBF number collapses all of that complexity.

## What it demonstrates

The model exposes one systems principle used in the vacuum-tube article:

> a component technology can be less reliable or require more maintenance and still enable much greater useful throughput if its speed advantage is large enough.

It also makes repairability visible. Two systems with identical failure intervals can have very different availability if one can be diagnosed and repaired much faster.

## What it does **not** demonstrate

This model does not establish historical ENIAC, Colossus, relay, or vacuum-tube reliability figures. It does not prove what any historical designer believed. It ignores failure clustering, warm-up, preventive replacement, component derating, power cycling, and multi-component reliability.

Those historical claims remain grounded in the sources cited in the article.

The point of the experiment is narrower: **reliability and speed must be evaluated at the system-throughput level, not by judging one component in isolation.**
