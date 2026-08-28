# Serial Memory Latency Experiment

Historical question:

> What changes when stored information is continuously circulating and can be accessed only when it reaches one point?

This experiment models a ring of equally spaced word slots moving past one conceptual access point.

It is inspired by acoustic delay-line memory, but its default timings are **synthetic**. It is not an EDSAC, SEAC, UNIVAC, or CSIRAC emulator.

## Run

```bash
python experiments/serial-memory/serial_memory.py
```

Default model:

```text
32 word slots
0.05 ms per slot
one access point
requests: 0,1,7,3,31,2
```

The script reports:

- full circulation time;
- best, mean, and worst wait from the starting phase;
- wait for each requested word;
- how the circulation phase changes after each access.

Try a larger store:

```bash
python experiments/serial-memory/serial_memory.py \
  --slots 64 \
  --slot-ms 0.05 \
  --requests 0,63,1,62,2
```

Or place the access point at another phase:

```bash
python experiments/serial-memory/serial_memory.py --phase 17
```

## What this exposes

In an ideal circular serial store, an address is not continuously available.

If the requested slot is at the access point now, waiting is near zero in this model.

If it has just passed, the system waits almost a full circulation.

So two requests to the same physical memory can have very different latency depending on **phase**.

This is the core architectural fact behind the experiment.

## Synthetic timing warning

The default `0.05 ms` per slot is chosen only to make output easy to read.

Do **not** cite it as a historical delay-line timing.

Machine-specific timing requires machine-specific primary documentation and must account for actual word organization, pulse rate, recirculation design, and controller behavior.

## What this does not model

It does not simulate:

- sound propagation;
- mercury;
- piezoelectric transducers;
- pulse attenuation;
- regeneration;
- pulse shaping;
- thermal drift;
- multiple delay lines operating in parallel;
- historical word formats;
- read/write electronics;
- instruction timing;
- simultaneous accesses;
- real machine clocking.

The model isolates **serial topology** only.

## Source anchors

- Computer History Museum, delay-line memory exhibits and Storage Engine material.
- Smithsonian SEAC mercury delay-line object records.
- Museums Victoria CSIRAC hot-box object documentation.
- National Museum of Computing EDSAC Replica Project.

Companion article:

[`../../docs/memory/why-memory-was-a-tube-of-sound.md`](../../docs/memory/why-memory-was-a-tube-of-sound.md)
