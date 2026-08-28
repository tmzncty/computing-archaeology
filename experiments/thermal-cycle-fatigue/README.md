# Thermal-cycle fatigue

A synthetic package/board fatigue proxy.

Run:

```bash
python experiments/thermal-cycle-fatigue/thermal_cycle_fatigue.py
```

The script converts CTE mismatch and temperature swing into a simple strain proxy, then applies a toy inverse-power fatigue relationship.

All parameters are synthetic. This is **not** a Coffin–Manson fit, finite-element model, or lifetime prediction for any solder alloy, BGA, QFN, DIP, PCB, or spacecraft assembly.

Its purpose is only to expose why package/board mismatch and larger thermal excursions can consume a fatigue-cycle budget nonlinearly.