# Roadmap

This roadmap is organized by **historical problems**, not by a single parade of machines. Chronology still matters, but the project should repeatedly stop and ask what problem made a technology sensible in its own time.

A checked item means the repository now has a defensible first treatment. It does **not** mean the historical topic is exhausted.

## M0 — Method and first excavations ✅

Goal: establish a repeatable way to separate evidence, reconstruction, and experiment.

- [x] Define the constraint-first method.
- [x] Write a Babbage / finite-difference case study.
- [x] Write an electromechanical relay case study.
- [x] Survey early memory as a design problem.
- [x] Write a punched-media interaction case study.
- [x] Start an 8-bit-byte case study using IBM Stretch material.
- [x] Add a source ledger with stable archival links where possible.
- [x] Add runnable experiments with explicit model limitations.
- [x] Add source/archival acknowledgements and AI-assistance disclosure.
- [x] Demonstrate the method across mechanical, electromechanical, electronic, memory, interaction, and architecture topics.

The foundation now supports deeper excavations without changing the method every time.

## M1 — Mechanical computation

Questions:

- What does it cost, mechanically, to carry a digit?
- Why can addition be dramatically easier than multiplication?
- Why did decimal survive inside machines that could in principle use other radices?
- How do tolerances, backlash, inertia, and gearing alter what an “algorithm” looks like?

Completed first treatments:

- [x] [`docs/mechanical/why-difference-engine.md`](docs/mechanical/why-difference-engine.md) — finite differences as a way to turn general tabulation into repeated addition.
- [x] [`docs/mechanical/why-carry-is-a-machine-problem.md`](docs/mechanical/why-carry-is-a-machine-problem.md) — Pascaline `sautoir`, long carry chains, complement subtraction, radix tradeoffs, and `9999 + 1` as a stress case.
- [x] [`experiments/finite-differences/`](experiments/finite-differences/) — addition-versus-multiplication cost model.
- [x] [`experiments/carry-propagation/`](experiments/carry-propagation/) — radix, digit-count, carry-frequency, and synthetic mechanical-cost explorer.

Still deepen with:

- Pascaline mechanism drawings and surviving-object measurements;
- stepped reckoner / Leibniz wheel;
- Babbage Analytical Engine carry and sequencing mechanisms;
- Scheutz engines;
- desk adding machines;
- Curta as a late mechanical endpoint;
- gear backlash and tolerance propagation;
- a virtual gear train with configurable error and wear.

## M2 — Punched media and information machinery

Questions:

- Why did holes become a durable representation of information?
- Why were census, accounting, railway, and office workflows so important to computing?
- How did card dimensions and column counts become software-visible constraints?
- What changes when programs are physical decks that can be dropped, sorted, duplicated, and queued?

Existing first treatment:

- [x] [`docs/interaction/why-programs-were-holes.md`](docs/interaction/why-programs-were-holes.md)

Still deepen with:

- Jacquard control media;
- Hollerith census machinery;
- IBM punched-card ecosystems;
- dedicated paper-tape history;
- readers, sorters, punches, reproducing punches, tabulators;
- card-oriented programming practice;
- card dimensions and 80-column path dependence.

Planned experiments:

- virtual card punch/reader;
- deck-based batch job runner;
- card sorting exercise that performs a real data-processing task.

## M3 — Relays, switching, and the telephone inheritance

Questions:

- Why did telephone switching supply useful logic components?
- What are the real costs of relay logic: speed, contact bounce, wear, coil power, fan-out, wiring?
- How did remote teleprinter access emerge before “online computing” became ordinary?

Completed first treatments:

- [x] [`docs/electromechanical/why-relays.md`](docs/electromechanical/why-relays.md) — telephone inheritance and relay calculation.
- [x] [`docs/electromechanical/why-one-switch-can-look-like-many.md`](docs/electromechanical/why-one-switch-can-look-like-many.md) — contact bounce as the gap between mechanical transition and Boolean event.
- [x] [`experiments/relay-bounce/`](experiments/relay-bounce/) — synthetic bounce waveform and three logical interpretations.

Still deepen with:

- George Stibitz and Bell Labs primary reports;
- Konrad Zuse's electromechanical machines;
- Harvard Mark I;
- relay adders and carry timing;
- relay logic notation;
- adjustment, contact materials, maintenance, and field practice;
- system-scale relay-versus-electronic timing comparison.

## M4 — Vacuum tubes and electronic speed

Questions:

- Why accept heat, power consumption, and component failure for electronic switching?
- How much of the system problem moved from logic into memory, power, cooling, and maintenance?
- Why was rewiring an acceptable programming method for some early machines?

Completed first treatments:

- [x] [`docs/electronic/why-vacuum-tubes.md`](docs/electronic/why-vacuum-tubes.md) — electronic speed versus heat, power, maintenance, and reliability engineering.
- [x] [`case-studies/eniac/from-wiring-to-stored-program.md`](case-studies/eniac/from-wiring-to-stored-program.md) — ENIAC programming, 1947–48 coded-control modification, EDVAC historiography, and Manchester comparison.
- [x] [`experiments/reliability-throughput/`](experiments/reliability-throughput/) — availability versus useful throughput.

Still deepen with:

- Colossus primary wartime/reconstruction documentation;
- ENIAC maintenance records and failure logs;
- full EDVAC documentation and correspondence;
- explicit relay-versus-electronic system timing.

## M5 — The memory problem

Early computers did not simply “have RAM.” Designers searched across radically different physical phenomena.

Questions:

- Why can a mercury tube be memory?
- Why can a CRT be memory?
- Why does rotating storage force programmers to think about time and geometry?
- Why did magnetic core become such a dominant compromise?
- When does reading physically alter or destroy the stored state?

Completed first treatments:

- [x] [`docs/memory/why-early-memory-looked-weird.md`](docs/memory/why-early-memory-looked-weird.md) — comparative survey.
- [x] [`docs/memory/why-memory-was-a-tube-of-sound.md`](docs/memory/why-memory-was-a-tube-of-sound.md) — radar-derived acoustic delay lines, recirculation, serial access, thermal control, and temporal addressing.
- [x] [`docs/memory/why-drum-memory-made-programmers-wait.md`](docs/memory/why-drum-memory-made-programmers-wait.md) — IBM 650 drum geometry, next-instruction addresses, and SOAP optimization.
- [x] [`docs/memory/why-core-memory-was-worth-weaving.md`](docs/memory/why-core-memory-was-worth-weaving.md) — coincident-current selection, destructive read/restore, manufacturing labor, and Whirlwind.
- [x] [`experiments/serial-memory/`](experiments/serial-memory/) — single-access-point circulating-memory latency.
- [x] [`experiments/drum-timing/`](experiments/drum-timing/) — rotational instruction-placement model.
- [x] [`experiments/core-memory/`](experiments/core-memory/) — conceptual half-select, coincidence, destructive read, and restore.

Still deepen with:

- Williams–Kilburn storage as a dedicated excavation;
- EDSAC, UNIVAC, SEAC, CSIRAC machine-specific delay-line timing from primary manuals;
- mercury versus wire/magnetostrictive acoustic media;
- core inhibit wiring and full word-oriented plane stacks;
- core production at commercial scale;
- early semiconductor memory;
- destructive-read / refresh comparisons across core, CRT, and later DRAM.

## M6 — Stored programs, words, and instruction formats

Questions:

- Why was a “word” once more fundamental than a byte?
- Why did 18-, 24-, 36-, 48-, and 60-bit machines make sense?
- Why were instruction formats often shaped by the physical memory technology?
- Why did character processing push architectures toward different compromises?

Completed first treatments:

- [x] [`case-studies/eniac/from-wiring-to-stored-program.md`](case-studies/eniac/from-wiring-to-stored-program.md) — why “stored program” is not one uncontested first.
- [x] [`docs/architecture/why-word-lengths-were-weird.md`](docs/architecture/why-word-lengths-were-weird.md) — PDP-1 18-bit, IBM 704 36-bit, CDC 6600 60-bit, and System/360 compatibility pressure.
- [x] [`docs/architecture/why-eight-bit-byte.md`](docs/architecture/why-eight-bit-byte.md) — Stretch byte/word tradeoffs.
- [x] [`experiments/word-packing/`](experiments/word-packing/) — field-packing tradeoff explorer.

Still deepen with:

- Manchester Mark I and EDSAC instruction formats;
- IAS-family diffusion;
- original System/360 architecture/design papers;
- 24- and 48-bit machine families;
- instruction-format tradeoffs beyond packing alone.

## M7 — Batch, operators, and the missing user

Questions:

- Why was direct user interaction once economically irrational?
- What did an operator actually do?
- Why did job queues, JCL-like control, and offline peripherals exist?
- How did machine utilization shape software organization?

Completed first treatments:

- [x] [`docs/interaction/why-batch-processing-made-sense.md`](docs/interaction/why-batch-processing-made-sense.md) — GM/NAA-style workflow, offline I/O, professional operators, throughput versus turnaround.
- [x] [`experiments/batch-economics/`](experiments/batch-economics/) — explicit throughput/utilization model with hypothetical costs.

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
- How did communications line speed shape command languages and interfaces?
- What hardware makes mutually independent users safe enough to share one machine?

Completed first treatments:

- [x] [`docs/interaction/why-terminals-were-teletypes.md`](docs/interaction/why-terminals-were-teletypes.md) — Teletype Model 33, paper tape, ASCII, control-character fossils, modem/telephone inheritance, and line-oriented interaction.
- [x] [`case-studies/ctss/from-batch-to-conversation.md`](case-studies/ctss/from-batch-to-conversation.md) — timer interrupt, protection, relocation, communications buffering, secondary storage, scheduling, and interactive user experience.
- [x] [`experiments/tty-budget/`](experiments/tty-budget/) — 110-baud-style output as human waiting time.
- [x] [`experiments/time-sharing/`](experiments/time-sharing/) — human think-time and short CPU bursts as a multiplexing opportunity.

Still deepen with:

- full Model 33 mechanism and interface documentation;
- Bell 103 and modem lineage;
- ASCII committee records and competing codes;
- CTSS scheduler and swapping from source/manual detail;
- Multics as a next major case study;
- early display terminals;
- line editors versus full-screen editors;
- terminal control standards and escape-sequence fossils.

## M9 — Minicomputers, microprocessors, and the shrinking machine

Questions:

- Which constraints disappear when a computer becomes physically smaller?
- Which new constraints appear because memory and I/O remain expensive?
- Why did buses, memory maps, and peripheral ecosystems matter so much?

Candidate excavations:

- PDP families;
- Intel 4004/8008/8080;
- MOS 6502;
- Z80;
- early hobbyist systems;
- front panels and bootstrap loaders;
- minicomputer buses and modular peripherals.

## M10 — Standards that fossilized into architecture

Questions:

- Which historical accidents became compatibility requirements?
- When does installed base beat technical elegance?
- How do character encodings, buses, file formats, and protocols become “geology” inside later systems?

Candidate excavations:

- ASCII and EBCDIC;
- 8-bit bytes;
- CR/LF and terminal control conventions;
- little versus big endian;
- x86 compatibility layers;
- legacy storage sector sizes;
- bus compatibility;
- modem/serial conventions.

The terminal excavation already provides an early example of the process:

```text
physical carriage / paper feed
-> control character
-> communications convention
-> software expectation
-> terminal emulator fossil
```

## M11 — Recurring constraints

A final cross-era track should connect early computing to present systems without pretending the technologies are identical.

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
- physical phenomena hidden beneath stable abstractions.

The historical payoff is not “everything repeats.” It is learning to recognize when an old **class of constraint** has returned in a new physical form.

## Definition of done for a substantial article

An article is ready when it includes:

1. a clearly stated historical question;
2. period constraints;
3. cited evidence;
4. a distinction between documented fact and reconstruction;
5. at least one rejected alternative or tradeoff;
6. a short “what this teaches us” section;
7. references suitable for further reading;
8. ideally, an experiment or reproducible exercise;
9. source-type/caveat notes when a key source is corporate, oral, retrospective, promotional, or reconstructed;
10. explicit credit when preservation, manufacturing, operating, or clerical labor materially enables the story.

## Definition of done for an experiment

A historical-engineering experiment is ready when:

1. it runs from the repository with documented commands;
2. its assumptions are explicit;
3. its default parameters are identified as historical or hypothetical;
4. its output exposes a concrete constraint;
5. its README says what the model cannot prove;
6. it is not presented as a historical emulator unless it actually reproduces the documented machine closely enough to justify that label;
7. CI executes its default non-interactive path.
