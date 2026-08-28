# Manufacturing Is Part of Computing History

A computer history that jumps from transistor invention to integrated circuits and then to microprocessors skips the industrial substrate that made the transition possible.

This repository treats manufacturing as a first-class historical track.

Start with [`docs/manufacturing/README.md`](docs/manufacturing/README.md).

## Semiconductor material and wafer fabrication

- [`docs/semiconductor/why-silicon-became-the-platform.md`](docs/semiconductor/why-silicon-became-the-platform.md)
- [`docs/semiconductor/why-semiconductor-purity-became-an-industrial-process.md`](docs/semiconductor/why-semiconductor-purity-became-an-industrial-process.md)
- [`docs/semiconductor/why-wafers-kept-getting-larger.md`](docs/semiconductor/why-wafers-kept-getting-larger.md)
- [`docs/semiconductor/why-planar-processing-made-ic-manufacturing-repeatable.md`](docs/semiconductor/why-planar-processing-made-ic-manufacturing-repeatable.md)
- [`docs/semiconductor/why-mask-making-became-a-machine-tool-industry.md`](docs/semiconductor/why-mask-making-became-a-machine-tool-industry.md)
- [`docs/semiconductor/why-lithography-became-a-capital-equipment-race.md`](docs/semiconductor/why-lithography-became-a-capital-equipment-race.md)
- [`docs/semiconductor/why-ion-implantation-made-doping-programmable.md`](docs/semiconductor/why-ion-implantation-made-doping-programmable.md)
- [`docs/semiconductor/why-mos-was-hard-before-it-was-cheap.md`](docs/semiconductor/why-mos-was-hard-before-it-was-cheap.md)
- [`docs/semiconductor/why-eprom-made-hardware-development-iterative.md`](docs/semiconductor/why-eprom-made-hardware-development-iterative.md)
- [`docs/semiconductor/why-the-fab-became-a-machine-around-the-machine.md`](docs/semiconductor/why-the-fab-became-a-machine-around-the-machine.md)
- [`docs/semiconductor/why-yield-is-an-architectural-constraint.md`](docs/semiconductor/why-yield-is-an-architectural-constraint.md)

## Equipment, automation, test, and industry structure

- [`docs/manufacturing/why-equipment-vendors-became-part-of-the-process.md`](docs/manufacturing/why-equipment-vendors-became-part-of-the-process.md)
- [`docs/manufacturing/why-automatic-test-became-an-industry.md`](docs/manufacturing/why-automatic-test-became-an-industry.md)
- [`docs/manufacturing/why-smif-put-the-cleanroom-around-the-wafer.md`](docs/manufacturing/why-smif-put-the-cleanroom-around-the-wafer.md)
- [`docs/manufacturing/why-design-rules-became-an-interface-to-the-fab.md`](docs/manufacturing/why-design-rules-became-an-interface-to-the-fab.md)
- [`docs/manufacturing/why-foundries-separated-design-from-fabrication.md`](docs/manufacturing/why-foundries-separated-design-from-fabrication.md)

These pages trace the second-order industry beneath semiconductors: crystal growers, mask shops, furnaces, lithography tools, implanters, wafer probers, automatic test, minienvironments, EDA/design-rule interfaces, and foundries that sell process capability as a service.

## Packaging and board assembly

- [`docs/packaging/why-a-chip-needs-a-package.md`](docs/packaging/why-a-chip-needs-a-package.md)
- [`docs/packaging/why-wire-bonds-failed-in-strange-colors.md`](docs/packaging/why-wire-bonds-failed-in-strange-colors.md)
- [`docs/packaging/why-flip-chip-shortened-the-interconnect.md`](docs/packaging/why-flip-chip-shortened-the-interconnect.md)
- [`docs/pcb/why-printed-wiring-replaced-hand-wiring.md`](docs/pcb/why-printed-wiring-replaced-hand-wiring.md)
- [`docs/pcb/why-the-board-became-a-system-layer.md`](docs/pcb/why-the-board-became-a-system-layer.md)
- [`docs/pcb/why-surface-mount-changed-the-board-factory.md`](docs/pcb/why-surface-mount-changed-the-board-factory.md)

## Source maps

- [`docs/references/manufacturing-substrate-field-set.md`](docs/references/manufacturing-substrate-field-set.md)
- [`docs/references/manufacturing-substrate-2-field-set.md`](docs/references/manufacturing-substrate-2-field-set.md)
- [`docs/references/manufacturing-substrate-3-field-set.md`](docs/references/manufacturing-substrate-3-field-set.md)

## Why this deserves its own track

The computer industry depends on other industries that ordinary architecture histories can make invisible:

```text
high-purity semiconductor materials
zone refining / crystal growth / wafer preparation
oxidation / diffusion / epitaxy / implantation
photoresist / mask making / lithography / reticle inspection
etch / deposition / contamination control
wafer probing / automatic test / yield analysis
sealed carriers / robotic material handling
wire bonding / flip-chip / packaging
copper-clad laminates / drilling / plating / multilayer PCB
through-hole / wave solder / SMT / paste / reflow
inspection / rework / X-ray / field service
semiconductor equipment suppliers
EDA / design rules / PDK-like interfaces
foundries / fabless design interfaces
```

These are not peripheral production details. They determine what architectures can be manufactured reliably, revised quickly, tested economically, connected densely, and sold cheaply enough to matter.

## Runnable manufacturing experiments

The manufacturing experiments are deliberately synthetic. They expose constraint structure without pretending to be historical fab data.

First field set:

- [`experiments/wafer-yield/`](experiments/wafer-yield/)
- [`experiments/lithography-overlay/`](experiments/lithography-overlay/)
- [`experiments/process-stack/`](experiments/process-stack/)
- [`experiments/package-pin-budget/`](experiments/package-pin-budget/)
- [`experiments/pcb-routing-density/`](experiments/pcb-routing-density/)
- [`experiments/assembly-defects/`](experiments/assembly-defects/)

Second field set:

- [`experiments/dopant-signal/`](experiments/dopant-signal/)
- [`experiments/wafer-scale/`](experiments/wafer-scale/)
- [`experiments/mask-replication/`](experiments/mask-replication/)
- [`experiments/mos-margin/`](experiments/mos-margin/)
- [`experiments/firmware-iteration/`](experiments/firmware-iteration/)
- [`experiments/tool-bottleneck/`](experiments/tool-bottleneck/)
- [`experiments/smt-density/`](experiments/smt-density/)
- [`experiments/foundry-boundary/`](experiments/foundry-boundary/)

Third field set:

- [`experiments/implant-dose/`](experiments/implant-dose/)
- [`experiments/lithography-throughput/`](experiments/lithography-throughput/)
- [`experiments/test-economics/`](experiments/test-economics/)
- [`experiments/bond-thermal-budget/`](experiments/bond-thermal-budget/)
- [`experiments/flip-chip-interconnect/`](experiments/flip-chip-interconnect/)
- [`experiments/minienvironment-exposure/`](experiments/minienvironment-exposure/)
- [`experiments/design-rule-interface/`](experiments/design-rule-interface/)

## Next excavations

The manufacturing track can now go deeper rather than rebuilding its foundation:

- specific e-beam mask-writer and reticle-inspection histories;
- stepper-to-scanner transition, wavelength changes, and lithography metrology;
- rapid thermal anneal and implant-damage recovery;
- statistical process control, run-to-run control, parametric test, and yield-learning organizations;
- probe cards, test sockets, burn-in, and ATE software/programming history;
- IBM C4, underfill, PGA/QFP/BGA, flip-chip, and package thermal design;
- purple plague, electromigration, corrosion, delamination, solder fatigue, and other failure mechanisms;
- phenolic laminates, FR-4, plated-through-hole, multilayer lamination, microvias;
- wave soldering, paste printing, pick-and-place, reflow, AOI, ICT, X-ray inspection;
- connectors, sockets, backplanes, cables, power distribution, and field-repair economics;
- SMIF-to-FOUP, 200/300 mm automated material handling, MES, and electronic lot tracking;
- semiconductor assembly and PCB production labor/geography;
- equipment-vendor ecosystems and process co-development;
- MOSIS, GDSII, PDKs, EDA/IP ecosystems, and the global fabless model.

> **A billion-transistor processor is not only a triumph of logic design. It is evidence that an enormous manufacturing civilization learned to purify matter, grow crystals, reproduce patterns, control interfaces, test populations, move wafers, connect packages, and coordinate factories with extraordinary reliability.**
