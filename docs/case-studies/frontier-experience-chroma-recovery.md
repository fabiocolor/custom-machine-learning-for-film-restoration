# Frontier Experience - Chroma Recovery

## Overview
Chroma recovery for the Frontier Experience project.

## Demo Video

[![Frontier Experience Chroma Recovery Demo](https://img.youtube.com/vi/0hkOd2OjGXM/0.jpg)](https://www.youtube.com/watch?v=0hkOd2OjGXM)

## Project Details
**Source Material:** Film project
**Challenge:** Chroma degradation with severely damaged reference color
**Workflow Version:** CopyCat-based chroma recovery
**Results:** Acceptable output but far from perfect or good

**Workflow Approach:** Processed as sequence-level, but results were suboptimal. Reference color was too damaged, and different scenes within the movie were too visually distinct for the model to generalize effectively. Should have been separated by scene at minimum. Demonstrates limitations when reference quality is poor and visual diversity is high.

**Lesson Learned:** Even correlative sequences may require scene-level separation when:
- Reference material is severely degraded
- Visual characteristics vary significantly between scenes
- "Acceptable" output is the goal rather than archival quality

---

## Complete Process Documentation

### Process Details
*Note: Add process images here*

---

## Technical Notes
*Note: Add technical details*

---

[← Back to all case studies](https://github.com/fabiocolor/nuke-chroma-recovery-template/blob/main/docs/case-studies.md) | [Main README](https://github.com/fabiocolor/nuke-chroma-recovery-template/blob/main/README.md)
