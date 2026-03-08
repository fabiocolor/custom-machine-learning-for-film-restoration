# Start Here: Shared Reference Workflow

This is the shared operational guide for the repository. Follow this page until the branch decision, then continue in the detailed guide for either chroma recovery or spatial recovery.

![Workflow overview](images_kebab/full-overview-comparison.png)
Figure 1 - End-to-end overview of the recovery workflow.

## How To Use This Repo

- [README.md](../README.md) is the project overview.
- This page covers the shared workflow up to the branch point.
- [chroma-recovery.md](chroma-recovery.md) is the detailed chroma branch.
- [spatial-recovery.md](spatial-recovery.md) is the detailed spatial branch.

If you are new to the repo, read this page first, then jump to the branch that matches the actual problem you are trying to solve.

## What Stays Shared

Both recovery modes share the same setup until the target-build stage:

- stabilize the source
- choose the strongest usable reference
- export both elements in the same container
- curate representative frame pairs
- align precisely and define a shared crop
- train a sequence-level model before splitting into shot fixes

![Raw source before balancing](images_kebab/muralla-verde-scan-27-35-preview.gif)
Figure 2 - Example of a source that should be technically balanced before training.

![Balanced source for training](images_kebab/muralla-verde-source-27-35-preview.gif)
Figure 3 - Balanced source plate used as a cleaner input to the workflow.

## 1. Prep Source And Reference Before Nuke

What matters most is not whether the reference is newer, sharper, or higher resolution. What matters most is whether it preserves better information for the problem you are solving.

Prepare both elements before training:

- technically balance the source
- remove severe flicker, dirt, or instability that would poison training
- clean the reference only enough to remove transfer artifacts that would mislead the model
- keep geometry, framing, and timing consistent between both exports

Rules:

- Keep the same frame range, framing, and resolution.
- Avoid creative grading.
- Fix interlacing, cadence problems, and obvious decode issues before training.

![Resolve reference prep](images_kebab/muralla-verde-reference-pre-alignment-timeline-resolve-cropped.png)
Figure 4 - Source and reference placed in the same Resolve container before Nuke.

## 2. Build A Clean Teaching Set In Nuke

Start with the template that matches your Nuke edition. Build a small teaching set from representative frames rather than throwing the whole sequence into training.

At this stage, both branches are still the same:

- verify project and `Read` node settings
- curate representative frames across the sequence
- align the reference with `F_Align` first
- check it with `Merge (difference)`
- fall back to a keyed `Transform` when auto-alignment fails
- define a shared crop that removes borders, subtitles, and empty container space

Good pairs are:

- frame-matched
- aligned well enough to compare cleanly
- diverse enough to cover lighting, materials, and difficult colors or textures

![Dataset curation](images_kebab/dataset-curation-cropped.png)
Figure 5 - Building paired training examples in Nuke.

![Alignment workflow](images_kebab/alignment-cropped.png)
Figure 6 - Auto and manual alignment paths inside the template.

![Crop node settings](images_kebab/crop-node-settings-cropped.png)
Figure 7 - Shared crop used to keep both branches in the same live picture area.

## 3. Branch At The Target Build

This is where the workflow diverges:

- Chroma recovery target: Source `Y` + Reference `Cb/Cr`
- Spatial recovery target: Reference `Y` + Source `Cb/Cr`

That is why the same template supports both branches. The layout is shared. The branch decision is which channels belong in the ground-truth target.

![Colorspace node settings](images_kebab/colorspace-node-linear-to-ycbcr-settings-cropped.png)
Figure 8 - Convert both branches to YCbCr before channel recombination.

![Shuffle node settings](images_kebab/shuffle-node-settings-cropped.png)
Figure 9 - `Shuffle` node used to build the ground-truth target.

## Shared Rules After The Branch

- Do not combine chroma and spatial recovery in the same target build.
- If you need both, validate one pass before attempting the second.
- Train sequence-level first, then split to smaller shot-level retrains only where needed.
- Run inference on the full source, not just the training subset.
- Compare against a simpler baseline such as `MatchGrade` so you can prove the model is doing something specific.

## What Usually Breaks Both Branches

- Training on an unstable source with flicker, dirt, or severe imbalance
- Trusting a bad reference just because it is higher resolution
- Keeping misaligned frames in the dataset
- Leaving borders, subtitles, or overlays inside the training area
- Expecting one model to solve every shot in a difficult sequence

## Continue In The Correct Branch

- Use [chroma-recovery.md](chroma-recovery.md) when detail is acceptable but color is faded, collapsed, or shifted.
- Use [spatial-recovery.md](spatial-recovery.md) when color is acceptable but detail, sharpness, or grain structure are weaker than the reference.
