# Why FinFET Wrapped the Gate Around the Channel

A planar MOSFET controls a conducting channel mainly from one surface. As the gate gets shorter, that geometry loses electrostatic authority: source and drain fields increasingly influence the channel that the gate is supposed to control.

FinFET changed the geometry instead of merely shrinking the old one.

## Historical record

UC Berkeley announced its FinFET prototype in November 1999. The university described a fork-shaped gate that straddled the channel so the channel could be controlled from both sides; the IEDM paper followed in December 1999.[^berkeley][^hu]

The important historical point is not that every later production FinFET was identical to that prototype. It is that multi-surface gate control became an explicit response to short-channel scaling pressure.

## Engineering reconstruction

A planar device asks one gate surface to control a channel whose source and drain are moving closer together.

A fin raises the channel out of the plane:

```text
planar:       gate
               |
          -----channel-----

FinFET:      | gate |
             | fin  |
             | gate |
```

The gate now acts on more of the channel perimeter. Better electrostatic control can reduce leakage and permit further gate-length scaling.

But geometry creates new constraints:

- fin width and height become process variables;
- fin patterning uniformity matters;
- parasitic resistance/capacitance move into new places;
- discrete fin count can quantize transistor width;
- local stress, corner shape, and work-function integration matter.

A transistor has become a three-dimensional manufactured object.

## Why this is archaeology

Architecture diagrams still draw a transistor as a symbol. Manufacturing had to replace that symbol with a narrow three-dimensional ridge whose surfaces were controlled within a process window.

The abstraction survived. The object underneath changed shape.

## Experiment

[`experiments/finfet-gate-control/finfet_gate_control.py`](../../experiments/finfet-gate-control/finfet_gate_control.py) uses a deliberately synthetic perimeter-control proxy to compare one-surface planar control with multi-surface fin control.

It is not a transistor simulator.

## Source caution

The Berkeley material is contemporary institutional reporting and bibliography evidence around the 1999 prototype. Later production adoption should be documented separately by manufacturer/process-node sources rather than projected backward onto the prototype.

[^berkeley]: UC Berkeley, “New world record, set by UC Berkeley's tiny new transistor,” 22 Nov. 1999, https://newsarchive.berkeley.edu/news/media/releases/99legacy/11-22-1999b.html
[^hu]: Chenming Hu publication list, entry for X. Huang et al., “Sub 50-nm FinFET: PMOS,” IEDM 1999, https://www.chu.berkeley.edu/publication/
