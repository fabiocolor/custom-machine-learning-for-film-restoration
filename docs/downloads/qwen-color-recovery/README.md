# Faded Qwen Color Recovery Image App

This package contains a ComfyUI workflow preset for single-frame faded-film color recovery on the `unbalanced_raw` route.

The output is the restoration composite: original source luminance plus generated Qwen chroma.

## Files

- `workflows/faded-qwen-2511-still-composite-app.json`
  - Still-image workflow preset for an unbalanced source frame.
- `assets/demo_unbalanced_source_frame.jpg`
  - Example unbalanced source frame.
- `assets/Belak_Color_Patch_Chart_softblur_32.png`
  - Calibration reference image expected by the workflows.
- `custom_nodes/faded_color_recovery/`
  - ComfyUI custom node that builds the final source-luma/generated-chroma composite.

## ComfyUI Cloud

1. Open ComfyUI Cloud.
2. Import `workflows/faded-qwen-2511-still-composite-app.json`.
3. Upload `assets/Belak_Color_Patch_Chart_softblur_32.png` if the workflow asks for the missing reference image.
4. Install or import the `faded_color_recovery` custom node if the workflow reports `FadedSourceLumaChromaComposite` as missing.
5. Enter App Mode, expose only the unbalanced source image, seed, and final composite output, then save/share the app.

## Self-hosted ComfyUI

1. Copy `custom_nodes/faded_color_recovery` into `ComfyUI/custom_nodes/`.
2. Restart ComfyUI.
3. Place `Belak_Color_Patch_Chart_softblur_32.png` into `ComfyUI/input/`.
4. Import `workflows/faded-qwen-2511-still-composite-app.json`.
5. Install the Qwen Image Edit 2511 model stack if ComfyUI reports missing models.

## Expected Models

- `qwen_image_edit_2511_bf16.safetensors`
- `qwen_2.5_vl_7b_fp8_scaled.safetensors`
- `qwen_image_vae.safetensors`
- `Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors`

If your GPU cannot run this model stack, use the workflow as a reference and adapt the model loader nodes to a smaller Qwen Image Edit profile.
