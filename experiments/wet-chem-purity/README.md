# Wet chemical purity budget

This tiny synthetic model exists to challenge the idea that one headline purity percentage is enough to describe a semiconductor wet chemical.

Run:

```bash
python experiments/wet-chem-purity/wet_chem_purity.py
```

It tracks separate channels for metals, particles, organics, and moisture, then computes a deliberately simple weighted risk proxy.

The parameters are hypothetical. They are **not** electronic-grade chemical specifications, process limits, or safety limits.

The experiment demonstrates only a structural point:

> two chemical lots with similarly impressive bulk assay can present different process risk if their trace contaminants or delivery-path contamination differ.

For historical context see [`../../docs/materials/why-wet-chemistry-had-to-be-electronic-grade.md`](../../docs/materials/why-wet-chemistry-had-to-be-electronic-grade.md).