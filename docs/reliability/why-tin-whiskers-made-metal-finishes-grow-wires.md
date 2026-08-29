# Why Tin Whiskers Made Metal Finishes Grow Wires

A metal finish can grow a new conductor years after manufacturing is finished.

That is the reliability problem of **tin whiskers**.

## Historical record

Tin whiskers are slender crystalline structures that can spontaneously grow from tin-rich surfaces. NASA's electronics reliability program documents whiskers reaching millimeter scales and records failures in terrestrial and space systems.[^nasa]

This is not a new phenomenon created by lead-free electronics. NASA explicitly notes that tin whiskers were known earlier, while renewed attention followed the wider use of pure-tin finishes and restrictions on lead.[^nasa]

A particularly unsettling field example describes a whisker-induced short appearing roughly twenty years after an electronic system entered service.[^twenty]

## A surface finish is not frozen in time

A schematic assumes that two pins separated today remain separated tomorrow.

Tin whiskers break that assumption:

```text
plated surface
-> internal / external stress evolves
-> whisker nucleates
-> whisker grows
-> gap shrinks
-> electrical bridge becomes possible
```

The conductor was not designed.

It was grown by the material system after shipment.

## Failure modes are strange

A whisker can produce:

- a stable low-current short;
- an intermittent short;
- a metal-vapor arc in higher-energy conditions;
- debris after a whisker fuses open;
- long-delayed failure that escapes ordinary production testing.

That makes tin whiskers especially hostile to simple qualification logic.

A product can pass:

```text
incoming inspection
assembly test
burn-in
system test
field operation for years
```

and still fail when a whisker finally reaches another conductor.

## Why lead mattered

Tin-lead finishes historically suppressed whisker growth much more effectively than pure tin. NASA guidance therefore treats pure-tin finishes as a special risk and has prohibited them in many mission-critical contexts.[^prohibition]

This created an awkward transition during lead-free conversion:

```text
remove lead for environmental / regulatory reasons
-> increase use of tin-rich finishes
-> re-open whisker risk
-> add procurement, mitigation, inspection, and risk controls
```

Again, a materials policy propagates into architecture and maintenance.

## Engineering reconstruction

The experiment in [`../../experiments/whisker-bridge/`](../../experiments/whisker-bridge/) uses a random synthetic whisker-growth population and conductor spacing.

It demonstrates only that a long-tailed growth distribution can produce rare late bridges even when most whiskers remain short.

It is not a tin-whisker growth model and cannot predict service life.

## What became invisible

The final PCB does not tell you whether a lead finish was:

- pure tin;
- tin-lead;
- nickel/palladium/gold;
- mitigated by annealing;
- conformally coated;
- accepted under a procurement waiver.

Yet those choices can determine whether a new microscopic wire appears a decade later.

The history of computing reliability therefore includes the unsettling fact that **materials continue manufacturing themselves after the factory stops**.

[^nasa]: NASA Electronic Parts and Packaging Program, “Basic Information Regarding Tin Whiskers,” https://nepp.nasa.gov/whisker/background/index.htm .
[^twenty]: NASA NEPP, “Tin Whisker Anecdote: 20 Years to Failure,” describing a fielded system from circa 1983 that failed circa 2002 after a whisker bridged adjacent IC pins, https://nepp.nasa.gov/WHISKER/anecdote/20year/index.html .
[^prohibition]: NASA Parts Selection List, “Pure Tin Plating Prohibition,” citing NASA advisories beginning in 1998, https://nepp.nasa.gov/npsl/prohibited/tin_prohibition.htm .
