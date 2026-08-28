# Why Microvia Filling Became Electrochemistry

High-density interconnect PCB technology creates a problem that looks like geometry:

> how do we connect one tiny layer to another through a blind hole?

But once the hole becomes small enough, the real problem becomes electrochemistry.

A microvia cannot merely be “copper plated.” It has to be plated in a way that fills a recessed feature without trapping a void, leaving a weak seam, or building excessive copper on the surface.

That makes microvia filling a board-level cousin of damascene copper in integrated circuits.

## Miniaturization changes the objective

IPC technical literature describes blind microvias emerging in the late 1980s and early 1990s, with copper filling becoming increasingly important in the following years.[^ipc-microvia]

Early approaches could plate walls or use plugging materials.

But stacking vias, via-in-pad structures, and fine-pitch routing reward **solid copper fill**.

The manufacturing objective therefore changes:

```text
make hole conductive
```

becomes:

```text
fill hole densely and reliably
while limiting surface overplating
```

## Conformal plating is not necessarily good enough

If copper deposits at roughly the same rate everywhere, a narrow opening can close before the interior is completely filled.

That creates:

- seams;
- voids;
- trapped chemistry;
- weak thermal/electrical paths.

So the desirable profile is often intentionally non-uniform.

The bottom of the feature may need to plate faster than the opening.

This is the same basic geometry problem that appears in chip-level copper superfilling.

## Additives turn a plating bath into a shape-control system

Electrolytic copper baths can contain additive systems that modify local deposition kinetics.

The result is not simply “more copper.”

It is controlled spatial growth.

A useful simplified picture is:

```text
copper ions
+ current
+ suppressor
+ accelerator
+ leveler
+ transport
+ via geometry
-> fill profile
```

That means a chemistry supplier is helping determine the 3D geometry of the final PCB interconnect.

The experiment in [`../../experiments/microvia-fill/`](../../experiments/microvia-fill/) compares a synthetic conformal fill with a bottom-up filling profile.

It is not a plating recipe.

## Surface copper is part of the tradeoff

A process that fills a via successfully can still create too much copper on the surrounding surface.

Excess surface thickness affects:

- later imaging;
- line/space capability;
- etch burden;
- planarity;
- material cost.

So via fill must be optimized jointly with panel-level copper distribution.

The best fill process is not the one that deposits copper fastest everywhere.

## Aspect ratio becomes a chemistry variable

As vias become deeper relative to their diameter, transport becomes harder.

Fresh ions and additives must reach recessed surfaces while reaction products leave.

So geometry influences local chemistry:

```text
feature depth
+ opening size
+ agitation / flow
+ additive transport
-> local deposition behavior
```

This is another example of algorithm-like path dependence inside manufacturing: the shape of the feature changes the behavior of the process intended to create the shape.

## HDI creates a materials/equipment ecosystem

Reliable microvia production depends on more than plating bath formulation.

It also depends on:

- laser drilling;
- desmear / cleaning;
- seed or electroless copper;
- electrolytic copper;
- panel agitation;
- current distribution;
- bath analysis;
- additive replenishment;
- cross-section inspection;
- thermal-cycle qualification.

The microvia therefore sits at the intersection of laser processing, wet chemistry, electrochemistry, and PCB reliability.

## Filled copper can replace plugging complexity

IPC literature notes that filled-via electroplating can avoid some extra process steps and materials associated with conductive plugging approaches.[^ipc-microvia]

This is historically interesting because a “more sophisticated chemistry” can simplify the overall factory route.

The right process innovation can move complexity from many assembly steps into one tightly controlled bath.

## Why this belongs in computer history

Modern compact electronics depend on boards and package substrates with extraordinary routing density.

The processor may receive most of the attention, but its signals still need to escape through:

- package build-up layers;
- vias;
- board layers;
- connectors.

If the tiny vertical connections cannot be manufactured reliably, the computational device cannot become a compact consumer product.

> **Miniaturization does not stop at the transistor. It continues through the electrochemistry of the board.**

## References

[^ipc-microvia]: IPC technical paper, “Filling of Microvias and Through Holes by Electrolytic Copper Plating,” discussing blind-microvia history, copper fill, and HDI manufacturing drivers, https://www.ipc.org/system/files/technical_resource/E42%26S02_01%20-%20Moody%20Dreiza_Mustafa%20Oezkoek.pdf

## Source note

The IPC paper is later industry technical literature that reconstructs microvia filling development over prior decades. It is useful for process lineage and current engineering logic, but detailed first-use claims should be checked against contemporary board-house and equipment records where available.