# Alignment — Detailed Node Recipe (from transcript)

Purpose: achieve pixel-accurate alignment of Reference to Source and propagate a linked crop so both branches share identical spatial metadata before training.

## Prerequisites
- Aligned EXR sequences exported from Resolve with identical dimensions and frame ranges (black borders on reference are acceptable pre-crop).
- Read nodes set to consistent colorspace.

## Node Graph Overview
- Two paths: Automatic (F_Align) and Manual (Transform). Choose via a `Dissolve` switch.
- QC via `Merge (difference)` to inspect residual misalignment.
- Final `Crop` linked/cloned to both branches.

## Step-by-Step Node Setup

1) Automatic alignment
- Node: `F_Align` (Reference to Source).
- ROI: fit to valid image region; avoid excessive tweaking.
- Enable: Translate, Scale, Rotate, Perspective.
- Guidance: leave most settings at defaults; over-tuning can degrade results.

2) QC: alignment residuals
- Node: `Merge` set to `difference` between aligned Reference and Source.
- Inspect edges, high-contrast detail for residual parallax/scale errors.

3) Manual fallback alignment
- Node: `Transform` on Reference.
- Keyframe `translate` and `scale` to match Source using the same `Merge (difference)` for feedback.

4) Path selection
- Node: `Dissolve` (0 = Automatic F_Align, 1 = Manual Transform).
- Use a single switch to choose which aligned reference continues downstream.

5) Linked crop (post-alignment)
- Node: `Crop` applied to both Source and aligned Reference; link/clone the same node so edits propagate.
- Goal: remove all black borders and any burned-in graphics/subtitles.
- Keyframe the crop if subtitles appear intermittently (e.g., trailers, TV versions).
- Tip: cropping a bottom sliver can preserve useful color content while excluding subtitles; ensure both branches use the identical crop.

6) BBox consistency
- Ensure both branches share the same bbox after crop; copy bbox if needed to avoid downstream artifacts.

## QC Checklist
- Merge(difference) shows minimal residuals across the frame.
- No black borders remain after the linked crop.
- Burned-in subtitles/logos excluded across all frames.
- BBox identical on both branches.

## Recommendations
- Default F_Align global solve usually suffices; resist per-parameter micro-tweaks.
- Prefer manual Transform only when auto fails or drifts.
- Keep alignment graph simple and well-labeled to reduce operator error.

## Cross-Reference
- Operator Quick Reference: see Annex A in `docs/chroma-recovery.md` and `docs/spatial-recovery.md` (Alignment stage)
- Resolve pre-alignment: `docs/references/resolve-dataset-curation-detailed.md`
