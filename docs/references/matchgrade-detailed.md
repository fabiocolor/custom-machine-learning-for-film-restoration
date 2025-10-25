# MatchGrade Baseline — Detailed (from transcript)

Purpose: produce a traditional color-matching baseline (3D LUT/CDL) for comparison against ML-based chroma recovery.

## Inputs
- Use the same curated frame indices used for CopyCat training (e.g., 4, 7, or 11 frames).
- Source: faded plate; Reference: color plate aligned to Source.

## Configuration

1) Pre-transform to log
- Apply `Linear → Log` to both Source and Reference before the MatchGrade node (Pre-LUT transform = Logarithmic).
- Rationale: stabilizes value ranges for LUT fitting.

2) MatchGrade modes
- `Match Grade Source`: often more accurate but can introduce artifacts.
- `Match Different Clip`: reduces artifacts in some cases but may be less accurate. Test both.

3) Transformation
- Use `3D LUT` for the transformation type (more expressive than CDL).
- LUT resolution: set to the maximum available in your Nuke version.

4) Post-transform back to linear
- After MatchGrade, convert `Log → Linear` to restore the working space.

## Applying to full shot/reel
- Build a separate tree for the entire sequence:
  - Source full sequence → `Linear→Log` → `MatchGrade` (copied from the frame-fit graph) → `Log→Linear` → `Crop` (remove borders) → optional `Reformat` (1080p if Non-Commercial) → `Write` (EXR, ACES 2065-1).
- Note: in some Nuke variants you can’t export LUTs; copy/paste the `MatchGrade` node into the render tree.

## Rationale and Limitations
- LUTs perform a mapping of existing values; severely faded or missing chroma cannot be reconstructed by LUTs alone.
- Use this step to demonstrate the delta between traditional color pipelines and ML-based recovery.

## Cross-Reference
- Operator Quick Reference: see Annex A in `docs/chroma-recovery.md` (Validation baseline)
- Chroma Recovery validation context: `docs/chroma-recovery.md`
