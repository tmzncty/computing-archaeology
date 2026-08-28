# Airflow removal

Run:

```bash
python experiments/airflow-removal/airflow_removal.py
```

The model injects the same synthetic particle source into two rooms and gives them different removal fractions per step.

It illustrates a single historical idea: a clean manufacturing environment must continuously remove contamination generated during operation.

## Not a historical cleanroom model

The source rate and removal fractions are synthetic.

This is not CFD, does not model turbulence or particle size, and does not reproduce Willis Whitfield's prototype.

See [`../../docs/facilities/why-clean-air-had-to-keep-moving.md`](../../docs/facilities/why-clean-air-had-to-keep-moving.md) for the historical discussion.