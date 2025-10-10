# Spatial Recovery Workflow

A comprehensive guide for using CopyCat in Nuke with convolutional neural networks (CNNs) to recover **spatial features** (resolution, sharpness, grain structure, detail) lost to damage or generational degradation. This workflow employs supervised learning to train custom models that transfer spatial characteristics between different sources of the same content, overcoming the limitations of traditional spatial filters that cannot "learn" from external references.

## Example Spatial Recovery Techniques

Based on the academic paper "Exploring Experimental Machine Learning in Film Restoration," spatial recovery is a vast field with numerous potential applications. The following three techniques represent explored use cases that demonstrate the range of possibilities:

1. **Gauge Recovery** - Transfer spatial characteristics between different film gauges (e.g., 16mm → 35mm quality matching)
2. **Generation Recovery** - Align quality across different film generations (e.g., positive print → internegative alignment)
3. **Analog Video Reference Recovery** - Two-step process using telecines to recover spatial features from less-damaged sections

**Note:** These techniques are examples of tested approaches, not an exhaustive catalog. The spatial recovery field is significantly broader than color recovery, offering many more potential use cases and creative applications yet to be explored.

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
- [Knights of the Trail](case-studies/knights-trail-spatial-recovery.md) - Multiple source spatial reconstruction
- [El Tinterillo](case-studies/tinterillo-spatial-recovery.md) - Analog video reference recovery technique
- [Mission Kill](case-studies/missionkill-combined-recovery.md) - Gauge recovery (16mm → 35mm) + color recovery

## Workflow Overview

Spatial recovery uses supervised learning with CNNs to train on overlapping content from multiple sources:

### 1️⃣ Source Identification & Approach Selection
Identify multiple sources and determine which spatial recovery approach best fits your scenario. Examples include:
- **Gauge Recovery**: Different film gauges of same content
- **Generation Recovery**: Different generations (print, duplicate, negative)
- **Analog Video Reference Recovery**: Telecine with partial damage requiring two-step approach
- **Other approaches**: The spatial recovery field is vast—these are starting points, not limitations

### 2️⃣ Overlap Detection
Find common frames between different sources for supervised learning pairs

### 3️⃣ Dataset Curation
Select overlapping frames representing spatial characteristics to transfer:
- High-quality source (ground truth reference)
- Low-quality source (degraded input)
- Pairs must show identical content for supervised learning

### 4️⃣ CopyCat Training (CNN)
Train convolutional neural network using supervised learning:
- Input: Low-quality spatial features
- Ground truth: High-quality spatial features
- Model learns to transfer resolution, grain, sharpness between sources

### 5️⃣ Inference & Validation
Apply trained model frame-by-frame to entire sequence and validate spatial consistency

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

## Example Spatial Recovery Techniques (Detailed)

Based on "Exploring Experimental Machine Learning in Film Restoration," the following three techniques represent tested approaches from real-world restoration projects. These are examples of what's possible, not an exhaustive list of all spatial recovery applications:

### Technique 1: Gauge Recovery

**Definition:** Transfer spatial characteristics between different film gauges to match quality

**When to use:**
- Different film gauges of the same content (e.g., 16mm positive print and 35mm internegative)
- Need to enhance lower gauge to match higher gauge spatial quality
- Homogenizing different gauge sources for consistent output

**Example from research:**
- **Mission Kill (1990)**: 16mm positive print enhanced to match 35mm internegative spatial quality
- Model trained on overlapping frames from both gauges
- Successfully transferred resolution and detail characteristics from 35mm to 16mm

**Process:**
1. Identify overlapping content between different gauges
2. Align frames precisely between 16mm and 35mm sources
3. Create supervised learning pairs (16mm input → 35mm reference)
4. Train CNN to learn spatial differences
5. Apply model to transfer 35mm spatial characteristics to 16mm sequence

**Key consideration:** Different gauges have inherently different spatial characteristics (grain structure, resolution limits). The model learns these differences and adapts accordingly.

---

### Technique 2: Generation Recovery

**Definition:** Align spatial quality across different film generations to recover original detail

**When to use:**
- Multiple generations of same film element (original negative → print → duplicate)
- Earlier generation has better spatial quality than later generations
- Need to recover lost detail from generational duplication process

**Generational degradation causes:**
- Loss of resolution through optical printing
- Grain structure changes across generations
- Detail loss from repeated duplications
- Contrast and sharpness degradation

**Process:**
1. Identify which generation preserves best spatial information
2. Find overlapping content across generations
3. Create supervised pairs (degraded generation → better generation)
4. Train model to reverse generational loss
5. Apply to entire sequence to align generations

**Key consideration:** Each film generation introduces cumulative degradation. ML models can "learn" to reverse this degradation by training on generational pairs.

---

### Technique 3: Analog Video Reference Recovery

**Definition:** Two-step process using telecines to recover spatial features from less-damaged sections

**When to use:**
- Telecine exists with better spatial preservation in some areas
- Film scan has severe damage or degradation in specific sections
- Cropping limitations prevent full-frame recovery
- Limited spatial data available from video reference

**Two-step process:**

**Step 1: Training on Less-Damaged Sections**
- Identify telecine sections with minimal damage
- Train model on these "clean" regions
- Model captures uncontaminated spatial features from telecine

**Step 2: Full-Frame Recovery Application**
- Apply trained model to entire damaged film scan
- Model transfers learned spatial features to damaged areas
- Recovers detail impossible with traditional spatial filters

**Example from research:**
- **El gran tinterillo (1975)**: Used telecine reference for spatial recovery
- Telecine cropped but preserved better spatial information in certain regions
- Two-step process allowed full-frame recovery despite telecine limitations

**Process:**
1. Analyze telecine to identify best-preserved spatial regions
2. Train first model on clean telecine sections (16mm scan → telecine spatial features)
3. Validate model on telecine quality
4. Apply model to full 16mm scan including damaged areas
5. Model transfers telecine spatial characteristics to entire sequence

**Key consideration:** This technique is unique because the reference (telecine) may not cover the full frame or entire sequence. The two-step approach overcomes these limitations by first learning "clean" spatial features, then applying them broadly.

---

## Comparison of Example Techniques

| Technique | Source Type | Use Case | Example | Complexity |
|-----------|-------------|----------|---------|------------|
| **Gauge Recovery** | Different film gauges | 16mm → 35mm quality matching | Mission Kill | Medium |
| **Generation Recovery** | Different generations | Reverse generational loss | Print → Negative alignment | Medium |
| **Analog Video Reference** | Telecine + film scan | Partial/damaged spatial recovery | El gran tinterillo | High (two-step) |

**Common principle:** All these techniques use supervised learning with CNNs to "learn" spatial features from reference sources, then transfer those features to improve degraded material—something traditional spatial filters cannot achieve.

**Beyond these examples:** The spatial recovery field is vast. Any scenario where you have multiple sources of the same content with different spatial characteristics could potentially benefit from custom ML-based spatial transfer. These three techniques are starting points that demonstrate the methodology, not boundaries of what's possible.

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

**Quick Links:** [Case Studies](case-studies.md) • [Chroma Recovery](chroma-recovery.md) • [SOP](copycat_sop.md)