# Furnace material contamination budget

This synthetic model treats a high-temperature process component as more than a bulk-composition number.

Run:

```bash
python experiments/furnace-material-budget/furnace_material_budget.py
```

The toy score combines bulk impurity, exposed-surface factor, outgassing tendency, and accumulated cycle age.

All values are hypothetical. This is **not** a materials database, contamination model, furnace qualification method, or safety tool.

The narrow lesson is that a low bulk-impurity number can be undermined by porosity, surface condition, outgassing, or process history.

Historical context: [`../../docs/materials/why-quartz-and-silicon-carbide-became-fab-furniture.md`](../../docs/materials/why-quartz-and-silicon-carbide-became-fab-furniture.md).