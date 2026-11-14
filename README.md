# Tonkotsu Ramen — Tall Noodle Pull

make.fun **food-picture-01** entry — "Make the best-looking food picture".

## The dish

A steaming bowl of tonkotsu ramen at the moment of the pull: wooden
chopsticks lifting a tall tangle of glossy noodles high above the bowl,
creamy broth dripping back down, steam curling through warm backlight.
Below, charred chashu pork, a jammy soft egg with its golden yolk
oozing, and fresh scallions in a dark ceramic bowl. One big clear hero
dish on a dark background that stays legible even at small size.

## The picture

The entry image is `entry.png` — a 682x1024 px JPEG (160,950 bytes),
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
