---
layout: default
title: FIAT/IFTA 2026 Companion
nav_order: 2
permalink: /fiat-ifta-2026-companion/
description: Video examples and practical workflow notes from Fabio Bedoya's FIAT/IFTA 2026 presentation on the limits of AI in film restoration.
---

<style>
.fiat-companion h1 { max-width: 30ch; font-size: clamp(2rem, 4.5vw, 3.3rem); }
.fiat-companion .fiat-byline { margin: 0.8rem 0 1.1rem; color: #56625c; }
.fiat-companion .fiat-links, .fiat-companion .fiat-jump { display: flex; flex-wrap: wrap; gap: 0.6rem; margin: 1rem 0 1.5rem; }
.fiat-companion .fiat-links a, .fiat-companion .fiat-jump a { display: inline-flex; align-items: center; min-height: 44px; padding: 0.5rem 0.85rem; border: 1px solid #a9a395; border-radius: 2px; text-decoration: none; font-size: 1rem; }
.fiat-companion .fiat-links a:first-child { color: #fff; background: #244136; border-color: #244136; }
.fiat-companion .fiat-links a:focus-visible, .fiat-companion .fiat-jump a:focus-visible, .fiat-companion summary:focus-visible { outline: 3px solid #a47a3c; outline-offset: 3px; }
.fiat-companion .fiat-note { padding: 1rem 1.15rem; border-left: 3px solid #a47a3c; background: #eae5d9; }
.fiat-companion section { scroll-margin-top: 1rem; margin: 2.5rem 0; }
.fiat-companion section h2 { margin-top: 0; }
.fiat-companion .fiat-card { margin: 1.4rem 0; padding: 1.1rem; background: #fbf9f3; border: 1px solid #d6d0c2; border-top: 3px solid #356c60; }
.fiat-companion .fiat-card h3 { margin: 0.15rem 0 0.5rem; }
.fiat-companion .fiat-meta { color: #56625c; font-size: 0.95rem; margin: 0 0 0.55rem; }
.fiat-companion video { display: block; width: 100%; height: auto; max-height: 70vh; background: #0c100e; margin: 1rem 0; }
.fiat-companion iframe { display: block; width: 100%; aspect-ratio: 16 / 9; border: 0; background: #0c100e; margin: 1rem 0; }
.fiat-companion .fiat-caption { color: #56625c; font-size: 0.95rem; line-height: 1.5; }
.fiat-companion .fiat-file { display: inline-flex; align-items: center; min-height: 44px; font-weight: 600; overflow-wrap: anywhere; }
.fiat-companion details { margin: 1rem 0 0; padding-top: 0.8rem; border-top: 1px solid #d6d0c2; }
.fiat-companion summary { min-height: 44px; cursor: pointer; font-weight: 600; }
.fiat-companion p:last-child { margin-bottom: 0; }
@media (max-width: 480px) { .fiat-companion .fiat-card { padding: 0.8rem; } .fiat-companion .fiat-links a { width: 100%; } }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
</style>

<div class="fiat-companion" markdown="1">

<p class="eyebrow">FIAT/IFTA World Conference · São Paulo · 8 October 2026</p>

# The Current Limits of AI in Film Restoration and How They May Be Surpassed

<p class="fiat-byline">Fabio Bedoya · Head of Restoration, Filmfinity<br>Cinemateca Brasileira</p>

<div class="fiat-links">
  <a href="https://github.com/fabiocolor/custom-machine-learning-for-film-restoration">Research and workflows on GitHub</a>
</div>

<p>Video examples from the talk, with original-resolution MP4 access and notes on what each result demonstrates.</p>

<p class="fiat-note">For the highest available streaming quality, open the player's settings and choose its highest resolution. Use <strong>Open video / download original MP4</strong> for the original export. The dimensions below describe the complete file; individual panels in a comparison can be smaller.</p>

<nav class="fiat-jump" aria-label="Video examples">
  <a href="#reference-recovery">Reference-based recovery</a>
  <a href="#telestyle">Colour through a shot</a>
  <a href="#diffusion-upscaling">Diffusion upscaling</a>
  <a href="#combining-sources">Combining sources</a>
  <a href="#inside-existing-tools">Tool control</a>
</nav>



<section id="video-examples">
<h2 id="video-examples-title">Video examples</h2>

<article id="reference-recovery" class="fiat-card">
  <p class="fiat-meta">Replacement for slides 5–6 · 1920 × 1080 comparison export · 1 minute 9.92 seconds · 24 fps</p>
  <h3 id="reference-recovery-title">Candy Candy: reference-based colour recovery</h3>
  <p>Colour from a matched French PAL DVD reference is transferred to a faded 16mm scan while retaining the film's detail. This is a different example of the reference-trained colour-recovery method discussed in the talk.</p>
  <iframe src="https://drive.google.com/file/d/11UucDpEAC5QRlfF3BN12f3mggg-S58Ds/preview" title="Candy Candy: scan, balanced source, PAL DVD reference and colour recovery" loading="lazy" allow="fullscreen" allowfullscreen></iframe>
  <p class="fiat-caption">The four-way comparison shows the original scan, the balanced and cleaned scan, the PAL DVD reference and the machine-learning result. The 1920 × 1080 file is a comparison export; the reference itself is standard definition. Reference colour can have its own grading and transfer limitations.</p>
  <a class="fiat-file" href="https://drive.google.com/file/d/11UucDpEAC5QRlfF3BN12f3mggg-S58Ds/view">Open comparison / download original MP4</a>
  <details>
    <summary>Full-resolution result: 4400 × 3300</summary>
    <p>The separate colour-recovery result retains the scan's 4400 × 3300 dimensions. The original file is silent, 24 fps, HEVC, about 298 MiB. Streaming may use a smaller rendition; download the original for full-resolution inspection.</p>
    <a class="fiat-file" href="https://drive.google.com/file/d/1EgkquRW2zm2lQzR_uWOQCSvpl0agE7G1/view">Open full-resolution result / download original MP4</a>
  </details>
</article>

<article id="telestyle" class="fiat-card">
  <p class="fiat-meta">Slide 9 · 1920 × 1080 export · 11.27 seconds · 30 fps</p>
  <h3 id="telestyle-title">Counter Attack: one reference for the whole shot</h3>
  <p>TeleStyle carries an approved colour reference through the shot. The result still needs frame-by-frame review.</p>
  <iframe src="https://drive.google.com/file/d/1uRuH6HdDL0v13uGQPMso3sRWXKP46LI8/preview" title="Counter Attack: one reference for the whole shot" loading="lazy" allow="fullscreen" allowfullscreen></iframe>
  <p class="fiat-caption">This comparison is an HD viewing export. The panels inside it are smaller than the full canvas.</p>
  <a class="fiat-file" href="https://drive.google.com/file/d/1uRuH6HdDL0v13uGQPMso3sRWXKP46LI8/view">Open video / download original MP4</a>
</article>

<article id="h3-controlnet" class="fiat-card">
  <p class="fiat-meta">Slide 11 · 1920 × 840 export · 12.83 seconds · 24 fps</p>
  <h3 id="h3-controlnet-title">Counter Attack: H3, ControlNet and Temporal CbCr</h3>
  <p>H3 proposes colour over a section of the shot. Edge control helps it follow the source geometry and movement. The Temporal CbCr adapter is used to finish the colour across the shot.</p>
  <iframe src="https://drive.google.com/file/d/1OQcp7SrwmFZoUiFJ6NC8EfHgI68TGmxi/preview" title="Counter Attack: H3, ControlNet and Temporal CbCr" loading="lazy" allow="fullscreen" allowfullscreen></iframe>
  <p class="fiat-caption">Only the chroma is retained; the original scan supplies luminance, grain and fine detail.</p>
  <a class="fiat-file" href="https://drive.google.com/file/d/1OQcp7SrwmFZoUiFJ6NC8EfHgI68TGmxi/view">Open video / download original MP4</a>
</article>

<article id="temporal-cbcr" class="fiat-card">
  <p class="fiat-meta">Slide 13 · 1920 × 850 export · 6.83 seconds · 24 fps</p>
  <h3 id="temporal-cbcr-title">Unman, Wittering and Zigo: Temporal CbCr adapter</h3>
  <p>A small model learns from approved teacher frames and supplies colour to the remaining frames. Watch the colour across the full shot, rather than judging a single frame.</p>
  <iframe src="https://drive.google.com/file/d/1s7i8nd7tRFuwbACbc-MnJHQNtpNxyhDD/preview" title="Unman, Wittering and Zigo: Temporal CbCr adapter" loading="lazy" allow="fullscreen" allowfullscreen></iframe>
  <p class="fiat-caption">The comparison export shows the workflow result. It is not evidence that generated colour is historically correct.</p>
  <a class="fiat-file" href="https://drive.google.com/file/d/1s7i8nd7tRFuwbACbc-MnJHQNtpNxyhDD/view">Open video / download original MP4</a>
</article>

<article id="diffusion-upscaling" class="fiat-card">
  <p class="fiat-meta">Slide 15 · 1920 × 756 export · 26.00 seconds · 24 fps</p>
  <h3 id="diffusion-upscaling-title">El Tinterillo: diffusion upscaling, the stairs</h3>
  <p>The surviving sources are a damaged 16mm print and a soft, cropped telecine. This test explores a video model rebuilding detail while following the surviving picture and movement.</p>
  <iframe src="https://drive.google.com/file/d/1IMC4AAJydIX2pnxw4hvxSTr4l9RWtrAw/preview" title="El Tinterillo: diffusion upscaling, the stairs" loading="lazy" allow="fullscreen" allowfullscreen></iframe>
  <p class="fiat-caption">The model result is 768 × 432, shown inside a 1920 × 756 comparison export. It includes geometry calibration and tone/dissolve finishing. A first-frame brightness jump and limitations in faces and fine detail remain. The synthetic detail must be declared.</p>
  <a class="fiat-file" href="https://drive.google.com/file/d/1IMC4AAJydIX2pnxw4hvxSTr4l9RWtrAw/view">Open video / download original MP4</a>
</article>

<article id="combining-sources" class="fiat-card">
  <p class="fiat-meta">Slide 19 · 1920 × 832 export · 9.42 seconds · 24 fps</p>
  <h3 id="combining-sources-title">Knight of the Trail: combining sources and reconstructing damage</h3>
  <p>A nitrate print and a safety copy are aligned and brought to a common look. Usable surviving frames are selected first; reconstruction is reserved for the damage that neither element can supply.</p>
  <iframe src="https://drive.google.com/file/d/1oNpHO2ljDAHTvxQYwU1eKfjBkyj3hk6K/preview" title="Knight of the Trail: combining sources and reconstructing damage" loading="lazy" allow="fullscreen" allowfullscreen></iframe>
  <p class="fiat-caption">This HD comparison export presents a 640 × 512 working-resolution test. It is not a native-HD restoration. Silent.</p>
  <a class="fiat-file" href="https://drive.google.com/file/d/1oNpHO2ljDAHTvxQYwU1eKfjBkyj3hk6K/view">Open video / download original MP4</a>
</article>

<article id="inside-existing-tools" class="fiat-card">
  <p class="fiat-meta">Slide 21 · 1920 × 1080 export · 30.00 seconds · 24 fps</p>
  <h3 id="inside-existing-tools-title">Point Blank: AI inside an existing restoration tool</h3>
  <p>An early research test in Phoenix: after Dry Clean, a model paints protection masks in the project. Red shows the changes made by Dry Clean.</p>
  <iframe src="https://drive.google.com/file/d/1mzL4lEaw5kf331CFtTPEtEfQqpLfmiVs/preview" title="Point Blank: AI inside an existing restoration tool" loading="lazy" allow="fullscreen" allowfullscreen></iframe>
  <p class="fiat-caption">This is a workflow screencast, not a finished restoration comparison. Silent.</p>
  <a class="fiat-file" href="https://drive.google.com/file/d/1mzL4lEaw5kf331CFtTPEtEfQqpLfmiVs/view">Open video / download original MP4</a>
</article>

</section>

<section id="public-examples" markdown="1">

## Reconstruction and dialogue examples

The 15-frame-gap and dialogue-recovery clips from the talk are not included in this public companion. The Knight of the Trail comparison above is a related reconstruction example: it concerns damaged picture supplied by two surviving elements, rather than a complete 15-frame gap. No alternate dialogue-recovery clip is presented here.

</section>

<section class="fiat-reading" markdown="1">

## Reading the examples

- In the colour-recovery workflow, the scan supplies the luminance, detail and grain. The model supplies a colour proposal. Generated colour remains an interpretation unless a surviving reference supports it.
- A convincing frame is only a starting point. Review the whole shot for flicker, drift, inconsistent colour and changes to movement or geometry.
- Diffusion upscaling creates fine detail that the surviving element may no longer contain. That synthetic contribution needs to be declared.
- For reconstruction, keep surviving frames and usable picture intact. Identify the regions or frames that were generated.

The resolution of a viewing file and the resolution used by a model are different things. An HD export does not mean the model worked at HD, or that generated detail was recovered from the film.

</section>

<section id="workflows" markdown="1">

## Workflows and research

- [Reference-trained colour recovery]({{ '/chroma-recovery/' | relative_url }}): learn from aligned source and reference frames, then combine the predicted colour with the source luminance.
- [Open-weight colour recovery]({{ '/open-weight-color-recovery/' | relative_url }}): create and review colour proposals while keeping the scan authoritative.
- [Training, inference and review]({{ '/training-inference-review/' | relative_url }}): preparation, iteration and the decisions needed before a result is accepted.
- [Research routes and unresolved questions]({{ '/open-weight-color-recovery/research-routes/' | relative_url }}): an earlier research snapshot with evidence, limitations and unresolved questions.

Film excerpts remain the property of their respective rights holders. Their inclusion here does not grant permission to reuse them. [Credits and attribution]({{ '/credits/' | relative_url }}).

</section>
</div>
