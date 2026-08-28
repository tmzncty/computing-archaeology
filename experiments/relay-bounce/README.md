# Relay Bounce Experiment

Historical question:

> Why can one intended electromechanical switch operation create several logical events?

The script uses a **synthetic deterministic waveform** representing one closing relay contact that rebounds several times before remaining closed.

It then interprets that same waveform three ways:

1. count every rising edge;
2. ignore the transition and sample once after a chosen settling interval;
3. accept closure only after the state has remained continuously stable for a chosen interval.

## Run

```bash
python experiments/relay-bounce/relay_bounce.py
```

Change the qualification assumptions:

```bash
python experiments/relay-bounce/relay_bounce.py \
  --sample-after 3 \
  --stable-ms 1
```

## What it demonstrates

One intended closure can look electrically like:

```text
0 -> 1 -> 0 -> 1 -> 0 -> 1 ...
```

A naive edge counter can therefore record several events.

A receiving circuit that waits for settling or requires a stable state can turn the same messy physical transition into one logical decision.

The important insight is:

> **one physical operation equals one logical event only after the interface enforces that interpretation.**

## Synthetic timing warning

All bounce times in the script are invented teaching values.

They are **not** measurements of a Bell System relay, a Stibitz calculator, Harvard Mark I, Zuse machine, or any other historical device.

Historical bounce duration depends on relay construction, adjustment, drive, load, wear, temperature, and measurement criteria.

## What this does not model

It does not simulate:

- coil current;
- armature motion;
- spring mechanics;
- contact metallurgy;
- arcing;
- inductive loads;
- contact resistance;
- electrical noise;
- relay-to-relay inertia;
- actual historical debounce networks.

It isolates the **logic interpretation problem**.

## Source anchors

- *Telephony III* (1951 reissue), §9.4, which explicitly discusses contact bounce, circuit failures, contact life, and mechanical damping strategies.
- “Relays in the Bell System,” *Bell System Technical Journal* (1924), for the industrial scale of relay switching.
- Later FDA and military relay documentation for stable terminology and formal bounce testing, not for projected historical timing values.

Companion article:

[`../../docs/electromechanical/why-one-switch-can-look-like-many.md`](../../docs/electromechanical/why-one-switch-can-look-like-many.md)
