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

The bundled picture is JPEG data (the competition reads the file by its
first bytes, and the name stays entry.png either way), so the copy is a
straight byte-for-byte copy with no re-encoding. The picture shows a
tonkotsu ramen bowl on a dark wooden table, shot square from a high
angle: wooden chopsticks lifting a tall, neat pull of glossy noodles
with creamy broth dripping, a vivid red chili-oil spiral across the
broth, an upright nori sheet at the left rim, a fan of seared chashu,
a jammy egg with its golden yolk dripping, and generous scallions and
sesame, steam curling through warm backlight.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    if sha256_of(SOURCE) != sha256_of(dest):
        print("error: copy does not match source", file=sys.stderr)
        return 1
    print(f"Wrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
