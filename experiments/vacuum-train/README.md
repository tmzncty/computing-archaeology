# Vacuum train

A synthetic model paired with `docs/facilities/why-semiconductor-vacuum-went-dry.md`.

It treats turbo and backing capacity as a serial vacuum train and adds optional harsh-process and contamination penalties.

The numbers are not real pump speeds, gas loads, pressures, maintenance intervals, or semiconductor process conditions. This is not a pump-sizing or safety tool.

```bash
python experiments/vacuum-train/vacuum_train.py
```
