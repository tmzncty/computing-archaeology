# Why Is Text Full of Device Fossils?

A modern text file feels abstract.

It contains characters. Newlines separate lines. Encodings map symbols to numbers.

But many of the conventions inside modern text systems were designed when “text” meant controlling electromechanical printers, paper tape, communications lines, card equipment, and incompatible host computers.

That history is still visible in names such as:

- carriage return;
- line feed;
- backspace;
- bell;
- form feed;
- delete;
- escape;
- device control.

The question is not:

> Why did standards committees choose such weird names?

It is:

> **What physical actions were character codes expected to cause?**

## ASCII was an interchange standard, not merely an alphabet

The American Standard Code for Information Interchange emerged from standards work intended to let different equipment exchange text and control information.

By 1969, RFC 20 proposed standard **7-bit ASCII** for ARPANET host-to-host interchange, embedded in an 8-bit byte with the high-order bit set to zero.[^rfc20]

ASCII therefore included printable graphics but also a large block of control characters.

RFC 20's reproduced 1968 standard defines, among others:

```text
BEL  Bell
BS   Backspace
HT   Horizontal Tabulation
LF   Line Feed
FF   Form Feed
CR   Carriage Return
SO   Shift Out
SI   Shift In
DC1–DC4 Device Controls
ESC  Escape
DEL  Delete
```

These are not arbitrary abbreviations.

They describe terminal, communications, and media operations.

## A carriage really returned

On a printing terminal, two motions can be physically distinct:

1. move the print position horizontally back to the left margin;
2. move the paper vertically to the next line.

ASCII therefore has separate control functions:

- **CR** — carriage return;
- **LF** — line feed.

RFC 20 defines CR as moving the printing position to the first position of the same line, and LF as moving to the next printing line.[^rfc20]

That separation makes perfect sense if the output device has real mechanical motion.

It looks strange only after the mechanical carriage disappears.

## Why does CRLF mean newline on networks?

Different hosts and terminals represented end-of-line differently.

By 1972, the TELNET protocol defined a Network Virtual Terminal and specified that the end of a line of text should be represented by the two-character sequence **CR LF**.[^rfc318]

RFC 318 explains the interoperability problem explicitly:

- some terminals perform both motions with one New Line function;
- some systems treat CR and LF separately;
- some software gives them semantic meanings beyond formatting;
- TELNET needs one network representation that each endpoint can translate into its local convention.[^rfc318]

So CRLF is not merely a Windows eccentricity that appeared from nowhere.

It belongs to a longer attempt to normalize heterogeneous terminal behavior.

## Network virtualization begins with printers

The TELNET Network Virtual Terminal is conceptually important.

Instead of requiring every host to understand every physical terminal, TELNET defines an abstract terminal with agreed control behavior.

Each side maps:

```text
local terminal semantics
        ↕
network virtual terminal
        ↕
remote host semantics
```

This is an early and very clear compatibility layer.

The protocol hides hardware differences by defining a common fiction.

That design pattern later appears everywhere in computing.

## Why does DEL have the value it has?

ASCII's **DEL** character is historically tied to punched media.

RFC 20 notes that DEL is used primarily to erase or obliterate unwanted characters in perforated tape.[^rfc20]

Why does all-ones make sense for deletion?

Because punching additional holes can turn an existing tape position into the all-holes pattern without needing to restore paper.

The code point reflects the failure/recovery properties of the medium.

Again, the representation is not abstract first.

It is physical first, then standardized.

## ASCII did not instantly replace every code

IBM's System/360 era also consolidated **EBCDIC** (Extended Binary Coded Decimal Interchange Code) across a major commercial ecosystem.

The important historical point is not to decide which code is aesthetically superior.

It is that IBM had a huge installed base of:

- punched-card data;
- business applications;
- peripheral equipment;
- BCD-family conventions;
- customers whose programs depended on character ordering and codes.

System/360 made compatibility across a family of machines a central design goal.

The original *System/360 Principles of Operation* defines an architecture organized around 8-bit bytes and the system's character representations.[^s360-poo]

Modern IBM documentation still explains why EBCDIC remains costly to abandon: enormous quantities of existing data and programs depend on the character set and its collating sequence.[^ibm-ebcdic]

That is path dependence in its pure form.

## Collating order is software-visible

An encoding does more than display glyphs.

Its numeric arrangement affects comparisons and sorting.

If software assumes:

```text
if code(A) < code(B): ...
```

or uses ranges such as:

```text
'A' <= c <= 'Z'
```

then the structure of the character set leaks into program behavior.

ASCII and EBCDIC assign different numeric values and have different collating arrangements.[^ibm-ebcdic]

Therefore conversion is not always:

> replace each byte with another byte.

It can change assumptions embedded in sorting, parsing, table indexing, record formats, and external data.

## Seven bits inside eight bits

ASCII itself is a 7-bit code.

RFC 20's network recommendation places it in an 8-bit byte with the high bit zero.[^rfc20]

That historical detail is useful because it separates two ideas that modern programmers often fuse:

```text
character code width
```

and:

```text
machine storage unit width
```

ASCII did not make the byte eight bits. Nor did an 8-bit byte logically require ASCII.

The two standards histories interacted.

See [`../architecture/why-eight-bit-byte.md`](../architecture/why-eight-bit-byte.md).

## Control characters are an interface contract

ASCII's control block shows that character streams were expected to control devices and communications, not merely store prose.

Examples include:

- BEL — request human attention;
- BS — move backward;
- HT — advance to a tab stop;
- FF — advance to another form/page;
- DC1–DC4 — control ancillary devices;
- SYN — maintain synchronization;
- ETB — delimit a transmission block;
- EM — indicate an end-of-medium condition;
- ESC — extend interpretation of following characters.[^rfc20]

A character set was partly a **small command language for terminals and links**.

That helps explain why later terminal protocols and escape-sequence systems grew naturally out of it.

## Why couldn't standards simply choose one newline?

Because standards sit above installed systems.

Suppose one host internally uses a single NL character, another uses CR, another preserves CR and LF as independent operations, and a fourth controls a physical printer where overprinting is meaningful.

A universal interchange format must either:

- destroy distinctions;
- require every host to change internally;
- or define translation rules.

TELNET chose translation around a virtual-terminal model.[^rfc318]

The resulting complexity is not proof that the designers were foolish.

It is evidence that compatibility was already expensive.

## A fossil can outlive the animal

Once software, protocols, source files, terminals, and APIs encode a convention, the original device can disappear while the convention survives.

That is why we still encounter:

```text
\r = carriage return
\n = line feed/newline
\b = backspace
\t = tab
\a = bell/alarm
```

in programming languages whose users may never have touched a mechanical teletype.

The physical terminal became a software vocabulary.

## Experiment

See [`../../experiments/text-fossils/`](../../experiments/text-fossils/).

The experiment:

- renders a tiny line using separate CR and LF cursor motions;
- shows why CR, LF, and CRLF are distinguishable operations;
- maps a small shared character subset between ASCII and EBCDIC using Python's standard codecs;
- demonstrates that byte values and lexical order assumptions do not transfer unchanged.

The experiment is not a historical terminal emulator or a standards conformance suite.

## What this teaches us

Text is not purely symbolic.

Its standards preserve traces of:

- printer motion;
- paper transport;
- punched tape repair;
- communications synchronization;
- device control;
- card-oriented business data;
- installed software bases;
- network translation between incompatible hosts.

The remarkable thing is not that ancient device names remain.

It is that standards succeeded so well that the hardware disappeared **without requiring the software vocabulary to disappear with it**.

## References

[^rfc20]: Vint Cerf, RFC 20, “ASCII format for Network Interchange,” 16 October 1969, reproducing USAS X3.4-1968 definitions, https://www.rfc-editor.org/rfc/rfc20.html

[^rfc318]: Jon Postel, RFC 318, “Telnet Protocols,” April 1972, Network Virtual Terminal and CR-LF end-of-line convention, https://www.rfc-editor.org/rfc/rfc318.html

[^s360-poo]: IBM, *IBM System/360 Principles of Operation*, Form A22-6821-0, original System/360 architecture manual, preserved by Bitsavers, https://www.bitsavers.org/pdf/ibm/360/princOps/A22-6821-0_360PrincOps.pdf

[^ibm-ebcdic]: IBM, “The EBCDIC character set,” z/OS basic skills documentation, https://www.ibm.com/docs/en/zos-basic-skills?topic=mainframe-ebcdic-character-set

## Source note

RFC 20 and RFC 318 are contemporary standards/protocol documents and are the main sources for ASCII controls and network newline semantics. The original System/360 manual is primary manufacturer documentation. Modern IBM EBCDIC documentation is used to document the continuing installed-base problem, not to infer every detail of the 1960s design process.