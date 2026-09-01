# Repository Coverage Audit

This is a structural audit of `computing-archaeology` after the manufacturing, materials, post-scaling, and speed-infrastructure expansions.

The repository now has **125 runnable constraint experiments** and unusually deep coverage of manufacturing. The main risk is no longer lack of material everywhere; it is **uneven depth**: some lower manufacturing layers have many articles while several central computing lineages still have no first-pass treatment.

This file separates three things that should not be confused:

1. **structural cleanup** — navigation or roadmaps that no longer describe the repository accurately;
2. **missing conceptual spine** — important historical layers with no defensible first treatment yet;
3. **source deepening** — topics already represented but still deserving better primary evidence or narrower studies.

## 1. Structural findings

### README is now an archaeological layer itself

The root README still presents the repository largely as the early field sets. Its `Start here`, research-infrastructure, and runnable-experiment sections do not adequately expose the later tracks:

- `MANUFACTURING.md`
- `MATERIALS.md`
- `MANUFACTURING-COMPLETION.md`
- `POST-SCALING.md`
- `SPEED.md`

It also describes only the early experiment suite even though the repository now contains 125 runnable experiments.

**Action:** keep the README concise and make it point to a current index rather than trying to enumerate every article and experiment forever.

### ROADMAP is useful but chronologically stale in places

The original milestones remain valuable because many of their `Still deepen` items are genuinely unfinished. But several lines became stale after the manufacturing expansion—for example, generic semiconductor fabrication/yield work is no longer an uncovered topic even though narrower primary-source deepening remains.

**Action:** preserve M0–M11 as the historical roadmap, but add later cross-track milestones and point future agents to this audit before interpreting an unchecked bullet as a blank topic.

### Root navigation should distinguish tracks from inventories

Recommended root roles:

- `README.md` — project thesis + short current map.
- `INDEX.md` — current track-level navigation.
- `ROADMAP.md` — historical milestones and research program.
- `AUDIT.md` — coverage gaps and prioritization.
- `MANUFACTURING-COMPLETION.md` — completion map for manufacturing/material/reliability work.
- `MANUFACTURING.md`, `MATERIALS.md`, `POST-SCALING.md`, `SPEED.md` — thematic track entrances.

## 2. P0 gaps — missing conceptual spine

These are the largest omissions discovered in the audit. They should be filled before adding many more highly specialized modern subtopics.

### P0-A — Semiconductor fabrication is missing the subtractive half

The repository is now strong on purity, oxidation, diffusion/implantation, lithography, deposition, CMP, materials, vacuum, and facilities, but it lacks a first-class history of **etching**.

Missing first treatments:

- wet chemical etching and selectivity;
- plasma etching;
- reactive-ion etching (RIE) and anisotropy;
- endpoint / selectivity / mask erosion;
- high-aspect-ratio etch and why vertical sidewalls became a scaling requirement;
- etch chamber conditioning and plasma damage.

Closely related missing process modules:

- epitaxy;
- dopant activation / furnace anneal / rapid thermal processing;
- wafer slicing, lapping, edge treatment and polishing;
- wafer thinning/backgrinding for packaging;
- critical-dimension / film-thickness / overlay metrology as a historical equipment industry, not only SPC in the abstract.

**Why this is P0:** a modern process flow cannot be explained as `deposit + lithography + CMP` without the repeated act of selectively removing material.

### P0-B — The memory story jumps over semiconductor memory

The repository goes very deep on delay lines, Williams tubes, drums, magnetic core, tape and disk, then later reaches HBM/HBM4. The bridge in the middle is largely missing.

**First treatment completed:**

- [SRAM/DRAM cell tradeoffs, 1T1C sensing/restoration/refresh, address multiplexing, FPM/EDO/SDRAM/DDR and cache hierarchy](docs/memory/why-semiconductor-ram-became-a-hierarchy.md);
- [mask ROM/PROM/EPROM/EEPROM -> Flash, erase blocks, remapping and wear](docs/memory/why-read-only-memory-kept-changing.md);
- [ECC, SECDED boundaries, scrubbing, layout and telemetry as statistical reliability infrastructure](docs/memory/why-ecc-became-memory-infrastructure.md);
- runnable [DRAM array](experiments/dram-array/) and [Flash erase](experiments/flash-erase/) constraint models;
- [source map](docs/references/semiconductor-memory-field-set.md) separating period evidence from reconstruction.

**Still deepen:** early SRAM cell-design primary literature; a tighter vendor-manual chronology for FPM and EDO; EEPROM's first commercial implementations; NOR/NAND product and controller histories; measured cache-hierarchy case studies; Chipkill/on-die ECC deployment history.

**Status:** the conceptual spine from core to ordinary semiconductor memory and onward to HBM now has a usable first treatment. Remaining work is source and case-study depth rather than a missing bridge.

### P0-C — Power delivery before the AI rack is almost absent

Recent rack power is covered, but ordinary computer power history has no comparable spine.

Missing first treatments:

- transformer + rectifier + linear regulator supplies;
- why switching power supplies became attractive;
- transistorized regulators and power semiconductors;
- AT/ATX supply conventions;
- motherboard point-of-load regulation;
- VRM evolution as CPU voltage fell and current rose;
- multiphase buck conversion;
- decoupling capacitors, package inductance and transient response;
- power sequencing, reset and power-good signals;
- battery-backed RTC/CMOS state.

**Why this is P0:** every logic family assumes a power-distribution system that the architecture diagram usually erases.

### P0-D — Clock and timing infrastructure is missing

The repository discusses speed but has little history of how machines manufacture a shared notion of time.

Missing first treatments:

- electromechanical timing and rotating-machine timing references;
- crystal oscillators;
- clock generators and frequency multiplication;
- PLL/DLL;
- clock trees and skew;
- jitter and timing margins;
- synchronous versus asynchronous design pressure;
- clock gating and the power cost of distributing time;
- spread-spectrum clocks as EMI engineering.

**Why this is P0:** a synchronous computer is a distributed timing machine. The clock is one of its largest hidden physical infrastructures.

### P0-E — Networking has almost no historical foundation

The repository now contains modern AI collective offload, but almost none of the historical network substrate that made it intelligible.

Missing first treatments:

- store-and-forward / message switching / packet switching;
- ARPANET IMP architecture;
- Ethernet coax, collision domains and CSMA/CD;
- repeaters, bridges and switches;
- TCP/IP layering and the end-to-end argument as engineering constraints;
- routing tables and router hardware;
- ARP and local-link address resolution;
- DNS hierarchy, caching and anycast evolution;
- NICs, DMA, checksum offload, RSS and later SmartNIC/DPU evolution;
- twisted pair / magnetics / PHY autonegotiation;
- Wi-Fi as shared-medium radio rather than `wireless Ethernet`.

**Why this is P0:** the project currently has a striking chronological hole from teletypes/modems-in-passing to contemporary high-speed AI fabrics.

## 3. P1 gaps — forgotten infrastructure that should be recovered next

### P1-A — Mainframe I/O and the printer queue

Still missing:

- IBM channels / channel programs / selector and multiplexer channels;
- programmed I/O versus DMA versus channel processors;
- line printers and offline printing;
- SPOOL/HASP-style queues and why slow peripherals became files/queues;
- interrupt controllers and I/O scheduling as hardware/software boundaries.

This would pair naturally with the existing UNIBUS/DMA work: mainframes and minicomputers solved the `CPU should not babysit every byte` problem differently.

### P1-B — Serial interfaces, modem control and current loop

Still missing:

- teletype current loop as electrical interface;
- EIA/RS-232 DTE/DCE distinction;
- TXD/RXD plus RTS/CTS/DTR/DSR/DCD/RI;
- null modems;
- Bell modem lineage beyond a passing mention;
- UARTs and baud-rate generators;
- why serial control lines survived into software APIs long after acoustic modems disappeared.

### P1-C — Disk and removable-media geometry after RAMAC

Still missing:

- tracks, heads, cylinders and sectors as software-visible geometry;
- floppy disks and sector interleave;
- bad-sector tables / sparing;
- seek scheduling;
- zone-bit recording;
- CHS -> LBA abstraction;
- controller intelligence;
- ST-506 / SCSI / IDE-ATA / SATA transitions;
- SSD/Flash translation layers as the later version of `physical geometry hidden below logical blocks`.

### P1-D — The personal-computer compatibility stack

The repository has PDP-8, UNIBUS and 6502, but the path into the commodity PC remains thin.

Missing first treatments:

- Intel 4004 / 8008 / 8080 and Z80;
- Altair and the S-100 bus;
- IBM PC bus -> ISA;
- BIOS as compatibility contract;
- DMA/PIC/PIT support chips;
- PC/AT keyboard controller;
- A20 gate;
- conventional/expanded/extended memory constraints;
- CGA/MDA/EGA/VGA and especially VGA text mode as a compatibility fossil;
- PCI and plug-and-play as later bus/ecosystem transitions.

### P1-E — Passive components are almost invisible

A computer is not built from active devices alone.

Missing first treatments:

- resistors and resistor networks;
- electrolytic/tantalum/ceramic capacitors;
- MLCC scaling and DC-bias effects;
- inductors and transformers;
- ferrites / beads for EMI suppression;
- connector magnetics;
- crystal resonators;
- component tolerances, aging and derating;
- why surface-mount passive components became so small and numerous.

### P1-F — Packaging end-of-line / OSAT process flow

The repository has rich packaging materials and reliability coverage but less of the ordinary factory sequence between finished wafer and shipped component.

Missing first treatments:

- wafer probe -> wafer thinning -> dicing/singulation;
- die attach;
- wire bond / flip-chip assembly as production flows;
- molding / encapsulation;
- trim-and-form;
- marking;
- package-level burn-in/final test;
- tray/tube/tape-and-reel handling;
- OSAT economics, qualification and traceability.

## 4. P2 gaps — software and human interfaces

These matter to a full computing archaeology but can follow the hardware/infrastructure holes above.

### Software toolchain

- assemblers and symbolic addresses;
- linkers/loaders;
- compiler history as a machine-cost response;
- relocatable object formats;
- dynamic linking beyond the Multics case;
- debugging hardware and software;
- microcode and writable control stores.

### Files and databases

- file systems from tape/disk geometry;
- directories, allocation and free-space management;
- journaling / crash consistency;
- indexed files and B-trees;
- database buffer pools and storage hierarchy.

### Displays, keyboards, mice and printing

- line printers;
- CRT raster scanning versus vector displays;
- framebuffer memory;
- character generators;
- keyboard matrices and scan codes;
- mouse/pointing-device lineage;
- graphics terminals;
- GPU/framebuffer evolution as memory-bandwidth history.

## 5. Already covered — do not accidentally reopen as blank work

Before proposing a new field set, agents should check the existing track entrances. The following are **not** blank topics anymore:

- semiconductor purity / crystal growth / wafer scaling;
- planar process and lithography history;
- masks, overlay, EUV, High-NA and EUV stochastic pressure;
- implant, process control, ATE, probe and burn-in;
- cleanroom / UPW / gas / vacuum / abatement;
- photoresist, CMP, thin-film precursors and target materials;
- copper interconnect, barriers, tungsten contacts, low-k/high-k;
- PCB stack materials, SMT, microvias and surface finishes;
- packaging, wire bonds, flip-chip, underfill, TIM and advanced packaging;
- TDDB / hot-carrier / BTI / electromigration / solder fatigue / moisture / whiskers;
- FinFET / GAA / forksheet / CFET / backside power;
- HBM / HBM4, interposers, hybrid bonding and chiplets;
- PAM4/FEC, retimers, 224G/448G channel pressure and CPO;
- rack busbars, 800 VDC, cold plates, CDU/coolant chemistry;
- in-network collective offload.

These should be **deepened**, not rediscovered from scratch.

## 6. Recommended next integrated field sets

Do not return to tiny one-topic PRs. The cleanest next program is:

### Field Set A — The missing semiconductor process middle

Etch + epitaxy + anneal/RTP + wafer preparation + process metrology.

### Field Set B — From magnetic core to HBM

SRAM + DRAM + sense/refresh + SDRAM/DDR + ROM/EEPROM/Flash + cache/ECC.

### Field Set C — Power and time

Power supplies + VRMs + decoupling + crystal oscillators + PLL/DLL + clock trees/jitter.

### Field Set D — I/O becomes infrastructure

IBM channels + SPOOL/line printers + current loop/RS-232/UART/modems + interrupt/DMA evolution.

### Field Set E — Storage geometry gets hidden

Floppy/interleave + HDD CHS/sectors/bad blocks + controllers + LBA + SCSI/IDE/SATA + FTL/SSD.

### Field Set F — The compatibility PC

4004/8080/Z80 + Altair/S-100 + IBM PC/ISA + BIOS + support chips + A20 + VGA.

### Field Set G — Networking before the AI fabric

Packet switching + ARPANET IMP + Ethernet + switching + TCP/IP + routing + DNS + NIC/offload.

These seven sets repair the largest chronological and systems-level holes before the repository pushes much further into contemporary accelerator infrastructure.

## 7. Audit rule for future agents

Before adding a new article:

1. search the repository for the mechanism, not only the product name;
2. check `README.md`, `INDEX.md`, `ROADMAP.md`, `MANUFACTURING-COMPLETION.md`, `POST-SCALING.md`, `SPEED.md`, and this file;
3. decide whether the task is a **blank first treatment** or **source deepening**;
4. prefer coherent field sets that close a dependency chain;
5. update navigation in the same PR;
6. never leave a completed topic described as future work;
7. keep historical record, engineering reconstruction and experiment distinct.

> **The repository is now deep enough that its next danger is not forgetting everything. It is forgetting the middle.**
