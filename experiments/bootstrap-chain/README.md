# Bootstrap Chain Experiment

Historical question:

> How can a machine load a large software environment when it begins with almost no software at all?

This experiment accompanies [`../../docs/interaction/why-booting-started-with-switches.md`](../../docs/interaction/why-booting-started-with-switches.md).

Run:

```bash
python experiments/bootstrap-chain/bootstrap_chain.py
```

## Model

The script represents startup as a ladder:

```text
manual seed
→ simple loader
→ richer loader
→ operating environment
```

Only the first stage requires manual word entry. Each later stage can load a much larger representation.

## Historical anchor

DEC documentation describes the PDP-8 RIM loader as a short program toggled into core through console switches, after which paper tape could load larger programs.

- DEC, *Small Computer Handbook*, 1970: https://bitsavers.org/pdf/dec/pdp8/handbooks/SmallComputerHandbook_1970.pdf
- DEC, *Introduction to Programming*, 1969: https://bitsavers.org/pdf/dec/pdp8/handbooks/IntroToProgramming1969.pdf

## Synthetic parameters

The default stage capacities are invented.

The first stage uses 17 words because DEC documentation describes a RIM loader of approximately that size in relevant PDP-8 material, but the later capacities are not historical PDP-8 measurements.

## What it demonstrates

A bootstrap chain lets a very small trusted/manual mechanism create access to a much larger software environment.

The interesting quantity is not the exact ratio printed by the script. It is the staged **capability amplification**.

## What it cannot prove

It does not emulate:

- PDP-8 instructions;
- RIM or BIN tape encoding;
- Teletype timing;
- device flags;
- core-memory loading;
- a historical operating system.

It is a conceptual loader-chain model.