# Drum timing experiment

This dependency-free Python model accompanies [`docs/memory/why-drum-memory-made-programmers-wait.md`](../../docs/memory/why-drum-memory-made-programmers-wait.md).

## Historical question

If instructions live on a rotating drum, how much performance can be lost when the next instruction is physically in the wrong angular position?

IBM's 1955 IBM 650 brochure specifies a 12,500 rpm drum with 50 word locations per band. Those values are the defaults used here. They imply 4.8 ms per revolution and 96 microseconds per angular location.

## Run

```bash
python experiments/drum-timing/drum_timing.py
```

Try a different sequence of operation times:

```bash
python experiments/drum-timing/drum_timing.py \
  --latencies 2,7,12,3,4 \
  --loops 100
```

Or change the hypothetical drum:

```bash
python experiments/drum-timing/drum_timing.py \
  --slots 100 \
  --rpm 6000
```

## Model

An instruction occupies one angular slot. Its execution latency is expressed as an integer number of drum slots. While the instruction executes, the drum continues rotating.

The program compares two layouts:

1. **consecutive** — instructions are placed in neighboring slots;
2. **timing-aware** — a simple greedy placer tries to put each next instruction at the angular position expected when the previous instruction finishes.

The output separates execution time from rotational waiting time.

With the defaults, consecutive placement is deliberately bad. The example is designed to expose the mechanism, not to reproduce a historically representative IBM 650 program.

## What it demonstrates

- a numerical address can also encode physical timing when storage rotates;
- consecutive addresses are not necessarily fast;
- predictable latency can be scheduled around;
- instruction execution time and memory placement can become coupled;
- software tools can optimize physical storage geometry.

## What it does **not** demonstrate

This is **not**:

- an IBM 650 emulator;
- an implementation of SOAP or SOAP II;
- a cycle-accurate model of 650 operations;
- evidence that a historical program used the placements generated here;
- a model of tracks, head selection, branch behavior, I/O, arithmetic overlap, or all timing exceptions.

The experiment tests the engineering mechanism only. Historical claims remain grounded in the IBM brochure, SOAP documentation, and other cited sources in the article.

## Reference values

- IBM, *650 Magnetic Drum Data Processing Machine*, 1955: https://s3data.computerhistory.org/brochures/ibm.650.1955.102646125.pdf
- IBM, *Reference Manual: SOAP II for the IBM 650 Data Processing System*, 1957: https://www.bitsavers.org/pdf/ibm/650/24-4000-0_SOAPII.pdf
