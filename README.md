# Custom Machine Learning for Film Restoration

<p align="center">
  <a href="https://github.com/sponsors/fabiocolor"><img src="https://img.shields.io/badge/Sponsor-❤️-red?style=for-the-badge" alt="Sponsor"></a>
  <a href="https://paypal.me/fabiocolor"><img src="https://img.shields.io/badge/Donate-PayPal-blue?style=for-the-badge" alt="Donate"></a>
</p>

<p align="center">
  <a href="https://fabiocolor.github.io/custom-machine-learning-for-film-restoration/">
    <img src="https://img.shields.io/badge/Read-Documentation-green?style=for-the-badge" alt="Documentation">
  </a>
  <a href="https://library.imaging.org/archiving/articles/22/1/35">
    <img src="https://img.shields.io/badge/Read-Research%20Paper-orange?style=for-the-badge" alt="Research Paper">
  </a>
</p>

<p align="center">
  <a href="README.es.md">Español</a> •
  <a href="docs/start-here.md">Shared Workflow</a> •
  <a href="docs/chroma-recovery.md">Chroma Recovery</a> •
  <a href="docs/spatial-recovery.md">Spatial Recovery</a> •
  <a href="docs/case-studies.md">Case Studies</a> •
  <a href="docs/es/index.md">Spanish Docs</a> •
  <a href="https://github.com/fabiocolor/custom-machine-learning-for-film-restoration/discussions">Discussions</a>
</p>

Reference-based restoration workflow for NukeX using `CopyCat` and `Inference`. Trains small CNNs against real source/reference pairs to recover lost chroma or spatial detail in degraded film elements.

Not a plugin. A repeatable, documented workflow for archives, preservation teams, and restoration practitioners.

## 💾 Download the Nuke Templates

This workflow is entirely based on pre-built templates provided in this repository. 
You can download the latest versions of the templates for your Nuke version from the releases page:

- [⬇️ Download Latest Nuke Templates (`.nknc` and `.nkind`)](https://github.com/fabiocolor/custom-machine-learning-for-film-restoration/releases/latest)

[![Watch the YouTube walkthrough](docs/images_kebab/video_previews/color-recovery-video-preview.gif)](https://youtu.be/kXerjFGX9Kg)
*Video walkthrough — a visual companion to this repository.*

![Workflow overview](docs/images_kebab/cropped/node-graph-overview-cropped.png)
*Recovery workflow overview.*

## Recovery Modes

| Mode | Use when | Ground truth target |
| --- | --- | --- |
| **Chroma recovery** | Luma/detail intact, chroma faded, shifted, or collapsed | Source `Y` + Reference `Cb/Cr` |
| **Spatial recovery** | Color acceptable, detail/sharpness/grain degraded vs. reference | Reference `Y` + Source `Cb/Cr` |

Start with chroma recovery unless your problem is clearly spatial. Do not combine both in the same target build — treat them as separate passes.

## Workflow Stages

1. Stabilize and technically balance the source (no creative grading).
2. Choose the best reference; prepare both elements in the same Resolve container.
3. Export matched sequences, open the Nuke template, curate frame pairs, align precisely.
4. Apply a shared crop (identical live picture area on both branches).
5. Build the YCbCr target — this is where chroma and spatial branches diverge.
6. Train sequence-level first; split to shot-level only where the wide pass fails.
7. Run inference on the full source, render EXR, compare against a baseline (`MatchGrade`), document results.

## Documentation

Follow these in order:

1. **[Shared Workflow](docs/start-here.md)** — Stages 0–2: Resolve export, Nuke setup, dataset curation, alignment, shared crop, and the branch decision.
2. **[Chroma Recovery](docs/chroma-recovery.md)** — Stage 3 onward: chroma target build, training, inference, validation.
3. **[Spatial Recovery](docs/spatial-recovery.md)** — Stage 3 onward: spatial target build, training, inference, validation.

Supporting material:

- [Case Studies](docs/case-studies.md) — Real-world results across eleven projects: animation, live action, non-reference, gauge recovery, and analog video reference.
- [Glossary](docs/references/terms-and-definitions.md)
- [Provenance and Metadata](docs/provenance-metadata.md) *(future — ethical training data documentation)*

## Requirements

- Foundry NukeX with `CopyCat` and `Inference` (GPU: Apple Silicon or NVIDIA)
- A source scan with surviving image information
- A reference with stronger color or spatial detail
- Resolve (or equivalent) for pre-alignment and container prep
- ACES/OCIO color management

## Templates

| Edition | File |
| --- | --- |
| Nuke Indie | `templates/COLOR_RECOVERY_TEMPLATE_INDIE.nkind` |
| Nuke Non-Commercial | `templates/COLOR_RECOVERY_TEMPLATE.nknc` |

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
        ├── ben/
        ├── beta/
        ├── candy-candy/
        ├── cropped/
        ├── friends/
        ├── frontier-experience/
        ├── full/
        ├── general/
        ├── knights-of-the-trail/
        ├── muralla-verde/
        ├── nuke-ui/
        ├── rebelion-de-las-tapadas/
        ├── tinterillo/
        ├── video_previews/
        └── workflow/
```

## License

This workflow template is provided for educational and research purposes in film preservation and restoration.
