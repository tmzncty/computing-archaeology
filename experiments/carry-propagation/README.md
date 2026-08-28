# Carry Propagation Experiment

Historical question:

> How does positional radix change the number of digit mechanisms, the frequency of carries, and the worst-case carry chain?

This experiment is a deliberately abstract model. It does **not** simulate the Pascaline, a Babbage engine, or any other historical calculator.

## What it measures

For a chosen numeric range and several radices, the script repeatedly increments a counter and reports:

- number of digit positions required for the range;
- average digit updates per increment;
- average carry-boundary crossings per increment;
- longest carry chain observed;
- a user-adjustable synthetic cost score.

The default radices are:

```text
2, 4, 8, 10, 16
```

## Why this matters historically

A lower radix gives each digit fewer stable states but requires more digit positions for the same numeric range. During repeated counting it also reaches the maximum digit more frequently, so carries happen more often.

A higher radix needs fewer positions and carries less frequently, but each position must reliably distinguish more states.

Those facts do **not** determine a universal best radix. They reveal why radix is an engineering tradeoff once digits become mechanisms.

The companion article is:

[`../../docs/mechanical/why-carry-is-a-machine-problem.md`](../../docs/mechanical/why-carry-is-a-machine-problem.md)

## Run

```bash
python experiments/carry-propagation/carry_propagation.py
```

No third-party dependencies are required.

Example variations:

```bash
python experiments/carry-propagation/carry_propagation.py \
  --max-value 999999 \
  --increments 200000 \
  --radices 2,3,4,5,8,10,12,16
```

## Synthetic cost model

The script also prints a deliberately artificial score:

```text
fixed digit cost
+ stable-state complexity
+ average carry cost
```

You can change the weights:

```bash
python experiments/carry-propagation/carry_propagation.py \
  --wheel-cost 30 \
  --state-cost 0.2 \
  --carry-cost 12
```

The score is useful precisely because it is **not authoritative**. If you change the assumptions, the apparent winner can change.

That is the lesson.

## What the model cannot prove

It does not model:

- actual gear geometry;
- tooth counts;
- spring or gravity mechanisms;
- friction;
- torque;
- backlash;
- wheel inertia;
- detent accuracy;
- carry timing;
- manufacturing tolerances;
- materials;
- operator force;
- historical cost data.

The `state_cost` term is only a conceptual proxy for the fact that a radix-10 digit must distinguish more positions than a radix-2 digit. It must **not** be interpreted as a claim that a decimal wheel literally costs five times as much as a binary one.

## Source anchors

- Blaise Pascal, *Avis nécessaire…*, 1645 — Pascal's own discussion of automatic carries/borrows, practical mechanism, durability, and the limits of abstract simplification.
- ACONIT / Inria, “La Pascaline” — museum explanation of the `sautoir` carry mechanism.
- Computer History Museum, Babbage Engine exhibit — decimal/radix tradeoffs and the mechanical value of addition-only finite differences.

The experiment tests a mechanism-level intuition. It does not establish what any historical designer intended unless a source states that intention.
