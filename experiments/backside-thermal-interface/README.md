# Backside thermal interface

A synthetic radial-zone model paired with `docs/manufacturing/why-backside-helium-became-a-wafer-interface.md`.

It varies helium coupling and leakage penalties while holding chuck temperature constant, showing why equal coolant setpoint does not imply equal wafer temperature.

It is not a heat-transfer, ESC, helium-pressure, or process-equipment design tool.

```bash
python experiments/backside-thermal-interface/backside_thermal_interface.py
```
