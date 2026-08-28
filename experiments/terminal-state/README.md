# Terminal State Experiment

Historical question:

> Why are cursor-motion and screen-control escape sequences useful on a serial terminal instead of simply retransmitting the entire display?

Run:

```bash
python experiments/terminal-state/terminal_state.py
```

The script implements a deliberately tiny stateful terminal with:

- printable characters;
- CR/LF;
- `ESC [ row ; col H` cursor positioning;
- `ESC [ 2 J` clear screen.

It paints a small status display, then updates one value by moving the cursor rather than repainting everything.

## What it demonstrates

A terminal can maintain local display state. Compact semantic commands can therefore replace bulk screen retransmission, an important property on limited-bandwidth links.

## What it does not reproduce

This is not a VT100 emulator and must not be used as a terminal parser in real software. It ignores almost the entire ANSI/VT100 control set, scrolling, attributes, wrap modes, origin modes, device reports, keyboard behavior, timing, and malformed input.

Historical context: [`../../docs/interaction/why-the-vt100-still-lives-in-your-terminal.md`](../../docs/interaction/why-the-vt100-still-lives-in-your-terminal.md).
