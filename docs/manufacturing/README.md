# Manufacturing Substrate

Computers do not emerge directly from logic diagrams.

Between an architectural idea and a working machine sits an industrial stack:

```text
materials
-> semiconductor process
-> wafer fabrication
-> yield and test
-> packaging
-> printed wiring
-> board assembly
-> inspection / rework
-> system integration
```

This track reconstructs the manufacturing capabilities that made computing scalable.

## Semiconductor platform

- [`../semiconductor/why-silicon-became-the-platform.md`](../semiconductor/why-silicon-became-the-platform.md) — germanium, high-purity silicon, diffusion, SiO2, and photolithography.
- [`../semiconductor/why-planar-processing-made-ic-manufacturing-repeatable.md`](../semiconductor/why-planar-processing-made-ic-manufacturing-repeatable.md) — how planar processing turned integration into a repeatable wafer process.
- [`../semiconductor/why-the-fab-became-a-machine-around-the-machine.md`](../semiconductor/why-the-fab-became-a-machine-around-the-machine.md) — cleanrooms, process recipes, equipment, metrology, and the factory as part of the device.
- [`../semiconductor/why-yield-is-an-architectural-constraint.md`](../semiconductor/why-yield-is-an-architectural-constraint.md) — die area, defect density, test, binning, and cost.
- [`../packaging/why-a-chip-needs-a-package.md`](../packaging/why-a-chip-needs-a-package.md) — fan-out, protection, thermal limits, pin count, and DIP/PCB co-evolution.

## Printed wiring and assembly

- [`../pcb/why-printed-wiring-replaced-hand-wiring.md`](../pcb/why-printed-wiring-replaced-hand-wiring.md) — printed circuits, Signal Corps Auto-Sembly, batch soldering, reproducibility, and repair.
- [`../pcb/why-the-board-became-a-system-layer.md`](../pcb/why-the-board-became-a-system-layer.md) — double-sided/multilayer routing, plated holes, packaging, signal integrity, and board manufacturing as system engineering.

## Experiments

- [`../../experiments/wafer-yield/`](../../experiments/wafer-yield/) — die area / defect density / cost.
- [`../../experiments/lithography-overlay/`](../../experiments/lithography-overlay/) — mask count and synthetic overlay error.
- [`../../experiments/process-stack/`](../../experiments/process-stack/) — cumulative process-step survival.
- [`../../experiments/package-pin-budget/`](../../experiments/package-pin-budget/) — package pins versus parallel/multiplexed interfaces.
- [`../../experiments/pcb-routing-density/`](../../experiments/pcb-routing-density/) — routing-layer pressure in a deliberately simple geometry model.
- [`../../experiments/assembly-defects/`](../../experiments/assembly-defects/) — independent hand connections versus repeatable batch assembly failure structures.

## Source map

See [`../references/manufacturing-substrate-field-set.md`](../references/manufacturing-substrate-field-set.md).

## What this track is trying to preserve

The manufacturing layer is unusually easy to erase from computer history because successful manufacturing becomes invisible.

A chip data sheet rarely tells you about:

- silicon purification;
- crystal growth;
- oxidation furnaces;
- photoresist;
- mask alignment;
- wafer cleaning;
- contamination control;
- process drift;
- probe stations;
- wire bonding;
- lead frames;
- copper-clad laminates;
- drill wear;
- plating chemistry;
- solder baths;
- board inspectors;
- rework technicians.

Yet these are precisely the things that determine whether a design can be built once, a thousand times, or a billion times.

> **The semiconductor revolution is not only the history of smaller switches. It is the history of repeatable manufacturing at microscopic scale, connected to repeatable manufacturing at board scale.**
