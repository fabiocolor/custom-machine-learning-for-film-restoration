---
layout: default
title: Open-Weight Color Recovery
nav_order: 1
has_children: true
permalink: /open-weight-color-recovery/
---

<p class="eyebrow">Primary research track</p>

# Open-Weight Colour Recovery

Open-weight image models create a new possibility for faded-film restoration: they can propose plausible colour even when no perfectly matching reference survives. This research studies how to use that ability without allowing the model to replace the photographic identity of the source.

Qwen Image Edit is the current focus because it can respond to the source frame, visual references, and written direction in one workflow. The model is not treated as an oracle. It is treated as one instrument in a larger restoration process.

<div class="hero-buttons">
  <a href="{{ '/qwen-color-recovery-app/' | relative_url }}" class="btn btn-primary">Use the Qwen workflow</a>
  <a href="{{ '/open-weight-color-recovery/research-routes/' | relative_url }}" class="btn btn-outline">See what works and what remains open</a>
</div>

> **Current status:** this is active, changing research—not a finished archival system or a fixed recipe. Workflows, prompts, settings, and conclusions will be revised as experiments continue. Individual-frame colour recovery is useful enough for controlled testing. One approved-anchor route and two favourable-shot video routes have succeeded under bounded conditions. General temporal consistency—especially through difficult motion and occlusion—remains unresolved.

## The central idea

The source frame should remain authoritative for:

- composition and framing;
- faces, bodies, objects, and silhouettes;
- luminance, texture, grain, softness, and damage;
- edge placement and local detail.

The model is asked to contribute colour information. Its proposal can be guided by a matched reference frame, a broader visual atlas, period evidence, a colour chart, or a carefully written description. The proposal is then recombined with the source so that original luminance and fine structure are retained.

<div class="method-flow" role="list" aria-label="Open-weight colour recovery method">
  <div role="listitem"><span>01</span><strong>Prepare</strong><p>Balance the faded scan without inventing a creative look.</p></div>
  <div role="listitem"><span>02</span><strong>Guide</strong><p>Choose the strongest available colour evidence and state its limits.</p></div>
  <div role="listitem"><span>03</span><strong>Generate</strong><p>Ask Qwen Image Edit for a source-faithful colour proposal.</p></div>
  <div role="listitem"><span>04</span><strong>Recombine</strong><p>Return to the original luminance, geometry, and texture.</p></div>
  <div role="listitem"><span>05</span><strong>Review</strong><p>Compare alternatives across frames and record uncertainty.</p></div>
</div>

## Why this is a research problem

A convincing still image is not enough. Film restoration adds several harder questions:

- Does the colour remain stable across neighbouring frames?
- Does a reference guide the model, or does it quietly replace source content?
- Can one palette remain coherent through camera and subject movement?
- Which parts of the result come from evidence, and which are interpretation?
- How should uncertain regions be marked and reviewed?

These questions define the next stage of this repository. New experiments will be organised around repeatable tests, visual comparisons, and downloadable working material.

## Current Qwen Image Edit workflow

The public ComfyUI workflow accepts a faded source frame, creates a colour proposal with Qwen Image Edit, and produces a composite that carries the proposal’s chroma over the source frame’s luminance.

It is designed for still-frame research and short controlled tests. It is not yet a complete archival pipeline for long sequences.

<div class="link-grid">
  <a href="{{ '/open-weight-color-recovery/research-routes/' | relative_url }}"><strong>Research routes and evidence</strong><span>A plain-language account of demonstrated, promising, and unresolved approaches.</span></a>
  <a href="{{ '/qwen-color-recovery-app/' | relative_url }}"><strong>Workflow and downloads</strong><span>Install, test, and understand the current ComfyUI workflow.</span></a>
  <a href="{{ '/seapavaa-2026-companion/' | relative_url }}"><strong>SEAPAVAA 2026 companion</strong><span>Inspect the examples, prompts, comparisons, and media shown in the presentation.</span></a>
</div>

## Research directions

The repository is being expanded to cover:

1. **Reference design** — matched frames, approved same-shot anchors, palette boards, atlases, period references, and reference-free prompting.
2. **Source preservation** — stronger controls against altered identity, geometry, texture, and lighting.
3. **Temporal colour** — Qwen keyframes, small learned chroma adapters, video-aware generation, and feature-based propagation.
4. **Paired-data learning** — open trainable models for productions with genuine aligned source/reference material.
5. **Resolution** — full-frame and tiled strategies that share evidence without seams or local semantic disagreement.
6. **Human review** — presenting alternatives and uncertainty clearly enough for curators, colourists, and restoration teams to make informed decisions.

## How to read the results

Every result should distinguish the surviving source, the evidence supplied to the model, the raw generated proposal, and the final source-preserving composite. When a historical colour is not known, the language should say “proposed,” “recovered from a reference,” or “interpreted”—not claim certainty that the evidence cannot support.
