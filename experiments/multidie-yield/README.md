# Multidie yield

A toy comparison between one monolithic die and a four-die assembly.

Run:

```bash
python experiments/multidie-yield/multidie_yield.py
```

The model intentionally keeps total silicon area identical and adds a synthetic package/assembly yield to the multi-die case.

It is **not** a chiplet cost model. Real outcomes depend on die partitioning, known-good-die screening, process-node mixing, reticle limits, package/interposer cost, repair/redundancy, assembly yield, test strategy, bandwidth, power, thermal design, and product binning.

Its purpose is to show that multi-die integration does not eliminate yield economics; it moves part of the problem into assembly and interface yield.