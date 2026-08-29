# Why LGA Sockets Became Precision Spring Machines

A modern desktop CPU socket looks like a plastic frame full of tiny metal hairs.

It is actually a high-density electromechanical machine.

## Historical record

Intel's LGA775 mechanical design guide describes a socket containing 775 contacts for I/O, power, and ground, with strict mechanical boundary conditions for motherboard and package integration.[^intel]

Moving the spring contact into the socket changed where mechanical complexity lived. The processor package could present flat lands while the socket supplied compliant contacts, load distribution, alignment, and repeated mating behavior.

Later reliability studies of LGA sockets treated corrosion and contact-resistance growth as system-level reliability concerns, including accelerated mixed-flow-gas testing of different socket contact constructions.[^calce]

## Hundreds of contacts must all work at once

A socket is a population problem.

If one contact has survival probability `p`, the probability that all `N` contacts are good is approximately:

```text
p^N
```

That does not describe real correlated failure, but it exposes the architectural pressure.

As pin count rises:

- dimensional tolerance tightens;
- load distribution matters more;
- board flatness matters more;
- package warpage matters more;
- contamination on one contact matters more;
- insertion and retention mechanics become more difficult.

## The load mechanism is part of the circuit

The socket does not merely locate the CPU.

Its retention hardware must create the right normal-force range across the array.

Too little force can produce unstable contact resistance.

Too much force can:

- damage package lands;
- deform the board;
- overstress socket contacts;
- increase insertion/retention problems.

The dependency becomes:

```text
load plate / lever / frame
-> package deformation
-> contact normal force distribution
-> contact resistance
-> power / signal integrity
```

Mechanical engineering has entered the electrical path.

## Power delivery makes contact resistance visible

Not every land carries a high-speed signal. Many contacts exist to distribute power and ground.

That is important because a small resistance increase under high current produces:

```text
voltage drop = I * R
heating      = I^2 * R
```

So contact metallurgy and force become part of processor power delivery.

## The socket is also replaceable infrastructure

Soldering the processor directly to the motherboard can reduce some connector penalties, but a socket provides other system values:

- replaceability;
- upgradeability;
- manufacturing separation;
- board rework;
- platform modularity.

The LGA socket therefore represents a deliberate trade:

> add a complex separable interface so the processor can remain a field-replaceable module.

## Engineering reconstruction

The experiment in [`../../experiments/lga-contact-array/`](../../experiments/lga-contact-array/) models a synthetic contact-force distribution across a large array and calculates how a small tail of weak contacts can dominate system yield.

It also includes a simple power-contact heating proxy.

The values are invented and do not represent LGA775 specifications.

## What became invisible

When a user drops a CPU into a socket, they inherit:

```text
spring metallurgy
plating
contact geometry
socket molding
pick-and-place / reflow
load plate
retention mechanism
board flatness rules
package warpage limits
contact resistance qualification
corrosion testing
```

The processor is removable because an entire precision-mechanics industry learned to make hundreds or thousands of microscopic springs behave as one reliable interface.

[^intel]: Intel, *LGA775 Socket Mechanical Design Guide*, circa 2005, https://www.intel.com/Assets/PDF/designguide/302666.pdf . The guide describes the 775-contact socket and platform mechanical boundary conditions.
[^calce]: S. Yang, J. Wu, and M. G. Pecht, “Reliability Assessment of Land Grid Array Sockets Subjected to Mixed Flowing Gas Environment,” *IEEE Transactions on Reliability* 58, no. 4 (2009), 634–640; abstract archived by CALCE, https://calcetalk.umd.edu/articles/abstracts/2009/Reliability_Assess_LandGridArray_abstract.html .
