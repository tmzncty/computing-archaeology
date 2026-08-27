# computing-archaeology

> **Computers are not inevitable. They are accumulated engineering decisions.**

`computing-archaeology` is an experimental history of computing: a repository for reconstructing **why computers became what they are** through material constraints, forgotten technologies, institutional choices, failed designs, and small hands-on experiments.

A normal timeline asks:

> What was invented, by whom, and when?

This repository asks a different set of questions:

> What could engineers actually build at the time?  
> Which constraints made one design reasonable and another absurd?  
> Which “obsolete” technologies were once excellent answers to real problems?  
> Which failures, accidents, industries, standards, and habits quietly shaped the machines we inherited?

The goal is not to replace conventional computer history. It is to put **engineering pressure back into history**.

## The method

Every substantial article should distinguish three layers:

1. **Historical record** — what surviving documents, machines, patents, oral histories, museum collections, and scholarship establish.
2. **Engineering reconstruction** — what follows when we reason from the period's available components, costs, speeds, manufacturing limits, interfaces, and operational needs.
3. **Experiment** — a simulation, replica, program, FPGA build, paper exercise, or physical demonstration that lets us test part of the reconstruction.

These layers must not be silently mixed. A plausible reconstruction is not automatically a historical fact.

See [`docs/methodology/constraint-first-history.md`](docs/methodology/constraint-first-history.md).

## Start here

- [`docs/mechanical/why-difference-engine.md`](docs/mechanical/why-difference-engine.md) — why finite differences made mechanical computation tractable.
- [`docs/electromechanical/why-relays.md`](docs/electromechanical/why-relays.md) — how telephone switching hardware became computing machinery.
- [`docs/memory/why-early-memory-looked-weird.md`](docs/memory/why-early-memory-looked-weird.md) — mercury, CRTs, drums, and magnetic cores as answers to the memory problem.
- [`docs/interaction/why-programs-were-holes.md`](docs/interaction/why-programs-were-holes.md) — why punched media fit data processing before keyboards and disks did.
- [`docs/architecture/why-eight-bit-byte.md`](docs/architecture/why-eight-bit-byte.md) — why “byte = 8 bits” is a historical outcome, not a law of nature.
- [`ROADMAP.md`](ROADMAP.md) — the larger excavation plan.

## Questions this project wants to answer

- Why did Babbage choose decimal wheels even though he considered binary?
- Why was repeated addition a useful *architectural* trick?
- Why could telephone relays become logic elements?
- Why did programming spend decades as wiring, switches, cards, and paper tape?
- Why did early main memory use sound waves in mercury?
- Why did CRTs briefly make sense as RAM?
- Why did magnetic drums make programmers care about rotational position?
- Why was magnetic-core memory worth threading by hand?
- Why were early word lengths so strange by modern standards?
- Why did the byte eventually settle at eight bits?
- Why did batch processing precede interactive computing?
- Why did terminals inherit so much from telegraphy and office machinery?
- Why do apparently “new” bottlenecks — memory bandwidth, locality, I/O, power — keep returning?

## What this is not

This is **not** a “great men and great machines” list, and it is not a claim that one technical constraint mechanically determines history. Engineering choices are also shaped by institutions, budgets, labor, standards, military and commercial demand, maintenance practices, available skills, and prior installed systems.

The repository should therefore preserve failed branches and awkward transitional designs, not edit history into a clean road toward the modern PC.

## Sources and citation policy

Historical claims should be cited as close to the claim as practical. Prefer, in roughly this order:

- primary documents, patents, manuals, design memos, correspondence, and contemporary reports;
- museum and archival collections with provenance;
- peer-reviewed history of computing and strong scholarly monographs;
- institutional histories, oral histories, and high-quality technical retrospectives;
- tertiary summaries only as navigation aids, not as the sole support for contentious claims.

A source can be valuable without being neutral. Corporate histories, memoirs, and oral histories should be identified for what they are.

See [`ACKNOWLEDGEMENTS.md`](ACKNOWLEDGEMENTS.md) for the institutions and collections this project currently leans on.

## Authorship and assistance

Repository owner and maintainer: **tmzncty**.

Initial research structure, drafting, and editorial assistance: **ChatGPT (GPT-5.6 Sol), OpenAI**.

AI-assisted text in this repository should be treated like any other secondary synthesis: useful for organizing questions and reconstructing engineering choices, but subject to verification against cited sources. The presence of a citation does not excuse a bad inference.

## Relationship to experiments

A companion experiment can be tiny. Good examples include:

- emulate a decimal carry chain and compare it with binary;
- implement a finite-difference table using only addition;
- build relay logic in a simulator;
- model serial memory latency for a delay line or rotating drum;
- write a card-deck batch runner;
- emulate a teleprinter-style terminal;
- explore historical word lengths and character encodings.

The point is not historical cosplay. The experiment should expose a constraint that prose alone tends to hide.

## Status

This repository is deliberately young. Its first milestone is to establish a defensible method and a set of worked examples before expanding into a full chronological map.

If a page makes you say “why on earth would anyone build it that way?”, that is probably where the excavation should begin.
