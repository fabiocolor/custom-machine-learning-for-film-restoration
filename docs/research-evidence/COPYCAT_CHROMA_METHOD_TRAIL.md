---
layout: default
title: CopyCat Chroma Method
parent: Research Evidence
nav_order: 1
---

# CopyCat Chroma Recovery Method Trail

## Method summary

**Reference-trained chroma recovery** uses aligned source/reference pairs to teach a neural network to recover colour in faded film while preserving the source's luminance, detail, grain, and damage.

**Core principle:** The model learns to map from source luminance (Y) to reference chroma (CbCr). The source remains the authority for composition, texture, and photographic structure. Only colour information comes from the reference.

## When to use this method

Use chroma recovery when:
- **Detail and grain survive** in the source, but colour has faded, shifted, or collapsed
- **A reference exists** that preserves better colour: DVD, telecine, alternate print, or carefully constructed guide
- **You need colour recovery** without replacing spatial detail or introducing synthetic texture

Do NOT use this method when:
- The source has lost spatial detail (use [Spatial Recovery]({% link spatial-recovery.md %}) instead)
- No reference exists and you cannot construct one ethically
- The reference is worse than the source in colour quality

## Input requirements

### Source requirements
- Intact luminance channel and detail structure
- Grain present (or intentionally removed if reference is also degrained)
- Minimal gate weave, splice flashes, or instability
- Pre-balanced if severe magenta/cyan casts are present (see **Faded Balancer DCTL**)

### Reference requirements
- **Colour must be better than source** — resolution does not matter as much as colour integrity
- SD references (DVD, VHS, Betacam) are acceptable because CopyCat learns colour mapping, not spatial detail
- Compression artifacts are tolerable with light cleanup (deband, light denoise)
- Frame coverage must overlap the source (letterbox/pillarbox acceptable)

### Alignment requirements
- Temporal match: same frame index or timecode
- Spatial alignment: Transform (translate/scale/rotate) to pixel-accurate match, verified with Merge (difference)
- Shared crop: Both branches must use identical live picture area
- Subtitles/overlays excluded from training area

## Core method: YCbCr channel recombination

1. **Prepare source:** Balance, stabilize, and lightly clean (no creative grade)
2. **Prepare reference:** Light denoise/deband only; preserve colour fidelity
3. **Align:** Use F_Align or manual Transform; verify with Merge (difference) until only colour differs
4. **Convert both to YCbCr** in the project's documented working space (typically Rec.709)
5. **Build ground truth target:**
   - Y channel from Source (preserves detail)
   - Cb and Cr channels from Reference (recovers colour)
6. **Clamp highlights** in both input and target to prevent the model learning incorrect relationships in blown areas
7. **Train CopyCat** on 4–64 carefully selected pairs
8. **Infer** on the complete source and review shot by shot

## Key decisions and trade-offs

### Shot-specific vs. sequence-specific models

**Sequence model (start here):**
- Train on 24–64 pairs across the full sequence
- Works when lighting, colour palette, and motion are consistent
- Faster and requires fewer training runs

**Shot-specific model (use when sequence fails):**
- Train on 4–9 pairs from one shot only
- Use when lighting varies (day/night, interior/exterior) or motion is complex
- Requires more models but produces better results for difficult material

**Evidence:** Candy Candy started with a sequence model, then switched to shot-specific models when complex motion caused the broader model to fail.

### Reference quality thresholds

**Acceptable references:**
- PAL/NTSC DVD (MPEG-2) with intact colour
- Betacam tape transfers with light compression
- Alternate film prints with better colour retention
- HD transfers with minor compression artifacts

**Problematic references:**
- Heavy banding, blocking, or colour posterization
- Baked-in creative grades that differ from source intent
- Burned-in subtitles covering training area (requires animated crop)
- Severe geometric distortion or parallax

**Stop rule:** If Merge (difference) after alignment shows structural mismatch (not just colour difference), the reference may be unusable without manual keyframing.

### Highlight management

**Problem:** Blown highlights in source or reference can cause the model to learn incorrect colour relationships.

**Solution:** Clamp both input and target to a safe range (typically 0–1 in display-referred space) before connecting to CopyCat.

**Evidence:** Candy Candy training converged faster and produced fewer artifacts after highlights were clamped.

### Pre-balancing vs. training from raw faded state

**When to pre-balance:**
- Severe magenta or cyan cast from differential dye fade
- Red channel heavily degraded; green/blue retain more information
- Channel imbalance would dominate early training and slow convergence

**Tool:** Faded Balancer DCTL (available separately) neutralizes magenta dye fade before Nuke ingest.

**Trade-off:** Pre-balancing reduces the model's workload but introduces an additional transform. Document the settings and keep the raw scan.

## What has worked

- **SD video references (DVD, VHS, Betacam)** successfully recovered colour in Candy Candy, Beta, and PSM
- **Shot-specific models** rescued difficult sequences where sequence models failed
- **Cropping to valid reference area** (excluding borders, subtitles) improved training stability
- **Highlight clamping** prevented colour artifacts in bright areas
- **Light reference cleanup** (deband, light denoise) removed compression artifacts without harming colour fidelity

## What has failed

- **Sequence models on varied lighting:** Frontier Experience showed that day/night and interior/exterior variations can exceed what one model can learn
- **Unclamped highlights:** Training without highlight management produced colour artifacts in bright areas
- **Including borders/subtitles in training area:** Models tried to learn these non-image features
- **Using higher-res references with worse colour:** Resolution does not compensate for bad colour
- **Expecting one model to solve everything:** Complex sequences often need shot-level models

## Stop rules: accept, reject, or iterate

**Accept the result when:**
- Held-out frames (not in training set) show plausible, stable colour
- Transitions, first/last frames, and shot boundaries look natural
- Colour relationships match the reference's palette without introducing new artifacts
- Grain and detail structure remain intact from source

**Reject and diagnose when:**
- Model memorizes training frames but fails on adjacent frames (add more diverse pairs)
- Colour shifts unnaturally at shot boundaries (try shot-specific models)
- Artifacts appear in highlights or shadows (check clamping and range)
- Result looks softer than source (wrong branch — this is a chroma problem, not spatial)

**Iterate by:**
- Adding pairs that cover lighting extremes, colour gamut edges, or texture types
- Switching from sequence to shot-specific models
- Checking alignment quality with Merge (difference)
- Reviewing checkpoint progression on held-out frames (not just loss curves)

## Reuse checklist

Before starting a chroma recovery:
- [ ] Source has intact detail and grain
- [ ] Reference has better colour than source
- [ ] Both can be aligned to pixel accuracy
- [ ] Shared crop excludes borders, subtitles, overlays
- [ ] Pre-balancing applied if severe cast is present
- [ ] Highlights clamped in both branches
- [ ] 4–64 diverse pairs selected (not consecutive frames)
- [ ] One held-out frame reserved for checkpoint evaluation

## Related documentation

- [Chroma Recovery workflow page]({% link chroma-recovery.md %})
- [Candy Candy case study]({% link case-studies.md %}#candy-candy-1976)
- [Training, Inference, and Review]({% link training-inference-review.md %})
- [Preparing Reliable Training Pairs]({% link automated-dataset-preparation.md %})

---

*This trail synthesizes evidence from Candy Candy, Beta, PSM, Friends, La Muralla Verde, and Frontier Experience case studies. Last updated: 2026-09-14.*
