# Why Surface Mount Changed the Board Factory

Through-hole assembly makes an intuitive picture:

```text
component lead
-> hole in board
-> solder joint on the other side
```

It is mechanically understandable and easy to repair.

But every hole consumes board area, drilling time, routing freedom, and assembly geometry.

The historical question is:

> **What changes when components stop needing leads to pass through the board at all?**

Surface-mount technology changes not only component packages but the entire board-production system.

## Through-holes solve one problem and create several others

Plated-through holes became essential to double-sided and multilayer printed-circuit boards because they allowed electrical connection between layers and component leads.[^army-pcb]

But a through-hole is expensive geometry.

It occupies space through the thickness of the board and can block routing on multiple layers.

For a dense system, component lead pitch and hole diameter become architectural constraints on the board.

### Reconstruction

If every signal pin requires a drilled plated hole, then increasing pin count creates several linked pressures:

```text
more pins
-> more holes
-> more blocked routing area
-> more layers or larger board
-> more drilling / plating / assembly cost
```

The component package and the PCB factory are negotiating the same geometry.

## Surface mounting removes the lead-through-board requirement

Surface-mount packages attach directly to pads on the board surface rather than requiring every terminal to pass through a hole.

The Computer History Museum's glossary defines SMT as a package format in which chips are mounted on the surface rather than through PCB holes.[^chm-glossary]

By the 1980s industry literature was describing SMT as a major packaging transition because it could increase board density, eliminate many costly through-holes, reduce layer pressure, and make automated board population easier.[^amd-smt]

This is not merely “smaller packages.”

It is a change in manufacturing topology.

## SMT makes placement automation more valuable

Through-hole parts can be manually inserted relatively easily because their leads physically locate the part in drilled holes.

Surface-mount parts require accurate placement on pads before soldering.

That creates strong incentives for:

- component tapes/trays;
- pick-and-place machines;
- fiducials;
- controlled solder-paste deposition;
- placement accuracy;
- automated inspection.

The assembly line becomes more dependent on machine vision, motion control, feeders, and process control.

## Solder paste changes the joining sequence

A common surface-mount flow separates solder alloy placement from component placement:

```text
print solder paste
-> place component
-> reflow board
-> inspect / test
```

That differs from individually soldering leads or passing a leaded board through a bulk soldering process.

The solder joint is created as part of a thermal process applied to the assembled board.

### Reconstruction

This shifts failure modes.

Instead of only asking whether a joint received enough solder, the process must control:

- paste volume;
- stencil definition;
- component placement;
- wetting;
- thermal profile;
- tombstoning/skew;
- bridges;
- hidden joints under some package families.

Assembly becomes a statistical process rather than a sequence of visible hand operations.

## Package standardization matters

The 1985 AMD packaging literature describes industry pressure to standardize surface-mount package outlines and explains the manufacturing attraction of higher board density, fewer through-holes, and automated board population.[^amd-smt]

This is an important compatibility point.

A board factory cannot automate effectively if every vendor invents a unique mechanical footprint, feeder, and handling method.

So package standards are manufacturing infrastructure.

They let component vendors and assembly-equipment vendors build around common geometries.

## Surface mount changes repair economics

Dense SMT boards can be cheaper to manufacture in volume while being harder to repair manually.

Fine-pitch packages, hidden solder joints, and small passive components can require specialized rework tools, microscopes, hot-air systems, or board-level replacement strategies.

This creates a familiar computing tradeoff:

> manufacturing efficiency improves while field-level inspectability decreases.

The board becomes more like an integrated subsystem and less like a collection of individually obvious parts.

## SMT and multilayer routing reinforce each other

Surface mounting frees routing space that would otherwise be consumed by through-hole barrels, while multilayer boards provide additional routing and power-distribution resources.

Together they allow much denser assemblies.

But the system now depends on more manufacturing layers:

```text
package coplanarity
pad geometry
solder mask
paste stencil
placement
reflow
inspection
multilayer registration
via technology
```

Density moves complexity into the factory.

## Why this belongs in computing history

The shrinking of computers is often credited entirely to IC integration.

But a small chip is not useful if the board around it still requires enormous mechanical spacing and manual wiring.

Surface mount, multilayer PCBs, automated placement, and controlled soldering allow the **rest of the computer** to shrink alongside the silicon.

Portable computers, dense expansion cards, compact storage devices, and eventually phones depend as much on assembly technology as on transistor count.

## What this teaches us

Surface mount is a good example of manufacturing changing system architecture without changing the Boolean logic.

The circuit may be logically identical.

But when the package and board no longer require a forest of drilled lead holes, the product can become:

- smaller;
- more automated to assemble;
- cheaper at volume;
- denser;
- less manually repairable.

The board factory is therefore part of the history of computer miniaturization.

## References

[^army-pcb]: U.S. Army Communications-Electronics Command, “Historical Innovations pave the way for current microelectronic mission at CECOM,” 2026, https://www.army.mil/article-amp/290502/historical_innovations_pave_the_way_for_current_microelectronic_mission_at_cecom
[^chm-glossary]: Computer History Museum, *The Silicon Engine* glossary, entry “SMT,” https://www.computerhistory.org/siliconengine/glossary/
[^amd-smt]: Michael C. Lancaster, “Surface Mount Technology, Plastic Chip Carrier Trends,” in *1985 AMD Annual Proceedings*, preserved by Bitsavers, https://bitsavers.computerhistory.org/components/amd/_dataBooks/1985_AMD_Annual_Proceedings.pdf

## Source note

The Army article is a recent institutional synthesis for printed-wiring history; the AMD proceedings provide contemporary industry evidence for the 1980s SMT transition. A deeper treatment should add IPC/JEDEC package standards, assembly-equipment manuals, solder-process literature, board-house records, and oral histories from line operators and rework technicians.