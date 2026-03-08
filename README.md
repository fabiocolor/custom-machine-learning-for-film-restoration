# Nuke Chroma Recovery Template

This repository documents a reference-based restoration workflow in NukeX using `CopyCat` and `Inference`. It is organized as one shared workflow for both chroma recovery and spatial recovery until the target-build stage, then two detailed branch guides.

It is not a one-click plugin. It is a repeatable workflow for archives, preservation teams, and restoration practitioners who want to train small models against a real source/reference pair and validate the result critically.

[![Watch the YouTube walkthrough](docs/images_kebab/video_previews/color-recovery-video-preview.gif)](https://youtu.be/kXerjFGX9Kg)
Figure 1 - Click the preview image to watch the YouTube walkthrough.

![Workflow overview](docs/images_kebab/node-graph-overview-cropped.png)
Figure 2 - Recovery workflow overview.

## Read This First

Use these in order:

1. [Start Here: Shared Reference Workflow](docs/start-here.md)
2. [Detailed Chroma Recovery Workflow](docs/chroma-recovery.md)
3. [Detailed Spatial Recovery Workflow](docs/spatial-recovery.md)

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

## Technical Overview

1. Stabilize and technically balance the source so the model does not learn flicker, dirt, or severe channel instability.
2. Choose the best available reference and prepare both elements in the same Resolve container.
3. Export matched image sequences, open the Nuke template, curate representative frame pairs, and align the reference precisely.
4. Apply a shared crop so both branches operate on the same live picture area.
5. Build the target in YCbCr and branch:
   - Chroma recovery: keep Source `Y`, replace `Cb/Cr` with Reference chroma.
   - Spatial recovery: keep Source `Cb/Cr`, replace `Y` with Reference luma.
6. Train a sequence-level model first, then split to smaller shot-level models only where the wide pass fails.
7. Run inference on the full source, render EXR outputs, compare against a simpler baseline, and document what worked and what did not.

If you want the step-by-step shared guide, use [docs/start-here.md](docs/start-here.md).

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
    ├── start-here.md
    ├── chroma-recovery.md
    ├── spatial-recovery.md
    ├── provenance-metadata.md
    ├── references/
    └── images_kebab/
```

## License

This workflow template is provided for educational and research purposes in film preservation and restoration.
