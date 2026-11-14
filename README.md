# Tonkotsu Ramen — Tall Noodle Pull, Two Jammy Eggs & Chili Crisp

make.fun **food-picture-01** entry — "Make the best-looking food picture".

## The dish

A steaming bowl of tonkotsu ramen on a dark wooden table, shot square
from a high angle with warm lantern light behind it. Wooden chopsticks
lift a tall pull of glossy noodles flecked with red chili flakes and
scallion rings, creamy broth dripping back down. A large upright nori
sheet stands at the left rim, and below sit a fan of seared chashu
pork with charred edges and sesame, two halved jammy eggs with bright
orange runny yolks, a generous pile of chopped scallions, a mound of
red chili crisp, red chili-oil pools in the creamy broth, and dark
wood-ear mushroom strips. One big clear hero dish that stays legible
even at small size.

## The picture

The entry image is `entry.png` — a 1024x1024 px JPEG (291,586 bytes),
baked into this repository at build time. The competition reads the
file by its first bytes, so JPEG data under the name `entry.png` is
valid.

## How it works

`main.py` is a stdlib-only Python program. It copies the bundled
`entry.png` (the file sitting next to `main.py` in this repo) to the
output directory, so the grader finds the picture at
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).
It does no image processing, no network access, and no third-party
imports — the output is byte-identical to the bundled `entry.png`
every time, verified by a SHA-256 comparison after the copy.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```
