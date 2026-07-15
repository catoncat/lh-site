# Digital Manufacturing Visual Alignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Align the homepage and manufacturing-page ERP+MES+TPM sections with the site's editorial industrial design while preserving all approved bilingual content and facts.

**Architecture:** Keep `build-pages.py` as the single bilingual content and markup generator. Replace card-oriented markup with shared flow, divided-list, and metric-strip structures, then update `css/site.css` at the existing homepage, manufacturing, and responsive blocks. Add a standard-library regression test that regenerates pages and inspects the emitted HTML/CSS contract.

**Tech Stack:** Python 3 static generator, HTML5, CSS3, Python `unittest`.

## Global Constraints

- Do not add JavaScript, images, packages, or third-party dependencies.
- Preserve the approved Chinese and English ERP, MES, TPM copy and public facts.
- Preserve semantic ordered lists, heading order, one `main`, and one `h1` per generated page.
- At 390px width, the sections must have no horizontal overflow and no fixed card heights.

---

### Task 1: Establish the visual-alignment regression contract

**Files:**
- Create: `tests/test_digital_visual_alignment.py`

**Interfaces:**
- Consumes: generated `zh/index.html`, `en/index.html`, `zh/manufacturing.html`, `en/manufacturing.html`, and `css/site.css`.
- Produces: `python -m unittest tests.test_digital_visual_alignment` as the repeatable structural check.

- [ ] **Step 1: Write the failing tests**

Create a `unittest.TestCase` whose `setUpClass` runs `build-pages.py`, then assert:

```python
for language in ("zh", "en"):
    home = read(f"{language}/index.html")
    manufacturing = read(f"{language}/manufacturing.html")
    self.assertIn('class="mes-system-rail"', home)
    self.assertIn('class="digital-outcome-strip"', manufacturing)
    self.assertNotIn('class="digital-outcomes"', manufacturing)
    self.assertEqual(home.count("<main"), 1)
    self.assertEqual(manufacturing.count("<h1"), 1)

self.assertNotIn("min-height: 250px", homepage_mes_css)
self.assertNotIn("background: rgba(255,255,255,0.42)", digital_css)
```

- [ ] **Step 2: Run the tests and verify RED**

Run: `python -m unittest tests.test_digital_visual_alignment -v`

Expected: FAIL because `mes-system-rail` and `digital-outcome-strip` do not exist and the old card classes/styles remain.

- [ ] **Step 3: Commit the regression contract with the implementation after it turns green**

The test and implementation form one behavior change and will be committed together after Task 3 verification.

### Task 2: Replace card-oriented generated markup

**Files:**
- Modify: `build-pages.py`

**Interfaces:**
- Consumes: existing `mes_items`, `digital_systems`, `digital_capabilities`, and `digital_outcomes` bilingual data.
- Produces: `.mes-system-rail`, `.mes-flow`, `.digital-system-flow`, `.digital-capabilities`, and `.digital-outcome-strip` structures.

- [ ] **Step 1: Add the homepage system rail**

Insert this semantic relationship before the homepage capability list:

```html
<p class="mes-system-rail mono"><span>ERP</span><i aria-hidden="true">→</i><span>MES</span><i aria-hidden="true">→</i><span>TPM</span></p>
```

Keep the four approved capability items in `ol.mes-flow`, but change each item to a compact row with a number column and a copy column.

- [ ] **Step 2: Simplify the manufacturing system flow**

Keep `ol.digital-system-flow` and its three items. Render each item as number, system name, role, and description without card-specific wrappers; move `digital_note` into a paragraph directly below the flow.

- [ ] **Step 3: Replace the results sidebar with a metric strip**

Render scenarios as a semantic list and replace the aside with:

```html
<div class="digital-outcome-strip" aria-label="PUBLIC OUTCOMES">
  <span class="eyebrow mono">PUBLIC OUTCOMES</span>
  <div class="digital-outcome">...</div>
  <div class="digital-outcome">...</div>
</div>
```

### Task 3: Align styles and responsive behavior

**Files:**
- Modify: `css/site.css`
- Test: `tests/test_digital_visual_alignment.py`

**Interfaces:**
- Consumes: markup classes produced by Task 2.
- Produces: two-column desktop sections, single-column mobile sections, continuous rails, divider lists, and a horizontal result strip.

- [ ] **Step 1: Restyle the homepage**

Remove sticky positioning and card minimum heights/backgrounds. Style `.mes-system-rail` as a compact inline flow and `.mes-flow-item` as a grid row with only a bottom divider. Keep the existing two-column `.home-mes-grid` at desktop and switch to one column at 800px.

- [ ] **Step 2: Restyle the manufacturing section**

Use one continuous bordered `.digital-system-flow`; use dividers rather than backgrounds for its items. Make `.digital-capabilities` a two-column list separated by row/column rules. Make `.digital-outcome-strip` span the container in a three-column layout: label plus two metrics.

- [ ] **Step 3: Add responsive rules**

At 960px, stack intro and result strip where needed. At 520px, use one-column scenario rows, reduce padding and type sizes, remove all digital-section minimum heights, and preserve full-width content without overflow.

- [ ] **Step 4: Regenerate and verify GREEN**

Run:

```powershell
python build-pages.py
python -m unittest tests.test_digital_visual_alignment -v
```

Expected: generator exits 0 and all tests pass.

### Task 4: Browser verification and publication

**Files:**
- Verify: `zh/index.html`, `en/index.html`, `zh/manufacturing.html`, `en/manufacturing.html`

**Interfaces:**
- Consumes: generated site from Tasks 2 and 3.
- Produces: verified desktop/mobile pages and a pushed `main` commit.

- [ ] **Step 1: Inspect desktop and mobile rendering**

Serve the repository locally and inspect both target sections at 1280×720 and 390×844. Confirm no horizontal overflow, no card-grid appearance, consistent heading hierarchy, and readable Chinese/English wrapping.

- [ ] **Step 2: Measure the manufacturing digital section**

Use the browser DOM to verify the section contains no `.digital-outcomes` element, has exactly three system steps and six scenario rows, and is materially shorter than the previous 3047px mobile baseline.

- [ ] **Step 3: Run final repository checks**

Run:

```powershell
python build-pages.py
python -m unittest discover -s tests -v
git diff --check
git status --short
```

Expected: generator and tests exit 0, `git diff --check` is empty, and only intended source/generated/test/plan files are changed.

- [ ] **Step 4: Commit and push**

```powershell
git add -- build-pages.py css/site.css zh en tests docs/superpowers/plans/2026-07-15-digital-manufacturing-visual-alignment.md
git commit -m "Align digital manufacturing sections"
git push origin main
```
