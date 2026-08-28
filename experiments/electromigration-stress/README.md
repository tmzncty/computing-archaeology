# Electromigration stress

A synthetic relative-lifetime proxy showing why current density and temperature become interconnect-design constraints.

Run:

```bash
python experiments/electromigration-stress/electromigration_stress.py
```

The script uses a Black-equation-like mathematical form only to expose sensitivity. Its exponent, activation energy, current-density units, and baseline are **not calibrated to any historical or modern semiconductor process**.

It cannot predict real lifetime. Real electromigration depends on metallurgy, geometry, grain structure, interfaces, current crowding, stress, process integration, and detailed temperature/current history.