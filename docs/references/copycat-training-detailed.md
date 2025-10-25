# `CopyCat` Training — Detailed Node Recipe (from transcript)

Purpose: precise, reproducible setup for chroma recovery training in Nuke `CopyCat` so that only color differs between input and target. This mirrors the transcript and fills gaps in the existing guides.

## Prerequisites
- Aligned, identical-resolution EXR plates for Source (faded) and Reference (good color), from Resolve.
- Linear working space in Nuke; consistent colorspace on Read nodes.
- GPU-enabled Nuke (Apple Silicon or NVIDIA).

## Node Graph Overview
- Two branches: `Source` and `Reference (Target)`.
- Normalize non-color differences so only chroma differs.

## Step-by-Step Node Setup

1) Reference pre-filter (optional but recommended)
- Node: `Median`
- Purpose: suppress dust/compression artifacts in video/telecine references.
- Size: start around 10; adjust per reference quality (lower if clean, higher if noisy).

2) Linked crop on both branches
- Node: `Crop` (clone/link the same crop to both Source and Reference).
- Purpose: remove overscan/edges and ensure identical bbox.

3) Convert both branches to YCbCr
- Node: `Colorspace` on Source and Reference.
- Transform: `Linear → YCbCr` (YUV). This separates luma (Y) from chroma (Cb/Cr).

4) Build the Ground Truth with Shuffle
- Goal: Ground Truth = Source luma (Y) + Reference chroma (Cb/Cr).
- Node: `Shuffle` (or `Copy`/`Shuffle` equivalent) with inputs:
  - A = Source (in YCbCr)
  - B = Reference (in YCbCr)
- Channel mapping (typical YCbCr packing in Nuke Colorspace):
  - Red   ← A.red   (Y from Source)
  - Green ← B.green (Cb from Reference)
  - Blue  ← B.blue  (Cr from Reference)
  - Alpha ← none/black

5) Convert the Ground Truth back to Linear
- Node: `Colorspace` on the Ground Truth output.
- Transform: `YCbCr → Linear`.

6) Clamp ranges on both Input and Ground Truth
- Node: `Grade` on both Source (Input) and the Ground Truth.
- Enable: Black clamp and White clamp to keep values within [0, 1].

7) Remove alpha channel on both
- Node: `Remove` → remove `alpha`.
- Rationale: `CopyCat` is most reliable with RGB-only training.

8) Copy bbox for consistency
- Node: `CopyBBox` (or `SetBBox`) → copy bbox from Reference to Source and the Ground Truth.
- Purpose: ensure identical spatial metadata; avoids processing artifacts.

9) Connect to `CopyCat`
- Input: the original Source RGB (post clamp/remove/bbox), i.e., degraded chroma with preserved luma.
- Target: the Ground Truth RGB (post clamp/remove/bbox), i.e., Source luma + Reference chroma.
- Result: Input and Target match in everything except color.

## Recommended `CopyCat` Settings
- Model: Medium
- GPU: enabled (Apple Silicon or NVIDIA)
- Patch: 512 (use 256 if crop-limited; increase steps accordingly)
- Batch: 3 (tune to VRAM)
- Steps: review checkpoints every 10k; plan 40k–80k total for most shots
- Dataset size: shots 3–9 pairs; scenes ~16; sequences 33+ (scale steps accordingly)
- Monitoring: use contact sheets; watch for chroma ringing/bleed

## QC and Validation
- Luma identity test: temporarily convert both Input and the Ground Truth to YCbCr and difference the red channel; it _should_ be ~0.
- Range check: verify no <0 or >1 values after clamps.
- BBox check: confirm identical bbox on both streams before training.
- Hold-out frames: validate on pairs not used for training.

## Notes and Rationale
- Median pre-filter stabilizes references with dust/compression without blurring edges like a generic blur would.
- Removing alpha avoids unintended channel learning; RGB-only training is more stable.
- Copying bbox prevents mismatches during training/inference.

## Related Images (optional)
- `docs/images_kebab/copycat-training.png`
- `docs/images_kebab/copycat-settings-preview.png`

## Cross-Reference to Existing Guides
- Operator Quick Reference: see Annex A in `docs/chroma-recovery.md` and `docs/spatial-recovery.md` (Stages 02–04). This document expands Stage 03 training details.
- Chroma Recovery: see `docs/chroma-recovery.md` for end-to-end context and case studies.

## Comparison Checklist (Transcript → Guides)
- Reference median pre-filter: detailed here (summarized in the quick-reference annex).
- Linked crop and bbox consistency: emphasized here; alignment/crop also summarized in the quick-reference annex.
- YCbCr conversion and channel mapping: high-level in the annex; full mapping shown here.
- Clamp and remove alpha: noted in the annex; rationale and placement detailed here.
- Input vs Ground Truth definition: clarified here to ensure only chroma differs.
- QC luma identity test: added here for quick validation.
