---
layout: default
title: Research Evidence
nav_order: 10
has_children: true
---

# Research Evidence

This folder collects method notes and decision trails that explain **why** certain CopyCat recovery strategies work and where their limits are. These pages are written for practitioners who need reusable patterns, not just case-by-case results.

## Purpose

The [Case Studies]({% link case-studies.md %}) document real projects with their specific contexts and results. This folder extracts the **method patterns** from those cases:
- What assumptions does a method rely on?
- When should you use it versus something else?
- What has failed in practice, and why?
- What stop rules help you decide to accept or reject a result?

## Available trails

- **[CopyCat Chroma Recovery Method]({% link research-evidence/COPYCAT_CHROMA_METHOD_TRAIL.md %})** — The reference-trained chroma recovery pattern: Y from source, CbCr from reference, alignment requirements, shot vs. sequence models, highlight management, and reference quality thresholds.

- **[Candy Candy Chroma Recovery Trail]({% link research-evidence/CANDY_CANDY_CHROMA_COPYCAT.md %})** — A worked example showing how the method was applied to a severely faded 16mm print with a PAL DVD reference. Documents key decisions, what worked, what failed, and lessons for reuse.

## How to use these trails

**When planning a new CopyCat recovery:**
1. Read the relevant method trail first to understand the pattern
2. Check whether your source and reference meet the documented requirements
3. Look at the worked example (e.g., Candy Candy) to see the method in action
4. Note the documented failure modes and stop rules
5. Adapt the method to your material while tracking your own decisions

**When reviewing results:**
- Compare your results against the documented success criteria
- If you encounter problems, check whether they match documented failure modes
- Record your own decisions and outcomes to build institutional knowledge

## What makes a good decision trail

A decision trail should teach **judgment**, not just procedures. Good trails explain:
- **Input requirements:** What quality of source and reference is needed?
- **Key decisions:** Why was one approach chosen over another?
- **What worked:** Which strategies succeeded and why?
- **What failed:** Which strategies were tried and rejected, and why?
- **Limitations:** Where does the method break down?
- **Stop rules:** How do you decide to accept, reject, or iterate?

## Contributing evidence

This is a public research site. If you use these methods and want to share your results:
- Open a GitHub Discussion with your findings
- Describe your source material, reference type, and key decisions
- Note what worked, what failed, and any adaptations you made
- Share comparisons if you can (respecting copyright and archive policies)

Your evidence helps improve the documented patterns and teaches others.

---

*See also: [Case Studies]({% link case-studies.md %}) | [CopyCat Workflow]({% link copycat-workflow.md %}) | [How to Use These Docs]({% link HOW_TO_USE_RESEARCH_DOCS.md %})*
