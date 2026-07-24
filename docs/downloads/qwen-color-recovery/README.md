# Faded Qwen Image Edit Colour Recovery

This package contains an experimental ComfyUI workflow for proposing colour for one faded, unbalanced film frame.

The workflow saves the direct Qwen proposal and a source-preserving composite. Review both against the original. The composite keeps the source luminance and uses Qwen for colour, but it is still an interpretation rather than proof of historical colour.

## Research status

This package is a dated snapshot of ongoing research, not a finished restoration product or a fixed recipe. Its workflows, prompts, model requirements, and recommended settings may change as experiments continue. Check the research website for the current version and the latest evidence before beginning a new test.

## Files

- `workflows/faded-qwen-2511-cloud-composite-app.json`
  - Open this first in ComfyUI Cloud.
- `workflows/faded-qwen-2511-still-composite-app.json`
  - Full workflow for your own ComfyUI setup.
- `assets/demo_unbalanced_source_frame.jpg`
  - Example faded source frame for a quick test.
- `assets/Belak_Color_Patch_Chart_softblur_32.png`
  - Included colour reference used by the workflow.
- `custom_nodes/faded_color_recovery/`
  - Included helper for the local workflow.

## ComfyUI Cloud

ComfyUI Cloud may require an active plan and available credits before it can queue the workflow.

1. Open ComfyUI Cloud.
2. Import `workflows/faded-qwen-2511-cloud-composite-app.json`.
3. Upload your faded source frame in the `source frame` input.
4. If Cloud asks for the color reference, upload `assets/Belak_Color_Patch_Chart_softblur_32.png`.
5. Run the workflow.
6. Save `Recovered color` to inspect the direct model proposal.
7. Save `Final composite` to inspect the source-luminance version.

The hard Canny guide is created inside the workflow from the source frame.

## Your Own ComfyUI

1. Copy `custom_nodes/faded_color_recovery` into `ComfyUI/custom_nodes/`.
2. Restart ComfyUI.
3. Place `Belak_Color_Patch_Chart_softblur_32.png` into `ComfyUI/input/`.
4. Import either workflow from `workflows/`.
5. If ComfyUI asks for Qwen Image Edit 2511 model files, download them through ComfyUI Manager or place them in the folders ComfyUI requests.

## Review

Check for altered faces or objects, colour crossing edges, invented detail, implausible global casts, and changes in meaning between the source and the proposal. Do not use one successful frame as evidence that a complete shot will remain temporally consistent.
