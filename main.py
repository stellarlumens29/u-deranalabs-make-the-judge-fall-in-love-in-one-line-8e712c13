#!/usr/bin/env python3
"""Make the Judge Fall in Love in One Line — make.fun bounty entry (u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13).

Writes the entry line to /output/entry.txt (or <argv[1]>/entry.txt).
Python standard library only. Deterministic: the same bytes on every run.
"""
import os
import sys

LINE = 'Every night my grandfather winds the same old clock, not to keep the time but to keep the house listening for him a little longer.'
MAX_CHARS = 240


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, limit {MAX_CHARS}"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
