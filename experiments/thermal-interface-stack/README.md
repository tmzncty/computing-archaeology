# Thermal interface stack

A synthetic one-dimensional resistance-chain model paired with `docs/packaging/why-tim-and-the-lid-became-part-of-the-processor.md`.

It varies TIM thickness and void fraction while holding a fixed synthetic die/lid/cooler resistance contribution, exposing why interface quality can dominate total temperature rise.

It is not a processor thermal-design calculator and contains no commercial TIM properties.

```bash
python experiments/thermal-interface-stack/thermal_interface_stack.py
```
