# Nuke Chroma Recovery Template

This repository is a companion to the chroma-recovery workflow shown in the YouTube video. It documents a practical way to recover color from faded film elements in NukeX with `CopyCat`, using a usable reference and a repeatable prep/training/inference pipeline.

It is not a one-click plugin. It is a documented workflow, with decisions, implementation notes, and a direct path through the process. Think of it as a living paper: a public working document for chroma-recovery experiments, examples, failures, refinements, and future directions.

[![Watch the YouTube walkthrough](docs/images_kebab/video_previews/color-recovery-video-preview.gif)](https://youtu.be/kXerjFGX9Kg)
Figure 1 — Click the preview GIF to watch the YouTube walkthrough.

![Workflow overview](docs/images_kebab/full-overview-comparison.png)
Figure 2 — Recovery workflow overview.

## Start Here

If you are coming from the video, follow these pages in order:

1. [Start Here: Video Companion Workflow](docs/start-here.md)
2. [Detailed Chroma Recovery Workflow](docs/chroma-recovery.md)
3. [Watch the Latest Walkthrough](docs/watch-the-video.md)

Secondary material:

- [Spatial Recovery Workflow](docs/spatial-recovery.md) — experimental research, not yet presented as a finished restoration workflow
- [Provenance and Metadata](docs/provenance-metadata.md) — work in progress
- [Glossary](docs/references/terms-and-definitions.md)

## Who This Is For

- Archivists, preservation teams, and restoration practitioners who want to test chroma recovery on their own material
- People who are comfortable following a workflow, even if they are not deeply technical
- Researchers who want to track the current state of the method and its future direction

You do not need to be a machine-learning specialist to understand the workflow. The main requirement is careful preparation, patience, and a willingness to compare results critically.

## What This Repo Covers

- Recovering faded or missing chroma from damaged film elements
- Using a direct reference such as telecine, tape, DVD, or another film element
- Building training pairs in Nuke by combining Source luma with Reference chroma
- Training sequence-level models first, then fixing weak shots separately when needed
- Comparing ML output against simpler baselines such as `MatchGrade`

## Current Focus

- Active track: chroma recovery with Nuke `CopyCat`
- Presentation style: a living document with focused inline examples, GIFs, and before/after comparisons
- Near-term future: LoRA-based color recovery experiments
- On hold: spatial recovery as a finished workflow; it remains in the repo as research context only

## What You Need

- Foundry NukeX with `CopyCat` and `Inference`
- A faded or damaged source scan
- A usable reference with better color information
- Enough prep discipline to balance, clean, align, and export matched sequences before training

## What You Do Not Need

- You do not need to write code
- You do not need to train large foundation models
- You do not need to understand every mathematical detail before trying the workflow
- You do need to keep good notes and judge results carefully

## The Workflow in One Pass

1. Balance or lightly clean the source so the model is not learning severe flicker, dirt, or channel instability.
2. Find the best available reference. Older video transfers, telecines, DVDs, or other film elements can still be useful if they preserve the original color state better than the damaged scan.
3. In Resolve, align source and reference, place both in the same container, and export matched EXR sequences.
4. In Nuke, curate the training dataset, align the reference more precisely, and crop both branches identically.
5. Convert both branches to YCbCr, keep Source luma, replace chroma with Reference Cb/Cr, and use that result as the `CopyCat` target.
6. Train a broad sequence-level model first. If certain shots fail, build a smaller shot-level training set and retrain only for those problem shots.
7. Run inference on the full source, composite the recovered color back over the balanced source, and compare against a simpler baseline.

If that feels too dense, use [docs/start-here.md](docs/start-here.md). It explains the same process in a more practical and less technical way.

## Recommended Reading Path

### 1. Start with chroma, not spatial

The new video and the strongest material in this repo are about chroma recovery. Spatial recovery is still included, but the README now treats it as secondary so new users can get to a working result faster.

### 2. Use the video companion guide first

[docs/start-here.md](docs/start-here.md) is the shortest path through the repo. It mirrors the video structure and calls out the practical decisions that matter most.

### 3. Use the detailed workflow as reference

[docs/chroma-recovery.md](docs/chroma-recovery.md) is the full procedural guide once you are ready to build or troubleshoot a real project.

## Examples and Results

The old case-study pages have been removed because they were drifting away from the current workflow and creating confusion.

For current examples:

- Use the new video as the main walkthrough: [docs/watch-the-video.md](docs/watch-the-video.md)
- Expect short inline GIFs to be added to the workflow docs instead of standalone example pages
- Treat spatial-recovery examples as experiments until that workflow is revised further
- Reuse older project results only when they clarify one specific point in the workflow, not as separate mini-destinations

## Future Direction

- Short-term: tighten the reference-based chroma workflow and make the documentation easier to follow
- Mid-term: add selective GIF examples directly beside the steps they clarify
- Research track: document LoRA-based color recovery as a separate future direction, with clear notes on where it overlaps with or diverges from the current `CopyCat` workflow
- Spatial track: keep it visible, but clearly marked as experimental until it is stable enough to present as a full workflow

## Current Scope

- Included: documentation, process breakdowns, images, and workflow notes
- Not included: licensed media, trained weights, and a one-size-fits-all restoration preset
- Included templates:
  - Nuke Indie: `templates/COLOR_RECOVERY_TEMPLATE_INDIE.nkind`
  - Nuke Non-Commercial: `templates/COLOR_RECOVERY_TEMPLATE.nknc`

## Repository Structure

```text
nuke-chroma-recovery-template/
├── README.md
├── CHANGELOG.md
├── templates/
│   ├── COLOR_RECOVERY_TEMPLATE.nknc
│   └── COLOR_RECOVERY_TEMPLATE_INDIE.nkind
└── docs/
    ├── start-here.md
    ├── chroma-recovery.md
    ├── spatial-recovery.md
    ├── watch-the-video.md
    ├── provenance-metadata.md
    ├── references/
    └── images_kebab/
```

## Suggested Next Improvements

These are the most useful follow-up changes if you want the repo to match the video even more closely:

- Add a commercial `.nk` variant if you want to support the full commercial Nuke line in addition to Indie and Non-Commercial
- Add one minimal sample project tree showing expected input/output folders
- Add a small set of optimized GIFs to the workflow docs instead of rebuilding case-study pages
- Add a short future-work section for LoRA-based chroma recovery once results are stable
- Add one troubleshooting page for alignment failures, bad references, and training instability

## License

This workflow template is provided for educational and research purposes in film preservation and restoration.
