# Why Programs and Data Were Holes

## The strange physicality of early information

A punched card looks absurd if we begin with a modern assumption:

> information should be invisible electrical state inside memory.

But punched media belonged to an earlier and extremely important way of thinking about information: **make state physically durable, mechanically readable, sortable, copyable, and inspectable**.

The same basic idea appeared in automated looms, census tabulation, business data processing, paper-tape systems, and later computer programming.

## Before computer programming: controlling machines with holes

Punched cards predate electronic computing by more than a century. Card-based control was used in textile machinery associated with the Jacquard loom, where patterns of holes represented control information for weaving.[^ibm-card]

Charles Babbage later planned to use punched cards to provide instructions and data to the Analytical Engine, explicitly borrowing the idea from Jacquard-style loom control.[^chm-babbage-engines]

This is already a useful archaeological pattern:

> a representation invented for one kind of automation can migrate into another once engineers recognize that the representation encodes choices independently of the mechanism executing them.

## Hollerith: holes become data processing

Herman Hollerith's late nineteenth-century tabulating system used punched cards to encode records for statistical processing. IBM's historical account describes Hollerith developing machine-readable punched-card data systems for the 1890 US Census, where his method dramatically reduced processing time relative to manual approaches.[^ibm-tabulator]

The important transition is that a card is no longer mainly a sequence of machine-control commands. It is a **record**.

A person's census attributes can be encoded as hole positions, and machines can then count, sort, classify, and tabulate those records.

## Why cards were powerful

A card had several properties that are easy to underestimate.

### 1. Persistence without power

Once punched, the record survives without batteries, magnetic retention, refresh circuits, or delicate electronics.

### 2. Visible individuality

One card can correspond to one record or, later, one source line. Humans can carry it, label it, remove it, duplicate it, reorder it, or accidentally drop it.

### 3. Machine readability

Electrical or mechanical readers can detect hole positions much faster and more consistently than a person can retype the same information.

### 4. Sortability

Physical records can be sorted and merged by machines specialized for those operations. Before general-purpose computers dominated data processing, an entire workflow could be built from punches, sorters, tabulators, collators, and printers.

### 5. Separation between preparation and expensive machine time

A program or dataset can be prepared offline. The central machine does not need to wait while a user types every instruction interactively.

That last point becomes crucial in the batch-processing era.

## The IBM card as an installed platform

IBM introduced its 80-column card format in 1928. IBM's current historical account describes the card as a core information medium for decades and notes that punched-card sales remained financially important to the company even in the 1950s.[^ibm-card]

Once organizations owned:

- keypunches;
- sorters;
- tabulators;
- card readers;
- filing systems;
- trained operators;
- procedures built around cards;

then the card was no longer just a piece of cardboard. It was an **installed information infrastructure**.

### Reconstruction

This helps explain why later electronic computers often accepted punched cards. Supporting existing media could connect a new electronic processor to established organizational workflows.

A superior processor does not automatically erase the input systems, clerical practices, and accumulated data around it.

Compatibility begins before software compatibility.

## Why a program could be a deck

In many later systems, one punched card represented roughly one source line or job-control record. IBM's history of the punched card notes the familiar 80-column format and its use for programming.[^ibm-card]

That creates a very different programming environment from an interactive editor.

A program is a physical ordered sequence.

Consequences include:

- insertion and deletion are physical operations;
- reordering can be literal reordering;
- duplication requires copying cards;
- revisions may require punching replacement cards;
- a dropped deck can become an operational disaster;
- comments and sequence numbers can have practical recovery value;
- submitting the job can mean handing the deck to an operator and waiting.

The medium therefore shapes programming habits.

## Batch processing is partly an economics story

Imagine a computer expensive enough that maximizing machine utilization matters more than minimizing an individual programmer's waiting time.

Interactive use can leave the processor idle while a person thinks, types, reads, and corrects mistakes.

Batch workflows instead collect prepared jobs and feed them through the machine under operator control.

### Reconstruction

Punched media fits this economic model well because:

- jobs can be prepared before machine access;
- jobs can be queued physically;
- operators can feed many jobs consecutively;
- output can be printed and returned later;
- the expensive computer spends less time waiting for a human at a keyboard.

This does not mean cards caused batch processing by themselves. It means card infrastructure and expensive centralized machines reinforced one another.

## The card's dimensions became a software constraint

A mature medium creates habits that outlive the medium.

The 80-column IBM card is a classic example. Fixed card width influenced source-code formatting and data layouts. Later software conventions could preserve column-oriented assumptions even after physical cards disappeared.

This is one of the repository's recurring themes:

> **hardware dimensions can fossilize into software conventions.**

The old physical object vanishes, but its shape remains inside formats, languages, interfaces, or habits.

## Experiment: a card-deck programming environment

A useful experiment should not simply draw a picture of a card. It should force the user to experience the constraints.

Rules:

- 80 columns per card;
- one source line per card;
- no direct insertion into a submitted deck;
- modifications require replacing cards;
- jobs enter a batch queue;
- turnaround time is visible;
- optional sequence columns help recover a shuffled deck.

Add a “drop deck” button that randomizes order.

Then compare recovery:

- deck with sequence numbers;
- deck without them.

That tiny experiment would explain more about some historical coding conventions than a page of nostalgia.

## What this teaches us

Punched cards were not merely a primitive substitute for disks.

They were successful because they combined:

> cheap physical storage  
> + machine readability  
> + offline preparation  
> + sorting and tabulation ecosystems  
> + organizational compatibility.

The deeper lesson is that information technologies survive when they fit **workflows**, not merely when their bit density looks good in retrospect.

## References

[^ibm-card]: IBM, “The IBM punched card,” *IBM History*, https://www.ibm.com/history/punched-card
[^ibm-tabulator]: IBM, “The punched card tabulator,” *IBM History*, https://www.ibm.com/history/punched-card-tabulator
[^chm-babbage-engines]: Computer History Museum, “The Engines,” *Babbage Engine*, https://www.computerhistory.org/babbage/engines/
