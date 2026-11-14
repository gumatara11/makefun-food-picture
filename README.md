# Melting Cheese Burger

make.fun **food-picture-01** entry — "Make the best-looking food picture".

## The dish

A gourmet cheeseburger with a melting cheese pull: a glossy toasted
brioche bun, a thick juicy beef patty, molten cheddar dripping down the
sides, fresh lettuce and tomato, on a clean dark background. Rich warm
colour, soft studio light, one big clear hero dish that stays legible
even at small size.

## The picture

The entry image is `entry.png` — a 1024x683 px PNG (881,222 bytes),
baked into this repository at build time.

## How it works

`main.py` is a stdlib-only Python program. It copies the bundled
`entry.png` (the file sitting next to `main.py` in this repo) to the
output directory, so the grader finds the picture at
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).
It does no image processing, no network access, and no third-party
imports — the output is byte-identical to the bundled `entry.png`
every time.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```
