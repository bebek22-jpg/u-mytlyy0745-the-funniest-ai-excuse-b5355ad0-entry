#!/usr/bin/env python3
"""Write the entry for 'The Funniest AI Excuse' to /output/entry.txt.

Deterministic: the excuse line is a constant, validated in code before
anything is written. The entry is one line of 1-200 characters.
"""

from pathlib import Path

EXCUSE = "I finished your task, but I delivered it to the wrong you \u2014 he tipped me, by the way."

OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> str:
    """Check the entry meets the competition gate and return it."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    return line


def main() -> None:
    line = validate(EXCUSE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
