"""Tiny fab traceability model.

Not a MES, GEM, or GEM300 implementation.
"""

from dataclasses import dataclass


@dataclass
class Event:
    lot: str
    tool: str
    step: str
    status: str


def main():
    events = [
        Event("LOT-A", "ETCH-1", "poly-etch", "ok"),
        Event("LOT-B", "ETCH-1", "poly-etch", "excursion"),
        Event("LOT-C", "ETCH-1", "poly-etch", "unknown"),
        Event("LOT-A", "MET-2", "cd-measure", "ok"),
        Event("LOT-B", "MET-2", "cd-measure", "fail"),
        Event("LOT-C", "MET-2", "cd-measure", "review"),
    ]

    suspect_tool = "ETCH-1"
    suspect_started_at = 1
    exposed = []
    for i, event in enumerate(events):
        print(f"{i:02d} {event.lot:5s} {event.tool:7s} {event.step:12s} {event.status}")
        if event.tool == suspect_tool and i >= suspect_started_at:
            exposed.append(event.lot)

    print("\npossible exposure set:", sorted(set(exposed)))


if __name__ == "__main__":
    main()
