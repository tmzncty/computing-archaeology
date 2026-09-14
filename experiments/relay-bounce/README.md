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

## Follow the continuous logical state

The original three-way comparison asks only **when the first closure qualifies**.
Its "accepts one closure" line is not a count over the rest of the waveform.
Add `--trace` to follow the qualified output after that first acceptance:

```bash
python experiments/relay-bounce/relay_bounce.py --trace
python experiments/relay-bounce/relay_bounce.py --trace --stable-ms 0.30
python experiments/relay-bounce/relay_bounce.py --trace --stable-ms 7
```

The trace reuses the same waveform and adds no physical relay model. It shows
raw changes, candidate starts/cancellations, qualification deadlines, accepted
state changes and the observation horizon. It then compares raw and qualified
rising-edge counts. The unflagged output and original first-closure helper are
unchanged for valid inputs.

For the supplied **synthetic** waveform, the continuous policy gives:

| Required stable interval | Raw rising edges | Qualified rising edges | Qualified closure times |
| --- | --- | --- | --- |
| 0.30 ms | 4 | 4 | 1.30, 2.00, 2.85, 4.00 ms |
| 2.00 ms (default) | 4 | 1 | 5.70 ms |
| 7.00 ms | 4 | 0 | None observed by 10.00 ms |

At 0.30 ms, qualified openings at 1.65, 2.40 and 3.40 ms re-arm the output
between the four closures. Waiting is not automatically enough: this threshold
is shorter than several rebounds. With 2.00 ms, those candidates are cancelled
and the final raw closure at 3.70 ms qualifies at 5.70 ms. With 7.00 ms, the
candidate's 10.70 ms deadline lies beyond the trace: the result is **not yet
observed**, not a prediction that closure can never qualify.

### Exact policy and observation boundaries

- The qualified output starts open/0. Initialization is not an edge. The first
  raw sample is an observation, not a counted raw transition. If that sample
  is already 1, qualification can start there and later produce a logical rise.
- Samples describe a piecewise-constant binary signal. Both opening and closing
  must remain continuously stable for the same interval before changing the
  qualified output. Qualified opening permits a later closure to count again.
- A raw return to the qualified state cancels the pending candidate. Repeated
  samples of the same state neither reset its timer nor create another event.
- A reached deadline is handled **before** an input change at the same time:
  `deadline`, then `qualified-change`, then `raw-change`. This matches the
  existing helper's convention that a full interval ending at an edge qualifies.
- The final sample time is the observation horizon. Qualification at the
  horizon is included; qualification after it is not. A pending later deadline
  may still appear in the final row.
- `candidate` and `deadline` identify the candidate involved in each event.
  Cancellation and qualified-change rows retain that candidate for explanation;
  it is cleared immediately afterwards. A deadline row shows the old qualified
  state, and its following qualified-change row shows the new state.

The pure `trace_debounce(samples, stable_ms)` function returns an immutable
`DebounceTrace`, with `DebounceEvent` records and raw/qualified closure counts.
It does not modify the supplied `Sample` objects. It rejects empty or malformed
samples, non-integer/bool states, non-finite or negative times, non-increasing
timestamps, and non-finite/non-positive intervals. States must be integer 0 or
1; time/interval inputs must be finite Python integers or floats, not booleans.
The CLI also rejects non-finite sampling times and intervals.

Continuous timing uses `Fraction(str(value))`: the decimal spelling of each
input number defines its exact value. Deadline comparisons and sums do not use
an epsilon or rounding. CLI inputs are parsed as floats before that conversion;
this is not an arbitrary-precision decimal-input interface. Event times and
deadlines are returned as `Fraction` values and printed as exact terminating
decimals, with at least two decimal places. Display does not decide acceptance.
The original helper retains its float arithmetic for compatibility; the new
trace makes its own timing rule explicit.

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
