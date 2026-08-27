# Why Early Computer Memory Looked So Strange

## Memory was not a solved component

Modern computer diagrams draw a box labeled **memory** as though designers simply choose a capacity and speed.

Early electronic computers faced a more primitive question:

> What physical phenomenon can preserve many bits, change them quickly, and let the machine get them back reliably enough to compute?

The Computer History Museum describes main memory as one of the central technical problems of early computing. Designers tried sound pulses in mercury, electrostatic charge on cathode-ray tubes, magnetized regions on rotating drums, and eventually magnetic cores.[^chm-memory-overview]

Seen without context, these technologies look bizarre. Seen as answers to a missing component, they become much more reasonable.

## 1. Mercury delay lines: memory as circulating sound

A delay line stores a sequence of bits in motion rather than in fixed individually addressable locations.

In a mercury acoustic delay line, electronics convert a digital signal into acoustic pulses. Those pulses travel through the medium, are detected at the other end, amplified, and recirculated.[^chm-delay-line]

The technique had roots in World War II radar, where delay lines were used to delay signals so that changing targets could be distinguished from persistent returns.[^chm-delay-revolution]

EDSAC, completed at Cambridge in 1949, used mercury delay-line memory. CHM describes EDSAC as the first practical stored-program computer to provide a regular computing service.[^chm-edsac]

### Why this is memory at all

If a pulse takes time to travel from one end of the line to the other, then the medium itself temporarily contains the information.

Feed the pulse back into the beginning, and the information can circulate repeatedly.

The important shift is conceptual:

> storage does not require a stationary object for every bit; it only requires a physical state that persists long enough to be regenerated.

### The cost: serial access

A delay line exposes data at a particular point in the circulation cycle. If the word you want has just passed, you wait for it to come around again.

CHM explicitly contrasts early serial memories such as delay lines and drums with later random-access memory.[^chm-main-memory]

### Reconstruction

This means memory latency becomes a scheduling and placement problem. A programmer or machine designer can care not only about *where* a word is stored but *when* it will become accessible.

That is a very different mental model from modern semiconductor RAM.

## 2. Williams–Kilburn tubes: memory on a CRT

Frederic Williams and Tom Kilburn developed a memory based on the electrostatic effects of writing dots on a cathode-ray tube. CHM describes it as the first high-speed, entirely electronic memory.[^chm-memory-timeline]

A spot written by the electron beam creates a charge pattern. A pickup plate detects changes associated with that charge. Because charge leaks away, the stored information has to be refreshed.[^chm-williams]

The Manchester Small-Scale Experimental Machine — the “Baby” — was built to test this memory technology and ran a stored program on 21 June 1948.[^chm-baby]

### Why a display tube?

A CRT already provides:

- an electron beam;
- fast electrical steering;
- a surface on which beam activity leaves measurable electrical effects;
- mature knowledge from radar and display electronics.

### Reconstruction

The Williams tube is less strange if we stop thinking of a CRT only as a human display. To an engineer, it is also a fast electronically addressable physical surface.

The fact that the surface can be used to show a picture is not its only exploitable property.

## 3. Magnetic drums: memory as geometry and rotation

A magnetic drum stores information on the surface of a rotating cylinder coated with magnetic material, with read/write heads arranged around it. CHM notes that ERA's Atlas, completed in 1950, used magnetic drum memory.[^chm-memory-timeline]

A drum can hold much more persistent information than an acoustic pulse circulating in a tube, but access depends on physical rotation.

### Reconstruction

Suppose a drum makes one revolution every `T` milliseconds. A requested word has an access latency determined by its angular position relative to the head.

Then program layout becomes partly geometric.

A machine can run faster if the next instruction arrives under the read head near the moment the current instruction finishes.

This produces a historical programming problem that sounds alien today:

> **instruction placement can be optimized against the rotation of memory.**

The distinction between “software optimization” and “mechanical timing” becomes blurry.

## 4. Magnetic core: turning bits into places

Magnetic-core memory uses tiny magnetic rings whose magnetization can represent state. Jay Forrester, while leading MIT's Whirlwind project, developed the coincident-current core-memory system into a practical high-speed random-access memory.[^chm-forrester]

CHM describes magnetic core as the first reliable high-speed random-access memory and notes that it dominated computer main memory well into the 1970s.[^chm-memory-timeline]

The key change is that a desired location can be selected by intersecting drive lines rather than waiting for information to circulate past a read point.

### Why this was such a big deal

Core memory addressed several painful properties of earlier systems:

- random rather than serial access;
- useful speed;
- nonvolatile magnetic state;
- physical robustness relative to delicate electrostatic storage.

But it came with its own costs:

- many tiny components;
- intricate wiring;
- manufacturing and assembly labor;
- destructive-read behavior in common designs, requiring rewrite after reading.

There is no magic “RAM appears” moment. There is another negotiated compromise.

## The recurring pattern

These memories can be arranged not as a ladder from stupid to smart, but as a set of answers to a multidimensional problem:

| Technology | Physical state | Access character | Major attraction | Major pain |
|---|---|---|---|---|
| Delay line | traveling acoustic pulse | serial | uses controllable delay/regeneration | must wait for circulation |
| Williams tube | electrostatic charge pattern | random | very fast electronic access | refresh and sensitivity |
| Magnetic drum | magnetized rotating surface | rotational/serial by track | persistent, useful capacity | mechanical latency |
| Magnetic core | magnetization of tiny cores | random | fast, reliable, nonvolatile | complex manufacture/wiring |

The table is deliberately qualitative. Exact capacities and timings varied substantially by machine and implementation.

## Experiment: make the wait visible

A useful browser experiment could present the same array abstraction implemented on four simulated media.

### Delay-line mode

Bits circulate continuously. A read waits until the target slot reaches the read point.

### Drum mode

Tracks are visible on a rotating cylinder. Access waits for angular position.

### Williams-tube mode

Access is fast but stored dots decay and require refresh.

### Core mode

Coordinates select a location directly; reads optionally model destructive read-and-rewrite.

Run the same access trace through all four and plot:

- average latency;
- worst-case latency;
- refresh/regeneration work;
- energy or synthetic component cost;
- sensitivity to access order.

The goal is to make “memory technology” change the behavior of the whole machine.

## What this teaches us

Early memory looks weird because **memory itself was the unsolved problem**.

Engineers searched across acoustics, electrostatics, mechanics, and magnetism because no single technology yet satisfied all of these at once:

> speed + capacity + reliability + random access + manufacturability + cost.

Modern computers hide that struggle behind a uniform load/store abstraction.

Computing archaeology removes the abstraction for a moment and asks what the bits were physically doing.

## References

[^chm-memory-overview]: Computer History Museum, “Memory,” *Selling the Computer Revolution*, https://www.computerhistory.org/brochures/memory/
[^chm-delay-line]: Computer History Museum, “1949: EDSAC computer employs delay-line storage,” *The Storage Engine*, https://www.computerhistory.org/storageengine/edsac-computer-employs-delay-line-storage/
[^chm-delay-revolution]: Computer History Museum, “Delay Lines,” *Revolution: The First 2000 Years of Computing*, https://www.computerhistory.org/revolution/memory-storage/8/309
[^chm-edsac]: Computer History Museum, “EDSAC,” *Revolution*, https://www.computerhistory.org/revolution/story/95
[^chm-main-memory]: Computer History Museum, “Main Memory,” *Revolution*, https://www.computerhistory.org/revolution/memory-storage/8/251
[^chm-memory-timeline]: Computer History Museum, “Memory & Storage,” *Timeline of Computer History*, https://www.computerhistory.org/timeline/memory-storage/
[^chm-williams]: Computer History Museum, “1946: Williams demonstrates CRT storage,” *The Storage Engine*, https://www.computerhistory.org/storageengine/williams-demonstrates-crt-storage/
[^chm-baby]: Computer History Museum, “1948,” *Timeline of Computer History*, Manchester Baby entry, https://www.computerhistory.org/timeline/1948/
[^chm-forrester]: Computer History Museum, “Jay W. Forrester,” https://computerhistory.org/profile/jay-w-forrester/
