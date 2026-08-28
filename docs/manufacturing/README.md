# Manufacturing Substrate

Computers do not emerge directly from logic diagrams.

Between an architectural idea and a working machine sits an industrial stack:

```text
materials
-> crystal / wafer
-> semiconductor process
-> lithography / equipment
-> implant / anneal
-> yield / probe / automatic test
-> packaging
-> printed wiring
-> board assembly
-> inspection / rework
-> automated material handling
-> system integration
```

This track reconstructs the manufacturing capabilities that made computing scalable.

## Materials, crystals, and wafers

- [`../semiconductor/why-silicon-became-the-platform.md`](../semiconductor/why-silicon-became-the-platform.md)
- [`../semiconductor/why-semiconductor-purity-became-an-industrial-process.md`](../semiconductor/why-semiconductor-purity-became-an-industrial-process.md)
- [`../semiconductor/why-wafers-kept-getting-larger.md`](../semiconductor/why-wafers-kept-getting-larger.md)

## Wafer processing and lithography

- [`../semiconductor/why-planar-processing-made-ic-manufacturing-repeatable.md`](../semiconductor/why-planar-processing-made-ic-manufacturing-repeatable.md)
- [`../semiconductor/why-mask-making-became-a-machine-tool-industry.md`](../semiconductor/why-mask-making-became-a-machine-tool-industry.md)
- [`../semiconductor/why-lithography-became-a-capital-equipment-race.md`](../semiconductor/why-lithography-became-a-capital-equipment-race.md)
- [`../semiconductor/why-ion-implantation-made-doping-programmable.md`](../semiconductor/why-ion-implantation-made-doping-programmable.md)
- [`../semiconductor/why-mos-was-hard-before-it-was-cheap.md`](../semiconductor/why-mos-was-hard-before-it-was-cheap.md)
- [`../semiconductor/why-the-fab-became-a-machine-around-the-machine.md`](../semiconductor/why-the-fab-became-a-machine-around-the-machine.md)
- [`../semiconductor/why-yield-is-an-architectural-constraint.md`](../semiconductor/why-yield-is-an-architectural-constraint.md)

## Iteration, equipment, test, and industrial organization

- [`../semiconductor/why-eprom-made-hardware-development-iterative.md`](../semiconductor/why-eprom-made-hardware-development-iterative.md)
- [`why-equipment-vendors-became-part-of-the-process.md`](why-equipment-vendors-became-part-of-the-process.md)
- [`why-automatic-test-became-an-industry.md`](why-automatic-test-became-an-industry.md)
- [`why-smif-put-the-cleanroom-around-the-wafer.md`](why-smif-put-the-cleanroom-around-the-wafer.md)
- [`why-design-rules-became-an-interface-to-the-fab.md`](why-design-rules-became-an-interface-to-the-fab.md)
- [`why-foundries-separated-design-from-fabrication.md`](why-foundries-separated-design-from-fabrication.md)

## Packaging and board assembly

- [`../packaging/why-a-chip-needs-a-package.md`](../packaging/why-a-chip-needs-a-package.md)
- [`../packaging/why-wire-bonds-failed-in-strange-colors.md`](../packaging/why-wire-bonds-failed-in-strange-colors.md)
- [`../packaging/why-flip-chip-shortened-the-interconnect.md`](../packaging/why-flip-chip-shortened-the-interconnect.md)
- [`../pcb/why-printed-wiring-replaced-hand-wiring.md`](../pcb/why-printed-wiring-replaced-hand-wiring.md)
- [`../pcb/why-the-board-became-a-system-layer.md`](../pcb/why-the-board-became-a-system-layer.md)
- [`../pcb/why-surface-mount-changed-the-board-factory.md`](../pcb/why-surface-mount-changed-the-board-factory.md)

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

Third field set:

- [`../../experiments/implant-dose/`](../../experiments/implant-dose/)
- [`../../experiments/lithography-throughput/`](../../experiments/lithography-throughput/)
- [`../../experiments/test-economics/`](../../experiments/test-economics/)
- [`../../experiments/bond-thermal-budget/`](../../experiments/bond-thermal-budget/)
- [`../../experiments/flip-chip-interconnect/`](../../experiments/flip-chip-interconnect/)
- [`../../experiments/minienvironment-exposure/`](../../experiments/minienvironment-exposure/)
- [`../../experiments/design-rule-interface/`](../../experiments/design-rule-interface/)

## Source maps

- [`../references/manufacturing-substrate-field-set.md`](../references/manufacturing-substrate-field-set.md)
- [`../references/manufacturing-substrate-2-field-set.md`](../references/manufacturing-substrate-2-field-set.md)
- [`../references/manufacturing-substrate-3-field-set.md`](../references/manufacturing-substrate-3-field-set.md)

## What this track is trying to preserve

The manufacturing layer is unusually easy to erase from computer history because successful manufacturing becomes invisible.

A chip data sheet rarely tells you about:

```text
zone refining
crystal pullers
wafer slicing / polishing
mask artwork / reticle writing
projection optics / stage control
implant beams / anneal
cleanroom shifts / sealed carriers
wafer probing / ATE programs
binning / failure analysis
wire bonds / solder bumps
package inspection
board drilling / plating
paste printing / pick-and-place / reflow
AOI / X-ray / rework
foundry customer engineering
PDK / design-rule maintenance
```

Yet these are precisely the things that determine whether a design can be built once, a thousand times, or a billion times.

> **The semiconductor revolution is not only the history of smaller switches. It is the history of an industrial system learning to control matter, geometry, interfaces, defects, feedback loops, and organizational boundaries at microscopic scale — then connect the result reliably at package, board, and system scale.**
