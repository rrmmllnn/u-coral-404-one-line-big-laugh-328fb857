#!/usr/bin/env python3
"""One Line, Big Laugh — writes a single funny line to /output/entry.txt.

The line: a hotel bill joke. A concrete, specific scene (an itemised hotel
bill: $14 Wi-Fi, $9 water), and one twist at the end — the ghost haunting
room 204 is the only guest who was not charged, because he left a
five-star review. Tighter and more visual than the first draft's GPS line.
"""
import os

LINE = "My hotel charged $14 for Wi-Fi, $9 for water, and $0 for the ghost in room 204 — he left a five-star review."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
