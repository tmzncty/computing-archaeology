# Wire-Bond Thermal Budget

This is a deliberately synthetic model of a historical idea:

> bond interfaces can continue changing after assembly, so reliability depends on time and temperature, not only initial pull strength.

Run:

```bash
python experiments/bond-thermal-budget/bond_thermal_budget.py
```

The script uses an invented Arrhenius-like risk proxy. It is **not** a model of AuAl2 growth, Kirkendall voiding, or any qualified package lifetime.

See [`../../docs/packaging/why-wire-bonds-failed-in-strange-colors.md`](../../docs/packaging/why-wire-bonds-failed-in-strange-colors.md).