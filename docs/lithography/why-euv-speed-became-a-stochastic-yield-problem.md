# Why EUV Speed Became a Stochastic Yield Problem

EUV creates a direct conflict between throughput and randomness.

## Historical record

Imec has repeatedly described random EUV printing failures such as broken lines, bridges, missing contacts, and merged contacts as stochastic defects. Its 2021 work correlated optical/e-beam inspection with electrical opens and shorts, and its 2025 High-NA work again used electrical structures to quantify stochastic-yield loss.[^imec2021][^imec2025]

ASML's EUV pellicle history makes another throughput trade visible: the membrane protects the reticle from particles, but every material placed in the 13.5 nm beam absorbs some photons. ASML reported 90% pellicle transmission in 2021 as a productivity milestone.[^pellicle]

## Engineering reconstruction

```text
higher dose
  -> more photons / feature
  -> lower stochastic risk
  -> slower scanner throughput

lower dose
  -> fewer photons / feature
  -> faster throughput
  -> higher random-failure pressure
```

The pellicle adds a second tax: protecting the mask reduces printable-particle risk but costs optical transmission and must survive high thermal load in vacuum.

## Why this matters to computing speed

A faster scanner is useless if random defects destroy yield. A lower-dose resist is useless if stochastic opens/shorts erase the throughput gain. Lithography speed therefore becomes a statistical manufacturing problem rather than only an optical one.

## Experiment

`experiments/euv-stochastic-window/euv_stochastic_window.py` models synthetic dose, transmission, throughput, and stochastic-failure pressure.

[^imec2021]: Imec, “Imec Pushes Single-Exposure Patterning Capability of 0.33NA EUVL to its Extreme Limits,” 2021, https://www.imec-int.com/en/press/imec-pushes-single-exposure-patterning-capability-033na-euvl-its-extreme-limits
[^imec2025]: Imec, “Imec demonstrates electrical yield for 20nm pitch metal lines obtained with High NA EUV single patterning,” 2025, https://www.imec-int.com/en/press/imec-demonstrates-electrical-yield-20nm-pitch-metal-lines-obtained-high-na-euv-single
[^pellicle]: ASML, “Q1 2021 financial results,” https://www.asml.com/en/news/press-releases/2021/q1-2021-financial-results
