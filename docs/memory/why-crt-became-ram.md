# Why Did a CRT Become RAM?

A cathode-ray tube looks like a display device to modern eyes.

In the late 1940s, that was only one possible use of the physics inside it.

Frederic Williams and Tom Kilburn used a conventional CRT as an electronic storage device by writing charge patterns onto the inside surface of the screen and sensing those patterns from outside the tube. The result, usually called the **Williams–Kilburn tube** or **Williams tube**, became one of the first practical forms of random-access electronic memory.

The useful question is not:

> Why did anyone misuse a television tube as memory?

It is:

> **What did a CRT offer that the other available memory technologies did not?**

## The memory problem in 1947

Electronic logic had become fast enough that mechanical and electromechanical storage could dominate system timing.

A useful main store needed some combination of:

- electronic access speed;
- enough bits to hold useful programs and working data;
- repeatability;
- addressability;
- affordable construction;
- manageable maintenance.

No mature semiconductor RAM industry existed. Engineers instead searched across physical phenomena: acoustic pulses in mercury, electrostatic charge, phosphor screens, rotating magnetic surfaces, relays, capacitors, and later magnetic cores.

Williams and Kilburn pursued **electrostatic storage on a commercial CRT**.

## Historical record: charge can remember a bit

Tom Kilburn's December 1947 report to the Telecommunications Research Establishment describes a storage system in which binary digits are represented by charge patterns on a CRT screen.[^kilburn1947]

The report is unusually explicit about the physical mechanism.

A beam writes patterns at selected locations on the screen. A metal pickup plate outside the face of the tube senses changes associated with those charge patterns. The pattern is arranged as a two-dimensional array, scanned using television-like raster techniques.[^kilburn1947]

Kilburn reports that the screen itself provides only short-term memory, on the order of **0.2 seconds**. Long-term storage therefore requires periodic regeneration at more than five cycles per second.[^kilburn1947]

That sentence alone destroys the modern intuition that memory is simply a passive box full of bits.

The Williams tube remembered because the machine kept **recreating the thing it was trying not to forget**.

## Random access was the prize

Acoustic delay-line memory is serial: a desired bit or word becomes available when its pulse reaches the pickup point.

A CRT store is different. The electron beam can be deflected toward a selected coordinate.

That means the physical arrangement can support an approximation to what we now call random access:

> choose an address → steer the beam → sense or rewrite that location.

The distinction matters.

With serial memory, access time depends strongly on where the desired information currently is in a circulating sequence. With electrostatic CRT storage, access depends more on beam positioning, selection circuitry, and read/write timing than on waiting for every earlier bit to pass by.

### Reconstruction

This changes what an architecture can afford to assume.

If memory locations can be selected electronically rather than encountered in time order, the instruction set and programming model do not need to expose the same temporal geometry that appears in a delay line or magnetic drum.

The abstraction of an address becomes easier to believe because the hardware is doing more work to hide locality.

## The tube did not store visible text

A common modern misunderstanding is to imagine the Williams tube as a tiny video display holding readable zeroes and ones.

That is not how the mechanism should be understood.

The screen carried **charge distributions** created by beam patterns. Different writing techniques were tested: dot-dash, dash-dot, defocused/focused forms, and related patterns.[^kilburn1947][^manchester-williams]

The visible glow could help operators inspect behavior, but the useful stored state was the electrical effect of the charge pattern, not a human-readable image.

## Reading is an electrical event

The pickup plate attached to the outside of the CRT face detects a transient associated with writing or probing a charged region.

The system therefore turns a local electrostatic condition into a signal that can be amplified and interpreted as binary state.

This is a recurring theme in memory history:

> memory is not merely a material that can have two states; it is a complete **write + preserve + select + sense + restore** system.

A material can retain information and still be useless as computer memory if there is no practical way to address or read it.

## Refresh was not invented by DRAM

Modern DRAM is famous for requiring refresh.

Williams storage makes clear that active refresh is much older.

The CRT charge dissipated. The machine had to revisit stored positions and regenerate their patterns before the information faded.[^kilburn1947]

So the store was doing background maintenance even when the programmer thought nothing was happening.

### Reconstruction

The same architectural pattern appears repeatedly:

```text
physical state decays
        ↓
controller periodically repairs state
        ↓
software receives the illusion of persistent memory
```

The abstraction is more stable than the underlying physics.

## Capacity was constrained by optics and materials

Kilburn's report describes successful storage of **2,048 digits** on one CRT and discusses how capacity depends on focus, screen uniformity, accelerating voltage, spot size, interference between neighboring digit areas, and amplifier gain.[^kilburn1947]

This is important because “memory density” was not a purely logical quantity.

It depended on:

- how small the electron spot could be made;
- whether the spot remained well focused across the screen;
- imperfections in the screen;
- signal-to-noise ratio;
- how closely neighboring charge regions could be packed;
- whether the pickup electronics could distinguish them reliably.

A one-millimeter spot is not a metaphor. It is part of the address-space budget.

## Why commercial CRTs mattered

The 1947 report emphasizes tests with **commercial CRTs**.[^kilburn1947]

That is a constraint-first clue.

A research team does not need to invent every physical component from scratch if another industry already manufactures evacuated tubes, electron guns, phosphor screens, deflection systems, and high-voltage supplies.

Radar and television engineering had already paid for much of the component knowledge.

Computing could appropriate that industrial base.

This is the same pattern seen with telephone relays and later magnetic tape:

> computing often advances by stealing a mature component ecosystem from another field and asking it to do a new job.

## The Baby was built partly to test the memory

Manchester's later preservation material makes the purpose unusually clear.

By the end of 1947, the group could store 2,048 bits, but they still needed to prove that arbitrary bits could be set, read, and preserved at electronic speed. The **Manchester Small-Scale Experimental Machine**, or Baby, was built largely as a practical test of the CRT storage system.[^digital60-how]

On 21 June 1948, the Baby successfully ran a stored program.

The machine is famous for that historical milestone, but from the memory engineer's perspective it was also a severe integration test:

> Can this strange charge-on-glass storage system actually support a working computer?

## Why not use delay lines?

Delay lines were already plausible and became successful in machines such as EDSAC.

They had important advantages:

- compact serial storage;
- relatively simple transducers and amplifiers once engineered;
- proven inheritance from radar timing technology.

But their access pattern was inherently serial.

Williams storage offered a different compromise:

- potentially direct electronic selection;
- no need to wait for a pulse to physically circulate through the entire delay path;
- a two-dimensional address geometry.

In exchange, it demanded difficult CRT behavior, regeneration, precision scanning, and sensitive pickup electronics.

Neither technology was simply “better.” They exposed different constraints to the rest of the computer.

## Why not use magnetic core immediately?

Because practical coincident-current magnetic-core memory was still being developed.

Whirlwind's successful core system came several years later.

A 1947 engineer cannot choose from a mature catalog of 1953 technologies.

The relevant comparison is against what could be made reliable **then**.

## The hidden software lesson

When memory hardware becomes genuinely random-access-like, programmers stop thinking about where a bit is in a circulating stream.

That disappearance is historically important.

An abstraction becomes ordinary when the system successfully hides the physical work required to maintain it.

A modern load instruction does not reveal:

- beam deflection;
- pickup transients;
- regeneration cycles;
- screen defects;
- focus limits;
- amplifier gain.

The whole point of the memory system is that software does not have to care.

## Experiment

See [`../../experiments/crt-refresh/`](../../experiments/crt-refresh/).

The experiment models a two-dimensional array whose cells lose signal over time unless scanned and refreshed. It is intentionally **not** a faithful Williams-tube electrical simulator.

It demonstrates three narrower ideas:

1. stored state can decay while the programmer sees a stable bit;
2. refresh consumes background work;
3. finite scan bandwidth creates a capacity/refresh-rate tradeoff.

## What this teaches us

The Williams tube makes four recurring computing ideas visible.

First, **random access is engineered**, not metaphysically given.

Second, **refresh is abstraction maintenance**: the machine performs invisible work so that memory appears stable.

Third, density depends on materials, sensing, geometry, and noise—not merely on how many address bits the architecture would like to have.

Fourth, computing repeatedly repurposes existing industrial ecosystems. A component built for display and radar engineering became memory because its physical behavior happened to solve a bottleneck that computing urgently had.

The surprising sentence is not:

> They used a television tube as RAM.

It is:

> **For a brief period, a commercial CRT was one of the most credible ways to obtain fast electronic random-access storage.**

## References

[^kilburn1947]: Tom Kilburn, “A Storage System for Use with Binary Digital Computing Machines,” report to TRE, 1 December 1947, University of Manchester Digital60 transcription, https://curation.cs.manchester.ac.uk/digital60/www.digital60.org/birth/manchestercomputers/mark1/documents/report1947.html

[^manchester-williams]: University of Manchester Computer 50 / Digital60, “The Williams Tube,” preservation history and technical summary, https://curation.cs.manchester.ac.uk/computer50/www.computer50.org/kgill/williams/williams.html

[^digital60-how]: University of Manchester Digital60, “How it all began,” Manchester Baby and CRT storage history, https://curation.cs.manchester.ac.uk/digital60/www.digital60.org/birth/how/index.html

## Source note

Kilburn's 1947 report is the central source because it is a contemporary technical document describing the storage problem, mechanism, capacity limits, and regeneration requirements. The Manchester preservation pages are later institutional histories useful for integration chronology and surviving-machine context.