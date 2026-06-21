---
layout: default
title: Qwen Color Recovery App
nav_order: 4
---

# Qwen Color Recovery Image App

Single-frame color recovery for the current `unbalanced_raw` route, packaged as a ComfyUI workflow preset. Upload one unbalanced faded source frame, run the workflow, and use the final composite as the restoration result.

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
  <a class="btn btn-outline" href="https://cloud.comfy.org/?template=image_qwen_image_edit_2511&utm_source=fabiocolor" target="_blank" rel="noopener">Open ComfyUI Cloud</a>
  <a class="btn btn-outline" href="{{ '/downloads/qwen-color-recovery/workflows/faded-qwen-2511-still-composite-app.json' | relative_url }}">Image workflow</a>
</div>

## What You Get

| File | Purpose |
| --- | --- |
| [`faded-qwen-color-recovery-app.zip`]({{ '/downloads/faded-qwen-color-recovery-app.zip' | relative_url }}) | Full image-workflow package: workflow, unbalanced demo source, calibration asset, and custom composite node. |
| [`faded-qwen-2511-still-composite-app.json`]({{ '/downloads/qwen-color-recovery/workflows/faded-qwen-2511-still-composite-app.json' | relative_url }}) | Upload one unbalanced source image and recover color for that frame. |
| [`demo_unbalanced_source_frame.jpg`]({{ '/downloads/qwen-color-recovery/assets/demo_unbalanced_source_frame.jpg' | relative_url }}) | Unbalanced example source frame used by the workflow package. |
| [`faded_color_recovery`]({{ '/downloads/qwen-color-recovery/custom_nodes/faded_color_recovery/README.md' | relative_url }}) | Custom ComfyUI node that builds the final source-luma/generated-chroma composite. |
| [`Belak_Color_Patch_Chart_softblur_32.png`]({{ '/downloads/qwen-color-recovery/assets/Belak_Color_Patch_Chart_softblur_32.png' | relative_url }}) | Hidden calibration reference used by the workflow. |

## Extract A Frame From Video

Use this before ComfyUI Cloud when your source is a video. The video stays in your browser; this page does not upload it. Choose a frame, download it as an image, then use that image in the ComfyUI workflow.

<div class="frame-extractor" id="frame-extractor">
  <label class="frame-extractor-file">
    <span>Choose source video</span>
    <input id="frame-video-file" type="file" accept="video/*">
  </label>
  <video id="frame-video" controls playsinline muted></video>
  <div class="frame-controls">
    <button type="button" class="btn btn-outline" id="frame-step-back" disabled>Back</button>
    <input id="frame-scrub" type="range" min="0" max="0" value="0" step="0.001" disabled>
    <button type="button" class="btn btn-outline" id="frame-step-forward" disabled>Forward</button>
  </div>
  <div class="frame-actions">
    <span id="frame-time">No video selected</span>
    <button type="button" class="btn btn-primary" id="frame-capture" disabled>Download selected frame</button>
  </div>
  <canvas id="frame-canvas" hidden></canvas>
  <img id="frame-preview" alt="Selected frame preview" hidden>
</div>

Browser video support depends on the device and codec. If a preservation master does not open, make a temporary H.264 or HEVC proxy, extract the frame here, and run the image workflow from that frame.

## Run On ComfyUI Cloud

1. Open [ComfyUI Cloud](https://cloud.comfy.org/).
2. Import the image workflow JSON from this page.
3. If Cloud asks for missing files, upload `Belak_Color_Patch_Chart_softblur_32.png` from the package.
4. If Cloud reports `FadedSourceLumaChromaComposite` as missing, install or import the included `faded_color_recovery` custom node, then restart the Cloud session.
5. Enter App Mode, expose only the unbalanced source image, seed, and final composite output.
6. Save and share the app from ComfyUI Cloud.

ComfyUI App Mode is designed for simplified user-facing workflow controls and supports mobile/narrow layouts. ComfyUI currently documents App Mode as officially supported from frontend version `1.41.13`; use a current Cloud session before creating a public share link.

Comfy Cloud can open official templates directly, but this custom workflow needs a Cloud share link created from a verified Cloud session. Once the image workflow, custom node, calibration asset, and model stack are confirmed in Cloud, replace the generic Cloud button above with that share link.

## Run Locally

1. Install or update ComfyUI.
2. Copy `qwen-color-recovery/custom_nodes/faded_color_recovery` into `ComfyUI/custom_nodes/`.
3. Restart ComfyUI.
4. Copy `Belak_Color_Patch_Chart_softblur_32.png` into `ComfyUI/input/`.
5. Import the image workflow JSON from `qwen-color-recovery/workflows/`.
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

The workflow uses Qwen Image Edit to generate a recovered color candidate from an unbalanced raw faded source frame, then builds the final restoration image by preserving the original source luminance and taking chroma from the generated result.

That final composite is the product result. The raw Qwen output is useful for inspection, but it is not the final restoration frame.

## Current Release Boundary

This page publishes the image workflow package and the self-hosted install path for the `unbalanced_raw` route. A permanent one-click ComfyUI Cloud share link should be created from a verified Cloud session after confirming that the workflow, custom node, calibration asset, and model stack all load correctly in Cloud.

For the underlying ComfyUI behavior, see the official [App Mode guide](https://docs.comfy.org/interface/app-mode), [Qwen Image Edit 2511 workflow guide](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit-2511), [custom node installation guide](https://docs.comfy.org/installation/install_custom_node), and [Comfy Cloud model import notes](https://docs.comfy.org/cloud/import-models).

<script>
(() => {
  const root = document.getElementById('frame-extractor');
  if (!root) return;

  const fileInput = root.querySelector('#frame-video-file');
  const video = root.querySelector('#frame-video');
  const scrub = root.querySelector('#frame-scrub');
  const back = root.querySelector('#frame-step-back');
  const forward = root.querySelector('#frame-step-forward');
  const capture = root.querySelector('#frame-capture');
  const canvas = root.querySelector('#frame-canvas');
  const preview = root.querySelector('#frame-preview');
  const timeLabel = root.querySelector('#frame-time');
  let objectUrl = null;
  let previewUrl = null;

  const setEnabled = (enabled) => {
    scrub.disabled = !enabled;
    back.disabled = !enabled;
    forward.disabled = !enabled;
    capture.disabled = !enabled;
  };

  const formatTime = (value) => {
    if (!Number.isFinite(value)) return '0:00.000';
    const minutes = Math.floor(value / 60);
    const seconds = value - minutes * 60;
    return `${minutes}:${seconds.toFixed(3).padStart(6, '0')}`;
  };

  const syncTime = () => {
    scrub.value = String(video.currentTime || 0);
    timeLabel.textContent = `${formatTime(video.currentTime || 0)} / ${formatTime(video.duration || 0)}`;
  };

  fileInput.addEventListener('change', () => {
    const file = fileInput.files && fileInput.files[0];
    if (!file) return;
    if (objectUrl) URL.revokeObjectURL(objectUrl);
    if (previewUrl) URL.revokeObjectURL(previewUrl);
    previewUrl = null;
    objectUrl = URL.createObjectURL(file);
    video.src = objectUrl;
    preview.hidden = true;
    setEnabled(false);
    timeLabel.textContent = 'Loading video';
  });

  video.addEventListener('loadedmetadata', () => {
    scrub.max = String(video.duration || 0);
    scrub.value = '0';
    setEnabled(true);
    syncTime();
  });

  video.addEventListener('error', () => {
    setEnabled(false);
    timeLabel.textContent = 'This browser cannot open that video. Use an H.264 or HEVC proxy.';
  });

  video.addEventListener('timeupdate', syncTime);
  video.addEventListener('seeked', syncTime);

  scrub.addEventListener('input', () => {
    video.currentTime = Number(scrub.value);
  });

  const step = (direction) => {
    const frameStep = 1 / 24;
    const next = Math.min(Math.max((video.currentTime || 0) + direction * frameStep, 0), video.duration || 0);
    video.pause();
    video.currentTime = next;
  };

  back.addEventListener('click', () => step(-1));
  forward.addEventListener('click', () => step(1));

  capture.addEventListener('click', () => {
    if (!video.videoWidth || !video.videoHeight) return;
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const context = canvas.getContext('2d', { alpha: false });
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob((blob) => {
      if (!blob) return;
      if (previewUrl) URL.revokeObjectURL(previewUrl);
      const url = URL.createObjectURL(blob);
      previewUrl = url;
      const link = document.createElement('a');
      link.href = url;
      link.download = `unbalanced_source_frame_${Math.round((video.currentTime || 0) * 1000)}ms.png`;
      link.click();
      preview.src = url;
      preview.hidden = false;
    }, 'image/png');
  });
})();
</script>
