# Text Fossils Experiment

Historical question:

> Why are carriage return and line feed separate, and why can the same text have very different byte values in different character sets?

This experiment accompanies [`../../docs/standards/why-text-is-full-of-device-fossils.md`](../../docs/standards/why-text-is-full-of-device-fossils.md).

Run:

```bash
python experiments/text-fossils/text_fossils.py
```

No third-party dependencies are required.

## Part 1 — CR and LF

The script treats a text position as two coordinates:

- row;
- column.

`CR` resets the column to zero.

`LF` advances the row while preserving horizontal position.

That makes `CR`, `LF`, and `CRLF` visibly different operations.

Historical anchor:

- RFC 20 definitions of ASCII format effectors: https://www.rfc-editor.org/rfc/rfc20.html
- RFC 318 TELNET CR-LF end-of-line convention: https://www.rfc-editor.org/rfc/rfc318.html

## Part 2 — ASCII and EBCDIC

The script encodes `ABC123` in:

- ASCII;
- Python's `cp037` EBCDIC-family codec.

It also sorts a tiny character set by encoded byte value to show that collating assumptions differ.

## Important caveat

`cp037` is a modern codec implementation of an EBCDIC code page.

EBCDIC is a family with historical variants. This demonstration does **not** claim that code page 037 exactly represents every System/360 installation or every later IBM environment.

## What it demonstrates

- device motions can survive as character semantics;
- newline is partly an interoperability convention;
- glyph identity does not imply byte identity;
- character-set ordering can leak into software behavior.

## What it cannot prove

It is not:

- a Teletype emulator;
- an ASCII electrical-link simulator;
- a complete EBCDIC converter;
- a TELNET conformance test;
- a reconstruction of a particular 1960s terminal.