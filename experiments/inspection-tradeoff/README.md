# Inspection tradeoff

A synthetic model of production inspection workload.

Run:

```bash
python experiments/inspection-tradeoff/inspection_tradeoff.py
```

The model separates:

- real defect prevalence;
- detection rate;
- escaped defects;
- false-call rate;
- total review workload.

All numbers are invented. This is not a performance model for any AOI, ICT, X-ray, acoustic, or human-inspection system.

Its purpose is to expose a factory-scale fact: when production volume is large, even a small false-call rate can create substantial human review work.