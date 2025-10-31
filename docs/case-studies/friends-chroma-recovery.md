# Friends - Chroma Recovery

Classification: Color Recovery (Reference-Based) • Technique: Telecine Reference

Quick Links: [Chroma Recovery](../chroma-recovery.md) • [All Case Studies](../case-studies.md)

## Overview
Chroma recovery for the Friends film project, demonstrating effective color reconstruction using the `CopyCat` workflow.

## Demo Video

[![Friends Chroma Recovery Demo](https://img.youtube.com/vi/VIkXbGwqDI4/0.jpg)](https://www.youtube.com/watch?v=VIkXbGwqDI4)

## Project Details

**Source Material:** Film project
**Challenge:** Faded/degraded chroma information
**Workflow Version:** `CopyCat` based chroma recovery
**Results:** Successful color reconstruction with preserved detail

**Workflow Approach:** Sequence level training worked successfully. All shots are correlative with consistent lighting and visual style, allowing effective sequence wide model training. Demonstrates when sequence level processing is appropriate.

---

## Complete Process Documentation

### 1. Initial State (Source Material)
The original scan showing faded chroma information:

*Note: Add source/faded state image here*

### 2. Training Dataset Selection
Representative frames selected for the training dataset:

![Friends Chroma Recovery Contact Sheet](../images/FRIENDS%20CHROMA%20RECOVERY%20CONTACT%20SHEET.jpeg)

![Friends Chroma Recovery Contact Sheet 2](../images/FRIENDS%20CHROMA%20RECOVERY%20CONTACT%20SHEET%202.jpeg)

### 3. ML Training Process
`CopyCat` training showing iterative improvement:

*Note: Add training steps image here*

### 4. Chroma Recovery Process
The ML-driven color reconstruction workflow:

*Note: Add chroma recovery process image here*

### 5. Side by Side Comparison
Four-way comparison showing the recovery process:

![Friends Chroma Recovery Comparison](../images/FRIENDS%20CHROMA%20RECOVERY%20COMPARISON.png)

Additional comparison views:

![Friends Chroma Recovery Comparison 3](../images/FRIENDS%20CHROMA%20RECOVERY%20COMPARISON%203.jpeg)

![Friends Chroma Recovery Comparison 4](../images/FRIENDS%20CHROMA%20RECOVERY%20COMPARISON%204.jpeg)

---

## Technical Notes

This case study demonstrates the application of `CopyCat` based chroma recovery to the Friends project, showing successful reconstruction of missing chroma information while preserving the original image characteristics.

---

## Lessons Learned

- **Sequence-level training effectiveness**: Successfully applied sequence-wide training due to consistent visual characteristics
- **Correlative shot processing**: Demonstrated when shots with similar lighting and composition can share a single model
- **Telecine reference quality**: Shows effectiveness of using telecine sources as color reference material
- **Preservation of detail**: Successfully maintained spatial characteristics while reconstructing color information

---

[← Back to all case studies](../case-studies.md) | [Main README](../../README.md)
