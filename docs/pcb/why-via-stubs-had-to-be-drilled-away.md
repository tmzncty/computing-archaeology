# Why Via Stubs Had to Be Drilled Away

A plated through-hole can be electrically connected exactly as designed and still become a high-speed signal problem because of the copper that is **not** being used.

That unused copper is the via stub.

## Historical record

As serial links moved into multi-gigabit regimes, PCB designers increasingly had to treat through-hole vias as transmission-line structures rather than ideal vertical wires.

IPC conference literature on backdrilling documents the effect of unused via length on impedance matching, insertion loss, crosstalk, and maximum usable signal-line length at high frequency.[^ipc]

The manufacturing response was wonderfully physical:

> drill the finished board again from the other side and remove the unused copper barrel.

## Why the stub matters

Suppose a plated via passes through many board layers, but the signal only enters on one layer and exits on another.

The remaining plated barrel continues beyond the exit layer:

```text
signal path
    |
    +------ target layer
    |
    |
    |  unused plated barrel
    |
```

At low frequency this may be almost irrelevant.

At high frequency it behaves like a transmission-line branch.

A sufficiently long open stub can approach quarter-wave resonance and create a severe notch or reflection in the channel.

## The board contains accidental resonators

This is an important historical shift.

A digital designer once asked:

> Are these nets connected?

A high-speed designer must also ask:

> What electromagnetic structure did the manufacturing geometry accidentally create?

That includes:

- via barrel length;
- anti-pad geometry;
- reference-plane transitions;
- return vias;
- stub resonance;
- connector launches;
- package vias.

Connectivity became insufficient as a description of correctness.

## Backdrilling is subtractive signal integrity

Controlled-depth backdrilling removes the unused via section after the main plated-through-hole structure has been made.

Conceptually:

```text
build full plated via
-> connect required layers
-> identify unused barrel
-> drill away most of it
-> leave controlled residual stub
```

This adds its own manufacturing problems:

- drill registration;
- depth tolerance;
- residual stub control;
- risk of damaging the target layer;
- extra process time;
- inspection.

So a high-speed electrical problem becomes a controlled mechanical drilling operation.

## Why not use blind/buried vias everywhere?

Blind vias, buried vias, and HDI structures can avoid some long stubs, but they carry different fabrication complexity and cost.

Backdrilling survives because it can retrofit high-speed behavior onto conventional multilayer through-hole architecture.

Again, architecture is a compromise between electrical ideality and manufacturing economy.

## Engineering reconstruction

The experiment in [`../../experiments/via-stub-resonance/`](../../experiments/via-stub-resonance/) uses a simple quarter-wave resonance proxy and compares several residual stub lengths.

It demonstrates why reducing a few millimeters of unused copper can move a resonance far enough upward to recover channel margin.

It is not a full via model and omits pads, anti-pads, return paths, mode conversion, loss, and connector effects.

## What became invisible

A modern server or workstation board may contain hundreds of carefully engineered vertical transitions.

Behind a clean routing diagram sit:

```text
drill stack planning
plating
backdrill tool diameter
depth control
registration
residual-stub specification
X-ray / cross-section inspection
signal-integrity simulation
TDR / VNA validation
```

The computer became fast enough that engineers started drilling away copper they had already paid to deposit.

[^ipc]: IPC / ECWC conference paper on backdrilling and unused plated-through-hole length, documenting effects on impedance, insertion loss, crosstalk, and high-frequency routing, https://www.ipc.org/system/files/technical_resource/E17%26S25-3.pdf .
