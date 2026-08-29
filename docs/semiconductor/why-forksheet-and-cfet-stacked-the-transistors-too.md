# Why Forksheet and CFET Stacked the Transistors Too

GAA nanosheets improve gate control, but cell scaling still runs into the space occupied by neighboring n- and p-type devices.

## Historical record

Imec introduced forksheet as an extension of the nanosheet family and later placed CFET on the beyond-1nm roadmap. In CFET, complementary devices are vertically stacked rather than placed only side-by-side.[^forksheet][^cfet]

## Engineering reconstruction

```text
planar CMOS: n and p beside each other
FinFET/GAA:   better electrostatic control
forksheet:    reduce n/p separation
CFET:         stack n and p vertically
```

The density gain is not free. Vertical stacking increases process-order dependence, thermal budget coupling, alignment difficulty, contact routing complexity, and test/rework constraints.

## Speed connection

Higher transistor density can shorten local wires and put more compute in a fixed area, but only if the process can preserve drive current, variability, contacts, and heat removal.

## Experiment

`experiments/cfet-density/cfet_density.py` compares synthetic side-by-side, forksheet-like, and stacked-CFET cell footprints with an integration penalty.

[^forksheet]: Imec, “Outer wall forksheet to bridge nanosheet and CFET device architectures,” https://www.imec-int.com/en/articles/outer-wall-forksheet-bridge-nanosheet-and-cfet-device-architectures-logic-technology
[^cfet]: Imec, “Imec puts complementary FET (CFET) on the logic technology roadmap,” https://www.imec-int.com/en/articles/imec-puts-complementary-fet-cfet-logic-technology-roadmap
