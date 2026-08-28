# Tape Locality Experiment

Historical question:

> Why can a storage device have high streaming bandwidth and still punish random access?

This experiment accompanies [`../../docs/memory/why-tape-made-you-think-sequentially.md`](../../docs/memory/why-tape-made-you-think-sequentially.md).

Run:

```bash
python experiments/tape-locality/tape_locality.py
```

## Two models

### 1. Positioning locality

A synthetic tape contains 1,000 ordered records. The script compares the physical movement needed to request them:

- in tape order;
- in a shuffled order.

Distance is measured in abstract record positions.

### 2. Blocking

The script also treats every physical block as paying a fixed gap overhead and calculates useful-media efficiency as more logical records are grouped into each block.

## Historical anchors

- Computer History Museum, early UNISERVO/IBM 726 tape history: https://www.computerhistory.org/storageengine/tape-unit-developed-for-data-storage/
- IBM, *Data File Handbook*, 1966, including nominal interrecord-gap specifications for tape families: https://www.bitsavers.org/pdf/ibm/generalInfo/C20-1638-1_Data_File_Handbook_Mar66.pdf
- IBM, “Magnetic tape”: https://www.ibm.com/history/magnetic-tape

## Synthetic parameters

The script's:

- movement unit;
- 100-byte logical record;
- 200-byte-equivalent gap;
- random request order

are teaching assumptions.

The gap value is deliberately **not** a conversion of a historical tape gap into bytes.

## What it demonstrates

- sequential requests exploit physical locality;
- random request order can cause much more positioning work;
- a fixed per-block overhead creates pressure toward blocking.

## What it cannot prove

It does not model:

- reel acceleration;
- vacuum columns;
- tape speed;
- rewind time;
- density;
- tape marks;
- read errors;
- a specific IBM or UNIVAC controller;
- historical operating-system buffering.

It is a geometry/cost model, not a tape-drive emulator.