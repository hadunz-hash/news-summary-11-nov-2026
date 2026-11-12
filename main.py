#!/usr/bin/env python3
"""make.fun bounty: Write the best summary of 11 November's world news.

The entry is a program that writes one summary, in English, of the
world's news of Wednesday 11 November 2026 to /output/entry.txt.
The summary is held in summary.txt next to this file; this program
copies it there. No network. Deterministic: both runs write the
same bytes, and the summary is checked to fit the 1-2000 character
rule before anything is written.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    with open(os.path.join(HERE, "summary.txt"), "r", encoding="utf-8") as f:
        text = f.read()
    if not 1 <= len(text) <= 2000 or not text.strip():
        raise SystemExit(
            f"summary must be 1-2000 non-blank characters, got {len(text)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
