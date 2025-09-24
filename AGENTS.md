# Repository Guidelines

## Project Structure & Module Organization
The repository mirrors the five-stage CopyCat workflow described in `README.md`. Keep curated source/reference frames inside `pipeline/01_dataset_curation/`, alignment scripts and renders in `pipeline/02_alignment/`, training assets under `pipeline/03_copycat_training/`, and final outputs in `pipeline/04_inference_render/` and `pipeline/05_matchgrade_render/`. Store your base `.nknc` template inside `nuke_base/` and duplicate it per reel. Capture research notes and parameter decisions in `notes/experiments.md`, and keep supporting reference material under `DOCS/` to avoid mixing it with production plates.

## Build, Test, and Development Commands
There is no traditional build step; everything runs through Nuke. Launch a stage directly with `nuke --nukex --script pipeline/02_alignment/<shot>.nk` while iterating, replacing `<shot>` with the shot identifier. Use `nuke --nukex --bg --script pipeline/03_copycat_training/<session>.nk` when you need to run CopyCat training headless; save the resulting log directory next to the session folder. For inference, `nuke --nukex --script pipeline/04_inference_render/<shot>_render.nk` keeps renders deterministic and ensures Write nodes inherit the relative paths checked into version control.

## Coding Style & Naming Conventions
Embedded Python knobs use 4-space indentation, `lower_snake_case` functions, and `CapWords` classes. Node names should retain the canonical forms from the template and append context when required (`Grade_matchRef`, `CopyCat_train`). Directory names stay lowercase with underscores; files that leave Nuke should follow `reel_stage_version.ext` to keep plates sortable. Avoid hard-coded absolute paths—always reference assets relative to the repository root.

## Testing Guidelines
Quality control is manual. Produce diagnostic renders per stage and store them in dated folders (`QC/2024-05-11/`) alongside screenshots. Compare ML recovery to the baseline documented in `pipeline/05_matchgrade_render/` before promoting changes. Log spectral artifacts, frame mismatches, and luma drift in `notes/experiments.md` with actionable follow-ups.

## Commit & Pull Request Guidelines
Commits are scoped by workflow stage: `alignment: adjust linked crop`, `copycat: refresh training pairs`. The message body should mention dataset updates, CopyCat hyperparameters, and the QC evidence reviewed. Pull requests need a concise summary, linked issue or task IDs, representative before/after frames (or paths to them), and a checklist of outstanding risks (untrained shots, pending approvals). Tag the next operator so ownership is explicit.

## Security & Configuration Tips
Store licensed or high-resolution scans outside the repository and reference them via relative mounts or environment variables. Clean temporary caches before pushing, and never commit CopyCat weight files unless explicitly approved for archival.
