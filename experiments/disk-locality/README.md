# Disk Locality Experiment

Historical question:

> Why can a random-access disk make direct lookup possible while still strongly rewarding locality?

Run:

```bash
python experiments/disk-locality/disk_locality.py
```

The model assigns records to synthetic tracks and charges invented costs for:

- radial seek distance;
- rotational position;
- transfer.

It compares the same selected records in random order and in track-clustered order, plus a sequential run.

## What it demonstrates

Random access removes the requirement to scan every earlier record, but physical positioning still costs time. Reordering work so nearby records are accessed together can reduce head movement dramatically.

## What it does not reproduce

This is **not** an IBM 350 simulator. The default timing constants are synthetic and should not be cited as historical RAMAC measurements.

It omits:

- multiple disk surfaces;
- exact IBM actuator geometry;
- real rotational scheduling;
- controller behavior;
- encoding;
- head settling;
- errors and retries;
- queueing.

Historical context: [`../../docs/memory/why-disk-made-random-access-a-business-feature.md`](../../docs/memory/why-disk-made-random-access-a-business-feature.md).
