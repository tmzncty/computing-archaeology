# Shared Bus / DMA Experiment

Historical question:

> What changes when a peripheral can become a bus master and transfer data directly to memory instead of making the CPU copy every word?

Run:

```bash
python experiments/shared-bus/shared_bus.py
```

The experiment has two deliberately simple parts:

1. compare CPU-mediated I/O with a synthetic DMA-style transfer count;
2. place CPU, disk, and network requests onto one shared bus with fixed priorities.

## What it demonstrates

A common bus is not passive wiring. It is a shared resource with ownership, arbitration, priority, and contention.

DMA can reduce repetitive CPU involvement, but DMA devices still consume bus/memory bandwidth and can delay other participants.

## What it does not reproduce

The model does not implement real UNIBUS electrical behavior, timing, grant chains, NPR/BR details, termination, interrupt vectors, or PDP-11 instruction execution.

All priorities, transfer widths, and workloads are synthetic.

Historical context: [`../../docs/architecture/why-unibus-made-a-small-computer-an-ecosystem.md`](../../docs/architecture/why-unibus-made-a-small-computer-an-ecosystem.md).
