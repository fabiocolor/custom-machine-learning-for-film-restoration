---
layout: default
title: Research Routes & Evidence
parent: Open-Weight Color Recovery
nav_order: 2
permalink: /open-weight-color-recovery/research-routes/
---

<p class="eyebrow">Evidence as of July 2026</p>

# Open-Weight Colour Recovery: Research Routes

This work is not yet a general-purpose colour-recovery system. It is a set of connected research routes, each tested under different conditions and each carrying different levels of confidence.

The most useful public account is therefore not a list of features. It is a map of what has been demonstrated, what looks promising, and what remains unresolved.

This map is a dated research snapshot rather than a permanent ranking. Routes may be revised, combined, downgraded, or replaced as new experiments are completed and reviewed.

<div class="status-legend" aria-label="Research status key">
  <span class="status status-demonstrated">Demonstrated</span><span>Repeated or completed on a defined test.</span>
  <span class="status status-promising">Promising</span><span>Strong evidence, but still narrow or awaiting broader review.</span>
  <span class="status status-open">Open question</span><span>A necessary route whose general solution has not been shown.</span>
</div>

## What we can say with confidence

- Qwen Image Edit can produce useful colour proposals for individual faded frames when the source and its control image remain geometrically aligned.
- Recombining generated chroma with untouched source luminance is more faithful to the surviving film than presenting raw generated RGB as the restoration.
- A carefully approved same-shot colour anchor can guide a complete shot more coherently than a generic prompt alone.
- Video models can produce stable colour on favourable low- or moderate-motion shots, but stability does not guarantee source fidelity.
- Hard motion, occlusion, changing faces, and long shots remain unsolved as a general problem.
- Human review is still the acceptance gate. Automated measures can expose alignment and flicker problems, but cannot establish historical truth or aesthetic correctness.

## Selected experiments, with context

The images below are not a gallery of finished restorations. Each one answers a narrower question. The notes explain what went into the test, what the comparison can support, and what it cannot prove. Film, model, software, and source information is collected on the [Credits & Attribution]({{ '/credits/' | relative_url }}) page; entries that still need source confirmation are clearly marked there.

<article class="experiment-evidence">
  <div class="experiment-evidence-copy">
    <p class="card-kicker">Experiment 01 · Source preservation</p>
    <h3>Can a model contribute colour without replacing the surviving image?</h3>
    <dl class="experiment-facts">
      <dt>Test</dt>
      <dd>A faded source frame, a soft colour-chart reference, and source-derived edge control were passed to Qwen Image Edit. The model’s direct RGB proposal was then separated from the final source-preserving composite.</dd>
      <dt>What to look for</dt>
      <dd>Read the board from left to right. The source, reference, control, raw proposal, and final composite remain visibly separate, so the generated image cannot be mistaken for the source or for historical evidence.</dd>
      <dt>What it supports</dt>
      <dd>The workflow can return proposed chroma to the source image while retaining the source as the record of luminance, framing, texture, and damage.</dd>
      <dt>Limit</dt>
      <dd>This structure limits the model’s authority; it does not prove that every proposed colour is correct.</dd>
    </dl>
  </div>
  <figure class="experiment-figure">
    <a href="{{ '/images_kebab/seapavaa2026/jug_auditorium_full_lineage_5stage.png' | relative_url }}" target="_blank">
      <img src="{{ '/images_kebab/seapavaa2026/jug_auditorium_full_lineage_5stage.png' | relative_url }}" alt="Five-stage Qwen experiment showing the faded source, soft colour reference, source edge control, raw generated proposal, and final source-preserving composite">
    </a>
    <figcaption><em>Juggernaut</em> (1974), directed by Richard Lester. Five-stage lineage from surviving frame to final composite. Exact research-source edition still requires confirmation; see <a href="{{ '/credits/' | relative_url }}">credits</a>.</figcaption>
  </figure>
</article>

<article class="experiment-evidence experiment-evidence-reverse">
  <div class="experiment-evidence-copy">
    <p class="card-kicker">Experiment 02 · No matched reference</p>
    <h3>Can Qwen produce a useful colour candidate when no matching colour frame survives?</h3>
    <dl class="experiment-facts">
      <dt>Test</dt>
      <dd>The FANJI garden frame used the faded source, a source-derived edge guide, a soft colour chart, and a restrained restoration prompt. It did not use a matched colour frame from the scene.</dd>
      <dt>What to look for</dt>
      <dd>The split moves from the faded source on the left to the source-luminance composite on the right. Building, trees, crowd, and framing remain tied to the source while the colour interpretation changes.</dd>
      <dt>What it supports</dt>
      <dd>A reference-free still can become a plausible candidate for human review.</dd>
      <dt>Limit</dt>
      <dd>Plausible is not the same as historically verified. The blue sky, green foliage, clothing, and architecture are interpretations unless other evidence confirms them.</dd>
    </dl>
  </div>
  <figure class="experiment-figure">
    <a href="{{ '/images_kebab/seapavaa2026/fanji_c4_row3_garden_split_comparison_fullframe_clean.png' | relative_url }}" target="_blank">
      <img src="{{ '/images_kebab/seapavaa2026/fanji_c4_row3_garden_split_comparison_fullframe_clean.png' | relative_url }}" alt="Split comparison with the faded FANJI garden source on the left and the source-preserving colour composite on the right">
    </a>
    <figcaption><code>FANJI</code> working research title. Faded source at left; reviewed colour proposal recombined with source luminance at right. Full filmographic and source credit still requires confirmation; see <a href="{{ '/credits/' | relative_url }}">credits</a>.</figcaption>
  </figure>
</article>

<article class="experiment-evidence experiment-evidence-wide">
  <div class="experiment-evidence-copy">
    <p class="card-kicker">Experiment 03 · Temporal colour</p>
    <h3>When does a colour interpretation hold together through time?</h3>
    <p>The same basic idea was tested on two very different shots: use the source sequence and source-derived structure to guide a video-aware colour proposal, then return the proposed chroma to source luminance.</p>
    <p>The comparison matters because a favourable result and a failure can look equally convincing in a single still. Motion exposes whether colour remains attached to the same face, garment, wall, or object.</p>
  </div>
  <div class="experiment-video-grid">
    <figure class="experiment-figure">
      <video controls preload="metadata" poster="{{ '/images_kebab/seapavaa2026/shot0006_source_raw_inference_final_composite_fullrun_preview.png' | relative_url }}">
        <source src="{{ '/media/seapavaa2026/shot0006_source_raw_inference_final_composite_fullrun.mp4' | relative_url }}" type="video/mp4">
      </video>
      <figcaption><strong>Favourable shot.</strong> Low-to-moderate motion remains coherent enough to demonstrate that video-aware chroma can work under bounded conditions. Footage source: see <a href="{{ '/credits/' | relative_url }}">credits and open confirmation items</a>.</figcaption>
    </figure>
    <figure class="experiment-figure">
      <video controls preload="metadata" poster="{{ '/images_kebab/seapavaa2026/shot0011_fourchunk_vace_stitched_source_raw_inference_composite_preview.png' | relative_url }}">
        <source src="{{ '/media/seapavaa2026/shot0011_fourchunk_vace_stitched_source_raw_inference_composite.mp4' | relative_url }}" type="video/mp4">
      </video>
      <figcaption><strong>Hard-motion failure.</strong> Faster movement and chunked processing expose inconsistent interpretation and temporal breakdown. This is why the method is not presented as a general video solution. Footage source: see <a href="{{ '/credits/' | relative_url }}">credits and open confirmation items</a>.</figcaption>
    </figure>
  </div>
</article>

<div class="experiment-pair">
  <article class="experiment-note">
    <p class="card-kicker">Experiment 04 · Semantic failure</p>
    <h3>A plausible image can still be the wrong image</h3>
    <a href="{{ '/images_kebab/seapavaa2026/ben_row2_source_vs_bad_semantic_inference.png' | relative_url }}" target="_blank">
      <img src="{{ '/images_kebab/seapavaa2026/ben_row2_source_vs_bad_semantic_inference.png' | relative_url }}" alt="Faded source compared with a visually polished but semantically incorrect generated image">
    </a>
    <p class="experiment-credit"><em>Ben</em> (1972), directed by Phil Karlson. Exact research-source edition still requires confirmation; see <a href="{{ '/credits/' | relative_url }}">credits</a>.</p>
    <p>The source is difficult to read, and the model invents a polished wooden structure and a face. The output is visually coherent but no longer describes the photographed scene. This is direct evidence for keeping the source visible and requiring human acceptance.</p>
  </article>
  <article class="experiment-note">
    <p class="card-kicker">Experiment 05 · High-resolution tiling</p>
    <h3>More local resolution can create a less coherent frame</h3>
    <a href="{{ '/images_kebab/seapavaa2026/reptilicus_beach_tiled_vs_fullframe_raw_inference.png' | relative_url }}" target="_blank">
      <img src="{{ '/images_kebab/seapavaa2026/reptilicus_beach_tiled_vs_fullframe_raw_inference.png' | relative_url }}" alt="Tiled raw Qwen inference with visible colour discontinuities compared with a coherent full-frame inference">
    </a>
    <p class="experiment-credit"><em>Reptilicus</em> (US release 1962), directed by Sidney Pink and Poul Bang. Exact research-source edition still requires confirmation; see <a href="{{ '/credits/' | relative_url }}">credits</a>.</p>
    <p>The four-tile result at left contains visible boundaries and conflicting local colour decisions. The full-frame result at right is more coherent, although it still remains a generated interpretation. This experiment is evidence against treating tiling as a solved route.</p>
  </article>
</div>

These are selected public examples. The [SEAPAVAA 2026 companion]({{ '/seapavaa-2026-companion/' | relative_url }}) contains the larger comparison set, individual source files, prompts, and presentation media.

## Route 1 · Source-owned luminance, generated chroma

<span class="status status-demonstrated">Demonstrated foundation</span>

The strongest common principle across the research is to keep the original frame responsible for luminance, geometry, texture, grain, softness, and damage. The generated result contributes chroma, which is mapped back over the source.

This does not prevent every colour error, but it sharply limits the model’s authority. It also makes failures easier to see: an invented colour can be reviewed as colour, without quietly replacing the complete photographic image.

**What is established:** this is the delivery and review format for the current public Qwen workflow and for the successful temporal experiments.

**What it does not solve:** colour can still attach to the wrong region, cross an edge, or change meaning between frames.

## Route 2 · Still-frame recovery without a matched reference

<span class="status status-demonstrated">Demonstrated, bounded</span>

For films with no surviving colour reference, Qwen Image Edit can work from the faded source, source-derived edge control, a softened colour chart, and a restrained restoration prompt.

Tests across several raw faded subjects produced useful first-pass chroma without visible chart patterns or the strongest forms of reference takeover. This is enough to justify continued research and a public test workflow.

**What is established:** the route can create plausible candidates worth human review.

**What is not established:** it is not historically authoritative, not consistently correct across subjects, and not yet a dependable one-click default.

## Route 3 · One approved same-shot colour anchor

<span class="status status-promising">Promising, strongest reference-driven route</span>

When one frame in a shot has an approved colour interpretation, that frame can act as a restrained palette and material guide for the remaining source frames. Each new frame still enters as the primary image; the anchor is not allowed to dictate pose, framing, or object layout.

The guarded TeleStyle V2 experiment completed all `338` frames of the FANJI waterfront shot without a processing failure. Human review promoted it as the best visual-quality route for that test. Delivery used untouched source luminance with generated chroma.

**What is established:** one carefully chosen anchor can hold a recurring shot palette across a substantial real sequence.

**Why confidence is still limited:** this is strong evidence from a defined shot, not proof of general success across films, motion types, or restoration aesthetics.

**Public evidence note:** the exact `338`-frame review package is not reproduced on this page. The conference companion shows an earlier [context-board experiment]({{ '/seapavaa-2026-companion/' | relative_url }}#slide-14) that explains the anchor idea, but it should not be read as evidence for the newer run.

## Route 4 · True paired data and a learned chroma model

<span class="status status-demonstrated">Demonstrated on paired material</span>

Where real source/reference pairs exist, a small open trainable model can learn residual chroma directly rather than asking a large image model to reinterpret every frame.

On the Frontier comparison, the retained full-resolution model used original source luminance and learned chroma. In the documented held-out review it was preferred to CopyCat on `9` of `16` shots and came within `1.79%` of CopyCat’s aggregate chroma error, while being much faster to run.

**What is established:** open, production-specific chroma learning is a credible route when genuine aligned pairs exist.

**What remains:** the result must be repeated on additional paired films before it can be described as a general replacement for the established CopyCat workflow.

**Public evidence note:** the published Frontier material currently documents how the paired frames were prepared and checked. A clearly labelled visual comparison for the newer open model will be added only after the held-out outputs have been cleared for publication.

## Route 5 · Video-aware chroma generation

<span class="status status-demonstrated">Demonstrated on favourable shots</span>

Wan/VACE-style video models can see a short sequence as a temporal object rather than as unrelated stills. The most successful setup used the source video, hard source-derived edge control, and one recovered middle-frame reference, then returned generated chroma to source luminance.

Two experiments are retained as archive-restoration-quality temporal successes. They show that the idea works on favourable low- or moderate-motion material.

**What is established:** video-aware generation can give coherent shot-level chroma under suitable conditions.

**What failed elsewhere:** a smooth video can still alter faces, clothing, objects, or geometry. On harder motion, temporal coherence sometimes stabilised the wrong interpretation.

## Route 6 · Approved keyframes plus temporal propagation

<span class="status status-promising">Active research</span>

A likely bridge between strong Qwen stills and a stable shot is:

1. choose a small number of representative source frames;
2. create and human-approve colour proposals for those exact frames;
3. use them as art-directed supervision for a temporal chroma model or feature-based propagation method;
4. infer the complete shot while retaining source luminance and geometry.

Early work has tested Qwen anchors and learned temporal adapters. Generated anchors are treated as **pseudo-targets**—approved interpretations, not historical ground truth.

**Why this route matters:** it could combine the visual quality of carefully reviewed stills with the speed and temporal calmness of a smaller shot model.

**Why it is not yet a result:** broader human review and comparison on difficult motion are still required.

## Route 7 · Full-resolution and tiled inference

<span class="status status-open">Open question</span>

High-resolution film scans can exceed the model’s comfortable image-editing range. Tiling can recover local detail, but it introduces seams, inconsistent colour ownership, and different interpretations of the same subject across tiles.

Some tiled tests were useful; others produced reference-content takeover or a scene assembled from incompatible local decisions. Tiling is therefore a research direction, not a recommended default.

The important next step is not simply “more pixels.” It is shared evidence across overlaps, source-bound registration, and a review method that catches tile-to-tile semantic drift.

## The unresolved centre of the problem

The working target is:

> original source luminance and geometry + temporally coherent, evidence-aware recovered chroma

Still-frame colour quality is no longer the only question. The harder problem is making one colour interpretation remain attached to the same face, garment, wall, tree, or object through motion, occlusion, and changing scale—without averaging the shot into lifeless colour and without allowing the model to redesign the film.

## What the project will not claim

- that generated colour is original colour when no historical evidence survives;
- that two favourable temporal shots solve general video consistency;
- that a high technical score replaces human viewing;
- that raw generated RGB is the preferred restoration result;
- that Qwen outputs become ground truth simply because they are visually strong;
- that one model or one reference strategy is appropriate for every film.

For the underlying examples, prompts, intermediate files, and presentation media, continue to the [SEAPAVAA 2026 companion]({{ '/seapavaa-2026-companion/' | relative_url }}).
