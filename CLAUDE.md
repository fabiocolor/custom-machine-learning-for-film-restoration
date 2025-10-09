# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **custom machine learning-based film restoration workflow template** using Foundry Nuke's CopyCat node with convolutional neural networks (CNNs). The repository documents reusable workflows for two complementary recovery approaches using supervised learning:

1. **Color Recovery** - Restoring missing or degraded color information in chromogenic film stocks
2. **Spatial Recovery** - Recovering spatial features (resolution, detail, grain) using three specialized techniques

**Academic Foundation:** Based on the paper "Exploring Experimental Machine Learning in Film Restoration" (Bedoya, 2024), which establishes the conceptual framework, methodology, and ethical principles for custom ML-based restoration.

## Architecture and Structure

The project follows a **5-stage pipeline structure** for both color and spatial recovery:

1. **Dataset Curation** (`pipeline/01_dataset_curation/`) - Select supervised learning pairs (degraded input + reference ground truth)
2. **Alignment** (`pipeline/02_alignment/`) - Pixel-level alignment of reference to source for supervised learning
3. **CopyCat Training** (`pipeline/03_copycat_training/`) - Train CNN model using supervised learning pairs
4. **Inference & Render** (`pipeline/04_inference_render/`) - Apply trained model frame-by-frame to full sequence
5. **Validation** (`pipeline/05_matchgrade_render/`) - Compare with traditional methods (MatchGrade for color, traditional filters for spatial)

### Color Recovery Approaches

**Reference-Based:**
- Uses DVDs, telecines, or other verifiable color-accurate sources
- Direct supervised learning from same film source

**Non-Reference:**
- Infers color from paintings, photographs, or manual references
- Used when no direct color reference exists

### Spatial Recovery Techniques

Based on academic paper, three specialized techniques:

1. **Gauge Recovery** - Transfer spatial characteristics between film gauges (16mm ↔ 35mm)
2. **Generation Recovery** - Align quality across film generations (print → negative)
3. **Analog Video Reference Recovery** - Two-step telecine-based process for partial damage recovery

### Key Directories

- `docs/` - Documentation including academic paper and workflow guides
  - `docs/spatial-recovery.md` - Three spatial recovery techniques
  - `docs/chroma-recovery.md` - Reference-based and non-reference color recovery
  - `docs/case-studies/` - Real-world examples with technique classifications
- `nuke_base/` - Store .nknc template files here
- `pipeline/` - Contains the 5-stage workflow directories (template structure)
- `notes/experiments.md` - Manual logging of changes, experiments, and reasoning

## Workflow Principles

**Core Philosophy (from academic paper):**
- **Recovery, not enhancement** - Restore what was originally there, never fabricate
- **Custom vs. General AI** - Small, film-specific models trained locally, not general-purpose AI (Runway, Sora, Pika Labs)
- **Supervised learning** - All training uses verified pairs (degraded input + reference ground truth)
- **Ethical data sourcing** - Only use authorized, verifiable reference material with proper provenance
- **Overcome filter limitations** - ML can "learn" from external references impossible for traditional spatial/temporal filters

**Implementation Principles:**
- **Film-specific models**: Train dedicated CNNs for each film/reel to preserve unique characteristics
- **Preservation-first**: Protect original spatial information (grain, texture, analog traits)
- **Transparency**: All training decisions documented in `notes/experiments.md`
- **Frame-by-frame inference**: Current hardware limitations make temporal models infeasible at consumer level
- **Local execution**: Models run on consumer hardware (Apple Silicon, NVIDIA GPUs)

## Film Damage Classification

Understanding damage types guides recovery approach selection:

**Intra-frame damage** (spatial recovery):
- Scratches, dust, dirt, stains
- Grain degradation, flicker
- Detail loss from physical damage or generation loss

**Inter-frame damage** (color recovery):
- Color fading across sequences (chromogenic dye degradation)
- Inconsistent color between scenes

## Development Notes

- This is primarily a **Nuke-based workflow** using .nk/.nknc files (not traditional software development)
- No package.json, build systems - this is a film restoration workflow template
- Repository designed for **project replication** and documentation
- Each pipeline stage maintains **node structure stability** for reproducibility
- Documentation should match academic paper's language, depth, and rigor
- Use proper terminology: **"spatial recovery"** (not "luma"), **"color recovery"** (not just "chroma")