# Why PCB Surface Finishes Became Electrical and Chemical Interfaces

A bare copper PCB cannot simply wait forever for assembly.

Copper oxidizes, changes solderability, and interacts with storage and handling environments. Fine-pitch assembly also demands flat, predictable pad surfaces.

So the final exposed copper often receives another material system:

- HASL;
- OSP;
- ENIG;
- ENEPIG;
- immersion tin;
- immersion silver;
- electrolytic nickel/gold;
- and other finishes.

This is not cosmetic plating.

The surface finish becomes the **interface between board fabrication, storage, soldering, wire bonding, test contact, and field reliability**.

## Copper needs temporary protection before it becomes a joint

A PCB pad has to survive the interval between fabrication and assembly.

During that time it can encounter:

- oxygen;
- humidity;
- packaging materials;
- fingerprints or contamination;
- multiple reflow cycles;
- cleaning;
- handling.

The finish protects or modifies the copper so that the later joining process remains predictable.

That means the finish is a time bridge:

```text
board fabrication
-> storage / shipping
-> assembly
-> solder joint or bond
```

## Flatness becomes a manufacturing requirement

Older hot-air-solder-leveling processes leave solder on pads, but surface-mount and fine-pitch assembly increasingly value planar pad surfaces.

IPC technical literature compares finishes such as OSP, ENIG, immersion silver/tin, and nickel/gold precisely because no single finish optimizes every requirement.[^ipc-finishes]

The finish can affect:

- solderability;
- coplanarity;
- wire bondability;
- contact wear;
- storage life;
- cost;
- high-frequency behavior.

So choosing a finish is a systems tradeoff.

## ENIG is a stack, not “gold plating”

Electroless nickel / immersion gold (ENIG) builds multiple layers with different jobs.

In simplified form:

```text
copper
-> electroless nickel
-> thin immersion gold
```

The nickel becomes an important barrier/interface; the gold protects the surface and supports assembly/contact behavior.

But because the layers are created chemically, the plating process itself matters.

IPC literature warns that process control is necessary to avoid severe ENIG failure modes such as “black pad.”[^ipc-enig]

That is another example where a finish can look perfect externally while the buried interface is already damaged.

## Thin noble metal can create another metallurgy problem

Gold is useful because it resists oxidation.

But too much gold dissolved into solder can contribute to brittle intermetallic behavior.

So the finish again has a narrow logic:

> enough material to protect and function, but not so much that the final joint chemistry becomes harmful.

The exact acceptable range depends on finish and assembly system.

The general lesson is more important than one thickness number:

> **a protective layer can become a contaminant in the next manufacturing step if its mass balance is wrong.**

## OSP uses a different philosophy

Organic solderability preservative does not rely on a thick metallic barrier stack.

It protects copper with an organic coating intended to preserve solderability until assembly.

That can offer a very flat surface and lower cost, but storage, handling, and repeated thermal exposure create different constraints.[^ipc-finishes]

So two finishes can solve the same high-level problem — “keep pads solderable” — using entirely different material strategies.

## Surface finish can enter signal integrity

At sufficiently high frequencies, surface roughness, conductor geometry, and material conductivity become increasingly important.

Some IPC discussions explicitly compare finishes for high-speed use as well as assembly reliability.[^ipc-finishes]

This is the point where the boundary between “PCB chemistry” and “electrical design” disappears.

The finish is no longer only about whether solder wets.

It can become part of the electrical path.

## Inspection cannot see every interface failure

A plated pad can look visually acceptable while suffering from buried corrosion or interface defects.

That is why surface-finish qualification may need:

- cross-sectioning;
- thickness measurement;
- solderability testing;
- bond testing;
- chemical/process controls;
- destructive analysis.

The appearance of gold is not proof that the interface is healthy.

The experiment in [`../../experiments/surface-finish-tradeoff/`](../../experiments/surface-finish-tradeoff/) uses a synthetic scoring model to show why no finish dominates cost, flatness, storage, bondability, and process-risk simultaneously.

## Why this belongs in computer history

A computer enters a home because millions of solder joints and contacts can be made cheaply and reliably.

That reliability depends on interfaces that may be only micrometers thick.

The final finish therefore belongs to the history of mass-produced computing just as surely as the processor does.

> **The board cannot become a product until its exposed copper has been turned into a predictable manufacturing interface.**

## References

[^ipc-finishes]: IPC technical paper, comparison of common PCB surface finishes including HASL, OSP, ENIG, immersion silver/tin, electrolytic Ni/Au, and ENEPIG, https://www.ipc.org/system/files/technical_resource/E32%26S04-5.pdf
[^ipc-enig]: IPC / ECWC technical resource discussing ENIG, OSP, gold thickness, and black-pad / embrittlement risks, https://www.ipc.org/system/files/technical_resource/E17%26S28-1.pdf

## Source note

The cited IPC papers are industry technical literature and represent mature PCB/assembly practice rather than early printed-circuit invention history. They are used here to reconstruct the engineering role and tradeoffs of surface finishes.