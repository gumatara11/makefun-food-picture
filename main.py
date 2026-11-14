#!/usr/bin/env python3
"""make.fun food-picture-01 entry program.

Copies the baked-in food picture (entry.png, sitting next to this script)
to the output directory so the grader can read it as /output/entry.png.

Usage:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The output directory defaults to /output/entry.png when the
MAKEFUN_OUTPUT_DIR environment variable is not set. The program is
deterministic and stdlib-only: it performs a plain binary copy, no
network access, no third-party imports, and always produces the exact
same bytes as the bundled entry.png. The copy is verified by comparing
SHA-256 hashes of the source and the written file.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    print(f"Wrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
