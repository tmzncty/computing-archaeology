# Why Solder Joints and Delamination Became System Failures

A packaged chip can pass every electrical test and still fail later because its materials expand at different rates.

That is why solder fatigue, interface delamination, package cracking, moisture, and thermal cycling belong inside computer history.

The historical question is:

> **When packaging stopped being a protective shell, how did it become a mechanical lifetime system?**

## Temperature cycling turns geometry into fatigue

Materials expand and contract with temperature.

If a component package, solder joint, and printed circuit board have different coefficients of thermal expansion (CTE), each temperature cycle imposes strain.

NASA work from 1969 already investigated crack development in solder joints under temperature cycling of printed circuit boards.[^nasa-1969]

Later JPL/NASA packaging studies describe differential-expansion fatigue as a leading solder-joint failure mechanism and explicitly connect thermal environment, package concept, strain, and qualification testing.[^nasa-1991]

The important point is cumulative damage:

```text
heat
-> materials expand differently
-> solder deforms
-> cool
-> reverse deformation
-> repeat
-> crack initiation / growth
```

The assembly may work perfectly for the first thousand cycles and fail later.

## Solder became a structural element

Early wiring practice often treated solder as something that electrically secured an already mechanically sound joint.

As electronics miniaturized, solder joints increasingly became part of the mechanical structure itself.

That saves space and assembly complexity, but it also means package/board geometry now determines lifetime.

Leadless and array packages make this especially visible because the interconnect must simultaneously provide:

- electrical conduction;
- mechanical attachment;
- strain accommodation;
- sometimes thermal conduction.

## Package interfaces can separate

The same thermal and moisture stresses that fatigue solder can damage internal package interfaces.

NASA thermal-reliability references list mechanisms including die cracking, package-seal defects, CTE mismatch, and delamination at chip/resin or other package interfaces.[^nasa-thermal]

Delamination matters because it can create secondary problems:

- altered stress distribution;
- moisture paths;
- wire-bond stress;
- local thermal resistance;
- cracking during solder reflow;
- underfill or substrate separation.

A failure can therefore migrate across layers of the package.

## Reliability becomes a system problem

There is no universal “good solder joint” independent of its context.

Lifetime depends on interactions among:

```text
package size
package material
board material / thickness
joint geometry
solder alloy
standoff height
underfill / encapsulant
thermal cycle range
ramp rate / dwell
mechanical constraint
power dissipation
```

This is why accelerated-life testing is necessary but difficult.

A harsh test can reveal mechanisms quickly, but the acceleration model must still correspond to the mechanism expected in use.

## Why this changes architecture and product design

Packaging fatigue can influence:

- allowable package size;
- leaded versus leadless choice;
- BGA/CGA geometry;
- underfill use;
- PCB thickness and pad design;
- heatsink attachment;
- thermal-management policy;
- service temperature limits;
- qualification cycles.

The computer therefore inherits mechanical design rules that software will never see.

## Experiment

[`../../experiments/thermal-cycle-fatigue/`](../../experiments/thermal-cycle-fatigue/) uses a synthetic CTE-mismatch × temperature-swing strain proxy and a deliberately simple fatigue relationship.

It is not a Coffin–Manson calibration for any package. It exists to show why larger mismatch and temperature swing can sharply consume a cycle budget.

## What this teaches us

A reliable computer is a negotiated truce among materials.

> **The package and PCB are not passive containers for logic. They are structures that repeatedly bend, creep, expand, contract, absorb moisture, and transfer stress.**

When electronics became dense enough, mechanical fatigue became part of digital-system lifetime.

## References

[^nasa-1969]: R. L. Moore and R. J. Vinson, “Investigation of the Development of Cracks in Solder Joints,” NASA, 1969, https://ntrs.nasa.gov/citations/19690000666
[^nasa-1991]: R. G. Ross Jr., “A Systems Approach to Solder Joint Fatigue in Spacecraft Electronic Packaging,” JPL/NASA, 1991, https://ntrs.nasa.gov/citations/19930058665
[^nasa-thermal]: NASA, thermal-environment failure-mechanism guidance including cracking, CTE mismatch, package defects, and delamination, https://ntrs.nasa.gov/api/citations/20230004376/downloads/20230004376.pdf?attachment=true

## Source note

NASA/JPL sources emphasize high-reliability and space hardware. Their failure physics is valuable, but package geometries, solder alloys, environments, and qualification rules should not be generalized into one universal commercial lifetime model.