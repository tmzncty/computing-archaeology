# Screening tradeoff

A synthetic population model for the tradeoff behind burn-in/screening.

Run:

```bash
python experiments/screening-tradeoff/screening_tradeoff.py
```

The model lets screening remove a fraction of latent weak units while also imposing a configurable damage/loss penalty on otherwise good units.

All values are invented for teaching. The model does **not** reproduce a historical burn-in schedule, bathtub curve, activation energy, or real semiconductor failure distribution.

Its purpose is to make one point visible: screening can reduce early field-failure risk, but stronger screening consumes time/capacity and can itself impose cost or damage.