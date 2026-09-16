"""
image_effects.py — pixelate, smooth, or sharpen an image.

Setup (run once in your terminal):
    pip install pillow

Usage examples:
    python image_effects.py photo.jpg --pixelate 16
    python image_effects.py photo.jpg --smooth 4
    python image_effects.py photo.jpg --sharpen 2.5
    python image_effects.py photo.jpg --pixelate 20 --sharpen 1.5   (combine effects)

Each run writes a new file next to your original, e.g. photo_pixelated.jpg
"""

import argparse
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance


def pixelate(img: Image.Image, block_size: int) -> Image.Image:
    """Shrink the image way down, then blow it back up with no smoothing.
    block_size = how many pixels wide each 'block' should look (bigger = chunkier)."""
    small = img.resize(
        (max(1, img.width // block_size), max(1, img.height // block_size)),
        resample=Image.NEAREST,
    )
    return small.resize(img.size, resample=Image.NEAREST)


def smooth(img: Image.Image, radius: float) -> Image.Image:
    """Gaussian blur. radius controls how strong the smoothing is (try 1-8)."""
    return img.filter(ImageFilter.GaussianBlur(radius=radius))


def sharpen(img: Image.Image, factor: float) -> Image.Image:
    """Unsharp-mask style sharpening. factor: 1.0 = no change, 2.0-3.0 = strong."""
    enhancer = ImageEnhance.Sharpness(img)
    return enhancer.enhance(factor)


def main():
    parser = argparse.ArgumentParser(description="Pixelate, smooth, or sharpen an image.")
    parser.add_argument("image", help="Path to the input image (jpg/png)")
    parser.add_argument("--pixelate", type=int, metavar="BLOCK_SIZE",
                         help="Pixelate with this block size, e.g. 12, 20, 32")
    parser.add_argument("--smooth", type=float, metavar="RADIUS",
                         help="Apply Gaussian blur with this radius, e.g. 2, 5")
    parser.add_argument("--sharpen", type=float, metavar="FACTOR",
                         help="Sharpen by this factor, e.g. 1.5, 2.5")
    parser.add_argument("--out", type=str, default=None,
                         help="Optional explicit output filename")
    args = parser.parse_args()

    in_path = Path(args.image)
    img = Image.open(in_path).convert("RGB")

    applied = []
    if args.pixelate:
        img = pixelate(img, args.pixelate)
        applied.append(f"pixelated{args.pixelate}")
    if args.smooth:
        img = smooth(img, args.smooth)
        applied.append(f"smoothed{args.smooth}")
    if args.sharpen:
        img = sharpen(img, args.sharpen)
        applied.append(f"sharpened{args.sharpen}")

    if not applied:
        print("Nothing to do — pass at least one of --pixelate / --smooth / --sharpen")
        return

    if args.out:
        out_path = Path(args.out)
    else:
        suffix = "_".join(applied)
        out_path = in_path.with_name(f"{in_path.stem}_{suffix}{in_path.suffix}")

    img.save(out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
