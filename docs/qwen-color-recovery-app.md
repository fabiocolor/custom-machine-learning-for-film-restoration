---
layout: default
title: Qwen Color Recovery App
nav_order: 4
---

# Qwen Color Recovery Image App

Recover color from one faded, unbalanced film frame. Upload a source frame, run the app, and save the final composite as the restoration result.

This public version runs in ComfyUI Cloud or on your own ComfyUI setup. It does not send work to Fabio's private machines.

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
    <img src="{{ '/images_kebab/seapavaa2026/originals/candy_ending_frame_1619/05_final_composite.png' | relative_url }}" alt="Final color recovery composite">
    <figcaption>Final composite</figcaption>
  </figure>
</div>

<div class="app-download-panel">
  <a class="btn btn-primary" href="{{ '/downloads/faded-qwen-color-recovery-app.zip' | relative_url }}">Download the app</a>
  <a class="btn btn-outline" href="{{ '/downloads/qwen-color-recovery/workflows/faded-qwen-2511-cloud-composite-app.json' | relative_url }}">Download Cloud workflow</a>
  <a class="btn btn-outline" href="https://cloud.comfy.org/" target="_blank" rel="noopener">Open ComfyUI Cloud</a>
</div>

## Downloads

| Download | What it is for |
| --- | --- |
| [`faded-qwen-color-recovery-app.zip`]({{ '/downloads/faded-qwen-color-recovery-app.zip' | relative_url }}) | Everything needed to open the app in ComfyUI. |
| [`faded-qwen-2511-cloud-composite-app.json`]({{ '/downloads/qwen-color-recovery/workflows/faded-qwen-2511-cloud-composite-app.json' | relative_url }}) | The Cloud workflow. Use this first in ComfyUI Cloud. |
| [`faded-qwen-2511-still-composite-app.json`]({{ '/downloads/qwen-color-recovery/workflows/faded-qwen-2511-still-composite-app.json' | relative_url }}) | The full local workflow for your own ComfyUI setup. |
| [`demo_unbalanced_source_frame.jpg`]({{ '/downloads/qwen-color-recovery/assets/demo_unbalanced_source_frame.jpg' | relative_url }}) | A faded source frame you can use for a quick test. |

## Extract A Frame From Video

Use this when your source is a video. The video stays in your browser; this page does not upload it. Choose a frame, download it as an image, then use that image in ComfyUI.

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

If your browser cannot open the original video, make a temporary H.264 or HEVC copy and extract the frame from that.

## Use In ComfyUI Cloud

ComfyUI Cloud may require an active plan and available credits before it can queue the workflow. You can still open and inspect the workflow without using Fabio's machines.

1. Open [ComfyUI Cloud](https://cloud.comfy.org/).
2. Import `faded-qwen-2511-cloud-composite-app.json`.
3. Upload your faded source frame in the `source frame` input.
4. If Cloud asks for the color reference, upload `Belak_Color_Patch_Chart_softblur_32.png` from the app package.
5. Run the workflow.
6. Save `Recovered color` if you want to inspect the direct model result.
7. Save `Final composite` as the restoration result.

The hard Canny guide is created inside the workflow from the source frame. You do not need to make it separately.

## Use On Your Computer

1. Install or update ComfyUI.
2. Download and unzip the app package.
3. Copy `qwen-color-recovery/custom_nodes/faded_color_recovery` into `ComfyUI/custom_nodes/`.
4. Restart ComfyUI.
5. Copy `Belak_Color_Patch_Chart_softblur_32.png` into `ComfyUI/input/`.
6. Import either workflow JSON from `qwen-color-recovery/workflows/`.
7. If ComfyUI asks for Qwen Image Edit 2511 model files, download them through ComfyUI Manager or place them in the folders ComfyUI requests.

## Result

The app creates two images: a recovered color candidate and a final composite. The final composite keeps the original frame detail and uses the recovered color as the color layer.

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
