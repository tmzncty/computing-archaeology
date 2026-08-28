# CMP planarity

This synthetic experiment treats a wafer cross-section as a small list of local heights.

Run:

```bash
python experiments/cmp-planarity/cmp_planarity.py
```

It compares:

- the original topography;
- a deliberately simplistic uniform-removal model;
- a density-sensitive removal model.

The numbers are hypothetical. This is **not** a CMP simulator and is not calibrated to any historical IBM process, pad, slurry, film, or pattern-density model.

Its purpose is to expose one engineering fact: polishing faster is not the same as polishing uniformly, and the useful process objective is coupled to local pattern geometry, defects, selectivity, and throughput.

Historical context: [`../../docs/materials/why-cmp-created-a-slurry-and-pad-supply-chain.md`](../../docs/materials/why-cmp-created-a-slurry-and-pad-supply-chain.md).