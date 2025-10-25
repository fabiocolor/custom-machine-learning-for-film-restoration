# Muralla Verde - Chroma Recovery

Classification: Color Recovery (Reference-Based) • Technique: DCP/Graded Reference

Quick Links: [Chroma Recovery](../chroma-recovery.md) • [All Case Studies](../case-studies.md)

## Overview
Chroma recovery for the Muralla Verde trailer project.

## Demo Video

[![Muralla Verde Chroma Recovery Demo](https://img.youtube.com/vi/RAKMxUw78gE/0.jpg)](https://www.youtube.com/watch?v=RAKMxUw78gE)

## Project Details
**Source Material:** Trailer project
**Challenge:** Faded chroma in trailer material
**Workflow Version:** CopyCat based chroma recovery

**Workflow Approach:** Initial sequence level training failed because trailer contains multiple distinct scenes spliced together. Required shot by shot processing. Trailers with rapid scene cuts and varying visual styles need individual shot treatment for consistent results.

---

## Complete Process Documentation

### 1. Initial State (Source Material)
The original scan showing degraded color information:

![Muralla Verde Raw Scan Unbalanced](../images_kebab/muralla-verde-raw-scan-unbalanced.png)

### 2. Balanced Source Material
The color-balanced source before chroma recovery:

![Muralla Verde Source](../images_kebab/muralla-verde-source.png)

### 3. Color Reference Material
Reference material for supervised learning:

![Muralla Verde Color Reference](../images_kebab/muralla-verde-color-reference.png)

### 4. Reference Pre-Alignment in Resolve
Initial alignment of reference material in DaVinci Resolve:

![Muralla Verde Reference Pre Alignment Timeline Resolve](../images_kebab/muralla-verde-reference-pre-alignment-timeline-resolve.png)

### 5. Chroma Recovery Process
The complete ML-driven color reconstruction workflow:

![Muralla Verde Chroma Recovery Script Full Overview](../images_kebab/muralla-verde-chroma-recovery-script-full-overview.png)

### 6. Final Result
Recovered chroma applied to the full sequence:

![Muralla Verde Chroma Recovery Output](../images_kebab/muralla-verde-chroma-recovery-output.png)

### 7. Color Composite Timeline in Resolve
Final color composite assembled in DaVinci Resolve:

![Muralla Verde Color Composite Timeline Resolve](../images_kebab/muralla-verde-color-composite-timeline-resolve.png)

---

## Technical Notes

This case study demonstrates comprehensive chroma recovery for the Muralla Verde trailer, showing the complete workflow from raw scan through final composite. The process utilized supervised learning with reference material to reconstruct degraded color information while preserving the original spatial characteristics.

---

[← Back to all case studies](../case-studies.md) | [Main README](../../README.md)
