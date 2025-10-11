# CopyCat Chroma Recovery: Operator SOP

Step by step, tool exact instructions for running the chroma recovery pipeline in Nuke using CopyCat. This SOP matches the repository’s 5 stage layout and the images in `DOCS/images/`.

## Prerequisites
- NukeX Indie/Full for full res renders; Non Commercial caps at 1920×1080.
- GPU: Apple Silicon or NVIDIA recommended; enable GPU in CopyCat.
- Color mgmt: Resolve exports in Rec.709; Nuke final outputs in ACES 2065-1.
- Paths: Use repository relative paths only; avoid absolute mounts.

## Stage 1: Dataset Curation (pipeline/01_dataset_curation)
Goal: pick representative frame pairs (source vs reference) after Resolve alignment.

Checklist
- Read nodes: Balanced source (`Read2`) and color reference (`Read3`).
- `FrameRange`: set 1 to 1 for each candidate frame; feed `FrameHold` nodes.
- `AppendClip`: assemble 3 to 4 frames minimum (begin, mid, end; 4 preferred).
- Verify: For each index, source and reference show identical content (luma), ignoring color.
- Save QC grabs to `pipeline/01_dataset_curation/QC/YYYY-MM-DD/` and log in `notes/experiments.md`.

Reference
- Screenshot: `DOCS/images/DATASET CURATION cropped.png`
- FrameRange: `DOCS/images/FRAME RANGE NODE SETTINGS CROPPED.png`

## Stage 2: Alignment (pipeline/02_alignment)
Goal: pixel accurate registration of reference to source, then linked crop.

Checklist
- Auto path: `F_Align` (default settings) with analysis region constrained to valid area.
- Manual path: `Transform` with keyed translate/scale when auto fails.
- Compare: `Merge (difference)` for alignment accuracy.
- Switch: `Dissolve` → 0 = auto, 1 = manual.
- Crop: Remove all black borders and subtitles; link/clone crop to both streams; keyframe if subtitles appear/disappear.
- Ensure identical crop boxes on source/reference; copy bbox where needed.

Reference
- Alignment overview: `DOCS/images/ALIGNMENT cropped.png`
- F_Align UI: `DOCS/images/F_ALIGN NODE CROPPED.png`
- Dissolve: `DOCS/images/DISSOLVE NODE SETTINGS CROPPED.png`
- Crop examples: `DOCS/images/CROP NODE SETTINGS CROPPED.png`
- Copy bbox: `DOCS/images/COPYBBOX NODE SETTINGS.png`

## Stage 3: CopyCat Training (pipeline/03_copycat_training)
Goal: train chroma only model; preserve original luma.

Node chain (per both branches unless noted)
1) Colorspace: Linear → YCbCr (YUV). See `DOCS/images/COLORSPACE NODE LINEAR TO YCBCR SETTINGS CROPPED.png`
2) Shuffle: Build target with reference chroma (Cb/Cr) + source luma (Y); build input from source as degraded chroma.
3) Colorspace: YCbCr → Linear. See `DOCS/images/COLORSPACE NODE YCBCR TO LINEAR SETTINGS CROPPED.png`
4) Grade: clamp black/white to avoid <0 or >1. See `DOCS/images/GRADE NODE SETTING CROPPED.png`
5) Remove: strip alpha; train RGB only. See `DOCS/images/REMOVE NODE SETTINGS.png`
6) Copy bbox: keep consistent bbox

CopyCat node (recommended settings)
- Data directory: per shot folder under `pipeline/03_copycat_training/<shot>/session_*`
- GPU: enabled; device auto
- Model size: Medium
- Initial weights: None
- Batch size: 3 (fixed)
- Patch size: 512 (or 256 when subtitle crop reduces area)
- Steps/checkpoints: every 10,000; plan for 40 to 80k total
- Contact sheet: every 100 for monitoring

Rules of thumb
- Epoch heuristic: steps ≈ batch × 10,000 (e.g., batch 3 → ~30k minimum)
- If patch size is 256, extend total steps (e.g., 60k) for stability
- Increase dataset frames progressively if convergence stalls (4→7→11)
 - Content vs container: prefer the reference container with superior color for chroma training; normalize luma/spatial so only color differs. For spatial training, prefer the container with superior spatial detail and match color.

Reference
- Training layout: `DOCS/images/COPYCAT TRAINING cropped.png`
- Settings panel: `DOCS/images/COPYCAT SETTINGS cropped.png`
- Preview: `DOCS/images/COPYCAT SETTINGS PREVIEW cropped.png`
- Contact sheet: `DOCS/images/COPYCAT SETTINGS CONTACT SHEET cropped.png`
- Shuffle/Channels: `DOCS/images/SHUFFLE NODE SETTINGS CROPPED.png`

Monitoring
- Loss should trend down smoothly; watch for chroma ringing/bleed in contact sheets.
- Keep QC snapshots in `pipeline/03_copycat_training/QC/YYYY-MM-DD/`.

## Stage 4: Inference & Render (pipeline/04_inference_render)
Goal: apply trained model to full sequence and render archival plates.

Checklist
- Read full source sequence; apply only the “image cleanup” crop (remove sprockets/sound track).
- Inference node: load trained `.cat` file from Stage 3.
- Recombine/Clamp: match training chain; ensure final in ACES 2065-1.
- Write node: EXR DWAA, 16 bit half float, path `pipeline/04_inference_render/<shot>_ml_####.exr`.
- Non Commercial: reformat to 1080p if required; document this in notes.

Reference
- Inference layout: `DOCS/images/INFERENCE RENDER cropped.png`
- Inference node: `DOCS/images/INFERENCE NODE SETTINGS CROPPED.png`
- Reformat/Write: `DOCS/images/REFORMAT NODE SETTINGS CROPPED.png`, `DOCS/images/WRITE NODE SETTINGS.png`

## Stage 5: MatchGrade Baseline (pipeline/05_matchgrade_render)
Goal: produce LUT based baseline for comparison/QC.

Checklist
- Use the same dataset frames; convert Linear→Log before `MatchGrade` and Log→Linear after.
- Choose 3D LUT; Pre LUT = Log; LUT resolution max.
- Copy node to a separate tree to apply to the whole sequence.
- Render baseline plates for A/B in Resolve.

Reference
- MatchGrade: `DOCS/images/MATCHGRADE NODE SETTINGS CROPPED.png`
- Stage overview: `DOCS/images/MATCHGRADE RENDER OPTIONAL cropped.png`

## QC & Logging (all stages)
- Place screenshots/comps in `QC/YYYY-MM-DD/` inside the active stage folder.
- Log shot ID, frames, crop box, alignment path, model settings, findings in `notes/experiments.md`.
- Check specifically: spectral artifacts, frame mismatches, luma drift, grain retention.

## Shot by Shot vs Whole Reel
- Whole reel single session is faster to stand up but rarely optimal.
- Shot by shot yields better quality and stability; prefer this for final outputs.

## Common Pitfalls
- Misalignment: use `Merge (difference)`; switch to manual path if residual edges appear.
- Black borders/subtitles: must be cropped out before training; animate crop when needed.
- Bounding box mismatches: copy bbox to keep spatial metadata aligned.
- Over tuning F_Align: default global solves suffice; excessive tweaks can degrade results.
