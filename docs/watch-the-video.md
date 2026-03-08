# Watch the Latest Walkthrough

The public examples for this repository now live in the new YouTube walkthrough instead of standalone case studies.

Video:

[Nuke Chroma Recovery Walkthrough](https://youtu.be/kXerjFGX9Kg)

## How This Page Fits the Repo

This repository is now structured like a living paper for chroma recovery:

- the video gives the broad walkthrough
- the workflow docs hold the detailed method
- inline GIFs and before/after examples will sit directly beside the steps they explain

Why this changed:

- The old case studies were not being kept in sync with the workflow
- Centralizing examples in one current video is clearer for new users
- Short GIFs will be added directly into the workflow docs where they are most useful

## What To Show In The Video

The most important beats to reinforce from the documentation are:

1. What this workflow is and is not
2. Why reference quality matters more than reference resolution
3. Why source balancing and deflicker happen before training
4. How YCbCr construction isolates chroma recovery from spatial recovery
5. Why sequence-level training comes first and shot-level fixes come second
6. Why `MatchGrade` is useful as a baseline but not a substitute
7. What is next: LoRA-based chroma recovery experiments
8. What is not ready yet: spatial recovery as a finished workflow

## Planned Future Section

Once the next experiments are presentable, add a short follow-up here for:

- LoRA-based color recovery
- differences versus the current `CopyCat` workflow
- where each approach is stronger or weaker
- what remains unresolved

## How To Reuse Older Results

Older project outputs can still appear in this repository, but only as focused proof points.

Examples:

- Use `Candy Candy` to show the strengths and limits of a PAL DVD reference
- Use `Mission Kill` to explain overlap between chroma and spatial recovery, while still labeling spatial work as experimental
- Use any older result only where it reinforces a specific sentence, step, or caution

Avoid rebuilding separate project pages. The structure should stay centered on the workflow, not on a catalog of projects.

Planned inline GIF placements:

- Chroma recovery overview and final result
- Raw source versus balanced source
- Resolve prep and alignment
- YCbCr target construction
- Sequence-level inference versus shot-level correction
- MatchGrade baseline versus trained chroma output
- One or two failure cases with a short explanation
- Spatial recovery examples, clearly labeled as experimental
