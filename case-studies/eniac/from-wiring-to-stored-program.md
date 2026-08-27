# ENIAC: From Wiring a Calculation to Coding One

ENIAC is useful precisely because it resists a clean textbook boundary between “calculator” and “modern computer.”

It was electronic and general-purpose, but its original programming model did not look like loading a sequence of instructions from memory. Later, the same physical machine was modified to operate with a much more code-like control scheme.

That makes ENIAC a particularly good archaeological site for the question:

> **What problem did the stored-program idea actually solve?**

The short answer is not merely “programs became easier to store.” The deeper change was that **control itself became information that could be represented compactly, fetched, sequenced, branched around, copied, and reasoned about**.

## Before “software” looked like software

ENIAC was built from functional units: accumulators, a multiplier, divider/square-root unit, function tables, initiating and cycling units, and I/O equipment. Its initial programming method configured the flow of data and control pulses among these units with switches and cables.

The Computer History Museum summarizes the original arrangement as functional units wired together for each problem. A multiplication after an addition could require a physical connection from one unit to another; control was distributed rather than represented as one central stream of instruction words.[^chm-programming]

Photographs of ENIAC staff show plugboards and cable fields as ordinary parts of programming the machine.[^chm-photo]

This was not “not programming.” It required algorithms, decomposition, sequencing, timing, debugging, and intimate knowledge of the machine. The historical mistake is to define programming backward from a modern text editor and then erase the work that does not resemble it.

## Programming was skilled systems work

Six women — Kathleen McNulty, Frances Bilas, Betty Jean Jennings, Ruth Lichterman, Marlyn Wescoff, and Betty Snyder — are conventionally identified as ENIAC's original programming team. Their work grew out of the Army's human-computing organization and required understanding both the mathematical problems and ENIAC's hardware behavior.

A Penn retrospective notes that the programmers initially learned much of the machine through diagrams and discussions with engineers and became capable of diagnosing faults deep into the machine.[^penn-75]

This matters for the constraint-first story. When the program is embodied partly in wiring, switches, timing relationships, and unit configuration, the distinction between:

```text
programmer
operator
hardware diagnostician
systems engineer
```

is not yet clean.

The later abstraction of “software” did not simply make code portable. It also helped reorganize technical labor.

## Why physical reconfiguration became a bottleneck

ENIAC's electronics made arithmetic fast, but changing a problem could still involve substantial manual setup.

That creates a mismatch:

```text
machine arithmetic: electronic speed
problem setup:       human wiring and switch-setting speed
```

Once a machine can perform thousands of operations per second, spending hours or days preparing its next calculation becomes economically and operationally conspicuous.

### Engineering reconstruction

Imagine a machine that completes a run in 20 minutes but needs 12 hours of engineering work before the next unrelated run.

Its nominal arithmetic speed may be extraordinary while its **problem-to-problem throughput** remains low.

A useful system metric is therefore not only:

```text
operations / second
```

but something closer to:

```text
useful completed problems / day
```

The faster the electronics become, the more visible configuration overhead becomes.

This is one reason “program as stored information” is so important: it attacks the setup bottleneck rather than the arithmetic bottleneck.

## The EDVAC report did not appear in a vacuum

The document most often associated with the stored-program architecture is John von Neumann's **First Draft of a Report on the EDVAC**, dated 30 June 1945.[^edvac-smithsonian]

The report is genuinely important. It gave a widely circulated logical description of a computer in which control instructions are represented in the machine's storage system.

But the shorthand “von Neumann invented the stored-program computer” is historically unsafe.

The Computer History Museum explicitly notes that Eckert and Mauchly were already aware of the limitations of rewiring ENIAC and that von Neumann's report drew on discussions within the ENIAC/EDVAC design environment.[^chm-making-case] CHM's later discussion of ENIAC software history calls the priority question contested and warns against reducing a collaborative design transition to a single lightbulb moment.[^chm-programming]

The report itself is credited to von Neumann, and its circulation had enormous influence. That fact is different from claiming that every idea in it originated uniquely with him.

## What “stored program” changes structurally

A physical configuration can describe a computation. So can a sequence of coded instructions.

The crucial difference is what operations become cheap.

With coded instructions, a machine can more readily support:

- repeated instruction sequences;
- conditional transfers;
- loops;
- subroutines;
- compact program storage;
- easier alteration of control flow;
- systematic loaders and assemblers;
- program libraries;
- later, programs that manipulate program representations.

It is useful to think of this as **compressing control structure into addressable representation**.

Instead of needing a new wire for every control relationship, many relationships can be expressed numerically:

```text
execute instruction at address N
then N+1
unless condition C
then continue at address M
```

Once control becomes encoded, sequential execution and branches replace much of the physical topology that had previously expressed the algorithm.

## ENIAC itself was modified

This is where a simple “ENIAC before, stored-program computers after” chronology breaks down.

CHM's synthesis of work by historians Thomas Haigh, Mark Priestley, and Crispin Rope describes a conversion of ENIAC beginning in 1947. Because ENIAC lacked a large writable electronic store suitable for a conventional instruction memory, coded instructions were placed in its **function tables** — banks of switches originally intended for numerical constants.[^chm-programming]

On **12 April 1948**, a substantial program using this modified control scheme began running on ENIAC according to the machine logs and notes analyzed by those historians.[^chm-programming]

CHM describes the program as an 840-instruction Monte Carlo calculation involving nested loops, a subroutine, and indirect addressing.[^chm-programming]

This is a beautiful example of engineering adaptation:

> ENIAC did not suddenly gain a modern RAM full of instructions. Engineers repurposed the storage-like resources the machine already had.

That is much more historically interesting than saying “they upgraded the software.”

## Was the modified ENIAC a stored-program computer?

This question immediately becomes definitional.

The modified ENIAC stored coded control instructions in function-table switches. Those instructions were not held in the same writable electronic memory used for arbitrary data in the later Manchester style.

CHM therefore discusses the modified ENIAC as operating in a “modern code paradigm,” while also noting that its program store was effectively read-only from the machine's point of view.[^chm-programming]

The Manchester Small-Scale Experimental Machine (“Baby”), by contrast, successfully ran a program on 21 June 1948 from the Williams-Kilburn tube storage system that also held ordinary machine information.[^manchester-baby]

This is exactly why “first stored-program computer” is a dangerous phrase unless the criterion is specified.

Possible criteria include:

- coded instructions instead of physical wiring;
- instructions stored internally;
- instructions held electronically;
- instructions and data sharing the same writable memory;
- a working general-purpose machine;
- a machine built primarily to demonstrate the storage principle;
- practical influence on later production systems.

Different criteria produce different answers.

The repository therefore prefers the question:

> **Which part of the modern programming model did this machine demonstrate, and under what physical constraints?**

## The Manchester Baby clarifies the other half of the story

The Manchester team built the Baby primarily to test Williams-Kilburn CRT storage. Their 1948 Nature letter explicitly says the machine was experimental and built to test the storage principle before proceeding to a full-scale machine.[^williams-kilburn-letter]

That fact is revealing.

The stored-program problem was inseparable from the memory problem.

It is easy to write on paper:

```text
put instructions in memory
```

It is much harder to build a memory in 1947 that is simultaneously:

- fast enough;
- large enough;
- writable;
- readable at electronic speed;
- reasonably reliable;
- affordable and constructible.

ENIAC could be reorganized into coded control before a large general writable electronic memory was available on the machine. Manchester's work approached the problem from the other direction: prove a practical random-access electronic store, then use a small computer to exercise it.

The “stored-program revolution” was therefore partly a **storage-technology revolution**.

## Why sequential control won despite losing some parallelism

Original ENIAC control could exploit parallel activity among functional units. A centralized coded instruction stream can appear, at first glance, like a retreat into one-thing-after-another execution.

### Reconstruction

Sequential coded control offers an enormous gain in *manageability*:

```text
physical graph of cables
        ↓
compact symbolic sequence
        ↓
addresses + operations + branches
```

A sequential model can also be extended with parallel devices, overlap, interrupts, channels, pipelines, and multiple processors later. What it supplies first is a manageable default abstraction.

This helps explain a recurring architectural pattern: systems often accept a locally less-general mechanism because it makes the whole machine easier to program, reason about, and standardize.

## The transition changes what a “program” can become

Once programs are coded data structures, an ecosystem becomes possible around them.

You can imagine — and soon historically observe — new layers:

```text
mnemonic assembly
symbolic addresses
loaders
libraries
compilers
monitors
operating systems
editors
debuggers
```

Those layers do not follow automatically from one 1945 report. They require memory, I/O, conventions, user communities, and years of engineering.

But they are much harder to build around a computation whose control structure exists mainly as a one-off physical wiring layout.

The shift is therefore not merely from “hardware” to “software.”

It is from:

> **control as machine configuration**

into:

> **control as reusable representation**.

## What this teaches us

ENIAC shows why the history of computing should not be written as a succession of clean inventions.

The same machine crossed conceptual regimes.

Its original form demonstrated that large electronic general-purpose calculation was practical. Its programming practice demonstrated that algorithms could be embodied in a configurable network of electronic units. Its later conversion showed that coded centralized control could be retrofitted even without the kind of writable program memory later associated with the stored-program concept.

Meanwhile the Manchester Baby demonstrated another crucial combination: a program held in electronic memory of the same general kind used by the machine's working data.

The transition was not one moment. It was a convergence of:

```text
faster electronics
+ pressure to reduce setup time
+ coded control
+ branching and sequencing
+ usable electronic memory
+ new programming practice
```

That convergence is much more informative than arguing endlessly over one unqualified “first.”

## References

[^chm-programming]: Leonard J. Shustek, “Programming the ENIAC: an example of why computer history is hard,” Computer History Museum, 2016, https://computerhistory.org/blog/programming-the-eniac-an-example-of-why-computer-history-is-hard/
[^chm-photo]: Computer History Museum collection, “ENIAC (Electronic Numerical Integrator and Computer),” ca. 1946, accession 102618640, https://www.computerhistory.org/chess/stl-42fa8835902ab/
[^penn-75]: University of Pennsylvania Almanac, “75th Anniversary of the Electronic Numerical Integrator and Computer (ENIAC),” 2021, https://almanac.upenn.edu/articles/75th-anniversary-of-the-electronic-numerical-integrator-and-computer-eniac
[^edvac-smithsonian]: John von Neumann, *First Draft of a Report on the EDVAC*, Moore School of Electrical Engineering, 30 June 1945, Smithsonian Libraries digital edition, https://library.si.edu/digital-library/book/firstdraftofrepo00vonn
[^chm-making-case]: Computer History Museum, “Making the Case,” *Revolution: The First 2000 Years of Computing*, https://www.computerhistory.org/revolution/birth-of-the-computer/4/88
[^manchester-baby]: University of Manchester, “The Baby,” Digital 60 / Computer Conservation material, https://curation.cs.manchester.ac.uk/digital60/www.digital60.org/birth/thebaby/index.html
[^williams-kilburn-letter]: F. C. Williams and T. Kilburn, “Electronic Digital Computers,” *Nature* 162 (1948), transcription/reproduction hosted by the University of Manchester, https://curation.cs.manchester.ac.uk/digital60/www.digital60.org/birth/manchestercomputers/mark1/documents/natletter.html

## Further reading

- Thomas Haigh, Mark Priestley, and Crispin Rope, *ENIAC in Action: Making and Remaking the Modern Computer*, MIT Press, 2016.
- Computer History Museum, ENIAC operating-manual catalog record, 1946, https://www.computerhistory.org/collections/catalog/102663195
- University of Manchester, “Mark 1 Documents,” including the 1947 Williams-Kilburn storage report and later technical papers, https://curation.cs.manchester.ac.uk/digital60/www.digital60.org/birth/manchestercomputers/mark1/documents/index.html

## Historiographical caution

This case deliberately avoids using “von Neumann architecture” as shorthand for sole invention by John von Neumann. The 1945 report was written under his name and was historically influential; the underlying development involved conversations and work by a larger ENIAC/EDVAC community. Priority claims should be stated with an explicit criterion and source.
