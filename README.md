# computing-archaeology

> **Computers are not inevitable. They are accumulated engineering decisions.**

`computing-archaeology` is an experimental history of computing: a repository for reconstructing **why computers became what they are** through material constraints, forgotten technologies, institutional choices, failed designs, labor, maintenance, standards, compatibility, and small runnable experiments.

A normal timeline asks:

> What was invented, by whom, and when?

This repository asks:

> What could engineers actually build at the time?  
> Which constraints made one design reasonable and another absurd?  
> Which physical formats became software interfaces?  
> Which successful technologies became so ordinary that their machinery and labor disappeared from memory?  
> Which old decisions survive today as compatibility, infrastructure, or manufacturing practice?

The goal is not to replace conventional computer history. It is to put **engineering pressure back into history**.

## Read the repository in layers

The repository is now large enough that this README is intentionally a map, not a complete table of contents.

- [`INDEX.md`](INDEX.md) — **current repository map**: where each major research track lives.
- [`AUDIT.md`](AUDIT.md) — **current coverage audit**: what is still genuinely missing versus what merely needs deeper sources.
- [`ROADMAP.md`](ROADMAP.md) — the original problem-oriented excavation plan.
- [`MANUFACTURING-COMPLETION.md`](MANUFACTURING-COMPLETION.md) — manufacturing/material/reliability completion map.

### Historical computing foundations

Start with:

- [`docs/mechanical/`](docs/mechanical/) — mechanical arithmetic and carry;
- [`docs/electromechanical/`](docs/electromechanical/) — relays and switching;
- [`docs/electronic/`](docs/electronic/) — vacuum-tube electronics;
- [`docs/memory/`](docs/memory/) — delay lines, CRT memory, drums, core, tape, disk and later memory infrastructure;
- [`docs/interaction/`](docs/interaction/) — punched media, batch, teletypes, bootstraps and terminals;
- [`case-studies/`](case-studies/) — ENIAC, CTSS, Multics and other machine/system transitions;
- [`docs/architecture/`](docs/architecture/) — words, bytes, buses, microprocessor economics and package-level architecture;
- [`docs/standards/`](docs/standards/) — compatibility fossils.

### Manufacturing civilization

The project now treats manufacturing as part of computer architecture rather than backstage trivia.

- [`MANUFACTURING.md`](MANUFACTURING.md) — semiconductor manufacturing, fab automation, test and facility infrastructure.
- [`MATERIALS.md`](MATERIALS.md) — process chemicals, photoresist, CMP, thin-film sources, hidden metals, polymers, PCB/package materials and thermal interfaces.
- [`docs/semiconductor/`](docs/semiconductor/) — silicon platform, wafer/process evolution and advanced transistor geometry.
- [`docs/facilities/`](docs/facilities/) — UPW, clean air, gases, vacuum, vibration, ESD and abatement.
- [`docs/packaging/`](docs/packaging/) — packages, wire bonds, flip-chip, underfill, interposers and hybrid bonding.
- [`docs/pcb/`](docs/pcb/) — printed wiring, material stacks, microvias, electrochemistry and high-speed board constraints.
- [`docs/reliability/`](docs/reliability/) — wear-out mechanisms that restore time to apparently static schematics.

### Post-scaling systems

When planar shrinking stopped carrying the whole performance burden, formerly external infrastructure became architecture.

- [`POST-SCALING.md`](POST-SCALING.md) — FinFET/GAA, EUV/High-NA, HBM, interposers, hybrid bonding, chiplets, PAM4/FEC, retimers, rack power and liquid cooling.
- [`SPEED.md`](SPEED.md) — EUV stochastic yield, backside power, CFET, HBM4, CPO, 224G/448G channels, 800 VDC, coolant chemistry and in-network collective offload.

## The method

Every substantial article must distinguish three layers:

1. **Historical record** — what surviving documents, machines, patents, manuals, oral histories, standards, archives and scholarship establish.
2. **Engineering reconstruction** — what follows when reasoning from period components, costs, speeds, manufacturing limits, interfaces and operational needs.
3. **Experiment** — a simulation, replica, program, paper exercise or physical demonstration that exposes one constraint.

These layers must not be silently mixed. A plausible reconstruction is not automatically a historical fact, and a modern experiment does not prove historical intent.

See [`docs/methodology/constraint-first-history.md`](docs/methodology/constraint-first-history.md) and [`AGENTS.md`](AGENTS.md).

## Runnable archaeology

The repository currently contains **123 runnable synthetic constraint experiments**.

They are intentionally small and usually dependency-free. The point is not to cosmetically imitate old machinery; it is to make a historical constraint visible:

```text
mechanical carry
    -> propagation and load

rotating memory
    -> waiting becomes address geometry

slow terminals
    -> bandwidth becomes user-interface design

die area
    -> yield becomes product economics

lithography / process stack
    -> small per-step errors accumulate

package / PCB / connectors
    -> hidden interfaces become reliability limits

HBM / chiplets / retimers
    -> distance becomes architecture

rack power / liquid cooling
    -> the building starts participating in computation
```

All experiment parameters are synthetic unless explicitly tied to historical evidence. They are not process recipes, qualification methods, compliance tools, safety calculations, or commercial performance forecasts.

Implementations live under [`experiments/`](experiments/). CI checks internal Markdown links, compiles experiment sources, and runs the experiment suites.

## Six recurring patterns

### 1. The physical world leaks upward

A clean abstraction usually exists because lower layers are working hard to hide torque, rebound, propagation delay, contamination, heat, geometry, resistance, capacitance, vibration, chemical drift or statistical defects.

### 2. The medium shapes the algorithm

Cards encourage sorting and streaming; tape encourages blocking and merge workflows; drums reward timing-aware placement; disk creates seek locality; HBM and chiplets reward moving data less distance.

### 3. Compatibility outlives the original machine

80-column cards, CR/LF, byte order, VT100 behavior and old bus conventions can stop being physical constraints and become economic ones because software, data and installed systems expect them.

### 4. Computing becomes infrastructure when interfaces stabilize

A stable bus, terminal protocol, design rule, package interface or chiplet link lets work proceed independently on both sides of the boundary.

### 5. Successful technology disappears into the background

The more reliable something becomes, the less history notices it. Core weavers, ATE operators, mask-data preparation, UPW technicians, PCB process workers, connector plating, pump service and coolant maintenance are therefore part of computing history.

### 6. Speed moves the bottleneck outward

Once transistor switching improves, memory, interconnect, power, cooling, lithography statistics, package distance, rack distribution or network collectives become the next wait to eliminate.

## Current priority: repair the missing middle

The repository is now exceptionally deep in semiconductor manufacturing and modern accelerator infrastructure, but several central historical bridges remain thin.

The highest-priority missing first treatments are summarized in [`AUDIT.md`](AUDIT.md):

1. **etch / plasma / RIE, epitaxy, anneal and process metrology**;
2. **SRAM / DRAM / ROM / EEPROM / Flash / cache**;
3. **ordinary computer power supplies, VRMs, passives and clock distribution**;
4. **mainframe channels, spooling, RS-232/UART/modems and disk geometry**;
5. **the S-100 -> IBM PC/ISA/BIOS compatibility stack**;
6. **packet switching -> Ethernet -> TCP/IP -> routing/DNS/NIC evolution**.

Future work should prefer coherent field sets that close these dependency chains rather than adding isolated modern curiosities.

## Source and labor policy

Source priority is documented in [`AGENTS.md`](AGENTS.md). In general:

1. primary technical documents;
2. archives and museums;
3. scholarly work;
4. institutional/oral histories;
5. technical retrospectives;
6. tertiary sources for navigation.

Corporate histories are useful but must be labeled as such. Later standards must not be projected backward as if early implementations already followed their mature wording.

The project also treats operators, assemblers, test technicians, process engineers, field service, maintenance crews, documentation teams, factory workers and preservation communities as part of the technical record.

See [`ACKNOWLEDGEMENTS.md`](ACKNOWLEDGEMENTS.md) and the field-set acknowledgements under [`docs/manufacturing/`](docs/manufacturing/).

## Related repositories

This repository explains **why a historical design made sense**. Hands-on reconstruction or interface emulation may live in companion projects instead:

- `mechanical-computing-playground` — build or simulate mechanisms;
- `obsolete-interface-museum` — experience obsolete interaction styles.

## License and assistance disclosure

See [`LICENSE`](LICENSE) for repository licensing.

Research framing, source triage, drafting, synthetic experiment design, navigation and repository integration include AI assistance. AI-generated historical claims are not exempt from the repository's source-verification rules.

Current AI assistance is transparently credited to **ChatGPT (GPT-5.6 Sol), OpenAI**.

> **A modern computer is not one invention. It is an enormous pile of once-visible engineering decisions that became reliable enough to disappear.**
