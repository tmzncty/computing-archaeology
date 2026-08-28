# Core Memory Experiment

Historical question:

> How can two shared coordinate wires select one magnetic bit, and why does a destructive read require restoration?

This is a **conceptual control-sequence model**, not a magnetic-field simulator or a faithful Whirlwind emulator.

## What it demonstrates

The script builds a small bit plane and exposes three ideas.

### 1. Half selection

Selecting one row gives every core on that row a normalized excitation of `0.5`.

Selecting one column does the same for that column.

### 2. Coincidence

At the selected row/column intersection, the two contributions add:

```text
0.5 + 0.5 = 1.0
```

The model treats `1.0` as the conceptual switching threshold.

This illustrates the addressing idea in Jay Forrester's coincident-current work: shared coordinate lines can select one element because the material responds differently to partial and coincident excitation.

### 3. Destructive read and restore

The model reads a bit by forcing it to zero.

If the old value was one, a conceptual sense pulse occurs because the state changed. The model can then restore the original one.

Run with `--no-restore` to leave the read bit destroyed.

## Run

```bash
python experiments/core-memory/core_memory.py
```

Try another address:

```bash
python experiments/core-memory/core_memory.py --size 8 --row 5 --col 3
```

Show the consequence of skipping restore:

```bash
python experiments/core-memory/core_memory.py --row 1 --col 2 --no-restore
```

No third-party dependencies are required.

## What this does **not** model

It does not numerically reproduce:

- a ferrite hysteresis curve;
- actual switching current;
- pulse width;
- sense-amplifier voltage;
- inhibit-wire schemes;
- temperature effects;
- half-select disturbance;
- noise margins;
- word-oriented plane stacking;
- historical core sizes;
- Whirlwind timing;
- manufacturing defects.

The normalized `0.5` and `1.0` values are pedagogical labels, not measured amperes.

## Source anchors

- Jay W. Forrester, “Digital Information Storage in Three Dimensions Using Magnetic Cores,” *Journal of Applied Physics* 22(1), 1951, pp. 44–48.
- Jay W. Forrester, U.S. Patent 2,736,880, filed 1951.
- Smithsonian Whirlwind magnetic-core plane object record.
- Computer History Museum, magnetic-core memory and Storage Engine exhibits.

The companion article is:

[`../../docs/memory/why-core-memory-was-worth-weaving.md`](../../docs/memory/why-core-memory-was-worth-weaving.md)

## Interpretation rule

The experiment demonstrates why the **control sequence** is coherent. It does not establish who invented every component of core memory, the exact behavior of every historical array, or the economics of any particular installation.
