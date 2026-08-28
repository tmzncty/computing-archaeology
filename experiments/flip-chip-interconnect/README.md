# Flip-Chip Interconnect Geometry

This toy compares two idealized connection geometries on a square die:

- pads around the perimeter;
- a full area array.

Run:

```bash
python experiments/flip-chip-interconnect/flip_chip_interconnect.py
```

The calculation is intentionally crude. It ignores keep-out zones, power/ground allocation, substrate escape routing, bump metallurgy, thermal expansion, underfill, and real package design.

Its purpose is to expose the geometric pressure described in [`../../docs/packaging/why-flip-chip-shortened-the-interconnect.md`](../../docs/packaging/why-flip-chip-shortened-the-interconnect.md): distributing connections across die area can scale differently from relying only on edge pads.