from __future__ import annotations

import importlib.util
import math
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "experiments" / "time-sharing" / "time_sharing.py"
README = SCRIPT.with_name("README.md")
CASE_STUDY = ROOT / "case-studies" / "ctss" / "from-batch-to-conversation.md"
SPEC = importlib.util.spec_from_file_location("time_sharing", SCRIPT)
if SPEC is None or SPEC.loader is None:  # pragma: no cover - importlib contract
    raise RuntimeError(f"could not load {SCRIPT}")
TIME_SHARING = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = TIME_SHARING
SPEC.loader.exec_module(TIME_SHARING)


class TimeSharingLoadTests(unittest.TestCase):
    def test_model_entry_points_reject_non_finite_values(self) -> None:
        invalid_values = (math.nan, math.inf, -math.inf)

        for invalid in invalid_values:
            with self.subTest(entry_point="per_user_offered_load", value=invalid):
                with self.assertRaisesRegex(ValueError, "positive finite"):
                    TIME_SHARING.per_user_offered_load(invalid, 1.0)
            with self.subTest(entry_point="build_requests", value=invalid):
                with self.assertRaisesRegex(ValueError, "positive finite"):
                    TIME_SHARING.build_requests(1, 1, 1.0, invalid)
            with self.subTest(entry_point="simulate_round_robin", value=invalid):
                with self.assertRaisesRegex(ValueError, "positive finite"):
                    TIME_SHARING.simulate_round_robin([], invalid)

    def test_simulator_rejects_non_finite_request_fields(self) -> None:
        with self.assertRaisesRegex(ValueError, "non-negative finite"):
            TIME_SHARING.simulate_round_robin(
                [TIME_SHARING.Request(math.nan, 0, 0, 1.0)], 1.0
            )
        with self.assertRaisesRegex(ValueError, "positive finite"):
            TIME_SHARING.simulate_round_robin(
                [TIME_SHARING.Request(0.0, 0, 0, math.inf)], 1.0
            )

    def test_nominal_load_matches_fixed_arrivals_at_saturation(self) -> None:
        requests = TIME_SHARING.build_requests(
            users=1,
            rounds=4,
            request_interval=1.0,
            cpu_burst=1.0,
        )
        metrics = TIME_SHARING.simulate_round_robin(requests, quantum=1.0)

        self.assertEqual(
            [request.arrival for request in requests], [0.0, 1.0, 2.0, 3.0]
        )
        self.assertEqual(TIME_SHARING.per_user_offered_load(1.0, 1.0), 1.0)
        self.assertEqual(TIME_SHARING.offered_load(1, 1.0, 1.0), 1.0)
        self.assertEqual(metrics.completed, 4)
        self.assertEqual(metrics.cpu_utilization, 1.0)
        self.assertEqual(metrics.makespan, 4.0)

    def test_load_boundary_tracks_adjacent_cpu_bursts(self) -> None:
        below = math.nextafter(1.0, 0.0)
        above = math.nextafter(1.0, math.inf)

        self.assertLess(TIME_SHARING.offered_load(1, below, 1.0), 1.0)
        self.assertEqual(TIME_SHARING.offered_load(1, 1.0, 1.0), 1.0)
        self.assertGreater(TIME_SHARING.offered_load(1, above, 1.0), 1.0)

    def test_default_nominal_load_matches_default_arrival_rate(self) -> None:
        requests = TIME_SHARING.build_requests(
            users=20,
            rounds=2,
            request_interval=10.0,
            cpu_burst=0.05,
        )
        first_interval = [request for request in requests if request.arrival < 10.0]

        self.assertEqual(len(first_interval), 20)
        self.assertEqual(TIME_SHARING.per_user_offered_load(0.05, 10.0), 0.005)
        self.assertEqual(TIME_SHARING.offered_load(20, 0.05, 10.0), 0.1)
        self.assertAlmostEqual(
            sum(request.cpu for request in first_interval) / 10.0,
            TIME_SHARING.offered_load(20, 0.05, 10.0),
        )

    def test_saturation_cli_reproducer_reports_queueing_pressure(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "-B",
                str(SCRIPT),
                "--users",
                "1",
                "--rounds",
                "4",
                "--think",
                "1",
                "--cpu",
                "1",
                "--quantum",
                "1",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertIn(
            "one user's offered load:      100.000% of one CPU", completed.stdout
        )
        self.assertIn(
            "aggregate offered load:      100.000% of one CPU", completed.stdout
        )
        self.assertIn("observed utilization:100.000%", completed.stdout)
        self.assertIn(
            "Interpretation: offered demand reaches/exceeds one CPU; "
            "queueing pressure is expected.",
            completed.stdout,
        )

    def test_think_help_defines_an_open_loop_request_interval(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--help"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertIn("--think SECONDS", completed.stdout)
        self.assertIn(
            "fixed seconds between request starts (open-loop)", completed.stdout
        )

    def test_cli_rejects_non_finite_values_without_hanging(self) -> None:
        for flag in ("--think", "--cpu", "--quantum"):
            for value in ("nan", "inf", "-inf"):
                with self.subTest(flag=flag, value=value):
                    completed = subprocess.run(
                        [sys.executable, "-B", str(SCRIPT), f"{flag}={value}"],
                        cwd=ROOT,
                        capture_output=True,
                        text=True,
                        timeout=2.0,
                    )

                    self.assertNotEqual(completed.returncode, 0)
                    self.assertIn("must be positive finite numbers", completed.stderr)

    def test_companion_docs_share_the_open_loop_contract(self) -> None:
        readme = README.read_text(encoding="utf-8")
        case_study = CASE_STUDY.read_text(encoding="utf-8")
        companion_section = case_study.split(
            "## Reconstruction: why slow humans create multiplexing opportunity", 1
        )[1].split("## What breaks the illusion", 1)[0]

        for document in (readme, companion_section):
            self.assertIn("start-to-start", document)
            self.assertIn("open-loop", document)
        self.assertNotIn("human think time", companion_section)
        self.assertNotIn("reserving a machine", companion_section)

    def test_default_output_reports_request_interval_and_keeps_simulation(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-B", str(SCRIPT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(
            completed.stdout,
            "Interactive sharing toy model\n"
            "users:                 20\n"
            "requests/user:         20\n"
            "request-start interval: 10.000 s\n"
            "CPU burst/request:     0.050 s\n"
            "round-robin quantum:   0.020 s\n"
            "\n"
            "one user's offered load:        0.500% of one CPU\n"
            "aggregate offered load:       10.000% of one CPU\n"
            "\n"
            "simulated shared CPU\n"
            "  completed requests:  400\n"
            "  mean response time:  0.0500 s\n"
            "  max response time:   0.0500 s\n"
            "  observed utilization: 10.023%\n"
            "  modeled makespan:    199.550 s\n"
            "\n"
            "Interpretation: substantial spare CPU capacity remains in this toy workload.\n",
        )


if __name__ == "__main__":
    unittest.main()
