# Changelog

All notable changes to this repository are documented here.

## [Unreleased]

### Website and research direction
- Reframed the project around two public research tracks: open-weight colour recovery and reference-trained CopyCat recovery.
- Made Qwen Image Edit the primary current research area, with a dedicated overview, workflow guide, downloads, and links to the SEAPAVAA 2026 evidence.
- Added a confidence-labelled route map separating demonstrated results, promising bounded routes, and unresolved temporal and high-resolution problems.
- Reorganised the website navigation so public research, practical workflows, case studies, and reference material have clear roles.
- Rewrote the automated training-pair page as a clear explanation of the method, evidence, and limits.
- Replaced the blue-purple visual treatment with a restrained warm research-publication design.
- Simplified the website navigation around current research, practical workflows, case studies, and resources.
- Rebuilt and revalidated the downloadable Qwen package with public-facing review guidance.
- Replaced the separate hand-maintained Spanish pages with automatically generated Spanish, French, German, Italian, Portuguese, Simplified Chinese, Japanese, and Hindi editions.
- Added a visible warning that generated translations are provided for accessibility, may contain errors, and do not replace the English edition.
- Clarified throughout the Qwen material that it is an ongoing research record whose workflows and conclusions will change as evidence develops.

### Added
- Public guide to preparing reliable training pairs from direct film matches and drifting video references, illustrated by the Frontier research.
- Case studies page (`docs/case-studies.md`) covering ten projects: Candy Candy, Beta, PSM, Friends, La Muralla Verde, Frontier Experience, Ben, Rebelion de las Tapadas, Knights of the Trail, and El Gran Tinterillo.
- IMAGE_CATALOG.md with descriptions for all image assets, organized by subject folder.
- Comparison GIFs for: Candy Candy, Beta, PSM, Friends, Frontier Experience, Ben, Rebelion de las Tapadas, Knights of the Trail, and El Tinterillo.
- GIF: contact sheet progression (17 milestones, Step 1 → 360k) showing CopyCat training convergence.
- GIF: inference output scrub — full-sequence playback demonstrating temporal consistency.
- GIF: merge difference alignment check (extracted from video walkthrough).

### Changed
- Restructured documentation: consolidated shared stages (0–2) into `start-here.md`, removed duplication from branch docs.
- Chroma and spatial recovery docs now cover only branch-specific content (Stages 3–5) and link back to shared workflow.
- Organized images into subject folders (per project + `cropped/`, `full/`, `nuke-ui/`, `workflow/`, `resolve-dctl/`, `general/`). Updated all doc references.
- Renamed 54 screenshot-timestamped files and 10 misnamed node-settings files to descriptive kebab-case names.
- Removed Annex A quick-reference sections (redundant with streamlined docs).
- Moved ACES/color management reference into `start-here.md` (single source of truth).
- Trimmed glossary to workflow-specific terms only.
- Marked provenance-metadata as future work.

## [0.1.0] - 2025-09-24

### Added
- Initial end-to-end workflow materials.
- Nuke Indie template.
- Supporting reference materials under `docs/`.

### Security
- Guidance to keep licensed scans and CopyCat weights out of public downloads and version control.
