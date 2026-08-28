# Flow-control error

This synthetic experiment compares a commanded gas dose with a simplified delivered dose affected by calibration bias and response lag.

Run:

```bash
python experiments/flow-control-error/flow_control_error.py
```

All numbers are hypothetical. This is **not** an MFC calibration, process-control, safety, or gas-delivery design tool.

The point is simply that a recipe setpoint is not identical to delivered material. Instrument bias and transient response can turn a nominally identical recipe into different chemistry.

Historical context: [`../../docs/manufacturing/why-mass-flow-control-made-gas-recipes-repeatable.md`](../../docs/manufacturing/why-mass-flow-control-made-gas-recipes-repeatable.md).