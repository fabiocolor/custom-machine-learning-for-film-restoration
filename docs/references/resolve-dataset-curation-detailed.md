# Resolve Pre-Alignment + Dataset Curation — Detailed (from transcript)

Purpose: normalize container differences in Resolve (res/frame rate) and curate representative frame pairs in Nuke so the training set is consistent and verifiable.

## Part A — Resolve Pre-Alignment & Export

1) Conform and align
- Timeline contains both Source (highest-quality scan) and Reference (telecine/DVD/print or constructed).
- Align Reference to Source timing; match frame rate and resolution. Black borders on the Reference are acceptable at this stage.

2) Export EXR sequences
- Render Source and Reference as EXR sequences with identical resolution and matching channel sets.
- Keep colorspace consistent with Nuke Read nodes (common: Rec.709 gamma 2.4 for training pairs to maintain 0–1 ranges, or linear with careful clamping later).

## Part B — Dataset Curation in Nuke

1) Shot vs reel granularity
- Reel-wide sessions can be attempted but usually underperform.
- Recommended: shot-based projects (VFX-style) for higher quality and easier iteration.

2) Select frames
- Default seed: 3–4 frames (begin, middle(s), end). Often 4 gives a better start (B, M1, M2, E).
- Escalation path: 4 → 7 → 11 frames by inserting midpoints between existing picks.

3) Build single-frame pairs
- Nodes: `FrameHold` for each chosen frame on both Source and Reference branches.
- Use `AppendClip` to assemble ordered pairs. Many workflows keep two `AppendClip` nodes (a maintenance buffer before the one referenced by downstream postage-stamps) to simplify edits.

4) Frame-by-frame verification (critical)
- For each pair index, compare Source vs Reference for identical composition/motion (ignore color).
- Use viewer wipe or `Merge (difference)` for certainty.
- If mismatch occurs, adjust selections until every pair truly corresponds.

5) Pass frames one at a time
- Keep each pair isolated (one frame per index) as it flows to training postage stamps; this avoids accidental blending across frames.

6) Iterate as needed
- If CopyCat convergence is weak, add more midpoints to increase dataset diversity.

## Practical Tips
- Document chosen frame indices and rationale in `notes/experiments.md`.
- Store QC contact sheets per shot/date under `pipeline/01_dataset_curation/QC/YYYY-MM-DD/`.

## Cross-Reference
- Operator Quick Reference: see Annex A in `docs/chroma-recovery.md` and `docs/spatial-recovery.md` (Dataset Curation)
- Alignment details: `docs/references/alignment-detailed.md`
