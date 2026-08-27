# Why Relays Became Computing Machinery

## Start with the industry that already existed

A relay is an electrically controlled switch. Long before general-purpose electronic computers became practical, relay technology was deeply embedded in telegraph and telephone systems.

That matters because early computing did not get to choose components from an imaginary catalog of ideal logic devices. Engineers used parts that existing industries already knew how to manufacture, wire, test, replace, and operate.

Bell Telephone Laboratories was therefore an unusually fertile place for electromechanical computing.

## George Stibitz's Model K

George Stibitz built a small relay-based binary adder in 1937, often called the **Model K** because he assembled it at home on his kitchen table.[^chm-stibitz-model-k]

The significance is easy to flatten into a trivia fact: “Stibitz built a relay computer.”

The more interesting question is:

> Why is a telephone relay a plausible computing element at all?

## A switch can represent a proposition

A relay contact is naturally useful for discrete state.

At a simplified level:

- energized / not energized;
- contact closed / contact open;
- current path present / absent.

With combinations of contacts, circuits can express conditions such as AND, OR, and inversion-like behavior. Relays can also control other relays, allowing logic to be composed into larger networks.

### Reconstruction

For an engineer already living inside switching systems, the conceptual distance between “route a telephone connection according to electrical states” and “route a signal according to logical states” is much smaller than it looks from the perspective of modern semiconductor logic.

The reusable industrial knowledge includes:

- reliable coils and contacts;
- wiring practices;
- switching diagrams;
- test procedures;
- replacement parts;
- technicians familiar with failure modes.

A component becomes historically powerful when an ecosystem exists around it.

## The Complex Number Calculator

Bell Labs completed Stibitz's Complex Number Calculator in 1939. In 1940, at an American Mathematical Society meeting at Dartmouth College, Stibitz demonstrated remote calculation using a Teletype terminal connected by telephone lines to the calculator in New York.[^chm-1940]

CHM describes this as likely the first example of remote-access computing.[^chm-1940]

That wording is important: “first” claims depend on definitions, so this repository should preserve the qualification rather than harden it into folklore.

## Why the remote demonstration matters

The striking part is not simply that the calculator was far away.

The demonstration joined three previously distinct systems:

1. **a computing machine**;
2. **a communications network**;
3. **a human terminal**.

That combination anticipates a pattern that later becomes ordinary: the expensive compute resource does not need to be physically beside its user.

### Reconstruction

Bell Labs had an obvious advantage for this experiment because remote electrical communication was its home territory. The telephone system was not an incidental cable attached after the computer had been invented; communications engineering was part of the institutional environment from which the calculator emerged.

This is an example of a broader rule:

> **A new computing architecture often borrows not only components but also operational habits from the industry that supplied those components.**

## Why not relays forever?

Relays are useful digital switches, but they carry severe costs.

A relay requires mechanical motion. That implies:

- switching delay;
- contact bounce;
- wear;
- acoustic noise;
- coil power;
- finite lifetime;
- physical bulk;
- large wiring volume as systems scale.

Electronic switching with vacuum tubes could be dramatically faster because no macroscopic armature needed to move. This speed advantage was one reason electronic machines such as ENIAC represented such a break from electromechanical calculators; CHM describes ENIAC as more than a thousand times faster than previous computers based on its electronic rather than electromechanical technology.[^chm-eniac]

But “faster” did not make vacuum tubes free. Electronic systems created their own problems in power, heat, reliability, circuit design, and maintenance.

So the transition should not be narrated as:

> primitive relay → obviously superior tube.

It is better understood as a change in which constraints dominated.

## Relay logic as an archaeological experiment

A useful simulator should model at least:

- coil activation delay;
- release delay;
- optional contact bounce;
- fan-out / load assumptions;
- switching count;
- component failure probability;
- power while energized.

Then construct:

- NOT;
- AND;
- OR;
- half adder;
- full adder;
- multi-bit ripple-carry adder.

The user should be able to watch a carry propagate physically through simulated relay delays.

This exposes something that a Boolean algebra diagram hides: two circuits with identical logical functions can behave very differently when their switches have real time constants.

## A second experiment: 1940 remote calculator

A companion interface experiment could deliberately restrict itself to a teleprinter-like interaction model:

```text
TYPE OPERAND A
> 12+34i
TYPE OPERAND B
> 5-2i
OPERATION
> /
TRANSMITTING...
```

Then model:

- low line rate;
- character-at-a-time transmission;
- remote processing delay;
- printed output rather than a screen.

Again, this would not prove what users at Dartmouth felt. It would make the communications constraints tangible.

## What this teaches us

The useful historical chain is:

> mature switching industry  
> → reliable electrically controlled switches  
> → composable logical state  
> → electromechanical calculation  
> → terminal plus telephone line  
> → remote access to centralized computation.

The lesson is not that the Internet was hidden inside a relay.

The lesson is that **computing repeatedly grows by recruiting mature technologies from neighboring systems and then giving them new logical roles**.

## References

[^chm-stibitz-model-k]: Computer History Museum, *Timeline of Computer History*, 1937 entry for George Stibitz's Model K / relay binary adder, https://www.computerhistory.org/timeline/computers/ . See the 1937 timeline entry.
[^chm-1940]: Computer History Museum, “1940,” *Timeline of Computer History*, entry “The Complex Number Calculator (CNC) is completed,” https://www.computerhistory.org/timeline/1940/
[^chm-eniac]: Computer History Museum, “1946,” *Timeline of Computer History*, entry “Public unveiling of ENIAC,” https://www.computerhistory.org/timeline/1946/
