# Start Here: Video Companion Workflow

This guide is the shortest path through the repository. It follows the same logic as the video: prepare the source, secure a reference, align both in Resolve, train in Nuke, then fix difficult shots separately if the sequence-wide pass is not enough.

For the full procedural breakdown, jump to [chroma-recovery.md](chroma-recovery.md).

## Who This Page Is For

This page is written for people who want to try the workflow without already being experts in Nuke, machine learning, or scripting.

If you work in an archive, preservation lab, or small restoration environment, this is the page you should start with.

## What This Workflow Is Not

Before starting, it helps to be clear about what this workflow does not do:

- It is not a magic automatic restoration button
- It is not a guarantee of archival-ready results on every film
- It is not a replacement for careful source prep, color judgment, or documentation

What it does offer is a practical way to test whether faded color can be reconstructed more effectively than with grading alone.

## What This Workflow Is

This workflow is for faded color film where the source still has usable luma and spatial detail, but the chroma has collapsed, shifted, or partially disappeared.

The core idea is simple:

- Keep the Source luma and geometry
- Borrow chroma from a better Reference
- Train `CopyCat` to learn that chroma mapping
- Apply the trained model back to the full source

## Before You Open Nuke

You need two things before this workflow makes sense:

### 1. A balanced or partially cleaned source

Do not train directly on a source with severe channel imbalance, unstable flicker, or obvious contamination if you can avoid it.

Typical prep:

- Neutral technical balancing
- Deflicker if flicker is severe enough to confuse training
- Basic cleanup if dirt, dust, or scanning artifacts dominate the image

The goal is not to cosmetically finish the shot. The goal is to stop avoidable damage from becoming part of the learned mapping.

### 2. A usable reference

A good reference can be:

- A telecine
- A tape or Betacam transfer
- A DVD or other video master
- Another film element that preserves better color
- A manually built or historical reference if no direct source exists

What matters most is not raw image quality. What matters most is whether the reference preserves more trustworthy color information than the faded source.

If the reference is interlaced or poorly transferred, recover the clean original frames first if possible. Combing and bad cadence will hurt alignment and training.

## A Plain-Language Summary

If you want the simplest version of the idea, it is this:

1. Prepare the faded source so it is stable enough to learn from.
2. Find a better color reference.
3. Teach the model to borrow color from the reference while keeping the source detail.
4. Apply that learned behavior back to the full source.
5. If a few shots fail, train those shots separately.

That is the whole workflow in plain terms.

## Recommended Order

1. Start broad with a sequence-level pass.
2. Inspect the output and identify problem shots.
3. Retrain smaller shot-level models only where the sequence-wide model fails.

This is usually faster and more informative than starting shot by shot from the beginning.

## If You Are Trying This For The First Time

Use the smallest sensible test first:

- one short shot
- one source
- one reference
- one training experiment

Do not begin with a whole feature or a difficult reel unless you already know the workflow is behaving correctly.

## Template File

The repository now includes two templates you can inspect and adapt:

- Nuke Indie: `templates/COLOR_RECOVERY_TEMPLATE_INDIE.nkind`
- Nuke Non-Commercial: `templates/COLOR_RECOVERY_TEMPLATE.nknc`

Open the file that matches your Nuke edition.

Use the template as a practical companion to this guide, not as a substitute for understanding the workflow decisions.

## Step 1: Prep Both Sources in Resolve

Resolve is the prep stage. Use it to create matched sequences before you hand anything to Nuke.

What to do:

1. Put Source and Reference in the same timeline.
2. Align them temporally first.
3. Align them spatially as far as possible with basic transforms.
4. Place both inside the same output container, usually the larger Source container.
5. Export matched image sequences, typically EXR.

Important details:

- Keep both exports in the same resolution, frame range, and framing.
- If the Reference is smaller, render it into the larger Source container instead of forcing a later resize in Nuke.
- Avoid creative grading here. Keep changes technical and repeatable.

Why this matters:

If Source and Reference do not match well before they reach Nuke, the training step becomes much harder to trust.

## Step 2: Build the Dataset in Nuke

Once the matched exports are in Nuke, build a smaller training set from the full sequence.

Two valid approaches:

- Sequence-first: sample the sequence into representative segments or frames
- Shot-first: use when only one short problem shot needs work

Sequence-first is the recommended default for the workflow shown in the video.

Dataset rules:

- Source and Reference must stay frame-matched
- Both branches need the same number of training examples
- Use only frames that align well enough to support a clean Input/Target relationship

In practical terms, this means you are choosing a small teaching set for the model. Good teaching examples matter more than a large random pile of frames.

If alignment breaks on some frames:

- Bypass `F_Align` for those frames and use keyed `Transform`
- Or drop those frames from the training set if they are not worth the cost

## Step 3: Align and Crop Properly

Alignment quality is one of the main factors that decides whether the model behaves well.

Recommended pattern:

1. Try `F_Align` as a fast first pass.
2. Check the result with `Merge (difference)`.
3. If it fails, switch to manual `Transform`.
4. After alignment is acceptable, crop out black borders, empty container space, subtitles, and overlays.
5. Clone or link the crop so Source and Reference always share the exact same picture area.

Do not train on large black borders. The model will waste capacity on them and can produce unstable output.

If you only remember one thing from this section, remember this: bad alignment causes bad training.

## Step 4: Build the Chroma Target

This is the core trick of the workflow.

1. Convert Source and Reference from working space to YCbCr.
2. Keep Y from the Source.
3. Replace Cb and Cr with the Reference chroma.
4. Convert that result back to working space.
5. Clamp values to `[0,1]`.
6. Remove alpha.
7. Copy bbox so Source and Target stay consistent.

That constructed image becomes the `CopyCat` target.

In short:

- Input = balanced Source
- Target = Source luma + Reference chroma

The network is then asked to learn chroma reconstruction, not spatial reconstruction.

If the YCbCr step feels abstract, do not worry. The practical idea is simple: keep the shape and detail of the faded source, but teach the model with the better color from the reference.

## Step 5: Train the First Model

A good starting point from the workflow shown in the video:

- Patch size: `512`
- Batch size: `3` for repeatable behavior across different GPUs
- Checkpoints: every `10000` steps
- Preview: one held-out frame that is not part of training

Practical guidance:

- Train the sequence-level model long enough to see whether it is converging
- Do not judge the workflow from the first weak checkpoint
- Use contact sheets and preview frames to catch obvious failure modes early

This stage often feels slower or more uncertain than the earlier steps. That is normal. The goal here is not perfection on the first try, but a credible first result that tells you whether the workflow is worth pushing further.

## Step 6: Run Inference on the Full Source

Inference should be fed from the full source sequence, not only the reduced training subset.

Before inference:

- Reuse the same crop logic from training
- Avoid sending large black borders through the inference node
- Keep preprocessing consistent with what the model saw during training

After inference, composite the recovered color back over the balanced source using the same color-composite logic used to build the target conceptually.

## Step 7: Compare Against a Simpler Baseline

A `MatchGrade` or LUT-like baseline is still useful.

Why:

- It gives you a fast control result
- It helps prove that the ML pass is recovering color relationships, not just shifting the overall cast
- It tells you whether the full training cost is justified

But treat it as a baseline, not a replacement. A good match-grade result can improve appearance, but it usually does not recover the missing chroma relationships that the trained model can.

## What To Look For In A Good Result

- More stable and believable color
- Better separation between colors that were previously collapsed together
- Preserved source detail rather than smeared or invented detail
- Fewer obvious color jumps from frame to frame

## What To Look For In A Bad Result

- Colors that pulse or drift unpredictably
- Areas that switch hue from frame to frame
- Clothing, skin, or backgrounds that never settle
- New artifacts that were not present in the balanced source

## When to Split Into Shot-Level Models

Move from sequence-level to shot-level training when:

- One shot keeps drifting while the rest of the sequence works
- A specific costume or object never converges
- Framing or lighting changes too much
- The reference quality changes inside the sequence

A small shot-level dataset often fixes these cases faster than forcing the sequence-wide model to solve everything.

## Common Failure Points

### Training on an unstable source

If the source still has heavy flicker, severe channel collapse, or obvious contamination, the model may learn the wrong problem.

### Trusting a bad reference

Low-resolution references are acceptable. Badly decoded, interlaced, mis-timed, or geometrically inconsistent references are much more dangerous.

### Keeping misaligned frames in the dataset

Bad pairs poison training. It is often better to drop a frame than to force it into the dataset.

### Leaving borders or subtitles in the image

Crop them out before training and inference.

### Expecting one model to solve every shot

Sequence-wide training is the first pass, not the final answer for every difficult shot.

### Treating `MatchGrade` as real chroma recovery

It is useful for comparison, but it does not replace a supervised chroma reconstruction model.

## When To Stop

If the source is too unstable, the reference is too weak, or the result stays unreliable after a fair test, it is better to stop and document the limitation than to overstate what the workflow can do.

## Recommended Next Pages

1. [Detailed Chroma Recovery Workflow](chroma-recovery.md)
2. [Watch the Latest Walkthrough](watch-the-video.md)
3. [Glossary](references/terms-and-definitions.md)

## Suggested Repo Follow-Up

If you want this repository to feel complete for new users landing from the video, the next best additions would be:

- A commercial `.nk` variant in addition to the current Indie and Non-Commercial templates
- One example project folder layout
- A dedicated troubleshooting page
- A few short GIFs embedded directly in the workflow pages instead of separate case studies
