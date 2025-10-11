# Color Recovery Workflow

A comprehensive guide for using CopyCat in Nuke with convolutional neural networks (CNNs) to restore missing or degraded **color information** in chromogenic film stocks affected by dye fading. This workflow employs supervised learning to train custom models that reconstruct chroma channels while preserving the original spatial information, overcoming the limitations of traditional color correction methods that can only manipulate existing color channels.

## Two Approaches to Color Recovery

Based on "Exploring Experimental Machine Learning in Film Restoration," color recovery encompasses two approaches depending on reference availability:

### 1. Reference-Based Recovery
Uses reference materials with accurate color information

**When to use:**
- DVDs, telecines, or other color-accurate transfers available
- Earlier-generation prints with better color preservation exist
- Color references from same film source can be verified

**Examples:**
- [Candy Candy Opening - 16mm](case-studies/candy-candy-opening.md) - DVD reference-based recovery
- [Friends](case-studies/friends-chroma-recovery.md) - Telecine reference
- [Frontier Experience](case-studies/frontier-experience-chroma-recovery.md) - Video transfer reference

### 2. Non-Reference Recovery
Infers color from external sources when direct references unavailable

**When to use:**
- No direct color reference exists for the film
- Historical films requiring period-accurate color reconstruction
- Color must be inferred from paintings, photographs, or similar materials

**Sources for non-reference recovery:**
- Historical paintings from same period/location
- Period photographs with color information
- Manual color painting in Photoshop based on research
- Artworks depicting similar subjects/settings

**Examples:**
- [Rebelión de Tapadas](case-studies/rebelion-de-tapadas-chroma-recovery.md) - Colonial-era paintings (Pancho Fierro, Johann Moritz Rugendas)
- [Ben](case-studies/ben-chroma-recovery.md) - Manual reference creation

---

## When to Use Color Recovery

**Ideal for films with inter-frame damage:**
- Chromogenic film stocks with dye fading (Eastman Color, Fuji, Agfa magenta shifts)
- Color negatives with degraded color layers over time
- Historical material requiring color reconstruction
- Films with inconsistent color across scenes due to degradation

**Addresses limitations of traditional methods:**
- Traditional color grading tools are time-consuming and subjective
- Can only manipulate existing color channels, cannot "learn" color from external references
- ML models overcome this by training on supervised pairs, learning color information impossible for traditional filters

## Workflow Overview

Color recovery uses supervised learning with CNNs, training on frame pairs from faded source and color reference (or inferred reference). Apply the content vs container principle: prefer the container with superior color as ground truth and normalize non target channels so only color differs.

### 1. Dataset Curation
Select representative frame pairs: faded source + color reference
- **Reference-based**: Use DVD/telecine frames with accurate color
- **Non-reference**: Use paintings/photos or manually created color references

### 2. Alignment
Precisely match reference to source at pixel level
- Remove overscan and ensure perfect spatial correspondence
- Critical for supervised learning to work correctly

### 3. CopyCat Training (CNN)
Train convolutional neural network using supervised learning:
- **Input**: Faded source frames (degraded chroma)
- **Ground truth**: Reference frames (accurate chroma)
- **Preservation**: Model learns to reconstruct chroma while preserving original spatial information (luma channel)

### 4. Inference & Render
Apply trained model frame by frame to full sequence
- Output archival-quality files (typically ACES 2065-1 EXR)
- Maintains film grain and analog characteristics

### 5. Validation
Compare with traditional methods and validate results
- MatchGrade baseline comparison (traditional LUT based approach)
- Validate color accuracy and grain preservation

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
- Validate on held out frames
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
- **Side by Side Comparison**: Original vs. Recovered
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
