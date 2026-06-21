# Faded Color Recovery ComfyUI Nodes

This package contains ComfyUI nodes used by the phone/App Mode demo workflows.

## Nodes

- `FadedSourceLumaChromaComposite`: builds the product-facing restoration image from original source `Y` plus generated `Cb/Cr`.

Default settings match the current production composite policy:

- geometry mode: `flux-kontext-inverse`
- Flux/Kontext border fill: `edge`
- shadow chroma mode: `neutral`
- shadow luma range: `32` to `96`
- deepest-shadow generated chroma weight: `0.05`

## Install Locally

Copy or symlink this folder into a ComfyUI checkout:

```bash
ln -s /path/to/FADED\ COLOR\ LORA\ RECOVERY/comfyui_custom_nodes/faded_color_recovery \
  /path/to/ComfyUI/custom_nodes/faded_color_recovery
```

Then restart ComfyUI and confirm `FadedSourceLumaChromaComposite` appears in the node list.

## App Mode Shape

The demo output should be the composite node, not the raw Qwen image.

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
