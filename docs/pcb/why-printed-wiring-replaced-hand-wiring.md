# Why Did Printed Wiring Replace Hand Wiring?

Before the printed circuit board became invisible infrastructure, electronic equipment was commonly assembled by point-to-point wiring: a worker connected components to sockets, terminal strips, and other parts with individual wires.

That method can produce excellent equipment. It is also labor-intensive, difficult to reproduce perfectly at scale, bulky, and vulnerable to wiring mistakes.

The historical question is:

> **When does wiring stop being an artisanal assembly task and become a manufactured pattern?**

## Printed circuits did not begin with computers

Printed-wiring ideas appeared before World War II. Paul Eisler is closely associated with the practical printed circuit in the 1930s and 1940s, while wartime proximity-fuze work pushed printed techniques into production.

A 1947 National Bureau of Standards circular described printed electronic circuits as already beyond the experimental stage and noted their wartime use.[^army-history]

The point is not to award one simple “first PCB” badge. Multiple printing, plating, spraying, etching, and lamination techniques converged over decades.

## The Army's Auto-Sembly process attacked assembly labor

In 1949 U.S. Signal Corps engineers Moe Abramson and Stanislaus F. Danko developed an “Auto-Sembly” process: component leads were inserted through holes in printed/etched circuitry and many joints could be soldered together in a bath rather than individually with a soldering iron.[^army-history]

This is a manufacturing breakthrough because it changes the unit of work.

Point-to-point assembly says:

```text
wire one connection
inspect one connection
repeat
```

Printed-board assembly says:

```text
manufacture wiring pattern once
insert many components
solder many joints in one process
```

The wiring geometry becomes repeatable tooling.

## A PCB is both wiring and structure

A printed circuit board does several jobs at once:

- mechanically locates components;
- defines electrical connections;
- constrains spacing and orientation;
- creates a reproducible module;
- supports automated inspection and test;
- provides standardized connectors to the rest of the machine.

This is why a PCB is more than a convenient replacement for wires. It turns circuit topology into a manufactured object.

## Repeatability changes reliability

Hand wiring can be repaired and rerouted easily, but two nominally identical units may contain different wire lengths, dress, solder quality, and accidental coupling.

A printed pattern reduces that variation.

For digital machines, standardized boards also enable maintenance by replacement:

```text
faulty logic module
-> remove board
-> insert spare
-> repair board offline
```

That maintenance model appears repeatedly in transistorized computers.

## PCB and semiconductor lithography are cousins

One of the most interesting cross-industry links is that photoengraving methods used for printed circuits were adapted to semiconductor photolithography at Bell Labs in the 1950s.[^chm-photo]

The two industries therefore share a manufacturing idea:

> use a patterning process to replace individually placed conductors.

At board scale the pattern is copper wiring. At wafer scale it defines diffusion windows and later transistor/interconnect geometry.

## Reconstruction: printed wiring shifts skill upstream

PCBs do not eliminate skilled labor. They relocate it.

Instead of every assembler deciding where every wire travels, more work moves into:

- artwork/layout;
- laminate and copper-foil production;
- imaging;
- etching;
- drilling/punching;
- plating;
- solder processing;
- inspection;
- test fixtures;
- process control.

A mass-produced board is easier to assemble because the factory preparation is more elaborate.

This is the same inversion seen in integrated circuits.

## The solder joint becomes an industrial process

Dip soldering and later wave soldering let many through-hole joints form in one controlled operation.

That creates new variables: flux, solder temperature, dwell time, board cleanliness, hole/component fit, thermal damage, bridging, and insufficient wetting.

Automation does not remove failure modes. It creates standardized failure modes that can be measured and improved.

## What this teaches us

Printed circuits were a prerequisite for affordable, repeatable transistorized and integrated-circuit systems.

The semiconductor industry made components smaller. The PCB industry made it possible to **assemble those components into machines without wiring every machine from scratch**.

The history of computing therefore runs through etching tanks, drill heads, solder baths, laminates, inspectors, and board-layout departments as surely as it runs through CPU architecture.

## References

[^army-history]: U.S. Army Communications-Electronics Command, “Historical Innovations pave the way for current microelectronic mission at CECOM,” 2026, drawing on Signal Corps historical archives and National Bureau of Standards Circular 468, https://www.army.mil/article/290502/historical_innovations_pave_the_way_for_current_microelectronic_mission_at_cecom
[^chm-photo]: Computer History Museum, “1955: Photolithography Techniques Are Used to Make Silicon Devices,” https://www.computerhistory.org/siliconengine/photolithography-techniques-are-used-to-make-silicon-devices/
