# Why Wire Bonds Failed in Strange Colors

A packaged semiconductor can fail even when the silicon itself is perfect.

One of the classic reminders is the gold-aluminum bond system.

When gold wire is bonded to aluminum metallization and later exposed to heat, intermetallic compounds can grow at the interface. Some of these compounds are mechanically weak, electrically resistive, or accompanied by void formation.

The resulting failure literature acquired memorable names:

- **purple plague**;
- **white plague**;
- **black death**.

The names sound folkloric. The failures were industrially real.

## The package contains a metallurgy experiment

Early microelectronics commonly connected die pads to package leads using very fine wire.

Gold thermocompression ball bonding was one of the earliest widely used techniques. But semiconductor die often used aluminum metallization.[^nasa-hybrid]

That creates a dissimilar-metal interface:

```text
gold wire
+
aluminum pad
+
heat
+
time
-> intermetallic growth
```

NASA reliability literature from the 1960s and 1970s documents failures associated with Au-Al intermetallic formation, including the purple AuAl2 phase and related voiding/weakening phenomena.[^nasa-review][^nasa-hybrid]

## A bond can look good and age badly

A wire bond must survive more than the moment it is made.

It may later experience:

- package sealing temperature;
- soldering heat;
- operating temperature;
- thermal cycling;
- vibration;
- mechanical stress;
- humidity or contaminants.

The interface can therefore continue changing after factory inspection.

This makes reliability a problem in **time**, not only initial strength.

A bond that passes pull test today may evolve metallurgically during years of service.

## Purple plague is not simply “purple material is bad”

Later summaries sometimes flatten the story into a color chart.

The real issue is more complicated.

Gold and aluminum can form several intermetallic phases. Different phases and void structures have different electrical and mechanical consequences. Kirkendall-type voiding can reduce the effective conducting area and weaken the joint.[^nasa-modern]

So the important engineering lesson is:

> the interface is a growing microstructure, not a static boundary.

## Packaging choices create new failure modes

Switching to aluminum wire can avoid some Au-Al problems at the die pad, but it introduces other process windows and mechanical behavior.

NASA-sponsored work in the 1970s investigated ultrasonic aluminum wire bonding, heat soak, thermal cycling, bond pull strength, and heel fatigue precisely because there was no single magical bond material.[^nasa-al]

A packaging engineer trades among:

- bondability;
- metallurgical compatibility;
- wire strength;
- pad damage;
- thermal behavior;
- corrosion;
- process speed;
- material cost.

## Reliability testing becomes a manufacturing discipline

Wire-bond failures helped drive routines such as:

- pull testing;
- ball shear;
- accelerated temperature storage;
- thermal cycling;
- cross-sectioning;
- microscopy;
- destructive physical analysis;
- process qualification.

The package line therefore needs materials science and failure analysis, not just assembly speed.

## The weakest link can move outside the die

As transistor reliability improved, packaging interfaces could become dominant failure sites.

A perfect logic design is useless if one 25-micrometer wire fractures or one bond interface becomes resistive.

That means computer reliability depends on a hierarchy:

```text
transistor
-> on-die metal
-> bond pad
-> bond wire
-> lead frame / package
-> solder joint
-> PCB trace
-> connector
```

Every transition between materials is an opportunity for mismatch.

## Flip chip is partly a response to interconnect burden

Industry interest in beam-lead and flip-chip approaches grew partly from the desire to reduce or eliminate long wire interconnects.[^nasa-hybrid]

That does not mean flip chip was invented only because of purple plague.

It means wire-bond limitations formed part of a broader pressure toward shorter, denser die-to-substrate connections.

See [`why-flip-chip-shortened-the-interconnect.md`](why-flip-chip-shortened-the-interconnect.md).

## What this teaches us

Packaging failure history makes one principle unusually clear:

> **a semiconductor device is not finished when the wafer works.**

The chip still has to survive a chain of metal interfaces, heat cycles, mechanical stresses, and environmental exposure.

The computer industry's reliability therefore rests on invisible metallurgy inside packages that users never see.

## References

[^nasa-hybrid]: NASA, *Interconnecting of Hybrid Microelectronic Assemblies and Devices*, 1970s-era technical material, https://ntrs.nasa.gov/api/citations/19740006027/downloads/19740006027.pdf
[^nasa-review]: NASA, *Reliability Abstracts and Technical Reviews*, review of 1964 Au-Al bond failure work, https://ntrs.nasa.gov/api/citations/20160003539/downloads/20160003539.pdf
[^nasa-al]: M. Macha and R. A. Thiel, *High Reliability Bond Program Using Small Diameter Aluminum Wire*, NASA-CR-143946, 1975, https://ntrs.nasa.gov/citations/19750024389
[^nasa-modern]: NASA, modern packaging body-of-knowledge discussion of Au-Al intermetallics and Kirkendall voiding, https://ntrs.nasa.gov/api/citations/20230014536/downloads/20230014536.pdf

## Source note

NASA reliability documents are especially useful because they treat packaging as a failure-analysis problem rather than a product-history anecdote. Modern summaries are used here to clarify metallurgy; period claims should be traced to period reports when precise temperatures, lifetimes, or phase behavior matter.