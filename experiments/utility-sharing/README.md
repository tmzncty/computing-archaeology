# Utility Sharing Experiment

Historical question:

> What new constraints appear when a computer is expected to behave like a continuously available shared utility rather than a machine that runs isolated jobs?

Run:

```bash
python experiments/utility-sharing/utility_sharing.py
```

The experiment contains three tiny models:

- object-level read/write permissions;
- memory savings from sharing a pure procedure rather than copying it into every process;
- a synthetic availability calculation using MTBF and recovery time.

## What it demonstrates

A shared utility needs explicit mechanisms for:

- isolation;
- selective sharing;
- common code;
- recovery and availability.

These are systems properties, not merely scheduler features.

## What it does not reproduce

This script is **not** a Multics emulator. It does not implement segmentation, paging, protection rings, descriptors, dynamic linking, GE 645 instructions, Multics access-control lists, or real recovery behavior.

The availability numbers are invented teaching parameters.

Historical context: [`../../case-studies/multics/when-a-computer-became-a-utility.md`](../../case-studies/multics/when-a-computer-became-a-utility.md).
