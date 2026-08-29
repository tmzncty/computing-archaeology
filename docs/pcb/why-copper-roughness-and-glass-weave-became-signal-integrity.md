# Why Copper Roughness and Glass Weave Became Signal Integrity

At low enough speed, a PCB trace can be treated as a wire drawn on an insulating board.

At high enough speed, the microscopic texture of the copper and the weave pattern inside the laminate become part of the signal path.

## Historical record

High-speed board-design guidance increasingly had to model insertion loss, dielectric loss, conductor loss, via geometry, and material construction rather than only DC continuity. Intel/Altera design guidance explicitly treats loss tangent, copper geometry, via-stub length, and fiberglass weave composition as high-speed channel variables.[^intel-highspeed][^intel-weave]

IPC technical material likewise treats copper roughness as a multiplier on high-frequency conductor loss.[^ipc-roughness]

This is the point where board-material microstructure becomes architecture.

## Skin effect makes the copper surface matter

As frequency rises, current crowds toward conductor surfaces.

A perfectly smooth mathematical trace and a rough electrodeposited copper surface therefore do not present the same effective path.

Conceptually:

```text
frequency rises
-> current occupies thinner surface region
-> microscopic roughness increases effective path / field disturbance
-> conductor loss rises
```

The exact models are more complicated than “roughness makes the wire longer,” but that intuition explains why copper-foil treatment and profile become signal-integrity parameters.

The copper foil was once chosen mostly for adhesion and manufacturability.

At multi-gigabit rates, its surface morphology also spends channel-loss budget.

## Glass weave makes nominally identical traces different

FR-4-like laminates are not homogeneous solids.

They contain:

```text
woven glass bundles
+ resin-rich regions
```

Glass and resin have different dielectric properties.

If the two traces of a differential pair happen to travel over different mixtures, they can propagate at slightly different velocities.

Intel guidance describes this **glass-weave skew** and recommends approaches such as angled routing, spread glass, or tighter weave for high-speed layers.[^intel-weave]

The astonishing implication is:

> **two equal-length copper traces can have different electrical length because of where they happen to cross microscopic textile.**

## PCB panel orientation became a timing variable

Once weave skew matters, layout and fabrication orientation become coupled.

Mitigations can include:

- routing differential pairs at an angle;
- rotating artwork relative to panel weave;
- selecting spread-glass styles;
- using multiple plies;
- matching pair pitch to weave pitch;
- moving to more homogeneous dielectric systems.

These choices cost:

- board area;
- routing freedom;
- laminate money;
- fabrication flexibility.

So picoseconds turn into procurement decisions.

## Material variability became statistical channel variability

A prototype can work because its particular trace-to-weave registration is favorable.

Another board from the same design may align differently.

That makes high-speed design a manufacturing-population problem:

```text
nominal stackup
+ material batch
+ weave registration
+ copper profile
+ drill / plating variation
-> channel distribution
```

This is why high-speed links require margin, coupons, measurement, and sometimes equalization rather than trusting one ideal geometry.

## Engineering reconstruction

The experiment in [`../../experiments/weave-roughness/`](../../experiments/weave-roughness/) combines two synthetic effects:

1. frequency-dependent conductor-loss penalty from roughness;
2. differential skew from unequal resin/glass exposure.

It demonstrates how a board can pass a low-frequency continuity view while failing a high-speed timing/loss budget.

It is not a field solver.

## What became invisible

A modern motherboard's high-speed channel depends on industries that once looked like ordinary materials supply:

```text
copper foil profile
foil treatment
resin chemistry
glass yarn
weave style
prepreg construction
lamination registration
stackup control
coupon measurement
TDR / VNA characterization
```

The faster the computer became, the more its “wires” turned back into materials science.

[^intel-highspeed]: Altera/Intel, *High-Speed Board Design Advisor: High-Speed Channel Design and Layout*, which discusses dielectric loss, conductor loss, copper geometry, and via-stub considerations, https://cdrdv2-public.intel.com/652630/tb-095.pdf .
[^intel-weave]: Intel, “Fiberglass Weave Composition,” PCB stackup guidance describing propagation skew from nonuniform glass/resin dielectric environment and recommending tighter/spread glass or angled routing for high-speed signals, https://www.intel.com/content/www/us/en/docs/programmable/683883/current/fiberglass-weave-composition.html .
[^ipc-roughness]: IPC conference material, “The Effect of Radiation Losses on High Frequency PCB Performance,” includes conductor-loss modeling with a copper-roughness multiplier, https://www.ipc.org/system/files/technical_resource/E15%26S30_01.pdf .
