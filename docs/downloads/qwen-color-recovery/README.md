# Faded Qwen Color Recovery Image App

This package contains a ComfyUI app for recovering color from one faded, unbalanced film frame.

Use the final composite as the restoration image.

## Files

- `workflows/faded-qwen-2511-still-composite-app.json`
  - Open this in ComfyUI.
- `assets/demo_unbalanced_source_frame.jpg`
  - Example faded source frame for a quick test.
- `assets/Belak_Color_Patch_Chart_softblur_32.png`
  - Included color reference used by the app.
- `custom_nodes/faded_color_recovery/`
  - Included helper that creates the final composite.

## ComfyUI Cloud

1. Open ComfyUI Cloud.
2. Import `workflows/faded-qwen-2511-still-composite-app.json`.
3. Upload your faded source frame.
4. Run the workflow.
5. Save the final composite.

If ComfyUI asks for an included file, upload it from this package.

## Your Own ComfyUI

1. Copy `custom_nodes/faded_color_recovery` into `ComfyUI/custom_nodes/`.
2. Restart ComfyUI.
3. Place `Belak_Color_Patch_Chart_softblur_32.png` into `ComfyUI/input/`.
4. Import `workflows/faded-qwen-2511-still-composite-app.json`.
5. If ComfyUI asks for Qwen Image Edit 2511 model files, download them through ComfyUI Manager or place them in the folders ComfyUI requests.
