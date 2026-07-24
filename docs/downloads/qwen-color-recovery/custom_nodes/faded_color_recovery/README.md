# Faded Colour Recovery ComfyUI Node

This folder contains the helper node used by the local Qwen Image Edit colour-recovery workflow.

## What it does

`FadedSourceLumaChromaComposite` combines the original source luminance with colour from the Qwen proposal. This keeps the source responsible for fine structure, texture, and light.

The included workflow already supplies the tested settings. Change them only after comparing the result with the source at full resolution.

## Install

1. Copy the `faded_color_recovery` folder into `ComfyUI/custom_nodes/`.
2. Restart ComfyUI.
3. Confirm that `FadedSourceLumaChromaComposite` appears when the supplied workflow opens.

## Output

The workflow saves both the direct model proposal and the final composite. Review both. The final composite is usually the more source-faithful result.

For still input:

```text
Load Image -> Qwen Image Edit workflow -> FadedSourceLumaChromaComposite -> Save Image / Preview Image
          \-------------------------------------------------------------^
```

For video input and frame picking:

```text
Load Video -> Get Video Components -> Image From Batch -> Qwen Image Edit workflow -> FadedSourceLumaChromaComposite
                                             \---------------------------------------------------------------^
```

Expose these controls in ComfyUI App Mode:

- source image or source video
- `batch_index` on `ImageFromBatch` when using video input
- optional seed
- optional conservative/vivid prompt preset later

Keep reference/model/workflow internals hidden for the public demo.
