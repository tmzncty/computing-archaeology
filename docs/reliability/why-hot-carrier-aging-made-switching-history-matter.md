# Why Hot-Carrier Aging Made Switching History Matter

A MOSFET can be electrically legal and still slowly damage itself while switching.

That is the historical importance of **hot-carrier degradation**.

## Historical record

As MOS devices were scaled, strong electric fields near the drain could accelerate carriers enough that a small fraction entered the gate oxide or generated interface damage. Reliability work in the 1980s treated this as a practical lifetime problem rather than a laboratory curiosity.[^chen]

By the 1990s the subject had accumulated enough mechanisms, stress methods, and lifetime models to require dedicated reviews.[^review]

The important historical shift was conceptual:

```text
transistor state
was no longer only
ON / OFF

it also had
stress history
```

A device could meet its original threshold voltage, transconductance, and drive-current targets at manufacture, then drift as repeated high-field operation created trapped charge or interface states.

## Why switching history matters

A circuit diagram normally hides time.

Hot-carrier reliability forces time back into the picture:

```text
Vd, Vg, edge shape, duty cycle
+ local electric field
+ carrier energy distribution
+ temperature
+ operating hours
-> parameter drift
```

This does not mean every transition damages every MOSFET in the same way. Device structure, oxide technology, supply voltage, channel length, source/drain engineering, and operating regime all matter.

The historical lesson is narrower and more useful:

> **maximum ratings were not enough; lifetime depended on how the device was exercised.**

## Scaling created a paradox

Smaller transistors reduced dimensions, but supply-voltage scaling did not always keep every internal electric field proportionally gentle.

That created pressure for engineering changes such as:

- altered source/drain profiles;
- lightly doped drain structures;
- process changes that reduced peak fields;
- circuit derating;
- accelerated stress qualification;
- lifetime models connected to real switching activity.

So the transistor architecture and the reliability model co-evolved.

## From device physics to product policy

Once a degradation mechanism depends on operating activity, product decisions inherit physics.

Questions appear that a pure logic diagram cannot answer:

- How often does this node switch?
- At what voltage?
- For how many years?
- Does a stress condition occur only during boot, or continuously?
- Does a faster edge reduce one loss while worsening another field condition?
- Which transistor geometry receives the worst stress?

This is a bridge between semiconductor reliability and architecture.

## Engineering reconstruction

The experiment in [`../../experiments/hot-carrier-duty/`](../../experiments/hot-carrier-duty/) uses a deliberately synthetic damage accumulator.

It compares workloads with different:

- drain-field stress;
- switching duty cycle;
- temperature;
- operating time.

The numerical relationship is invented. The model exists only to demonstrate that **equal wall-clock time does not imply equal accumulated stress**.

## What became invisible

Users later inherited processors with voltage tables, guard bands, qualification standards, and reliability-aware process technology already built in.

That success hides the chain:

```text
high-field carrier physics
-> accelerated stress
-> device parameter drift
-> compact reliability model
-> process redesign
-> voltage/frequency limits
-> product lifetime expectation
```

A stable household computer therefore contains not only transistors, but decades of knowledge about how transistors age while doing useful work.

## Source caution

Hot-carrier degradation contains multiple physical mechanisms and device-generation dependencies. The sources below establish the period reliability problem and later synthesis; they should not be flattened into one universal lifetime equation.

[^chen]: K.-L. Chen et al., “Reliability Effects on MOS Transistors Due to Hot-Carrier Injection,” *IEEE Journal of Solid-State Circuits* 20, no. 1 (1985), 306–313, DOI 10.1109/JSSC.1985.1052307.
[^review]: A. Acovic, G. La Rosa, and Y.-C. Sun, “A review of hot-carrier degradation mechanisms in MOSFETs,” *Microelectronics Reliability* 36, nos. 7–8 (1996), 845–869, https://doi.org/10.1016/0026-2714(96)00022-4 .
