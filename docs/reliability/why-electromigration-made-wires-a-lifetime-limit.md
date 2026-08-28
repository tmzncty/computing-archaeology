# Why Electromigration Made Wires a Lifetime Limit

Shrinking a transistor is not enough if the metal that connects it slowly moves under current.

That is the historical importance of **electromigration**.

The problem is easy to miss because a metal interconnect looks static in a layout. Under high current density and temperature, however, momentum transfer from conducting electrons can drive atomic transport.

The historical question is:

> **When did semiconductor reliability stop being only about junctions and oxides and become a lifetime problem for microscopic wiring?**

## A conductor can move while the chip stands still

J. R. Black's 1969 paper on aluminum metallization described wear-out failure modes involving mass transport under current flow.[^black]

One characteristic failure is void formation:

```text
atomic flux
-> local depletion
-> void grows
-> cross-section shrinks
-> resistance rises
-> open circuit
```

Elsewhere material can accumulate and form hillocks or extrusions.

A wire therefore has a history.

It can begin electrically correct and become incorrect after enough current-time-temperature exposure.

## Current density changes the meaning of scaling

If a conductor becomes narrower while carrying comparable current, current density rises.

That creates a conflict:

```text
smaller geometry
-> denser circuits

but also

smaller cross-section
-> higher current density
-> stronger reliability pressure
```

So interconnect scaling is not a free consequence of transistor scaling.

It requires materials, geometry, current distribution, temperature control, and lifetime rules to evolve too.

## Temperature couples electrical design to packaging

Electromigration is strongly temperature sensitive.

That means the failure mechanism crosses organizational boundaries:

- circuit switching activity affects current;
- power distribution affects local current density;
- layout affects wire width and crowding;
- package and cooling affect temperature;
- process metallurgy affects resistance to atomic transport.

A reliability rule such as a maximum allowed current density is therefore a compressed interface between physics and design.

## Black's equation became a design vocabulary

The exact models and fitted exponents vary by material system and geometry, but the historical importance of Black's work is broader than one formula.

It made interconnect lifetime something engineers could discuss in terms of measurable stress variables rather than mysterious late failures.

A simplified engineering vocabulary emerged around relationships of the form:

```text
lifetime decreases as current density increases
lifetime decreases sharply as temperature increases
```

This turns a metallurgical mechanism into a design constraint.

## Why this changes architecture

Electromigration affects more than physical-design signoff.

It can influence:

- power-grid width;
- clock distribution;
- allowable current per pin/bump;
- metal stack choices;
- redundancy;
- thermal design;
- package interconnect density;
- voltage/frequency operating envelopes.

A processor cannot simply switch more devices faster if the delivery network cannot survive the resulting current distribution.

## Experiment

[`../../experiments/electromigration-stress/`](../../experiments/electromigration-stress/) uses a deliberately simplified relative-lifetime proxy based on current density and temperature.

The constants are synthetic. The point is to expose why modest changes in width/current/temperature can strongly change a wear-out budget.

## What this teaches us

Reliability creates architecture from below.

> **A metal line is not merely a geometric connection. It is a material carrying a stress history.**

Once integration became dense enough, computer performance depended on a manufacturing civilization that could control not only whether a conductor existed on day one, but whether it would remain a conductor years later.

## References

[^black]: J. R. Black, “Electromigration Failure Modes in Aluminum Metallization for Semiconductor Devices,” *Proceedings of the IEEE*, vol. 57, no. 9, 1969, DOI 10.1109/PROC.1969.7340. Bibliographic record: https://cir.nii.ac.jp/crid/1362262943933168768

## Source note

Black's 1969 paper is a foundational period source for aluminum-metallization wear-out. Modern copper/barrier/low-k interconnect systems involve additional mechanisms and should not be read directly back into the 1969 aluminum case. The experiment is a teaching proxy, not a calibrated Black-equation implementation for a real process.