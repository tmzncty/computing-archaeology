# Why Did a Byte Become Eight Bits?

## First: it was not always eight

One of the easiest modern assumptions to project backward is:

> byte = 8 bits, therefore a byte has always meant 8 bits.

That is historically false.

During IBM's Project Stretch in 1956, **Werner Buchholz** used the term *byte* for a variable-sized group of bits involved in serial processing and input/output. In an IBM Stretch memo dated 31 July 1956, Buchholz discussed bytes from one to six bits while comparing candidate word lengths.[^stretch40]

A later Stretch memo dated 19 September 1956 states that the maximum input/output byte size for serial operation would be eight bits and that the Exchange would operate on an 8-bit-byte basis.[^stretch45]

So the interesting question is not “what is a byte?” but:

> **What problem was the byte solving before its size became standardized?**

## Word and byte were different design ideas

Early machines were often described around a **word**: a natural chunk moved to or from memory or processed by the machine.

Word sizes were not universally powers of two. Historically important computers used many sizes, including 18, 24, 36, 48, and 60 bits.

Project Stretch itself illustrates the design tension. Stretch Memo No. 40 records a then-tentative 60-bit word and explicitly weighs reasons to consider 64 bits instead.[^stretch40]

The memo discusses several interacting concerns:

- floating-point precision;
- addressing;
- table lookup and searching;
- compatibility between parts of the system;
- packing input/output units into words.

This is exactly the kind of evidence computing archaeology wants: **word length appears as a negotiated systems decision, not a sacred mathematical constant**.

## The byte begins as a useful grouping

In the Stretch design work, a byte was associated with handling fields smaller than a full word.

That is conceptually different from today's tendency to treat the byte as the machine's unquestioned basic addressable unit.

### Documented

Stretch Memo No. 40 notes that a 60-bit word packs byte lengths of 1, 2, 3, 4, 5, and 6 bits evenly, while a 64-bit word creates different packing tradeoffs, especially for six-bit units.[^stretch40]

### Reconstruction

That discussion reveals an architectural tension:

> Choose a word size for arithmetic and addressing, and you may make character/I/O packing awkward.  
> Choose a word size for character packing, and you may make binary addressing or other operations awkward.

The word and the byte are therefore part of a larger system compromise.

## Why were six bits attractive?

Six bits can encode 64 distinct values. That is enough for uppercase letters, digits, and a limited set of punctuation/control symbols.

For many mid-century data-processing tasks, especially those inherited from punched-card and office-machine environments, that could be useful.

But 64 code points become cramped as expectations expand.

If a system wants, for example:

- both uppercase and lowercase alphabetic characters;
- ten digits;
- punctuation;
- controls or special symbols;

then six bits becomes restrictive.

Seven bits gives 128 values. Eight gives 256.

Yet this is still not enough to explain why **eight** became dominant. Standards survive through ecosystems, not arithmetic alone.

## Stretch did not settle the world by itself

It would be another historical mistake to say:

> IBM Stretch chose 8-bit bytes, therefore everyone immediately followed.

Other machines continued to use different character sizes and word organizations. The term *byte* itself could refer to different-sized fields in some architectures.

The eventual dominance of the 8-bit byte is connected to later architecture and standards, especially IBM System/360 and the broader growth of 8-bit character-oriented data processing.

This page deliberately stops short of presenting a one-cause story. A later case study should trace:

- Stretch's 1956 design memos;
- the evolution of character sets;
- ASCII's 7-bit interchange code and parity practices;
- IBM EBCDIC;
- IBM System/360's byte-addressed architecture;
- minicomputer and microprocessor ecosystems;
- standards that eventually define the octet / 8-bit byte clearly.

That deserves primary-source work of its own.

## Why powers of two exert pressure

Binary addressing creates a recurring convenience: powers-of-two sizes align cleanly with binary fields and masks.

Stretch Memo No. 40 explicitly notes that binary bit addressing favors a word length that is itself a power of two, such as 64.[^stretch40]

### Reconstruction

Once word size, field size, address arithmetic, character representation, storage devices, and I/O interfaces all interact, powers of two can simplify boundaries and indexing.

But “powers of two are convenient” still does not mean every historical machine must choose the same unit size. Different workloads and installed systems can justify different compromises.

## A simple packing experiment

Take several hypothetical character widths:

```text
4 bits  = 16 symbols
5 bits  = 32 symbols
6 bits  = 64 symbols
7 bits  = 128 symbols
8 bits  = 256 symbols
9 bits  = 512 symbols
```

Then try packing them into historical word sizes:

```text
18, 24, 36, 48, 60, 64 bits
```

Measure:

- characters per word;
- unused bits;
- whether characters cross word boundaries;
- complexity of extracting an arbitrary character;
- how many address bits are convenient;
- what symbol repertoire each character width allows.

The exercise quickly shows why there is no universally “obvious” answer when the system's priorities are unspecified.

## A better question than “why eight?”

Instead of hunting for one eureka moment, ask:

> Which sequence of design choices made eight-bit groups increasingly easy to produce, store, address, transmit, standardize, and program against?

That formulation lets us see standardization as **path dependence**.

Once enough machines, interfaces, languages, file formats, operating systems, and communications standards assume an 8-bit byte, deviating becomes expensive even if another unit might be elegant in isolation.

The physical constraint becomes an ecosystem constraint.

## What this teaches us

The byte is a compact example of the repository's main argument.

What looks today like a natural unit is actually the residue of:

> word-length decisions  
> + I/O design  
> + character repertoire  
> + binary addressing  
> + packing efficiency  
> + architecture  
> + standards  
> + installed base.

Eight bits eventually became ordinary enough to feel inevitable.

Computing archaeology begins when we stop treating that feeling as an explanation.

## Primary references

[^stretch40]: Werner Buchholz, “Memory Word Length,” IBM Project Stretch Memo No. 40, 31 July 1956, Computer History Museum archive, https://archive.computerhistory.org/resources/text/IBM/Stretch/pdfs/06-08/102632289.pdf
[^stretch45]: IBM Project Stretch Memo No. 45, “Memory Word Length and Indexing,” section “Input-Output Byte Size,” 19 September 1956, Computer History Museum archive, https://archive.computerhistory.org/resources/text/IBM/Stretch/pdfs/06-08/102632292.pdf

## Further reading

- Werner Buchholz, ed., *Planning a Computer System: Project Stretch*, McGraw-Hill, 1962.
- Computer History Museum, IBM Stretch archival material, https://archive.computerhistory.org/resources/text/IBM/Stretch/

> **Research note:** the later consolidation of the 8-bit byte through System/360 and character-code standards should be expanded with additional primary IBM and standards documents before this page is treated as a complete history of the 8-bit byte.
