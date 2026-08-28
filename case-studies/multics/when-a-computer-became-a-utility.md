# When a Computer Became a Utility: Multics

CTSS showed that many people could interact with one large computer.

Multics asked a more ambitious question:

> What if computing were operated like a public utility — continuously available, remotely accessible, shared, protected, and able to grow without forcing users to reorganize everything?

That framing is not a modern analogy imposed afterward.

In 1964, Fernando Corbató's Multics Design Notebook explicitly listed the long-range goal of operating a **computer utility** continuously, 7 days a week and 365 days a year, in a manner compared to telephone and power services.[^design-notebook]

The 1965 overview repeated the goal: a system running continuously and reliably while serving remote interactive users, absentee jobs, multiple languages, shared information, and a wide range of hardware configurations.[^multics-overview]

## CTSS solved interaction; Multics tried to solve permanence

See [`../ctss/from-batch-to-conversation.md`](../ctss/from-batch-to-conversation.md).

CTSS made interactive work practical enough to transform programming practice.

Multics tried to make interactive shared computing into **infrastructure**.

That requires more than time slicing.

A utility has to answer:

- How does one user's program avoid corrupting another user's data?
- How do programs share code safely?
- How does storage outlive processes?
- How can the system grow while running?
- How are failures contained?
- How does a user name information without knowing its physical location?
- How can subsystems be protected without making every call expensive and alien?

Those questions force operating-system ideas into hardware architecture.

## Segmentation made named program structure visible to hardware

Multics used segmented addressing.

Instead of treating a process as one flat anonymous array of words, programs could refer to separately protected and shareable segments.

The 1965 system-design papers describe a virtual-memory architecture combining **segmentation and paging**.[^multics-overview][^multics-system-design]

Conceptually:

```text
process
  |
  +-- segment: procedure A
  +-- segment: procedure B
  +-- segment: data table
  +-- segment: shared library
  +-- segment: user file mapping
```

A segment is closer to a logical object than a mere range of addresses.

### Reconstruction

This creates an opportunity to align:

- protection;
- sharing;
- naming;
- dynamic linking;
- memory management.

The cost is architectural complexity: translation, descriptors, protection metadata, and more complicated fault handling.

## Paging solved a different problem

Segmentation answers:

> What logical object is this address part of?

Paging answers:

> Which pieces of that object are physically resident right now?

Combining them lets a logically large segment occupy physical memory only where needed.

The result is powerful but not simple.

A reference may require:

```text
segment selection
-> access validation
-> page mapping
-> residency check
-> possible page fault
-> physical memory access
```

The abstraction “address a variable” has become a collaboration between compiler, linker, OS, hardware tables, disk, and protection logic.

## Dynamic linking moved work from build time to use time

The original Multics overview highlighted dynamic linking of segment cross-references at execution time.[^multics-overview]

Later Multics documentation describes symbolic links being resolved when first referenced, after which subsequent calls can use a process-specific pointer.[^multics-exec]

This is one of those ideas that feels ordinary only because descendants are everywhere.

A program does not need every dependency permanently fixed before execution.

Instead:

```text
symbolic reference
-> first use
-> linker resolves target
-> process linkage updated
-> later calls reuse resolution
```

That helps a large shared system evolve independently in pieces.

## Protection rings made privilege a structured gradient

A simple protected system can divide the world into:

```text
kernel
user
```

Multics developed a richer ring model.

Schroeder and Saltzer's 1972 paper describes concentric rings of decreasing privilege associated with computation, with hardware validation of cross-ring references and controlled calls.[^protection-rings]

The important design goal was not “more ring numbers.”

It was:

> let protected subsystems be called with procedure-like mechanisms rather than forcing every boundary crossing through one giant supervisor interface.

That matters for a utility containing many independently protected services.

## A file system becomes part of the machine's social architecture

The 1965 papers envisioned a reliable internal file system supporting automatic management of secondary storage, backup, retrieval, and selective sharing.[^multics-overview]

In batch systems, storage often looks like named datasets managed through job-control conventions.

In a utility, persistent information is part of daily interactive life.

Users need:

- personal files;
- shared project files;
- protected system files;
- directories;
- access control;
- backup;
- long-lived names.

The file system is therefore not merely an I/O library.

It is a way of organizing a community sharing one machine.

## Continuous operation changes maintenance philosophy

Corbató's 1964 design notes explicitly compared desired availability to power and telephone service and stated that failures should be infrequent and short.[^design-notebook]

That is a different expectation from a machine that runs one scheduled batch and can be stopped between jobs.

A utility pushes designers toward:

- online maintenance;
- fault isolation;
- recovery;
- configuration flexibility;
- persistent user state;
- controlled system evolution.

The machine is no longer merely an instrument.

It becomes a service people organize their work around.

## The hardware was specialized because the abstractions were ambitious

Multics ran on machines modified specifically for its architecture.

The GE 645 and later Honeywell systems supported features needed for segmentation, paging, protection, and controlled execution.

This is worth emphasizing because modern software culture sometimes assumes operating systems should be portable abstractions independent of hardware.

Multics represents another tradition:

> if the operating-system model is important enough, build hardware that makes it efficient and enforceable.

The tradeoff is obvious: specialized hardware increases cost and narrows the compatible machine family.

## Not everything in the 1965 design survived unchanged

The Multics History Project explicitly warns that the 1965 papers described what the team intended to build, not always exactly what later Multics became.[^multics-papers]

This is historiographically important.

Design documents are evidence of goals.

They are not automatically evidence of final implementation.

A good history therefore needs both:

```text
early design intent
+ later implementation evidence
```

The gap between them is often where the most interesting engineering decisions live.

## “Computer utility” was also a social claim

A utility changes who computing is for.

If access is remote and interactive, users no longer have to organize their lives around card-deck submission windows.

If files persist online, the system can become a place where work accumulates.

If many users share software and information, the machine becomes a community environment.

This is why the Multics project discussed not only processors and paging but the social implications of accessible computing as part of its 1965 presentation set.[^multics-fjcc]

## Why this matters to later systems

Many Multics ideas have descendants in later operating systems, though lineage should be traced carefully rather than claimed by vague resemblance.

Themes that became durable include:

- virtual memory;
- protection domains;
- dynamic linking;
- hierarchical file systems;
- persistent interactive computing;
- least-privilege thinking;
- online services;
- hardware-supported protection.

Some later systems simplified Multics deliberately because its integrated ambition was expensive.

That simplification is itself part of the history.

## Experiment

See [`../../experiments/utility-sharing/`](../../experiments/utility-sharing/).

The experiment models a shared interactive service with:

- user sessions;
- protected objects;
- shared procedures;
- page residency;
- synthetic faults and recovery windows.

It compares a fragile single-user mental model with a utility-style model where isolation and sharing are explicit.

It is not a Multics emulator and does not reproduce GE 645 timing.

## What this teaches us

Multics makes a major historical shift visible:

> computing stops being merely a machine that runs jobs and becomes an environment expected to remain available while many people trust it with persistent work.

That expectation forces architecture into domains that can be easy to forget:

- protection;
- naming;
- recovery;
- sharing;
- storage management;
- remote access;
- hardware/software co-design.

The modern idea that “the computer is just there” is not natural.

A great deal of machinery had to be invented before shared computing could feel like infrastructure.

## References

[^design-notebook]: F. J. Corbató, *Multics Design Notebook, Section I: Introduction*, 30 November 1964, preserved by the Multics History Project, https://multicians.org/mdn-intro.html
[^multics-overview]: F. J. Corbató and V. A. Vyssotsky, “Introduction and Overview of the Multics System,” 1965 Fall Joint Computer Conference, https://multicians.org/fjcc1.html
[^multics-system-design]: E. L. Glaser, J. F. Couleur, and G. A. Oliver, “System Design of a Computer for Time-Sharing Applications,” 1965, https://multicians.org/fjcc2.html
[^multics-exec]: Multics History Project, “Multics Execution Environment,” technical preservation/synthesis drawing on system documentation, https://multicians.org/exec-env.html
[^protection-rings]: Michael D. Schroeder and Jerome H. Saltzer, “A Hardware Architecture for Implementing Protection Rings,” 1972, https://multicians.org/protection.html
[^multics-papers]: Multics History Project, “Multics Technical Papers Online,” preservation note on the 1965 papers, https://multicians.org/papers.html
[^multics-fjcc]: Multics History Project, “1965 Fall Joint Computer Conference Papers,” https://multicians.org/fjcc.html

## Preservation note

The Multics History Project is itself essential infrastructure for this topic. Its maintainers have preserved papers, manuals, source material, recollections, and corrections that make it possible to distinguish original goals from later implementation. Cite original papers where possible, and credit the preservation chain that keeps them accessible.
