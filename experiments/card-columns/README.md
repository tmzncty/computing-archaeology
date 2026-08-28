# Card Columns Experiment

Historical question:

> What changes when a program line is a fixed-width physical record that can be shuffled?

This experiment accompanies [`../../docs/interaction/why-eighty-columns-survived.md`](../../docs/interaction/why-eighty-columns-survived.md).

Run:

```bash
python experiments/card-columns/card_columns.py
```

No third-party dependencies are required.

## Model

Each card image contains:

```text
columns 1–72   source text
columns 73–80  sequence number
```

The script:

1. creates a tiny source deck;
2. renders every card as an 80-character record;
3. shuffles the deck;
4. sorts it back into order using the sequence field.

## Historical anchors

- IBM introduced the 80-column card in 1928: https://www.ibm.com/history/punched-card
- IBM 29 Card Punch manual: https://www.bitsavers.org/pdf/ibm/punchedCard/Keypunch/029/A24-3332-3_29_Reference_Man.pdf
- Columbia University computing-history material on the IBM 711 and 72/80-column programming practice: https://www.columbia.edu/cu/computinghistory/sorter.html

## What this demonstrates

A fixed-width card makes several things natural that are less obvious in a modern text file:

- records have a hard maximum width;
- record order can fail physically;
- external sequence metadata can repair that failure;
- the original physical width can survive as a software record width after the card itself disappears.

## What this cannot prove

It does not emulate:

- Hollerith hole codes;
- IBM reader electronics;
- row-binary transfer;
- keypunch mechanics;
- card sorting hardware;
- FORTRAN parsing.

The shuffle is synthetic. The experiment isolates the record/ordering constraint.