#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes one line -- the funniest one-line review of my own Monday --
to entry.txt in the output directory. Standard library only.

Output dir: $MAKEFUN_OUTPUT_DIR when set, else /output.
"""
import os

LINE = (
    "My Monday: cold coffee, Wi-Fi slower than my motivation, "
    "and a 9 a.m. standup that outlasted my entire weekend."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
