# Nuke Chroma Recovery Template

This repository documents a reference-based restoration workflow in NukeX using `CopyCat` and `Inference`. It now centers on a single operational path for both chroma recovery and spatial recovery, with separate detailed pages for each branch when you need more depth.

It is not a one-click plugin. It is a repeatable workflow for archives, preservation teams, and restoration practitioners who want to train small models against a real source/reference pair and validate the result critically.

[![Watch the YouTube walkthrough](docs/images_kebab/video_previews/color-recovery-video-preview-palette.png)](https://youtu.be/kXerjFGX9Kg)
Figure 1 - Click the preview image to watch the YouTube walkthrough.

![Workflow overview](docs/images_kebab/full-overview-comparison.png)
Figure 2 - Recovery workflow overview.

## Read This First

If you want one page to follow from start to finish, use these in order:

1. [One-Step Reference Recovery Guide](docs/one-step-guide.md)
2. [Start Here: Video Companion Workflow](docs/start-here.md)
3. [Detailed Chroma Recovery Workflow](docs/chroma-recovery.md)
4. [Detailed Spatial Recovery Workflow](docs/spatial-recovery.md)
5. [Watch the Latest Walkthrough](docs/watch-the-video.md)

Supporting material:

- [Glossary](docs/references/terms-and-definitions.md)
- [Provenance and Metadata](docs/provenance-metadata.md)

## What This Repo Covers

- Reference-based chroma recovery when detail is still usable but color has faded or collapsed
- Reference-based spatial recovery when a better-detail element exists and can be aligned tightly
- Dataset curation, alignment, `CopyCat` training, inference, and validation in Nuke
- Sequence-level training first, then shot-level rescue for outliers
- Comparison against simpler baselines such as `MatchGrade`

## Choose the Right Branch

| Recovery mode | Use it when | `CopyCat` ground truth |
| --- | --- | --- |
| Chroma recovery | Luma and detail are usable, but chroma is faded, shifted, or collapsed | Source `Y` + Reference `Cb/Cr` |
| Spatial recovery | Color is acceptable, but detail, sharpness, or grain structure are degraded relative to another source | Reference `Y` + Source `Cb/Cr` |

Practical guidance:

- Most users should start with chroma recovery.
- Spatial recovery remains more experimental and depends much more on alignment quality.
- Do not try to solve chroma and spatial recovery in the same target build. Treat them as separate passes and validate each one independently.

## What You Need

- Foundry NukeX with `CopyCat` and `Inference`
- A source scan with enough surviving image information to train against
- A usable reference with stronger color or stronger spatial detail than the source
- Resolve or another prep stage that can align both elements into the same container before Nuke
- Enough discipline to keep notes on references, frame picks, checkpoints, and validation decisions

## The Workflow in One Pass

1. Stabilize and technically balance the source so the model does not learn flicker, dirt, or severe channel instability.
2. Choose the best available reference and decide whether the task is chroma or spatial recovery.
3. In Resolve, align source and reference, keep both in the same output container, and export matched image sequences.
4. In Nuke, open the template, verify project and `Read` node settings, and curate a training dataset.
5. Align the reference precisely, compare with `Merge (difference)`, and apply a shared crop to remove borders, subtitles, and empty container space.
6. Build the target in YCbCr:
   - Chroma recovery: keep Source `Y`, replace `Cb/Cr` with Reference chroma.
   - Spatial recovery: keep Source `Cb/Cr`, replace `Y` with Reference luma.
7. Train a sequence-level model first, then split to smaller shot-level models only where the wide pass fails.
8. Run inference on the full source, render EXR outputs, compare against a simpler baseline, and document what worked and what did not.

If you want the step-by-step version of that list, use [docs/one-step-guide.md](docs/one-step-guide.md).

## Templates Included

- Nuke Indie: `templates/COLOR_RECOVERY_TEMPLATE_INDIE.nkind`
- Nuke Non-Commercial: `templates/COLOR_RECOVERY_TEMPLATE.nknc`

Open the template that matches your Nuke edition and adapt it to your project.

## Repository Structure

```text
nuke-chroma-recovery-template/
├── README.md
├── CHANGELOG.md
├── templates/
│   ├── COLOR_RECOVERY_TEMPLATE.nknc
│   └── COLOR_RECOVERY_TEMPLATE_INDIE.nkind
└── docs/
    ├── one-step-guide.md
    ├── start-here.md
    ├── chroma-recovery.md
    ├── spatial-recovery.md
    ├── watch-the-video.md
    ├── provenance-metadata.md
    ├── references/
    └── images_kebab/
```

## License

This workflow template is provided for educational and research purposes in film preservation and restoration.
