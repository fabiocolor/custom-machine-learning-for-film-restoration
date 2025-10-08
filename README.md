
# Chroma Recovery Workflow Template for Nuke

This repository documents a reusable workflow for machine‑learning‑assisted chroma recovery in film restoration, implemented in Foundry Nuke with the CopyCat node. It captures the logic and purpose of each stage without project‑specific settings, serving as a foundation for consistent, adaptable restoration work.

![Node Graph Overview](DOCS/images/NODE%20GRAPH%20OVERVIEW%20cropped.png)

---

## Start Here
- Read the canonical workflow guide: [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md)
- Operator checklist and SOP: [DOCS/copycat_sop.md](DOCS/copycat_sop.md)
- Log decisions and QC notes: [notes/experiments.md](notes/experiments.md)

 

---

## Purpose and Rationale
Restore missing or degraded chroma in scanned film by training small, targeted models on curated source and reference material. This approach prioritizes:
1. Archival integrity — ethically sourced, verifiable references; no opaque pre‑trained data.
2. Specificity — per‑film or per‑reel models to keep grain, texture, and color traits.
3. Control — transparent, reproducible decisions end‑to‑end.

---

## Workflow Stages

### 1) Dataset Curation
Select representative frames from faded source and matching color reference. Lock matching frames (FrameHold) and assemble with AppendClip.

![Dataset Curation](DOCS/images/DATASET%20CURATION%20cropped.png)

### 2) Alignment (with linked Crop)
Align reference precisely to source so only chroma differs. Combine global F_Align with manual Transform for edge cases; use Dissolve to compare modes; apply a linked Crop for consistent framing.

![Alignment](DOCS/images/ALIGNMENT%20cropped.png)

### 3) CopyCat Training
Reconstruct chroma only while preserving original luma and detail. Replace reference luma with source luma, remove extra channels, clamp values, and train CopyCat on aligned pairs.

![CopyCat Training](DOCS/images/COPYCAT%20TRAINING%20cropped.png)

### 4) Inference & Render
Apply the trained model to the full sequence, remove non‑image areas (sprockets/audio), format for output, and render to the archival colorspace.

![Inference Render](DOCS/images/INFERENCE%20RENDER%20cropped.png)

### 5) MatchGrade Baseline (optional)
Compare ML recovery to Nuke’s MatchGrade using the same dataset frames as a baseline.

![MatchGrade Comparison](DOCS/images/MATCHGRADE%20RENDER%20OPTIONAL%20cropped.png)

---

## Docs Index
- Workflow guide: [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md)
- SOP/quick checklist: [DOCS/copycat_sop.md](DOCS/copycat_sop.md)
- Notes and QC log: [notes/experiments.md](notes/experiments.md)
- Reference images: [DOCS/images/](DOCS/images)

---

## Demos (Inline Players)
GitHub strips `<video>` tags in READMEs, so inline players may not render on the repository page even if they work in editors or previewers. Please view the demos on GitHub Pages instead:

- Live players: https://fabiocolor.github.io/nuke-chroma-recovery-template/demos.html

### MKILL
COLOR-MATCHED-COMPARISON

[View video](https://github.com/fabiocolor/nuke-chroma-recovery-template/releases/download/media-20251008-143010/mkill_color_matched_comparison_web.mp4)

MKILL GAUGE MATCHING COMPARISON (x265)

[View video](https://github.com/fabiocolor/nuke-chroma-recovery-template/releases/download/media-20251008-143010/mkill_mkill_gauge_matching_comparison_x265_web.mp4)

MKILL COLOR COMPARISON (x265)

[View video](https://github.com/fabiocolor/nuke-chroma-recovery-template/releases/download/media-20251008-143010/mkill_mkill_color_comparison_x265_web.mp4)

MKILL COLOR RECOVERY (x265)

[View video](https://github.com/fabiocolor/nuke-chroma-recovery-template/releases/download/media-20251008-143010/mkill_mkill_color_recovery_x265_web.mp4)

### REBELION DE TAPADAS
ROGER_REBELIONDELASTAPADAS_P3D65_NUKE-COMPARISON

[View video](https://github.com/fabiocolor/nuke-chroma-recovery-template/releases/download/media-20251008-143010/rebelion_de_tapadas_roger_rebeliondelastapadas_p3d65_nuke_comparison_web.mp4)

REBELION FINAL COMPARISON (x265)

[View video](https://github.com/fabiocolor/nuke-chroma-recovery-template/releases/download/media-20251008-143010/rebelion_de_tapadas_rebelion_final_comparison_x265_web.mp4)

### FRIENDS
FRIENDS COMPARISON (x265)

[View video](https://github.com/fabiocolor/nuke-chroma-recovery-template/releases/download/media-20251008-143010/friends_friends_comparison_x265_web.mp4)

FRIENDS COLOR RESULT (x265)

[View video](https://github.com/fabiocolor/nuke-chroma-recovery-template/releases/download/media-20251008-143010/friends_friends_color_result_x265_web.mp4)

### CANDY CANDY
CANDY CANDY OPENING 16MM COLOR (x265)

[View video](https://github.com/fabiocolor/nuke-chroma-recovery-template/releases/download/media-20251008-143010/candy_candy_candy_candy_opening_16mm_color_x265_web.mp4)

CANDY CANDY FINAL COMPARISON (x265)

[View video](https://github.com/fabiocolor/nuke-chroma-recovery-template/releases/download/media-20251008-143010/candy_candy_candy_candy_final_comparison_x265_web.mp4)

### FRONTIER EXPERIENCE
FRONTIER EXPERIENCE — COLOR

[View video](https://github.com/fabiocolor/nuke-chroma-recovery-template/releases/download/media-20251008-143010/frontier_experience_frontier_experience_color_web.mp4)

FRONTIER EXPERIENCE — COMPARISON

[View video](https://github.com/fabiocolor/nuke-chroma-recovery-template/releases/download/media-20251008-143010/frontier_experience_frontier_experience_comparison_web.mp4)

### KNIGHTS OF THE TRAILS
KNIGHTS COMPARISON

[View video](https://github.com/fabiocolor/nuke-chroma-recovery-template/releases/download/media-20251008-143010/knights_of_the_trails_knights_comparison_web.mp4)

### MURALLA VERDE
MURALLA-VERDE — TRAILER COMPARACIÓN

[View video](https://github.com/fabiocolor/nuke-chroma-recovery-template/releases/download/media-20251008-143010/muralla_verde_muralla_verde_trailer_comparacion_web.mp4)

---

## Repository Structure
```
nuke-chroma-recovery-template/
├── README.md
├── WORKFLOW_GUIDE.md
├── DOCS/
│   ├── copycat_sop.md
│   └── images/
├── notes/
│   └── experiments.md
├── nuke_base/                # store base .nknc template
└── pipeline/
    ├── 01_dataset_curation/
    ├── 02_alignment/
    ├── 03_copycat_training/
    ├── 04_inference_render/
    └── 05_matchgrade_render/
```

---

## Versioning
- Track changes in [CHANGELOG.md](CHANGELOG.md). Use commit scopes per stage (e.g., `alignment:`, `copycat:`).
- Tag stable checkpoints after QC review, e.g., `git tag -a v0.1.0 -m "first working template" && git push origin v0.1.0`.

---

## License
Currently unlicensed and private. All rights reserved until finalized.
