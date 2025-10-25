# Spatial Recovery Workflow

A comprehensive guide for using CopyCat in Nuke with convolutional neural networks (CNNs) to recover **spatial features** (resolution, sharpness, grain structure, detail) lost to damage or generational degradation. This workflow employs supervised learning to train custom models that transfer spatial characteristics between different sources of the same content, overcoming the limitations of traditional spatial filters that cannot "learn" from external references.

## Reference-Based Spatial Recovery

Based on the academic paper "Exploring Experimental Machine Learning in Film Restoration," this workflow focuses on **reference-based spatial recovery**: transferring spatial characteristics from actual film sources to degraded targets using supervised learning with CNNs.

**What is reference-based spatial recovery?**
Using verifiable film sources (different gauges, generations, or preservation elements) as spatial references to improve degraded material.

**The fundamental technique is the same regardless of source type.** What varies is:
- **Available sources**: Different film gauges, generations, preservation elements (telecines, safety copies)
- **Specific scenario**: Damage patterns, completeness, quality differences
- **Application approach**: Single-step transfer, two-step for partial damage, combined with color recovery

**Common source scenarios:**
- Multiple film gauges (16mm vs 35mm)
- Different generations (print, internegative, duplicate)
- Early preservation elements (telecines, safety copies made closer to original)
- Multiple prints/scans of varying quality
- Combinations of the above (e.g., 35mm internegative + 16mm print = gauge + generation)

**Note on non-reference spatial recovery:**
Like color recovery has non-reference approaches (paintings, manual references), spatial recovery could theoretically use non-reference approaches by applying pre-trained commercial or open-source models (upscaling, denoising, etc.) without custom training on film-specific references. However, this is outside the scope of this repository, which focuses exclusively on reference-based methods using actual film sources and custom supervised learning.

## When to Use Spatial Recovery

**Ideal for films with intra-frame damage:**
- Detail loss from physical damage, generation loss, or nitrate decay
- Multiple sources with varying spatial qualities requiring homogenization
- Gauge-related quality differences (16mm vs 35mm)
- Generational degradation (print → duplicate → internegative)
- Partial damage where telecines or alternate sources preserve better spatial information

**Addresses limitations of traditional methods:**
- Traditional spatial filters (sharpen, blur, interpolation) operate only within same or neighboring frames
- Cannot "learn" spatial features from external references
- ML models overcome this by training on supervised pairs from different sources, applying that knowledge across entire films

**Real-world examples:**
- [Knights of the Trail](case-studies/knights-trail-spatial-recovery.md) - Multiple nitrate print sources
- [El Tinterillo](case-studies/tinterillo-spatial-recovery.md) - Early telecine preservation element (two-step approach)
- [Mission Kill](case-studies/missionkill-combined-recovery.md) - 35mm internegative + 16mm print (gauge + generation + color recovery)

## Terminology & Conventions

See Terms and definitions (Glossary): [docs/references/terms-and-definitions.md](docs/references/terms-and-definitions.md)

## Workflow Overview

Spatial recovery uses supervised learning with CNNs to train on frame pairs from different containers of the same film. Use the container with superior spatial detail as ground truth and neutralize color so only spatial features differ.

### 1. Source Identification and Analysis
Identify and analyze all available sources of the same content:
- **Film gauges**: Different gauges (16mm, 35mm) of same content
- **Film generations**: Different generations (print, internegative, duplicate)
- **Preservation elements**: Early telecines, safety copies, video transfers
- **Multiple prints/scans**: Different scans or prints with varying quality
- **Combinations**: Sources may differ in multiple ways simultaneously

### 2. Overlap Detection
Find common frames between different sources for supervised learning pairs

### 3. Dataset Curation
Select representative overlapping frame pairs (for example, 3, 6, 9, or 33) representing spatial characteristics to transfer. Keep some held out pairs for validation. Rule of thumb: shots 3 to 4 pairs; scenes about 16; sequences 33 or more depending on complexity:
- High-quality source (ground truth reference)
- Low-quality source (degraded input)
- Pairs must show identical content for supervised learning

### 4. CopyCat Training (CNN)
Train a convolutional neural network using supervised learning:
- Input: Low-quality spatial features
- Ground truth: High-quality spatial features
- Model learns to transfer resolution, grain, sharpness between sources

### 5. Inference and Validation
Apply the trained model to the full original source for the selected shot, scene, or sequence and validate spatial consistency

---

## Detailed Workflow Steps

### Stage 1: Source Identification and Analysis

**Objective:** Identify and analyze multiple sources of the same content

**Process:**
1. **Source Inventory**: Catalog all available versions
   - Different film prints (different generations)
   - Various transfers (telecine, scanning)
   - Multiple scans (different equipment/settings)
   - Archive materials vs. restoration elements

2. **Spatial Quality Assessment**:
   - **Resolution**: Sharpness and detail level
   - **Grain Structure**: Film grain characteristics
   - **Damage Assessment**: Scratches, dust, degradation
   - **Completeness**: Which sources have complete vs. partial content

3. **Source Classification**:
   - **High-Quality**: Best spatial characteristics (reference)
   - **Low-Quality**: Target for improvement
   - **Partial Sources**: Missing sections or damaged areas

### Stage 2: Overlap Detection and Mapping

**Objective:** Find matching frames between different sources

**Process:**
1. **Temporal Alignment**: Match timing between sources
2. **Content Analysis**: Identify overlapping scenes
3. **Frame Matching**: Find corresponding frames
4. **Quality Mapping**: Determine which source provides best spatial info for each section

**Tools and Techniques:**
- Manual frame by frame comparison
- Automated scene detection
- Content analysis for matching
- Timecode synchronization

### Stage 3: Dataset Curation

**Objective:** Select optimal training pairs for spatial transfer

**Training Pair Selection:**
1. **Source Frames**: Low-quality elements needing improvement
2. **Reference Frames**: High-quality elements with desired spatial characteristics
3. **Overlap Requirements**: Exact frame correspondence
4. **Diversity**: Include various spatial scenarios (sharp edges, textures, grain patterns)

**Pair counts and coverage (typical):**
- Shots: begin with 4–9 pairs; scale up to 11+ if generalization is weak.
- Scenes: 12–24; Sequences: 24–64+, scaled by variability in textures and lighting.
- Balance across edges, fine textures (fabric, foliage), skin and neutrals; include extremes (deep shadows, speculars) for robustness.

**Nuke build notes:**
- Create a `FrameHold` per selected index on both branches and assemble training/validation `AppendClip` stacks.
- Verify each pair using viewer wipe or `Merge (difference)` and judge geometry only; color differences are irrelevant for spatial transfer.

**Optimal Training Data:**
- **Sharp Edges**: For detail transfer
- **Textural Areas**: For grain structure learning
- **Mixed Content**: Various image types and lighting
- **Problem Areas**: Challenging spatial scenarios

### Stage 4: CopyCat Training for Spatial Transfer

**Objective:** Train ML model to transfer spatial characteristics

**Node Configuration:**
```
Input: Low-quality source (target for improvement)
Reference: High-quality source (spatial characteristics)
Output: Enhanced source with reference spatial qualities
```

**Training Parameters:**
- **Iterations**: 150-300 (spatial learning requires more iterations)
- **Learning Rate**: Adjust based on complexity
- **Validation**: Test on non-training overlap frames
- **Quality Focus**: Emphasize detail and grain transfer

**Monitoring Training:**
- Watch for spatial detail preservation
- Monitor grain structure transfer
- Check for over-sharpening or artifacts
- Validate on challenging spatial scenarios

**Alignment and crop (practical guidance):**
- Achieve pixel-accurate alignment (auto path with `F_Align` first; switch to keyed `Transform` if residual edges remain in `Merge (difference)`).
- Remove overscan/black borders on both branches; animate a shared crop to exclude burned‑in subtitles/logos when present.
- Keep identical picture areas and bbox on both branches to isolate spatial differences only.

### Stage 5: Application and Homogenization

**Objective:** Apply trained model and achieve spatial consistency

**Application Process:**
1. **Model Application**: Apply to entire target sequence
2. **Spatial Validation**: Check for consistency across frames
3. **Quality Assessment**: Verify spatial improvement
4. **Blending**: Combine with existing elements if needed

**Output and limits:**
- For archival renders use EXR 16‑bit half (DWAA/ZIP) with ACES 2065‑1 as delivery space.
- NukeX Non‑Commercial is limited to 1920×1080 output; use Nuke Indie/Full for full‑resolution renders.

**Homogenization Techniques:**
- **Complete Sequence**: Apply to entire film for consistency
- **Sectional Application**: Apply only to problematic sections
- **Progressive Enhancement**: Multiple passes for gradual improvement
- **Selective Transfer**: Transfer only specific spatial characteristics

---

## Case Study Examples

Real world spatial recovery projects demonstrating different source scenarios:

### Mission Kill (1990)
**Sources:** 35mm internegative + 16mm positive print
**Scenario:** Gauge difference (16mm vs 35mm) + generational difference (print vs internegative)
**Approach:** Trained model on overlapping frames to transfer spatial characteristics from 35mm internegative to 16mm print
**Combined with:** Color recovery
**Result:** Successfully transferred resolution and detail characteristics, demonstrating that gauge and generation differences can be addressed simultaneously

**Key insight:** Real-world projects often involve multiple differences (gauge + generation). The model learns all spatial differences present in the training pairs.

---

### El Tinterillo (1975)
**Sources:** Early telecine preservation element + damaged 16mm film scan
**Scenario:** Telecine made closer to original (less damage) but with cropping/quality limitations
**Approach:** Two-step process:
1. Train on less-damaged telecine sections to learn "clean" spatial features
2. Apply to full 16mm scan including damaged areas

**Result:** Full-frame recovery despite telecine limitations (cropping, lower resolution)

**Key insight:** Early preservation elements (telecines, safety copies) made closer to original creation can preserve better spatial information even if lower quality. Two-step approach overcomes partial coverage.

---

## Troubleshooting & QC
- Misalignment shimmer: avoid over‑tuning `F_Align`; prefer keyed `Transform` and evaluate with `Merge (difference)`.
- Over-sharpening/halos: reduce total steps, patch size, or adjust training data toward more fine textures.
- Grain mismatch: verify reference grain characteristics; consider adding representative grain textures to the training pairs.
- Temporal inconsistency: expand pair coverage and include transition frames; confirm crops exclude transient overlays.

---

### Knights of the Trail
**Sources:** Multiple nitrate print sources with varying quality
**Scenario:** Different prints with different damage patterns and spatial qualities
**Approach:** Used better-preserved sections from multiple sources to improve degraded sections
**Result:** Spatial reconstruction using overlapping content technique

**Key insight:** When multiple prints/scans exist, can selectively use best spatial information from each source.

---

## Technical Considerations

### Spatial Characteristics Transfer

**What the Model Learns:**
- **Resolution**: Sharpness and detail level
- **Grain Structure**: Film grain patterns and characteristics
- **Edge Definition**: Clarity of edges and transitions
- **Texture**: Fine details and surface characteristics
- **Spatial Relationships**: How spatial elements relate to each other

### Source Quality Considerations

**High-Quality Source Requirements:**
- Superior resolution and sharpness
- Clean grain structure
- Minimal damage or degradation
- Complete or near-complete content
- Consistent spatial characteristics

**Low-Quality Source Characteristics:**
- Lower resolution or softness
- Damaged or degraded areas
- Missing spatial information
- Inconsistent quality across frames
- Partial content coverage

### Common Spatial Recovery Scenarios

**Scenario 1: Print-to-Print Transfer**
- Different generations of same film
- Transfer spatial characteristics from better to worse print
- Maintain film authenticity while improving quality

**Scenario 2: Scan-to-Scan Enhancement**
- Different scanning equipment or settings
- Transfer best spatial qualities between scans
- Optimize for archival preservation

**Scenario 3: Partial Reconstruction**
- Source A has complete content but poor quality
- Source B has excellent quality but incomplete content
- Transfer spatial information where content overlaps

**Scenario 4: Homogenization**
- Multiple sources with different spatial characteristics
- Create consistent spatial quality across entire project
- Maintain original characteristics while improving overall quality

---

## Case Study Integration

### Related Case Studies

**Spatial Recovery Examples:**
- [Knights of the Trail](case-studies/knights-trail-spatial-recovery.md) - Multiple source spatial reconstruction
- [El Tinterillo](case-studies/tinterillo-spatial-recovery.md) - Analog video reference recovery technique
- [Mission Kill](case-studies/missionkill-combined-recovery.md) - Combined spatial and chroma recovery

**Learning from Examples:**
Each case study demonstrates specific aspects of spatial recovery:
- Different source combinations and overlaps
- Various spatial quality improvement techniques
- Different application scenarios and validation approaches

---

## Tools and Templates

### Nuke Node Templates

**Basic Spatial Recovery Node Graph:**
```
Low-Quality Source → Transform → CopyCat (trained) → Enhanced Output
High-Quality Source → Transform → CopyCat (reference)
```

**Advanced Multi-Source Setup:**
```
Low-Quality → Transform → CopyCat → Grade → Enhanced Output
High-Quality 1 → Transform → CopyCat → Validation
High-Quality 2 → Transform → CopyCat → Quality Check
```

### Quality Assessment Tools

**Spatial Quality Analysis:**
- **Waveform Monitor**: For spatial frequency analysis
- **Vectorscope**: For spatial relationship verification
- **Comparison Tools**: Before/after analysis
- **Edge Detection**: For detail preservation checking

### Quick Reference

**Keyboard Shortcuts:**
- `Tab`: Toggle between sources for comparison
- `Shift+Tab`: Quick spatial quality check
- `Ctrl+S`: Save training progress
- `Space`: Play for motion-based spatial assessment

**Node Tips:**
- Use Viewer Wipe for before/after spatial comparison
- Enable CopyCat's built-in spatial validation
- Monitor with waveform for spatial consistency

---

## Quality Assurance

### Checklist Before Final Render

- [ ] Spatial detail properly transferred from reference
- [ ] Grain structure matches reference characteristics
- [ ] No spatial artifacts or over-sharpening
- [ ] Consistent results across sequence
- [ ] Original content preserved and enhanced
- [ ] Spatial homogenization achieved where needed

### Validation Requirements

For each project, validate:
- **Detail Transfer**: Check sharpness and edge preservation
- **Grain Matching**: Verify grain structure transfer
- **Consistency**: Ensure uniform spatial quality
- **Authenticity**: Maintain original film characteristics

---

## Troubleshooting

### Common Issues

**Spatial Artifacts:**
- Reduce model complexity or training iterations
- Check reference source quality
- Validate training data alignment

**Over-sharpening:**
- Adjust training parameters
- Add regularization to training
- Use softer reference source

**Inconsistent Results:**
- Ensure consistent overlap between sources
- Add more diverse training examples
- Check for temporal consistency

### When to Seek Help

- Training fails to converge after 300 iterations
- Significant spatial artifacts appear
- Grain structure not properly transferred
- Complex multi-source scenarios

---

## Advanced Applications

### Multi-Source Spatial Synthesis

**Complex Scenarios:**
- Three or more sources with different qualities
- Transfer best spatial characteristics from each source
- Create optimal spatial quality through synthesis

### Progressive Spatial Enhancement

**Multi-Stage Approach:**
1. Initial spatial transfer
2. Quality assessment and adjustment
3. Additional refinement passes
4. Final validation and homogenization

### Partial Content Reconstruction

**Missing Information Recovery:**
- Use overlapping content to train reconstruction
- Apply model to missing or damaged areas
- Blend with existing content seamlessly

---

## Next Steps

**After completing spatial recovery:**
1. Document spatial improvements and validation results
2. Consider chroma recovery if color issues remain
3. Archive trained model for future use
4. Share case study with spatial recovery details

**Related Workflows:**
- [Chroma Recovery](chroma-recovery.md) - For color reconstruction
- [Combined Recovery](case-studies/missionkill-combined-recovery.md) - For complex projects

---

## Comparison: Spatial vs. Chroma Recovery

| Aspect | Spatial Recovery | Chroma Recovery |
|--------|------------------|------------------|
| **Target** | Resolution, sharpness, grain | Color information |
| **Sources** | Multiple versions of same content | Source + color reference |
| **Challenge** | Spatial detail transfer | Color accuracy |
| **Validation** | Spatial quality assessment | Color accuracy testing |
| **Common Uses** | Print homogenization, detail enhancement | Color faded film recovery |

---

**Quick Links:** [Case Studies](case-studies.md) • [Chroma Recovery](chroma-recovery.md)

## Annex A (informative) Operator Quick Reference — Spatial

Prerequisites
- NukeX Indie/Full recommended; Non‑Commercial limited to 1920×1080.
- GPU enabled for `CopyCat` (Apple Silicon or NVIDIA).
- Color management: ACES/OCIO; archival plates in ACES 2065‑1 EXR (half).

Pipeline Stages (condensed)
1) Source & overlap — identify all sources; map overlapping frames; choose high‑quality reference vs low‑quality target.
2) Dataset curation — select 4–9 overlapping pairs per shot (expand to 11+ as needed); verify identical content via viewer wipe or `Merge (difference)`; hold out 15–25% for validation.
3) Alignment — `F_Align` first, keyed `Transform` fallback; remove overscan/subtitles with a shared crop; keep identical bbox.
4) Training — for spatial transfer, use target RGB as Ground Truth (with matched color) or neutralize color to isolate spatial differences; Batch 3, Patch 512/256, 40–80k steps, checkpoints every 10k, contact sheets ~100 steps.
5) Inference — mirror training transforms; validate on 50–100 frames; render EXR 16‑bit half, ACES 2065‑1.
6) Validation — check detail/grain transfer and temporal consistency; homogenize sequences as needed.

Nuke CLI Shortcuts
- Alignment: `nuke --nukex --script pipeline/02_alignment/<shot>.nk`
- Training (bg): `nuke --nukex --bg --script pipeline/03_copycat_training/<session>.nk`
- Inference: `nuke --nukex --script pipeline/04_inference_render/<shot>_render.nk`

QC Tips
- Misalignment shimmer: prefer keyed `Transform` over over‑tuning `F_Align`.
- Grain/texture mismatch: ensure representative textures in pairs; verify reference grain.
- Over‑sharpening/halos: reduce steps or patch size; balance dataset toward fine textures.
