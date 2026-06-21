---
layout: default
title: Qwen Color Recovery App
nav_order: 4
---

# Qwen Color Recovery App

Single-frame color recovery for faded film sources, packaged as ComfyUI workflow presets. Upload a source frame or a video, choose the frame you want to test, run the workflow, and use the final composite as the restoration result.

This is the public path. It does not use private machines, private worker queues, or hidden credentials.

<div class="app-hero-strip" aria-label="Color recovery example">
  <figure>
    <img src="{{ '/images_kebab/seapavaa2026/originals/candy_ending_frame_1619/01_source_frame.png' | relative_url }}" alt="Faded source frame">
    <figcaption>Source</figcaption>
  </figure>
  <figure>
    <img src="{{ '/images_kebab/seapavaa2026/originals/candy_ending_frame_1619/04_raw_inference.png' | relative_url }}" alt="Raw Qwen color inference">
    <figcaption>Raw inference</figcaption>
  </figure>
  <figure>
    <img src="{{ '/images_kebab/seapavaa2026/originals/candy_ending_frame_1619/05_final_composite.png' | relative_url }}" alt="Final source-luma generated-chroma composite">
    <figcaption>Final composite</figcaption>
  </figure>
</div>

<div class="app-download-panel">
  <a class="btn btn-primary" href="{{ '/downloads/faded-qwen-color-recovery-app.zip' | relative_url }}">Download app package</a>
  <a class="btn btn-outline" href="https://cloud.comfy.org/" target="_blank" rel="noopener">Open ComfyUI Cloud</a>
  <a class="btn btn-outline" href="{{ '/downloads/qwen-color-recovery/workflows/faded-qwen-2511-video-frame-composite-app.json' | relative_url }}">Video-frame workflow</a>
  <a class="btn btn-outline" href="{{ '/downloads/qwen-color-recovery/workflows/faded-qwen-2511-still-composite-app.json' | relative_url }}">Still-image workflow</a>
</div>

## What You Get

| File | Purpose |
| --- | --- |
| [`faded-qwen-color-recovery-app.zip`]({{ '/downloads/faded-qwen-color-recovery-app.zip' | relative_url }}) | Full package: workflows, calibration asset, and custom composite node. |
| [`faded-qwen-2511-video-frame-composite-app.json`]({{ '/downloads/qwen-color-recovery/workflows/faded-qwen-2511-video-frame-composite-app.json' | relative_url }}) | Upload a video, select one frame, recover color for that frame. |
| [`faded-qwen-2511-still-composite-app.json`]({{ '/downloads/qwen-color-recovery/workflows/faded-qwen-2511-still-composite-app.json' | relative_url }}) | Upload one still image and recover color for that image. |
| [`faded_color_recovery`]({{ '/downloads/qwen-color-recovery/custom_nodes/faded_color_recovery/README.md' | relative_url }}) | Custom ComfyUI node that builds the final source-luma/generated-chroma composite. |
| [`Belak_Color_Patch_Chart_softblur_32.png`]({{ '/downloads/qwen-color-recovery/assets/Belak_Color_Patch_Chart_softblur_32.png' | relative_url }}) | Hidden calibration reference used by the workflow. |

## Run On ComfyUI Cloud

1. Open [ComfyUI Cloud](https://cloud.comfy.org/).
2. Import either workflow JSON from this page.
3. If Cloud asks for missing files, upload `Belak_Color_Patch_Chart_softblur_32.png` from the package.
4. If Cloud reports `FadedSourceLumaChromaComposite` as missing, install or import the included `faded_color_recovery` custom node, then restart the Cloud session.
5. Enter App Mode, expose only the source image or video, frame index for video, seed, and final composite output.
6. Save and share the app from ComfyUI Cloud.

ComfyUI App Mode is designed for simplified user-facing workflow controls and supports mobile/narrow layouts. ComfyUI currently documents App Mode as officially supported from frontend version `1.41.13`; use a current Cloud session before creating a public share link.

## Run Locally

1. Install or update ComfyUI.
2. Copy `qwen-color-recovery/custom_nodes/faded_color_recovery` into `ComfyUI/custom_nodes/`.
3. Restart ComfyUI.
4. Copy `Belak_Color_Patch_Chart_softblur_32.png` into `ComfyUI/input/`.
5. Import one workflow JSON from `qwen-color-recovery/workflows/`.
6. Install the Qwen Image Edit 2511 model stack if ComfyUI reports missing models.
7. Enter App Mode and expose only the controls users need.

Expected model files:

```text
ComfyUI/models/diffusion_models/qwen_image_edit_2511_bf16.safetensors
ComfyUI/models/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors
ComfyUI/models/vae/qwen_image_vae.safetensors
ComfyUI/models/loras/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors
```

## What The Workflow Does

The workflow uses Qwen Image Edit to generate a recovered color candidate, then builds the final restoration image by preserving the original source luminance and taking chroma from the generated result.

That final composite is the product result. The raw Qwen output is useful for inspection, but it is not the final restoration frame.

## Current Release Boundary

This page publishes the workflow package and the self-hosted install path. A permanent one-click ComfyUI Cloud share link should be created from a verified Cloud session after confirming that the workflow, custom node, calibration asset, and model stack all load correctly in Cloud.

For the underlying ComfyUI behavior, see the official [App Mode guide](https://docs.comfy.org/interface/app-mode), [Qwen Image Edit 2511 workflow guide](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit-2511), [custom node installation guide](https://docs.comfy.org/installation/install_custom_node), and [Comfy Cloud model import notes](https://docs.comfy.org/cloud/import-models).
