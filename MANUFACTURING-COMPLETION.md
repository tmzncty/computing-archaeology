# Manufacturing Completion Map

This file exists so the manufacturing/materials/reliability track no longer depends on chat memory or repeated reminders.

The track's thesis is:

> **A fingernail-sized computer chip is the visible endpoint of a manufacturing civilization that controls matter, geometry, contamination, stress, data lineage, interfaces, and lifetime from raw material to household use.**

## Scope boundary

This completion map covers the current **manufacturing → materials → package/PCB → household reliability** mainline.

It does **not** mean every archival source, vendor manual, factory oral history, regional labor history, or later process generation has been exhausted. Those are continuing source-deepening tasks.

It does mean that the conceptual gaps repeatedly identified in this research thread now have first treatments and runnable constraint experiments.

## Completed foundation

- [x] semiconductor purity / crystal growth / wafer scaling
- [x] planar process / oxidation / diffusion / lithography
- [x] mask making / overlay / step-and-repeat
- [x] MOS manufacturability / silicon gate / EPROM iteration
- [x] yield economics / die size / foundry-fabless boundary
- [x] implant / ATE / process control / probe / burn-in
- [x] GDSII / tapeout / design rules / manufacturing data
- [x] SMIF / FOUP / MES / traceability
- [x] UPW / clean air / specialty gas / clean vacuum
- [x] temperature / vibration / ESD / exhaust / abatement
- [x] wet chemistry / photoresist / CMP / quartz / SiC / PFA
- [x] filters / MFC / ABF / PCB materials
- [x] sputter targets / CVD-ALD precursors / chemically amplified resist
- [x] copper barrier-seed-plating-CMP integration
- [x] ESC / chamber seals / pad conditioning
- [x] PCB surface finishes / microvia fill
- [x] WF6 tungsten / hidden barriers / low-k-high-k split
- [x] backside helium / dry vacuum train
- [x] microvia desmear / electroless seed
- [x] solder paste / underfill / TIM / lid

## Completion tranche: device aging

- [x] **TDDB** — dielectric lifetime is statistical and stress-dependent.
  - Article: [`docs/reliability/why-tddb-made-dielectrics-have-lifetimes.md`](docs/reliability/why-tddb-made-dielectrics-have-lifetimes.md)
  - Experiment: [`experiments/dielectric-breakdown-stress/`](experiments/dielectric-breakdown-stress/)
- [x] **Hot-carrier aging** — switching history and local high fields accumulate device damage.
  - Article: [`docs/reliability/why-hot-carrier-aging-made-switching-history-matter.md`](docs/reliability/why-hot-carrier-aging-made-switching-history-matter.md)
  - Experiment: [`experiments/hot-carrier-duty/`](experiments/hot-carrier-duty/)
- [x] **BTI** — even state residency / sustained bias can become a lifetime variable.
  - Article: [`docs/reliability/why-bti-made-bias-a-lifetime-variable.md`](docs/reliability/why-bti-made-bias-a-lifetime-variable.md)
  - Experiment: [`experiments/bti-duty-cycle/`](experiments/bti-duty-cycle/)

## Completion tranche: packaging, radiation, moisture, solder

- [x] **Alpha-particle soft errors** — package radioactivity can become a logical bit error.
  - Article: [`docs/memory/why-alpha-particles-made-packaging-a-memory-problem.md`](docs/memory/why-alpha-particles-made-packaging-a-memory-problem.md)
  - Experiment: [`experiments/alpha-soft-error/`](experiments/alpha-soft-error/)
- [x] **Moisture / popcorn cracking** — storage history becomes package state.
  - Article: [`docs/packaging/why-moisture-made-plastic-packages-popcorn.md`](docs/packaging/why-moisture-made-plastic-packages-popcorn.md)
  - Experiment: [`experiments/moisture-reflow/`](experiments/moisture-reflow/)
- [x] **Lead-free solder transition** — regulation changes alloy, reflow, package stress, and reliability models together.
  - Article: [`docs/reliability/why-lead-free-solder-rewrote-assembly-reliability.md`](docs/reliability/why-lead-free-solder-rewrote-assembly-reliability.md)
  - Experiment: [`experiments/lead-free-fatigue/`](experiments/lead-free-fatigue/)
- [x] **Tin whiskers** — a finish can grow a new conductor years after assembly.
  - Article: [`docs/reliability/why-tin-whiskers-made-metal-finishes-grow-wires.md`](docs/reliability/why-tin-whiskers-made-metal-finishes-grow-wires.md)
  - Experiment: [`experiments/whisker-bridge/`](experiments/whisker-bridge/)

## Completion tranche: PCB electrochemistry

- [x] **CAF** — the laminate interior can become an electrochemical conduction path.
  - Article: [`docs/pcb/why-caf-made-laminate-a-reliability-path.md`](docs/pcb/why-caf-made-laminate-a-reliability-path.md)
  - Experiment: [`experiments/caf-path/`](experiments/caf-path/)
- [x] **Surface electrochemical migration** — ionic residue + moisture + bias can grow dendrites.
  - Article: [`docs/pcb/why-ionic-residues-can-grow-dendrites.md`](docs/pcb/why-ionic-residues-can-grow-dendrites.md)
  - Experiment: [`experiments/ecm-dendrite/`](experiments/ecm-dendrite/)

## Completion tranche: separable electrical interfaces

- [x] **Connector plating / wipe / fretting** — a connector is an electrical tribology system.
  - Article: [`docs/interconnect/why-separable-contacts-need-plating-force-and-wipe.md`](docs/interconnect/why-separable-contacts-need-plating-force-and-wipe.md)
  - Experiment: [`experiments/contact-fretting/`](experiments/contact-fretting/)
- [x] **LGA CPU sockets** — hundreds or thousands of spring contacts become one precision interface.
  - Article: [`docs/interconnect/why-lga-sockets-became-precision-spring-machines.md`](docs/interconnect/why-lga-sockets-became-precision-spring-machines.md)
  - Experiment: [`experiments/lga-contact-array/`](experiments/lga-contact-array/)

## Completion tranche: cooling lifetime

- [x] **TIM aging** — pump-out and dry-out make thermal resistance a lifetime variable.
  - Article: [`docs/reliability/why-tim-aging-made-cooling-a-lifetime-problem.md`](docs/reliability/why-tim-aging-made-cooling-a-lifetime-problem.md)
  - Experiment: [`experiments/tim-aging/`](experiments/tim-aging/)
- [x] **Heat pipes / vapor chambers** — passive two-phase machines move and spread heat in consumer systems.
  - Article: [`docs/thermal/why-heat-pipes-moved-heat-without-a-pump.md`](docs/thermal/why-heat-pipes-moved-heat-without-a-pump.md)
  - Experiment: [`experiments/heatpipe-capillary/`](experiments/heatpipe-capillary/)

## Completion tranche: high-speed board physics

- [x] **Copper roughness + glass weave** — PCB microstructure becomes loss and picosecond skew.
  - Article: [`docs/pcb/why-copper-roughness-and-glass-weave-became-signal-integrity.md`](docs/pcb/why-copper-roughness-and-glass-weave-became-signal-integrity.md)
  - Experiment: [`experiments/weave-roughness/`](experiments/weave-roughness/)
- [x] **Via stubs / backdrilling** — unused copper becomes a resonator and is physically drilled away.
  - Article: [`docs/pcb/why-via-stubs-had-to-be-drilled-away.md`](docs/pcb/why-via-stubs-had-to-be-drilled-away.md)
  - Experiment: [`experiments/via-stub-resonance/`](experiments/via-stub-resonance/)

## Completed later-generation extension: post-scaling integration

The first later-generation extension is covered in [`POST-SCALING.md`](POST-SCALING.md):

- [x] FinFET process-integration archaeology;
- [x] gate-all-around nanosheet scaling;
- [x] EUV source / mirror / vacuum infrastructure;
- [x] High-NA EUV as a new optical/mechanical scaling step;
- [x] HBM / TSV stacked-memory architecture;
- [x] silicon interposer / CoWoS-style package-scale wiring;
- [x] hybrid bonding / fine-pitch 3D integration;
- [x] modern chiplet die-to-die standardization through UCIe;
- [x] PCIe 6 PAM4 / FEC / FLIT reliability machinery;
- [x] active retimers as channel infrastructure;
- [x] 48 V busbar / high-current AI-rack power distribution;
- [x] cold plates / manifolds / quick disconnects in liquid-cooled servers.

## Completed later-generation extension: speed infrastructure

The second later-generation extension is covered in [`SPEED.md`](SPEED.md):

- [x] EUV stochastic-defect / dose / pellicle throughput tradeoffs;
- [x] backside power-delivery networks;
- [x] forksheet / CFET density scaling;
- [x] HBM4-class 2048-bit memory interfaces and base-die pressure;
- [x] hybrid-bond known-good-die / inspection economics;
- [x] co-packaged optics and external laser source infrastructure;
- [x] CEI 224G -> 448G channel-system scaling;
- [x] 800 VDC / megawatt-class rack distribution;
- [x] CDU / coolant chemistry as compute-availability infrastructure;
- [x] in-network collective computation / SHARP-style offload.

The repository now contains **123 runnable synthetic constraint experiments** across the original suite, post-scaling extension, and speed-infrastructure extension.

## What remains after these completion passes

The remaining work is no longer a missing conceptual spine. It is **archival and specialist deepening**, plus genuinely newer extensions.

### Primary-source deepening

- recover more original factory manuals, process specifications, vendor data books, qualification procedures, conference proceedings, and standard revisions;
- replace later institutional summaries with period documents where accessible;
- preserve exact revision dates for standards and distinguish first appearance from later mature practice;
- add more cross-company evidence before making priority claims.

### Labor and organization

- semiconductor / PCB / OSAT labor geography;
- supplier quality, incoming inspection, field service, maintenance and spare-parts logistics;
- women and migrant labor in assembly, test, packaging, cleanroom and board factories;
- equipment-vendor/customer co-development and process-transfer teams;
- EUV field service, HBM/package yield, retimer/CPO validation, rack-power commissioning, coolant-chemistry monitoring, and liquid-cooling maintenance labor.

### Newer extensions that remain open

- EUV stochastic modeling at higher resolution, mask-defect inspection, actinic metrology, and next-generation pellicle materials;
- GAA inner-spacer / sheet-release / work-function-fill process archaeology, plus CFET thermal/contact integration;
- HBM4E/HBM5-class stack evolution, base-die logic, repair, redundancy, and package-yield economics;
- hybrid-bond defect inspection, repair/rework limits, and die-to-wafer automation history;
- co-packaged optics deployment history, optical-engine serviceability, and co-packaged laser/ELSFP fleet operations;
- 224G/448G cable assemblies, connector/material evolution, compliance instrumentation, and eventual 800G-class lane research;
- 800 VDC protection, conversion stages, fault management, commissioning, and facility integration;
- CDU fleet control, facility-water quality, corrosion monitoring, leak detection, and coolant lifecycle management;
- cross-vendor in-network collective history and AI-fabric scheduling/control-plane archaeology;
- contemporary AI infrastructure supply-chain geography and capacity bottlenecks.

## Completion criterion

The manufacturing track is considered **first-pass structurally complete** when:

- each tracked topic has a long-form article;
- each tracked topic has a runnable synthetic constraint experiment where appropriate;
- internal links pass;
- all Python experiment entry points compile;
- source-type caveats and invisible labor are preserved.

> **The goal is not to claim that manufacturing history is finished. The goal is to make sure nobody can look at a CPU, GPU, HBM stack, optical engine, AI fabric, rack busbar, or coolant manifold and imagine that “performance” came from transistor design alone.**
