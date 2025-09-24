
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
The repository README can render inline players for MP4s stored in the repo. These examples use relative paths with `?raw=1` so GitHub serves the media bytes directly. Playback is limited to collaborators if the repo is private.

### MKILL
COLOR-MATCHED-COMPARISON

<video controls preload="metadata" width="960" src="DEMOS - Exploración del Aprendizaje Automático Experimental en la Restauración de Películas/MKILL/COLOR-MATCHED-COMPARISON.mp4?raw=1"></video>

MKILL GAUGE MATCHING COMPARISON (x265)

<video controls preload="metadata" width="960" src="DEMOS - Exploración del Aprendizaje Automático Experimental en la Restauración de Películas/MKILL/MKILL GAUGE MATCHING COMPARISON_x265.mp4?raw=1"></video>

MKILL COLOR COMPARISON (x265)

<video controls preload="metadata" width="960" src="DEMOS - Exploración del Aprendizaje Automático Experimental en la Restauración de Películas/MKILL/MKILL COLOR COMPARISON _x265.mp4?raw=1"></video>

MKILL COLOR RECOVERY (x265)

<video controls preload="metadata" width="960" src="DEMOS - Exploración del Aprendizaje Automático Experimental en la Restauración de Películas/MKILL/MKILL COLOR RECOVERY _x265.mp4?raw=1"></video>

### REBELION DE TAPADAS
ROGER_REBELIONDELASTAPADAS_P3D65_NUKE-COMPARISON

<video controls preload="metadata" width="960" src="DEMOS - Exploración del Aprendizaje Automático Experimental en la Restauración de Películas/REBELION DE TAPADAS/ROGER_REBELIONDELASTAPADAS_P3D65_NUKE-COMPARISON.mp4?raw=1"></video>

REBELION FINAL COMPARISON (x265)

<video controls preload="metadata" width="960" src="DEMOS - Exploración del Aprendizaje Automático Experimental en la Restauración de Películas/REBELION DE TAPADAS/REBELION FINAL COMPARISON_x265.mp4?raw=1"></video>

### FRIENDS
FRIENDS COMPARISON (x265)

<video controls preload="metadata" width="960" src="DEMOS - Exploración del Aprendizaje Automático Experimental en la Restauración de Películas/FRIENDS/FRIENDS COMPARISON_x265.mp4?raw=1"></video>

FRIENDS COLOR RESULT (x265)

<video controls preload="metadata" width="960" src="DEMOS - Exploración del Aprendizaje Automático Experimental en la Restauración de Películas/FRIENDS/FRIENDS COLOR RESULT_x265.mp4?raw=1"></video>

### CANDY CANDY
CANDY CANDY OPENING 16MM COLOR (x265)

<video controls preload="metadata" width="960" src="DEMOS - Exploración del Aprendizaje Automático Experimental en la Restauración de Películas/CANDY CANDY/CANDY_CANDY_OPENING_16MM_COLOR_x265.mp4?raw=1"></video>

CANDY CANDY FINAL COMPARISON (x265)

<video controls preload="metadata" width="960" src="DEMOS - Exploración del Aprendizaje Automático Experimental en la Restauración de Películas/CANDY CANDY/CANDY CANDY FINAL COMPARISON_x265.mp4?raw=1"></video>

### FRONTIER EXPERIENCE
FRONTIER EXPERIENCE — COLOR

<video controls preload="metadata" width="960" src="DEMOS - Exploración del Aprendizaje Automático Experimental en la Restauración de Películas/FRONTIER EXPERIENCE/FRONTIER_EXPERIENCE-COLOR.mp4?raw=1"></video>

FRONTIER EXPERIENCE — COMPARISON

<video controls preload="metadata" width="960" src="DEMOS - Exploración del Aprendizaje Automático Experimental en la Restauración de Películas/FRONTIER EXPERIENCE/FRONTIER_EXPERIENCE-COMPARISON.mp4?raw=1"></video>

### KNIGHTS OF THE TRAILS
KNIGHTS COMPARISON

<video controls preload="metadata" width="960" src="DEMOS - Exploración del Aprendizaje Automático Experimental en la Restauración de Películas/KNIGHTS OF THE TRAILS/KNIGHTS COMPARISON.mp4?raw=1"></video>

### MURALLA VERDE
MURALLA-VERDE — TRAILER COMPARACIÓN

<video controls preload="metadata" width="960" src="DEMOS - Exploración del Aprendizaje Automático Experimental en la Restauración de Películas/MURALLA VERDE/MURALLA-VERDE-TRAILER_COMPARACION.mp4?raw=1"></video>

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
