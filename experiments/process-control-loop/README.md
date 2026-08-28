# Process-control loop

A deliberately small synthetic model of a process that drifts while measurements are taken only periodically.

Run:

```bash
python experiments/process-control-loop/process_control_loop.py
```

The model exposes one simple constraint: if a process drifts between observations, more material can be processed after the excursion starts and before a hold is triggered.

The defaults are **not historical fab parameters**. Change `drift_per_step`, `measure_every`, and `control_limit` to explore the relationship between measurement frequency and exposure to an excursion.

This model cannot prove how a particular fab implemented SPC, how control limits were chosen, or whether a real measured parameter predicts final yield.