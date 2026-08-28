# TTY Bandwidth Budget

Historical question:

> What does an interface look like when every character consumes a noticeable fraction of a second?

The default model uses a common Teletype Model 33 operating envelope:

```text
110 baud
11 signal units per character
≈ 10 characters per second
```

The exact serial framing of historical installations could vary. The defaults are a pedagogical Model-33-style case, not a universal property of all teleprinters.

## Run

```bash
python experiments/tty-budget/tty_budget.py
```

The program reports approximate print/transmission time for:

- a short prompt;
- a 72-column line;
- a compact error;
- 500 characters of help;
- a 1,000-character listing;
- an 80×24 screenful of text.

Try a different line rate:

```bash
python experiments/tty-budget/tty_budget.py --baud 300
```

Calculate your own output size:

```bash
python experiments/tty-budget/tty_budget.py --characters 2400
```

Or text:

```bash
python experiments/tty-budget/tty_budget.py \
  --text "READY. TYPE COMMAND"
```

## Optional live mode

If you want to **feel** the rate rather than calculate it:

```bash
python experiments/tty-budget/tty_budget.py \
  --text "THE COMPUTER IS ANSWERING AT TEN CHARACTERS PER SECOND." \
  --live
```

Live mode intentionally sleeps between characters and is therefore not used in automated tests.

## What this exposes

At roughly ten characters per second:

```text
10 chars     ≈ 1 second
100 chars    ≈ 10 seconds
1000 chars   ≈ 100 seconds
1920 chars   ≈ 192 seconds
```

That makes several historical interface choices less mysterious:

- terse prompts;
- compact diagnostics;
- line-oriented editing;
- avoiding unnecessary output;
- abbreviations;
- preparing long input offline on paper tape;
- paging or interrupting listings.

The model does not claim terminal speed was the sole cause of these conventions.

## What this does **not** model

It does not simulate:

- typewheel motion;
- carriage return mechanics;
- line-feed timing differences;
- keyboard force;
- echo modes;
- paper-tape reader/punch mechanics;
- modem latency;
- telephone-network errors;
- computer scheduling delays;
- terminal buffering;
- retransmission protocols.

It isolates one constraint: **character bandwidth becomes human waiting time**.

## Sources

- Teletype Corporation Model 33/35 brochures and price documentation preserved by Bitsavers and historical communications archives.
- Digital Equipment Corporation PDP-12 maintenance manual, which documents the Model 33 ASR at a maximum transfer rate of ten characters per second.
- MIT CTSS project documentation for remote typewriter/telephone-line interaction.

Companion article:

[`../../docs/interaction/why-terminals-were-teletypes.md`](../../docs/interaction/why-terminals-were-teletypes.md)
