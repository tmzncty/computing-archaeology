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

First-field-set additions:

- [`docs/electronic/why-vacuum-tubes.md`](docs/electronic/why-vacuum-tubes.md)
- [`case-studies/eniac/from-wiring-to-stored-program.md`](case-studies/eniac/from-wiring-to-stored-program.md)
- [`docs/memory/why-drum-memory-made-programmers-wait.md`](docs/memory/why-drum-memory-made-programmers-wait.md)
- [`docs/interaction/why-batch-processing-made-sense.md`](docs/interaction/why-batch-processing-made-sense.md)
- [`docs/architecture/why-word-lengths-were-weird.md`](docs/architecture/why-word-lengths-were-weird.md)
- [`experiments/drum-timing/`](experiments/drum-timing/)
- [`experiments/batch-economics/`](experiments/batch-economics/)
- [`experiments/word-packing/`](experiments/word-packing/)

## M1 — Mechanical computation

Questions:

- What does it cost, mechanically, to carry a digit?
- Why can addition be dramatically easier than multiplication?
- Why did decimal survive inside machines that could in principle use other radices?
- How do tolerances, backlash, inertia, and gearing alter what an “algorithm” looks like?

Candidate excavations:

- Pascaline and stepped reckoners.
- Babbage Difference Engines.
- Babbage Analytical Engine.
- Scheutz difference engines.
- Mechanical adding machines and desk calculators.
- Curta as a late, highly refined mechanical endpoint.

Experiments:

- decimal vs binary carry simulator;
- finite-difference engine using addition only — **initial version exists** in [`experiments/finite-differences/`](experiments/finite-differences/);
- virtual gear train with configurable backlash/error.

## M2 — Punched media and information machinery

Questions:

- Why did holes become a durable representation of information?
- Why were census, accounting, railway, and office workflows so important to computing?
- How did card dimensions and column counts become software-visible constraints?
- What changes when programs are physical decks that can be dropped, sorted, duplicated, and queued?

Candidate excavations:

- Jacquard control media;
- Hollerith census machinery;
- IBM punched-card ecosystems;
- paper tape;
- card readers, sorters, punches, and tabulators;
- card-oriented programming habits.

Existing first treatment:

- [`docs/interaction/why-programs-were-holes.md`](docs/interaction/why-programs-were-holes.md)

Experiments:

- virtual card punch/reader;
- deck-based batch job runner;
- card sorting exercise that performs a nontrivial data-processing task.

## M3 — Relays, switching, and the telephone inheritance

Questions:

- Why did telephone switching supply useful logic components?
- What are the real costs of relay logic: speed, contact bounce, wear, coil power, fan-out, wiring?
- How did remote teleprinter access emerge before “online computing” became ordinary?

Candidate excavations:

- George Stibitz and Bell Labs relay calculators;
- Konrad Zuse's electromechanical work;
- Harvard Mark I;
- relay logic notation and maintenance.

Existing first treatment:

- [`docs/electromechanical/why-relays.md`](docs/electromechanical/why-relays.md)

Experiments:

- relay adder;
- contact-bounce simulator;
- dial-up / teleprinter-style remote calculator mockup.

## M4 — Vacuum tubes and electronic speed

Questions:

- Why accept heat, power consumption, and component failure for electronic switching?
- How much of the system problem moved from logic into memory, power, cooling, and maintenance?
- Why was rewiring an acceptable programming method for some early machines?

Candidate excavations:

- Colossus;
- ENIAC;
- EDVAC debates and stored-program ideas;
- early reliability practices.

Completed first treatments:

- [x] [`docs/electronic/why-vacuum-tubes.md`](docs/electronic/why-vacuum-tubes.md) — electronic speed versus heat, power, maintenance, and reliability engineering.
- [x] [`case-studies/eniac/from-wiring-to-stored-program.md`](case-studies/eniac/from-wiring-to-stored-program.md) — ENIAC programming, 1947–48 coded-control modification, EDVAC historiography, and Manchester comparison.

Still deepen with:

- Colossus primary wartime/reconstruction documentation;
- ENIAC maintenance records and failure logs;
- full EDVAC documentation and correspondence;
- an explicit relay-vs-electronic system-scale timing experiment.

## M5 — The memory problem

This is a major track. Early computers did not simply “have RAM.” Designers searched across radically different physical phenomena.

Questions:

- Why can a mercury tube be memory?
- Why can a CRT be memory?
- Why does rotating storage force programmers to think about time and geometry?
- Why did magnetic core become such a dominant compromise?

Candidate excavations:

- mercury acoustic delay lines;
- Williams–Kilburn tubes;
- magnetic drums;
- electrostatic and capacitor memories;
- magnetic-core memory;
- early semiconductor memory.

Completed first treatments:

- [x] [`docs/memory/why-early-memory-looked-weird.md`](docs/memory/why-early-memory-looked-weird.md) — comparative survey.
- [x] [`docs/memory/why-drum-memory-made-programmers-wait.md`](docs/memory/why-drum-memory-made-programmers-wait.md) — IBM 650 drum geometry, next-instruction addresses, and SOAP optimization.
- [x] [`experiments/drum-timing/`](experiments/drum-timing/) — rotational instruction-placement model.

Still deepen with dedicated excavations for:

- mercury acoustic delay lines;
- Williams–Kilburn storage;
- magnetic-core memory and its manufacturing labor;
- destructive read/refresh;
- early semiconductor memory.

Planned experiments:

- serial-memory latency visualizer;
- destructive-read / refresh models.

## M6 — Stored programs, words, and instruction formats

Questions:

- Why was a “word” once more fundamental than a byte?
- Why did 18-, 24-, 36-, 48-, and 60-bit machines make sense?
- Why were instruction formats often shaped by the physical memory technology?
- Why did character processing push architectures toward different compromises?

Candidate excavations:

- Manchester Baby and Mark I;
- EDSAC;
- IAS-family machines;
- IBM 701/704;
- IBM Stretch;
- DEC and CDC word-oriented machines;
- IBM System/360 and the consolidation of the 8-bit byte.

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
- instruction-format tradeoff explorer beyond packing alone.

## M7 — Batch, operators, and the missing user

Questions:

- Why was direct user interaction once economically irrational?
- What did an operator actually do?
- Why did job queues, JCL-like control, and offline peripherals exist?
- How did machine utilization shape software organization?

Candidate excavations:

- batch processing centers;
- offline card-to-tape workflows;
- operator consoles;
- job control systems.

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

Candidate excavations:

- teleprinters and ASCII;
- CTSS;
- Multics;
- early display terminals;
- modem-connected systems.

Experiments:

- 110-baud shell;
- terminal latency simulator;
- line-oriented editor.

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
- early hobbyist systems.

## M10 — Standards that fossilized into architecture

Questions:

- Which historical accidents became compatibility requirements?
- When does installed base beat technical elegance?
- How do character encodings, buses, file formats, and protocols become “geology” inside later systems?

Candidate excavations:

- ASCII and EBCDIC;
- 8-bit bytes;
- little vs big endian;
- x86 compatibility layers;
- terminal control conventions;
- legacy storage sector sizes.

## M11 — Recurring constraints

A final cross-era track should connect early computing to present systems without pretending the technologies are identical.

Themes:

- memory bandwidth and locality;
- serial vs random access;
- energy per operation;
- I/O bottlenecks;
- human waiting vs machine waiting;
- capital cost vs utilization;
- compatibility as a design constraint;
- specialized accelerators;
- remote access and centralized compute.

The historical payoff is not “everything repeats.” It is learning to recognize when an old class of constraint has returned in a new physical form.

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
9. source-type/caveat notes when a key source is corporate, oral, retrospective, or reconstructed.

## Definition of done for an experiment

A historical-engineering experiment is ready when:

1. it runs from the repository with documented commands;
2. its assumptions are explicit;
3. its default parameters are identified as historical or hypothetical;
4. its output exposes a concrete constraint;
5. its README says what the model cannot prove;
6. it is not presented as a historical emulator unless it actually reproduces the documented machine closely enough to justify that label.
