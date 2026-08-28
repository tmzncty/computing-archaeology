# Manufacturing Substrate

Computers do not emerge directly from logic diagrams.

Between an architectural idea and a working machine sits an industrial stack:

```text
materials
-> crystal / wafer
-> semiconductor process
-> lithography / equipment
-> yield and test
-> packaging
-> printed wiring
-> board assembly
-> inspection / rework
-> system integration
```

This track reconstructs the manufacturing capabilities that made computing scalable.

## Materials, crystals, and wafers

- [`../semiconductor/why-silicon-became-the-platform.md`](../semiconductor/why-silicon-became-the-platform.md) — why silicon and silicon dioxide became a process platform.
- [`../semiconductor/why-semiconductor-purity-became-an-industrial-process.md`](../semiconductor/why-semiconductor-purity-became-an-industrial-process.md) — zone refining, Czochralski-derived crystal growth, float-zone processing, and why intentional doping requires extreme purity.
- [`../semiconductor/why-wafers-kept-getting-larger.md`](../semiconductor/why-wafers-kept-getting-larger.md) — why wafer area is economic leverage and why diameter transitions require factory-wide changes.

## Wafer processing and lithography

- [`../semiconductor/why-planar-processing-made-ic-manufacturing-repeatable.md`](../semiconductor/why-planar-processing-made-ic-manufacturing-repeatable.md) — planar processing and integration as a repeatable wafer process.
- [`../semiconductor/why-mask-making-became-a-machine-tool-industry.md`](../semiconductor/why-mask-making-became-a-machine-tool-industry.md) — rubylith, photographic reduction, step-and-repeat, overlay, masks, and lithography-tool specialization.
- [`../semiconductor/why-mos-was-hard-before-it-was-cheap.md`](../semiconductor/why-mos-was-hard-before-it-was-cheap.md) — MOS surface/interface instability, process maturation, silicon gate, and density economics.
- [`../semiconductor/why-the-fab-became-a-machine-around-the-machine.md`](../semiconductor/why-the-fab-became-a-machine-around-the-machine.md) — cleanrooms, recipes, metrology, contamination control, and fab operations.
- [`../semiconductor/why-yield-is-an-architectural-constraint.md`](../semiconductor/why-yield-is-an-architectural-constraint.md) — die area, defect density, test, binning, and cost per good function.

## Iteration, equipment, and industrial organization

- [`../semiconductor/why-eprom-made-hardware-development-iterative.md`](../semiconductor/why-eprom-made-hardware-development-iterative.md) — why erasable nonvolatile memory shortened firmware feedback loops.
- [`why-equipment-vendors-became-part-of-the-process.md`](why-equipment-vendors-became-part-of-the-process.md) — furnaces, epitaxy, implantation, probing, lithography, and the second-order industry that manufactures fab capability.
- [`why-foundries-separated-design-from-fabrication.md`](why-foundries-separated-design-from-fabrication.md) — how independent manufacturing, explicit process interfaces, PDK-like contracts, and the pure-play foundry model changed which chip companies could exist.

## Packaging and board assembly

- [`../packaging/why-a-chip-needs-a-package.md`](../packaging/why-a-chip-needs-a-package.md) — fan-out, protection, thermal limits, pin count, and DIP/PCB co-evolution.
- [`../pcb/why-printed-wiring-replaced-hand-wiring.md`](../pcb/why-printed-wiring-replaced-hand-wiring.md) — printed circuits, Signal Corps Auto-Sembly, batch soldering, reproducibility, and repair.
- [`../pcb/why-the-board-became-a-system-layer.md`](../pcb/why-the-board-became-a-system-layer.md) — multilayer routing, plated holes, packaging, signal integrity, and board manufacturing as system engineering.
- [`../pcb/why-surface-mount-changed-the-board-factory.md`](../pcb/why-surface-mount-changed-the-board-factory.md) — why eliminating through-hole leads changed routing density, placement automation, soldering, inspection, and repair economics.

## Experiments

First field set:

- [`../../experiments/wafer-yield/`](../../experiments/wafer-yield/)
- [`../../experiments/lithography-overlay/`](../../experiments/lithography-overlay/)
- [`../../experiments/process-stack/`](../../experiments/process-stack/)
- [`../../experiments/package-pin-budget/`](../../experiments/package-pin-budget/)
- [`../../experiments/pcb-routing-density/`](../../experiments/pcb-routing-density/)
- [`../../experiments/assembly-defects/`](../../experiments/assembly-defects/)

Second field set:

- [`../../experiments/dopant-signal/`](../../experiments/dopant-signal/)
- [`../../experiments/wafer-scale/`](../../experiments/wafer-scale/)
- [`../../experiments/mask-replication/`](../../experiments/mask-replication/)
- [`../../experiments/mos-margin/`](../../experiments/mos-margin/)
- [`../../experiments/firmware-iteration/`](../../experiments/firmware-iteration/)
- [`../../experiments/tool-bottleneck/`](../../experiments/tool-bottleneck/)
- [`../../experiments/smt-density/`](../../experiments/smt-density/)
- [`../../experiments/foundry-boundary/`](../../experiments/foundry-boundary/)

## Source maps

- [`../references/manufacturing-substrate-field-set.md`](../references/manufacturing-substrate-field-set.md)
- [`../references/manufacturing-substrate-2-field-set.md`](../references/manufacturing-substrate-2-field-set.md)

## What this track is trying to preserve

The manufacturing layer is unusually easy to erase from computer history because successful manufacturing becomes invisible.

A chip data sheet rarely tells you about:

```text
zone refining
crystal pullers
wafer slicing / polishing
mask artwork
photo-repeaters
furnace uniformity
epitaxy reactors
implant beams
cleanroom shifts
wafer probing
process-control charts
package assembly
board drilling / plating
paste printing
pick-and-place
reflow
inspection / rework
foundry customer engineering
```

Yet these are precisely the things that determine whether a design can be built once, a thousand times, or a billion times.

> **The semiconductor revolution is not only the history of smaller switches. It is the history of an industrial system learning to control matter, geometry, interfaces, defects, and feedback loops at microscopic scale — then connect the result reliably at board and system scale.**
