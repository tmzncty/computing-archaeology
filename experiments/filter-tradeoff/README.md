# Filter tradeoff

This synthetic model exposes a basic filtration compromise: tighter retention can improve contaminant capture while increasing pressure drop, and filter loading can further consume flow margin.

Run:

```bash
python experiments/filter-tradeoff/filter_tradeoff.py
```

All numbers are hypothetical. This is **not** a HEPA/ULPA performance model, membrane-sizing tool, gas-filter model, CMP-filter model, or maintenance criterion.

The purpose is only to show why a semiconductor filter is a process component with capture, pressure-drop, loading, and replacement tradeoffs rather than an ideal zero-cost sieve.

Historical context: [`../../docs/materials/why-filters-became-consumable-process-parts.md`](../../docs/materials/why-filters-became-consumable-process-parts.md).