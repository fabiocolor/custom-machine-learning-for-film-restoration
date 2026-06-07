---
title: SEAPAVAA 2026 Companion
nav_order: 7
---

<style>
.seapavaa-note {
  padding: 1rem 1.1rem;
  margin: 1rem 0 1.4rem;
  border-left: 4px solid #d97706;
  background: rgba(245, 158, 11, 0.08);
  border-radius: 0.4rem;
}
.seapavaa-jump {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin: 1rem 0 1.8rem;
}
.seapavaa-jump a {
  display: inline-block;
  padding: 0.4rem 0.7rem;
  border-radius: 999px;
  border: 1px solid rgba(148, 163, 184, 0.35);
  text-decoration: none;
}
.seapavaa-guide {
  margin: 1rem 0 2rem;
  padding: 1rem 1.1rem;
  border: 1px solid rgba(148, 163, 184, 0.25);
  border-radius: 0.8rem;
  background: rgba(15, 23, 42, 0.22);
}
.seapavaa-guide p,
.seapavaa-guide ul {
  margin: 0.45rem 0;
}
.seapavaa-guide ul {
  padding-left: 1.2rem;
}
.seapavaa-slide {
  margin: 2.2rem 0 2.7rem;
  padding-top: 0.2rem;
}
.seapavaa-slide h2 {
  margin-bottom: 0.55rem;
}
.seapavaa-slide-intro {
  margin-bottom: 1rem;
}
.seapavaa-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
  margin: 1rem 0 0;
}
.seapavaa-card {
  border: 1px solid rgba(148, 163, 184, 0.35);
  border-radius: 0.9rem;
  padding: 0.85rem;
  background: rgba(255, 255, 255, 0.04);
}
.seapavaa-card h3 {
  margin-top: 0;
  margin-bottom: 0.35rem;
}
.seapavaa-role {
  display: inline-block;
  margin-bottom: 0.7rem;
  padding: 0.2rem 0.55rem;
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.01em;
  background: rgba(59, 130, 246, 0.12);
  color: #93c5fd;
}
.seapavaa-card p {
  margin-bottom: 0.65rem;
}
.seapavaa-card img,
.seapavaa-card video {
  width: 100%;
  height: auto;
  border-radius: 0.5rem;
  margin-bottom: 0.75rem;
}
.seapavaa-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}
</style>

# SEAPAVAA 2026 Companion

This page is meant to be read alongside the `SEAPAVAA 2026` presentation.

The projection version of the talk compresses many of the comparisons too much. This companion organizes the material by slide, so that when a given slide appears in the presentation, the audience can later revisit the exact images used on that slide, plus one or two extra references that support the same point.

<div class="seapavaa-note">
Open any still in a new tab to inspect it at full saved resolution. The motion examples below are native `mp4` files copied or rebuilt from the original source packages, not converted from the presentation GIFs.
</div>

<div class="seapavaa-guide">
  <p><strong>How to use this companion:</strong></p>
  <ul>
    <li>Go to the section that matches the slide number you just saw in the talk.</li>
    <li>The first card is the exact still shown on the slide, or the browser-safe motion equivalent of the slide GIF.</li>
    <li>The next one or two cards extend the same point with more context, wider framing, or an alternate example.</li>
  </ul>
</div>

## Jump by Slide

<div class="seapavaa-jump">
  <a href="#slide-1">1 Hero</a>
  <a href="#slide-2">2 Lineage</a>
  <a href="#slide-3">3 Recovery</a>
  <a href="#slide-4">4 Testing</a>
  <a href="#slide-5">5 Source Paths</a>
  <a href="#slide-6">6 References</a>
  <a href="#slide-7">7 Semantics</a>
  <a href="#slide-8">8 Contract</a>
  <a href="#slide-9">9 Still Route</a>
  <a href="#slide-10">10 Interior Woman</a>
  <a href="#slide-11">11 Shot0006</a>
  <a href="#slide-12">12 Hard Motion</a>
  <a href="#slide-13">13 Context Boards</a>
  <a href="#slide-14">14 Atlas</a>
  <a href="#slide-15">15 Tiling</a>
  <a href="#slide-16">16 Current Claim</a>
  <a href="#slide-17">17 Resources</a>
</div>

<section id="slide-1" class="seapavaa-slide">
  <h2>Slide 1 — Title / Hero Frame</h2>
  <p class="seapavaa-slide-intro">
    The opening image establishes the overall claim visually: constrained chroma recovery can preserve the frame while recovering missing color.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Shown on slide</span>
      <h3>Fanji full-frame split hero</h3>
      <a href="{{ '/images_kebab/seapavaa2026/fanji_c4_row3_garden_split_comparison_fullframe_clean.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/fanji_c4_row3_garden_split_comparison_fullframe_clean.png' | relative_url }}" alt="Fanji split hero image">
      </a>
      <p>The actual clean split comparison used to open the talk.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Fanji source versus composite</h3>
      <a href="{{ '/images_kebab/seapavaa2026/fanji_c4_row3_garden_source_vs_composite.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/fanji_c4_row3_garden_source_vs_composite.png' | relative_url }}" alt="Fanji source versus composite">
      </a>
      <p>The same subject presented as a direct before/after pair instead of a wipe comparison.</p>
    </div>
  </div>
</section>

<section id="slide-2" class="seapavaa-slide">
  <h2>Slide 2 — From CopyCat to Open-Weight Chroma Recovery</h2>
  <p class="seapavaa-slide-intro">
    This slide is mostly conceptual, but it points back to the earlier custom-machine-learning workflow that led into the current open-weight route.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Resource link</span>
      <h3>Public custom-machine-learning repo QR</h3>
      <a href="{{ '/images_kebab/seapavaa2026/custom_machine_learning_for_film_restoration_qr.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/custom_machine_learning_for_film_restoration_qr.png' | relative_url }}" alt="Public repository QR">
      </a>
      <div class="seapavaa-links">
        <a href="https://github.com/fabiocolor/custom-machine-learning-for-film-restoration" target="_blank">Open the public repository</a>
      </div>
    </div>
  </div>
</section>

<section id="slide-3" class="seapavaa-slide">
  <h2>Slide 3 — Correction Versus Recovery</h2>
  <p class="seapavaa-slide-intro">
    This slide defines the boundary between ordinary correction and constrained chroma recovery.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Shown on slide</span>
      <h3>Reptilicus full-frame recovery pair</h3>
      <a href="{{ '/images_kebab/seapavaa2026/recovery_pair_reptilicus_beach_fullframe.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/recovery_pair_reptilicus_beach_fullframe.png' | relative_url }}" alt="Reptilicus recovery pair">
      </a>
      <p>A clean full-frame before/after used to show why some problems require recovery rather than normal balancing.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Fanji hero as an alternate example</h3>
      <a href="{{ '/images_kebab/seapavaa2026/fanji_c4_row3_garden_split_comparison_fullframe_clean.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/fanji_c4_row3_garden_split_comparison_fullframe_clean.png' | relative_url }}" alt="Fanji alternate correction versus recovery example">
      </a>
      <p>An alternate framing of the same distinction on a different title and scene class.</p>
    </div>
  </div>
</section>

<section id="slide-4" class="seapavaa-slide">
  <h2>Slide 4 — Why Open-Weight Models, and How I Tested Them</h2>
  <p class="seapavaa-slide-intro">
    This slide is mainly methodological. I am not mirroring the private ComfyUI workflow screenshots publicly, but these two boards are the public-facing evidence of how the tests were structured and narrowed.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Prompt tournament selection</h3>
      <a href="{{ '/images_kebab/seapavaa2026/fanji_round4_row9_top3_raw_generations.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/fanji_round4_row9_top3_raw_generations.png' | relative_url }}" alt="Prompt tournament selection">
      </a>
      <p>A reduced board that shows the comparative-prompt workflow behind the still route, rather than a single one-off run.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Generated context board</h3>
      <a href="{{ '/images_kebab/seapavaa2026/02_overview_t091_generated_anchor_contact_sheet_t073_unl-55294673.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/02_overview_t091_generated_anchor_contact_sheet_t073_unl-55294673.png' | relative_url }}" alt="Generated context board">
      </a>
      <p>A public-safe example of the structured support material later used to keep neighboring frames and related shots aligned.</p>
    </div>
  </div>
</section>

<section id="slide-5" class="seapavaa-slide">
  <h2>Slide 5 — Two Source Paths, Two Different Problems</h2>
  <p class="seapavaa-slide-intro">
    The same film material can behave very differently depending on whether the model sees the raw scan or a balanced, partially stabilized version of it.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Shown on slide</span>
      <h3>Balanced versus unbalanced path comparison</h3>
      <a href="{{ '/images_kebab/seapavaa2026/shot0006_balanced_vs_unbalanced_paths_2x2.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/shot0006_balanced_vs_unbalanced_paths_2x2.png' | relative_url }}" alt="Balanced versus unbalanced comparison">
      </a>
      <p>The same subject shown under both source-condition routes.</p>
    </div>
  </div>
</section>

<section id="slide-6" class="seapavaa-slide">
  <h2>Slide 6 — The Reference Problem</h2>
  <p class="seapavaa-slide-intro">
    This is where the project failed clearly at the beginning: the reference image donated semantics instead of only guiding chroma.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Shown on slide</span>
      <h3>Leader-lady semantic contamination</h3>
      <a href="{{ '/images_kebab/seapavaa2026/leader_lady_semantic_contamination_gar01_triptych.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/leader_lady_semantic_contamination_gar01_triptych.png' | relative_url }}" alt="Leader lady semantic contamination">
      </a>
      <p>The clearest public example of a human reference rewriting the source subject instead of only guiding color.</p>
    </div>
  </div>
</section>

<section id="slide-7" class="seapavaa-slide">
  <h2>Slide 7 — The Semantic Boundary</h2>
  <p class="seapavaa-slide-intro">
    After the reference problem, the broader issue became clear: the model is not only predicting color, it is also trying to interpret what it thinks the image contains.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Shown on slide</span>
      <h3>Source versus bad semantic inference</h3>
      <a href="{{ '/images_kebab/seapavaa2026/ben_row2_source_vs_bad_semantic_inference.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/ben_row2_source_vs_bad_semantic_inference.png' | relative_url }}" alt="Source versus bad semantic inference">
      </a>
      <p>The model hallucinates a face because it cannot read the ambiguous source reliably.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Reference contamination as the harder version</h3>
      <a href="{{ '/images_kebab/seapavaa2026/leader_lady_semantic_contamination_gar01_triptych.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/leader_lady_semantic_contamination_gar01_triptych.png' | relative_url }}" alt="Reference contamination extra reference">
      </a>
      <p>If slide 7 defines semantics broadly, slide 6 shows what happens when a foreign semantic source is explicitly injected into the workflow.</p>
    </div>
  </div>
</section>

<section id="slide-8" class="seapavaa-slide">
  <h2>Slide 8 — The Product Contract</h2>
  <p class="seapavaa-slide-intro">
    The usable product is not the raw generated frame alone. It is the source frame retaining ownership of geometry, with generated or propagated chroma added back under review.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Shown on slide</span>
      <h3>Full lineage board</h3>
      <a href="{{ '/images_kebab/seapavaa2026/jug_auditorium_full_lineage_5stage.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/jug_auditorium_full_lineage_5stage.png' | relative_url }}" alt="Full lineage board">
      </a>
      <p>Source, reference, hard-Canny control, raw inference, and final composite in one view.</p>
    </div>
  </div>
</section>

<section id="slide-9" class="seapavaa-slide">
  <h2>Slide 9 — The Still Route Finally Generalized</h2>
  <p class="seapavaa-slide-intro">
    By this point the work stopped being a one-subject demo and started looking like a reusable still-image route.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Shown on slide</span>
      <h3>Varied still benchmark contact sheet</h3>
      <a href="{{ '/images_kebab/seapavaa2026/raw_scan_vs_raw_inference_contact_sheet_4x2.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/raw_scan_vs_raw_inference_contact_sheet_4x2.png' | relative_url }}" alt="Still benchmark contact sheet">
      </a>
      <p>Different scene classes, faces, daylight exteriors, and crowd material shown under the same general frame-by-frame route.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Prompt tournament selection</h3>
      <a href="{{ '/images_kebab/seapavaa2026/fanji_round4_row9_top3_raw_generations.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/fanji_round4_row9_top3_raw_generations.png' | relative_url }}" alt="Prompt tournament selection">
      </a>
      <p>A reduced view of the prompt-search process used to narrow the reusable still route.</p>
    </div>
  </div>
</section>

<section id="slide-10" class="seapavaa-slide">
  <h2>Slide 10 — First Temporal Success: Interior Woman</h2>
  <p class="seapavaa-slide-intro">
    This is the first bounded temporal success. The presentation used a GIF; this page exposes the same three-lane comparison as a browser-friendly `mp4`, plus the prompt-side semantic anchor layout used to explain why it held together at all.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Shown on slide</span>
      <h3>Interior Woman three-way temporal comparison</h3>
      <video controls preload="metadata">
        <source src="{{ '/media/seapavaa2026/obsession_interior_woman24_source_raw_inference_final_composite.mp4' | relative_url }}" type="video/mp4">
      </video>
      <p>Source, raw inference, and final composite across the full promoted 24-frame sequence.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Prompt-side semantic anchor layout</h3>
      <a href="{{ '/images_kebab/seapavaa2026/obsession_interior_woman24_source_raw_inference_final_composite_with_prompt_side.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/obsession_interior_woman24_source_raw_inference_final_composite_with_prompt_side.png' | relative_url }}" alt="Prompt-side semantic anchor layout">
      </a>
      <p>The layout used in the talk to show the semantic prompt anchoring explicitly.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Interior Woman preview still</h3>
      <a href="{{ '/images_kebab/seapavaa2026/obsession_interior_woman24_source_raw_inference_final_composite_preview.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/obsession_interior_woman24_source_raw_inference_final_composite_preview.png' | relative_url }}" alt="Interior Woman preview still">
      </a>
      <p>A single-frame still from the three-way comparison for closer inspection.</p>
    </div>
  </div>
</section>

<section id="slide-11" class="seapavaa-slide">
  <h2>Slide 11 — Temporal Success 2: Shot0006 Wan/VACE</h2>
  <p class="seapavaa-slide-intro">
    This is the cleaner bounded temporal success. The presentation used a GIF; the companion uses a source-built `mp4` version of the same three-lane comparison for easier inspection in the browser.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Shown on slide</span>
      <h3>Shot0006 native three-way comparison</h3>
      <video controls preload="metadata">
        <source src="{{ '/media/seapavaa2026/shot0006_source_raw_composite_native.mp4' | relative_url }}" type="video/mp4">
      </video>
      <p>Rebuilt from the original source, raw inference, and source-luma/final-composite review files.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Shot0006 preview still</h3>
      <a href="{{ '/images_kebab/seapavaa2026/shot0006_source_raw_inference_final_composite_fullrun_preview.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/shot0006_source_raw_inference_final_composite_fullrun_preview.png' | relative_url }}" alt="Shot0006 preview still">
      </a>
      <p>A single frame from the promoted run for closer still inspection.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Balanced versus unbalanced source path</h3>
      <a href="{{ '/images_kebab/seapavaa2026/shot0006_balanced_vs_unbalanced_paths_2x2.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/shot0006_balanced_vs_unbalanced_paths_2x2.png' | relative_url }}" alt="Shot0006 balanced versus unbalanced">
      </a>
      <p>The same shot also helps explain why the balanced route became more important for temporal work.</p>
    </div>
  </div>
</section>

<section id="slide-12" class="seapavaa-slide">
  <h2>Slide 12 — What Still Fails: Hard Motion</h2>
  <p class="seapavaa-slide-intro">
    The failure is not only wrong color. It is interpretation drift across contiguous frames. As with the other temporal slides, the presentation used a GIF and this page exposes the same comparison as a browser-safe `mp4`.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Shown on slide</span>
      <h3>Shot0011 native failure comparison</h3>
      <video controls preload="metadata">
        <source src="{{ '/media/seapavaa2026/shot0011_source_raw_composite_native.mp4' | relative_url }}" type="video/mp4">
      </video>
      <p>Native three-way comparison built from the original source, inference, and final composite package.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Shot0011 preview still</h3>
      <a href="{{ '/images_kebab/seapavaa2026/shot0011_fourchunk_vace_stitched_source_raw_inference_composite_preview.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/shot0011_fourchunk_vace_stitched_source_raw_inference_composite_preview.png' | relative_url }}" alt="Shot0011 preview still">
      </a>
      <p>A single still for reading the failure at frame level rather than only in motion.</p>
    </div>
  </div>
</section>

<section id="slide-13" class="seapavaa-slide">
  <h2>Slide 13 — Balanced Route: Context Boards</h2>
  <p class="seapavaa-slide-intro">
    Context boards helped later frames inherit earlier color decisions, but they remain limited by context length and semantic drift over long spans. The main card below is the motion version of the slide asset, with the actual context board visible under every frame.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Shown on slide</span>
      <h3>Shot0001 with context board motion comparison</h3>
      <video controls preload="metadata">
        <source src="{{ '/media/seapavaa2026/shot0001_t091_source_raw_inference_final_composite_fullrun_with_context_board.mp4' | relative_url }}" type="video/mp4">
      </video>
      <p>Source, raw inference, and final composite with the context board locked underneath the full run.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Shot0001 context-board preview still</h3>
      <a href="{{ '/images_kebab/seapavaa2026/shot0001_t091_source_raw_inference_final_composite_fullrun_with_context_board.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/shot0001_t091_source_raw_inference_final_composite_fullrun_with_context_board.png' | relative_url }}" alt="Shot0001 context-board preview still">
      </a>
      <p>The exact still layout from the presentation, for close reading without playing the clip.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Original T091 context board</h3>
      <a href="{{ '/images_kebab/seapavaa2026/02_overview_t091_generated_anchor_contact_sheet_t073_unl-55294673.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/02_overview_t091_generated_anchor_contact_sheet_t073_unl-55294673.png' | relative_url }}" alt="Original T091 context board">
      </a>
      <p>The actual context board itself, shown separately for close reading.</p>
    </div>
  </div>
</section>

<section id="slide-14" class="seapavaa-slide">
  <h2>Slide 14 — Atlas: Useful, But Not Yet Reliable</h2>
  <p class="seapavaa-slide-intro">
    The atlas can produce strong color, but the atlas itself becomes a semantic object, which is why the route remains unstable.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Shown on slide</span>
      <h3>Liked atlas target</h3>
      <a href="{{ '/images_kebab/seapavaa2026/liked_t085_target_resized_to_t092.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/liked_t085_target_resized_to_t092.png' | relative_url }}" alt="Liked atlas target">
      </a>
      <p>The preferred atlas artifact isolated from the comparison board.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Atlas comparison board</h3>
      <a href="{{ '/images_kebab/seapavaa2026/atlas_top_comparison.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/atlas_top_comparison.png' | relative_url }}" alt="Atlas comparison board">
      </a>
      <p>The wider comparison that shows why one attractive atlas output is not yet enough to call the route reliable.</p>
    </div>
  </div>
</section>

<section id="slide-15" class="seapavaa-slide">
  <h2>Slide 15 — Tiling and the Spatial-Context Hypothesis</h2>
  <p class="seapavaa-slide-intro">
    Tiling suggests that these models may be starved more by spatial context than by color alone.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Shown on slide</span>
      <h3>Tiled versus full-frame raw inference</h3>
      <a href="{{ '/images_kebab/seapavaa2026/reptilicus_beach_tiled_vs_fullframe_raw_inference.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/reptilicus_beach_tiled_vs_fullframe_raw_inference.png' | relative_url }}" alt="Tiled versus full-frame raw inference">
      </a>
      <p>The raw inference often retains more detail once the model sees more spatial context.</p>
    </div>
  </div>
</section>

<section id="slide-16" class="seapavaa-slide">
  <h2>Slide 16 — What We Can Claim Now</h2>
  <p class="seapavaa-slide-intro">
    The closing claim of the talk is not that temporal restoration is solved. It is that still-image chroma recovery is already useful on varied faded-film material, and that bounded temporal successes are real. The long run below is the browser-safe companion version of the final motion example.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Shown on slide</span>
      <h3>Fanji 600-frame full run</h3>
      <video controls preload="metadata">
        <source src="{{ '/media/seapavaa2026/fanji_600_source_raw_inference_final_composite_fullrun.mp4' | relative_url }}" type="video/mp4">
      </video>
      <p>A long-span example used to support the claim that the still route is already practically useful.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Fanji 600-frame preview still</h3>
      <a href="{{ '/images_kebab/seapavaa2026/fanji_600_source_raw_inference_final_composite_fullrun_preview.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/fanji_600_source_raw_inference_final_composite_fullrun_preview.png' | relative_url }}" alt="Fanji 600 frame preview still">
      </a>
      <p>A still from the same run for closer frame-level inspection.</p>
    </div>
    <div class="seapavaa-card">
      <span class="seapavaa-role">Companion expansion</span>
      <h3>Still-route diversity sheet</h3>
      <a href="{{ '/images_kebab/seapavaa2026/raw_scan_vs_raw_inference_contact_sheet_4x2.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/raw_scan_vs_raw_inference_contact_sheet_4x2.png' | relative_url }}" alt="Still route diversity sheet">
      </a>
      <p>A second reminder that the closing claim depends on variety, not on a single good-looking example.</p>
    </div>
  </div>
</section>

<section id="slide-17" class="seapavaa-slide">
  <h2>Slide 17 — Thank You / Resources</h2>
  <p class="seapavaa-slide-intro">
    The presentation closes by inviting further inspection. This public repository is one of the main open references connected to the broader workflow lineage.
  </p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Resource link</span>
      <h3>Public repository QR</h3>
      <a href="{{ '/images_kebab/seapavaa2026/custom_machine_learning_for_film_restoration_qr.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/custom_machine_learning_for_film_restoration_qr.png' | relative_url }}" alt="Public repository QR code">
      </a>
      <div class="seapavaa-links">
        <a href="https://github.com/fabiocolor/custom-machine-learning-for-film-restoration" target="_blank">Open the public repository</a>
      </div>
    </div>
  </div>
</section>
