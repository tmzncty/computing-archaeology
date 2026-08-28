# Roadmap

This roadmap is organized by **historical problems**, not by a single parade of machines. Chronology still matters, but the project should repeatedly stop and ask what problem made a technology sensible in its own time.

A checked item means the repository now has a defensible first treatment. It does **not** mean the historical topic is exhausted.

## M0 — Method and first excavations ✅

Goal: establish a repeatable way to separate evidence, reconstruction, and experiment.

- [x] Define the constraint-first method.
- [x] Establish source/citation rules and historical caution points.
- [x] Add source maps, acknowledgements, and AI-assistance disclosure.
- [x] Demonstrate the method across mechanical, electromechanical, electronic, memory, storage, interaction, architecture, and standards topics.
- [x] Attach runnable experiments with explicit model limitations.
- [x] Run experiment smoke tests and internal-link checks in CI.

The foundation now supports deeper excavations without changing the method every time.

## M1 — Mechanical computation

Questions:

- What does it cost, mechanically, to carry a digit?
- Why can addition be dramatically easier than multiplication?
- Why did decimal survive inside machines that could in principle use other radices?
- How do tolerances, backlash, inertia, and gearing alter what an algorithm looks like?

Completed first treatments:

- [x] [`docs/mechanical/why-difference-engine.md`](docs/mechanical/why-difference-engine.md) — finite differences as a way to turn tabulation into repeated addition.
- [x] [`docs/mechanical/why-carry-is-a-machine-problem.md`](docs/mechanical/why-carry-is-a-machine-problem.md) — Pascaline `sautoir`, long carry chains, complement subtraction, and radix tradeoffs.
- [x] [`experiments/finite-differences/`](experiments/finite-differences/)
- [x] [`experiments/carry-propagation/`](experiments/carry-propagation/)

Still deepen with:

- surviving Pascaline mechanism drawings/measurements;
- Leibniz stepped reckoner / stepped drum;
- Babbage Analytical Engine carry and sequencing;
- Scheutz engines;
- desk adding machines and comptometers;
- Curta;
- backlash, tolerance, wear, and a gear-train error model.

## M2 — Punched media and information machinery

Questions:

- Why did holes become a durable representation of information?
- Why were census, accounting, railway, and office workflows so important?
- How did card dimensions and column counts become software-visible constraints?
- What changes when programs are physical decks that can be dropped, sorted, duplicated, and queued?

Completed first treatments:

- [x] [`docs/interaction/why-programs-were-holes.md`](docs/interaction/why-programs-were-holes.md) — why punched media fit data processing.
- [x] [`docs/interaction/why-eighty-columns-survived.md`](docs/interaction/why-eighty-columns-survived.md) — IBM's 80-column card, 72/80-column programming practice, sequence fields, and format fossilization.
- [x] [`experiments/card-columns/`](experiments/card-columns/) — fixed-width card images, shuffled deck, sequence-based recovery.

Still deepen with:

- Jacquard control media;
- Hollerith's census machinery and early card formats;
- IBM readers, sorters, punches, reproducing punches, tabulators;
- dedicated paper-tape history;
- card verification/keypunch labor;
- one substantial card-sorting data-processing experiment rather than only source-deck recovery.

## M3 — Relays, switching, and the telephone inheritance

Questions:

- Why did telephone switching supply useful logic components?
- What are the real costs of relay logic: speed, bounce, wear, coil power, fan-out, wiring?
- How did remote teleprinter access emerge before online computing became ordinary?

Completed first treatments:

- [x] [`docs/electromechanical/why-relays.md`](docs/electromechanical/why-relays.md)
- [x] [`docs/electromechanical/why-one-switch-can-look-like-many.md`](docs/electromechanical/why-one-switch-can-look-like-many.md)
- [x] [`experiments/relay-bounce/`](experiments/relay-bounce/)

Still deepen with:

- Stibitz/Bell Labs primary reports;
- Zuse machines;
- Harvard Mark I;
- relay adders and carry timing;
- relay logic notation, adjustment, contact materials, and maintenance;
- system-scale relay-versus-electronic timing.

## M4 — Vacuum tubes and electronic speed

Questions:

- Why accept heat, power consumption, and component failure for electronic switching?
- How much of the system problem moved into memory, power, cooling, and maintenance?
- Why was rewiring an acceptable programming method for some early machines?

Completed first treatments:

- [x] [`docs/electronic/why-vacuum-tubes.md`](docs/electronic/why-vacuum-tubes.md)
- [x] [`case-studies/eniac/from-wiring-to-stored-program.md`](case-studies/eniac/from-wiring-to-stored-program.md)
- [x] [`experiments/reliability-throughput/`](experiments/reliability-throughput/)

Still deepen with:

- Colossus primary documentation;
- ENIAC maintenance records and failure logs;
- full EDVAC correspondence/documentation;
- relay-versus-electronic system timing.

## M5 — The memory and storage problem

Early computers did not simply “have RAM” and “have a disk.” Designers searched across radically different physical phenomena.

Questions:

- Why can a mercury tube be memory?
- Why can a CRT be memory?
- Why does rotating storage force programmers to think about time and geometry?
- Why did magnetic core become such a dominant compromise?
- When does reading or simply waiting physically damage stored state?
- Why can a storage device stream quickly while still having terrible random access?

Completed first treatments:

- [x] [`docs/memory/why-early-memory-looked-weird.md`](docs/memory/why-early-memory-looked-weird.md) — comparative survey.
- [x] [`docs/memory/why-memory-was-a-tube-of-sound.md`](docs/memory/why-memory-was-a-tube-of-sound.md) — acoustic delay lines.
- [x] [`docs/memory/why-crt-became-ram.md`](docs/memory/why-crt-became-ram.md) — Williams–Kilburn charge storage, pickup, regeneration, density constraints, and Baby integration.
- [x] [`docs/memory/why-drum-memory-made-programmers-wait.md`](docs/memory/why-drum-memory-made-programmers-wait.md) — IBM 650 rotational timing.
- [x] [`docs/memory/why-core-memory-was-worth-weaving.md`](docs/memory/why-core-memory-was-worth-weaving.md) — coincident-current core memory, destructive read/restore, and labor.
- [x] [`docs/memory/why-tape-made-you-think-sequentially.md`](docs/memory/why-tape-made-you-think-sequentially.md) — sequential tape geometry, vacuum buffering, interblock gaps, blocking, and stream-oriented algorithms.
- [x] [`experiments/serial-memory/`](experiments/serial-memory/)
- [x] [`experiments/crt-refresh/`](experiments/crt-refresh/)
- [x] [`experiments/drum-timing/`](experiments/drum-timing/)
- [x] [`experiments/core-memory/`](experiments/core-memory/)
- [x] [`experiments/tape-locality/`](experiments/tape-locality/)

Still deepen with:

- full Williams-tube circuit-level scanning/read/write reconstruction;
- EDSAC/SEAC/CSIRAC machine-specific delay timing;
- core inhibit wiring and commercial production at scale;
- UNIVAC/IBM tape formats, controllers, tape marks, buffering, and operating-system libraries;
- external sorting / tape merge as a full reproducible exercise;
- early semiconductor memory;
- RAMAC and disk geometry as the next locality transition.

## M6 — Stored programs, words, and instruction formats

Questions:

- Why was a word once more fundamental than a byte?
- Why did 18-, 24-, 36-, 48-, and 60-bit machines make sense?
- Why were instruction formats shaped by physical memory technology?
- Why did character processing push architectures toward different compromises?

Completed first treatments:

- [x] [`case-studies/eniac/from-wiring-to-stored-program.md`](case-studies/eniac/from-wiring-to-stored-program.md)
- [x] [`docs/architecture/why-word-lengths-were-weird.md`](docs/architecture/why-word-lengths-were-weird.md)
- [x] [`docs/architecture/why-eight-bit-byte.md`](docs/architecture/why-eight-bit-byte.md)
- [x] [`experiments/word-packing/`](experiments/word-packing/)

Still deepen with:

- Manchester Mark I and EDSAC instruction formats;
- IAS-family diffusion;
- original System/360 design papers;
- 24- and 48-bit families;
- instruction-format tradeoff explorer beyond packing.

## M7 — Batch, operators, and the missing user

Questions:

- Why was direct user interaction once economically irrational?
- What did an operator actually do?
- Why did job queues, job control, and offline peripherals exist?
- How did machine utilization shape software organization?

Completed first treatments:

- [x] [`docs/interaction/why-batch-processing-made-sense.md`](docs/interaction/why-batch-processing-made-sense.md)
- [x] [`experiments/batch-economics/`](experiments/batch-economics/)

Still deepen with:

- original GM-NAA documentation;
- operator manuals and machine-room procedures;
- job-control languages;
- scheduler/accounting evolution;
- labor history across more installations.

## M8 — Time-sharing and terminals

Questions:

- What had to become cheap or fast enough before interactive computing worked?
- Why did early terminals look like teletypes?
- How did line speed shape command languages and interfaces?
- What hardware makes mutually independent users safe enough to share one machine?

Completed first treatments:

- [x] [`docs/interaction/why-terminals-were-teletypes.md`](docs/interaction/why-terminals-were-teletypes.md)
- [x] [`case-studies/ctss/from-batch-to-conversation.md`](case-studies/ctss/from-batch-to-conversation.md)
- [x] [`experiments/tty-budget/`](experiments/tty-budget/)
- [x] [`experiments/time-sharing/`](experiments/time-sharing/)

Still deepen with:

- full Model 33 mechanism/interface documentation;
- Bell 103/modem lineage;
- CTSS scheduler and swapping detail;
- Multics as a major case study;
- early display terminals;
- line editors versus full-screen editors;
- terminal escape sequences and VT-series standards.

## M9 — Minicomputers, buses, bootstraps, and microprocessors

Questions:

- Which constraints disappear when a computer becomes physically smaller?
- Which new constraints appear because memory and I/O remain expensive?
- Why did buses, memory maps, and peripheral ecosystems matter so much?
- How do you load software before enough software exists to understand the boot device?

Completed first treatment:

- [x] [`docs/interaction/why-booting-started-with-switches.md`](docs/interaction/why-booting-started-with-switches.md) — PDP-8 front-panel loading, RIM/BIN loader chain, octal/operator ergonomics, and bootstrap capability amplification.
- [x] [`experiments/bootstrap-chain/`](experiments/bootstrap-chain/) — conceptual staged loader.

Still deepen with:

- PDP-8 bus/peripheral ecosystem;
- PDP-11 UNIBUS;
- core-to-ROM bootstrap transition;
- DECtape/disk boot ROMs;
- Intel 4004/8008/8080;
- MOS 6502;
- Z80;
- early hobbyist systems;
- why the 6502 could be sold so cheaply;
- memory maps and peripheral registers as architecture.

## M10 — Standards that fossilized into architecture ✅ first field set

Questions:

- Which historical accidents became compatibility requirements?
- When does installed base beat technical elegance?
- How do character encodings, byte order, buses, file formats, and protocols become geology inside later systems?

Completed first treatments:

- [x] [`docs/interaction/why-eighty-columns-survived.md`](docs/interaction/why-eighty-columns-survived.md) — physical card width becoming source/file conventions.
- [x] [`docs/architecture/why-eight-bit-byte.md`](docs/architecture/why-eight-bit-byte.md) — byte width as negotiated architecture/standards outcome.
- [x] [`docs/standards/why-text-is-full-of-device-fossils.md`](docs/standards/why-text-is-full-of-device-fossils.md) — ASCII controls, CR/LF, TELNET NVT, EBCDIC, and installed-base translation.
- [x] [`docs/architecture/why-byte-order-became-a-holy-war.md`](docs/architecture/why-byte-order-became-a-holy-war.md) — PDP-11, IBM big-endian lineage, Cohen's terminology, and Internet canonical order.
- [x] [`experiments/text-fossils/`](experiments/text-fossils/)
- [x] [`experiments/endianness/`](experiments/endianness/)

Still deepen with:

- original ASCII committee records and competing codes;
- original System/360 EBCDIC/design documentation;
- terminal control conventions and ANSI escape sequences;
- little/big-endian implementation rationale in more machine families;
- x86 compatibility layers;
- legacy disk sector sizes and CHS/LBA transitions;
- bus compatibility;
- serial/modem conventions;
- file-format magic numbers and binary serialization fossils.

## M11 — Recurring constraints

A cross-era track should connect early computing to present systems without pretending the technologies are identical.

Themes:

- memory bandwidth and locality;
- serial versus random access;
- energy per operation;
- I/O bottlenecks;
- human waiting versus machine waiting;
- capital cost versus utilization;
- compatibility as a design constraint;
- specialized accelerators;
- remote access and centralized compute;
- buffering between mismatched timescales;
- statistical multiplexing and contention;
- physical phenomena hidden beneath stable abstractions;
- canonical serialization at system boundaries;
- background maintenance required to preserve apparently static state.

The historical payoff is not “everything repeats.” It is learning to recognize when an old **class of constraint** has returned in a new physical form.

## Definition of done for a substantial article

An article is ready when it includes:

1. a clearly stated historical question;
2. period constraints;
3. cited evidence near the claims it supports;
4. a distinction between documented fact and reconstruction;
5. at least one rejected alternative or tradeoff;
6. a short “what this teaches us” section;
7. references suitable for further reading;
8. ideally, an experiment or reproducible exercise;
9. source-type/caveat notes when a key source is corporate, oral, retrospective, promotional, reconstructed, or a modern descendant document;
10. explicit credit when preservation, manufacturing, operating, standards, or clerical labor materially enables the story.

## Definition of done for an experiment

A historical-engineering experiment is ready when:

1. it runs from the repository with documented commands;
2. its assumptions are explicit;
3. its default parameters are identified as historical or hypothetical;
4. its output exposes a concrete constraint;
5. its README says what the model cannot prove;
6. it is not presented as a historical emulator unless it reproduces the documented machine closely enough to justify that label;
7. CI executes its default non-interactive path.
