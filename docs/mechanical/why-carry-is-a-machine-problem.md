# Why Is Carry a Machine Problem?

Modern arithmetic notation makes carrying look almost free.

Write:

```text
  9999
+    1
------
 10000
```

and the carries are marks in a margin or transient states inside electronic logic. In a mechanical calculator, however, every carried digit must become a **physical event**: a wheel moves, a latch releases, a spring loads, a lever falls, a tooth engages, or some other mechanism transfers one unit of state into the next numerical place.

That changes the historical question.

Instead of asking only:

> How did early calculators add numbers?

ask:

> **What does a carry cost when digits are pieces of machinery?**

That question connects Pascal's seventeenth-century calculator to Babbage's nineteenth-century engines and to later desk calculators. It also explains why an apparently tiny algorithmic detail can dominate a mechanical design.

## Historical record: Pascal wanted the machine to remember the carry

Blaise Pascal developed his arithmetic machine in the 1640s while dealing with the burden of large calculations connected with his father's administrative work.[^pascal-letter]

In the 1645 *Avis nécessaire* accompanying the machine, Pascal explicitly contrasts calculation by pen with the machine's automatic behavior. Human arithmetic requires the operator to remember carries and borrows; Pascal presents the machine as relieving the operator of that memory burden.[^pascal-avis]

That is an important way to read the Pascaline.

It is not merely a box that turns wheels. It transfers a piece of the **control discipline of arithmetic** from the human into mechanism.

The user should not have to notice that a units digit has crossed from nine to zero, remember a carry, and then manually advance the tens place. The machine has to make the boundary crossing itself consequential.

## The Pascaline's `sautoir`

A surviving technical description of the Pascaline explains its carry mechanism using the *sautoir* — literally a jumping mechanism. Modern museum descriptions reconstruct the process as follows: rotation of one digit gradually arms a metal piece; when the wheel passes from 9 to 0, the piece falls under gravity and advances the next digit by one step.[^inria-pascaline]

The important feature is not merely that it carries.

The next wheel is not driven through a permanently rigid gear train that must transmit the full force of every downstream carry at the same instant. The mechanism stores and releases enough local energy to advance the next position.

The INRIA/ACONIT history emphasizes that this arrangement helps make the wheels relatively independent and avoids a lock-up when a carry must propagate through several positions.[^inria-pascaline]

So `9999 + 1` is already a mechanical architecture problem.

A naive mechanism may need the lowest wheel to supply enough torque to move:

```text
units -> tens -> hundreds -> thousands -> ten-thousands
```

all through one coupled event.

Pascal's design instead breaks propagation into staged local actions.

## Pascal himself argued against abstractly 'simpler' machines

One of the most revealing parts of the 1645 *Avis* is Pascal's defense of mechanical complexity.

He anticipated critics who would say that the machine could have been made with fewer parts. His answer, in modern paraphrase, is that people who know geometry or mechanics only abstractly can imagine arrangements that fail when confronted with matter, space, movement, durability, transport, and interference between parts.[^pascal-avis]

He lists practical goals including a movement that is simple and convenient for the user, a machine that is durable and solid, and mechanisms whose parts can move without obstructing one another.[^pascal-avis]

That is almost a manifesto for this repository.

A design that is logically simpler on paper may be mechanically worse.

## Carry chains turn notation into force

Consider a decimal counter.

Most increments are easy:

```text
1234 -> 1235
```

One digit changes.

Some require one carry:

```text
1239 -> 1240
```

Two digits change.

Some require a longer carry chain:

```text
1299 -> 1300
```

Three digits change.

And occasionally:

```text
9999 -> 10000
```

five digits change.

In handwritten arithmetic the rare long case is only slightly more annoying than the common short case. In mechanism it can create a worst-case load path very different from the average case.

This produces several engineering questions:

- Where does the energy for a carry come from?
- Does one digit have to push all higher digits?
- Can energy be stored locally and released later?
- How much backlash or lost motion accumulates?
- What happens when several carries occur in one operation?
- Can the mechanism distinguish a real digit step from vibration or overshoot?
- Does the operator have to slow down near a long carry chain?
- How are wheels returned to exact detent positions after movement?

A notation does not answer any of these.

## Reconstruction: ripple carry has a mechanical analogue

The following is an engineering reconstruction, not a claim that seventeenth-century designers used modern digital-logic terminology.

In electronic logic, a ripple-carry adder lets a carry propagate from a low-order position toward higher positions. Its delay depends on how far the carry travels.

A mechanical calculator can face an analogous structural problem: if the result in one digit determines whether the next mechanism must move, and that movement determines whether another must move, then a long run of maximum digits creates a long dependency chain.

The physical details are completely different from a transistor adder, but the abstract constraint is recognizable:

> **local arithmetic state can create a variable-length propagation path.**

Pascal's `sautoir` is interesting partly because it does not simply pretend the propagation problem is absent. It gives carry transfer its own mechanism.

## Higher radix: fewer columns, more states per column

It is tempting to jump from the carry problem to a slogan:

> Binary is mechanically superior because a wheel only needs two states.

That is too simple.

For a fixed numerical range, a lower radix needs more digit positions.

For example, representing values up to roughly one million requires about:

```text
base 2:   20 digits
base 4:   10 digits
base 8:    7 digits
base 10:   6 digits
base 16:   5 digits
```

A binary mechanism may have simpler individual state elements, but it needs more of them. It also encounters carry boundaries more frequently when incrementing by one because every `1` is already the maximum digit.

Decimal has more states per wheel but fewer wheels for the same human-scale range.

Babbage explicitly considered multiple number bases before settling on decimal. The Computer History Museum summarizes his decision as involving both engineering efficiency — reducing moving parts — and familiarity to users.[^chm-engines]

That does **not** prove that decimal is universally optimal for gears. It proves the opposite of the modern myth: radix choice was a systems tradeoff rather than an obvious march toward binary.

## A simple carry-frequency model

Suppose we repeatedly increment an odometer by one.

A carry crosses one digit boundary whenever the current low-order digit is already at `radix - 1`.

In base 10:

```text
...8 -> ...9   no boundary carry
...9 -> ..10   one or more carries
```

In base 2:

```text
...0 -> ...1   no boundary carry
...1 -> ..10   one or more carries
```

So a binary counter typically uses more digit positions and triggers carry propagation more often, even though each digit has only two states.

A high-radix counter uses fewer positions and carries less often, but each position must distinguish and reliably stop at more states.

This is exactly the kind of tradeoff that disappears when we ask only whether binary or decimal is mathematically sufficient.

See [`../../experiments/carry-propagation/`](../../experiments/carry-propagation/) for a small model.

## Subtraction exposes another mechanical constraint

The Pascaline's carry mechanism was not simply reversible.

The ACONIT/INRIA description notes that subtraction was therefore handled by complements rather than by running the mechanism backward.[^inria-pascaline]

This is historically revealing.

On paper we may define subtraction as the inverse of addition. A mechanism does not owe us a physically reversible implementation.

If a ratchet, gravity latch, or one-way transfer mechanism makes addition robust, the most practical subtraction algorithm may be changed to fit the machine:

> **alter the arithmetic procedure rather than double the complexity of the mechanism.**

That is a recurring pattern in computing history.

Algorithms are often shaped around what the machine can do reliably, not only around abstract operation counts.

## Babbage: addition as the mechanically cheap primitive

The same pressure becomes much larger in Babbage's Difference Engines.

The method of finite differences converts polynomial tabulation into repeated additions. The Computer History Museum explicitly connects this mathematical choice to mechanism: addition using gear wheels is easier to implement than general multiplication or division.[^chm-how]

This does not mean addition itself was trivial.

A large automatic decimal engine still needed:

- controlled digit movement;
- carry propagation;
- sequencing;
- prevention of interference between mechanisms;
- reliable stopping positions;
- enough energy to move many components;
- mechanisms that work across many columns and repeated cycles.

The point is relative complexity.

If you can build a dependable adding mechanism, a mathematical transformation that removes multiplication is extraordinarily valuable.

## Anticipating the worst case

A useful mechanical design cannot be judged only by the most common input.

Suppose a machine usually changes one digit per addition but once in several thousand operations must propagate a carry through six positions.

If that rare operation jams the machine, slips a tooth, or leaves a wheel between detents, the machine is not reliable enough for unattended table making or office work.

This creates a design philosophy familiar to modern systems engineering:

> optimize the common case, but survive the pathological case.

The pathological case for a mechanical adder may literally be a long row of nines.

## Carry and stored energy

Mechanical carry also forces an energy question.

A digit wheel does not move because arithmetic says it should. Something must supply work against:

- inertia;
- friction;
- springs;
- detents;
- gravity;
- contact forces;
- whatever load is coupled to the next stage.

One family of solutions transmits the operator's force directly through the calculation. Another stores small amounts of energy in springs, weights, or latched mechanisms and releases them when a boundary condition occurs.

The Pascaline's gravity-operated carry is an early example of separating the operator's immediate motion from the next digit's eventual step.

Later calculating machines developed many other carry mechanisms, each negotiating speed, force, wear, manufacturability, and reliability.

A complete history should not flatten those different solutions into one generic picture of 'gears doing arithmetic.'

## Carry is also a maintenance problem

Repeated boundary crossings concentrate wear.

If certain teeth, latches, or detents participate in every carry while other parts move only during direct digit entry, maintenance loads can be uneven.

A mechanism must tolerate:

- contamination and lubrication changes;
- wear that increases backlash;
- springs losing tension;
- shafts moving out of alignment;
- operators applying different amounts of force;
- transport and shock.

Pascal's insistence on durability and transportability is therefore not decorative marketing language. It identifies requirements that can alter the internal architecture.[^pascal-avis]

## Experiment: do not ask which radix 'wins'

The companion experiment deliberately refuses to output one universal best radix.

Instead it reports, for several bases:

- digits required for a chosen numerical range;
- average digit updates during repeated increments;
- average boundary carries;
- longest observed carry chain;
- a transparent synthetic cost function whose weights the user can change.

That lets us ask conditional questions such as:

> If each additional wheel is very expensive, what changes?

> If a carry transfer is much more expensive than holding another stable digit position, what changes?

> If high-radix detents are difficult to manufacture accurately, what changes?

The point is not to reconstruct Pascal's workshop numerically. The point is to make the hidden tradeoff visible.

## What this teaches us

Mechanical carry is a compact example of why computing history benefits from treating algorithms as physical processes.

A carry is simultaneously:

- a mathematical dependency;
- a control event;
- a transfer of energy;
- a timing problem;
- a possible worst-case cascade;
- a source of wear;
- a reason to change an algorithm;
- a reason to care about radix.

The Pascaline did not merely 'know how to add.' It embodied a policy for how arithmetic state should propagate through matter.

And once arithmetic becomes matter, `9999 + 1` stops being a trivial example.

It becomes a stress test.

## References

[^pascal-letter]: Blaise Pascal, *Lettre Dédicatoire à Monseigneur le Chancelier*, 1645, text in *Œuvres de Blaise Pascal*, Brunschvicg and Boutroux edition, Wikisource, https://fr.wikisource.org/wiki/%C5%92uvres_de_Blaise_Pascal/Lettre_D%C3%A9dicatoire_de_la_Machine_Arithm%C3%A9tique_et_Avis_n%C3%A9cessaire/Lettre

[^pascal-avis]: Blaise Pascal, *Avis nécessaire à ceux qui auront curiosité de voir la Machine Arithmétique, et de s'en servir*, 1645, text in *Œuvres de Blaise Pascal*, Brunschvicg and Boutroux edition, Wikisource, https://fr.wikisource.org/wiki/%C5%92uvres_de_Blaise_Pascal/Lettre_D%C3%A9dicatoire_de_la_Machine_Arithm%C3%A9tique_et_Avis_n%C3%A9cessaire/Avis

[^inria-pascaline]: ACONIT / Inria, “Histoire des machines : La Pascaline,” virtual computing museum, https://aconit.inria.fr/omeka/exhibits/show/histoire-machines/prehistoire/pascaline.html

[^chm-engines]: Computer History Museum, “The Engines,” Babbage Engine exhibit, https://www.computerhistory.org/babbage/engines

[^chm-how]: Computer History Museum, “How it Works,” Babbage Engine exhibit, https://www.computerhistory.org/babbage/howitworks/

## Source notes

Pascal's *Avis* is a primary text for his stated design goals and his own claims about the machine, but it is also promotional writing by the inventor. It should not be treated as an independent performance evaluation.

The ACONIT/Inria page is a museum synthesis describing surviving Pascaline mechanisms. The Babbage pages are modern museum syntheses grounded in the surviving drawings, artifacts, and reconstruction program.

The cross-era comparison to ripple-carry logic is explicitly a modern reconstruction analogy, not historical terminology attributed to Pascal or Babbage.
