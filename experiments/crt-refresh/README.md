# CRT Refresh Experiment

Historical question:

> Why can a memory that physically forgets still present apparently stable bits to software?

This experiment accompanies [`../../docs/memory/why-crt-became-ram.md`](../../docs/memory/why-crt-became-ram.md).

## Model

Each cell has a synthetic signal strength. The model approximates decay in discrete time steps. A refresh scanner revisits cells and restores their signal.

The experiment varies memory capacity while holding scan bandwidth fixed.

Run:

```bash
python experiments/crt-refresh/crt_refresh.py
```

No third-party dependencies are required.

### What happens in one tick?

`refreshes_per_second` sets the simulation tick rate, not the number of complete passes over memory. At each tick the model:

1. subtracts one tick's decay from every cell;
2. records any cell whose signal is **below** the threshold as ever lost;
3. spends the cumulative scan budget on round-robin visits, resetting each visited signal to 1.

`scan_capacity_per_second` counts cell visits per second. Fractional capacity carries into later ticks. Visits within a tick are treated as instantaneous; this is not continuous beam scheduling. `lost_cells` counts cells that **ever** crossed the threshold: a later signal reset does not erase that loss or demonstrate recovery of the stored bit. The model does not simulate corrupted bit values.

Only complete ticks run: the tick count is `floor(seconds * refreshes_per_second)`. Duration, tick rate, and scan capacity use their caller-visible decimal strings for exact tick/visit budgeting. Thus 0.29 seconds at 100 ticks/s runs 29 ticks, even though binary floating-point multiplication can produce 28.999999999999996. A duration of 0.285 runs 28 ticks; the remaining half-tick applies neither decay nor scanning. Signal decay itself still uses floating-point arithmetic, so this is not an exact electrical model.

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

### Catch the last tick

From the repository root, compare two short runs with no scanning:

```python
from runpy import run_path

simulate = run_path("experiments/crt-refresh/crt_refresh.py")["simulate"]
for seconds in (0.28, 0.29):
    result = simulate(1, seconds, 100.0, 0.0, 1.0, threshold=0.715)
    print(seconds, result.lost_cells)
# 0.28 0
# 0.29 1
```

After 28 ticks the signal is approximately 0.72; after 29 it is 0.71. The synthetic 0.715 threshold lies between them. Dropping the last tick would conceal a loss, not just undercount refresh work. These values illustrate the model's bookkeeping, not historical retention measurements.

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
