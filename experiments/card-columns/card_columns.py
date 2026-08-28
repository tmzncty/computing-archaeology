#!/usr/bin/env python3
"""Fixed-column punched-card source model.

This is a teaching model. It demonstrates why sequence fields and fixed-width
records are useful when program lines are physical records that can be shuffled.
"""

from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass(frozen=True)
class Card:
    source: str
    sequence: int

    def image(self) -> str:
        body = self.source[:72].ljust(72)
        seq = f"{self.sequence:08d}"[-8:]
        return body + seq


def make_deck(lines: list[str]) -> list[Card]:
    return [Card(line, (i + 1) * 10) for i, line in enumerate(lines)]


def recover(deck: list[Card]) -> list[Card]:
    return sorted(deck, key=lambda card: card.sequence)


def main() -> None:
    lines = [
        "C DEMONSTRATION PROGRAM",
        "      INTEGER I,S",
        "      S=0",
        "      DO 100 I=1,10",
        "      S=S+I",
        "  100 CONTINUE",
        "      PRINT *,S",
        "      END",
    ]
    deck = make_deck(lines)
    shuffled = deck[:]
    random.Random(1928).shuffle(shuffled)

    print("Original card images (72 source + 8 sequence):")
    for card in deck:
        print(repr(card.image()))

    print("\nAfter a synthetic dropped-deck shuffle:")
    print([card.sequence for card in shuffled])

    restored = recover(shuffled)
    print("Recovered by sequence field:")
    print([card.sequence for card in restored])

    assert restored == deck
    assert all(len(card.image()) == 80 for card in deck)
    print("\nEvery record is exactly 80 characters and deck order was recovered.")


if __name__ == "__main__":
    main()
