# Current Repository Index

`computing-archaeology` has grown beyond a single linear README. This file is the current map of the repository's major research tracks.

For project method, start with [`README.md`](README.md) and [`docs/methodology/constraint-first-history.md`](docs/methodology/constraint-first-history.md).

For what is still missing, use [`AUDIT.md`](AUDIT.md).

## Historical foundations

### Mechanical computation

- difference engines and finite differences;
- mechanical carry propagation and radix;
- future deepening: stepped reckoners, comptometers, Curta, tolerances and wear.

Start in [`docs/mechanical/`](docs/mechanical/).

### Relay and vacuum-tube computation

- telephone-relay inheritance;
- contact bounce and imperfect switching;
- vacuum-tube speed, reliability and maintenance;
- ENIAC wiring -> coded control.

Start in [`docs/electromechanical/`](docs/electromechanical/), [`docs/electronic/`](docs/electronic/), and [`case-studies/eniac/`](case-studies/eniac/).

### Memory and storage: from physical circulation to semiconductor hierarchy

- acoustic delay lines;
- Williams tubes;
- magnetic drums;
- magnetic core;
- tape locality;
- RAMAC/direct-access disk.

Start in [`docs/memory/`](docs/memory/).

### Punched media, batch and interactive computing

- cards and fixed-width records;
- physical sort/merge;
- batch economics;
- teletypes;
- CTSS;
- Multics;
- VT100 compatibility.

Start in [`docs/interaction/`](docs/interaction/) and [`case-studies/`](case-studies/).

### Architecture and compatibility fossils

- word lengths;
- eight-bit byte;
- endianness;
- UNIBUS;
- low-cost 6502 economics;
- ASCII/EBCDIC/device control fossils.

Start in [`docs/architecture/`](docs/architecture/) and [`docs/standards/`](docs/standards/).

## Manufacturing civilization

### Semiconductor manufacturing

[`MANUFACTURING.md`](MANUFACTURING.md) is the main entrance.

It covers first-pass work on:

- silicon purity, crystal growth and wafer scaling;
- planar processing;
- mask making and lithography equipment;
- ion implantation;
- MOS manufacturability;
- yield economics;
- process control / ATE / probe / burn-in;
- fab automation, design rules, tapeout and foundry boundaries;
- facility infrastructure: UPW, clean air, gases, vacuum, thermal/vibration stability, ESD, exhaust and abatement.

The current completion status is tracked in [`MANUFACTURING-COMPLETION.md`](MANUFACTURING-COMPLETION.md).

### Materials and consumables

[`MATERIALS.md`](MATERIALS.md) covers:

- electronic-grade wet chemistry;
- photoresist and chemically amplified resist;
- CMP slurry/pads/conditioning;
- quartz, SiC and fluoropolymer process parts;
- filters and mass-flow control;
- sputter targets and CVD/ALD precursors;
- tungsten, barriers, copper plating/CMP, low-k/high-k;
- ABF and PCB material stacks;
- underfill, solder paste and TIM/lid interfaces.

### Packaging, reliability, PCB and physical interfaces

See:

- [`docs/packaging/`](docs/packaging/)
- [`docs/reliability/`](docs/reliability/)
- [`docs/pcb/`](docs/pcb/)
- [`docs/interconnect/`](docs/interconnect/)
- [`docs/thermal/`](docs/thermal/)

Coverage includes wire bonding, flip-chip, multidie packaging, hybrid bonding, moisture/popcorn cracking, electromigration, TDDB, BTI, hot carriers, whiskers, CAF/ECM, connector fretting, LGA sockets, high-speed PCB roughness/weave, via stubs, TIM aging and heat pipes.

## Post-scaling and speed infrastructure

### Post-scaling integration

[`POST-SCALING.md`](POST-SCALING.md) connects:

- FinFET;
- GAA nanosheets;
- EUV and High-NA;
- HBM/TSV;
- silicon interposers;
- hybrid bonding;
- chiplets/UCIe;
- PAM4/FEC;
- retimers;
- rack power;
- cold-plate liquid cooling.

### Speed infrastructure

[`SPEED.md`](SPEED.md) follows performance pressure into:

- EUV stochastic yield;
- backside power;
- forksheet/CFET;
- HBM4;
- hybrid-bond KGD economics;
- CPO;
- 224G/448G channels;
- 800 VDC rack distribution;
- coolant chemistry;
- in-network collective offload.

## Experiments

The repository currently contains **125 runnable synthetic constraint experiments** across three CI suites.

Do not treat experiment values as historical measurements unless a specific experiment explicitly says otherwise. Their purpose is to expose mechanism and tradeoff structure.

Experiment implementations live under [`experiments/`](experiments/).

## Research maps

- [`docs/references/source-ledger.md`](docs/references/source-ledger.md) — original source ledger.
- [`docs/references/`](docs/references/) — field-set source maps and source-type caveats.
- [`ACKNOWLEDGEMENTS.md`](ACKNOWLEDGEMENTS.md) — project-wide preservation acknowledgements.
- [`docs/manufacturing/`](docs/manufacturing/) — field-set acknowledgements for manufacturing labor and infrastructure.

## Planning documents

- [`ROADMAP.md`](ROADMAP.md) — historical problem-oriented roadmap.
- [`AUDIT.md`](AUDIT.md) — current gap analysis and priority repair program.
- [`MANUFACTURING-COMPLETION.md`](MANUFACTURING-COMPLETION.md) — manufacturing/material/reliability completion map.

## The present priority

The repository is now exceptionally deep in manufacturing, but uneven across the rest of computing history.

The highest-priority missing bridges are:

1. semiconductor etch / epitaxy / anneal / metrology;
2. deeper period sourcing for SRAM cell design, FPM/EDO transitions and Flash controller history;
3. ordinary computer power supplies, VRMs and timing/clock distribution;
4. mainframe I/O, spooling, serial interfaces and disk geometry;
5. the commodity-PC compatibility stack;
6. packet switching, Ethernet, TCP/IP, routing, DNS and NIC evolution.

See [`AUDIT.md`](AUDIT.md) before starting another new field set.

> **The project should now optimize for continuity: preserve the middle layers that make the spectacular endpoints understandable.**
