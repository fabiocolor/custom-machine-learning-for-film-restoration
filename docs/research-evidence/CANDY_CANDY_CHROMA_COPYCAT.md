---
layout: default
title: Candy Candy Trail
parent: Research Evidence
nav_order: 2
---

# Candy Candy Chroma Recovery: A Worked Example

## Case overview

**Film:** *Candy Candy* (1976), directed by Hiroshi Shidara  
**Gauge:** 16mm positive print  
**Problem:** Severe magenta dominance from dye fading; green and blue channels retain information, red/cyan layers heavily degraded  
**Reference:** French PAL DVD (SD, MPEG-2, with compression artifacts)  
**Method:** Reference-trained chroma recovery using CopyCat in Nuke  
**Result:** Successfully recovered DVD colours onto 16mm scan while preserving film resolution and grain

This case established the reusable CopyCat chroma recovery pattern and demonstrated that SD video references can work when colour integrity matters more than resolution.

## Initial state

### Source condition
- 16mm print scanned at higher resolution than reference
- Detail and grain structure intact
- Severe magenta shift from differential dye fade (red/cyan layers degraded faster than green/blue)
- Red-channel flicker present
- Original scan had not been balanced or cleaned

### Reference condition
- PAL DVD: standard definition (720×576), MPEG-2 compression
- Deinterlaced to progressive using Handbrake before import to Resolve
- Colour intact and representative of original production
- Less image area than 16mm scan (different framing)
- Some frames have burned-in French subtitles
- Compression artifacts visible but tolerable

### Initial question
Can a low-resolution DVD reference teach colour recovery to a higher-resolution film scan?

## Key decisions

### Decision 1: Accept SD reference for chroma learning

**Reasoning:** CopyCat learns **colour mapping** (YCbCr space), not spatial detail. The DVD's spatial resolution is irrelevant because the training target uses source Y (luminance/detail) with reference Cb and Cr (colour only).

**What was tested:** Training on 33 aligned source/reference pairs with the DVD as the colour guide.

**Outcome:** Successful. The model learned the colour relationships without requiring the reference to match film resolution.

**Lesson for reuse:** SD references (DVD, VHS, Betacam) are acceptable for chroma recovery when colour integrity is preserved. Do not reject a reference just because it is lower resolution.

---

### Decision 2: Pre-balance with Faded Balancer DCTL

**Problem:** Raw faded scan had extreme magenta dominance that would dominate early training.

**Solution:** Apply Faded Balancer DCTL in Resolve before exporting to Nuke. This tool neutralizes magenta dye fade by rebalancing channels based on the strongest-surviving channel (usually green).

**Outcome:** Pre-balanced source trained faster and produced more stable results.

**Trade-off:** Introduces an additional transform step. Must be documented, and the raw scan must be kept.

**Lesson for reuse:** Pre-balance severe casts before training. The model still has work to do (learning fine colour relationships), but it does not waste capacity fighting global imbalance.

---

### Decision 3: Crop to valid reference area

**Problem:** The 16mm scan had more image area than the DVD. Black borders and different framing meant the model would try to learn non-image content.

**Solution:** Apply a shared crop to both source and reference so both branches show the same live picture area. Training happens only within this crop.

**Outcome:** Training stability improved. The model focused on picture content, not borders.

**Lesson for reuse:** Always crop to the valid overlapping area. Do not train on borders, letterbox, or subtitles unless you intentionally want the model to learn them.

---

### Decision 4: Clamp highlights before training

**Problem:** Blown highlights in source or reference can cause the model to learn incorrect colour relationships in overexposed areas.

**Solution:** Clamp both input and target to 0–1 range (in display-referred Rec.709 space) before connecting to CopyCat.

**Outcome:** Fewer artifacts in bright areas. Training convergence improved.

**Lesson for reuse:** Highlight clamping is a standard preprocessing step. If your footage has specular highlights or overexposed areas, clamp before training.

---

### Decision 5: Start sequence-level, then switch to shot-specific models

**Initial approach:** Train one model on 33 pairs across multiple shots, expecting it to generalize across the sequence.

**What happened:** The sequence model worked well for static or simple motion, but failed when motion became complex (fast pans, character movement, lighting changes).

**Pivot:** Switch to shot-specific models for difficult sections. Train 4–9 pairs per shot, using only frames from that shot.

**Outcome:** Shot-specific models produced significantly better results for complex motion and varied lighting.

**Lesson for reuse:**
- Start with a sequence model (faster, fewer training runs)
- If the sequence model fails on specific shots, train dedicated models for those sections
- Complex motion, lighting changes, and varied colour palettes are signals to go shot-specific

---

## Method application

### Workflow stages

1. **Resolve export:**
   - Source: 16mm scan, pre-balanced with Faded Balancer DCTL
   - Reference: PAL DVD deinterlaced in Handbrake, imported as progressive
   - Both placed in the same timeline with identical colour management (Rec.709 display transform)

2. **Nuke project setup:**
   - Both branches ingested with matching OCIO transforms
   - Manual Transform keyframing used for alignment (F_Align insufficient due to framing differences)
   - Merge (difference) verified that only colour differed after alignment

3. **Dataset curation:**
   - 33 frame pairs selected across multiple shots
   - Frames avoided when subtitles were present (or animated crop used)
   - Held-out frame reserved for checkpoint evaluation

4. **YCbCr target build:**
   - Both branches converted to YCbCr
   - Shuffle node: red from Source red (Y), green from Reference green (Cb), blue from Reference blue (Cr)
   - Target converted back to working space
   - Highlights clamped, alpha removed, bounding box matched

5. **Training:**
   - Model: Medium
   - Patch size: 512
   - Steps: 40,000–80,000 (monitored with held-out frames)
   - Checkpoints every 10,000 steps

6. **Inference:**
   - Applied chosen `.cat` checkpoint to full source sequence
   - Reviewed transitions, first/last frames, shot boundaries
   - Re-trained shot-specific models for problem areas

7. **Delivery:**
   - Output compared to source and reference in 4-way viewer
   - Provenance recorded: source scan, reference edition, DCTL settings, training pairs, model checkpoint

---

## What worked

- **SD DVD reference:** Colour learning succeeded despite resolution mismatch
- **Pre-balancing:** Reduced magenta cast and improved training speed
- **Cropping to valid area:** Prevented the model learning borders
- **Highlight clamping:** Reduced artifacts in bright areas
- **Shot-specific pivot:** Rescued difficult sections after sequence model failed

---

## What failed or had limits

- **Sequence model on complex motion:** Could not generalize across fast pans and varied lighting
- **Manual alignment:** DVD framing differences required time-consuming keyframing
- **Subtitle handling:** Frames with burned-in subtitles required animated crops or exclusion from training set

---

## Stop rules applied

**Accepted results when:**
- Held-out frames showed stable, plausible colour
- Colour matched DVD reference palette without introducing softness
- Grain and detail structure preserved from 16mm source
- Shot boundaries and transitions looked natural

**Rejected and iterated when:**
- Sequence model failed on fast motion (switched to shot-specific)
- Artifacts appeared in specific shots (added more pairs or re-trained for that shot)

---

## Reuse guidance

**Use this pattern when:**
- Source has intact detail but faded colour
- Reference is SD video (DVD, VHS, Betacam) with good colour
- You have access to NukeX/Nuke Indie with CopyCat
- You can invest time in alignment and training

**Expect these challenges:**
- Manual alignment if framing differs
- Shot-specific models may be needed for complex sequences
- Subtitle/overlay handling requires animated crops

**Before starting:**
- Pre-balance severe casts with Faded Balancer DCTL or similar
- Verify reference colour quality (not just resolution)
- Plan for shot-specific models if lighting or motion varies
- Reserve held-out frames for checkpoint evaluation

---

## Related case studies

- **Beta:** Similar workflow with Betacam reference (also SD video)
- **PSM:** Explored both sequence and shot-level strategies
- **Frontier Experience:** Showed limits of sequence models on varied lighting

---

*This trail documents the decisions, outcomes, and lessons from the Candy Candy chroma recovery experiment. For the full case context, see [Case Studies: Candy Candy]({% link case-studies.md %}#candy-candy-1976). Last updated: 2026-09-14.*
