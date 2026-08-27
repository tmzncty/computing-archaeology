# Why Were Computer Word Lengths So Weird?

Modern general-purpose computing trains us to expect powers of two:

```text
8-bit byte
16-bit halfword
32-bit word
64-bit word
```

That pattern is so familiar that an older specification such as **18 bits**, **36 bits**, or **60 bits** can look like evidence that early designers had not yet discovered the “right” sizes.

They had.

They were solving different systems problems.

The useful historical question is therefore:

> **Before byte-oriented compatibility became dominant, what did a machine's word length have to accomplish?**

The answer explains why many apparently strange sizes were perfectly rational.

## A word was a physical and architectural unit

Historically, *word* usually meant a machine-sized unit of information — a quantity naturally transferred from memory, held in a major register, or processed by the arithmetic hardware.

That unit might contain:

- an integer;
- a floating-point value;
- one or more characters;
- an instruction;
- several packed instructions;
- a bit field;
- an address or parts of several addresses.

There was no law saying all these uses had to fit an 8-bit-derived hierarchy.

If the memory, registers, arithmetic circuits, and instruction format are organized around N bits, then N becomes the machine's natural word whether or not N pleases a modern programmer.

## Concrete machines refuse a neat progression

A few examples are enough to break the idea that word sizes simply marched toward 32 and 64 bits.

### DEC PDP-1 — 18 bits

The Computer History Museum's PDP-1 specifications list:

```text
word length:      18 bits
memory:           4K words, expandable to 16K
instruction set:  28 single-address instructions
```

DEC's maintenance manual likewise describes the accumulator, I/O register, and memory buffer as 18-bit registers.[^pdp1-chm][^pdp1-manual]

The PDP-1 was not a defective 16-bit machine. Its registers, memory transfers, arithmetic, and instruction representation were designed around eighteen-bit units.

### IBM 704 — 36 bits

IBM's 1955 manual is equally explicit:

> the word, or basic unit of information, consists of 36 binary digits.

The same manual says a word can represent a 36-bit logical quantity and can contain **six characters** when IBM's six-bit binary-coded decimal character representation is used.[^ibm704]

Thirty-six is therefore doing several jobs at once:

```text
one arithmetic word
= 36 bits
= twelve octal digits
= six 6-bit characters
```

Those relationships are not accidental conveniences imposed after the fact. They are part of the machine's data representation.

### CDC 6600 — 60 bits

The Control Data 6600 makes the design rationale unusually well documented.

James E. Thornton, one of the machine's principal designers, wrote that the central processor's operand registers were 60 bits long while address and index registers were 18 bits. He then states directly that the 60-bit length was selected for **efficient instruction packing and extended floating-point precision**.[^thornton]

The 6600 used instructions of 15 or 30 bits, which could be packed efficiently into a 60-bit instruction word.[^cdc-manual]

This is crucial evidence because it prevents us from inventing a modern rationale after the fact. For the 6600, a designer explicitly tells us why sixty was attractive.

## The word does not have to equal the address size

Modern discussion often conflates “64-bit computer” with a bundle of ideas:

- 64-bit general registers;
- large virtual addresses;
- 64-bit integer arithmetic;
- 64-bit pointers;
- 64-bit data paths.

Historical machines make it obvious that these widths can be chosen separately.

The CDC 6600 used 60-bit operand registers but 18-bit address and index registers.[^thornton]

That split is sensible. An address needs enough bits to name the installed memory; a scientific floating-point operand may need much greater numerical precision.

There is no engineering requirement that the two be identical.

The pressure to make many widths line up grows later through implementation convenience, compilers, standardized data types, compatible product families, and software ecosystems.

## Why 36 bits could be attractive

For the IBM 704 we have direct evidence of the 36-bit word and six-character packing. We should distinguish that evidence from broader reconstruction.

### Documented

IBM's manual says:

- a word is 36 bits;
- binary-coded character data can place six characters in one word;
- three binary bits correspond exactly to one octal digit, so a word is twelve octal digits.[^ibm704]

### Reconstruction

Those properties make 36 a useful compromise for a machine serving both scientific and symbolic/data-processing work.

It divides evenly by:

```text
2 → 18
3 → 12
4 → 9
6 → 6
9 → 4
12 → 3
18 → 2
```

That gives designers and programmers many convenient field sizes.

But divisibility alone does **not** prove why IBM selected 36 bits. A historical explanation would require tracing the 701/704 design record, scientific precision requirements, predecessor compatibility, instruction formats, and IBM's character conventions.

The repository therefore treats “36 is nicely divisible” as an engineering property, not a documented single cause.

## Why 60 bits could be attractive

For the CDC 6600, Thornton gives us stronger causal evidence.

A 60-bit word packs:

```text
4 × 15-bit instructions
2 × 30-bit instructions
2 × 15 + 1 × 30
```

The technical manual describes exactly these mixed 15/30-bit instruction-word arrangements.[^cdc-manual]

Sixty bits also gives room for a large floating-point significand. Thornton explicitly connects the choice with extended floating-point precision.[^thornton]

This is a very different objective from “make pointers bigger.”

The machine was designed for high-performance scientific computation, and its word width reflects that emphasis.

## Why 18 bits could be attractive

The PDP-1 shows another pattern.

Eighteen bits is divisible by six, so it can interact naturally with six-bit character codes; it is also three groups of six and six octal digits. Its single-address instruction format can devote substantial portions of a word to an operation and a memory address without requiring a 32-bit container.[^pdp1-chm]

Again, that is partly reconstruction.

The historical claim we can make confidently is narrower: DEC deliberately built an 18-bit word machine with 18-bit registers and a word-organized core memory. It was a coherent architectural unit, not a transitional mistake on the way to sixteen bits.[^pdp1-manual]

## Octal was a clue, not an eccentricity

Many machines with word widths divisible by three were naturally represented in octal.

Why?

Because:

```text
1 octal digit = 3 binary bits
```

So:

```text
18 bits = 6 octal digits
36 bits = 12 octal digits
60 bits = 20 octal digits
```

Octal lets a human read binary structures compactly while preserving exact bit grouping.

The later dominance of hexadecimal follows a similar logic around four-bit groups:

```text
1 hex digit = 4 binary bits
```

Hex becomes especially comfortable when bytes and words are multiples of eight bits.

Number notation therefore reflects architecture. The “natural” debugging representation changes when the machine's grouping changes.

## Character size was not fixed either

The companion article [`why-eight-bit-byte.md`](why-eight-bit-byte.md) documents a related historical trap: the byte itself did not originally have a universally fixed eight-bit size.

IBM's Project Stretch design work in 1956 considered byte sizes from one through six bits and debated a tentative 60-bit word against 64 bits.[^stretch40]

That memo exposes the system-level negotiation directly:

- binary addressing creates pressure toward powers of two;
- character and I/O packing creates pressure toward divisible field sizes;
- floating-point work creates precision requirements;
- memory and instruction formats create their own structural costs.

A word length is therefore a **compromise surface**.

## There was no one workload called “computing”

Different computer families were optimized around different mixes of work.

A scientific machine may care intensely about:

- floating-point precision;
- matrix and numerical workloads;
- arithmetic throughput;
- compact instruction delivery.

A commercial data-processing machine may care more about:

- decimal arithmetic;
- character strings;
- records;
- card and tape formats;
- sorting and reporting.

A small interactive research machine may prioritize:

- lower hardware cost;
- fast response;
- display and I/O flexibility;
- compact instructions.

There is no reason these workloads must choose the same natural word.

The surprising historical fact is not that machines used many widths.

It is that later ecosystems became standardized enough that a much smaller set of widths came to feel universal.

## Hardware cost scales with width

A wider word can require more physical resources across the machine:

```text
more memory bits per word
more register flip-flops
wider adders
wider buses
more wiring
more sensing/driving circuitry
```

The exact cost does not scale linearly across every technology, but width is not free.

Therefore “just use 64 bits” is not a historically neutral suggestion.

If a machine can meet its numerical, address, instruction, and character needs with 18 or 36 bits, making every path wider may buy little while increasing component count and cost.

This is especially important in eras when each additional bit position means literal extra hardware repeated across registers and arithmetic units.

## Instruction format can pull word length in either direction

A word must often accommodate instructions as well as data.

Several choices interact:

```text
number of opcodes
number of explicit addresses
register count
address width
immediate constants
indexing fields
instruction count per word
```

If one instruction occupies a whole word, the word must be large enough for all required fields.

If several short instructions can be packed into one word, as in the CDC 6600, divisibility by instruction lengths becomes valuable.

If memory capacity grows, address fields may need more bits, which can force new instruction encodings even when arithmetic precision stays unchanged.

So the word size is not merely “how big an integer the ALU likes.”

It can be an agreement among the **memory, ISA, arithmetic system, and data representation**.

## IBM System/360 changes the terms of the argument

IBM's System/360, announced in 1964, is important not because it suddenly discovered powers of two, but because it made a byte-oriented compatible architecture the foundation for an enormous product family.

IBM's historical account emphasizes the goal of one software-compatible family spanning a wide performance range and identifies the 8-bit byte as a major architectural choice.[^ibm360-history]

In the System/360 lineage, an eight-bit byte is the individually addressable storage unit, and a word is four bytes — 32 bits. Modern IBM architecture documentation still describes this inherited organization explicitly.[^ibm-z]

That changes the source of pressure.

Once a large software and peripheral ecosystem assumes:

```text
8-bit bytes
16-bit halfwords
32-bit words
```

choosing a beautiful 36-bit or 60-bit native word for a new compatible machine becomes vastly more expensive.

Compatibility begins to dominate local elegance.

## Standardization makes history look like mathematics

After decades of byte-addressed systems, programming languages, file formats, network protocols, microprocessors, and operating systems, powers-of-two widths feel almost mathematical.

But history matters.

The modern sequence:

```text
8 → 16 → 32 → 64
```

is partly a consequence of compatibility paths that reinforce themselves.

Once software assumes 8-bit bytes and common integer widths, each new machine inherits billions of reasons not to diverge.

What began as architecture becomes ecosystem geology.

That does not mean 8/16/32/64 is arbitrary. Binary hardware genuinely makes powers of two convenient. It means **convenience alone does not explain why one convenient family defeated many other coherent arrangements**.

## A packing experiment

The companion experiment in [`../../experiments/word-packing/`](../../experiments/word-packing/) compares historical word sizes against several character/field widths.

For each pair it reports:

- complete fields per word;
- unused bits;
- whether fields divide the word exactly;
- number of possible symbols for that field width.

Try:

```text
word sizes:   18, 24, 36, 48, 60, 64
field sizes:   5,  6,  7,  8,  9, 12
```

No single word wins every column.

That is the point.

An “optimal word size” cannot be selected without specifying what the machine is for.

## What this teaches us

Historical word lengths look strange when the present is mistaken for a law of nature.

Restore the old constraints and the design space becomes legible:

```text
arithmetic precision
+ address needs
+ instruction packing
+ character representation
+ memory organization
+ hardware cost
+ I/O conventions
+ predecessor compatibility
= word length
```

The PDP-1's 18 bits, IBM 704's 36 bits, and CDC 6600's 60 bits are not three failed attempts to invent 32-bit computing.

They are three different answers to three different system designs.

The later triumph of byte-oriented powers-of-two widths is historically important precisely because it was **not always obvious**.

## References

[^pdp1-chm]: Computer History Museum, “Specifications,” PDP-1 Restoration Project, https://www.computerhistory.org/pdp-1/specifications/
[^pdp1-manual]: Digital Equipment Corporation, *Programmed Data Processor-1 Maintenance Manual*, 1962, Computer History Museum scan, https://s3data.computerhistory.org/pdp-1/DEC.pdp_1.1962.102652404.pdf
[^ibm704]: IBM, *704 Electronic Data-Processing Machine Manual of Operation*, Form 24-6661-2, 1955, preserved by Bitsavers, https://bitsavers.org/pdf/ibm/704/24-6661-2_704_Manual_1955.pdf
[^thornton]: James E. Thornton, *Design of a Computer: The Control Data 6600*, Scott, Foresman, 1970, p. 13, Computer History Museum archive scan, https://archive.computerhistory.org/resources/text/CDC/cdc.6600.thornton.design_of_a_computer_the_control_data_6600.1970.102630394.pdf
[^cdc-manual]: Control Data Corporation, *6600 Central Processor Technical Manual*, preserved transcription/scan, instruction-stack section describing 60-bit instruction words containing 15- and 30-bit instructions, https://manualzz.com/doc/19741919/control-data-6600-central-processor-technical-manual
[^stretch40]: Werner Buchholz, “Memory Word Length,” IBM Project Stretch Memo No. 40, 31 July 1956, Computer History Museum archive, https://archive.computerhistory.org/resources/text/IBM/Stretch/pdfs/06-08/102632289.pdf
[^ibm360-history]: IBM, “The IBM System/360,” IBM History, https://www.ibm.com/history/system-360
[^ibm-z]: IBM, *z/Architecture Principles of Operation*, information-formats section documenting the inherited 8-bit byte and 4-byte word organization, https://www.ibm.com/docs/en/module_1678991624569/pdf/SA22-7832-14.pdf?cp=HW11W

## Source note

The strongest causal statement in this article is the CDC 6600 rationale because Thornton explicitly records it. For the PDP-1 and IBM 704, manuals securely establish word organization and representation but do not by themselves establish every design motive. Sections labeled as reconstruction therefore discuss attractive properties without presenting them as quotations from the original design teams. IBM's System/360 history is a corporate retrospective and is used mainly for family-level compatibility context; architecture manuals carry more weight for technical definitions.
