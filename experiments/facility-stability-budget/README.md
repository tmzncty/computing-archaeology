# Facility stability budget

Run:

```bash
python experiments/facility-stability-budget/facility_stability_budget.py
```

This model combines three **synthetic normalized** facility contributions:

- thermal drift;
- vibration;
- power disturbance.

It uses a root-sum-square combination only to illustrate a general idea: multiple individually tolerable environmental errors can consume a shared precision budget.

## Not a scanner specification

The numbers are not micrometers, nanometers, degrees Celsius, acceleration, or volts.

This is not a model of a real fab, lithography tool, building, or SEMI requirement.

See [`../../docs/facilities/why-temperature-and-vibration-became-process-variables.md`](../../docs/facilities/why-temperature-and-vibration-became-process-variables.md).