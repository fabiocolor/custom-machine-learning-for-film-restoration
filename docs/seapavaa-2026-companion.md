---
title: SEAPAVAA 2026 Companion
nav_order: 7
---

<style>
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
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
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
.seapavaa-files {
  margin-top: 0.6rem;
  padding-top: 0.65rem;
  border-top: 1px solid rgba(148, 163, 184, 0.2);
  font-size: 0.94rem;
}
.seapavaa-files summary {
  cursor: pointer;
  font-weight: 600;
  margin-bottom: 0.5rem;
}
.seapavaa-filelist {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 0.8rem;
}
</style>

# SEAPAVAA 2026 Companion

This page follows the presentation slide by slide.

Each section gives you the exact element shown in the talk, and when useful, the separate parts behind that same element so you can inspect them individually.

## Jump by Slide

<div class="seapavaa-jump">
  <a href="#slide-1">1 Hero</a>
  <a href="#slide-2">2 CopyCat</a>
  <a href="#slide-3">3 Recovery</a>
  <a href="#slide-4">4 Workflow</a>
  <a href="#slide-5">5 Source Paths</a>
  <a href="#slide-6">6 Reference Problem</a>
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
  <p class="seapavaa-slide-intro">This is the exact image from the presentation, followed by the separate parts behind the same example.</p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Fanji full-frame split hero</h3>
      <a href="{{ '/images_kebab/seapavaa2026/fanji_c4_row3_garden_split_comparison_fullframe_clean.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/fanji_c4_row3_garden_split_comparison_fullframe_clean.png' | relative_url }}" alt="Fanji split hero image">
      </a>
      <details class="seapavaa-files">
        <summary>Open the parts of this example</summary>
        <div class="seapavaa-filelist">
          <a href="{{ '/images_kebab/seapavaa2026/originals/fanji_garden/01_source_fanji_film_copy_000015-db56f6f7.png' | relative_url }}" target="_blank">Source</a>
          <a href="{{ '/images_kebab/seapavaa2026/originals/fanji_garden/02_control_fanji_film_copy_r4_v1_03_garden_buil-dd5a1638.png' | relative_url }}" target="_blank">Control</a>
          <a href="{{ '/images_kebab/seapavaa2026/originals/fanji_garden/03_reference_Belak_Color_Patch_Chart_softblur_32-9142a789.png' | relative_url }}" target="_blank">Reference</a>
          <a href="{{ '/images_kebab/seapavaa2026/originals/fanji_garden/04_inference_frame_000000_test-7b87dbc0.png' | relative_url }}" target="_blank">Raw inference</a>
          <a href="{{ '/images_kebab/seapavaa2026/originals/fanji_garden/05_final_composite_fanji_film_copy_r4_v1_03_garden_buil-1622230d.png' | relative_url }}" target="_blank">Final composite</a>
        </div>
      </details>
    </div>
  </div>
</section>

<section id="slide-2" class="seapavaa-slide">
  <h2>Slide 2 — From CopyCat to Open-Weight Chroma Recovery</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Mission: Kill comparison</h3>
      <video controls preload="metadata" poster="{{ '/images_kebab/mission-kill/mission-kill-chroma-recovery-comparison.png' | relative_url }}">
        <source src="{{ '/media/seapavaa2026/mission_kill_color_comparison_web.mp4' | relative_url }}" type="video/mp4">
      </video>
      <details class="seapavaa-files">
        <summary>Open this example</summary>
        <div class="seapavaa-filelist">
          <a href="{{ '/media/seapavaa2026/mission_kill_color_comparison_web.mp4' | relative_url }}" target="_blank">Video comparison</a>
          <a href="{{ '/images_kebab/mission-kill/mission-kill-chroma-recovery-comparison.png' | relative_url }}" target="_blank">Still comparison</a>
        </div>
      </details>
    </div>
  </div>
</section>

<section id="slide-3" class="seapavaa-slide">
  <h2>Slide 3 — Correction Versus Recovery</h2>
  <p class="seapavaa-slide-intro">This is the exact comparison shown in the presentation, with the individual files behind it.</p>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Reptilicus full-frame recovery pair</h3>
      <a href="{{ '/images_kebab/seapavaa2026/recovery_pair_reptilicus_beach_fullframe.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/recovery_pair_reptilicus_beach_fullframe.png' | relative_url }}" alt="Reptilicus recovery pair">
      </a>
      <details class="seapavaa-files">
        <summary>Open the parts of this example</summary>
        <div class="seapavaa-filelist">
          <a href="{{ '/images_kebab/seapavaa2026/originals/reptilicus_beach/01_source_reptilicus_tlr_000025-40689881.png' | relative_url }}" target="_blank">Source</a>
          <a href="{{ '/images_kebab/seapavaa2026/originals/reptilicus_beach/02_control_reptilicus_tlr_05_beach_woman_canny-73d21cd9.png' | relative_url }}" target="_blank">Control</a>
          <a href="{{ '/images_kebab/seapavaa2026/originals/reptilicus_beach/03_reference_Belak_Color_Patch_Chart_softblur_32-9142a789.png' | relative_url }}" target="_blank">Reference</a>
          <a href="{{ '/images_kebab/seapavaa2026/originals/reptilicus_beach/04_inference_frame_000000_seed_0_cfg_1.000_Belak-0c1f0329.png' | relative_url }}" target="_blank">Raw inference</a>
          <a href="{{ '/images_kebab/seapavaa2026/originals/reptilicus_beach/05_final_composite_reptilicus_tlr_05_beach_woman_source-38de94d1.png' | relative_url }}" target="_blank">Final composite</a>
        </div>
      </details>
    </div>
  </div>
</section>

<section id="slide-4" class="seapavaa-slide">
  <h2>Slide 4 — Why Open-Weight Models, and How I Tested Them</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>ComfyUI workflow screenshot</h3>
      <a href="{{ '/images_kebab/seapavaa2026/comfyui_workflow_fanji_waterfront_screenshot.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/comfyui_workflow_fanji_waterfront_screenshot.png' | relative_url }}" alt="ComfyUI workflow screenshot">
      </a>
      <details class="seapavaa-files">
        <summary>Open the workflow</summary>
        <div class="seapavaa-filelist">
          <a href="{{ '/images_kebab/seapavaa2026/fanji_waterfront_workflow_for_jiminc.json' | relative_url }}" target="_blank">Workflow JSON</a>
          <a href="{{ '/images_kebab/seapavaa2026/fanji_waterfront_runnable_prompt_for_jiminc.json' | relative_url }}" target="_blank">Runnable prompt JSON</a>
        </div>
      </details>
    </div>
  </div>
</section>

<section id="slide-5" class="seapavaa-slide">
  <h2>Slide 5 — Two Source Paths, Two Different Problems</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Balanced versus unbalanced path comparison</h3>
      <a href="{{ '/images_kebab/seapavaa2026/interior_woman_balanced_vs_unbalanced_paths_2x2.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/interior_woman_balanced_vs_unbalanced_paths_2x2.png' | relative_url }}" alt="Balanced versus unbalanced comparison">
      </a>
    </div>
  </div>
</section>

<section id="slide-6" class="seapavaa-slide">
  <h2>Slide 6 — The Reference Problem</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Leader-lady semantic contamination</h3>
      <a href="{{ '/images_kebab/seapavaa2026/leader_lady_semantic_contamination_gar01_triptych.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/leader_lady_semantic_contamination_gar01_triptych.png' | relative_url }}" alt="Leader lady semantic contamination">
      </a>
    </div>
  </div>
</section>

<section id="slide-7" class="seapavaa-slide">
  <h2>Slide 7 — The Semantic Boundary</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Source versus bad semantic inference</h3>
      <a href="{{ '/images_kebab/seapavaa2026/ben_row2_source_vs_bad_semantic_inference.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/ben_row2_source_vs_bad_semantic_inference.png' | relative_url }}" alt="Source versus bad semantic inference">
      </a>
    </div>
  </div>
</section>

<section id="slide-8" class="seapavaa-slide">
  <h2>Slide 8 — The Product Contract</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Full lineage board</h3>
      <a href="{{ '/images_kebab/seapavaa2026/jug_auditorium_full_lineage_5stage.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/jug_auditorium_full_lineage_5stage.png' | relative_url }}" alt="Full lineage board">
      </a>
      <details class="seapavaa-files">
        <summary>Open the parts of this example</summary>
        <div class="seapavaa-filelist">
          <a href="{{ '/images_kebab/seapavaa2026/originals/jug_auditorium/01_source_juggernaut_tlr_000066-ed2dda29.png' | relative_url }}" target="_blank">Source</a>
          <a href="{{ '/images_kebab/seapavaa2026/originals/jug_auditorium/02_control_juggernaut_tlr_r5_v1_10_auditorium_c-16fdc330.png' | relative_url }}" target="_blank">Control</a>
          <a href="{{ '/images_kebab/seapavaa2026/originals/jug_auditorium/03_reference_Belak_Color_Patch_Chart_softblur_32-9142a789.png' | relative_url }}" target="_blank">Reference</a>
          <a href="{{ '/images_kebab/seapavaa2026/originals/jug_auditorium/04_inference_frame_000000_test-feb2c14f.png' | relative_url }}" target="_blank">Raw inference</a>
          <a href="{{ '/images_kebab/seapavaa2026/originals/jug_auditorium/05_final_composite_juggernaut_tlr_r5_v1_10_auditorium_c-9d2f7cbe.png' | relative_url }}" target="_blank">Final composite</a>
        </div>
      </details>
    </div>
  </div>
</section>

<section id="slide-9" class="seapavaa-slide">
  <h2>Slide 9 — The Still Route Finally Generalized</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Varied still benchmark contact sheet</h3>
      <a href="{{ '/images_kebab/seapavaa2026/raw_scan_vs_raw_inference_contact_sheet_4x2.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/raw_scan_vs_raw_inference_contact_sheet_4x2.png' | relative_url }}" alt="Still benchmark contact sheet">
      </a>
    </div>
  </div>
</section>

<section id="slide-10" class="seapavaa-slide">
  <h2>Slide 10 — First Temporal Success: Interior Woman</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Interior Woman temporal comparison</h3>
      <video controls preload="metadata">
        <source src="{{ '/media/seapavaa2026/obsession_interior_woman24_source_raw_inference_final_composite.mp4' | relative_url }}" type="video/mp4">
      </video>
      <details class="seapavaa-files">
        <summary>Open this example</summary>
        <div class="seapavaa-filelist">
          <a href="{{ '/media/seapavaa2026/obsession_interior_woman24_source_raw_inference_final_composite.mp4' | relative_url }}" target="_blank">Full comparison video</a>
          <a href="{{ '/images_kebab/seapavaa2026/obsession_interior_woman24_source_raw_inference_final_composite_preview.png' | relative_url }}" target="_blank">Preview still</a>
          <a href="{{ '/images_kebab/seapavaa2026/obsession_interior_woman24_source_raw_inference_final_composite_with_prompt_side.png' | relative_url }}" target="_blank">Prompt-side still</a>
        </div>
      </details>
    </div>
  </div>
</section>

<section id="slide-11" class="seapavaa-slide">
  <h2>Slide 11 — Temporal Success 2: Shot0006 Wan/VACE</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Shot0006 native three-way comparison</h3>
      <video controls preload="metadata">
        <source src="{{ '/media/seapavaa2026/shot0006_source_raw_composite_native.mp4' | relative_url }}" type="video/mp4">
      </video>
      <details class="seapavaa-files">
        <summary>Open this example</summary>
        <div class="seapavaa-filelist">
          <a href="{{ '/media/seapavaa2026/shot0006_source_raw_composite_native.mp4' | relative_url }}" target="_blank">Full comparison video</a>
          <a href="{{ '/images_kebab/seapavaa2026/shot0006_source_raw_inference_final_composite_fullrun_preview.png' | relative_url }}" target="_blank">Preview still</a>
          <a href="{{ '/images_kebab/seapavaa2026/shot0006_source_raw_inference_final_composite.png' | relative_url }}" target="_blank">Three-panel still</a>
        </div>
      </details>
    </div>
  </div>
</section>

<section id="slide-12" class="seapavaa-slide">
  <h2>Slide 12 — What Still Fails: Hard Motion</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Shot0011 native failure comparison</h3>
      <video controls preload="metadata">
        <source src="{{ '/media/seapavaa2026/shot0011_source_raw_composite_native.mp4' | relative_url }}" type="video/mp4">
      </video>
      <details class="seapavaa-files">
        <summary>Open this example</summary>
        <div class="seapavaa-filelist">
          <a href="{{ '/media/seapavaa2026/shot0011_source_raw_composite_native.mp4' | relative_url }}" target="_blank">Full comparison video</a>
          <a href="{{ '/images_kebab/seapavaa2026/shot0011_fourchunk_vace_stitched_source_raw_inference_composite_preview.png' | relative_url }}" target="_blank">Preview still</a>
        </div>
      </details>
    </div>
  </div>
</section>

<section id="slide-13" class="seapavaa-slide">
  <h2>Slide 13 — Balanced Route: Context Boards</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Shot0001 with context board</h3>
      <video controls preload="metadata">
        <source src="{{ '/media/seapavaa2026/shot0001_t091_source_raw_inference_final_composite_fullrun_with_context_board.mp4' | relative_url }}" type="video/mp4">
      </video>
      <details class="seapavaa-files">
        <summary>Open this example</summary>
        <div class="seapavaa-filelist">
          <a href="{{ '/media/seapavaa2026/shot0001_t091_source_raw_inference_final_composite_fullrun_with_context_board.mp4' | relative_url }}" target="_blank">Full comparison video</a>
          <a href="{{ '/images_kebab/seapavaa2026/shot0001_t091_source_raw_inference_final_composite_fullrun_with_context_board.png' | relative_url }}" target="_blank">Preview still</a>
          <a href="{{ '/images_kebab/seapavaa2026/02_overview_t091_generated_anchor_contact_sheet_t073_unl-55294673.png' | relative_url }}" target="_blank">Context board</a>
        </div>
      </details>
    </div>
  </div>
</section>

<section id="slide-14" class="seapavaa-slide">
  <h2>Slide 14 — Atlas: Useful, But Not Yet Reliable</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Liked atlas target</h3>
      <a href="{{ '/images_kebab/seapavaa2026/liked_t085_target_resized_to_t092.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/liked_t085_target_resized_to_t092.png' | relative_url }}" alt="Liked atlas target">
      </a>
    </div>
  </div>
</section>

<section id="slide-15" class="seapavaa-slide">
  <h2>Slide 15 — Tiling and the Spatial-Context Hypothesis</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Tiled versus full-frame raw inference</h3>
      <a href="{{ '/images_kebab/seapavaa2026/reptilicus_beach_tiled_vs_fullframe_raw_inference.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/reptilicus_beach_tiled_vs_fullframe_raw_inference.png' | relative_url }}" alt="Tiled versus full-frame raw inference">
      </a>
    </div>
  </div>
</section>

<section id="slide-16" class="seapavaa-slide">
  <h2>Slide 16 — What We Can Claim Now</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Fanji 600-frame full run</h3>
      <video controls preload="metadata">
        <source src="{{ '/media/seapavaa2026/fanji_600_source_raw_inference_final_composite_fullrun.mp4' | relative_url }}" type="video/mp4">
      </video>
      <details class="seapavaa-files">
        <summary>Open this example</summary>
        <div class="seapavaa-filelist">
          <a href="{{ '/media/seapavaa2026/fanji_600_source_raw_inference_final_composite_fullrun.mp4' | relative_url }}" target="_blank">Full comparison video</a>
          <a href="{{ '/images_kebab/seapavaa2026/fanji_600_source_raw_inference_final_composite_fullrun_preview.png' | relative_url }}" target="_blank">Preview still</a>
        </div>
      </details>
    </div>
  </div>
</section>

<section id="slide-17" class="seapavaa-slide">
  <h2>Slide 17 — Thank You / Resources</h2>
  <div class="seapavaa-grid">
    <div class="seapavaa-card">
      <span class="seapavaa-role">Seen in the talk</span>
      <h3>Public repository QR</h3>
      <a href="{{ '/images_kebab/seapavaa2026/custom_machine_learning_for_film_restoration_qr.png' | relative_url }}" target="_blank">
        <img src="{{ '/images_kebab/seapavaa2026/custom_machine_learning_for_film_restoration_qr.png' | relative_url }}" alt="Public repository QR code">
      </a>
      <div class="seapavaa-filelist">
        <a href="https://github.com/fabiocolor/custom-machine-learning-for-film-restoration" target="_blank">Open repository</a>
      </div>
    </div>
  </div>
</section>
