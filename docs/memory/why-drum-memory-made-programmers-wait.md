# Why Did Programmers Have to Wait for Memory to Rotate?

A modern programmer normally treats a memory address as a place:

```text
load address 1234
```

The physical position of the bits is deliberately hidden.

On a magnetic-drum computer, that abstraction could leak spectacularly.

The requested word might already be under the read head. Or it might have just passed the head, forcing the machine to wait almost a full revolution before seeing it again.

That makes the historical question unusually concrete:

> **What happens to programming when memory has geometry and phase?**

The IBM 650 is an excellent case because its architecture made the answer visible even in the instruction format.

## A drum is storage on a rotating cylinder

A magnetic drum is a metal cylinder coated with magnetic material. Information is recorded in tracks or bands around its surface, while fixed or movable heads read and write magnetic patterns as the cylinder rotates.

The idea predates the IBM 650. Gustav Tauschek patented an electromagnetic drum memory in Austria in the early 1930s; the Computer History Museum traces drum storage from those patents into later computers.[^chm-tauschek]

A drum offered several attractive properties to early designers:

- it was nonvolatile compared with many electronic stores;
- it could hold substantially more information than small high-speed electronic memories;
- its magnetic state did not require acoustic recirculation or CRT refresh;
- recording technology could be manufactured with existing electromechanical and magnetic techniques;
- capacity could be increased by adding tracks and recording area.

But a rotating surface imposes time on every address.

## The IBM 650 makes the geometry explicit

IBM announced the **650 Magnetic Drum Data Processing Machine** in 1953. The drum was central enough to the product that it appeared in the machine's name.[^ibm-650-history]

IBM's 1955 brochure gives unusually clear physical specifications. The standard drum was approximately four inches in diameter and sixteen inches long, rotated at **12,500 revolutions per minute**, and was divided into **40 bands with 50 word locations per band**, for 2,000 ten-digit words.[^ibm-650-brochure]

Those numbers let us recover the machine's time geometry.

At 12,500 rpm:

```text
one revolution = 60 / 12,500 seconds
               = 0.0048 seconds
               = 4.8 ms
```

With 50 addressable angular positions around a track:

```text
one position = 4.8 ms / 50
             ≈ 96 microseconds
```

These are derived values from the brochure's physical specifications, not quoted IBM timing figures.

IBM's current historical account gives an average access time of roughly **2.4 ms**, exactly the scale expected from waiting, on average, about half of a 4.8 ms revolution.[^ibm-650-history]

The important point is not the arithmetic itself. It is that the latency of a memory reference depended on **where the drum happened to be when the reference became ready**.

## Sequential addresses were not necessarily sequential in time

Suppose instruction A finishes just after instruction B's location has passed the read head.

Even if B is the numerically next address, the machine may wait almost a complete revolution:

```text
A finishes
    ↓
[B has just passed]
    ↓
................................ drum rotates ................................
    ↓
B arrives again
```

Now place B at the angular position expected to arrive just as A finishes:

```text
A executes
    ↓
drum rotates during execution
    ↓
B arrives at head
    ↓
execute B immediately
```

The program has not changed mathematically.

Its **physical layout** has.

And that can transform its speed.

## The IBM 650 instruction contains the next instruction's address

This is one of the most revealing features of the machine.

The 650 used ten-digit instruction words. IBM's 1955 brochure explains that an instruction contains:

```text
operation code
address of the operand/data
address of the next instruction
```

The final field is often called the **I-address** or instruction address.[^ibm-650-brochure]

Why spend precious digits explicitly naming the next instruction instead of simply incrementing a program counter?

Because “next numerically” and “next at the right rotational moment” are different concepts on a drum.

### Engineering reconstruction

If an addition consumes a known number of drum positions worth of time, the programmer or assembler can place the next instruction approximately that many positions ahead around the drum.

The I-address then says, in effect:

> After this operation, jump to the location that should be arriving under the head now.

The architecture turns a physical latency into a software-visible scheduling problem.

This is not merely an optimization trick added after the fact. The ability to name the next instruction independently is built into the instruction representation described by IBM itself.[^ibm-650-brochure]

## “Optimal coding” meant spatial scheduling

IBM 650 programmers did not have to optimize every placement by hand forever.

The **Symbolic Optimal Assembly Program (SOAP)** family automated much of this work. IBM's SOAP II reference manual says that symbolic addresses were assigned “optimum drum equivalents”; when a blank D- or I-address referred to the next item, the assembler could fill the address optimally.[^soap2]

The manual also tells programmers to put frequently executed portions earlier in the assembly deck because priority for optimal locations diminished as assembly proceeded.[^soap2]

An IBM 650 program-library abstract describes SOAP as producing an “optimumly coded absolute program” from symbolic input.[^ibm-soap-abstract]

That phrase is easy to misunderstand from a modern perspective. “Optimal” did not simply mean fewer instructions or smarter algebra.

It meant that the assembler was partly solving a **physical placement problem on a rotating memory device**.

A 1958 programming text makes the consequence vivid: code placed serially in consecutive drum locations could be close to the worst possible arrangement because the next instruction might not arrive until nearly another revolution had passed; programmers therefore used placement rules and optimizing assemblers to reduce rotational waiting.[^andree-650]

## Execution time becomes part of address placement

To place instruction B optimally after instruction A, software needs to know approximately how long A takes.

This creates an unusual coupling:

```text
instruction timing
        +
drum angular position
        +
next-instruction address
        =
program layout
```

A multiplication, branch, table lookup, or I/O operation can consume different amounts of time. Therefore the best angular distance to the next instruction depends on the current operation.

The programmer is, in a limited sense, scheduling both **computation and moving storage media**.

Modern systems still optimize layout and prefetch around latency, but they usually hide physical geometry beneath caches, controllers, virtual memory, disk schedulers, and out-of-order execution. The IBM 650 exposes the same class of problem with unusual honesty.

## Why tolerate this at all?

Rotational latency sounds intolerable only if we silently assume inexpensive random-access electronic memory already exists.

In the early 1950s it did not exist in the modern commodity sense.

Designers were comparing imperfect choices:

- acoustic delay lines were serial and required recirculation;
- electrostatic CRT stores could be fast but demanded refresh and careful electronics;
- magnetic-core memory was emerging but initially expensive and labor-intensive;
- drums were mechanically slow but could provide useful capacity, persistence, and established magnetic recording behavior.

The relevant question is therefore not:

> Why would anyone choose memory that rotates?

It is:

> **How much storage can we afford, how reliable can we make it, and can software exploit its predictable rotation?**

For many workloads, especially when arithmetic itself was not nanosecond-scale, predictable milliseconds could be manageable.

## Predictable latency can be optimized

A drum is slow, but it is not random chaos.

If rotation speed is stable and operation timing is known, latency is strongly structured.

That predictability is what makes optimal coding possible.

Consider two kinds of bad memory:

```text
A. slow but predictably periodic
B. occasionally fast, occasionally arbitrarily slow
```

A programmer can schedule around A much more effectively.

This is an important engineering lesson: **variance and predictability matter alongside mean latency**.

## The drum leaks through the abstraction boundary

A clean abstraction hides implementation details that callers should not need to know.

On the 650, drum behavior leaks upward into:

- instruction format;
- assembler design;
- source-program ordering;
- performance tuning;
- programming manuals;
- the mental model of a good programmer.

That is why magnetic drums belong in architectural history, not merely storage history.

The physical memory technology helped shape the machine language.

## A miniature timing model

The companion experiment in [`../../experiments/drum-timing/`](../../experiments/drum-timing/) models a loop on a 50-position drum.

It asks the user to specify operation latencies measured in drum positions and compares:

1. **naive consecutive placement** — instruction 0 at slot 0, instruction 1 at slot 1, and so on;
2. **timing-aware placement** — each next instruction is placed near the position expected when the previous operation finishes.

The model deliberately ignores many real IBM 650 details. It exists to make one mechanism visible:

> if storage is rotating while computation proceeds, instruction placement changes waiting time.

The experiment does **not** reproduce SOAP or certify historically exact 650 timings.

## From explicit geometry to hidden locality

Magnetic drums eventually lost their role as ordinary primary computer memory. Faster magnetic-core and semiconductor memories made random access much less physically conspicuous.

But the underlying problem did not disappear.

Modern machines still reward software that understands locality:

- cache lines;
- DRAM rows and banks;
- NUMA placement;
- SSD erase blocks and flash translation layers;
- disk seeks and rotational delay;
- GPU memory coalescing;
- accelerator scratchpads;
- distributed-data placement.

The details differ radically, and it would be misleading to call a GPU “a drum computer.”

The recurring constraint is more abstract:

> **data is not equally expensive to reach from every physical state of the machine.**

The IBM 650 simply made that fact impossible to ignore.

## What this teaches us

The magnetic drum overturns one of the strongest modern intuitions about programming: that an address is just a number.

On a drum machine, an address could also be a **future moment in a mechanical cycle**.

The resulting architecture teaches four things:

1. memory technology can shape instruction formats;
2. predictable latency can be scheduled around;
3. assemblers can optimize physical placement, not only symbolic translation;
4. locality problems are much older than caches.

The apparently bizarre I-address on the IBM 650 becomes sensible as soon as we restore the missing physical constraint:

> **the memory is moving.**

## References

[^chm-tauschek]: Computer History Museum, “Tauschek Patents Magnetic Drum Storage,” *The Storage Engine*, https://www.computerhistory.org/storageengine/tauschek-patents-magnetic-drum-storage/
[^ibm-650-history]: IBM, “The IBM 650,” IBM History, https://www.ibm.com/history/650
[^ibm-650-brochure]: IBM, *650 Magnetic Drum Data Processing Machine*, brochure, 1955, Computer History Museum collection scan, https://s3data.computerhistory.org/brochures/ibm.650.1955.102646125.pdf
[^soap2]: IBM, *Reference Manual: SOAP II for the IBM 650 Data Processing System*, Form 24-4000-0, 1957, preserved by Bitsavers, https://www.bitsavers.org/pdf/ibm/650/24-4000-0_SOAPII.pdf
[^ibm-soap-abstract]: IBM 650 Program Library, “Symbolic Optimal Assembly Program: SOAP,” program abstract, preserved by Bitsavers, https://bitsavers.computerhistory.org/pdf/ibm/650/programLibrary/Additional_Abstracts_of_IBM_650_Programs_Mar57.pdf
[^andree-650]: Richard V. Andree, *Programming the IBM 650 Magnetic Drum Computer and Data-Processing Machine*, 1958, preserved by Bitsavers/Computer History Museum, https://bitsavers.computerhistory.org/pdf/ibm/650/Andree_Programming_the_IBM_650_Magnetic_Drum_Computer_and_Data-Processing_Machine_1958.pdf

## Source note

IBM's modern history page is a corporate retrospective and is therefore used mainly for basic product chronology and a readable description of the drum. The 1955 IBM brochure and SOAP II manual are period primary documents and carry more weight for the machine's physical organization, instruction format, and optimizing workflow. The timing calculations in this article are explicitly modern derivations from the brochure's stated rpm and location count.
