# Why Did Byte Order Become a Holy War?

Take the 32-bit value:

```text
0x12345678
```

It contains four bytes:

```text
12 34 56 78
```

Now place those bytes in memory.

Should the lowest address contain `12` or `78`?

Both answers have existed in major computer families.

The disagreement became famous enough that Danny Cohen's 1980 paper **“On Holy Wars and a Plea for Peace”** borrowed the names *Big-Endians* and *Little-Endians* from *Gulliver's Travels*.[^cohen]

The useful question is not:

> Which endian is correct?

It is:

> **Why did byte order become software-visible, and what happens when incompatible machines exchange structured data?**

## Byte addressing creates an ordering question

A machine that manipulates only indivisible words does not need to expose the internal byte order of those words in the same way.

Once memory is byte-addressable and instructions can access both bytes and larger words, a multi-byte quantity occupies several separately addressable locations.

Then the architecture must decide which significance goes at which address.

For a 16-bit word:

```text
value = 0x1234
bytes = 0x12 and 0x34
```

Two common layouts are:

### Big-endian

```text
low address     high address
   12              34
```

The most-significant byte comes first in increasing address order.

### Little-endian

```text
low address     high address
   34              12
```

The least-significant byte comes first.

Neither arrangement changes the mathematical value *inside the processor*.

The difference appears when software or hardware observes individual bytes.

## PDP-11: low byte at the even address

DEC documentation is unusually explicit.

The 1970 *PDP-11 Conventions* defines the low-order byte as the least-significant byte in a word and states that on the PDP-11 the low-order byte is always at an **even address**.[^pdp11-conventions]

PDP-11 processor documentation similarly shows the low byte at the lower/even memory address and the high byte at the next odd address.[^pdp11-handbook]

For the word:

```text
0x1234
```

memory therefore contains conceptually:

```text
address N     34
address N+1   12
```

This is the layout later called little-endian.

## IBM's architecture lineage chose the other arrangement

IBM System/360 established a byte-addressed architecture whose descendants preserve big-endian organization.

Modern *z/Architecture Principles of Operation* states explicitly that System/360, System/370, ESA/390, and z/Architecture use **big-endian byte order**: the most-significant byte is stored at the leftmost/lowest-addressed byte of a field.[^z-poo]

So the same abstract integer can have a different byte image on PDP-11-family and IBM-family systems.

That becomes important the instant data crosses an architectural boundary.

## Why can both choices be internally coherent?

There are real conveniences on both sides.

### Big-endian intuition

If memory addresses increase left-to-right in a printed dump, a multi-byte integer appears in the same significance order as conventional hexadecimal notation:

```text
12 34 56 78
```

The lowest-address byte is also the most significant.

### Little-endian intuition

The lowest address always contains the least-significant part of an integer.

That can make some variable-width arithmetic and extension patterns conceptually regular: the address of a multi-byte integer is also the address of its low-order byte.

But historical architecture choices emerge from complete machine designs, buses, instruction sets, existing conventions, and implementation constraints.

It would be too simple to claim that every architect consciously selected one universal philosophical advantage.

## Danny Cohen's point was larger than byte order

In April 1980, Danny Cohen wrote IEN 137, “On Holy Wars and a Plea for Peace.”[^cohen]

He did not merely coin cute terminology.

His central complaint was interoperability.

Different systems disagreed about:

- bit order;
- byte order;
- word representation;
- message layout.

If each machine exports its native representation directly onto a network, every connection becomes a translation problem.

The “holy war” is therefore not dangerous because engineers enjoy arguing.

It is dangerous because **local representation choices become protocol dependencies**.

## Memory order is not transmission order

A crucial distinction:

```text
how bytes are stored locally
```

is not necessarily:

```text
how bytes are sent on a wire
```

A little-endian host can transmit a multi-byte integer in big-endian network order.

It simply has to serialize it explicitly.

Likewise, a big-endian host can read a little-endian file format by decoding the field according to the file specification rather than treating the bytes as native memory.

The bug appears when software silently assumes:

> external bytes == my machine's in-memory representation.

## The network needed a canonical order

Internet Protocol standardization resolved this problem by defining a wire representation.

RFC 791 states that when a multi-octet quantity is transmitted, the **most significant octet is transmitted first**.[^rfc791]

This is what programmers commonly call **network byte order**.

The network does not care how the host stores the value internally.

It requires the host to translate into the agreed external format.

That creates another abstraction boundary:

```text
native representation
      ↓ serialize
canonical wire representation
      ↓ parse
remote native representation
```

Compatibility is purchased by explicit conversion.

## A file format has the same problem

Suppose a binary file contains:

```text
78 56 34 12
```

If the specification says “32-bit little-endian integer,” the value is `0x12345678`.

If the specification says “32-bit big-endian integer,” the same four bytes mean `0x78563412`.

The bytes alone do not tell you the semantic order.

You need a contract.

That is why binary file formats, instruction sets, peripheral registers, and protocols must specify byte order.

## Why text often escapes this problem

A stream of one-byte ASCII characters does not create the same multi-byte numeric ambiguity.

The sequence:

```text
'1' '2' '3' '4'
```

has an externally visible character order independent of the host's integer representation.

But as soon as the protocol embeds binary integers—lengths, addresses, timestamps, checksums—the endian question returns.

This is one reason text protocols historically offered portability advantages despite their parsing overhead.

## Endianness can leak through unsafe programming

Consider code that stores an integer and then examines its first byte through a byte pointer.

The result depends on architecture.

Likewise:

- binary dumps;
- unions/type punning;
- memory-mapped files;
- network packets;
- device registers;
- serialized structs

can expose native ordering.

The architectural choice becomes a software portability issue.

## Why can't we standardize all CPUs now?

Because installed base is itself a constraint.

Changing native byte order can break:

- binaries;
- operating systems;
- file formats;
- peripheral interfaces;
- language ABIs;
- debugging tools;
- firmware;
- decades of application assumptions.

Once an architecture succeeds, compatibility can cost more than local elegance is worth.

This is the same fossilization mechanism seen with 80-column records and character encodings.

## Bi-endian and conversion hardware

Some architectures later supported multiple byte orders or provided byte-swap instructions.

That does not make the historical choice irrelevant.

It shows how much engineering effort can accumulate around **translation between established conventions**.

A conflict that began as local representation becomes a permanent systems feature.

## Experiment

See [`../../experiments/endianness/`](../../experiments/endianness/).

The experiment:

- encodes the same integers as big- and little-endian byte strings;
- intentionally decodes them with the wrong order;
- demonstrates canonical network serialization;
- shows why copying native memory bytes into a protocol is non-portable.

It uses Python's standard integer conversion routines and is not a CPU emulator.

## What this teaches us

Endianness is a classic compatibility problem because all of the following statements can be true at once:

- both local representations are workable;
- both can have implementation advantages;
- software can be written correctly on either;
- interoperability fails if the representation is left implicit.

The solution is not necessarily to win the holy war.

It is to know where the representation boundary is and make it explicit.

That lesson applies far beyond byte order.

## References

[^cohen]: Danny Cohen, IEN 137, “On Holy Wars and a Plea for Peace,” 1 April 1980, IETF archive, https://www.ietf.org/ietf-ftp/rfc/ien/ien137.html

[^pdp11-conventions]: Digital Equipment Corporation, *PDP-11 Conventions*, DEC-11-HR6A-D, September 1970, preserved by Bitsavers, https://www.bitsavers.org/pdf/dec/pdp11/handbooks/DEC-11-HR6A-D_PDP-11_Conventions_197009.pdf

[^pdp11-handbook]: Digital Equipment Corporation, *PDP-11/40 Processor Handbook*, 1972, byte/word addressing diagrams, https://bitsavers.org/pdf/dec/pdp11/handbooks/PDP-11_40_Processor_Handbook_1972.pdf

[^z-poo]: IBM, *z/Architecture Principles of Operation*, Information Formats section documenting the System/360-to-z big-endian lineage, https://www.ibm.com/docs/en/module_1678991624569/pdf/SA22-7832-14.pdf?cp=HW11W

[^rfc791]: Jon Postel, RFC 791, *Internet Protocol*, September 1981, Appendix B “Data Transmission Order,” https://www.rfc-editor.org/rfc/rfc791.html

## Source note

DEC manuals are primary manufacturer documentation for PDP-11 byte placement. Cohen's IEN is the contemporary source for the Big-/Little-Endian terminology and interoperability debate. IBM's modern architecture manual explicitly documents the preserved System/360 lineage; original System/360 Principles of Operation should be used when making claims about the 1964 design process rather than only the enduring result.