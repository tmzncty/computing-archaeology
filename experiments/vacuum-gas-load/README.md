# Vacuum gas load

Run:

```bash
python experiments/vacuum-gas-load/vacuum_gas_load.py
```

The model compares three synthetic chamber histories:

- no continuing gas source;
- persistent surface outgassing;
- a small continuous leak.

The point is to separate **pumping strength** from **gas cleanliness**.

A strong pump can lower total pressure while still fighting a continuing source of unwanted molecules.

## Historical status

All values are normalized and synthetic.

This is not a vacuum sizing calculation, residual-gas analysis, or reconstruction of a specific semiconductor process tool.

See [`../../docs/facilities/why-clean-vacuum-became-a-process-requirement.md`](../../docs/facilities/why-clean-vacuum-became-a-process-requirement.md).