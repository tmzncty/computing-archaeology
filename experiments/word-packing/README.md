# Historical word-packing experiment

This dependency-free Python model accompanies [`docs/architecture/why-word-lengths-were-weird.md`](../../docs/architecture/why-word-lengths-were-weird.md) and [`docs/architecture/why-eight-bit-byte.md`](../../docs/architecture/why-eight-bit-byte.md).

## Historical question

If a machine's natural word is not predetermined, which widths are convenient for which kinds of fields?

The default comparison uses:

```text
word widths:  18, 24, 36, 48, 60, 64 bits
field widths:  5,  6,  7,  8,  9, 12 bits
```

Those choices make several historical tensions visible: six-bit characters fit 18-, 24-, 36-, 48-, and 60-bit words exactly, while eight-bit fields fit 24-, 48-, and 64-bit words exactly but leave spare bits in 18-, 36-, and 60-bit words.

## Run

```bash
python experiments/word-packing/word_packing.py
```

Try another design space:

```bash
python experiments/word-packing/word_packing.py \
  --words 18,36,60,64 \
  --fields 6,7,8
```

## Output

For every word/field pair the program reports:

- complete fields per word;
- unused bits;
- whether the field divides the word exactly;
- the number of distinct values representable by one field.

For example, a 36-bit word contains six complete 6-bit fields with no waste, but only four complete 8-bit fields with four bits left over.

## What it demonstrates

Packing is one genuine pressure on architecture. A word size that looks awkward under an 8-bit assumption can look very natural when the machine uses 6-bit characters, 15-bit instructions, 18-bit addresses, or another historical unit.

The table also makes a negative lesson visible: **there is no universally best word width until the workload and other architectural constraints are specified.**

## What it does **not** demonstrate

This table does not choose a historically correct architecture by itself. It ignores:

- floating-point precision;
- address size;
- opcode and instruction fields;
- register/circuit cost;
- memory organization;
- I/O devices and external media;
- predecessor compatibility;
- software ecosystem effects.

A clean packing result is an engineering property, not proof of a historical designer's motive. The article marks such reconstructions separately from documented rationales such as James Thornton's explanation of the CDC 6600's 60-bit word.

## Suggested exercise

Run the defaults, then answer three questions before reading the article again:

1. If the machine primarily stores 6-bit characters, which words look attractive?
2. If it primarily stores 8-bit characters, which words look attractive?
3. If instructions are 15 or 30 bits, which word size becomes unusually convenient?

The point is not to guess one historical machine. It is to experience how quickly “obvious” architectural units change when the constraints change.
