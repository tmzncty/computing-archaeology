# Photoresist process window

This synthetic model treats exposure dose and development time as coupled process variables.

Run:

```bash
python experiments/resist-window/resist_window.py
```

The output is a toy quality surface. Too little exposure or development fails; too much processing also incurs a penalty.

All parameters are hypothetical. This is **not** a model of KPR, Shipley photoresist, chemically amplified resist, or any historical lithography line.

The narrow lesson is that photoresist manufacturing is not a one-bit question of “exposed / not exposed.” A usable pattern requires a window of coating, exposure, development, adhesion, etch survival, and contamination performance.

Historical context: [`../../docs/materials/why-photoresist-became-a-semiconductor-consumable.md`](../../docs/materials/why-photoresist-became-a-semiconductor-consumable.md).