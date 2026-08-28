# Why Did Computer Terminals Look Like Telegraph Machines?

A modern terminal is a software window. A mid-century computer terminal was often a **machine** in the literal sense: keyboard linkages, motors, clutches, a printer, a paper roll, sometimes a paper-tape reader and punch, and a communications interface descended from telegraph and telephone systems.

The Teletype Model 33 is the iconic example.

It was noisy, uppercase-only in common computer configurations, mechanically limited to roughly ten characters per second, and slow enough that printing a screenful of text would have taken minutes.

Yet it became one of the characteristic interfaces of early minicomputing and remote time-sharing.

The useful question is not:

> Why were old terminals so primitive?

It is:

> **Why did an electromechanical teleprinter become a sensible human-computer interface?**

The answer connects telegraphy, standard character codes, paper tape, telephone networks, modem economics, terminal price, and the discovery that a very fast computer could spend most of its time waiting for very slow humans.

## A terminal existed before the computer needed one

Computers did not invent remote text communication from scratch.

By the time interactive computing became technically and economically attractive, telecommunications industries already knew how to build machines that could:

- turn key presses into coded electrical signals;
- transmit those signals over lines;
- receive coded signals;
- print characters mechanically;
- operate unattended from tape;
- survive office and communications-service use;
- be maintained by an existing service organization.

That inheritance matters.

If you are designing a computer system in the early 1960s and need remote textual input/output, the relevant choice is not:

> teletype versus a modern LCD terminal.

The modern terminal does not exist.

The choice is closer to:

> adapt a mature communications machine, design an expensive special-purpose console, or wait for display technology and electronics to become cheaper.

Under those constraints, the teleprinter is much less strange.

## Model 33: a low-cost data terminal

Teletype Corporation's own 1965 brochure described the Model 33 and Model 35 families as equipment for 8-level code conforming to the newly approved American Standard Code for Information Interchange. The Model 33 was presented as a **low-cost standard-duty** machine operating at 100 words per minute.[^teletype-brochure]

Contemporary Teletype pricing documentation identifies 100 wpm operation as **110 baud** for Model 33 equipment.[^teletype-price]

A DEC PDP-12 maintenance manual later describes the Model 33 ASR as standard equipment with a maximum transfer rate of **10 characters per second** and an integrated paper-tape reader and punch.[^pdp12]

That is the performance envelope that shaped software.

At ten characters per second:

```text
10-character prompt       ~ 1 second
72-character line         ~ 7.2 seconds
1,000 characters          ~ 100 seconds
2,000 characters          ~ 200 seconds
```

A terminal interface that casually redraws the whole screen after every command is absurd in this environment.

## Why 110 baud produces about ten characters per second

The Model 33 did not send only the visible character bits.

A typical asynchronous character frame included framing overhead — a start interval and stop intervals — in addition to the information and parity bits. Eleven signal units at 110 baud produce roughly ten complete characters per second.

The exact framing and options depend on terminal configuration, so this repository should avoid turning one common format into a universal law.

The broader point is robust:

> **line speed was close enough to mechanical print speed that every character consumed noticeable wall-clock time.**

The communications channel and the printer mechanism formed one user-visible latency budget.

## The terminal was a printer, not a display

A printing terminal cannot move the cursor upward and repaint arbitrary earlier text the way a CRT terminal can.

Once ink hits paper, it stays there.

This changes interface design.

Useful interaction patterns include:

- short prompts;
- line-oriented commands;
- append-only transcripts;
- explicit corrections;
- line editors rather than full-screen editors;
- compact error messages;
- abbreviations;
- output only when requested;
- pagination or stopping long listings;
- command languages that can be typed and understood incrementally.

The physical output medium encourages a conversational history:

```text
USER TYPES A LINE
COMPUTER PRINTS A RESPONSE
USER TYPES ANOTHER LINE
```

The terminal literally leaves the session transcript on paper.

## Paper tape made the terminal partly into storage

The `ASR` in Model 33 ASR means **Automatic Send-Receive**. A common ASR configuration included a paper-tape reader and punch.[^pdp12]

That combination is historically important.

The same machine could serve as:

- keyboard;
- printer;
- communications endpoint;
- offline paper-tape punch;
- paper-tape reader;
- program/data loading device.

Paper tape converted temporal interaction into a portable physical artifact.

You could prepare information separately, carry the tape, duplicate it, store it, and feed it later without retyping every character live.

That matters enormously at ten characters per second.

If the computer is expensive and the human is slow, **prepare input offline** is an economically rational strategy.

The terminal therefore sits at the boundary between interactive computing and older batch/media workflows rather than cleanly replacing them.

## ASCII grew out of an interchange problem

The arrival of computer terminals also created a code problem.

Different manufacturers and communications systems used incompatible character encodings. A character stream was useful only if both ends agreed on what bit patterns meant.

Bob Bemer's contemporary account of ASCII describes the new standard as explicitly aimed at **information interchange**, not as a demand that every computer adopt one internal representation.[^bemer-ascii]

The American standard X3.4 was approved in June 1963.[^bemer-ascii]

NIST's later history emphasizes the same systems problem: as computers and data communications spread, a shared code became necessary for equipment from different sources to exchange commands and data.[^nist-ascii]

ASCII therefore belongs in architecture history because of **interfaces**.

It is a treaty between machines.

## Why seven information bits did not mean seven bits on the wire

ASCII defines code points. A communication link must also delimit characters and often provide parity or other framing.

So a seven-bit character code does not imply a seven-baud character transmission.

The Model 33 environment illustrates the distinction:

```text
character repertoire
!=
physical serial frame
```

This becomes important later when 'byte', 'character', 'octet', serial frame, memory word, and storage unit become entangled in modern explanations.

See [`../architecture/why-eight-bit-byte.md`](../architecture/why-eight-bit-byte.md).

## Control characters reveal the machine underneath text

ASCII did not consist only of printable letters and punctuation.

It included control functions for devices and communication.

Names such as:

```text
CR   carriage return
LF   line feed
BEL  bell
BS   backspace
```

make much more sense when the endpoint contains an actual carriage, paper feed, bell, and printing mechanism.

Many control conventions that later became invisible software semantics began as commands for physical machinery.

The phrase **carriage return** is a fossil.

A terminal emulator today may implement `CR` without any carriage existing anywhere in the system.

That is exactly the kind of historical layer this repository wants to preserve.

## Compatibility can outlive the object that created it

Once software assumes:

- carriage-return behavior;
- line-feed behavior;
- line-oriented editing;
- echo conventions;
- serial terminal control;
- particular control characters;

newer terminals must either emulate those expectations or force software changes.

The original physical constraint can disappear while its interface survives.

This is technological geology:

```text
mechanical requirement
-> communications convention
-> software API
-> compatibility requirement
-> emulator behavior
```

A modern pseudoterminal can therefore preserve habits that once existed because metal had to move across paper.

## The telephone network became part of the computer

Remote terminals needed more than character codes.

They needed a transport system.

The Bell System's Data Set 103A documentation describes a device designed for simultaneous transmission and reception of low-speed serial data over the switched voice network, at up to 300 baud in DATA-PHONE service and lower rates for teletypewriter exchange applications.[^bell103]

This is another case where computing borrowed an existing infrastructure rather than building one from nothing.

The public or institutional telephone network already supplied:

- wiring;
- switching;
- dialing;
- long-distance reach;
- maintenance;
- billing;
- familiar endpoint practices.

A modem made that network legible to digital equipment.

Remote computing therefore grew partly by **standing on top of telephony**.

## CTSS: a typewriter character becomes a systems event

MIT's CTSS technical notes give a remarkably concrete description of terminal input.

A user types a character on a typewriter. The character travels over telephone lines to an IBM 7750 communications computer. The 7750 transfers it through a channel into the IBM 7094 system, where an interrupt/trap lets the supervisor buffer and route it to the correct user.[^ctss-tech]

The notes emphasize character-by-character handling so a program can communicate interactively with the user.[^ctss-tech]

That means one keystroke crosses several layers:

```text
human finger
-> electromechanical terminal
-> serial communication
-> telephone line
-> communications computer
-> I/O channel
-> supervisor buffer
-> user process
```

The 'terminal' is not merely a keyboard attached to a CPU.

It is the edge of a distributed system.

## Slow terminals can make time-sharing easier, not harder

This sounds paradoxical.

A 110-baud terminal is painfully slow for a human reader. But human think time and mechanical I/O time are **vastly slower** than a mainframe executing instructions.

While one user is:

- reading output;
- deciding what to type;
- physically typing a command;
- waiting for ten characters per second to print;

the processor can serve someone else.

The time gap that is frustrating to one user is an opportunity for multiplexing at the system level.

This does not mean slow terminals caused time-sharing or made it free. Time-sharing required memory protection, timer interrupts, secondary storage, scheduling, communications hardware, and substantial supervisor software.

But slow human interaction creates the economic opening:

> **many people can feel as though they have a responsive computer because most of them are not demanding the CPU at the same instant.**

See [`../../case-studies/ctss/from-batch-to-conversation.md`](../../case-studies/ctss/from-batch-to-conversation.md).

## Output economy becomes interface design

At ten characters per second, verbosity has a direct time cost.

Suppose an error message is:

```text
?FILE NOT FOUND
```

rather than a modern multi-line diagnostic of 800 characters.

The short message may be unfriendly by modern standards, but a long explanation could occupy the terminal for more than a minute.

This does not explain every terse historical interface. Memory limits, software complexity, and programming culture matter too.

It does, however, show why terminal bandwidth must be included in the causal story.

An interface designed under 110 baud has a different optimal verbosity from one designed for a local gigabit connection.

## Line editing makes physical sense

On a printing terminal, full-screen editing is unavailable because there is no addressable screen.

A line-oriented editor can instead operate by commands such as:

```text
print line
replace line
insert after line
delete line
search
```

The user edits an abstract file while the terminal prints only the pieces needed to understand the change.

CTSS tools such as `TYPSET` and `RUNOFF` grew in exactly this environment. Jerome Saltzer's CTSS documentation describes editing requests that move a conceptual pointer among lines and apply operations to the selected text rather than continually repainting a display.[^ctss-typeset]

The interface is not merely primitive screen editing.

It is a different interface optimized for a different physical medium.

## Reconstruction: terminal speed as a budget

The companion experiment [`../../experiments/tty-budget/`](../../experiments/tty-budget/) treats terminal output as a time budget.

For any text length it asks:

```text
How long must the user physically wait for this to arrive?
```

The model compares common line speeds and lets the user calculate the cost of:

- prompts;
- source listings;
- diagnostics;
- help text;
- a hypothetical full-screen repaint.

It is not a Teletype mechanism emulator. It isolates the constraint that software developers could not ignore.

## Why not use displays immediately?

CRT displays existed well before inexpensive video terminals became widespread.

But a display terminal needs more than a tube:

- character generation;
- deflection/control electronics;
- memory or refresh logic;
- keyboard encoding;
- communications interface;
- power supplies;
- a maintainable enclosure;
- sufficient production volume to lower cost.

A mature teleprinter could remain economically attractive even when a display was technically possible.

The comparison is therefore not old versus new.

It is total system cost and availability.

## What this teaches us

The teletype terminal is a convergence point for several histories.

### Telegraph history

Coded electrical text communication predates interactive computing.

### Telephone history

Modems and switched lines turn a computer center into a remotely reachable service.

### Standards history

ASCII makes heterogeneous equipment more interoperable.

### Media history

Paper tape lets a terminal become both live interface and offline storage device.

### Interface history

Slow printing favors terse, line-oriented interaction.

### Software history

Control characters and terminal conventions outlive the mechanisms that created them.

The Model 33 therefore should not be remembered as a bad keyboard and printer attached to an old computer.

It was an **existing communications technology that computing learned to speak**.

And once software learned its language, traces of the machine remained long after the carriage stopped moving.

## References

[^teletype-brochure]: Teletype Corporation, *Here's How Teletype Equipment Can Help You Move Data*, Model 32/33/35 line brochure, 1965 issue, preserved at Bitsavers, https://bitsavers.org/communications/teletype/brochures/LINE35M10565_Teletype_Line_Brochure_1965.pdf

[^teletype-price]: Teletype Corporation, equipment features and pricing documentation, P.D. No. 129, 1969, preserved by Navy Radio / historical manual archive, https://www.navy-radio.com/manuals/tty/tty-equip-price-1969-04.pdf

[^pdp12]: Digital Equipment Corporation, *PDP-12 Maintenance Manual, Volume I*, November 1972, chapter 4, Teletype Model 33 ASR, https://deramp.com/downloads/mfe_archive/011-Digital%20Equipment%20Corporation/09%20PDP-12/01%20PDP-12%20Documentation/DEC-12-HR1B-D%20Maintenance%20Manual%20Vol%20I%20Nov72.pdf

[^bemer-ascii]: R. W. Bemer, “The American Standard Code for Information Interchange,” contemporary article preserved in the Computer History Museum Bemer papers, https://archive.computerhistory.org/resources/access/text/2021/04/102785423-05-02-acc.pdf

[^nist-ascii]: National Institute of Standards and Technology, “Code for Information Interchange—ASCII,” in *A Century of Excellence in Measurements, Standards, and Technology*, NIST Special Publication 958, https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication958.pdf

[^bell103]: Bell System Practices, Section 591-014-100, *Data Set 103A Type: Identification and Operation*, AT&T, https://www.manualslib.com/manual/1847989/Bell-103a.html

[^ctss-tech]: Jerome H. Saltzer et al., *CTSS Technical Notes*, MIT Project MAC Technical Report MAC-TR-16, March 1965, https://web.mit.edu/saltzer/www/publications/TRs%2BTMs/Multics/TR-016.pdf

[^ctss-typeset]: Jerome H. Saltzer, “Manuscript Typing and Editing,” section AH.9.01 of *The Compatible Time-Sharing System: A Programmer's Guide*, December 1966 revision, https://web.mit.edu/saltzer/www/publications/ctss/AH.9.01.pdf

## Source notes

The Teletype brochure and pricing documents are manufacturer materials and therefore primary evidence for how the company described its products, speeds, and intended markets, not independent evaluations of reliability or market dominance.

DEC's PDP-12 manual is primary technical documentation for one computer integration of the Model 33.

Bemer's article is a contemporary participant account of ASCII standardization. NIST's later history is an institutional retrospective that helps frame the federal standards context.

The CTSS documents are project documentation from MIT and are particularly strong sources for how terminal characters moved through the system and how users actually interacted with text tools.
