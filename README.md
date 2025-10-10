# Custom Machine Learning for Film Restoration in Nuke

A comprehensive workflow template for training custom machine learning models using Foundry Nuke's CopyCat node and convolutional neural networks (CNNs) for **both spatial recovery and color recovery** in film restoration. This approach overcomes the limitations of traditional spatial and temporal filters by training small, film-specific models on ethically sourced data, preserving the unique analog characteristics of the original material.

![Node Graph Overview](docs/images/NODE%20GRAPH%20OVERVIEW%20cropped.png)

---

## Quick Start

1. **Introduction** → Read below to understand both recovery approaches
2. **Color Recovery** → [docs/chroma-recovery.md](docs/chroma-recovery.md) - Restore missing or faded color information using reference materials or inferred sources
3. **Spatial Recovery** → [docs/spatial-recovery.md](docs/spatial-recovery.md) - Transfer spatial features between different sources of the same content
4. **Case Studies** → [docs/case-studies.md](docs/case-studies.md) - Real-world examples of both approaches
5. **Quick Reference** → [docs/copycat_sop.md](docs/copycat_sop.md) - Operator checklist and SOP

---

## Overview

### What This Template Provides

Custom machine learning-based film restoration using supervised learning with convolutional neural networks (CNNs), addressing two fundamental types of film damage:

**🎨 Color Recovery**
- Restores missing or faded **color information** in chromogenic film stocks affected by dye degradation
- **Reference-based**: Trains models using DVDs, telecines, or other color-accurate sources
- **Non-reference**: Infers color from paintings, photographs, or manually created references
- Addresses **inter-frame damage**: Color fading across sequences

**💡 Spatial Recovery**
- Restores **spatial features** (resolution, sharpness, grain structure) lost to damage or generational degradation
- **Reference-based**: Transfers spatial characteristics from actual film sources (different gauges, generations, preservation elements like telecines/safety copies)
- Real-world projects often combine multiple source differences (e.g., 16mm print + 35mm internegative)
- Addresses **intra-frame damage**: Detail loss, degradation affecting individual frames
- **Note**: Non-reference spatial recovery (using commercial/open-source models) is outside the scope of this repository

### Why Custom ML for Film Restoration?

Custom ML complements traditional film restoration methods, addressing challenges previously deemed impossible or prohibitively costly:

**What traditional methods cannot do:**
- **Spatial and temporal filters** cannot "learn" from external references or apply knowledge across distant parts of a film
- **Traditional color correction** (LUTs, channel balancing) can make images more pleasing to view but cannot truly recover color information lost to degradation or fading. Limited by what exists in the channels (though frame-by-frame painting is theoretically possible but completely impractical)

**New value of multiple film elements:**
Custom ML gives new purpose to multiple copies or elements of the same film. Different prints, generations, or gauges can each contribute unique information to training, improving model accuracy and making previously "redundant" archive materials valuable for restoration.

**General-purpose AI tools (Runway, Sora, Pika Labs) fall short because:**
- **Aesthetic mismatch**: Trained on contemporary images, impose modern aesthetics, smooth out film grain
- **Homogenization**: Overfit to modern visual styles, erasing unique historical characteristics
- **Temporal inconsistency**: Struggle with frame-to-frame consistency, introduce artifacts and hallucinations
- **Lack of control**: Film archivists require precise control over restoration decisions
- **Ethical concerns**: Often trained on unauthorized datasets

**Custom ML models offer:**

1. **🎯 Film-Specific Training** - Small models trained on supervised learning pairs from the specific film being restored
2. **🔬 Ethical Data Sourcing** - Uses only authorized, verifiable reference material with proper provenance
3. **🤖 Transparent & Reproducible** - All training decisions documented, results reproducible
4. **🎨 Preservation of Authenticity** - Maintains original analog characteristics (grain, texture, flicker)
5. **⚡ Overcome Filter Limitations** - Can "learn" information from external references impossible for traditional filters
6. **🖥️ Locally Executed** - Small models run on consumer hardware, no cloud dependencies

---

## Recovery Procedures

### 🎨 Color Recovery Workflow

**When to use:** Chromogenic film stocks with dye fading, color negatives with degraded color layers, films requiring historical color reconstruction

**Approach:**
- **Reference-based recovery**: Uses DVDs, telecines, or other color-accurate sources to train supervised learning models
- **Non-reference recovery**: Infers color from paintings, period photographs, or manually created color references when no direct reference exists

**Process Overview:**
1. **Dataset Curation** - Select frame pairs: faded source + color reference (or inferred reference)
2. **Alignment** - Precisely match reference to source at pixel level
3. **CopyCat Training** - Train CNN model using supervised learning to reconstruct chroma while preserving original spatial information
4. **Inference & Render** - Apply trained model frame-by-frame to full sequence
5. **Validation** - Compare with traditional color grading methods (MatchGrade baseline)

**Detailed Guide:** → [docs/chroma-recovery.md](docs/chroma-recovery.md)

### 💡 Spatial Recovery Workflow

**When to use:** Films with generational loss, multiple sources of same content, gauge-related quality differences, damage requiring detail reconstruction

**Core Approach:**
Transfer spatial characteristics from better-quality sources to degraded targets using supervised learning with CNNs.

**Common Source Scenarios:**
- Multiple film gauges (16mm vs 35mm)
- Different generations (print, internegative, duplicate)
- Early preservation elements (telecines, safety copies made closer to original)
- Multiple prints/scans of varying quality
- **Combinations** (e.g., 35mm internegative + 16mm print = gauge + generation differences)

**Process Overview:**
1. **Source Identification** - Identify all available sources with different spatial qualities
2. **Overlap Detection** - Find common frames between sources for supervised learning pairs
3. **Dataset Curation** - Select overlapping frames representing spatial characteristics to transfer
4. **CopyCat Training** - Train CNN model to transfer spatial features (resolution, grain, sharpness)
5. **Application & Validation** - Apply frame-by-frame and validate spatial consistency

**Detailed Guide:** → [docs/spatial-recovery.md](docs/spatial-recovery.md)

---

## Case Studies

Real-world applications demonstrating both recovery approaches:

### Color Recovery Examples
- **[Candy Candy Opening - 16mm](docs/case-studies/candy-candy-opening.md)** - Reference-based recovery using DVD source
- **[Friends](docs/case-studies/friends-chroma-recovery.md)** - Reference-based color reconstruction
- **[Rebelión de Tapadas](docs/case-studies/rebelion-de-tapadas-chroma-recovery.md)** - Non-reference recovery using historical paintings
- **[Ben](docs/case-studies/ben-chroma-recovery.md)** - Manual reference creation approach
- **[Muralla Verde](docs/case-studies/muralla-verde-chroma-recovery.md)** - Trailer restoration
- **[Frontier Experience](docs/case-studies/frontier-experience-chroma-recovery.md)** - Telecine reference-based recovery

### Spatial Recovery Examples
- **[Mission Kill](docs/case-studies/missionkill-combined-recovery.md)** - 35mm internegative + 16mm print (gauge + generation + color recovery)
- **[El Tinterillo](docs/case-studies/tinterillo-spatial-recovery.md)** - Early telecine preservation element (two-step approach)
- **[Knights of the Trail](docs/case-studies/knights-trail-spatial-recovery.md)** - Multiple nitrate print sources with varying quality

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
1. Choose your recovery type: **Chroma** (color) or **Spatial** (resolution, grain, detail)
2. Read the appropriate workflow guide
3. Review relevant case studies
4. Follow the SOP checklist
5. Start with dataset curation

### For Different Film Types

| Film Type | Recommended Recovery | Examples |
|-----------|---------------------|----------|
| Color-faded prints | Chroma Recovery | Candy Candy, Friends |
| Multiple sources available | Spatial Recovery | Knights of the Trail, El Tinterillo |
| Complex degradation | Combined Recovery | Mission Kill |
| Historical material | Chroma Recovery (careful) | Rebelión de Tapadas |

---

## Technical Approach

### Machine Learning Methodology

This workflow employs **supervised learning** using **convolutional neural networks (CNNs)** implemented through Nuke's CopyCat node.

**Custom Model Philosophy:**
- **Small, film-specific models**: Train dedicated models for each film or reel (not generalized models)
- **Supervised learning pairs**: Training uses frame pairs (degraded input + reference ground truth)
- **Ethically sourced data**: All training data obtained with proper authorization and provenance
- **Locally executed**: Models run on consumer-grade hardware (Apple Silicon, NVIDIA GPUs)
- **Frame-by-frame inference**: Current hardware limitations make temporal models infeasible at consumer level

**Training Methodology:**
1. **Data Preparation** - Film digitized, damaged areas identified, reference materials prepared
2. **Model Training** - Small ML model trained on subset of frames (complexity determines frame count)
3. **Inference** - Trained model applied frame-by-frame to entire film
4. **Evaluation & Refinement** - Results evaluated, model refined iteratively to improve quality

**Advantages Over Traditional Methods:**
- Spatial and temporal filters operate only within/between neighboring frames
- ML models can "learn" from external references across entire films
- Can apply knowledge to distant parts of the film impossible for traditional filters
- Enables recovery tasks that traditional methods cannot accomplish

### CopyCat Node Configuration

Key technical settings for successful CNN training:
- **Dataset Quality** - Representative frame selection balanced across lighting, color, and damage conditions
- **Alignment Accuracy** - Pixel-level precise source-reference matching
- **Training Parameters** - Iterations and learning rates adjusted for footage complexity
- **Supervised Pairs** - Ground truth reference paired with degraded input
- **Validation** - Regular testing on held-out frames during training

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

**Start exploring:** [Color Recovery](docs/chroma-recovery.md) • [Spatial Recovery](docs/spatial-recovery.md) • [Case Studies](docs/case-studies.md)