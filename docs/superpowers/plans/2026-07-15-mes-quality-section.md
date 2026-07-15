# MES Quality Section Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reposition Lihua around high-quality electronics and add bilingual MES process-control content to the homepage and manufacturing page.

**Architecture:** Keep `build-pages.py` as the single source of truth for bilingual copy and generated HTML. Add one reusable visual section to the homepage, extend the manufacturing quality section, then regenerate all eight static pages and verify their structure and responsive rendering.

**Tech Stack:** Python static-page generator, semantic HTML, CSS, browser-based responsive verification.

## Global Constraints

- Use “高质量电子产品 / high-quality electronics” for company positioning.
- Preserve “复杂装配 / complex assemblies” where it describes manufacturing difficulty.
- Do not claim unconfirmed dashboards, automatic alarms, customer portals, or named MES software.
- Do not add JavaScript, backend APIs, or third-party dependencies.
- Maintain one H1 and one main landmark per page.

---

### Task 1: Bilingual positioning and MES content model

**Files:**
- Modify: `build-pages.py`

**Interfaces:**
- Consumes: existing `I18N["zh"]["home"]` and `I18N["en"]["home"]` dictionaries.
- Produces: `mes_kicker`, `mes_title`, `mes_body`, and `mes_items` values consumed by `page_home()`; manufacturing MES copy consumed by `page_manufacturing()`.

- [ ] **Step 1: Add a source-content assertion that initially fails**

```powershell
rg -n "高质量电子产品|high-quality electronics|mes_title|MES PROCESS CONTROL" build-pages.py
```

Expected before implementation: no MES content keys and old positioning copy remains.

- [ ] **Step 2: Replace positioning copy and add bilingual MES fields**

```python
"hero_title": "高质量电子产品的\n一站式制造伙伴",
"mes_kicker": "DIGITAL PROCESS CONTROL",
"mes_title": "MES 连接每一道工序，\n让质量过程可追溯",
"mes_items": [
    ("01", "工单与物料", "关联生产任务、BOM 与物料批次。"),
    ("02", "工序执行", "记录关键工序的人员、设备与时间。"),
    ("03", "检验与测试", "汇集制程检验、测试结果与不良信息。"),
    ("04", "追溯与闭环", "建立生产履历并记录异常处置与改进。"),
],
```

Add equivalent English copy using “MES connects each production step” and “high-quality electronics.”

- [ ] **Step 3: Verify source content**

```powershell
rg -n "高质量电子产品|high-quality electronics|mes_title|MES connects" build-pages.py
```

Expected: Chinese and English positioning plus MES fields are present.

### Task 2: Homepage and manufacturing MES presentation

**Files:**
- Modify: `build-pages.py`
- Modify: `css/site.css`

**Interfaces:**
- Consumes: Task 1 MES dictionaries.
- Produces: `.home-mes`, `.mes-flow`, `.mes-flow-item`, and manufacturing MES markup styled at desktop and mobile breakpoints.

- [ ] **Step 1: Render the homepage MES section**

```html
<section class="home-mes">
  <div class="container home-mes-grid">
    <div class="home-mes-copy">...</div>
    <ol class="mes-flow">...</ol>
  </div>
</section>
```

Place it between the manufacturing capability overview and the existing quality section.

- [ ] **Step 2: Extend manufacturing quality copy with MES controls**

```html
<div class="manufacturing-mes">
  <span class="eyebrow mono">MES PROCESS CONTROL</span>
  <p>...</p>
  <ul><li>生产任务</li><li>工序记录</li><li>质量数据</li><li>批次追溯</li></ul>
</div>
```

- [ ] **Step 3: Add responsive styling**

```css
.home-mes-grid { display: grid; grid-template-columns: minmax(0, .8fr) minmax(0, 1.2fr); }
.mes-flow { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); }
@media (max-width: 960px) { .home-mes-grid { grid-template-columns: 1fr; } }
@media (max-width: 600px) { .mes-flow { grid-template-columns: 1fr; } }
```

- [ ] **Step 4: Regenerate static pages**

```powershell
python build-pages.py
```

Expected: all eight files under `zh/` and `en/` are rewritten successfully.

### Task 3: Validation and publication

**Files:**
- Test: `build-pages.py`
- Test: `zh/index.html`, `en/index.html`, `zh/manufacturing.html`, `en/manufacturing.html`

**Interfaces:**
- Consumes: generated static site.
- Produces: a verified Git commit pushed to `origin/main`.

- [ ] **Step 1: Run generator and repository checks**

```powershell
python -m py_compile build-pages.py
python build-pages.py
git diff --check
```

Expected: exit code 0 for every command.

- [ ] **Step 2: Verify content and landmarks**

```powershell
rg -n "高质量电子产品|high-quality electronics|MES" zh en
```

Expected: bilingual MES sections exist; every generated page has one H1 and one main.

- [ ] **Step 3: Verify desktop and 390px mobile rendering**

Run the local HTTP server and inspect the Chinese and English home/manufacturing pages. Expected: no horizontal overflow, no broken images, and no browser console errors.

- [ ] **Step 4: Commit and push**

```powershell
git add -- build-pages.py css/site.css zh en docs/superpowers/plans/2026-07-15-mes-quality-section.md
git commit -m "Add MES process control section"
git push origin main
```

Expected: `origin/main` contains the MES section commit.
