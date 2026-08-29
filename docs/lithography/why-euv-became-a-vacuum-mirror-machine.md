# Why EUV Became a Vacuum Mirror Machine

Lithography once looked like increasingly sophisticated photography. Extreme ultraviolet (EUV) broke that intuition.

At 13.5 nm, ordinary transmissive optics are no longer the obvious path. The exposure system becomes a reflective, vacuum-operated machine whose source, mirrors, mask, contamination control, stages, metrology, and resist all have to cooperate.

## Historical record

ASML records shipment of its first pre-production TWINSCAN NXE:3100 EUV system in 2010, the first NXE:3300 production system in 2013, increased NXE:3400 orders after 2016, and EUV entering high-volume manufacturing around 2020.[^asml-products][^asml-history]

ASML also describes EUV optical systems as multilayer mirrors operating in vacuum rather than conventional refractive lenses.[^mirrors]

## Engineering reconstruction

An EUV scanner is a chain of imperfect reflections:

```text
source
 -> collector
 -> illumination mirrors
 -> reflective mask
 -> projection mirrors
 -> resist
```

If every mirror reflects less than 100%, throughput depends on the product of many efficiencies. That is why source power, mirror contamination, collector lifetime, resist sensitivity, and stage speed become tightly coupled.

## Vacuum is optical infrastructure

EUV light is strongly absorbed by ordinary matter, including air. Vacuum is therefore not merely chamber housekeeping; it is part of the optical path.

This pulls vacuum engineering, contamination control, hydrogen cleaning, mask protection, source debris mitigation, and mirror service into lithography history.

## Why one wavelength reorganized an industry

Moving to 13.5 nm did not mean replacing one lamp with a shorter-wavelength lamp. It demanded a new source, new optics, new masks, new resist behavior, new metrology, and new maintenance infrastructure.

## Experiment

[`experiments/euv-reflection-chain/euv_reflection_chain.py`](../../experiments/euv-reflection-chain/euv_reflection_chain.py) multiplies synthetic per-mirror reflectivities to show why small losses compound through a reflective optical train.

## Source caution

ASML is the dominant equipment supplier and its pages are corporate technical history. They are excellent evidence for ASML platform chronology and architecture, but not neutral evidence for every priority dispute in EUV's multi-institution development history.

[^asml-products]: ASML, “EUV lithography systems,” https://www.asml.com/en/en/products/euv-lithography-systems
[^asml-history]: ASML, “Our history,” https://www.asml.com/en/company/about-asml/history
[^mirrors]: ASML, “Lenses & mirrors,” https://www.asml.com/en/en/technology/lithography-principles/lenses-and-mirrors
