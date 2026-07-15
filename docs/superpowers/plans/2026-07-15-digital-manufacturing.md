# Digital Manufacturing Section Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand the bilingual website with a public-safe ERP+MES+TPM digital manufacturing story supported by the June 2026 case materials.

**Architecture:** Keep `build-pages.py` as the single source of truth. Upgrade the homepage summary and add one self-contained digital manufacturing section to `page_manufacturing()`, then style it in `css/site.css` and regenerate all static pages.

**Tech Stack:** Python static-page generator, semantic HTML, CSS, browser responsive verification.

## Global Constraints

- Do not expose internal work-order numbers, product codes, user accounts, or dashboard screenshots.
- Show only stable facts: 63 TPM-managed devices and quality traceability reduced from hours to minutes.
- Do not present forecast percentages or dynamic monthly KPI snapshots as achieved results.
- Do not add JavaScript, backend APIs, or third-party dependencies.
- Keep Chinese and English meaning aligned.

---

### Task 1: Upgrade bilingual digital-manufacturing content

**Files:**
- Modify: `build-pages.py`

**Interfaces:**
- Consumes: existing `home.mes_*` values and the local `page` dictionary in `page_manufacturing()`.
- Produces: homepage ERP+MES+TPM summary plus `digital_*` values consumed by the manufacturing-page renderer.

- [ ] **Step 1: Confirm new content is absent**

```powershell
rg -n "ERP 管计划|63 台设备|hours to minutes|digital_systems" build-pages.py
```

Expected: no digital manufacturing content model exists.

- [ ] **Step 2: Upgrade homepage content**

```python
"mes_title": "ERP、MES 与 TPM 协同，\n让制造过程透明可追溯",
"mes_items": [
    ("01", "计划与执行协同", "ERP 工单与 MES 生产执行衔接。"),
    ("02", "扫码过站与自动采集", "记录工序流转并采集关键设备数据。"),
    ("03", "质量与物料闭环", "连接检验、缺陷、返工、批次和上料防错。"),
    ("04", "设备全生命周期管理", "TPM 覆盖台账、报修、保养和维修任务。"),
],
```

Add equivalent English copy and change the system label to `ERP · MES · TPM · TRACEABILITY`.

- [ ] **Step 3: Add manufacturing-page content model**

Define bilingual fields for `digital_kicker`, `digital_title`, `digital_body`, three system stages, six capability items, and two stable outcome facts.

- [ ] **Step 4: Verify the source model**

```powershell
rg -n "ERP 管计划|63 台设备|hours to minutes|digital_systems" build-pages.py
```

Expected: both language variants and public outcome facts are present.

### Task 2: Render and style the digital manufacturing section

**Files:**
- Modify: `build-pages.py`
- Modify: `css/site.css`

**Interfaces:**
- Consumes: Task 1 `digital_*` fields.
- Produces: `.digital-manufacturing`, `.digital-system-flow`, `.digital-capabilities`, and `.digital-outcomes` markup and styles.

- [ ] **Step 1: Render the section before test and quality**

```html
<section class="digital-manufacturing">
  <div class="container digital-intro">...</div>
  <div class="container digital-system-flow">...</div>
  <div class="container digital-detail-grid">...</div>
</section>
```

- [ ] **Step 2: Render the three-system flow**

Use semantic ordered-list items for ERP, MES and TPM, each with role and description. Use a separate capability list for scan stations, automatic collection/reporting, smart-shelf material controls, quality closure, traceability and preventive maintenance.

- [ ] **Step 3: Render stable outcomes**

```html
<div class="digital-outcome"><strong>63</strong><span>台设备纳入 TPM</span></div>
<div class="digital-outcome"><strong>分钟级</strong><span>质量异常追溯定位</span></div>
```

Use equivalent English labels without adding unsupported numeric claims.

- [ ] **Step 4: Add desktop and responsive CSS**

```css
.digital-system-flow { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); }
.digital-detail-grid { display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(320px, .9fr); }
@media (max-width: 960px) { .digital-system-flow, .digital-detail-grid { grid-template-columns: 1fr; } }
```

At 600px, reduce type sizes and make capability and outcome grids single-column where needed.

- [ ] **Step 5: Regenerate static pages**

```powershell
python build-pages.py
```

Expected: all eight static pages are regenerated.

### Task 3: Verify and publish

**Files:**
- Test: `build-pages.py`
- Test: `zh/index.html`, `en/index.html`, `zh/manufacturing.html`, `en/manufacturing.html`

**Interfaces:**
- Consumes: generated site.
- Produces: verified commits on `origin/main`.

- [ ] **Step 1: Run generator and structural verification**

```powershell
python -m py_compile build-pages.py
python build-pages.py
git diff --check
```

Expected: exit code 0; every page has one H1 and one main landmark.

- [ ] **Step 2: Check public-content boundaries**

```powershell
rg -n "20%|30%|50%|70%|MTTR|工单号|产品编码" zh en
```

Expected: no newly exposed forecast percentages, dynamic KPIs, internal work-order numbers or product codes.

- [ ] **Step 3: Browser verification**

Check Chinese and English home/manufacturing pages at 1280px desktop and 390px mobile. Expected: digital section present, no horizontal overflow, no broken images and no console errors.

- [ ] **Step 4: Commit and push**

```powershell
git add -- build-pages.py css/site.css zh en docs/superpowers/plans/2026-07-15-digital-manufacturing.md
git commit -m "Expand ERP MES TPM digital manufacturing content"
git push origin main
```

Expected: `origin/main` contains both the design-spec and implementation commits.
