#!/usr/bin/env python3
"""Encode lossless WebP presentation copies; retain original PNG files.

Requires Pillow. This changes encoding, not artwork, dimensions, or pixels.
"""

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "docs" / "images"


def main() -> None:
    original_total = 0
    encoded_total = 0
    for source in sorted(IMAGES.glob("*.png")):
        destination = source.with_suffix(".webp")
        with Image.open(source) as image:
            reference = image.convert("RGBA" if "A" in image.getbands() else "RGB")
            reference.save(destination, format="WEBP", lossless=True, exact=True, method=6)
            with Image.open(destination) as encoded:
                if encoded.size != reference.size or encoded.convert(reference.mode).tobytes() != reference.tobytes():
                    raise ValueError(f"Pixel equality failed: {destination.name}")
        original_total += source.stat().st_size
        encoded_total += destination.stat().st_size
        print(f"{source.name}: {source.stat().st_size:,} -> {destination.stat().st_size:,} bytes; identical pixels")
    print(f"Total: {original_total:,} -> {encoded_total:,} bytes; originals retained")


if __name__ == "__main__":
    main()
