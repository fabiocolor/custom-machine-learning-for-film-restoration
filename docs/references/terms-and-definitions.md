# Terms and definitions (Glossary)

Informative glossary for terms used across the film recovery workflows in this repository. Definitions reflect how terms are used in the Nuke `CopyCat`‑based chroma and spatial recovery guides and follow a consistent editorial style.

### ACES 2065‑1
Linear AP0 scene‑referred color space used for archival/exchange masters. Recommended as delivery space with EXR half.

### Alignment
Pixel‑accurate registration of a Reference to the Source, including crop to ensure an identical picture area. Alignment isolates the intended difference (color or spatial) between branches.

### AppendClip (Nuke)
Concatenates multiple inputs as a single sequence for building training and validation stacks from FrameHold nodes.

### BBox (Bounding box)
Image metadata in Nuke that defines the region of valid pixels. For training pairs, both branches should carry identical bbox to avoid processing artifacts.

### Chroma (Cb, Cr)
Color‑difference channels in YCbCr that carry chrominance information. In color recovery, chroma typically comes from the Reference branch.

### Contact sheet
A grid of frames used for qualitative QC during training or inference to observe trends (ringing, bleed, oversaturation, loss of detail) across frames.

### `CopyCat`
A Nuke node that trains a compact convolutional neural network (CNN) using supervised Input/Target pairs assembled inside the node graph.

### Dataset curation
The selection of representative overlapping frame pairs for training and validation. Pairs cover diverse textures, lighting, and edge cases; some are held out for validation.

### DWAA/ZIP (EXR compression)
Wavelet (DWAA/DWAB) and lossless ZIP compression options for OpenEXR. Use with EXR 16‑bit half for efficient archival renders.

### Ground Truth (Target)
The desired output used as the Target during training. Typical constructions:
- Color recovery — Source luma (Y) combined with Reference chroma (Cb/Cr) in linear space
- Spatial recovery — Reference image with the desired spatial features; color is neutralized so only spatial detail differs

### Hold‑out frames
Overlapping frame pairs intentionally excluded from training and used only for validation.

### `Inference`
A Nuke node that applies a trained model to new frames or sequences, producing deterministic renders from the node graph.

### `F_Align` (Nuke)
An alignment operator (e.g., Furnace `F_Align` or equivalent) used to estimate and correct geometric differences between sources; often used as an automated first pass before a keyed `Transform`.

### FrameHold (Nuke)
Locks a stream to a specific frame index. Used to extract discrete overlapping frames for training/validation pairs.

### Luma (Y)
The brightness channel in YCbCr. In color recovery, luma typically comes from the Source branch.

### MatchGrade
A Nuke node for look matching between images. In these workflows it can be used as an optional aid for color normalization or validation.

### Merge (difference)
Viewer or node operation that reveals residual geometric differences as edges; used to judge alignment independent of color.

### OCIO (OpenColorIO)
Color management framework used by Nuke for consistent transforms (for example, ACES workflows and Linear ↔ display conversions).

### Reference
The element or branch that provides the correct color or spatial characteristics for training. References may come from DVDs, telecines, alternate prints, or constructed sources.

### ROI (Region of interest)
A spatial sub‑region used for training to focus learning and improve efficiency. ROIs are typically created via `Crop` and coordinated across branches.

### EXR (16‑bit half)
OpenEXR pixel type with 10‑bit mantissa (“half precision”). Recommended for archival masters together with ACES 2065‑1 and DWAA/ZIP.

### Film gauge
Physical film width (for example, 16mm, 35mm). Different gauges often have distinct spatial characteristics and damage patterns.

### Film generation
Relative duplication stage (for example, original negative, internegative, print, duplicate). Generational differences affect spatial quality.

### Internegative
An intermediate negative created from a positive element, used for printing. Often higher spatial quality than distribution prints.

### Telecine
Video transfer of a film element created during earlier preservation workflows; may preserve cleaner sections despite lower resolution.

### Source
The degraded or target element to be improved via training and inference.

### Transform (Nuke)
Keyed or static 2D transform used to refine alignment after automated alignment; preferred when `Merge (difference)` shows residual edges.

### PostageStamp (Nuke)
Node that caches a small image for quick previews. Sometimes used to embed small reference images or notes in a script.

### Read / Write (Nuke)
I/O nodes for file ingest and render. Reads bring plates into the graph; Writes produce outputs (for example, EXR in ACES 2065‑1).

### Training pair (Input/Target pair)
A single supervised example for `CopyCat`: the Input (degraded) and the Target (Ground Truth) that share identical content and alignment.

### Working space
The color space in which processing occurs in Nuke. The workflows assume linear working space for node operations and YCbCr conversions during chroma construction.

### YCbCr
A color model that separates luma (Y) from chroma (Cb, Cr). Conversions between Linear and YCbCr are used to construct Ground Truth for color recovery.

### `CopyBBox` / `SetBBox`
Nuke nodes used to copy or set the bbox on an image stream to ensure consistent spatial metadata across branches.

### `Colorspace` (Nuke)
A Nuke node that converts between color models (for example, Linear ↔ YCbCr) as part of Ground Truth construction or validation.

### LoRA (Low‑Rank Adaptation)
Parameter‑efficient fine‑tuning technique for larger neural networks. Mentioned in context as complementary to custom `CopyCat` models.

### Provenance
Recorded history of sources, processes, parameters, and outputs that enables reproducibility and auditability of restoration work.
