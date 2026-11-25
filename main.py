#!/usr/bin/env python3
"""Midnight Fridge Roast - make.fun entry.

Writes one one-line roast of a smart fridge that refuses to open after
midnight to /output/entry.txt. Pure Python standard library only.
Deterministic: every run writes the exact same bytes.
"""

import os
import sys

LINE = "My smart fridge locks itself at midnight \u2014 apparently my leftovers have better security than my bank account."
OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def fail(message):
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def main():
    # Validate the gate in code: 1-200 characters, single line,
    # not only whitespace, valid UTF-8 (it is a str literal by construction).
    if not (MIN_CHARS <= len(LINE) <= MAX_CHARS):
        fail(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(LINE))
        )
    if not LINE.strip():
        fail("entry must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        fail("entry must be a single line (no newline or carriage return inside)")
    try:
        raw = LINE.encode("utf-8")
    except UnicodeEncodeError as exc:
        fail("entry is not valid UTF-8: %s" % exc)

    output_dir = os.path.dirname(OUTPUT_PATH)
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as exc:
        fail("cannot create output directory %s: %s" % (output_dir, exc))

    try:
        with open(OUTPUT_PATH, "wb") as f:
            f.write(raw)
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError as exc:
        fail("cannot write %s: %s" % (OUTPUT_PATH, exc))

    print("entry.txt: %d characters" % len(LINE))


if __name__ == "__main__":
    main()
