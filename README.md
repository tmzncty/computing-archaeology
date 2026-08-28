# computing-archaeology

> **Computers are not inevitable. They are accumulated engineering decisions.**

`computing-archaeology` is an experimental history of computing: a repository for reconstructing **why computers became what they are** through material constraints, forgotten technologies, institutional choices, failed designs, labor, maintenance, standards, and small hands-on experiments.

A normal timeline asks:

> What was invented, by whom, and when?

This repository asks a different set of questions:

> What could engineers actually build at the time?  
> Which constraints made one design reasonable and another absurd?  
> Which “obsolete” technologies were once excellent answers to real problems?  
> Which failures, accidents, industries, standards, habits, and forms of labor quietly shaped the machines we inherited?

The goal is not to replace conventional computer history. It is to put **engineering pressure back into history**.

## The method

Every substantial article distinguishes three layers:

1. **Historical record** — what surviving documents, machines, patents, oral histories, museum collections, and scholarship establish.
2. **Engineering reconstruction** — what follows when we reason from the period's available components, costs, speeds, manufacturing limits, interfaces, and operational needs.
3. **Experiment** — a simulation, replica, program, FPGA build, paper exercise, or physical demonstration that lets us test part of the reconstruction.

These layers must not be silently mixed. A plausible reconstruction is not automatically a historical fact, and a modern experiment does not prove historical intent.

See [`docs/methodology/constraint-first-history.md`](docs/methodology/constraint-first-history.md) and [`AGENTS.md`](AGENTS.md).

## Start here

### Mechanical arithmetic: when notation becomes force

- [`docs/mechanical/why-difference-engine.md`](docs/mechanical/why-difference-engine.md) — why finite differences made mechanical computation tractable.
- [`docs/mechanical/why-carry-is-a-machine-problem.md`](docs/mechanical/why-carry-is-a-machine-problem.md) — why `9999 + 1` becomes a worst-case load path when every carry is a physical event.

### Relays and electronics: making imperfect switches behave like logic

- [`docs/electromechanical/why-relays.md`](docs/electromechanical/why-relays.md) — how telephone switching hardware became computing machinery.
- [`docs/electromechanical/why-one-switch-can-look-like-many.md`](docs/electromechanical/why-one-switch-can-look-like-many.md) — why contact bounce can turn one mechanical closure into several logical edges.
- [`docs/electronic/why-vacuum-tubes.md`](docs/electronic/why-vacuum-tubes.md) — why electronic speed could justify heat, power, failure risk, and a new maintenance culture.
- [`case-studies/eniac/from-wiring-to-stored-program.md`](case-studies/eniac/from-wiring-to-stored-program.md) — why the transition from physical configuration to coded control was gradual rather than one clean invention.

### Memory: sound, rotation, magnetism, and locality

- [`docs/memory/why-early-memory-looked-weird.md`](docs/memory/why-early-memory-looked-weird.md) — mercury, CRTs, drums, and magnetic cores as answers to the memory problem.
- [`docs/memory/why-memory-was-a-tube-of-sound.md`](docs/memory/why-memory-was-a-tube-of-sound.md) — how radar-derived acoustic delay lines made an address into a time at which the word came back.
- [`docs/memory/why-drum-memory-made-programmers-wait.md`](docs/memory/why-drum-memory-made-programmers-wait.md) — how IBM 650 programmers and assemblers scheduled code around a rotating drum.
- [`docs/memory/why-core-memory-was-worth-weaving.md`](docs/memory/why-core-memory-was-worth-weaving.md) — coincident-current selection, destructive read/restore, and why manual core weaving belonged inside architecture history.

### Programs, operators, terminals, and users

- [`docs/interaction/why-programs-were-holes.md`](docs/interaction/why-programs-were-holes.md) — why punched media fit data processing before keyboards and disks did.
- [`docs/interaction/why-batch-processing-made-sense.md`](docs/interaction/why-batch-processing-made-sense.md) — why removing the programmer from the console could improve total installation throughput.
- [`docs/interaction/why-terminals-were-teletypes.md`](docs/interaction/why-terminals-were-teletypes.md) — why telegraph machines, paper tape, ASCII, telephone lines, and 110-baud printing became one computer interface lineage.
- [`case-studies/ctss/from-batch-to-conversation.md`](case-studies/ctss/from-batch-to-conversation.md) — what timer interrupts, protection, relocation, buffering, storage, and scheduling had to do before one mainframe could feel personal to many users.

### Architecture that no longer looks “normal”

- [`docs/architecture/why-word-lengths-were-weird.md`](docs/architecture/why-word-lengths-were-weird.md) — why 18-, 36-, and 60-bit words could be coherent engineering choices.
- [`docs/architecture/why-eight-bit-byte.md`](docs/architecture/why-eight-bit-byte.md) — why “byte = 8 bits” is a historical outcome, not a law of nature.

### Research infrastructure

- [`docs/references/source-ledger.md`](docs/references/source-ledger.md) — the main archival/source map.
- [`docs/references/strange-constraints-field-set.md`](docs/references/strange-constraints-field-set.md) — detailed source map for carry, bounce, delay lines, core memory, teletypes, ASCII, and CTSS.
- [`ACKNOWLEDGEMENTS.md`](ACKNOWLEDGEMENTS.md) — the people and institutions whose preservation and operational work makes this repository possible.
- [`ROADMAP.md`](ROADMAP.md) — the larger excavation plan.

## Runnable experiments

The experiments are intentionally small and dependency-free where practical. They expose one constraint at a time rather than cosmetically imitating an old machine.

- [`experiments/finite-differences/`](experiments/finite-differences/) — compare direct polynomial evaluation with repeated finite-difference addition under different operation-cost assumptions.
- [`experiments/carry-propagation/`](experiments/carry-propagation/) — compare radix, digit count, carry frequency, and a deliberately adjustable synthetic mechanical-cost model.
- [`experiments/relay-bounce/`](experiments/relay-bounce/) — let one intended closure become several edges, then compare qualification strategies.
- [`experiments/reliability-throughput/`](experiments/reliability-throughput/) — show why a faster but less available machine can still deliver much more useful work.
- [`experiments/serial-memory/`](experiments/serial-memory/) — make a requested word wait until it reaches the only access point in a circulating store.
- [`experiments/drum-timing/`](experiments/drum-timing/) — compare consecutive and timing-aware instruction placement on a rotating drum.
- [`experiments/core-memory/`](experiments/core-memory/) — expose half-selection, coincident selection, destructive read, and restore in a conceptual core plane.
- [`experiments/batch-economics/`](experiments/batch-economics/) — compare machine occupancy and throughput under direct per-job setup and batching.
- [`experiments/tty-budget/`](experiments/tty-budget/) — translate slow serial output into seconds of human waiting.
- [`experiments/time-sharing/`](experiments/time-sharing/) — show how long human think times can leave enough gaps for many interactive users to share one CPU.
- [`experiments/word-packing/`](experiments/word-packing/) — compare how historical word widths pack different character/field widths.

Each experiment README states its assumptions and, just as importantly, what the model **cannot** establish historically.

## A recurring pattern: the physical world leaks upward

The current excavation set makes one theme hard to miss.

A clean abstraction often exists because lower layers are doing substantial work to hide physical behavior:

```text
arithmetic carry
    <- torque, latches, gravity, backlash

Boolean contact
    <- impact, rebound, settling time

memory address
    <- sound propagation or drum rotation

random-access core bit
    <- ferrite thresholds, sense pulses, restore cycles, hand threading

terminal character
    <- motors, paper, serial framing, telephone infrastructure

interactive process
    <- interrupts, protection, buffers, swapping, scheduling
```

Computing history gets more interesting when those hidden layers are restored.

## Questions this project wants to answer

- Why did Babbage choose decimal wheels even though he considered binary?
- Why can `9999 + 1` be a mechanical stress test?
- Why was repeated addition a useful *architectural* trick?
- Why could telephone relays become logic elements?
- Why can one relay closure look like several events?
- Why accept thousands of vacuum tubes instead of staying with relays?
- Why did programming spend decades as wiring, switches, cards, and paper tape?
- What exactly changed when control became coded information?
- Why did early main memory use sound waves in mercury?
- Why did CRTs briefly make sense as RAM?
- Why did magnetic drums make programmers care about rotational position?
- Why was magnetic-core memory worth threading by hand?
- Why could reading core memory destroy the bit and still be a good design?
- Why were early word lengths so strange by modern standards?
- Why did the byte eventually settle at eight bits?
- Why did batch processing precede interactive computing?
- Why did terminals inherit so much from telegraphy and office machinery?
- Why can 110 baud shape a command language?
- What hardware has to exist before time-sharing becomes socially safe and responsive?
- Why do apparently “new” bottlenecks — memory bandwidth, locality, I/O, power, contention — keep returning?

## What this is not

This is **not** a “great men and great machines” list, and it is not a claim that one technical constraint mechanically determines history. Engineering choices are also shaped by institutions, budgets, labor, standards, military and commercial demand, maintenance practices, available skills, and prior installed systems.

The repository should therefore preserve failed branches and awkward transitional designs, not edit history into a clean road toward the modern PC.

It also avoids unqualified priority slogans. “First computer,” “first programmer,” “first operating system,” and “first stored-program computer” are questions that require a criterion, not badges to be handed out casually.

## Sources and citation policy

Historical claims are cited as close to the claim as practical. Prefer, in roughly this order:

- primary documents, patents, manuals, design memos, correspondence, and contemporary reports;
- museum and archival collections with provenance;
- peer-reviewed history of computing and strong scholarly monographs;
- institutional histories, oral histories, and high-quality technical retrospectives;
- tertiary summaries only as navigation aids, not as the sole support for contentious claims.

A source can be valuable without being neutral. Corporate histories, memoirs, oral histories, inventor descriptions, advertisements, and modern reconstructions are identified for what they are.

Current material draws on the Computer History Museum, Bitsavers, IBM documentation, DEC documentation, CDC design records, MIT/Project MAC and CTSS records, the University of Manchester, the University of Pennsylvania, Smithsonian collections, Museums Victoria, the National Museum of Computing, ACONIT/Inria, Bell System publications, and standards/preservation archives.

See [`docs/references/source-ledger.md`](docs/references/source-ledger.md) and the field-set source maps for source-level notes, plus [`ACKNOWLEDGEMENTS.md`](ACKNOWLEDGEMENTS.md) for preservation credit.

## Authorship and assistance

Repository owner and maintainer: **tmzncty**.

Initial research structure, source triage, experiments, drafting, and editorial assistance: **ChatGPT (GPT-5.6 Sol), OpenAI**.

AI-assisted text in this repository should be treated like any other secondary synthesis: useful for organizing questions and reconstructing engineering choices, but subject to verification against cited sources. The presence of a citation does not excuse a bad inference.

## Status

**M0 — method and first excavations: complete.**

The repository now has defensible first treatments spanning mechanical arithmetic, electromechanical logic, early electronics, serial and random-access memory, punched/batch workflows, slow terminals, time-sharing, and word/byte architecture, with runnable constraint experiments attached to the major mechanisms.

The next milestones can go deeper instead of rebuilding the foundation: gear backlash and tolerances, Jacquard/Hollerith/card sorting, relay adders, Williams–Kilburn storage, original System/360 design papers, Multics, minicomputers/microprocessors, ASCII/EBCDIC and terminal standards, endianness, buses, storage sectors, and compatibility fossils that still shape modern machines.

If a page makes you say “why on earth would anyone build it that way?”, that is probably where the excavation should begin.
