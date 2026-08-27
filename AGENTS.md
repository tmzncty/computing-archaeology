# AGENTS.md

This repository is a historical-engineering project, not a generic encyclopedia. Contributors and coding agents should preserve that distinction.

## Core objective

Reconstruct **why a computing technology made sense under the constraints of its own period**.

Do not merely produce timelines, biographies, or lists of specifications. A good contribution connects documented history to concrete constraints: manufacturing, component behavior, cost, labor, interfaces, reliability, power, memory, communications, institutional demand, installed base, or maintenance.

## Three-layer rule

Every historical reconstruction must keep these layers distinguishable:

### 1. Historical record

Claims directly supported by primary documents, archival records, museum collections, patents, manuals, oral histories, or serious scholarship.

Use explicit citations.

### 2. Engineering reconstruction

Reasoning from known constraints to explain why a design may have been attractive or why an alternative may have been difficult.

Mark this as reconstruction, inference, or a model. Never phrase an inference as though a historical actor explicitly stated it unless a source shows that they did.

### 3. Experiment

A simulator, replica, program, model, calculation, FPGA implementation, or physical demonstration.

Experiments test mechanisms and constraints. They do **not** prove historical intent.

## Source discipline

Prefer sources in this order when available:

1. contemporary primary documents;
2. archival or museum material with provenance;
3. peer-reviewed history of computing and scholarly books;
4. institutional histories and oral histories;
5. reliable technical retrospectives;
6. tertiary summaries for navigation only.

Corporate histories are useful but interested sources. Memoirs and oral histories are evidence, not omniscient narration. Wikipedia may help locate references but should not normally be the final citation for a central claim.

For unstable web pages, prefer an archival copy or record a title, institution, author if known, and access path sufficient to recover the source.

## Citation style

Markdown footnotes are preferred for long-form articles:

```markdown
Babbage considered several number bases before settling on decimal.[^chm-babbage-engines]

[^chm-babbage-engines]: Computer History Museum, “The Engines,” Babbage Engine exhibit, https://www.computerhistory.org/babbage/engines/
```

Citations should appear near the claims they support. Do not use one giant reference list to support an entire page implicitly.

## Writing style

Use clear technical prose. Avoid false drama and inevitability language.

Prefer:

> Given a serial delay-line memory, access time depended on when the desired word reached the read point.

Avoid:

> Humanity inevitably realized that random-access memory was the future.

Prefer “one important factor was…” over monocausal claims such as “X happened because Y” unless the evidence warrants it.

Do not modernize historical actors' vocabulary silently. If using a modern term such as “CPU,” “RAM,” “microcode,” or “parallelism” to illuminate an older design, make clear when the original source used different language.

## Counterfactuals

Counterfactual reasoning is welcome when disciplined.

A useful counterfactual specifies:

- a date or technological envelope;
- available components and manufacturing techniques;
- cost/reliability assumptions;
- the task to be solved;
- what knowledge is allowed;
- what is intentionally held back to avoid hindsight.

Bad counterfactual:

> Why didn’t Babbage just build a transistor computer?

Useful counterfactual:

> If multiplication requires substantially more mechanical state and motion than addition, what tabulation methods become attractive in a gear-based machine?

## Experiments

Experiments should expose constraints rather than merely reproduce appearances.

Good experiment:

- a delay-line memory simulator that makes the user wait for the desired word to circulate.

Weak experiment:

- a modern text box with a sepia skin labeled “1950 computer.”

When implementing experiments, add a short README explaining:

- historical question;
- model assumptions;
- simplifications;
- what the experiment demonstrates;
- what it cannot establish historically.

## Repository organization

Use these broad locations:

- `docs/methodology/` — historiography and reconstruction method;
- `docs/mechanical/` — mechanical calculation;
- `docs/electromechanical/` — relay and switching systems;
- `docs/memory/` — memory and storage technologies;
- `docs/interaction/` — punched media, batch, terminals, interfaces;
- `docs/architecture/` — words, bytes, instruction formats, stored programs;
- `case-studies/` — machine-, institution-, or person-centered deep dives;
- `experiments/` — runnable or buildable demonstrations.

Create new top-level categories only when the material clearly outgrows these.

## Historical caution points

Treat the following as claims requiring care rather than folklore:

- “first computer”;
- “first programmer”;
- “first stored-program computer”;
- “first remote computer”; 
- “the bug was named after Grace Hopper's moth”;
- “von Neumann invented the stored-program architecture”;
- “the byte has always meant 8 bits”;
- “binary was obviously superior to decimal”;
- “one inventor single-handedly created” a complex system.

Prefer precise formulations that identify what kind of “first” is meant.

## AI-assisted contributions

AI assistance is allowed and is part of this repository's initial workflow. It must not weaken source discipline.

For AI-generated or AI-edited historical prose:

- verify names, dates, machine specifications, quotations, and priority claims;
- follow cited sources rather than the model's memory when they conflict;
- never invent page numbers, archival identifiers, quotations, or bibliography entries;
- label uncertainty instead of filling gaps with plausible prose;
- keep inference visibly separate from evidence.

Initial research structure and drafting assistance for the repository was provided by **ChatGPT (GPT-5.6 Sol), OpenAI**.

## Pull requests

A substantial historical PR should say:

- what question it answers;
- what primary or authoritative sources it adds;
- which statements are reconstruction rather than documented intent;
- whether an experiment is included;
- known uncertainties or disputes.

The standard is not “sounds convincing.” The standard is **traceable evidence plus honest reconstruction**.
