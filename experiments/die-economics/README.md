# Die Economics Experiment

Historical question:

> Why can a target selling price force architectural decisions before a microprocessor is fully designed?

Run:

```bash
python experiments/die-economics/die_economics.py
```

The model varies die area and uses a simple synthetic yield function to estimate working dies and cost per packaged good chip.

## What it demonstrates

Larger die consume more wafer area and, under a defect model, have a greater chance of containing a defect. A hard product-cost target can therefore create a hard silicon-area budget.

That makes architecture, layout, process, yield, and product economics one coupled problem.

## What it does not reproduce

None of the default wafer, defect-density, package, or cost values are historical MOS Technology data. The yield model is deliberately simplified and ignores dies lost around wafer edges in a realistic geometric way, redundancy, parametric yield, test binning, mask costs, volume pricing, and many process details.

Historical context: [`../../docs/architecture/why-the-6502-was-designed-backward-from-price.md`](../../docs/architecture/why-the-6502-was-designed-backward-from-price.md).
