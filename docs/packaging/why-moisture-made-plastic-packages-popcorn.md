# Why Moisture Made Plastic Packages Popcorn

A plastic package can look dry and still contain enough absorbed moisture to crack during assembly.

That is the origin of the infamous **popcorn** problem.

## Historical record

Surface-mount assembly changed package reliability because the entire component body began passing through high-temperature reflow rather than keeping most of the package relatively cool while leads were soldered.[^jstd033]

Plastic molding compounds and other polymeric package materials absorb moisture from ambient humidity. During reflow, the package is heated rapidly above 200 °C. Moisture expansion, interfacial weakness, and coefficient-of-thermal-expansion mismatch can produce internal delamination or cracking.[^jstd033]

The package may literally make an audible pop in severe cases.

## A component acquired a floor life

Once moisture/reflow sensitivity became standardized, a component was no longer simply:

```text
part number
+ electrical rating
```

It also had a logistics state:

```text
dry packed
-> bag opened
-> floor exposure clock starts
-> assembly before limit
or
-> bake / controlled recovery
```

This is an important computing-history transition.

Warehouse time, humidity, packaging bags, desiccant, humidity indicator cards, and assembly scheduling became part of semiconductor reliability.

## The failure is distributed across layers

Popcorn cracking is not one material “failing.”

The chain can include:

```text
ambient humidity
-> diffusion into molding compound
-> local moisture concentration
-> rapid reflow heating
-> vapor pressure / hygroscopic expansion
-> CTE mismatch
-> interface delamination
-> crack growth
-> wire / die / package damage
```

That means the relevant unit is not only the package material.

It is the **package + storage history + reflow history**.

## Surface mount changed the meaning of storage

Through-hole assembly and early packages had moisture concerns too, but widespread SMD reflow created a standardized industrial problem because the whole body experienced a short high-temperature excursion.

IPC/JEDEC J-STD-033 explicitly describes moisture/reflow-sensitive components, floor-life exposure, dry packing, and handling practices intended to avoid cracking and delamination.[^jstd033]

The point for archaeology is not the current revision number.

The important structural change is:

> **a sealed component became a perishable manufacturing input once storage history could change reflow survival.**

## Engineering reconstruction

The experiment in [`../../experiments/moisture-reflow/`](../../experiments/moisture-reflow/) uses synthetic moisture uptake and reflow-stress proxies.

It compares:

- freshly dry-packed parts;
- short floor exposure;
- long humid exposure;
- a baked/recovered condition.

It is not an MSL classifier and must not be used to set bake or floor-life procedures.

## What became invisible

A finished laptop gives no sign that its packages once lived inside:

- moisture-barrier bags;
- desiccant packs;
- humidity cards;
- dry cabinets;
- floor-life tracking systems;
- bake ovens;
- reflow-profile qualification.

But without this logistics infrastructure, the move to dense plastic surface-mount packaging would have carried a much larger hidden yield and field-reliability penalty.

## Source caution

The cited standard is mature standardization evidence. It should not be projected backward as if every early SMD factory already used the current terminology or procedures.

[^jstd033]: IPC/JEDEC J-STD-033C-1, *Handling, Packing, Shipping, and Use of Moisture/Reflow and/or Process Sensitive Components* (2014). Its foreword explains that SMD reflow introduced cracking/delamination concerns because atmospheric moisture diffuses into permeable package materials and then experiences high reflow temperature. Public table-of-contents copy: https://www.ipc.org/TOC/IPC-JEDEC-J-STD-033C-1.pdf .
