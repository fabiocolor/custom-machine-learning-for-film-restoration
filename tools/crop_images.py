#!/usr/bin/env python3
"""
Auto-crop margins from screenshots and optionally resize.

Usage examples:
  python3 tools/crop_images.py -o DOCS/images/cropped \
    "DOCS/images/NODE GRAPH OVERVIEW.png" \
    "DOCS/images/DATASET CURATION.png" \
    "DOCS/images/ALIGNMENT.png" \
    "DOCS/images/COPYCAT TRAINING.png" \
    "DOCS/images/INFERENCE RENDER.png" \
    "DOCS/images/MATCHGRADE RENDER OPTIONAL.png"

Options:
  --max-width: downscale to this width if larger (default: 1600)
  --tol: color tolerance for border detection (0-255, default: 18)
  --pad: pixels to keep around detected content (default: 6)
  --inset-pct: shrink bbox by this fraction of width/height after trim (default: 0)

Notes:
 - This trims uniform or near-uniform borders by sampling the 4 corners and
   computing a content bounding box where pixels differ from the corner color
   within a specified tolerance.
 - It then applies a small padding and optional inset percentage before saving.
"""
from __future__ import annotations

import argparse
import os
import sys
from typing import Tuple

from PIL import Image, ImageChops


def _clamp(v: int, lo: int, hi: int) -> int:
    return max(lo, min(hi, v))


def _rgb_distance(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> int:
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))


def _choose_bg_color(img: Image.Image) -> Tuple[int, int, int]:
    # Sample the 4 corners and choose the median by channel to be robust.
    w, h = img.size
    pts = [
        img.getpixel((0, 0))[:3],
        img.getpixel((w - 1, 0))[:3],
        img.getpixel((0, h - 1))[:3],
        img.getpixel((w - 1, h - 1))[:3],
    ]
    rs = sorted(p[0] for p in pts)
    gs = sorted(p[1] for p in pts)
    bs = sorted(p[2] for p in pts)
    # median of 4 = average of middle two
    r = (rs[1] + rs[2]) // 2
    g = (gs[1] + gs[2]) // 2
    b = (bs[1] + bs[2]) // 2
    return (r, g, b)


def detect_content_bbox(img: Image.Image, tol: int) -> Tuple[int, int, int, int]:
    # Convert to RGB to simplify comparisons
    if img.mode not in ("RGB", "RGBA"):
        base = img.convert("RGBA")
    else:
        base = img
    rgb = base.convert("RGB")

    bg = _choose_bg_color(rgb)
    # Create a mask where pixels differ from bg by more than tol
    # Efficient approach: compare against a solid bg image and threshold diff
    bg_img = Image.new("RGB", rgb.size, bg)
    diff = ImageChops.difference(rgb, bg_img)
    # Convert diff to a single channel (max of RGB) for thresholding
    # Split and take per-pixel max
    r, g, b = diff.split()
    max_rgb = ImageChops.lighter(ImageChops.lighter(r, g), b)
    # Threshold: content if above tol
    content = max_rgb.point(lambda v: 255 if v > tol else 0).convert("L")
    bbox = content.getbbox()
    if bbox is None:
        # Fallback to full image if nothing detected
        return (0, 0, img.width, img.height)
    return bbox


def expand_bbox(bbox: Tuple[int, int, int, int], pad: int, w: int, h: int) -> Tuple[int, int, int, int]:
    x0, y0, x1, y1 = bbox
    return (
        _clamp(x0 - pad, 0, w),
        _clamp(y0 - pad, 0, h),
        _clamp(x1 + pad, 0, w),
        _clamp(y1 + pad, 0, h),
    )


def inset_bbox(bbox: Tuple[int, int, int, int], inset_pct: float, w: int, h: int) -> Tuple[int, int, int, int]:
    if inset_pct <= 0:
        return bbox
    x0, y0, x1, y1 = bbox
    bw = x1 - x0
    bh = y1 - y0
    dx = int(round(bw * inset_pct))
    dy = int(round(bh * inset_pct))
    return (
        _clamp(x0 + dx, 0, w),
        _clamp(y0 + dy, 0, h),
        _clamp(x1 - dx, 0, w),
        _clamp(y1 - dy, 0, h),
    )


def process_image(path: str, out_dir: str, tol: int, pad: int, inset_pct: float, max_width: int) -> str:
    img = Image.open(path)
    bbox = detect_content_bbox(img, tol=tol)
    bbox = expand_bbox(bbox, pad=pad, w=img.width, h=img.height)
    bbox = inset_bbox(bbox, inset_pct=inset_pct, w=img.width, h=img.height)
    cropped = img.crop(bbox)

    # Downscale if wider than max_width
    if max_width and cropped.width > max_width:
        new_h = int(round(cropped.height * (max_width / float(cropped.width))))
        cropped = cropped.resize((max_width, new_h), Image.LANCZOS)

    os.makedirs(out_dir, exist_ok=True)
    base = os.path.basename(path)
    out_path = os.path.join(out_dir, base)
    # Preserve format by extension; default to PNG if unknown
    ext = os.path.splitext(base)[1].lower()
    fmt = None
    if ext in (".jpg", ".jpeg"):
        fmt = "JPEG"
        # Use quality for screenshots
        cropped.save(out_path, fmt, quality=92, optimize=True)
    else:
        fmt = "PNG"
        cropped.save(out_path, fmt, optimize=True)
    return out_path


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Auto-crop margins from screenshots and optionally resize.")
    p.add_argument("images", nargs="+", help="Input image paths")
    p.add_argument("-o", "--out-dir", default="DOCS/images/cropped", help="Output directory")
    p.add_argument("--max-width", type=int, default=1600, help="Downscale to this width if larger (0 to disable)")
    p.add_argument("--tol", type=int, default=18, help="Color tolerance for border detection (0-255)")
    p.add_argument("--pad", type=int, default=6, help="Pixels to keep around detected content")
    p.add_argument("--inset-pct", type=float, default=0.0, help="Shrink bbox by this fraction after trim")
    args = p.parse_args(argv)

    outputs = []
    for img_path in args.images:
        if not os.path.isfile(img_path):
            print(f"warning: file not found: {img_path}", file=sys.stderr)
            continue
        out = process_image(
            img_path,
            out_dir=args.out_dir,
            tol=args.tol,
            pad=args.pad,
            inset_pct=args.inset_pct,
            max_width=args.max_width,
        )
        outputs.append(out)
        print(f"cropped: {img_path} -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

