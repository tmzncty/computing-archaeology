# CRT Refresh Experiment

Historical question:

> Why can a memory that physically forgets still present apparently stable bits to software?

This experiment accompanies [`../../docs/memory/why-crt-became-ram.md`](../../docs/memory/why-crt-became-ram.md).

## Model

Each cell has a synthetic signal strength. Signal decays continuously. A refresh scanner revisits cells and restores their signal.

The experiment varies memory capacity while holding scan bandwidth fixed.

Run:

```bash
python experiments/crt-refresh/crt_refresh.py
```

No third-party dependencies are required.

## Historical anchor

Tom Kilburn's December 1947 report describes CRT charge storage with short-term retention on the order of 0.2 seconds and long-term retention achieved by regeneration more frequently than five times per second.

- Tom Kilburn, “A Storage System for Use with Binary Digital Computing Machines,” 1947: https://curation.cs.manchester.ac.uk/digital60/www.digital60.org/birth/manchestercomputers/mark1/documents/report1947.html

## What the default numbers mean

Only the existence of decay/regeneration is historically anchored.

The script's:

- decay rate;
- threshold;
- scan rate;
- time step;
- failure criterion

are **synthetic teaching parameters**. They are not measurements of a Williams tube.

## What to try

Increase the number of cells without increasing scan bandwidth.

Then change:

```python
scan_capacity_per_second
```

and:

```python
decay_per_second
```

The model makes one systems point visible:

> if physical state decays, maximum useful capacity depends partly on how quickly the machine can revisit and repair that state.

## What this cannot prove

It does not model:

- CRT secondary emission;
- dot/dash charge patterns;
- beam deflection dynamics;
- pickup-plate transients;
- focus errors;
- screen defects;
- actual Manchester timing;
- historical refresh scheduling.

It is a constraint model, not a Williams-tube emulator.