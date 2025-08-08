
# Chroma Recovery Workflow Template for Nuke

This repository documents a reusable workflow for **machine learning assisted chroma recovery** in film restoration, implemented in Foundry Nuke with the CopyCat node.  
It captures the logic and purpose of each stage without project-specific settings, serving as a foundation for consistent, adaptable restoration work.

---

## Purpose and Rationale

The goal is to restore missing or degraded chroma in scanned film by training **small, targeted models** on curated source and reference material.  
This approach prioritizes:

1. **Archival Integrity** – Only use ethically sourced, verifiable references; avoid opaque pre-trained datasets.  
2. **Specificity** – Train for one film or reel to preserve unique grain, texture, and color traits.  
3. **Control** – Keep all workflow decisions transparent and reproducible.

---

## Workflow Stages

### 1. Dataset Curation
**Purpose:** Select representative frames from faded source and matching color reference.  
**Why:** The dataset defines what the model learns; mismatched or poor frames produce poor results.  
**Method:** Lock matching frames (`FrameHold`) and assemble them with `AppendClip`.

---

### 2. Alignment (with Crop)
**Purpose:** Align reference precisely to source so only chroma differs.  
**Why:** Misalignment creates false color edges and ghosting.  
**Method:**  
- Auto: `F_Align` with global settings.  
- Manual: `Transform` with keyframes for frame-by-frame fixes.  
- `Dissolve` toggles between auto and manual.  
- **Linked Crop** removes overscan/black borders and keeps framing consistent across source and reference.

---

### 3. CopyCat Training
**Purpose:** Train a model to reconstruct chroma only, preserving original luma and detail.  
**Why:** Prevents the model from altering texture or sharpness while restoring color.  
**Method:**  
- Replace reference luma with source luma.  
- Remove extra channels and clamp values.  
- Train CopyCat on aligned pairs.

---

### 4. Inference & Render
**Purpose:** Apply the trained model to the full sequence and output archival-ready files.  
**Why:** This is the final chroma-restored version for preservation or grading.  
**Method:**  
- Apply model to source sequence.  
- Remove non-image areas (sprockets, audio).  
- Format for output and render to archival color space.

---

### 5. MatchGrade Comparison (Optional)
**Purpose:** Compare ML-based recovery with Nuke’s built-in MatchGrade.  
**Why:** Provides a performance baseline for evaluating model output.  
**Method:** Use same dataset frames, apply grade to sequence, compare results.

---

## Key Principles
- **No fixed values** – Steps remain constant; parameters vary per project.  
- **Manual logging** – Record changes and reasoning in `notes/experiments.md` and commits.  
- **Consistency** – Keep node structure stable for reproducibility.  
- **Preservation-first** – All choices protect original image integrity.

---

## Repository Structure
```
nuke-chroma-recovery-template/
├── README.md
├── notes/experiments.md
├── nuke_base/                # Store your .nknc template here
├── pipeline/
│   ├── 01_dataset_curation/
│   ├── 02_alignment/
│   ├── 03_copycat_training/
│   ├── 04_inference_render/
│   └── 05_matchgrade_render/
└── tools/
```

---

## License
Currently unlicensed and private. All rights reserved until finalized.
