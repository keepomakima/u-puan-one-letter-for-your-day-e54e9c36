"""One Letter for Your Day -- make.fun entry.

The program writes a single letter, "D", to /output/entry.txt and
nothing else. Only the Python standard library is used (os and sys);
there is no network access, no randomness, and the output is the
same on every run.

The letter: "D" stands for "doomscrolling" -- the word for a day
spent scrolling bad news in bed at 3 a.m. instead of sleeping. It
is a real initial of a real word for the day, and the word itself
paints a concrete picture (phone glow, 3 a.m., a thumb that will
not stop) rather than a vague mood. It is a self-own, which makes
it funny, and it is true of an ordinary night in 2026 far more
often than a night of literally zero sleep.

The competition gate requires /output/entry.txt to hold UTF-8 text
of exactly one character, and not only white space. A trailing
newline would count as a second character and fail the gate, so
the file is written with no newline: precisely one byte, "D".
"""

import os
import sys

DAY_LETTER = "D"

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def _check_letter(letter):
    """Return an error message if the letter breaks the gate, else None."""
    if len(letter) != 1:
        return "entry must be exactly one character, got %d" % len(letter)
    if letter != letter.strip():
        return "entry must not be only white space"
    if letter < "A" or letter > "Z":
        return "entry must be a capital letter A-Z, got %r" % letter
    return None


def _write_entry(letter):
    """Write the single letter with no trailing newline."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(letter)


def run():
    problem = _check_letter(DAY_LETTER)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    _write_entry(DAY_LETTER)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
