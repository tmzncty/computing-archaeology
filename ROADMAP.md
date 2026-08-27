# Roadmap

This roadmap is organized by **historical problems**, not by a single parade of machines. Chronology still matters, but the project should repeatedly stop and ask what problem made a technology sensible in its own time.

## M0 — Method and first excavations

Goal: establish a repeatable way to separate evidence, reconstruction, and experiment.

- [x] Define the constraint-first method.
- [x] Write a Babbage / finite-difference case study.
- [x] Write an electromechanical relay case study.
- [x] Survey early memory as a design problem.
- [x] Write a punched-media interaction case study.
- [x] Start an 8-bit-byte case study using IBM Stretch material.
- [ ] Add a source ledger with stable archival links where possible.
- [ ] Add at least one runnable experiment.

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
- finite-difference engine using addition only;
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

Experiments:

- compare relay and electronic switching latency at system scale;
- patch-panel programming model.

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

Experiments:

- serial-memory latency visualizer;
- optimal instruction placement on a simulated drum;
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

Experiments:

- historical word-size emulator;
- packing text into 6-, 7-, 8-, 9-, and 12-bit character units;
- instruction-format tradeoff explorer.

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

Experiment:

- multi-user batch scheduler where machine time is expensive and human time is cheap.

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
8. ideally, an experiment or reproducible exercise.
