# Wafer Scale Experiment

Question:

> Why does a larger wafer offer more candidate die while still depending on die area and yield?

This synthetic geometry model estimates gross die count from wafer diameter and die area, then applies a simple yield fraction.

Run:

```bash
python experiments/wafer-scale/wafer_scale.py
```

This is not a fab cost model. It ignores edge-placement geometry, process-specific defect models, tool depreciation, cycle time, wafer cost, and real wafer exclusion zones.