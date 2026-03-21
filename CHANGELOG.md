# Changelog

All notable changes to this repository are documented here.

## [Unreleased]

### Added
- GIF: contact sheet progression (17 milestones, Step 1 → 360k) showing CopyCat training convergence.
- GIF: inference output scrub — full-sequence playback demonstrating temporal consistency.
- GIF: spatial recovery proof of concept (El Tinterillo) — 4-way gauge/generation comparison.
- GIF: merge difference alignment check (extracted from video walkthrough).
- GIF: Mission Kill spatial recovery preview (16mm vs. 35mm vs. ML result).

### Changed
- Restructured documentation: consolidated shared stages (0–2) into `start-here.md`, removed duplication from branch docs.
- Chroma and spatial recovery docs now cover only branch-specific content (Stages 3–5) and link back to shared workflow.
- Organized images into `cropped/` and `full/` subdirectories for clarity. Updated all doc references.
- Removed Annex A quick-reference sections (redundant with streamlined docs).
- Moved ACES/color management reference into `start-here.md` (single source of truth).
- Trimmed glossary to workflow-specific terms only.
- Marked provenance-metadata as future work.

## [0.1.0] - 2025-09-24

### Added
- Initial end-to-end workflow materials.
- Nuke templates (Indie and Non-Commercial editions).
- Supporting reference materials under `docs/`.

### Security
- Guidance to keep licensed scans and CopyCat weights out of the repo.
