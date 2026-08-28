# computing-archaeology

> **Computers are not inevitable. They are accumulated engineering decisions.**

`computing-archaeology` is an experimental history of computing: a repository for reconstructing **why computers became what they are** through material constraints, forgotten technologies, institutional choices, failed designs, labor, maintenance, standards, compatibility, and small hands-on experiments.

A normal timeline asks:

> What was invented, by whom, and when?

This repository asks a different set of questions:

> What could engineers actually build at the time?  
> Which constraints made one design reasonable and another absurd?  
> Which obsolete technologies were once excellent answers to real problems?  
> Which physical formats became software interfaces?  
> Which standards survived long after their original machines disappeared?  
> Which forms of labor and maintenance made the abstraction possible?

The goal is not to replace conventional computer history. It is to put **engineering pressure back into history**.

## The method

Every substantial article distinguishes three layers:

1. **Historical record** — what surviving documents, machines, patents, manuals, oral histories, museum collections, standards, and scholarship establish.
2. **Engineering reconstruction** — what follows when we reason from the period's available components, costs, speeds, manufacturing limits, interfaces, and operational needs.
3. **Experiment** — a simulation, replica, program, FPGA build, paper exercise, or physical demonstration that lets us test part of the reconstruction.

These layers must not be silently mixed. A plausible reconstruction is not automatically a historical fact, and a modern experiment does not prove historical intent.

See [`docs/methodology/constraint-first-history.md`](docs/methodology/constraint-first-history.md) and [`AGENTS.md`](AGENTS.md).

## Start here

### Mechanical arithmetic: when notation becomes force

- [`docs/mechanical/why-difference-engine.md`](docs/mechanical/why-difference-engine.md) — why finite differences made mechanical computation tractable.
- [`docs/mechanical/why-carry-is-a-machine-problem.md`](docs/mechanical/why-carry-is-a-machine-problem.md) — why `9999 + 1` becomes a worst-case load path when every carry is a physical event.

### Relays and electronics: making imperfect devices behave like logic

- [`docs/electromechanical/why-relays.md`](docs/electromechanical/why-relays.md) — how telephone switching hardware became computing machinery.
- [`docs/electromechanical/why-one-switch-can-look-like-many.md`](docs/electromechanical/why-one-switch-can-look-like-many.md) — why contact bounce can turn one mechanical closure into several logical edges.
- [`docs/electronic/why-vacuum-tubes.md`](docs/electronic/why-vacuum-tubes.md) — why electronic speed could justify heat, power, failure risk, and a new maintenance culture.
- [`case-studies/eniac/from-wiring-to-stored-program.md`](case-studies/eniac/from-wiring-to-stored-program.md) — why the transition from physical configuration to coded control was gradual rather than one clean invention.

### Memory and storage: sound, charge, rotation, magnetism, and tape

- [`docs/memory/why-early-memory-looked-weird.md`](docs/memory/why-early-memory-looked-weird.md) — comparative survey of early memory technologies.
- [`docs/memory/why-memory-was-a-tube-of-sound.md`](docs/memory/why-memory-was-a-tube-of-sound.md) — how acoustic delay lines made an address into a time at which the word came back.
- [`docs/memory/why-crt-became-ram.md`](docs/memory/why-crt-became-ram.md) — why charge patterns on a commercial CRT briefly became credible random-access electronic memory.
- [`docs/memory/why-drum-memory-made-programmers-wait.md`](docs/memory/why-drum-memory-made-programmers-wait.md) — how IBM 650 programmers and assemblers scheduled code around a rotating drum.
- [`docs/memory/why-core-memory-was-worth-weaving.md`](docs/memory/why-core-memory-was-worth-weaving.md) — coincident-current selection, destructive read/restore, and why manual core weaving belonged inside architecture history.
- [`docs/memory/why-tape-made-you-think-sequentially.md`](docs/memory/why-tape-made-you-think-sequentially.md) — why high streaming bandwidth could coexist with terrible arbitrary access and why interblock gaps made blocking a systems concern.

### Programs, cards, booting, operators, and terminals

- [`docs/interaction/why-programs-were-holes.md`](docs/interaction/why-programs-were-holes.md) — why punched media fit data processing before keyboards and disks did.
- [`docs/interaction/why-eighty-columns-survived.md`](docs/interaction/why-eighty-columns-survived.md) — how an office-machine card format became a source-code and record-format fossil.
- [`docs/interaction/why-booting-started-with-switches.md`](docs/interaction/why-booting-started-with-switches.md) — why a PDP-8 could begin with an operator toggling a tiny loader into core so that software could load more software.
- [`docs/interaction/why-batch-processing-made-sense.md`](docs/interaction/why-batch-processing-made-sense.md) — why removing the programmer from the console could improve total installation throughput.
- [`docs/interaction/why-terminals-were-teletypes.md`](docs/interaction/why-terminals-were-teletypes.md) — why telegraph machines, paper tape, ASCII, telephone lines, and 110-baud printing became one computer-interface lineage.
- [`case-studies/ctss/from-batch-to-conversation.md`](case-studies/ctss/from-batch-to-conversation.md) — what timer interrupts, protection, relocation, buffering, storage, and scheduling had to do before one mainframe could feel personal to many users.

### Architecture and standards: decisions that became compatibility

- [`docs/architecture/why-word-lengths-were-weird.md`](docs/architecture/why-word-lengths-were-weird.md) — why 18-, 36-, and 60-bit words could be coherent engineering choices.
- [`docs/architecture/why-eight-bit-byte.md`](docs/architecture/why-eight-bit-byte.md) — why `byte = 8 bits` is a historical outcome, not a law of nature.
- [`docs/architecture/why-byte-order-became-a-holy-war.md`](docs/architecture/why-byte-order-became-a-holy-war.md) — why local byte layout became an interoperability problem and why networks need canonical serialization.
- [`docs/standards/why-text-is-full-of-device-fossils.md`](docs/standards/why-text-is-full-of-device-fossils.md) — why CR, LF, BEL, DEL, ASCII, EBCDIC, and TELNET still carry physical-device and installed-base history.

### Research infrastructure

- [`docs/references/source-ledger.md`](docs/references/source-ledger.md) — the main archival/source map.
- [`docs/references/strange-constraints-field-set.md`](docs/references/strange-constraints-field-set.md) — Pascaline carry, relay bounce, acoustic delay lines, magnetic core, teletypes, ASCII, and CTSS.
- [`docs/references/fossils-and-media-field-set.md`](docs/references/fossils-and-media-field-set.md) — CRT refresh, 80-column cards, magnetic tape, front-panel bootstrapping, text standards, and endianness.
- [`ACKNOWLEDGEMENTS.md`](ACKNOWLEDGEMENTS.md) — the people and institutions whose preservation and operational work makes this repository possible.
- [`ROADMAP.md`](ROADMAP.md) — the larger excavation plan.

## Runnable experiments

The experiments are intentionally small and dependency-free where practical. They expose one constraint at a time rather than cosmetically imitating an old machine.

### Arithmetic and switching

- [`experiments/finite-differences/`](experiments/finite-differences/) — direct polynomial evaluation versus repeated finite-difference addition.
- [`experiments/carry-propagation/`](experiments/carry-propagation/) — radix, digit count, carry frequency, and a synthetic mechanical-cost model.
- [`experiments/relay-bounce/`](experiments/relay-bounce/) — one intended contact closure becoming several edges.
- [`experiments/reliability-throughput/`](experiments/reliability-throughput/) — why a faster but less available machine can still deliver more useful work.

### Memory and storage

- [`experiments/serial-memory/`](experiments/serial-memory/) — a requested word waits until it reaches the only access point in a circulating store.
- [`experiments/crt-refresh/`](experiments/crt-refresh/) — decaying cells, background refresh, and the capacity-versus-scan-bandwidth tradeoff.
- [`experiments/drum-timing/`](experiments/drum-timing/) — consecutive versus timing-aware placement on a rotating drum.
- [`experiments/core-memory/`](experiments/core-memory/) — half-selection, coincidence, destructive read, and restore.
- [`experiments/tape-locality/`](experiments/tape-locality/) — sequential versus shuffled access and the effect of fixed interblock overhead.

### Media, users, and compatibility

- [`experiments/card-columns/`](experiments/card-columns/) — 72-character source fields, 8-character sequence fields, deck shuffling, and recovery.
- [`experiments/bootstrap-chain/`](experiments/bootstrap-chain/) — how a tiny manual seed can load a much larger software environment.
- [`experiments/batch-economics/`](experiments/batch-economics/) — machine occupancy and throughput under direct setup versus batching.
- [`experiments/tty-budget/`](experiments/tty-budget/) — slow serial output translated into human waiting time.
- [`experiments/time-sharing/`](experiments/time-sharing/) — human think-time as a multiplexing opportunity.
- [`experiments/text-fossils/`](experiments/text-fossils/) — separate CR/LF motions and ASCII/EBCDIC byte differences.
- [`experiments/endianness/`](experiments/endianness/) — the same integer serialized in opposite byte orders and decoded correctly/incorrectly.
- [`experiments/word-packing/`](experiments/word-packing/) — historical word widths packing different character and field widths.

Every experiment README states its assumptions and, just as importantly, what the model **cannot** establish historically.

## Three recurring patterns

### 1. The physical world leaks upward

A clean abstraction often exists because lower layers are doing substantial work to hide physical behavior:

```text
arithmetic carry
    <- torque, latches, gravity, backlash

Boolean contact
    <- impact, rebound, settling time

memory address
    <- sound propagation, beam deflection, drum rotation, ferrite thresholds

stable RAM bit
    <- refresh, regeneration, destructive read/restore

terminal character
    <- motors, paper, serial framing, telephone infrastructure
```

### 2. The medium shapes the algorithm

```text
punched card
    -> fixed-width record, physical ordering, sequence fields

magnetic tape
    -> sequential scan, blocking, merge/update workflows

magnetic drum
    -> rotational placement, timing-aware instruction layout

slow terminal
    -> short prompts, line editors, buffered interaction
```

The algorithm is not designed in a vacuum. It learns the geometry of the device beneath it.

### 3. Compatibility outlives the original machine

```text
80-column card
    -> 80-byte/card-image records

mechanical carriage + paper feed
    -> CR / LF controls

host character set
    -> ASCII / EBCDIC translation

native byte layout
    -> serialization rules / network byte order

manual seed loader
    -> firmware boot chain
```

A historical constraint can stop being physical and become **economic**: too much existing software, data, documentation, and hardware expects the old convention.

## Questions this project wants to answer

- Why did Babbage choose decimal wheels even though he considered binary?
- Why can `9999 + 1` be a mechanical stress test?
- Why can one relay closure look like several events?
- Why accept thousands of vacuum tubes instead of staying with relays?
- Why can memory be a sound wave, a CRT charge pattern, a rotating drum, or a hand-threaded ferrite grid?
- Why can reading memory destroy the bit and still be a good design?
- Why can a storage device stream quickly but be terrible at random access?
- Why did programming spend decades as wiring, switches, cards, and paper tape?
- Why did 80 columns remain meaningful after the card stopped being the physical medium?
- How do you load software before software exists to load it?
- Why did batch processing precede interactive computing?
- Why did terminals inherit so much from telegraphy and office machinery?
- Why are carriage return and line feed still separate characters?
- Why did ASCII and EBCDIC coexist instead of one code instantly winning?
- Why were early word lengths so strange by modern standards?
- Why did the byte eventually settle at eight bits?
- Why did byte order become a compatibility war?
- Why does a network need a canonical representation independent of host memory layout?
- Why do apparently new bottlenecks — memory bandwidth, locality, I/O, power, contention, serialization — keep returning?

## What this is not

This is **not** a “great men and great machines” list, and it is not a claim that one technical constraint mechanically determines history. Engineering choices are also shaped by institutions, budgets, labor, standards, military and commercial demand, maintenance practices, available skills, and prior installed systems.

The repository therefore preserves failed branches and awkward transitional designs instead of editing history into a clean road toward the modern PC.

It also avoids unqualified priority slogans. “First computer,” “first programmer,” “first operating system,” and “first stored-program computer” are questions that require a criterion, not badges to be handed out casually.

## Sources and citation policy

Historical claims are cited as close to the claim as practical. Prefer, in roughly this order:

- primary documents, patents, manuals, design memos, correspondence, standards, and contemporary reports;
- museum and archival collections with provenance;
- peer-reviewed history of computing and strong scholarly monographs;
- institutional histories, oral histories, and high-quality technical retrospectives;
- tertiary summaries only as navigation aids, not as the sole support for contentious claims.

A source can be valuable without being neutral. Corporate histories, memoirs, oral histories, inventor descriptions, advertisements, standards documents, and modern reconstructions are identified for what they are.

Current material draws on the Computer History Museum, Bitsavers, IBM and DEC documentation, CDC design records, MIT/Project MAC and CTSS records, the University of Manchester, the University of Pennsylvania, Smithsonian collections, Museums Victoria, the National Museum of Computing, ACONIT/Inria, Bell System publications, IETF/RFC archives, and specialist preservation sites.

## Authorship and assistance

Repository owner and maintainer: **tmzncty**.

Initial research structure, source triage, experiments, drafting, and editorial assistance: **ChatGPT (GPT-5.6 Sol), OpenAI**.

AI-assisted text in this repository should be treated like any other secondary synthesis: useful for organizing questions and reconstructing engineering choices, but subject to verification against cited sources. The presence of a citation does not excuse a bad inference.

## Status

**M0 — method and first excavations: complete.**

The repository now has defensible first treatments spanning mechanical arithmetic, electromechanical logic, early electronics, serial/random-access memory, magnetic mass storage, punched/batch workflows, startup/bootstrapping, slow terminals, time-sharing, word/byte architecture, character standards, and interoperability fossils, with runnable constraint experiments attached to the major mechanisms.

The next milestones can go deeper instead of rebuilding the foundation: Jacquard/Hollerith sorting, full Williams-tube electrical details, core production at scale, magnetic-tape software ecosystems, Multics, PDP buses, Intel 4004/8008, MOS 6502, Z80, disk geometry and sectors, terminal escape standards, x86 compatibility, and the increasingly strange places where old interfaces survive inside modern machines.

If a page makes you say “why on earth would anyone build it that way?”, that is probably where the excavation should begin.
