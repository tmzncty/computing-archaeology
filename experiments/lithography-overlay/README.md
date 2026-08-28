# Lithography Overlay Experiment

Historical question:

> Why does adding layers to an integrated circuit make alignment accuracy a manufacturing constraint rather than a drawing detail?

The model places a small feature on several masks and applies synthetic random x/y overlay error. A feature is counted as surviving only if every layer remains within a chosen alignment tolerance.

## What it demonstrates

- more layers create more opportunities for misregistration;
- smaller design margins demand tighter alignment;
- manufacturing precision is part of the usable density of a process.

## What it does not prove

It is not a model of any historical aligner, mask set, process node, or fab. Overlay errors are synthetic and independent; real lithography errors include systematic distortion, wafer expansion, lens effects, stepper fields, process bias, and metrology feedback.

## Run

```bash
python experiments/lithography-overlay/lithography_overlay.py
```
