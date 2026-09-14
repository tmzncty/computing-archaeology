from __future__ import annotations

from dataclasses import FrozenInstanceError
from fractions import Fraction
import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "experiments" / "relay-bounce" / "relay_bounce.py"
SPEC = importlib.util.spec_from_file_location("relay_bounce", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"could not load {SCRIPT}")
RELAY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = RELAY
SPEC.loader.exec_module(RELAY)


def waveform(*pairs):
    return [RELAY.Sample(time, state) for time, state in pairs]


def changes(result):
    return [(event.time_ms, event.qualified_state) for event in result.events
            if event.kind == "qualified-change"]


def expected_changes(*pairs):
    # Independent literal oracle, not computed from the production waveform.
    return [(Fraction(str(time)), state) for time, state in pairs]


class ContinuousDebounceTests(unittest.TestCase):
    def test_clean_closure_has_exact_immutable_event_snapshots(self):
        result = RELAY.trace_debounce(waveform((0, 0), (1, 1), (4, 1)), 2)
        actual = [(e.time_ms, e.kind, e.raw_state, e.qualified_state,
                   e.candidate_state, e.deadline_ms) for e in result.events]
        self.assertEqual(actual, [
            (0, "initial", 0, 0, None, None),
            (1, "raw-change", 1, 0, None, None),
            (1, "candidate-start", 1, 0, 1, 3),
            (3, "deadline", 1, 0, 1, 3),
            (3, "qualified-change", 1, 1, 1, 3),
            (4, "horizon", 1, 1, None, None),
        ])
        self.assertEqual((result.raw_closures, result.qualified_closures,
                          result.final_state, result.horizon_ms), (1, 1, 1, 4))
        self.assertIsInstance(result.events, tuple)
        self.assertTrue(all(isinstance(e.time_ms, Fraction) for e in result.events))
        with self.assertRaises(FrozenInstanceError):
            result.final_state = 0
        with self.assertRaises(FrozenInstanceError):
            result.events[0].raw_state = 1

    def test_bounce_cancels_old_deadline_and_starts_a_new_interval(self):
        result = RELAY.trace_debounce(
            waveform((0, 0), (1, 1), (2, 0), (3, 1), (6, 1)), 2,
        )
        self.assertEqual(changes(result), expected_changes((5, 1)))
        self.assertEqual([(e.time_ms, e.candidate_state, e.deadline_ms)
                          for e in result.events if e.kind == "candidate-cancel"],
                         [(2, 1, 3)])
        self.assertEqual([(e.time_ms, e.deadline_ms) for e in result.events
                          if e.kind == "candidate-start"], [(1, 3), (3, 5)])
        self.assertEqual((result.raw_closures, result.qualified_closures), (2, 1))

    def test_supplied_waveform_is_the_documented_synthetic_input(self):
        self.assertEqual([(s.time_ms, s.state) for s in RELAY.DEFAULT_WAVEFORM], [
            (0, 0), (1, 1), (1.35, 0), (1.70, 1), (2.10, 0),
            (2.55, 1), (3.10, 0), (3.70, 1), (10, 1),
        ])

    def test_short_threshold_qualifies_every_rebound_and_release(self):
        result = RELAY.trace_debounce(RELAY.DEFAULT_WAVEFORM, 0.30)
        self.assertEqual(changes(result), expected_changes(
            (1.30, 1), (1.65, 0), (2.00, 1), (2.40, 0),
            (2.85, 1), (3.40, 0), (4.00, 1),
        ))
        self.assertEqual((result.raw_closures, result.qualified_closures), (4, 4))
        self.assertFalse(any(e.kind == "candidate-cancel" for e in result.events))

    def test_default_threshold_has_one_accepted_closure(self):
        result = RELAY.trace_debounce(RELAY.DEFAULT_WAVEFORM, 2)
        self.assertEqual(changes(result), expected_changes((5.70, 1)))
        self.assertEqual((result.raw_closures, result.qualified_closures), (4, 1))
        self.assertEqual([e.time_ms for e in result.events if e.kind == "candidate-cancel"],
                         [Fraction("1.35"), Fraction("2.10"), Fraction("3.10")])

    def test_long_threshold_retains_pending_deadline_without_future_acceptance(self):
        result = RELAY.trace_debounce(RELAY.DEFAULT_WAVEFORM, 7)
        self.assertEqual(changes(result), [])
        self.assertEqual((result.qualified_closures, result.final_state), (0, 0))
        last = result.events[-1]
        self.assertEqual((last.kind, last.time_ms, last.candidate_state, last.deadline_ms),
                         ("horizon", 10, 1, Fraction("10.70")))
        self.assertTrue(all(e.time_ms <= result.horizon_ms for e in result.events))

    def test_genuine_release_rearms_a_second_operation(self):
        result = RELAY.trace_debounce(
            waveform((0, 0), (1, 1), (5, 0), (9, 1), (13, 1)), 2,
        )
        self.assertEqual(changes(result), expected_changes((3, 1), (7, 0), (11, 1)))
        self.assertEqual((result.raw_closures, result.qualified_closures), (2, 2))

    def test_short_release_does_not_rearm_or_double_count(self):
        result = RELAY.trace_debounce(
            waveform((0, 0), (1, 1), (5, 0), (6, 1), (10, 1)), 2,
        )
        self.assertEqual(changes(result), expected_changes((3, 1)))
        self.assertEqual((result.raw_closures, result.qualified_closures), (2, 1))
        cancel = next(e for e in result.events if e.kind == "candidate-cancel")
        self.assertEqual((cancel.time_ms, cancel.raw_state, cancel.qualified_state,
                          cancel.candidate_state, cancel.deadline_ms), (6, 1, 1, 0, 7))

    def test_redundant_observations_do_not_reset_or_emit_events(self):
        sparse = waveform((0, 0), (1, 1), (5, 0), (9, 0))
        dense = waveform((0, 0), (0.5, 0), (1, 1), (2, 1), (3, 1),
                         (4, 1), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0))
        self.assertEqual(RELAY.trace_debounce(sparse, 2), RELAY.trace_debounce(dense, 2))

    def test_initial_raw_state_is_not_an_edge_and_requires_observed_duration(self):
        for state in (0, 1):
            result = RELAY.trace_debounce(waveform((5, state)), 2)
            self.assertEqual((result.raw_closures, result.qualified_closures,
                              result.final_state), (0, 0, 0))
            self.assertEqual(changes(result), [])
        result = RELAY.trace_debounce(waveform((5, 1), (7, 1)), 2)
        self.assertEqual(changes(result), expected_changes((7, 1)))
        self.assertEqual((result.raw_closures, result.qualified_closures), (0, 1))

    def test_deadline_at_horizon_is_included_but_not_just_after(self):
        for horizon, count in ((2.999, 0), (3, 1)):
            with self.subTest(horizon=horizon):
                result = RELAY.trace_debounce(waveform((0, 0), (1, 1), (horizon, 1)), 2)
                self.assertEqual(result.qualified_closures, count)
        result = RELAY.trace_debounce(waveform((0, 0), (3, 1)), 2)
        self.assertEqual(changes(result), [])  # A last-instant edge has no dwell time.

    def test_decimal_deadline_precedes_same_time_input_edge(self):
        result = RELAY.trace_debounce(waveform((0, 0), (0.1, 1), (0.3, 0), (0.5, 0)), 0.2)
        self.assertEqual(changes(result), expected_changes((0.3, 1), (0.5, 0)))
        self.assertEqual([e.kind for e in result.events if e.time_ms == Fraction("0.3")],
                         ["deadline", "qualified-change", "raw-change", "candidate-start"])
        self.assertEqual(result.final_state, 0)

    def test_finer_decimal_precision_is_not_rounded_into_acceptance(self):
        samples = waveform((0, 0), (0.1, 1), (0.3, 0), (0.5, 0))
        result = RELAY.trace_debounce(samples, 0.20000000000000004)
        self.assertEqual(changes(result), [])
        self.assertEqual(RELAY._format_ms(Fraction("0.30000000000000004")),
                         "0.30000000000000004")
        self.assertEqual(RELAY._format_ms(Fraction("0.000001")), "0.000001")

    def test_finite_large_pending_deadline_does_not_overflow(self):
        result = RELAY.trace_debounce(waveform((0, 0), (1e308, 1)), 1e308)
        self.assertEqual(changes(result), [])
        self.assertEqual(result.events[-1].deadline_ms, Fraction("2e308"))
        self.assertEqual(RELAY._format_ms(result.events[-1].deadline_ms),
                         "2" + "0" * 308 + ".00")

    def test_trace_conserves_input_and_records_survive_later_list_changes(self):
        samples = waveform((0, 0), (1, 1), (4, 1))
        before = tuple(samples)
        result = RELAY.trace_debounce(samples, 2)
        self.assertEqual(tuple(samples), before)
        saved = repr(result)
        samples.append(RELAY.Sample(8, 0))
        self.assertEqual(repr(result), saved)

    def test_invalid_thresholds_are_rejected(self):
        for value in (0, -1, float("nan"), float("inf"), -float("inf"), True, False, "2", None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                RELAY.trace_debounce(waveform((0, 0), (5, 1)), value)

    def test_invalid_samples_are_rejected(self):
        bad = [None, [], [object()], [(0, 0)],
               waveform((-1, 0)), waveform((0, 0), (0, 1)), waveform((2, 0), (1, 1))]
        bad += [waveform((value, 0)) for value in
                (float("nan"), float("inf"), -float("inf"), True, "0", None)]
        bad += [waveform((0, state)) for state in (-1, 2, True, False, 1.0, "1", None)]
        for samples in bad:
            with self.subTest(samples=samples), self.assertRaises(ValueError):
                RELAY.trace_debounce(samples, 2)

    def test_legacy_helpers_still_return_start_not_acceptance_time(self):
        self.assertEqual(RELAY.rising_edges(RELAY.DEFAULT_WAVEFORM), 4)
        self.assertEqual(RELAY.state_at(RELAY.DEFAULT_WAVEFORM, 3), 1)
        self.assertEqual(RELAY.state_at(RELAY.DEFAULT_WAVEFORM, 3.1), 0)
        self.assertEqual(RELAY.first_stable_transition(RELAY.DEFAULT_WAVEFORM, 1, 2), 3.7)
        self.assertEqual(RELAY.first_stable_transition(RELAY.DEFAULT_WAVEFORM, 1, 0.3), 1)
        self.assertIsNone(RELAY.first_stable_transition(RELAY.DEFAULT_WAVEFORM, 1, 7))


class RelayCliTests(unittest.TestCase):
    def run_cli(self, *args, status=0):
        result = subprocess.run([sys.executable, "-B", str(SCRIPT), *args],
                                cwd=ROOT, capture_output=True, text=True, timeout=5)
        self.assertEqual(result.returncode, status, result.stderr)
        return result

    def test_default_stdout_remains_exactly_legacy_output(self):
        expected = "\n".join([
            "Synthetic relay contact waveform", "time (ms)  state", "---------  -----",
            "     0.00      0", "     1.00      1", "     1.35      0", "     1.70      1",
            "     2.10      0", "     2.55      1", "     3.10      0", "     3.70      1",
            "    10.00      1", "", "Three interpretations of one intended closure",
            "naive rising-edge counter:       4 events", "sample once at 5.00 ms:      state=1",
            "stable-for-2.00ms qualifier: accepts one closure at ~5.70 ms", "",
            "The waveform and timing thresholds are synthetic teaching values.",
            "They are not measurements of a specific historical relay.", "",
        ])
        result = self.run_cli()
        self.assertEqual(result.stdout, expected)
        self.assertEqual(result.stderr, "")

    def test_trace_cli_preserves_legacy_prefix_and_reports_golden_sequences(self):
        cases = [
            ("0.30", [("1.30", 1), ("1.65", 0), ("2.00", 1), ("2.40", 0),
                      ("2.85", 1), ("3.40", 0), ("4.00", 1)], 4),
            ("2", [("5.70", 1)], 1), ("7", [], 0),
        ]
        for threshold, expected, count in cases:
            with self.subTest(threshold=threshold):
                plain = self.run_cli("--stable-ms", threshold).stdout
                result = self.run_cli("--stable-ms", threshold, "--trace")
                self.assertEqual(result.stderr, "")
                self.assertTrue(result.stdout.startswith(plain + "\nContinuous qualified-state trace"))
                rows = [line.split() for line in result.stdout.splitlines()]
                actual = [(row[0], int(row[3])) for row in rows
                          if len(row) == 6 and row[1] == "qualified-change"]
                self.assertEqual(actual, expected)
                self.assertEqual([(Fraction(t), state) for t, state in actual],
                                 changes(RELAY.trace_debounce(RELAY.DEFAULT_WAVEFORM, float(threshold))))
                self.assertIn("raw rising edges: 4\n", result.stdout)
                self.assertIn(f"qualified rising edges: {count}\n", result.stdout)
                self.assertIn("only the first accepted closure", result.stdout)
                self.assertIn("synthetic policy, not a historical relay circuit", result.stdout)

    def test_cli_rejects_nonfinite_and_out_of_range_arguments_without_tracebacks(self):
        for flag, values in (("--stable-ms", ("nan", "inf", "-inf", "0", "-1")),
                             ("--sample-after", ("nan", "inf", "-inf", "-1"))):
            for value in values:
                for trace in ([], ["--trace"]):
                    with self.subTest(flag=flag, value=value, trace=trace):
                        result = self.run_cli(f"{flag}={value}", *trace, status=2)
                        self.assertEqual(result.stdout, "")
                        self.assertIn("error:", result.stderr)
                        self.assertNotIn("Traceback", result.stderr)

    def test_help_documents_optional_continuous_trace(self):
        result = self.run_cli("--help")
        self.assertIn("--trace", result.stdout)
        self.assertIn("continuous opening/closing qualification", result.stdout)


if __name__ == "__main__":
    unittest.main()
