---
name: create-study-materials
description: Create explanatory, visually structured study guides, lessons, and printable handbooks for learning a concept or practical skill, including synthesis of supplied references. Use for substantial learning materials rather than isolated factual answers.
---

# Create study materials

Create material a learner can study independently, reason with, and apply. Treat the following as this user's defaults; explicit instructions for the current task take precedence. This file is a portable instruction document. For an installed Codex skill, its entrypoint must be named `SKILL.md` inside a skill folder; attaching this file to a chat also works as an explicit instruction source.

## Learner and scope

- Assume an analytical, visually oriented learner with general engineering literacy but no background in the requested subject. Adapt to a different audience when specified.
- Establish the target capability: what the learner should be able to explain, calculate, build, diagnose, evaluate, or perform. Infer it from the conversation where possible.
- Identify prerequisite knowledge, supplied references, preferred deliverables, and practical constraints. Ask only for missing information that materially changes the work; proceed with stated assumptions otherwise.
- Match the requested scale. A single lesson remains a lesson; a handbook develops the full prerequisite-to-application path. Let required explanations determine length. A page count or a multiple of an earlier word count is not a substitute for depth.
- For a complete handbook, default to a printable PDF plus editable source when tools permit. For shorter lessons, follow the requested medium. Publish or deploy only when requested; a local document request does not imply a website deployment.

## 1. Map the learning path

Create a dependency-based outline before drafting. Introduce concepts before relying on them. Group chapters around meaningful capabilities, rather than copying the order of a bibliography.

Prepare a visual concept map showing how the subject's major ideas relate. Distinguish prerequisite, part-of, causal, and comparison relationships; label edges when their meaning would otherwise be ambiguous.

For each main chapter, identify its prerequisites, learning outcomes, central mechanisms, useful visuals, and an application that demonstrates understanding. Connect advanced material back to earlier foundations. Choose the number of chapters for the topic; no fixed chapter count is required.

**Completion criterion:** every target capability has a place in the outline, and every prerequisite is either taught earlier or explicitly assumed.

## 2. Review and account for references

When the user supplies references:

1. Extract each individual link and document title. Keep a record of every original entry, while deduplicating retrieval work. Distinguish an individual paper from an entire course or documentation collection.
2. Open the sources. Read the relevant text, equations, figures, tables, and captions; inspect PDF pages where layout or visual evidence matters. If full-document reading is requested, track that separately from targeted section review.
3. Record an honest access status: full text reviewed, specified sections reviewed, abstract only, inaccessible, or replaced by an identified alternate edition or author-hosted copy. A successful URL fetch alone does not establish that the source was read.
4. For each substantive source, extract the problem, central claim, reasoning or mechanism, supporting evidence, assumptions, alternatives, strengths, limitations, and practical implications. Mark dimensions that genuinely do not apply. For a specification, emphasize behavior, invariants, constraints, and interoperability rather than inventing an experimental hypothesis.
5. Map every source to the teaching section that uses it. Include a coverage table or annotated reference map so the learner can trace the synthesis. Group related sources in the narrative while preserving their distinct contributions in the source notes.

Prefer primary sources. Verify version-sensitive facts, current standards, and superseded editions. Distinguish a proposal, historical implementation, current specification, and deployed behavior. When sources disagree, explain the differing models, versions, workloads, measurements, or assumptions.

If an original is inaccessible, try a legitimate primary-source alternative, document the limitation, and continue supported work. Attribute abstract-level findings as such. Never claim complete source coverage or full-paper review when only summaries or selected sections were accessible.

Write original teaching prose and diagrams with citations near the claims they support. Use brief permitted quotations or attributed excerpts only when they improve learning. A self-contained explanation does not require reproducing entire copyrighted documents.

**Completion criterion:** every supplied entry has a coverage/access disposition, and consequential claims have adequate support or are clearly labeled as illustrative reasoning or uncertainty.

## 3. Teach mechanisms and argumentation

Write connected explanatory prose. Introduce a concrete problem, then show why the mechanism or method is needed. Define new terms, symbols, and units at first use.

Develop each important idea through the following questions where applicable:

- What problem does it solve, and what would happen without it?
- What parts, representations, states, or rules does it use?
- What happens step by step in a concrete example?
- Why does the conclusion follow from the premises or mechanism?
- Under which assumptions does it work? What evidence supports it?
- What are the competing approaches and their tradeoffs?
- How does it fail, and what observation would expose that failure?
- Where is it useful, and what changes when the assumptions change?

Make the distinction between description and explanation visible. Naming an algorithm's phases is insufficient: walk through how its state changes and why each change matters. Stating that an approach is faster is insufficient: identify the workload, comparison, metric, and limitations.

Use analogies as an entry point, then map them to the actual mechanism and explain where they break down. Keep historical context when it explains a design choice. Separate evidence, hypothesis, proof, and teaching example.

For a handbook, give each main chapter substantial explanation, a worked application, relevant failure cases, practice, and answers. Add a glossary and navigable terminology references when the subject introduces many new terms. End with an integrated application or capstone connecting the major concepts.

**Completion criterion:** a learner can reconstruct the central reasoning and work through an example using the material provided, without needing the originals to fill basic explanatory gaps. Advanced proofs or specialist details outside the chosen scope should be identified honestly.

## 4. Use visuals as teaching tools

Select visuals by the reasoning task:

| Learning task | Useful visual |
| --- | --- |
| Understand structure and dependencies | Concept map, hierarchy, architecture diagram |
| Follow an interaction over time | Sequence diagram or timeline |
| Understand representation | Labeled field layout, memory layout, syntax tree, annotated example |
| Follow state and decisions | State machine or decision diagram |
| Compare behavior and tradeoffs | Comparison table, graph, controlled before/after example |
| Learn a procedure or physical skill | Annotated stages, positions, checkpoints, observed outcomes |
| Understand quantitative behavior | Plot with units, assumptions, and interpretable scales |

Place each visual beside the explanation it supports. Explain how to read it and use it in a worked example. Make labels legible at printed size. Prefer vector diagrams for technical layouts and structures; use raster illustrations when their visual qualities materially help.

Visual accuracy matters as much as prose accuracy:

- Label units, field widths, coordinate axes, directions, states, and boundaries where relevant.
- Distinguish an illustrative schematic from measured data or a proportionally accurate layout.
- Use arrows for a defined relationship. Alternative branches should not look like sequential steps.
- Show separate actors or scopes clearly. A sequence diagram's time direction and message direction must be unambiguous.
- Keep numbers, names, and assumptions consistent between figure, caption, and worked example.
- Show important constraints rather than visually implying they disappear. For example, independent network streams can progress separately, while later bytes in a stream with a missing range still wait.

Use domain-specific visuals when applicable: packet headers and exchanges for networking; stack, heap, dataflow, and execution traces for programming; geometric interpretations and graphs for mathematics. Do not force one domain's diagram vocabulary onto another.

### Visual style and color palette

Use this palette consistently across the cover, page furniture, diagrams, tables, and companion learning materials:

| Color | Role |
| --- | --- |
| `#001524` | Primary ink: body text, major titles, labels, and strong outlines |
| `#15616D` | Structural accent: section headings, links, diagram connectors, and table headers |
| `#FFECD1` | Light surface: example panels, selected diagram fields, and restrained callout backgrounds |
| `#FF7D00` | Highlight: active steps, focal points, and important changes |
| `#78290F` | Secondary emphasis: limitations, failure paths, and caution callouts |

Keep ordinary page backgrounds white to conserve ink. Use cream for localized panels rather than full-page fills. Use navy text on cream or orange surfaces; avoid orange as small body text on white and avoid white text on orange. Check contrast at actual output size, including figure labels. Use light tints of teal for note lines and secondary rules. Keep the palette restrained and supplement color with labels, shapes, line styles, or symbols so grayscale printing remains understandable.

## 5. Build practice that reveals understanding

Include worked examples with intermediate steps and reasoning, followed by exercises the learner can attempt independently. Provide explained solutions after the exercises or in a clearly linked answer section.

Balance recall with prediction, calculation, diagnosis, implementation, and design judgment. Include a changed-assumption or counterexample exercise where it helps expose shallow understanding. For practical skills, specify observable success criteria and common mistakes.

For labs, state prerequisites, inputs, steps, expected observations, interpretation, and recovery or cleanup when needed. Distinguish examples from actions actually executed. Verify runnable examples in an appropriate environment when available, and clearly identify anything not run. Constructing a lab does not authorize changes to the learner's live systems.

**Completion criterion:** the exercises test the stated learning outcomes, and the solutions explain why the answers follow rather than merely giving final values.

## 6. Format printable handbooks for an A4 punch-hole binder

Apply these defaults when producing a printable handbook; user-specified dimensions override them:

- A4 portrait; print at actual size, double-sided, flipping on the long edge.
- **20 mm total inside margin and 18 mm outside margin.** These are total page margins, not an additional 20 mm added to an existing margin.
- Mirror the inside margin: left on odd physical PDF pages, right on even physical PDF pages. Apply it to prose, tables, diagrams, note lines, headers, and footers.
- Create a dedicated cover on physical page 1 and leave page 2 completely blank, including headers and footers.
- Put a redesigned, clickable table of contents on one page, normally page 3, with a completely blank reverse. Group entries by learning stage, align page numbers, and use readable leaders or spacing. For a very large book, show major chapters or parts on this page and expose deeper headings through PDF bookmarks rather than shrinking type excessively.
- Keep printed page numbers consistent with physical PDF page numbers so parity and printing remain predictable. Recalculate contents links and page references after every reflow.
- Start every main chapter at the top of a new odd-numbered page.
- Fill usable space remaining after a chapter with lightly ruled notes and sketches space. If an intervening even page is needed before the next chapter, use it for notes too. This replaces a fixed half-page notes quota; do not reserve notes space on every content page.
- Use comfortably readable body text, sharp diagrams, restrained print-friendly color, and clear heading hierarchy. Keep headings with their following content and figures with their captions. Use outer-edge page numbers on facing pages.

Cover and contents blank backs are intentional exceptions to the notes-space rule. Preserve the chapter content when applying a formatting-only revision.

Use available document/PDF authoring guidance for the actual output format. If PDF creation is unavailable, provide the editable material and disclose the limitation instead of claiming a finished printable artifact.

### Manual-duplex exports for a single-sided printer

After finalizing the complete PDF, also deliver two print-only PDFs derived from its final physical page order:

1. `<report>-even-descending.pdf`: all even physical pages, largest page number first. Print this file first.
2. `<report>-odd-descending.pdf`: all odd physical pages, largest page number first. Reload the printed stack and print this file second.

Keep the complete PDF in normal reading order as the primary export. Split by physical PDF page index (one-based), not chapter numbers or PDF page-label metadata. Preserve the original printed page numbers, page sizes, rotation, mirrored margins, and every intentional blank page; do not reflow or renumber the split files.

Both passes must contain the same number of sheets. If the complete report has an odd page count, add a synthetic blank final even back to the print set only; keep the complete PDF unchanged. For a five-page report, the even pass is `[blank page 6, 4, 2]` and the odd pass is `[5, 3, 1]`. For six pages, the passes are `[6, 4, 2]` and `[5, 3, 1]`. Original blank pages, including the backs of the cover and contents, remain in their positions.

For an installed skill package, use `scripts/export_manual_duplex.py` (requires `pypdf`) to generate both files and a page-order manifest:

```bash
python scripts/export_manual_duplex.py /path/to/report.pdf --output-dir /path/to/exports
```

If this portable instruction file is used without its helper script, implement the same page-selection rules with an available PDF library and verify the result.

Include print directions with the exports: A4, actual size, one PDF page per sheet, single-sided mode for each pass, all pages, and no additional odd/even filtering or reverse-order setting. Disable blank-page skipping. Preserve the stack's pairing order between passes: the sheet carrying the highest even page must receive the highest odd page on its reverse. Give a four-page trial instruction to determine the printer's output-stack order, which face to reload, and feed-edge orientation before printing the book. Both exports are already descending; a PDF viewer or printer must not silently reverse them again. Do not claim that one universal tray-flipping instruction works for every printer.

Verify output page counts, exact descending source-page sequences, paired sheet counts, and any inserted blank. Provide the page-order manifest so the learner can check the pass order. Treat the split PDFs as print-only copies; the complete PDF retains the navigable reading experience.

## 7. Verify and deliver

Check the actual generated artifacts, not only the source or intended settings:

- Compare the finished material with learning outcomes and reference coverage. Check prerequisite definitions, explanatory depth, cited claims, and answer completeness.
- Verify important calculations, example bytes or states, diagram semantics, and agreement between figures and text.
- Render the PDF and inspect the cover, contents, representative dense pages, diagrams, tables, chapter transitions, and notes spaces. Inspect more pages where reflow or automated checks indicate risk. Fix clipping, overlap, unreadable labels, and orphan headings before delivery.
- Check all pages for binding-margin violations. Verify odd chapter starts, blank cover/contents backs, correct page references, functioning navigation, and that intended content survived reflow.
- Report what was actually validated and any material source-access or execution limitations. Do not describe a coverage check as a full scholarly or formal audit.

Deliver the complete PDF, both manual-duplex print PDFs, the page-order manifest, and editable source for substantial handbooks. For other requested media, deliver the corresponding artifact directly. Give a brief account of the result and the relevant print settings. Keep implementation chatter out of the learner-facing book. Preserve the original goal through revisions: improve the requested aspect without silently changing scope, deleting teaching content, or restoring superseded preferences.
