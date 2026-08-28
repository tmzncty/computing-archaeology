# Sputter Target Utilization

This synthetic model asks why a target can be retired while substantial material remains.

It compares uniform erosion with increasingly concentrated erosion profiles. Retirement is triggered by the deepest local region rather than average remaining mass.

Run:

```bash
python experiments/target-utilization/target_utilization.py
```

The numbers are dimensionless and **not** measurements of a commercial sputter cathode. The model isolates one idea: local erosion geometry can determine useful target lifetime.