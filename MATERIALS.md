# Materials and Consumables Are Part of Computing History

A computer does not emerge from silicon alone.

Semiconductor fabs and electronics factories continuously consume, replace, qualify, erode, plate, polish, and discard materials that conventional computing history rarely names.

Some vanish during manufacture. Some are worn out as process parts. Others remain permanently inside the package or PCB.

All of them can constrain yield, geometry, lifetime, cost, and which architectures can be manufactured.

## Process chemicals and temporary materials

- [`docs/materials/why-wet-chemistry-had-to-be-electronic-grade.md`](docs/materials/why-wet-chemistry-had-to-be-electronic-grade.md) — electronic-grade wet chemistry, trace contamination, packaging, delivery, and analytics.
- [`docs/materials/why-photoresist-became-a-semiconductor-consumable.md`](docs/materials/why-photoresist-became-a-semiconductor-consumable.md) — photoresist as temporary information-carrying material.
- [`docs/materials/why-chemically-amplified-resist-made-one-photon-do-more.md`](docs/materials/why-chemically-amplified-resist-made-one-photon-do-more.md) — photoacid catalysis, DUV sensitivity, blur, and airborne molecular contamination.
- [`docs/materials/why-cmp-created-a-slurry-and-pad-supply-chain.md`](docs/materials/why-cmp-created-a-slurry-and-pad-supply-chain.md) — slurry, pads, conditioning, filtration, and post-CMP cleaning.
- [`docs/materials/why-cmp-pad-conditioning-became-a-process-within-the-process.md`](docs/materials/why-cmp-pad-conditioning-became-a-process-within-the-process.md) — why the polishing consumable itself requires a controlled renewal process.

## Thin-film source materials and deposition chemistry

- [`docs/materials/why-sputter-targets-became-consumable-thin-film-sources.md`](docs/materials/why-sputter-targets-became-consumable-thin-film-sources.md) — target purity, erosion, backing, cooling, cross-contamination, and end-of-life.
- [`docs/materials/why-cvd-and-ald-precursors-became-chemical-source-code.md`](docs/materials/why-cvd-and-ald-precursors-became-chemical-source-code.md) — gas-phase chemistry, precursor delivery, self-limiting cycles, purge, and vanished molecular inputs.
- [`docs/materials/why-copper-needed-barrier-seed-plating-and-cmp.md`](docs/materials/why-copper-needed-barrier-seed-plating-and-cmp.md) — why copper interconnect required liner/barrier, seed, electroplating additives, damascene, CMP, and reliability integration.

## Process-contact materials and replaceable parts

- [`docs/materials/why-quartz-and-silicon-carbide-became-fab-furniture.md`](docs/materials/why-quartz-and-silicon-carbide-became-fab-furniture.md) — furnace tubes, boats, paddles, liners, and injectors.
- [`docs/materials/why-fluoropolymers-became-the-wet-chemistry-pipes.md`](docs/materials/why-fluoropolymers-became-the-wet-chemistry-pipes.md) — PFA/PTFE extractables, permeability, static behavior, joints, and cleanliness.
- [`docs/materials/why-filters-became-consumable-process-parts.md`](docs/materials/why-filters-became-consumable-process-parts.md) — retention, pressure drop, loading, outgassing, replacement, and qualification.
- [`docs/manufacturing/why-mass-flow-control-made-gas-recipes-repeatable.md`](docs/manufacturing/why-mass-flow-control-made-gas-recipes-repeatable.md) — sensors, valves, calibration, and programmable gas delivery.
- [`docs/manufacturing/why-electrostatic-chucks-became-thermal-process-parts.md`](docs/manufacturing/why-electrostatic-chucks-became-thermal-process-parts.md) — wafer holding, ceramic stages, thermal uniformity, and process-part aging.
- [`docs/materials/why-vacuum-seals-became-contamination-parts.md`](docs/materials/why-vacuum-seals-became-contamination-parts.md) — leaks, permeation, outgassing, plasma attack, particles, and replacement history.

## Materials that remain inside the computer

- [`docs/packaging/why-abf-became-a-hidden-cpu-material.md`](docs/packaging/why-abf-became-a-hidden-cpu-material.md) — package build-up dielectric as interconnect architecture.
- [`docs/pcb/why-a-pcb-is-a-materials-stack.md`](docs/pcb/why-a-pcb-is-a-materials-stack.md) — copper foil, woven glass, epoxy, prepreg, plating, solder mask, finishes, and solder.
- [`docs/pcb/why-surface-finishes-became-electrical-and-chemical-interfaces.md`](docs/pcb/why-surface-finishes-became-electrical-and-chemical-interfaces.md) — OSP/ENIG/etc. as storage, soldering, bondability, and electrical interfaces.
- [`docs/pcb/why-microvia-filling-became-electrochemistry.md`](docs/pcb/why-microvia-filling-became-electrochemistry.md) — why HDI vertical interconnect became a copper-filling chemistry problem.

## Runnable experiments

Earlier materials field set:

- [`experiments/wet-chem-purity/`](experiments/wet-chem-purity/)
- [`experiments/resist-window/`](experiments/resist-window/)
- [`experiments/cmp-planarity/`](experiments/cmp-planarity/)
- [`experiments/furnace-material-budget/`](experiments/furnace-material-budget/)
- [`experiments/tubing-extractables/`](experiments/tubing-extractables/)
- [`experiments/filter-tradeoff/`](experiments/filter-tradeoff/)
- [`experiments/flow-control-error/`](experiments/flow-control-error/)
- [`experiments/build-up-stack/`](experiments/build-up-stack/)
- [`experiments/pcb-material-stack/`](experiments/pcb-material-stack/)

Deposition and interconnect field set:

- [`experiments/target-utilization/`](experiments/target-utilization/) — local erosion versus remaining target mass.
- [`experiments/precursor-cycle-window/`](experiments/precursor-cycle-window/) — surface saturation versus purge completeness.
- [`experiments/photoacid-amplification/`](experiments/photoacid-amplification/) — catalytic gain versus spatial blur.
- [`experiments/copper-superfill/`](experiments/copper-superfill/) — conformal versus bottom-up recessed copper fill.
- [`experiments/wafer-stage-uniformity/`](experiments/wafer-stage-uniformity/) — average stage temperature versus radial wafer spread.
- [`experiments/seal-aging-budget/`](experiments/seal-aging-budget/) — thermal/plasma/motion exposure against maintenance threshold.
- [`experiments/pad-conditioning-window/`](experiments/pad-conditioning-window/) — glazing versus conditioning and pad wear.
- [`experiments/surface-finish-tradeoff/`](experiments/surface-finish-tradeoff/) — synthetic PCB finish multi-objective comparison.
- [`experiments/microvia-fill/`](experiments/microvia-fill/) — conformal versus bottom-biased blind-via filling.

All experiment parameters are explicitly synthetic unless stated otherwise. None is a process recipe, materials specification, safety calculation, or commercial product model.

## Source maps and acknowledgements

- [`docs/references/materials-and-consumables-field-set.md`](docs/references/materials-and-consumables-field-set.md)
- [`docs/references/deposition-and-interconnect-field-set.md`](docs/references/deposition-and-interconnect-field-set.md)
- [`docs/manufacturing/ACKNOWLEDGEMENTS-FIELD-SET-6.md`](docs/manufacturing/ACKNOWLEDGEMENTS-FIELD-SET-6.md)
- [`docs/manufacturing/ACKNOWLEDGEMENTS-FIELD-SET-7.md`](docs/manufacturing/ACKNOWLEDGEMENTS-FIELD-SET-7.md)

## The recurring pattern

The materials layer keeps producing the same historical surprise:

```text
bulk chemical purity
    is not point-of-use purity

source material
    is not deposited film

self-limiting chemistry
    is not self-running chemistry

average target mass
    is not useful target lifetime

wafer support
    is not merely mechanical support

vacuum-tight seal
    is not necessarily a clean seal

copper conductor
    is not merely copper

PCB pad
    is not merely exposed copper
```

A wafer remembers materials that no longer exist.
A film remembers a target that was later recycled.
A patterned layer remembers photoacid chemistry that was washed away.
A copper line remembers plating additives that went down the waste/recovery stream.
A planar surface remembers a pad and conditioner that wore out.
A package and board permanently retain other materials for the machine's entire life.

## Next excavations

This track can now move deeper into:

- sputter-target metallurgy, bonding, recycling, and erosion monitoring;
- evaporation sources and e-beam evaporation;
- semiconductor CVD precursors such as silane/chlorosilanes, TEOS, WF6, and metal-organic sources;
- ALD precursor/reactor history and precursor supply chains;
- PAG / quencher / TMAH developer industries and airborne molecular contamination;
- barrier/liner material transitions including Ti/TiN, Ta/TaN, Ru/Co and scaling constraints;
- copper plating bath analytics, anodes, organic additive control and metal recovery;
- ESC ceramics, backside-gas interfaces, ceramic heaters and refurbishment;
- vacuum elastomer formulation, permeation/outgassing data and load-lock seal history;
- CMP conditioner supplier history and conditioner wear metrology;
- PCB finish chemistry, black-pad history, ENEPIG and high-speed surface behavior;
- microvia laser drilling, desmear, electroless seed and via-fill chemistry.

> **A chip can be the size of a fingernail because an enormous materials civilization learned how to make atoms, molecules, surfaces, interfaces, and expendable process parts behave repeatably.**
