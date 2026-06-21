from __future__ import annotations

import numpy as np
import torch
from PIL import Image


PREFERRED_KONTEXT_RESOLUTIONS = [
    (672, 1568),
    (688, 1504),
    (720, 1456),
    (752, 1392),
    (800, 1328),
    (832, 1248),
    (880, 1184),
    (944, 1104),
    (1024, 1024),
    (1104, 944),
    (1184, 880),
    (1248, 832),
    (1328, 800),
    (1392, 752),
    (1456, 720),
    (1504, 688),
    (1568, 672),
]


def tensor_to_pil(image: torch.Tensor) -> Image.Image:
    array = image.detach().cpu().numpy()
    array = np.clip(array * 255.0, 0, 255).astype(np.uint8)
    return Image.fromarray(array, mode="RGB")


def pil_to_tensor(image: Image.Image) -> torch.Tensor:
    array = np.asarray(image.convert("RGB"), dtype=np.float32) / 255.0
    return torch.from_numpy(array)


def clamp_int(value: int, low: int, high: int) -> int:
    return min(max(int(value), low), high)


def flux_kontext_target_size(source_size: tuple[int, int]) -> tuple[int, int]:
    source_w, source_h = source_size
    source_aspect = source_w / source_h
    _, width, height = min(
        (abs(source_aspect - width / height), width, height)
        for width, height in PREFERRED_KONTEXT_RESOLUTIONS
    )
    return width, height


def flux_kontext_source_crop(
    source_size: tuple[int, int],
    target_size: tuple[int, int],
    *,
    x_offset: int = 0,
    y_offset: int = 0,
) -> tuple[int, int, int, int]:
    source_w, source_h = source_size
    target_w, target_h = target_size
    old_aspect = source_w / source_h
    new_aspect = target_w / target_h
    x = 0
    y = 0
    if old_aspect > new_aspect:
        x = round((source_w - source_w * (new_aspect / old_aspect)) / 2)
    elif old_aspect < new_aspect:
        y = round((source_h - source_h * (old_aspect / new_aspect)) / 2)
    crop_w = source_w - x * 2
    crop_h = source_h - y * 2
    x = min(max(x + int(x_offset), 0), source_w - crop_w)
    y = min(max(y + int(y_offset), 0), source_h - crop_h)
    return x, y, x + crop_w, y + crop_h


def edge_extend_channel(channel: Image.Image, canvas_size: tuple[int, int], crop_box: tuple[int, int, int, int]) -> Image.Image:
    canvas_w, canvas_h = canvas_size
    left, top, right, bottom = crop_box
    canvas = Image.new("L", canvas_size)
    canvas.paste(channel, (left, top))
    if top > 0:
        canvas.paste(channel.crop((0, 0, channel.width, 1)).resize((channel.width, top)), (left, 0))
    if bottom < canvas_h:
        canvas.paste(
            channel.crop((0, channel.height - 1, channel.width, channel.height)).resize((channel.width, canvas_h - bottom)),
            (left, bottom),
        )
    if left > 0:
        canvas.paste(canvas.crop((left, 0, left + 1, canvas_h)).resize((left, canvas_h)), (0, 0))
    if right < canvas_w:
        canvas.paste(canvas.crop((right - 1, 0, right, canvas_h)).resize((canvas_w - right, canvas_h)), (right, 0))
    return canvas


def inverse_flux_kontext_chroma_to_source(
    source: Image.Image,
    result: Image.Image,
    *,
    x_offset: int,
    y_offset: int,
    border_fill: str,
) -> tuple[Image.Image, Image.Image]:
    target_size = flux_kontext_target_size(source.size)
    crop_box = flux_kontext_source_crop(source.size, target_size, x_offset=x_offset, y_offset=y_offset)
    crop_w = crop_box[2] - crop_box[0]
    crop_h = crop_box[3] - crop_box[1]

    _, result_cb, result_cr = result.convert("YCbCr").split()
    cb_crop = result_cb.resize((crop_w, crop_h), resample=Image.Resampling.LANCZOS)
    cr_crop = result_cr.resize((crop_w, crop_h), resample=Image.Resampling.LANCZOS)

    if border_fill == "edge":
        source_cb = edge_extend_channel(cb_crop, source.size, crop_box)
        source_cr = edge_extend_channel(cr_crop, source.size, crop_box)
    else:
        _, source_cb, source_cr = source.convert("YCbCr").split()
    source_cb.paste(cb_crop, (crop_box[0], crop_box[1]))
    source_cr.paste(cr_crop, (crop_box[0], crop_box[1]))
    return source_cb, source_cr


def apply_shadow_chroma_gate(
    source_y: Image.Image,
    source_cb: Image.Image,
    source_cr: Image.Image,
    result_cb: Image.Image,
    result_cr: Image.Image,
    *,
    mode: str,
    luma_start: int,
    luma_end: int,
    min_generated_weight: float,
) -> tuple[Image.Image, Image.Image]:
    if mode == "none":
        return result_cb, result_cr
    if mode not in {"neutral", "source"}:
        raise ValueError(f"Unsupported shadow chroma mode: {mode}")

    luma_start = clamp_int(luma_start, 0, 255)
    luma_end = clamp_int(luma_end, 0, 255)
    if luma_end <= luma_start:
        raise ValueError("shadow_luma_end must be greater than shadow_luma_start")
    min_generated_weight = min(max(float(min_generated_weight), 0.0), 1.0)

    if mode == "neutral":
        base_cb = Image.new("L", result_cb.size, 128)
        base_cr = Image.new("L", result_cr.size, 128)
    else:
        base_cb = source_cb
        base_cr = source_cr

    weight_lut = []
    for value in range(256):
        if value <= luma_start:
            weight = min_generated_weight
        elif value >= luma_end:
            weight = 1.0
        else:
            t = (value - luma_start) / (luma_end - luma_start)
            smooth = t * t * (3.0 - 2.0 * t)
            weight = min_generated_weight + (1.0 - min_generated_weight) * smooth
        weight_lut.append(round(weight * 255))

    generated_weight = source_y.point(weight_lut, "L")
    gated_cb = Image.composite(result_cb, base_cb, generated_weight)
    gated_cr = Image.composite(result_cr, base_cr, generated_weight)
    return gated_cb, gated_cr


def composite_one(
    source: Image.Image,
    result: Image.Image,
    *,
    geometry_mode: str,
    flux_kontext_x_offset: int,
    flux_kontext_y_offset: int,
    flux_kontext_border_fill: str,
    shadow_chroma_mode: str,
    shadow_luma_start: int,
    shadow_luma_end: int,
    shadow_min_generated_weight: float,
) -> Image.Image:
    source = source.convert("RGB")
    result = result.convert("RGB")
    source_y, source_cb, source_cr = source.convert("YCbCr").split()

    if geometry_mode == "flux-kontext-inverse":
        result_cb, result_cr = inverse_flux_kontext_chroma_to_source(
            source,
            result,
            x_offset=flux_kontext_x_offset,
            y_offset=flux_kontext_y_offset,
            border_fill=flux_kontext_border_fill,
        )
    else:
        if result.size != source.size:
            result = result.resize(source.size, resample=Image.Resampling.LANCZOS)
        _, result_cb, result_cr = result.convert("YCbCr").split()

    result_cb, result_cr = apply_shadow_chroma_gate(
        source_y,
        source_cb,
        source_cr,
        result_cb,
        result_cr,
        mode=shadow_chroma_mode,
        luma_start=shadow_luma_start,
        luma_end=shadow_luma_end,
        min_generated_weight=shadow_min_generated_weight,
    )
    return Image.merge("YCbCr", (source_y, result_cb, result_cr)).convert("RGB")


class FadedSourceLumaChromaComposite:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "source_image": ("IMAGE",),
                "chroma_image": ("IMAGE",),
                "geometry_mode": (["flux-kontext-inverse", "resize"], {"default": "flux-kontext-inverse"}),
                "flux_kontext_x_offset": ("INT", {"default": 0, "min": -4096, "max": 4096, "step": 1}),
                "flux_kontext_y_offset": ("INT", {"default": 0, "min": -4096, "max": 4096, "step": 1}),
                "flux_kontext_border_fill": (["edge", "source"], {"default": "edge"}),
                "shadow_chroma_mode": (["neutral", "source", "none"], {"default": "neutral"}),
                "shadow_luma_start": ("INT", {"default": 32, "min": 0, "max": 255, "step": 1}),
                "shadow_luma_end": ("INT", {"default": 96, "min": 1, "max": 255, "step": 1}),
                "shadow_min_generated_weight": ("FLOAT", {"default": 0.05, "min": 0.0, "max": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("composite_image",)
    FUNCTION = "composite"
    CATEGORY = "faded color recovery"

    def composite(
        self,
        source_image,
        chroma_image,
        geometry_mode,
        flux_kontext_x_offset,
        flux_kontext_y_offset,
        flux_kontext_border_fill,
        shadow_chroma_mode,
        shadow_luma_start,
        shadow_luma_end,
        shadow_min_generated_weight,
    ):
        source_batch = source_image
        chroma_batch = chroma_image
        source_count = int(source_batch.shape[0])
        chroma_count = int(chroma_batch.shape[0])
        output = []
        for index in range(source_count):
            chroma_index = index if chroma_count > 1 else 0
            chroma_index = min(chroma_index, chroma_count - 1)
            source = tensor_to_pil(source_batch[index])
            chroma = tensor_to_pil(chroma_batch[chroma_index])
            composite = composite_one(
                source,
                chroma,
                geometry_mode=geometry_mode,
                flux_kontext_x_offset=flux_kontext_x_offset,
                flux_kontext_y_offset=flux_kontext_y_offset,
                flux_kontext_border_fill=flux_kontext_border_fill,
                shadow_chroma_mode=shadow_chroma_mode,
                shadow_luma_start=shadow_luma_start,
                shadow_luma_end=shadow_luma_end,
                shadow_min_generated_weight=shadow_min_generated_weight,
            )
            output.append(pil_to_tensor(composite))
        return (torch.stack(output, dim=0),)


NODE_CLASS_MAPPINGS = {
    "FadedSourceLumaChromaComposite": FadedSourceLumaChromaComposite,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FadedSourceLumaChromaComposite": "Faded: Source Luma + Generated Chroma Composite",
}
