# Chroma Recovery Workflow

A comprehensive guide for using CopyCat in Nuke to restore missing or degraded **color information** in film material. This workflow trains machine learning models to reconstruct chroma channels while preserving the original luma.

## When to Use Chroma Recovery

**Ideal for:**
- Color-faded film prints and negatives
- Damaged chroma channels
- Color negatives with degraded color layers
- Historical material with color loss
- Film with inconsistent color across scenes

**Real-world examples:**
- [Candy Candy Opening - 16mm](case-studies/candy-candy-opening.md) - 16mm film color reconstruction
- [Friends](case-studies/friends-chroma-recovery.md) - Film project chroma recovery
- [Rebelión de Tapadas](case-studies/rebelion-de-tapadas-chroma-recovery.md) - Historical archival material
- [Ben](case-studies/ben-chroma-recovery.md) - Manual reference creation

## Workflow Overview

The chroma recovery process follows five key stages:

### 1️⃣ Dataset Curation
Select representative frames from faded source and matching color reference

### 2️⃣ Alignment
Precisely match reference to source with crop to remove overscan

### 3️⃣ CopyCat Training
Train model to reconstruct chroma while preserving original luma

### 4️⃣ Inference & Render
Apply trained model to full sequence and output archival files

### 5️⃣ Validation
Compare with MatchGrade baseline and validate results

---

## Detailed Workflow Steps

### Stage 1: Dataset Curation

**Objective:** Select matching frame pairs from source and reference materials

**Process:**
1. **Source Selection**: Choose frames with faded chroma but visible detail
2. **Reference Selection**: Choose frames with accurate color from same film
3. **Matching**: Ensure temporal and spatial correspondence
4. **Quantity**: 8-16 representative frames typically sufficient
5. **Variety**: Include different lighting conditions and color palettes

**Best Practices:**
- Lock matching frames with FrameHold node
- Use AppendClip to assemble pairs
- Ensure consistent resolution and format
- Include challenging cases (shadows, highlights, skin tones)

### Stage 2: Alignment

**Objective:** Align reference precisely to source for accurate training

**Key Nodes:**
- **F_Align**: Global alignment for overall positioning
- **Transform**: Fine-tune positioning and rotation
- **Dissolve**: Compare modes and verify alignment
- **Crop**: Linked crop to remove overscan and ensure perfect match

**Alignment Checklist:**
- [ ] Source and reference are perfectly aligned
- [ ] No edge artifacts or misalignment
- [ ] Color information matches where present
- [ ] Crop removes any overscan differences

### Stage 3: CopyCat Training

**Objective:** Train ML model to reconstruct chroma from reference

**Node Configuration:**
```
Input: Source (faded chroma)
Reference: Aligned reference (good chroma)
Output: Reconstructed chroma
```

**Training Parameters:**
- **Iterations**: 100-200 (monitor for convergence)
- **Learning Rate**: Default typically works well
- **Validation**: Test on frames not in training set
- **Quality Check**: Look for artifacts or color bleeding

**Monitoring Training:**
- Watch loss curves for convergence
- Check intermediate results
- Validate on held-out frames
- Stop before overfitting

### Stage 4: Inference & Render

**Objective:** Apply trained model to full sequence

**Process:**
1. Load trained CopyCat node
2. Connect to source footage
3. Process entire sequence
4. Monitor for edge cases
5. Render to archival format

**Output Settings:**
- **Format**: Archival codec (ProRes, DNxHD)
- **Color Space**: Original or archival color space
- **Bit Depth**: Match source (10-bit for film)
- **Quality**: Visually lossless

### Stage 5: Validation

**Objective:** Validate recovery quality and compare with alternatives

**Validation Methods:**
- **Side-by-Side Comparison**: Original vs. Recovered
- **MatchGrade Baseline**: Compare with Nuke's built-in tools
- **Quality Metrics**: Visual assessment and technical analysis
- **Cross-Reference**: Multiple viewers and displays

**Quality Indicators:**
- Natural color reproduction
- No color bleeding or artifacts
- Preserved detail and texture
- Consistent across sequence

---

## Technical Considerations

### Color Space Management

**Recommended Workflow:**
1. **Source Analysis**: Understand original color space
2. **Linear Working**: Convert to linear for training
3. **Reference Matching**: Ensure consistent color spaces
4. **Output Conversion**: Render to appropriate archival space

### Model Size and Quality

**Trade-offs:**
- **Small Models**: Faster training, less detail
- **Large Models**: Better quality, slower training
- **Recommendation**: Start small, increase if needed

### Common Issues and Solutions

**Problem:** Color bleeding or artifacts
**Solution:** Reduce model size or training iterations

**Problem:** Inconsistent color across frames
**Solution:** Check alignment and add more diverse training frames

**Problem:** Loss of detail
**Solution:** Ensure source luma is preserved in training

---

## Case Study Integration

### Related Case Studies

**Chroma Recovery Examples:**
- [Candy Candy](case-studies/candy-candy-opening.md) - 16mm film with workflow images
- [Friends](case-studies/friends-chroma-recovery.md) - Contact sheet methodology
- [Rebelión de Tapadas](case-studies/rebelion-de-tapadas-chroma-recovery.md) - Historical material
- [Ben](case-studies/ben-chroma-recovery.md) - Manual reference creation

**Learning from Examples:**
Each case study demonstrates specific aspects of chroma recovery:
- Different source materials (16mm, archival, contemporary)
- Various challenges (fading, damage, reference creation)
- Different validation approaches

---

## Tools and Templates

### Nuke Node Templates

**Basic Chroma Recovery Node Graph:**
```
Source → Transform → CopyCat (trained) → Output
Reference → F_Align → Transform → CopyCat (reference)
```

**Advanced Setup:**
```
Source → Grade → Transform → CopyCat → Grade → Output
Reference → F_Align → Transform → CopyCat → Grade → Validation
```

### Quick Reference

**Keyboard Shortcuts:**
- `Tab`: Toggle between source and reference
- `Shift+Tab`: Quick alignment check
- `Ctrl+S`: Save training progress
- `Space`: Play/pause for motion checking

**Node Tips:**
- Use Viewer Wipe for before/after comparison
- Enable CopyCat's built-in validation
- Save intermediate results for reference

---

## Quality Assurance

### Checklist Before Final Render

- [ ] Training converged without artifacts
- [ ] No color bleeding or halos
- [ ] Consistent results across test frames
- [ ] Preserved detail and texture
- [ ] Natural color reproduction
- [ ] Match or exceed traditional methods

### Documentation Requirements

For each project, document:
- Source material details
- Reference selection criteria
- Training parameters and iterations
- Validation results
- Lessons learned

---

## Troubleshooting

### Common Issues

**Training Not Converging:**
- Check alignment accuracy
- Increase training frames diversity
- Adjust learning rate or model size

**Color Artifacts:**
- Reduce model complexity
- Check for reference contamination
- Validate training data quality

**Inconsistent Results:**
- Ensure consistent alignment
- Add more diverse training examples
- Check for temporal consistency

### When to Seek Help

- Training fails to converge after 200 iterations
- Significant color artifacts appear
- Results don't match expectations
- Technical issues with node setup

---

## Next Steps

**After completing chroma recovery:**
1. Document results in experiments log
2. Consider combined spatial recovery if needed
3. Archive trained model for future use
4. Share case study if appropriate

**Related Workflows:**
- [Spatial Recovery](luma-recovery.md) - For spatial information reconstruction
- [Combined Recovery](case-studies/missionkill-combined-recovery.md) - For complex projects

---

**Quick Links:** [Case Studies](case-studies.md) • [Spatial Recovery](luma-recovery.md) • [SOP](copycat_sop.md)