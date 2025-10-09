# Machine Learning-Based Film Recovery in Nuke

A comprehensive workflow template for using Foundry Nuke with CopyCat to create custom machine learning models for **both luma and chroma recovery** in film restoration. This approach trains small, targeted models specific to each film or reel, preserving the unique characteristics of the original material.

![Node Graph Overview](docs/images/NODE%20GRAPH%20OVERVIEW%20cropped.png)

---

## Quick Start

1. **Introduction** → Read below to understand both recovery approaches
2. **Chroma Recovery** → [docs/chroma-recovery.md](docs/chroma-recovery.md) - Restore missing or faded color information
3. **Luma Recovery** → [docs/luma-recovery.md](docs/luma-recovery.md) - Restore missing or degraded brightness/luminance
4. **Case Studies** → [docs/case-studies.md](docs/case-studies.md) - Real-world examples of both approaches
5. **Quick Reference** → [docs/copycat_sop.md](docs/copycat_sop.md) - Operator checklist and SOP

---

## Overview

### What This Template Provides

Two complementary machine learning approaches for film restoration in Nuke:

**🎨 Chroma Recovery**
- Restores missing or faded **color information**
- Trains models to reconstruct chroma (color channels) while preserving original luma
- Essential for color-faded films, damaged color negatives, or chroma loss

**💡 Luma Recovery**
- Restores missing or degraded **brightness/luminance information**
- Trains models to reconstruct luma (brightness channel) while preserving existing chroma
- Essential for damaged emulsion, brightness degradation, or luma channel loss

### Why Machine Learning in Nuke?

Traditional film restoration often relies on:
- Manual color grading tools (time-consuming, subjective)
- Generic filters (don't respect film-specific characteristics)
- One-size-fits-all approaches (lose unique film traits)

**Our ML approach offers:**

1. **🎯 Film-Specific Models** - Each model learns the unique grain, texture, and characteristics of a specific film
2. **🔬 Archival Integrity** - Uses ethically sourced reference material from the same film
3. **🤖 Transparent Process** - All training decisions are documented and reproducible
4. **🎨 Preserves Authenticity** - Maintains the original look and feel of the source material
5. **⚡ Efficient Workflow** - Once trained, models can be applied to entire sequences

---

## Recovery Procedures

### 🎨 Chroma Recovery Workflow

**When to use:** Color-faded films, chroma channel damage, color negatives with degraded color layers

**Process Overview:**
1. **Dataset Curation** - Select frames from faded source + color reference
2. **Alignment** - Precisely match reference to source
3. **CopyCat Training** - Train model to reconstruct chroma
4. **Inference & Render** - Apply to full sequence
5. **Validation** - Compare with traditional methods

**Detailed Guide:** → [docs/chroma-recovery.md](docs/chroma-recovery.md)

### 💡 Luma Recovery Workflow

**When to use:** Damaged emulsion, brightness degradation, luma channel damage, under/overexposed areas

**Process Overview:**
1. **Dataset Curation** - Select frames from damaged source + good reference
2. **Alignment** - Match brightness and contrast levels
3. **CopyCat Training** - Train model to reconstruct luma
4. **Inference & Render** - Apply to full sequence
5. **Validation** - Verify brightness and detail preservation

**Detailed Guide:** → [docs/luma-recovery.md](docs/luma-recovery.md)

---

## Case Studies

Real-world applications demonstrating both recovery approaches:

### Chroma Recovery Examples
- **[Candy Candy Opening - 16mm](docs/case-studies/candy-candy-opening.md)** - 16mm film color reconstruction
- **[Friends](docs/case-studies/friends-chroma-recovery.md)** - Film project chroma recovery
- **[Rebelión de Tapadas](docs/case-studies/rebelion-de-tapadas-chroma-recovery.md)** - Historical archival material
- **[Ben](docs/case-studies/ben-chroma-recovery.md)** - Manual reference creation
- **[Muralla Verde](docs/case-studies/muralla-verde-chroma-recovery.md)** - Trailer project
- **[Frontier Experience](docs/case-studies/frontier-experience-chroma-recovery.md)** - Film project

### Luma Recovery Examples
- **[Knights of the Trail](docs/case-studies/knights-trail-luma-recovery.md)** - Luma reconstruction
- **[El Tinterillo](docs/case-studies/tinterillo-luma-recovery.md)** - Comprehensive luma recovery

### Combined Recovery Examples
- **[Mission Kill](docs/case-studies/missionkill-combined-recovery.md)** - Both luma and chroma recovery

**All Case Studies:** → [docs/case-studies.md](docs/case-studies.md)

---

## Repository Structure

```
nuke-chroma-recovery-template/
├── README.md                              # This file - project overview
├── WORKFLOW_GUIDE.md                      # Detailed technical guide
├── docs/
│   ├── chroma-recovery.md                 # Chroma recovery workflow
│   ├── luma-recovery.md                   # Luma recovery workflow
│   ├── copycat_sop.md                     # Operator checklist
│   ├── case-studies.md                    # All case studies index
│   ├── case-studies/                      # Individual case studies
│   └── images/                            # Workflow images and examples
├── notes/
│   └── experiments.md                     # Project notes and QC log
├── nuke_base/                             # Store base .nknc templates
└── pipeline/                              # Stage-based pipeline templates
    ├── 01_dataset_curation/
    ├── 02_alignment/
    ├── 03_copycat_training/
    ├── 04_inference_render/
    └── 05_matchgrade_render/
```

---

## Getting Started

### Prerequisites
- Foundry Nuke with CopyCat node
- Source film material (scanned)
- Reference material (same film or compatible)
- Basic understanding of ML concepts (helpful but not required)

### First Project
1. Choose your recovery type: **Chroma** (color) or **Luma** (brightness)
2. Read the appropriate workflow guide
3. Review relevant case studies
4. Follow the SOP checklist
5. Start with dataset curation

### For Different Film Types

| Film Type | Recommended Recovery | Examples |
|-----------|---------------------|----------|
| Color-faded prints | Chroma Recovery | Candy Candy, Friends |
| Damaged negatives | Combined Recovery | Mission Kill |
| Brightness issues | Luma Recovery | Knights of the Trail, El Tinterillo |
| Historical material | Chroma Recovery (careful) | Rebelión de Tapadas |

---

## Technical Approach

### Machine Learning Strategy

**Small, Targeted Models:**
- Train specific models for each film/reel
- Avoid large, generic pre-trained models
- Preserve unique film characteristics

**Data-Driven Training:**
- Use reference material from the same film
- Curate representative frames
- Document all training decisions

**Quality Assurance:**
- Validate against traditional methods
- Compare side-by-side results
- Log all experiments and decisions

### CopyCat Node Configuration

Key settings for successful training:
- **Dataset Quality** - Representative frame selection
- **Alignment Accuracy** - Precise source-reference matching
- **Training Parameters** - Appropriate iterations and learning rates
- **Validation** - Regular testing during training

---

## Contributing

This template serves as a foundation for your film restoration work. Contributions are welcome through:
- **Case Studies** - Add your projects with documentation
- **Workflow Improvements** - Share optimized techniques
- **Documentation** - Enhance guides and examples
- **Tools** - Create utility scripts and templates

---

## License

This workflow template is provided for educational and research purposes in film preservation and restoration.

---

## Questions & Support

- **Technical Issues:** Check [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md)
- **Quick Reference:** See [docs/copycat_sop.md](docs/copycat_sop.md)
- **Real Examples:** Browse [case studies](docs/case-studies.md)
- **Project Notes:** Review [notes/experiments.md](notes/experiments.md)

---

**Start exploring:** [Chroma Recovery](docs/chroma-recovery.md) • [Luma Recovery](docs/luma-recovery.md) • [Case Studies](docs/case-studies.md)