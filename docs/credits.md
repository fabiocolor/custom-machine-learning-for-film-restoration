---
layout: default
title: Credits & Attribution
parent: Resources
nav_order: 4
permalink: /credits/
---

<p class="eyebrow">People, films, models, and tools</p>

# Credits & Attribution

Film-restoration research is collaborative. The examples on this website depend on filmmakers, archives and source providers, software teams, model researchers, and colleagues who made material or knowledge available.

This page records the credits that can currently be verified from the public research record. An incomplete credit is labelled as such rather than guessed. If you can help complete or correct an entry, please [open an attribution issue](https://github.com/fabiocolor/custom-machine-learning-for-film-restoration/issues/new?title=Attribution%20correction).

> **Rights notice:** A credit identifies a source; it does not grant permission to reuse it. Film frames and clips remain the property of their respective rights holders. Their inclusion here is for research, criticism, documentation, and education. This repository does not relicense third-party footage, models, or software.

## Footage and visual sources

| Material used in the research | Film and people | Research source or acknowledgement | Public credit status |
| --- | --- | --- | --- |
| *Candy Candy* | 1976, directed by Hiroshi Shidara | 16 mm positive print; colour reference from a French PAL DVD release | Film and working sources recorded; exact print and DVD providers are not yet identified publicly |
| *La muralla verde* | 1970, directed by Armando Robles Godoy | Film scan with DVD/DCP colour reference; [Filmoteca PUCP film record](https://filmoteca.pucp.edu.pe/ciclos-cine/la-muralla-verde) | Film credit recorded; exact source providers still need confirmation |
| *The Frontier Experience* | 1975, directed by Barbara Loden | Telecine supplied by film-restoration specialist Ross Lipman; [film record](https://www.criterionchannel.com/videos/the-frontier-experience) | Film, director, and source contribution recorded |
| *Rebelión de las Tapadas* | 1943, directed by Nelson García Miranda | Colour research also consulted paintings by Johann Moritz Rugendas and Pancho Fierro | Film and visual references recorded; exact reproduction sources still need confirmation |
| *Ben* | 1972, directed by Phil Karlson; [AFI Catalog record](https://catalog.afi.com/Film/54439-BEN) | A difficult faded frame is shown as a semantic-failure example | Film credit recorded; exact edition and footage provider need confirmation |
| *Juggernaut* | 1974, directed by Richard Lester; [AFI Catalog record](https://catalog.afi.com/Film/67610-JUGGERNAUT?cxt=filmography) | Auditorium frame used in the five-stage Qwen lineage example | Film credit recorded; exact trailer, scan, or edition needs confirmation |
| *Obsession* | 1976, directed by Brian De Palma; [AFI Catalog record](https://catalog.afi.com/Film/55840-OBSESSION) | Short sequence used in temporal-colour experiments | Film credit recorded; exact trailer, scan, or edition needs confirmation |
| *Reptilicus* | US release 1962, directed by Sidney Pink and Poul Bang; [AFI Catalog record](https://catalog.afi.com/Film/19659-REPTILICUS) | Beach frame used to demonstrate tiled-inference failure | Film credit recorded; exact trailer, scan, or edition needs confirmation |
| `FANJI` working research title | Garden and waterfront material used in still and shot-level experiments | Current public files do not contain a reliable full filmographic or source record | **Credit requires confirmation before the material is reused outside this research account** |
| *Knights of the Trail* research material | Restoration work supported by La Cinémathèque française, Fondazione Cineteca Italiana, and George Eastman Museum, with support from the Louis B. Mayer Foundation | See the [case study]({{ '/case-studies/' | relative_url }}) | Institutional acknowledgements recorded |
| Other working labels, including `Beta`, `PSM`, `Friends`, and *El Gran Tinterillo* | Project labels retained from the research archive | Exact productions, editions, and source providers are not fully documented on the public site | **Credits require confirmation** |
| `Belak_Color_Patch_Chart_softblur_32.png` | Softened colour-chart reference included in the downloadable Qwen workflow | Creator and original publication source are not established in the public repository | **Attribution requires confirmation; do not redistribute separately as an independently cleared asset** |

The “needs confirmation” entries are visible deliberately. They are an attribution and clearance checklist, not permission to reuse the material.

## Models and machine-learning projects

| Model or project | Credit and role in this research | Licence or terms |
| --- | --- | --- |
| [Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511) | Qwen team. Produces the colour proposals in the downloadable still-image workflow and several research experiments. | Apache 2.0 model repository; consult the model card and any applicable acceptable-use terms |
| [Qwen-Image-Edit-2511-Lightning](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning) | LightX2V team. Four-step acceleration LoRA used by the local workflow. | Apache 2.0 repository |
| Qwen 2.5 VL encoder and Qwen image VAE | Qwen components packaged for ComfyUI in the downloadable workflow. Download links point to [Comfy-Org model packaging](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI). | Follow the Qwen and packaging repositories for exact file terms |
| [Wan2.1](https://github.com/Wan-Video/Wan2.1) and [VACE](https://github.com/ali-vilab/VACE) | Wan team and Tongyi Lab researchers. Used in the video-aware colour experiments discussed on the research-routes page. | Apache 2.0 repositories |
| Project-specific chroma and temporal models | Research models developed by Fabio P. Bedoya Huerta from production-specific examples and approved pseudo-targets. | Research status; weights and general-use packages have not been publicly released |

Model output is not historical evidence by itself. Generated examples on this website remain interpretations reviewed within a film-restoration research process.

## Software and technical projects

- [ComfyUI](https://github.com/Comfy-Org/ComfyUI), by the ComfyUI contributors, hosts the public Qwen workflows.
- [Nuke and CopyCat](https://learn.foundry.com/nuke/13.0/content/reference_guide/air_nodes/copycat.html), by Foundry, support the reference-trained restoration workflow.
- [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve/), by Blackmagic Design, is used for conforming, review, and colour work.
- [Phoenix, Loki, and DVO Steady](https://filmworkz.com/phoenix/), by Filmworkz, are used in documented cleaning, stabilisation, and restoration steps.
- [Adobe Photoshop Neural Filters](https://helpx.adobe.com/photoshop/desktop/effects-filters/neural-filters/overview-of-neural-filters.html) appear in the *La muralla verde* comparison.
- [HandBrake](https://handbrake.fr/) and [FFmpeg](https://ffmpeg.org/) support media preparation and encoding in parts of the research.
- [Faded Balancer DCTL and OFX](https://github.com/fabiocolor) are colour-balancing tools developed by Fabio P. Bedoya Huerta and used in the preparation workflow.
- NumPy, PyTorch, and Pillow are used by the local helper included with the downloadable ComfyUI workflow.

Commercial product names and trademarks belong to their respective owners. Their mention describes the research workflow and does not imply endorsement.

## Website, publication, and translation tools

This website is built with [Jekyll](https://jekyllrb.com/) and [Just the Docs](https://just-the-docs.github.io/just-the-docs/), and is published through [GitHub Pages](https://pages.github.com/). Automatic translations are generated through GitHub Models using OpenAI GPT-4o mini. They are provided for accessibility and may contain errors; the English pages are the authoritative research record.

## Research and acknowledgements

The research, workflows, writing, and website are by **Fabio P. Bedoya Huerta**, unless another credit is given beside the relevant material.

Ross Lipman is thanked for supplying the *Frontier Experience* telecine used in the paired-restoration research. The film institutions, foundations, filmmakers, artists, software developers, and model researchers listed above retain credit for their respective contributions.

For a citable account of the earlier research:

> Fabio P. Bedoya Huerta, “[Exploring Experimental Machine Learning in Film Restoration](https://library.imaging.org/archiving/articles/22/1/35),” *Archiving Conference*, 22(1), 2025.

## Corrections and additions

Attribution will be updated as source records are confirmed. Please report a missing person, project, source institution, rights holder, or licence through the [GitHub issue tracker](https://github.com/fabiocolor/custom-machine-learning-for-film-restoration/issues).
