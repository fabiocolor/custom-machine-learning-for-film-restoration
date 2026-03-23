---
layout: default
title: Glossary
nav_order: 5
---

# Glossary

Terms specific to the chroma and spatial recovery workflows in this repository. Standard Nuke node names (`Read`, `Write`, `Merge`, `Transform`, `Crop`, etc.) are not redefined here — consult Foundry documentation for those.

### ACES 2065-1
Linear AP0 scene-referred color space for archival/exchange masters. Recommended delivery space with EXR half.

### Alignment
Pixel-accurate registration of Reference to Source, including crop, so branches differ only in the intended characteristic (color or spatial).

### Chroma (Cb, Cr)
Color-difference channels in YCbCr. In chroma recovery, these come from the Reference branch.

### CopyCat
Nuke node that trains a compact CNN using supervised Input/Target pairs assembled in the node graph.

### F_Align
Furnace alignment operator used as an automated first pass before manual `Transform` refinement.

### Film gauge
Physical film width (16mm, 35mm). Different gauges have distinct spatial characteristics and damage patterns.

### Film generation
Duplication stage (original negative, internegative, print, duplicate). Generational differences affect spatial quality.

### Ground truth (Target)
The desired output used as Target during training:
- **Chroma recovery:** Source Y + Reference Cb/Cr
- **Spatial recovery:** Reference Y + Source Cb/Cr

### Hold-out frames
Frame pairs excluded from training, used only for validation.

### Inference
Nuke node that applies a trained `.cat` model to new frames/sequences.

### Internegative
Intermediate negative created from a positive element. Often higher spatial quality than distribution prints.

### Luma (Y)
Brightness channel in YCbCr. In chroma recovery, luma comes from the Source branch.

### MatchGrade
Nuke node for look matching. Used in these workflows as an optional baseline to compare against learned reconstruction.

### Provenance
Recorded history of sources, processes, and parameters enabling reproducibility and auditability.

### Telecine
Video transfer of a film element from earlier preservation workflows. May preserve cleaner sections despite lower resolution.

### Training pair
A single supervised example: Input (degraded) and Target (ground truth) sharing identical content and alignment.

### YCbCr
Color model separating luma (Y) from chroma (Cb, Cr). Used to construct ground truth by recombining channels from Source and Reference.
