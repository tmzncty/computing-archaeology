# Endianness Experiment

Historical question:

> What goes wrong when two systems agree on an integer's width but not on the order of its bytes?

This experiment accompanies [`../../docs/architecture/why-byte-order-became-a-holy-war.md`](../../docs/architecture/why-byte-order-became-a-holy-war.md).

Run:

```bash
python experiments/endianness/endianness.py
```

## Model

The script encodes the same 32-bit integer in:

- big-endian order;
- little-endian order.

It then deliberately decodes each byte string with the wrong convention.

Finally it performs a canonical big-endian wire roundtrip.

## Historical anchors

- PDP-11 low-order byte at the even/lower address: DEC, *PDP-11 Conventions*, 1970, https://www.bitsavers.org/pdf/dec/pdp11/handbooks/DEC-11-HR6A-D_PDP-11_Conventions_197009.pdf
- Danny Cohen, “On Holy Wars and a Plea for Peace,” 1980: https://www.ietf.org/ietf-ftp/rfc/ien/ien137.html
- RFC 791 IP transmission order: https://www.rfc-editor.org/rfc/rfc791.html

## What it demonstrates

The same four bytes can denote different integers if the external representation contract is missing or misapplied.

A canonical wire order prevents hosts from simply exporting their native memory layout without agreement.

## What it cannot prove

The program uses Python integer conversion.

It does not emulate:

- PDP-11 memory cycles;
- System/360 storage;
- bus wiring;
- instruction behavior;
- a real network stack.

It isolates serialization semantics.