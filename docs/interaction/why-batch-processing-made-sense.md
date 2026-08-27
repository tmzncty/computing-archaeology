# Why Did Batch Processing Make Sense?

To a modern user, early batch computing can look almost deliberately hostile.

You prepare a deck of punched cards. Someone carries it away. You do not sit at the machine. Hours later, perhaps the next day, paper output comes back. A typo near the beginning may mean another trip through the queue.

From the perspective of an interactive terminal, the obvious question is:

> Why did computer centers tolerate such a terrible user experience?

But that question silently assumes that **the user's waiting time was the most expensive resource**.

In many 1950s computer installations, it was not.

A better question is:

> **How do you keep an extremely expensive computer doing useful work when programmers, cards, printers, tapes, setup procedures, and mechanical I/O all run on much slower human or electromechanical time scales?**

Under that constraint, batch processing begins to look less like cruelty and more like production engineering.

## The scarce resource was the installed machine

Early electronic computers were capital equipment. A site might have one central machine serving many programmers and departments.

When that machine sat idle while a programmer mounted media, studied a console, loaded translators, corrected operating mistakes, or decided what to do next, an expensive shared resource was doing nothing.

Robert L. Patrick, who worked on early IBM 704 operating-system practice at General Motors Research Laboratories and North American Aviation, later described the problem bluntly: in 1954 the normal pattern was often **programmer present, personally operating the console**. Programmers varied in operating skill, and while they were operating they were not programming.[^patrick-conception]

The problem was therefore both economic and organizational:

```text
scarce programmer
        +
scarce mainframe
        +
slow manual setup
        =
poor total throughput
```

Batch systems tried to separate these resources so each could spend more time on its specialized work.

## “Batch” is a production-line idea

Patrick's 2006 Computer History Museum oral history describes his thinking in unusually explicit terms. He says he approached computer operations using ideas from production control and Gantt-style scheduling: gather independent jobs, standardize their presentation, and move them through a controlled production process.[^patrick-oral]

The jobs were not necessarily related mathematically.

The batch was a **logistical unit**.

A collection of programs could be assembled onto input tape, processed one after another at machine speed, and have their output collected for later printing. The point was to remove as many human pauses as possible between jobs.

That is an important distinction:

> batch processing does not mean “do one giant calculation.”

It means:

> **organize many independent jobs so the machine can transition among them automatically or through standardized operator actions.**

## A 1955 workflow: cards become tapes, then computation, then paper

Patrick's oral history gives a concrete North American Aviation workflow from 1955.[^patrick-oral]

A programmer's card deck did not necessarily go directly into the mainframe.

Instead, the pipeline could look roughly like this:

```text
programmer's punched cards
        ↓ messenger
card-to-tape operation
        ↓
input tape containing many jobs
        ↓
IBM 704 mainframe
        ↓
output tape
        ↓
tape-to-print operation
        ↓
printed output + original deck
        ↓ messenger
programmer's desk
```

The mainframe's input phase converted the incoming representation and prepared jobs. Jobs then executed sequentially. Output accumulated on tape. A later phase converted and printed it away from the central computation.[^patrick-oral]

The mainframe was therefore insulated from much of the slow mechanical card and printer handling.

That is the first major reason batch made sense:

> **move slow peripherals off the critical path of expensive computation.**

## Offline I/O was not an inconvenience bolted onto the machine

A card reader and a line printer are mechanical devices. Their throughput and handling requirements can be painfully slow compared with electronic arithmetic.

If the central computer must wait directly for every card and every printed line, its expensive electronics inherit the speed of the peripheral.

Magnetic tape provides a buffer between worlds:

```text
slow cards → tape   [performed separately]
fast-ish tape → CPU [mainframe phase]
CPU → tape          [mainframe phase]
tape → slow printer [performed separately]
```

The machine room has effectively invented a **pipeline**.

Different equipment can work concurrently on different batches:

- one batch can be converted from cards to tape;
- another can be executing on the mainframe;
- a third can be printing.

The whole installation, not only the CPU, becomes the unit being optimized.

## Professional operators change the economics

Batch operation also separated programming from machine operation.

Patrick recalled that with standardized input formats, deck setup, calling sequences, and recovery procedures, operators could process batches without needing to understand the mathematical purpose of every program.[^patrick-oral]

This matters because a programmer and an operator optimize different things.

A programmer wants to:

- design algorithms;
- write and debug code;
- interpret results;
- prepare the next run.

An operator wants to:

- keep equipment supplied;
- mount tapes;
- recover from common faults;
- follow standard procedures;
- maintain job flow;
- maximize usable machine time.

Making every programmer become a part-time console operator wastes programming expertise and creates inconsistent operational practice.

Batch processing therefore contributed to the emergence of a more specialized computing workforce.

## Standardization is what makes programmer-absent operation possible

A machine cannot automatically process arbitrary piles of cards unless there is a convention for telling jobs apart and describing what each job needs.

Batch processing therefore creates pressure for standardized control information.

The exact mechanisms differed across systems, but the pattern becomes familiar:

```text
job begins
identify program / translator
specify input
specify output
request resources
run
handle normal termination or failure
advance to next job
```

Later job-control languages make this structure explicit. Earlier systems could embody it in card formats, calling sequences, monitor conventions, tapes, and operator procedures.

The conceptual move is important:

> **the computer center needs metadata about work, not only the work itself.**

That metadata lets a monitor or operator decide what to do without asking the programmer at every step.

## The GM-NAA I/O system: keep jobs moving

The General Motors / North American Aviation I/O system for the IBM 704 is often cited as an early operating system.

Priority terminology around “first operating system” is messy, so this repository avoids treating that label as the main historical point.

What matters here is the operational objective.

Patrick's retrospective says the system entered production in 1956 and was designed to increase the number of jobs an installed 704 could process. It automated repeated input/output and job-transition work and allowed binary, assembly, and later FORTRAN jobs to be mixed in an input stream.[^patrick-conception]

Patrick contrasts short, scheduled programmer-operated checkout slots with the later system's ability to process many short test jobs automatically — in his account, as many as **60 test jobs per hour**, depending on test length.[^patrick-conception]

That number comes from a participant's retrospective and should not be universalized to all 704 installations. Its value is that it reveals the metric the designers cared about:

> **jobs per hour, not merely arithmetic operations per second.**

## A hung job must not capture the machine forever

Batch processing introduces a new danger.

If no programmer is standing at the console and one job loops forever, the entire queue can stop.

That creates pressure for another class of system function:

- detect abnormal conditions;
- dump or terminate a failing job;
- protect the monitor from user code;
- account for resources;
- continue with the next job.

Patrick's 1955 account describes a standard button sequence used to dump an offending job after a hang or system problem and restart processing from the input tape.[^patrick-oral]

Later systems increasingly automate and formalize this kind of control.

This is one route by which operating systems become necessary: **once users are absent, the machine needs mechanisms that perform some of the coordination a present human used to provide.**

## Turnaround got worse so throughput could get better

Here is the central tradeoff.

Batching can improve:

```text
machine utilization
jobs per day
operator consistency
peripheral overlap
translator reuse
```

while making this worse:

```text
individual interactive feedback latency
```

Those metrics are not the same.

Suppose ten programmers each need a 30-second test.

### Direct console model

If each programmer consumes five minutes of setup, explanation, media handling, and exit time around the 30-second run:

```text
useful compute = 10 × 30 s = 300 s
setup overhead = 10 × 300 s = 3000 s
```

Only a small fraction of central-machine occupancy is useful computation.

### Batch model

If preparation happens away from the machine and the central system pays one larger batch setup plus small automated transitions, useful computation can occupy a much greater fraction of central-machine time.

These numbers are illustrative; they are not measurements of the IBM 704.

The companion experiment in [`../../experiments/batch-economics/`](../../experiments/batch-economics/) lets the user vary these costs.

## Why this can still feel awful to the programmer

Throughput optimization has a human cost.

Interactive debugging is a feedback loop:

```text
idea → edit → run → observe → edit
```

Batch processing stretches the middle of that loop:

```text
idea
  ↓
prepare deck
  ↓
submit
  ↓
queue
  ↓
run
  ↓
print
  ↓
return output
  ↓
observe
```

If one cycle takes hours, the programmer gets far fewer experimental iterations per day.

So batch does not “solve computing.”

It solves **machine utilization under one economic regime** while making interactive thought increasingly frustrating.

That frustration becomes historically productive.

## Time-sharing attacks a different objective function

When memories became larger, processors faster, interrupt/control mechanisms better, and communications terminals practical, another question became increasingly attractive:

> Can we preserve high machine utilization while giving many users the illusion of immediate access?

Time-sharing does not simply replace batch because someone finally discovers that waiting is unpleasant.

It changes the allocation strategy.

Batch says:

> collect work and minimize gaps between jobs.

Time-sharing says:

> switch among active users quickly enough that human think time can overlap and interactive response remains acceptable.

Both are responses to the fact that human and machine time scales differ.

The economics and available hardware determine which kind of multiplexing is attractive.

## Batch processing created durable concepts

Even after interactive systems became ordinary, batch never disappeared.

Modern computing is full of descendants:

- build farms;
- render queues;
- HPC schedulers;
- ETL pipelines;
- CI jobs;
- cloud batch services;
- GPU training queues;
- print spooling;
- background data processing.

The interfaces are better and the machines vastly different, but the scheduling question survives:

> **When immediate human feedback is unnecessary, can work be queued, standardized, and packed together to improve utilization?**

This is why calling batch processing merely “primitive UX” misses its historical logic.

## The missing user was a design feature

A batch system deliberately removes the programmer from the critical machine-time loop.

That sounds anti-user only if we treat physical presence as the natural form of computing.

Under the economics of a shared 1950s mainframe, the opposite could be true:

```text
programmer absent from machine
→ professional operator handles routine procedure
→ jobs standardized
→ slow I/O moved offline
→ monitor advances through work
→ CPU spends less time waiting for people
```

The price is delayed feedback.

The benefit is much higher system throughput.

Neither side of that tradeoff should be hidden.

## What this teaches us

Batch processing is a reminder that “performance” is always a choice of metric.

If performance means **minimum response time for one person**, batch looks terrible.

If performance means **maximum useful jobs through one expensive installation per day**, batch can be excellent.

It also shows that operating systems grew partly out of logistics:

- who owns the machine now;
- what job comes next;
- how input is staged;
- where output goes;
- what happens when a job fails;
- how expensive devices remain occupied with useful work.

Those questions are still operating-system questions.

The old card queue is therefore not a bizarre prehistory of “real” interactive computing.

It is one of the places where computing learned to **schedule scarcity**.

## References

[^patrick-conception]: Robert L. Patrick, “Operating Systems at Conception,” Computer History Museum Software Preservation Group, December 2008, https://softwarepreservation.computerhistory.org/os/gm.html
[^patrick-oral]: Robert L. Patrick, oral history conducted by Gardner Hendrie, Computer History Museum, 22 February 2006, CHM Reference X3804.2007, especially discussion of GM-NAA batch operations and the 1955 North American Aviation workflow, https://archive.computerhistory.org/resources/text/Oral_History/Patrick_Robert/Patrick_Robert.oral_history_transcript.2006.102657941.pdf

## Further reading

- Robert L. Patrick and Richard K. Van Vranken, “The Direct Couple for the IBM 7090,” Computer History Museum Software Preservation Group, 2009, https://softwarepreservation.computerhistory.org/os/dc.html
- Robert L. Patrick, “General Motors/North American Monitor for the IBM 704 Computer,” RAND Paper P-7316, 1987.
- Computer History Museum Software Preservation Group, operating-system preservation material, https://softwarepreservation.computerhistory.org/

## Source note

Patrick's accounts are unusually valuable because he participated directly in the systems described and explains operational motives rarely visible in hardware specifications. They are nevertheless retrospective oral/history accounts written decades after the events. Exact performance and priority claims should be corroborated with contemporary records where available. This article therefore uses Patrick primarily to reconstruct workflow and design objectives rather than to declare a single uncontested “first operating system.”
