# Layout hierarchy

A toy representation-cost model for a repeated array.

Run:

```bash
python experiments/layout-hierarchy/layout_hierarchy.py
```

The model compares:

- repeating every shape for every instance;
- defining one cell and referencing it many times.

The units are invented and are **not** GDSII bytes, mask-writer shot counts, file sizes, or real data-preparation costs.

Its purpose is simply to expose why hierarchical layout databases became valuable when integrated circuits contained large repeated structures.