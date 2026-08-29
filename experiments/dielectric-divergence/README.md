# Dielectric divergence

A synthetic model paired with `docs/materials/why-dielectrics-split-into-low-k-and-high-k.md`.

It shows two different optimization directions:

- lower dielectric constant reduces an interconnect capacitance proxy;
- higher dielectric constant allows a thicker gate dielectric at the same simple capacitance proxy, reducing a synthetic thickness-sensitive leakage term.

It is not a transistor, tunneling, low-k mechanics, or RC extraction model.

```bash
python experiments/dielectric-divergence/dielectric_divergence.py
```
