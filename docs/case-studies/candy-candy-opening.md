# Candy Candy Opening - 16mm Color Recovery

## Overview
Chroma recovery for the opening sequence of Candy Candy, scanned from 16mm film. This demonstration uses a previous version of the workflow and shows effective color reconstruction results while preserving the distinctive characteristics of 16mm source material.

## Demo Video

https://youtu.be/-ZKn-qbuuoQ

## Project Details

**Source Material:** 16mm film
**Challenge:** Faded/degraded chroma information
**Workflow Version:** Previous iteration (pre-template standardization)
**Results:** Strong color recovery while preserving original grain and texture

---

## Workflow Documentation

### Training Steps
The CopyCat training process showing the iterative improvement of the chroma reconstruction model:

![Candy Training Steps](../images/candy%20training%20steps.jpeg)

### Contact Sheet
Representative frames selected for the training dataset, showing the range of scenes and color conditions:

![Candy Contact Sheet](../images/candy%20contact%20sheet.jpeg)

### Chroma Recovery Process
The chroma recovery workflow showing the transformation from faded source to reconstructed color:

![Candy Chroma Recovery v1](../images/candy%20candy%20chroma%20recovery%20v1.jpeg)

### Color Recovery Result
Detailed view of the color recovery process:

![Candy Color Recovery v1](../images/candy%20color%20recovery%20v1.jpeg)

### Final Comparison
Side-by-side comparison showing the effectiveness of the chroma recovery:

![Candy Final Comparison](../images/candy%20final%20comparison.jpeg)

---

## Technical Notes

This case study demonstrates several key aspects of the CopyCat-based chroma recovery approach:

1. **16mm Grain Preservation**: The workflow successfully maintains the characteristic grain structure of 16mm film while reconstructing missing chroma information.

2. **Training Dataset Curation**: Careful selection of representative frames ensures the model learns the full range of color and lighting conditions present in the sequence.

3. **Iterative Refinement**: The training steps visualization shows how the model progressively improves its chroma reconstruction accuracy through multiple iterations.

4. **Earlier Workflow Iteration**: While this project used a previous version of the workflow (before the current template standardization), the core principles and effective results demonstrate the robustness of the CopyCat approach.

---

## Lessons Learned

- **Dataset diversity is critical**: Including frames with varied lighting conditions and color palettes improves model generalization
- **16mm requires special attention**: The unique characteristics of 16mm film (grain, resolution, color response) must be respected during training and inference
- **Previous workflow versions remain valid**: While the current template offers improved organization and reproducibility, earlier iterations of the workflow produced high-quality results

---

[← Back to all case studies](../case-studies.md) | [Main README](../../README.md)
