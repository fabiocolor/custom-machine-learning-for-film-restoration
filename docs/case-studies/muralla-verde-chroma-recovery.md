# Muralla Verde - Chroma Recovery

## Overview
Chroma recovery for the Muralla Verde trailer project.

## Demo Video

[![Muralla Verde Chroma Recovery Demo](https://img.youtube.com/vi/RAKMxUw78gE/0.jpg)](https://www.youtube.com/watch?v=RAKMxUw78gE)

## Project Details
**Source Material:** Trailer project
**Challenge:** Faded chroma in trailer material
**Workflow Version:** CopyCat-based chroma recovery

---

## Complete Process Documentation

### 1. Initial State (Source Material)
The original scan showing degraded color information:

![Muralla Verde Raw Scan Unbalanced](../images/MURALLA%20RAW%20SCAN%20UNBALANCED.png)

### 2. Balanced Source Material
The color-balanced source before chroma recovery:

![Muralla Verde Source](../images/MURALLA%20VERDE%20SOURCE.png)

### 3. Color Reference Material
Reference material for supervised learning:

![Muralla Verde Color Reference](../images/MURALLA%20VERDE%20COLOR%20REFERENCE.png)

### 4. Reference Pre-Alignment in Resolve
Initial alignment of reference material in DaVinci Resolve:

![Muralla Verde Reference Pre Alignment Timeline Resolve](../images/MURALLA%20VERDE%20REFERENCE%20PRE%20ALIGNMENT%20TIMELINE%20RESOLVE%20CROPPED.png)

### 5. Chroma Recovery Process
The complete ML-driven color reconstruction workflow:

![Muralla Verde Chroma Recovery Script Full Overview](../images/MURALLA%20VERDE%20CHROMA%20RECOVERY%20SCRIPT%20FULL%20OVERVIEW%20cropped.png)

### 6. Final Result
Recovered chroma applied to the full sequence:

![Muralla Verde Chroma Recovery Output](../images/MURALLA%20VERDE%20CHROMA%20RECOVERY%20OUTPUT.png)

### 7. Color Composite Timeline in Resolve
Final color composite assembled in DaVinci Resolve:

![Muralla Verde Color Composite Timeline Resolve](../images/MURALLA%20VERDE%20COLOR%20COMPOSITE%20TIMELINE%20RESOLVE%20CROPPED.png)

---

## Technical Notes

This case study demonstrates comprehensive chroma recovery for the Muralla Verde trailer, showing the complete workflow from raw scan through final composite. The process utilized supervised learning with reference material to reconstruct degraded color information while preserving the original spatial characteristics.

---

[← Back to all case studies](https://github.com/fabiocolor/nuke-chroma-recovery-template/blob/main/docs/case-studies.md) | [Main README](https://github.com/fabiocolor/nuke-chroma-recovery-template/blob/main/README.md)
