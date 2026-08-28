# Firmware Iteration Experiment

Question:

> What happens to prototype feedback time when firmware can be erased and reprogrammed locally instead of requiring a new fixed-ROM manufacturing turn?

The model compares two synthetic development loops.

Run:

```bash
python experiments/firmware-iteration/firmware_iteration.py
```

The timing assumptions are invented and intentionally simple. The experiment demonstrates where delay sits in the workflow; it does not reproduce Intel's actual 1702 development schedule.