
# Chroma Recovery Workflow Template for Nuke

This repository documents a reusable workflow for machine‑learning‑assisted chroma recovery in film restoration, implemented in Foundry Nuke with the CopyCat node. It captures the logic and purpose of each stage without project‑specific settings, serving as a foundation for consistent, adaptable restoration work.

![Node Graph Overview](docs/images/NODE%20GRAPH%20OVERVIEW%20cropped.png)

---

## Start Here
- Read the canonical workflow guide: [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md)
- Operator checklist and SOP: [docs/copycat_sop.md](docs/copycat_sop.md)
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

![Dataset Curation](docs/images/DATASET%20CURATION%20cropped.png)

### 2) Alignment (with linked Crop)
Align reference precisely to source so only chroma differs. Combine global F_Align with manual Transform for edge cases; use Dissolve to compare modes; apply a linked Crop for consistent framing.

![Alignment](docs/images/ALIGNMENT%20cropped.png)

### 3) CopyCat Training
Reconstruct chroma only while preserving original luma and detail. Replace reference luma with source luma, remove extra channels, clamp values, and train CopyCat on aligned pairs.

![CopyCat Training](docs/images/COPYCAT%20TRAINING%20cropped.png)

### 4) Inference & Render
Apply the trained model to the full sequence, remove non‑image areas (sprockets/audio), format for output, and render to the archival colorspace.

![Inference Render](docs/images/INFERENCE%20RENDER%20cropped.png)

### 5) MatchGrade Baseline (optional)
Compare ML recovery to Nuke’s MatchGrade using the same dataset frames as a baseline.

![MatchGrade Comparison](docs/images/MATCHGRADE%20RENDER%20OPTIONAL%20cropped.png)

---

## Docs Index
- Workflow guide: [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md)
- SOP/quick checklist: [docs/copycat_sop.md](docs/copycat_sop.md)
- **Case studies:** [docs/case-studies.md](docs/case-studies.md) - Real-world restoration examples
- Notes and QC log: [notes/experiments.md](notes/experiments.md)
- Reference images: [docs/images/](docs/images)

---

## Repository Structure
```
nuke-chroma-recovery-template/
├── README.md
├── WORKFLOW_GUIDE.md
├── docs/
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
