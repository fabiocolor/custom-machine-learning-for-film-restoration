# Spatial Information Recovery (Luma Channel)

A comprehensive guide for using CopyCat in Nuke to recover and enhance **spatial information** using overlapping content from multiple sources. This workflow trains machine learning models to transfer spatial characteristics (resolution, sharpness, grain structure) between different versions of the same content.

## When to Use Spatial Recovery

**Ideal for:**
- Homogenizing different film elements (prints, transfers, scans)
- Transferring spatial quality from high-quality source to lower-quality source
- Reconstructing missing or damaged image parts
- Sharpening and detail enhancement
- Grain structure matching
- Spatial quality improvement across multiple sources

**Real-world examples:**
- [Knights of the Trail](case-studies/knights-trail-luma-recovery.md) - Spatial reconstruction with detailed workflow
- [El Tinterillo](case-studies/tinterillo-luma-recovery.md) - Comprehensive spatial recovery with training steps
- [Mission Kill](case-studies/missionkill-combined-recovery.md) - Combined spatial and chroma recovery

## Workflow Overview

The spatial recovery process uses overlapping content from multiple sources:

### 1️⃣ Source Identification
Identify multiple sources of the same content with different spatial qualities

### 2️⃣ Overlap Detection
Find common frames between different sources

### 3️⃣ Dataset Curation
Select overlapping frames for training spatial transfer

### 4️⃣ CopyCat Training
Train model to transfer spatial characteristics from high-quality to low-quality source

### 5️⃣ Application & Homogenization
Apply trained model to entire sequence and validate spatial consistency

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
- Manual frame-by-frame comparison
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

### Stage 5: Application and Homogenization

**Objective:** Apply trained model and achieve spatial consistency

**Application Process:**
1. **Model Application**: Apply to entire target sequence
2. **Spatial Validation**: Check for consistency across frames
3. **Quality Assessment**: Verify spatial improvement
4. **Blending**: Combine with existing elements if needed

**Homogenization Techniques:**
- **Complete Sequence**: Apply to entire film for consistency
- **Sectional Application**: Apply only to problematic sections
- **Progressive Enhancement**: Multiple passes for gradual improvement
- **Selective Transfer**: Transfer only specific spatial characteristics

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
- [Knights of the Trail](case-studies/knights-trail-luma-recovery.md) - Spatial reconstruction workflow
- [El Tinterillo](case-studies/tinterillo-luma-recovery.md) - Comprehensive spatial recovery with training steps
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

**Quick Links:** [Case Studies](case-studies.md) • [Chroma Recovery](chroma-recovery.md) • [SOP](copycat_sop.md)