# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Nuke chroma recovery workflow template** for machine learning-assisted film restoration. The repository documents a reusable workflow for restoring missing or degraded chroma in scanned film using Foundry Nuke with the CopyCat node.

## Architecture and Structure

The project follows a **5-stage pipeline structure** where each stage builds upon the previous:

1. **Dataset Curation** (`pipeline/01_dataset_curation/`) - Select representative frames from faded source and matching color reference
2. **Alignment** (`pipeline/02_alignment/`) - Align reference precisely to source with crop to remove overscan
3. **CopyCat Training** (`pipeline/03_copycat_training/`) - Train ML model to reconstruct chroma while preserving original luma
4. **Inference & Render** (`pipeline/04_inference_render/`) - Apply trained model to full sequence and output archival files
5. **MatchGrade Comparison** (`pipeline/05_matchgrade_render/`) - Optional baseline comparison with Nuke's built-in MatchGrade

### Key Directories

- `nuke_base/` - Store .nknc template files here
- `pipeline/` - Contains the 5-stage workflow directories (currently empty template structure)
- `tools/` - Utility scripts and tools
- `notes/experiments.md` - Manual logging of changes, experiments, and reasoning

## Workflow Principles

- **Template-based**: This is a template repository - no fixed parameter values, only consistent workflow steps
- **Manual documentation**: All changes and reasoning must be logged in `notes/experiments.md` and git commits
- **Preservation-first**: All workflow decisions prioritize protecting original image integrity
- **Archival integrity**: Only use ethically sourced, verifiable references; avoid opaque pre-trained datasets
- **Specificity**: Train models for one film/reel to preserve unique grain, texture, and color traits

## Development Notes

- This is primarily a **Nuke-based workflow** using .nk/.nknc files (not currently present in template)
- No package.json, build systems, or traditional development commands - this is a film restoration workflow template
- The repository structure is designed for **project replication** rather than software development
- Each pipeline stage maintains **node structure stability** for reproducibility
- Focus on **small, targeted ML models** rather than large pre-trained datasets