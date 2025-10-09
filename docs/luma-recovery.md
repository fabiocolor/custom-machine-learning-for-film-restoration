# Luma Recovery Workflow

A comprehensive guide for using CopyCat in Nuke to restore missing or degraded **brightness/luminance information** in film material. This workflow trains machine learning models to reconstruct luma channels while preserving the original chroma.

## When to Use Luma Recovery

**Ideal for:**
- Damaged emulsion or film base
- Brightness degradation over time
- Luma channel damage or loss
- Under/overexposed areas
- Film with inconsistent brightness
- Chemical damage affecting silver halides

**Real-world examples:**
- [Knights of the Trail](case-studies/knights-trail-luma-recovery.md) - Luma reconstruction
- [El Tinterillo](case-studies/tinterillo-luma-recovery.md) - Comprehensive luma recovery

## Workflow Overview

The luma recovery process follows five key stages:

### 1️⃣ Dataset Curation
Select representative frames from damaged source and good reference

### 2️⃣ Alignment
Match brightness and contrast levels between source and reference

### 3️⃣ CopyCat Training
Train model to reconstruct luma while preserving original chroma

### 4️⃣ Inference & Render
Apply trained model to full sequence and output archival files

### 5️⃣ Validation
Verify brightness preservation and detail reconstruction

---

## Detailed Workflow Steps

### Stage 1: Dataset Curation

**Objective:** Select matching frame pairs from damaged source and good reference

**Process:**
1. **Source Selection**: Choose frames with luma damage but preserved chroma
2. **Reference Selection**: Choose frames with good exposure and detail from same film
3. **Matching**: Ensure temporal and spatial correspondence
4. **Quantity**: 8-16 representative frames typically sufficient
5. **Variety**: Include different lighting conditions and exposure levels

**Best Practices:**
- Focus on brightness/contrast issues rather than color
- Lock matching frames with FrameHold node
- Use AppendClip to assemble pairs
- Include challenging cases (shadows, highlights, midtones)

### Stage 2: Alignment

**Objective:** Match brightness and contrast levels between source and reference

**Key Nodes:**
- **Grade**: Adjust brightness and contrast to match levels
- **Gamma**: Fine-tune midtone matching
- **Multiply/Screen**: Adjust for exposure differences
- **Lookup**: Create custom LUTs for matching

**Alignment Checklist:**
- [ ] Source and reference brightness levels match
- [ ] Contrast ratios are similar
- [ ] Shadow and highlight details correspond
- [ ] No over/underexposure artifacts

### Stage 3: CopyCat Training

**Objective:** Train ML model to reconstruct luma from reference

**Node Configuration:**
```
Input: Source (damaged luma)
Reference: Aligned reference (good luma)
Output: Reconstructed luma
```

**Training Parameters:**
- **Iterations**: 100-200 (monitor for convergence)
- **Learning Rate**: Default typically works well
- **Validation**: Test on frames not in training set
- **Quality Check**: Look for brightness artifacts or halos

**Monitoring Training:**
- Watch loss curves for convergence
- Check intermediate results for brightness accuracy
- Validate on held-out frames
- Monitor for luma bleeding or halos

### Stage 4: Inference & Render

**Objective:** Apply trained model to full sequence

**Process:**
1. Load trained CopyCat node
2. Connect to source footage
3. Process entire sequence
4. Monitor for brightness consistency
5. Render to archival format

**Output Settings:**
- **Format**: Archival codec (ProRes, DNxHD)
- **Color Space**: Original or archival color space
- **Bit Depth**: Match source (10-bit for film)
- **Quality**: Visually lossless

### Stage 5: Validation

**Objective:** Verify brightness preservation and detail reconstruction

**Validation Methods:**
- **Waveform Monitoring**: Check brightness levels
- **Histogram Analysis**: Verify distribution
- **Detail Preservation**: Check for loss or enhancement
- **Consistency Check**: Ensure uniform results

**Quality Indicators:**
- Natural brightness reproduction
- No halos or ringing artifacts
- Preserved detail in shadows and highlights
- Consistent across sequence

---

## Technical Considerations

### Brightness vs. Luma

**Understanding the Difference:**
- **Brightness**: Perceived lightness
- **Luma**: Technical luminance signal (Y in YUV/YCbCr)
- **Our Focus**: Reconstruct luma while preserving chroma

### Color Space Management

**Recommended Workflow:**
1. **Source Analysis**: Understand original luma range
2. **Linear Working**: Convert to linear for training
3. **Reference Matching**: Ensure consistent brightness levels
4. **Output Conversion**: Render to appropriate archival space

### Model Size and Quality

**Trade-offs:**
- **Small Models**: Faster training, less detail reconstruction
- **Large Models**: Better detail preservation, slower training
- **Recommendation**: Balance detail needs with performance

### Common Issues and Solutions

**Problem:** Brightness halos or ringing
**Solution:** Reduce model size or training iterations

**Problem:** Loss of detail in shadows/highlights
**Solution**: Ensure reference has good dynamic range

**Problem:** Inconsistent brightness across frames
**Solution**: Check alignment and add more diverse training frames

---

## Case Study Integration

### Related Case Studies

**Luma Recovery Examples:**
- [Knights of the Trail](case-studies/knights-trail-luma-recovery.md) - Luma reconstruction
- [El Tinterillo](case-studies/tinterillo-luma-recovery.md) - Comprehensive luma recovery with training steps

**Learning from Examples:**
Each case study demonstrates specific aspects of luma recovery:
- Different types of luma damage
- Various reference materials
- Different validation approaches

---

## Tools and Templates

### Nuke Node Templates

**Basic Luma Recovery Node Graph:**
```
Source → Grade → Transform → CopyCat (trained) → Output
Reference → Grade → Transform → CopyCat (reference)
```

**Advanced Setup:**
```
Source → Grade → Transform → CopyCat → Grade → Output
Reference → Grade → Transform → CopyCat → Grade → Validation
```

### Brightness Matching Tools

**Useful Nuke Nodes:**
- **Grade**: Overall brightness/contrast adjustment
- **Gamma**: Midtone brightness control
- **Histogram**: Monitor brightness distribution
- **Waveform**: Check luma levels visually

### Quick Reference

**Keyboard Shortcuts:**
- `Tab`: Toggle between source and reference
- `W`: Enable waveform monitor
- `H`: Enable histogram display
- `Ctrl+S`: Save training progress

**Node Tips:**
- Use Viewer Wipe for before/after comparison
- Enable CopyCat's built-in validation
- Monitor with waveform for accuracy

---

## Quality Assurance

### Checklist Before Final Render

- [ ] Training converged without brightness artifacts
- [ ] No halos or ringing around edges
- [ ] Consistent results across test frames
- [ ] Preserved detail in shadows and highlights
- [ ] Natural brightness reproduction
- [ ] Waveform monitoring shows correct levels

### Documentation Requirements

For each project, document:
- Source material details
- Reference selection criteria
- Training parameters and iterations
- Validation results
- Brightness/contrast adjustments made

---

## Troubleshooting

### Common Issues

**Training Not Converging:**
- Check brightness alignment accuracy
- Increase training frames diversity
- Adjust learning rate or model size

**Brightness Artifacts:**
- Reduce model complexity
- Check for reference contamination
- Validate training data quality

**Inconsistent Results:**
- Ensure consistent brightness matching
- Add more diverse training examples
- Check for temporal consistency

### When to Seek Help

- Training fails to converge after 200 iterations
- Significant brightness artifacts appear
- Results don't match expected levels
- Technical issues with node setup

---

## Combined Recovery Projects

**When Both Luma and Chroma Recovery Needed:**
Some projects may require both types of recovery. See:
- [Mission Kill - Combined Recovery](case-studies/missionkill-combined-recovery.md)

**Recommended Approach:**
1. Complete chroma recovery first
2. Validate chroma results
3. Perform luma recovery on chroma-corrected footage
4. Final validation of both recoveries

---

## Next Steps

**After completing luma recovery:**
1. Document results in experiments log
2. Consider chroma recovery if color issues remain
3. Archive trained model for future use
4. Share case study if appropriate

**Related Workflows:**
- [Chroma Recovery](chroma-recovery.md) - For color reconstruction
- [Combined Recovery](case-studies/missionkill-combined-recovery.md) - For complex projects

---

## Comparison: Luma vs. Chroma Recovery

| Aspect | Luma Recovery | Chroma Recovery |
|--------|---------------|------------------|
| **Target** | Brightness/contrast | Color information |
| **Reference** | Good exposure | Good color |
| **Challenges** | Halos, ringing | Color bleeding |
| **Validation** | Waveform monitoring | Color accuracy |
| **Common Uses** | Emulsion damage | Faded film |

---

**Quick Links:** [Case Studies](case-studies.md) • [Chroma Recovery](chroma-recovery.md) • [SOP](copycat_sop.md)