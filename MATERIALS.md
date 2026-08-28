# Materials and Consumables Are Part of Computing History

A computer does not emerge from silicon alone.

Semiconductor fabs and electronics factories continuously consume, replace, qualify, and discard materials that conventional computing history rarely names:

```text
acids / bases / oxidizers / solvents
photoresist / developer / stripper
CMP slurry / pad / conditioner
quartz / SiC process furniture
PFA / PTFE fluid handling
filter media
MFC valves / wetted paths
package-substrate dielectric film
copper foil / glass cloth / epoxy / solder
```

Some of these materials vanish during manufacture. Others become part of the final package or PCB.

All of them can constrain yield, geometry, lifetime, cost, and which architectures can be manufactured.

## Process chemicals and temporary materials

- [`docs/materials/why-wet-chemistry-had-to-be-electronic-grade.md`](docs/materials/why-wet-chemistry-had-to-be-electronic-grade.md) — why familiar acids and solvents become different industrial products once trace contamination, packaging, delivery, and analytics matter.
- [`docs/materials/why-photoresist-became-a-semiconductor-consumable.md`](docs/materials/why-photoresist-became-a-semiconductor-consumable.md) — how photographic / printing chemistry became the temporary material that carries design information into permanent wafer geometry.
- [`docs/materials/why-cmp-created-a-slurry-and-pad-supply-chain.md`](docs/materials/why-cmp-created-a-slurry-and-pad-supply-chain.md) — why planarization created an industry around slurry chemistry, abrasives, pads, conditioning, filtration, and post-CMP cleaning.

## Process-contact materials

- [`docs/materials/why-quartz-and-silicon-carbide-became-fab-furniture.md`](docs/materials/why-quartz-and-silicon-carbide-became-fab-furniture.md) — why furnace tubes, boats, paddles, liners, and injectors must survive heat without becoming contamination sources.
- [`docs/materials/why-fluoropolymers-became-the-wet-chemistry-pipes.md`](docs/materials/why-fluoropolymers-became-the-wet-chemistry-pipes.md) — why PFA/PTFE fluid paths are judged by extractables, permeability, static behavior, joints, and cleanliness rather than corrosion resistance alone.
- [`docs/materials/why-filters-became-consumable-process-parts.md`](docs/materials/why-filters-became-consumable-process-parts.md) — why filters have retention, pressure-drop, loading, outgassing, replacement, and qualification histories.
- [`docs/manufacturing/why-mass-flow-control-made-gas-recipes-repeatable.md`](docs/manufacturing/why-mass-flow-control-made-gas-recipes-repeatable.md) — how sensors, control valves, calibration, and high-purity wetted paths turned gas delivery into a programmable recipe interface.

## Materials that remain inside the computer

- [`docs/packaging/why-abf-became-a-hidden-cpu-material.md`](docs/packaging/why-abf-became-a-hidden-cpu-material.md) — why build-up dielectric film became part of the package interconnect system between dense CPU bumps and board-scale wiring.
- [`docs/pcb/why-a-pcb-is-a-materials-stack.md`](docs/pcb/why-a-pcb-is-a-materials-stack.md) — why copper foil, woven glass, epoxy resin, prepreg, plating, solder mask, finishes, and solder form a coupled mechanical/electrical materials stack.

## Runnable experiments

- [`experiments/wet-chem-purity/`](experiments/wet-chem-purity/) — multi-channel chemical contamination budget.
- [`experiments/resist-window/`](experiments/resist-window/) — synthetic exposure/development process window.
- [`experiments/cmp-planarity/`](experiments/cmp-planarity/) — topography and density-sensitive planarization proxy.
- [`experiments/furnace-material-budget/`](experiments/furnace-material-budget/) — bulk impurity × surface × outgassing × cycle history.
- [`experiments/tubing-extractables/`](experiments/tubing-extractables/) — cumulative point-of-use contamination along a fluid path.
- [`experiments/filter-tradeoff/`](experiments/filter-tradeoff/) — capture / pressure-drop / loading tradeoff.
- [`experiments/flow-control-error/`](experiments/flow-control-error/) — commanded versus delivered synthetic gas dose.
- [`experiments/build-up-stack/`](experiments/build-up-stack/) — routing opportunity versus accumulated build-up layer burden.
- [`experiments/pcb-material-stack/`](experiments/pcb-material-stack/) — synthetic thermal mismatch inside a board-material stack.

All experiment parameters are explicitly synthetic unless stated otherwise. None is a process recipe, materials specification, safety calculation, or commercial product model.

## Source map and acknowledgements

- [`docs/references/materials-and-consumables-field-set.md`](docs/references/materials-and-consumables-field-set.md)
- [`docs/manufacturing/ACKNOWLEDGEMENTS-FIELD-SET-6.md`](docs/manufacturing/ACKNOWLEDGEMENTS-FIELD-SET-6.md)

## The recurring pattern

The materials layer keeps producing the same historical surprise:

```text
bulk chemical purity
    is not point-of-use purity

bulk material composition
    is not surface cleanliness

nominal filter pore size
    is not zero-cost perfect retention

recipe setpoint
    is not delivered gas

package dielectric
    is not merely insulation

PCB substrate
    is not merely a mechanical board
```

The final computer hides the state of the materials that made it possible.

A wafer remembers a photoresist film that no longer exists.
A polished layer remembers slurry and pad wear that were discarded.
A diffusion step remembers the cleanliness of a quartz tube later replaced.
A wet process remembers every meter of tubing and every filter it passed through.
A processor package permanently retains its dielectric film.
A motherboard retains its glass, resin, copper, and solder for its entire life.

## Next excavations

This track should continue into:

- electronic-grade HF/HCl/H2SO4/H2O2 production and container supply chains;
- RCA-clean lineage and semiconductor chemical analytics;
- KPR / Shipley / positive-resist / chemically amplified resist histories;
- photoresist filtration, bottle cleanliness, solvent and developer industries;
- CMP pad and slurry supplier histories, conditioner diamonds, post-CMP cleaners;
- high-purity quartz raw material, synthetic silica, SiC coatings and chamber parts;
- PFA valve / fitting / beadless-weld and SEMI F57 history;
- HEPA/ULPA media, gas/liquid membrane filters, depth filtration and filter integrity tests;
- Tylan / UNIT / Brooks / MKS MFC manuals and valve/seal histories;
- ABF / BT resin / package-substrate vendor and laser-microvia histories;
- NEMA laminate standards, FR-4 formulation evolution, copper foil, glass weave, prepreg, solder mask and surface finishes;
- tin-lead solder infrastructure, lead-free conversion, flux and solder-paste supply chains;
- supplier quality, certificates of analysis, incoming inspection and change qualification.

> **Computing scales when materials that seem ordinary become repeatable enough to disappear into the process.**
