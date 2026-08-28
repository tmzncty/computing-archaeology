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

## Process control, test, automation, and manufacturing data

- [`docs/manufacturing/why-equipment-vendors-became-part-of-the-process.md`](docs/manufacturing/why-equipment-vendors-became-part-of-the-process.md)
- [`docs/manufacturing/why-automatic-test-became-an-industry.md`](docs/manufacturing/why-automatic-test-became-an-industry.md)
- [`docs/manufacturing/why-process-control-became-a-product-feature.md`](docs/manufacturing/why-process-control-became-a-product-feature.md)
- [`docs/manufacturing/why-probe-and-burn-in-screened-a-population.md`](docs/manufacturing/why-probe-and-burn-in-screened-a-population.md)
- [`docs/manufacturing/why-smif-put-the-cleanroom-around-the-wafer.md`](docs/manufacturing/why-smif-put-the-cleanroom-around-the-wafer.md)
- [`docs/manufacturing/why-the-300mm-fab-needed-a-digital-shadow.md`](docs/manufacturing/why-the-300mm-fab-needed-a-digital-shadow.md)
- [`docs/manufacturing/why-design-rules-became-an-interface-to-the-fab.md`](docs/manufacturing/why-design-rules-became-an-interface-to-the-fab.md)
- [`docs/manufacturing/why-tapeout-became-a-data-interface-to-the-mask-shop.md`](docs/manufacturing/why-tapeout-became-a-data-interface-to-the-mask-shop.md)
- [`docs/manufacturing/why-foundries-separated-design-from-fabrication.md`](docs/manufacturing/why-foundries-separated-design-from-fabrication.md)

These pages trace a second machine hidden inside every fab: measurement, event logs, wafer maps, test programs, carriers, robots, mask data, design rules, and software that keeps physical production state consistent.

## Reliability: when a correct device can still die later

- [`docs/reliability/why-electromigration-made-wires-a-lifetime-limit.md`](docs/reliability/why-electromigration-made-wires-a-lifetime-limit.md)
- [`docs/reliability/why-solder-joints-and-delamination-became-system-failures.md`](docs/reliability/why-solder-joints-and-delamination-became-system-failures.md)

Reliability history restores time to a device that a schematic draws as timeless: metal migrates, solder creeps and fatigues, interfaces delaminate, and screening itself can consume lifetime.

## Packaging and board assembly

- [`docs/packaging/why-a-chip-needs-a-package.md`](docs/packaging/why-a-chip-needs-a-package.md)
- [`docs/packaging/why-wire-bonds-failed-in-strange-colors.md`](docs/packaging/why-wire-bonds-failed-in-strange-colors.md)
- [`docs/packaging/why-flip-chip-shortened-the-interconnect.md`](docs/packaging/why-flip-chip-shortened-the-interconnect.md)
- [`docs/packaging/why-advanced-packaging-became-architecture.md`](docs/packaging/why-advanced-packaging-became-architecture.md)
- [`docs/pcb/why-printed-wiring-replaced-hand-wiring.md`](docs/pcb/why-printed-wiring-replaced-hand-wiring.md)
- [`docs/pcb/why-the-board-became-a-system-layer.md`](docs/pcb/why-the-board-became-a-system-layer.md)
- [`docs/pcb/why-surface-mount-changed-the-board-factory.md`](docs/pcb/why-surface-mount-changed-the-board-factory.md)
- [`docs/pcb/why-inspection-became-machine-vision-and-electrical-test.md`](docs/pcb/why-inspection-became-machine-vision-and-electrical-test.md)

## Source maps

- [`docs/references/manufacturing-substrate-field-set.md`](docs/references/manufacturing-substrate-field-set.md)
- [`docs/references/manufacturing-substrate-2-field-set.md`](docs/references/manufacturing-substrate-2-field-set.md)
- [`docs/references/manufacturing-substrate-3-field-set.md`](docs/references/manufacturing-substrate-3-field-set.md)
- [`docs/references/manufacturing-substrate-4-field-set.md`](docs/references/manufacturing-substrate-4-field-set.md)

## Why this deserves its own track

The computer industry depends on other industries that ordinary architecture histories can make invisible:

```text
high-purity semiconductor materials
zone refining / crystal growth / wafer preparation
oxidation / diffusion / epitaxy / implantation
photoresist / mask making / lithography / reticle inspection
etch / deposition / contamination control
SPC / metrology / parametric test / wafer maps
wafer probing / burn-in / automatic test / yield analysis
sealed carriers / FOUP / robotic material handling
SECS-GEM / MES / lot and wafer traceability
GDSII / mask-data preparation / tapeout
wire bonding / flip-chip / interposer / multidie packaging
copper-clad laminates / drilling / plating / multilayer PCB
through-hole / wave solder / SMT / paste / reflow
AOI / ICT / X-ray / failure analysis / rework
semiconductor equipment suppliers
EDA / design rules / PDK-like interfaces
foundries / fabless design interfaces
```

These are not peripheral production details. They determine what architectures can be manufactured reliably, revised quickly, tested economically, connected densely, traced after failure, and sold cheaply enough to matter.

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

Fourth field set:

- [`experiments/process-control-loop/`](experiments/process-control-loop/)
- [`experiments/screening-tradeoff/`](experiments/screening-tradeoff/)
- [`experiments/electromigration-stress/`](experiments/electromigration-stress/)
- [`experiments/thermal-cycle-fatigue/`](experiments/thermal-cycle-fatigue/)
- [`experiments/inspection-tradeoff/`](experiments/inspection-tradeoff/)
- [`experiments/fab-traceability/`](experiments/fab-traceability/)
- [`experiments/layout-hierarchy/`](experiments/layout-hierarchy/)
- [`experiments/multidie-yield/`](experiments/multidie-yield/)

## Next excavations

The track can now go deeper into narrower factory subsystems rather than rebuilding the foundation:

- specific e-beam mask-writer / reticle-inspection tool histories;
- stepper-to-scanner transitions, wavelengths, resists, focus/overlay metrology;
- rapid thermal anneal and implant-damage recovery;
- probe-card technologies, sockets, handlers, and tester programming languages;
- run-to-run/APC and detailed yield-learning organizations;
- ESD/EOS, TDDB, hot-carrier aging, corrosion, moisture, whiskers, and package cracking;
- package substrates, ABF, BGA/PGA/QFP, underfill, TSV, interposers, hybrid bonding, and die-to-die interfaces;
- phenolic laminates, FR-4, microvias, HDI, backplanes, connectors, cables, and power distribution;
- AOI/ICT/X-ray/acoustic inspection equipment lineages and review labor;
- 200→300 mm AMHS, stockers, overhead transport, FOUP repair, and factory recovery procedures;
- SECS/GEM revision history, MES, scheduling, recipe governance, and electronic genealogy;
- GDSII successors, fracture/job-deck history, OPC, mask correction, and data-volume growth;
- semiconductor/PCB labor geography, OSAT, and the equipment/material supply chains below the fab.

> **A billion-transistor processor is not only a triumph of logic design. It is evidence that an enormous manufacturing civilization learned to purify matter, grow crystals, reproduce patterns, measure distributions, screen populations, track material, preserve data lineage, connect packages, and coordinate factories with extraordinary reliability.**
