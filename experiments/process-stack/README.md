# Process Stack Experiment

Historical question:

> Why does a more capable semiconductor process also create more opportunities for manufacturing loss?

This synthetic model assigns a per-step survival probability and multiplies it across a growing process stack. It contrasts a simple device flow with increasingly complex multi-mask flows.

## What it demonstrates

A process step that is individually very reliable can still matter when repeated many times. Better process control can therefore be as important as adding another device feature.

## Limitation

Real semiconductor steps are neither identical nor statistically independent. This is not a fab yield model; it is a simple way to make cumulative process risk visible.

## Run

```bash
python experiments/process-stack/process_stack.py
```
