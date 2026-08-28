# Wafer Yield Experiment

Historical question:

> Why can a larger, more capable chip become disproportionately harder to manufacture economically?

This teaching model uses a simple Poisson-style random-defect approximation:

```text
Y = exp(-D * A)
```

where `D` is defect density and `A` is die area.

It then estimates gross die per wafer, good die, and wafer-cost contribution per good die.

## Important limitation

This is **not** a historical reconstruction of any specific Fairchild, Intel, TI, IBM, MOS Technology, or modern fab. Real yield models account for edge loss, defect clustering, parametric failures, process excursions, redundancy, test escape, and many other effects.

The point is only to expose the nonlinear relationship between die area, defect density, and cost.

## Run

```bash
python experiments/wafer-yield/wafer_yield.py
```
