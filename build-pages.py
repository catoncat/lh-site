#!/usr/bin/env python3
"""Generate static bilingual Lihua site pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

I18N = {
    "zh": {
        "lang": "zh-CN",
        "dir": "zh",
        "other": "en",
        "other_label": "EN",
        "self_label": "中文",
        "status": "SYSTEM STATUS: OPTIMAL // EST. 1993",
        "location": "LOCATION: TAISHAN, CN [22.25N 112.79E]",
        "nav": {
            "home": "首页",
            "manufacturing": "制造能力",
            "about": "关于利华",
            "contact": "联系",
        },
        "paths": {
            "home": "./",
            "manufacturing": "./manufacturing.html",
            "about": "./about.html",
            "contact": "./contact.html",
        },
        "other_paths": {
            "home": "../en/",
            "manufacturing": "../en/manufacturing.html",
            "about": "../en/about.html",
            "contact": "../en/contact.html",
        },
        "footer": {
            "tagline": "电子制造服务 · EMS",
            "copy": "© 1993-2026 台山市利华电子厂有限公司",
            "contact": "联系",
            "social": "社交",
            "legal": "合规",
            "phone": "T: +86 750 5625181",
            "email": "E: raylee@ts-lihua.com / jared.lee@ts-lihua.com",
            "social_lines": "WECHAT",
            "legal_lines": "ISO 9001 / IATF 16949 / IPC",
            "end": "END OF DOCUMENT // TRANSMISSION SECURE",
        },
        "home": {
            "title": "利华电子 | 工业精密制造",
            "ref": "REF: LIHUA-ELECTRONICS_V.04",
            "build": "BUILD DATE: 2026.07.13",
            "brand1": "LIHUA.",
            "brand2": "ELECTRONICS",
            "facility": "PRIMARY FACILITY",
            "hero_line": "30 年 EMS 经验：PCBA、线束与机电装配。",
            "cap_cat": "CATEGORY 01",
            "cap_title": "核心能力",
            "cap_total": "4 MODULES",
            "caps": [
                ("[ 01 ]", "PCBA<br>SMT", "锡膏印刷、高速贴片、回流；AOI / X-Ray。", False),
                ("[ 02 ]", "插件<br>组装", "成型、插装、波峰焊、手焊与过程检验。", True),
                ("[ 03 ]", "线缆<br>线束", "压接 / 焊接 / IDC；拉力与线束测试。", False),
                ("[ 04 ]", "机电<br>装配", "Box-build、整机测试、老化与定制包装。", False),
            ],
            "company_tag": "THE COMPANY",
            "company_p1": "台山市利华电子厂有限公司成立于 1993 年。30 年电子制造服务经验，服务涵盖供应链管理、生产配套与工程支持。",
            "company_p2": "客户与产品分布于航空控制、工业仪器、交通运输、医疗设备与专业音响等领域；强调数字化管理、全过程追溯与稳定质量。",
            "company_mono": "台山市利华电子厂有限公司 // SINCE 1993",
            "stats": [
                ("成立", "1993"),
                ("经验", "30Y"),
                ("车间", "7,000㎡"),
                ("厂区", "50亩"),
            ],
            "lean_left": "METHODOLOGY: LEAN MANUFACTURING",
            "lean_right": "FLOW OPTIMIZATION: ACTIVE",
            "lean_peak": "PEAK EFFICIENCY POINT",
            "lean_items": [
                ("01. PROCESS", "在合适产品/工序导入精益，提高效率与一致性。"),
                ("02. QUALITY", "IPC-A-610 Class 2/3、J-STD-001 等工艺标准落地现场。"),
                ("03. TRACE", "数字化管理与全过程追溯，缩短响应时间。"),
            ],
            "sector_cat": "MARKETS",
            "sector_title": "服务行业",
            "sectors": [
                ("01. AERO", "航空控制", "高可靠板卡与线束制造经验。"),
                ("02. INDUSTRIAL", "工业与电力", "仪器、控制与电力系统相关装配。"),
                ("03. MOBILITY", "交通与充电", "交通设备与新能源汽车充电相关 PCBA。"),
            ],
            "cta_title": "CONTACT",
            "cta_body": "项目评估、工艺能力或样品需求，直接联系工厂窗口。",
            "cta_btn": "[ 联系我们 ]",
            "offers_cat": "WHY LIHUA",
            "offers_title": "合作方式",
            "offers": [
                ("质量与交付", "稳定工艺标准，强调准时交付。"),
                ("灵活响应", "多品种、中高批量，节奏跟得上变化。"),
                ("成本效益", "为复杂产品提供可执行的性价比方案。"),
                ("长期协作", "定制化服务，做长期制造伙伴。"),
            ],
            "customers_label": "国际客户项目经验沉淀",
            "customers": "Boeing · HP · IBM · Thermo · ABB · Emerson",
            "apps_cat": "APPLICATIONS",
            "apps_title": "典型应用",
            "apps": [
                ("新能源汽车充电", "交流/直流充电相关 PCBA 与可靠制造支持。", "app-charging.jpg"),
                ("生命科学与检测", "成分/元素分析等仪器类电子装联。", "app-life.png"),
                ("工业设备", "工业控制与设备侧板卡、组件制造。", "app-industrial.png"),
                ("电力系统", "电力与能源相关电子装配场景。", "app-power2.jpg"),
            ],
            "campus_title": "厂区与现场",
            "campus_body": "厂区占地 50 亩（后备 30 亩），生产车间约 7,000 平方米。以可交付、可追溯的制造服务支撑长期合作。",
        },
        "manufacturing": {
            "title": "制造能力 | 利华电子",
            "kicker": "CATEGORY 01",
            "h1": "制造能力",
            "lead": "按工艺主路径组织：SMT、插件、线束、机电装配与测试。只放能支撑判断的事实，不堆设备清单。",
            "items": [
                {
                    "no": "[ 01 ]",
                    "name": "PCBA · SMT",
                    "desc": "锡膏印刷 → 高速贴片 → 回流 → AOI / X-Ray。支持 RoHS 或有铅、水洗或免洗。",
                    "points": ["最大板尺寸 510×510mm", "元件 0201+，间距 ≥0.25mm", "贴片产能约 350K pcs/小时"],
                },
                {
                    "no": "[ 02 ]",
                    "name": "插件组装",
                    "desc": "成型、插装、波峰焊、DI 清洗（如适用）、手焊与过程质量检查。",
                    "points": ["通孔 PCBA 主路径", "AAOI / AOI 过程检查", "与后段测试衔接"],
                },
                {
                    "no": "[ 03 ]",
                    "name": "线缆与线束",
                    "desc": "压接、焊接与 IDC；面向工业、汽车与航空类定制线束。",
                    "points": ["拉力测试 0–500kg", "Cirris 线束测试至 32,000 点", "高压 / 可靠性测试"],
                },
                {
                    "no": "[ 04 ]",
                    "name": "机电装配与测试",
                    "desc": "Box-build、ICT/FCT、老化、环境试验与定制包装。",
                    "points": ["Agilent 3070 ICT", "FCT 与固件编程", "热压焊 / 敷形涂覆 / 温循"],
                },
            ],
            "note_title": "补充能力",
            "note_body": "热压焊（FPC-Rigid）、自动敷形涂覆、激光标识、温循（-70°C~+200°C）与老化（至 +150°C）可按项目配置，不单独做成空栏目。",
        },
        "about": {
            "title": "关于利华 | 利华电子",
            "kicker": "THE COMPANY",
            "h1": "关于利华",
            "lead": "公司、厂区、质量体系与精益放在一页。只保留能对外说清的事实。",
            "blocks": [
                {
                    "tag": "01 / PROFILE",
                    "title": "公司",
                    "body": "台山市利华电子厂有限公司成立于 1993 年。30 年 EMS 经验，提供供应链管理、完整生产配套与工程支持，并服务 Boeing、HP、IBM、Thermo、ABB、Emerson 等国际客户相关项目经验所沉淀的执行标准。",
                },
                {
                    "tag": "02 / CAMPUS",
                    "title": "厂区",
                    "body": "厂区占地 50 亩（后备 30 亩），生产车间约 7,000 平方米。以稳定交付与质量一致性为运营重点。",
                },
                {
                    "tag": "03 / QUALITY",
                    "title": "质量与认证",
                    "body": "ISO 9001、ISO 14000、IATF 16949；工艺执行 IPC-A-610 Class 2/3、IPC J-STD-001、IPC/WHMA-A-620，并为 IPC 会员企业。",
                },
                {
                    "tag": "04 / LEAN",
                    "title": "精益生产",
                    "body": "在合适的产品与工序导入精益方法，目标是提高效率与产品质量，而不是增加展示性文案。",
                },
            ],
            "facts_title": "一览",
            "facts": [
                ("成立", "1993 · 台山"),
                ("车间", "约 7,000㎡"),
                ("厂区", "50 亩（+30 后备）"),
                ("认证", "ISO / IATF / IPC"),
            ],
        },
        "contact": {
            "title": "联系 | 利华电子",
            "kicker": "CONTACT CHANNEL",
            "h1": "联系利华",
            "lead": "商务与项目对接优先联系以下窗口。",
            "people": [
                {
                    "role": "CONTACT 01",
                    "name": "Ray Lee / 李炼",
                    "title": "Plant Manager / 厂长",
                    "lines": ["T: +86 750 5625181", "E: raylee@ts-lihua.com"],
                },
                {
                    "role": "CONTACT 02",
                    "name": "Jare Lee / 李卓星",
                    "title": "General Manager / 总经理",
                    "lines": ["T: +86 135 5690 3684", "E: jared.lee@ts-lihua.com"],
                },
            ],
            "addr_title": "台山市利华电子厂有限公司",
            "addr_body": "中国广东省台山市",
            "note_title": "www.ts-lihua.com",
            "note_body": "www.ts-lihua.com",
        },
    },
    "en": {
        "lang": "en",
        "dir": "en",
        "other": "zh",
        "other_label": "中文",
        "self_label": "EN",
        "status": "SYSTEM STATUS: OPTIMAL // EST. 1993",
        "location": "LOCATION: TAISHAN, CN [22.25N 112.79E]",
        "nav": {
            "home": "Home",
            "manufacturing": "Manufacturing",
            "about": "About",
            "contact": "Contact",
        },
        "paths": {
            "home": "./",
            "manufacturing": "./manufacturing.html",
            "about": "./about.html",
            "contact": "./contact.html",
        },
        "other_paths": {
            "home": "../zh/",
            "manufacturing": "../zh/manufacturing.html",
            "about": "../zh/about.html",
            "contact": "../zh/contact.html",
        },
        "footer": {
            "tagline": "Electronics manufacturing services (EMS).",
            "copy": "© 1993-2026 Taishan City Lihua Electric Factory Ltd.",
            "contact": "CONTACT",
            "social": "SOCIAL",
            "legal": "LEGAL",
            "phone": "T: +86 750 5625181",
            "email": "E: raylee@ts-lihua.com / jared.lee@ts-lihua.com",
            "social_lines": "WECHAT",
            "legal_lines": "ISO 9001 / IATF 16949 / IPC",
            "end": "END OF DOCUMENT // TRANSMISSION SECURE",
        },
        "home": {
            "title": "LIHUA ELECTRONICS | Industrial Precision Systems",
            "ref": "REF: LIHUA-ELECTRONICS_V.04",
            "build": "BUILD DATE: 2026.07.13",
            "brand1": "LIHUA.",
            "brand2": "ELECTRONICS",
            "facility": "PRIMARY FACILITY",
            "hero_line": "30 years of EMS: PCBA, cable harness, and box-build.",
            "cap_cat": "CATEGORY 01",
            "cap_title": "Core Capabilities",
            "cap_total": "4 MODULES",
            "caps": [
                ("[ 01 ]", "PCBA<br>SMT", "Print, high-speed placement, reflow; AOI / X-Ray.", False),
                ("[ 02 ]", "THT<br>Assembly", "Forming, insertion, wave solder, hand solder, WIP QC.", True),
                ("[ 03 ]", "Cable<br>Harness", "Crimp / solder / IDC with pull and harness testing.", False),
                ("[ 04 ]", "Box<br>Build", "Electro-mechanical assembly, FCT, burn-in, packaging.", False),
            ],
            "company_tag": "THE COMPANY",
            "company_p1": "Taishan City Lihua Electric Factory Ltd. was founded in 1993. Financially stable EMS with 30 years of experience across supply chain, manufacturing and engineering support.",
            "company_p2": "Products serve aerospace controls, industrial instrumentation, transportation, medical devices and professional audio — with digitalized management and full-process traceability.",
            "company_mono": "TAISHAN CITY LIHUA ELECTRIC FACTORY LTD // SINCE 1993",
            "stats": [
                ("Founded", "1993"),
                ("EMS", "30Y"),
                ("Floor", "7,000㎡"),
                ("Campus", "50 acres"),
            ],
            "lean_left": "METHODOLOGY: LEAN MANUFACTURING",
            "lean_right": "FLOW OPTIMIZATION: ACTIVE",
            "lean_peak": "PEAK EFFICIENCY POINT",
            "lean_items": [
                ("01. PROCESS", "Lean applied where it improves efficiency and product consistency."),
                ("02. QUALITY", "IPC-A-610 Class 2/3 and J-STD-001 workmanship standards on the floor."),
                ("03. TRACE", "Digitalized management and full-process traceability for faster response."),
            ],
            "sector_cat": "MARKETS",
            "sector_title": "Industries Served",
            "sectors": [
                ("01. AERO", "Aerospace<br>Controls", "High-reliability board and harness manufacturing experience."),
                ("02. INDUSTRIAL", "Industrial<br>& Power", "Instrumentation, controls and power-system assemblies."),
                ("03. MOBILITY", "Transport<br>& Charging", "Transportation equipment and EV charging related PCBA."),
            ],
            "cta_title": "CONTACT",
            "cta_body": "For capability review, NPI or sample builds, contact the plant team.",
            "cta_btn": "[ Contact Us ]",
            "offers_cat": "WHY LIHUA",
            "offers_title": "How we work",
            "offers": [
                ("Quality & Delivery", "Consistent workmanship with on-time delivery focus."),
                ("Flexibility", "High mix, medium-to-high volume, responsive to change."),
                ("Cost effective", "Practical cost-effective builds for complex products."),
                ("Long-term partnership", "Personalized collaboration, not one-off transactions."),
            ],
            "customers_label": "Global customer experience base",
            "customers": "Boeing · HP · IBM · Thermo · ABB · Emerson",
            "apps_cat": "APPLICATIONS",
            "apps_title": "Typical applications",
            "apps": [
                ("EV charging", "AC/DC charging related PCBA and reliable build support.", "app-charging.jpg"),
                ("Life science & test", "Instrument electronics for analysis and measurement.", "app-life.png"),
                ("Industrial equipment", "Control boards and assemblies for industrial systems.", "app-industrial.png"),
                ("Power systems", "Electronics assembly for power and energy contexts.", "app-power2.jpg"),
            ],
            "campus_title": "Campus & floor",
            "campus_body": "50-acre campus with 30 acres reserve; about 7,000㎡ manufacturing space built for deliverable, traceable EMS work.",
        },
        "manufacturing": {
            "title": "Manufacturing | LIHUA ELECTRONICS",
            "kicker": "CATEGORY 01",
            "h1": "Manufacturing",
            "lead": "Organized by process path: SMT, THT, cable/harness, box-build and test. Facts that help decisions — not a brochure dump.",
            "items": [
                {
                    "no": "[ 01 ]",
                    "name": "PCBA · SMT",
                    "desc": "Print → high-speed placement → reflow → AOI / X-Ray. RoHS or leaded; clean or no-clean.",
                    "points": ["Max board 510×510mm", "0201+ , pitch ≥0.25mm", "~350K pcs/hour placement"],
                },
                {
                    "no": "[ 02 ]",
                    "name": "THT Assembly",
                    "desc": "Forming, insertion, wave solder, DI wash when needed, hand solder and WIP inspection.",
                    "points": ["Thru-hole main path", "AAOI / AOI checks", "Handoff to test"],
                },
                {
                    "no": "[ 03 ]",
                    "name": "Cable & Harness",
                    "desc": "Crimp, solder and IDC for industrial, automotive and aircraft harness work.",
                    "points": ["Pull test 0–500kg", "Cirris tester up to 32,000 points", "Hi-pot / reliability tests"],
                },
                {
                    "no": "[ 04 ]",
                    "name": "Box-Build & Test",
                    "desc": "Electro-mechanical assembly with ICT/FCT, burn-in, environmental test and custom packaging.",
                    "points": ["Agilent 3070 ICT", "FCT & firmware programming", "Hot-bar / coating / temp cycle"],
                },
            ],
            "note_title": "Also available",
            "note_body": "Hot-bar (FPC to rigid), automated conformal coating, laser marking, temperature cycle (-70°C to +200°C) and burn-in (to +150°C) are configured by project — not empty menu pages.",
        },
        "about": {
            "title": "About | LIHUA ELECTRONICS",
            "kicker": "THE COMPANY",
            "h1": "About Lihua",
            "lead": "Company, campus, quality system and lean on one page. Only facts that should be public.",
            "blocks": [
                {
                    "tag": "01 / PROFILE",
                    "title": "Company",
                    "body": "Taishan City Lihua Electric Factory Ltd., founded in 1993. 30 years of EMS with supply-chain management, full manufacturing processes and engineering support. Execution standards shaped by work with global customers including Boeing, HP, IBM, Thermo, ABB and Emerson.",
                },
                {
                    "tag": "02 / CAMPUS",
                    "title": "Campus",
                    "body": "50-acre campus with 30 acres reserve; about 7,000 square meters of manufacturing space focused on stable delivery and consistent quality.",
                },
                {
                    "tag": "03 / QUALITY",
                    "title": "Quality & Certifications",
                    "body": "ISO 9001, ISO 14000, IATF 16949; workmanship to IPC-A-610 Class 2/3, IPC J-STD-001 and IPC/WHMA-A-620. IPC member company.",
                },
                {
                    "tag": "04 / LEAN",
                    "title": "Lean Manufacturing",
                    "body": "Lean is applied on appropriate product/process paths to improve efficiency and quality — not as decorative copy.",
                },
            ],
            "facts_title": "At a glance",
            "facts": [
                ("Founded", "1993 · Taishan"),
                ("Floor", "~7,000㎡"),
                ("Campus", "50 acres (+30 reserve)"),
                ("Systems", "ISO / IATF / IPC"),
            ],
        },
        "contact": {
            "title": "Contact | LIHUA ELECTRONICS",
            "kicker": "CONTACT CHANNEL",
            "h1": "Contact",
            "lead": "For commercial and project coordination, start with the windows below.",
            "people": [
                {
                    "role": "CONTACT 01",
                    "name": "Ray Lee",
                    "title": "Plant Manager",
                    "lines": ["T: +86 750 5625181", "E: raylee@ts-lihua.com"],
                },
                {
                    "role": "CONTACT 02",
                    "name": "Jare Lee",
                    "title": "General Manager",
                    "lines": ["T: +86 135 5690 3684", "E: jared.lee@ts-lihua.com"],
                },
            ],
            "addr_title": "Taishan City Lihua Electric Factory Ltd.",
            "addr_body": "Taishan, Guangdong, China",
            "note_title": "www.ts-lihua.com",
            "note_body": "www.ts-lihua.com",
        },
    },
}


def nav(t, active: str) -> str:
    links = []
    for key in ("home", "manufacturing", "about", "contact"):
        current = ' aria-current="page"' if key == active else ""
        links.append(f'<a href="{t["paths"][key]}"{current}>{t["nav"][key]}</a>')
    other_href = t["other_paths"][active]
    return f"""
<nav class="site-nav">
  <div class="mono nav-status">{t["status"]}</div>
  <div class="nav-links">
    {''.join(links)}
  </div>
  <div class="nav-end">
    <div class="mono">{t["location"]}</div>
    <div class="lang-switch">
      <a href="{t["paths"][active]}" aria-current="true" data-set-lang="{t["dir"]}">{t["self_label"]}</a>
      <a href="{other_href}" data-set-lang="{t["other"]}">{t["other_label"]}</a>
    </div>
  </div>
</nav>
"""


def footer(t) -> str:
    f = t["footer"]
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">LIHUA®</div>
        <p class="mono muted">{f["tagline"]}<br>{f["copy"]}</p>
      </div>
      <div>
        <span class="mono col-title">{f["contact"]}</span>
        <p class="mono">{f["phone"]}<br>{f["email"]}</p>
      </div>
      <div>
        <span class="mono col-title">{f["social"]}</span>
        <p class="mono">{f["social_lines"]}</p>
      </div>
      <div>
        <span class="mono col-title">{f["legal"]}</span>
        <p class="mono">{f["legal_lines"]}</p>
      </div>
    </div>
    <div class="divider-double"></div>
    <div class="mono footer-end">{f["end"]}</div>
  </div>
</footer>
"""


def shell(t, title: str, active: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="{t["lang"]}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="Taishan City Lihua Electronics Factory — PCBA, harness, electromechanical manufacturing." />
  <link rel="stylesheet" href="../css/site.css" />
</head>
<body>
{nav(t, active)}
{body}
{footer(t)}
<script src="../js/site.js"></script>
</body>
</html>
"""



def page_home(t):
    h = t["home"]
    cards = []
    for idx, (no, name, desc, featured) in enumerate(h["caps"]):
        cls = "service-card featured" if featured else "service-card"
        cards.append(
            f'<div class="{cls}"><span class="mono">{no}</span><div><h3>{name}</h3><p class="mono">{desc}</p></div></div>'
        )
    stats = []
    for idx, (label, value) in enumerate(h["stats"]):
        blue = " blue" if idx == 1 else ""
        stats.append(
            f'<div class="stat-item"><span class="mono">{label}</span><span class="value{blue}">{value}</span></div>'
        )
    lean = []
    for no, text in h["lean_items"]:
        lean.append(
            f'<div><span class="mono accent-label">{no}</span><p>{text}</p></div>'
        )
    offers = []
    for idx, (title, desc) in enumerate(h.get("offers", []), 1):
        offers.append(
            f'<div class="offer-card"><span class="mono">[ 0{idx} ]</span><h3>{title}</h3><p>{desc}</p></div>'
        )
    apps = []
    for idx, (title, desc, img) in enumerate(h.get("apps", []), 1):
        apps.append(
            "<article class=\"app-card\">"
            f"<div class=\"app-photo\"><img src=\"../assets/{img}\" alt=\"{title}\" /></div>"
            "<div class=\"app-copy\">"
            f"<span class=\"mono\">0{idx}</span>"
            f"<h3>{title}</h3>"
            f"<p>{desc}</p>"
            "</div></article>"
        )
    sectors = []
    for no, title, desc in h["sectors"]:
        sectors.append(
            f'<div class="solution-col"><span class="mono">{no}</span><h3>{title}</h3><p class="mono">{desc}</p></div>'
        )
    campus_title = h.get("campus_title", "Campus")
    campus_body = h.get("campus_body", "")
    body = f"""
<div class="container">
  <header class="hero">
    <div class="hero-meta">
      <span class="mono">{h["ref"]}</span>
      <span class="mono">{h["build"]}</span>
    </div>
    <h1 class="brand-display">{h["brand1"]}</h1>
    <h1 class="brand-display accent">{h["brand2"]}</h1>
    <div class="hero-image-container hero-image-single">
      <div class="hero-overlay">
        <span class="tag">{h["facility"]}</span>
        <p class="mono">{h["hero_line"]}</p>
      </div>
      <img src="../assets/plant.jpg" alt="Lihua plant campus" />
    </div>
  </header>

  <section id="services">
    <div class="section-header">
      <div>
        <span class="mono">{h["cap_cat"]}</span>
        <h2>{h["cap_title"]}</h2>
      </div>
      <div class="mono">{h["cap_total"]}</div>
    </div>
    <div class="services-grid">
      {''.join(cards)}
    </div>
  </section>

  <section class="offers-section">
    <div class="section-header">
      <div>
        <span class="mono">{h.get("offers_cat", "WHY LIHUA")}</span>
        <h2>{h.get("offers_title", "")}</h2>
      </div>
    </div>
    <div class="offers-grid">
      {''.join(offers)}
    </div>
  </section>

  <section class="customers-bar">
    <span class="mono">{h.get("customers_label", "")}</span>
    <p class="customers-line">{h.get("customers", "")}</p>
  </section>

  <section id="about" class="about-split">
    <div class="about-text">
      <span class="tag tag-spaced">{h["company_tag"]}</span>
      <p>{h["company_p1"]}</p>
      <p>{h["company_p2"]}</p>
      <div class="divider-double"></div>
      <span class="mono">{h["company_mono"]}</span>
    </div>
    <div class="stats-grid">
      {''.join(stats)}
    </div>
  </section>
</div>

<section class="media-band">
  <div class="media"><img src="../assets/lean.jpg" alt="Factory floor" /></div>
  <div class="copy">
    <span class="mono">CAMPUS</span>
    <h3>{campus_title}</h3>
    <p>{campus_body}</p>
    <div class="chip-row">
      <span class="chip">EMS</span>
      <span class="chip">PCBA</span>
      <span class="chip">HARNESS</span>
      <span class="chip">BOX-BUILD</span>
    </div>
  </div>
</section>

<section id="lean" class="lean-section">
  <div class="container">
    <div class="hero-meta hero-meta-light">
      <span class="mono">{h["lean_left"]}</span>
      <span class="mono">{h["lean_right"]}</span>
    </div>
    <div class="lean-visualization">
      <svg class="wave-svg" viewBox="0 0 1000 200" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M0,100 C150,100 250,50 400,50 C550,50 650,150 800,150 C950,150 1000,100 1000,100" fill="none" stroke="#1A5C40" stroke-width="4"></path>
        <path d="M0,110 C150,110 250,60 400,60 C550,60 650,160 800,160 C950,160 1000,110 1000,110" fill="none" stroke="white" stroke-width="1" stroke-dasharray="5,5"></path>
        <rect x="390" y="40" width="20" height="20" fill="white"></rect>
        <text x="420" y="55" fill="white" font-family="monospace" font-size="12">{h["lean_peak"]}</text>
      </svg>
    </div>
    <div class="lean-grid">
      {''.join(lean)}
    </div>
  </div>
</section>

<div class="container">
  <section id="solutions">
    <div class="section-header">
      <div>
        <span class="mono">{h["sector_cat"]}</span>
        <h2>{h["sector_title"]}</h2>
      </div>
    </div>
    <div class="solutions-strip">
      {''.join(sectors)}
    </div>
  </section>

  <section class="apps-section">
    <div class="section-header">
      <div>
        <span class="mono">{h.get("apps_cat", "APPLICATIONS")}</span>
        <h2>{h.get("apps_title", "")}</h2>
      </div>
    </div>
    <div class="apps-grid">
      {''.join(apps)}
    </div>
  </section>

  <section class="content-block cta-block">
    <span class="mono">{h["cta_title"]}</span>
    <h3>{h["cta_body"]}</h3>
    <p><a class="text-link" href="{t["paths"]["contact"]}">{h["cta_btn"]}</a></p>
  </section>
</div>
"""
    return shell(t, h["title"], "home", body)


def page_manufacturing(t):
    m = t["manufacturing"]
    images = ["smt-line-single.png", "tht-line.jpg", "harness.png", "box-build.png"]
    blocks = []
    for i, item in enumerate(m["items"]):
        img = images[i % len(images)]
        points = "".join(f"<li>{p}</li>" for p in item["points"])
        reverse = " is-reverse" if i % 2 else ""
        blocks.append(
            f'<section class="process-block{reverse}">'
            f'<div class="process-photo"><img src="../assets/{img}" alt="{item["name"]}" /></div>'
            f'<div class="process-copy">'
            f'<span class="mono">{item["no"]}</span>'
            f'<h3>{item["name"]}</h3>'
            f'<p class="process-desc">{item["desc"]}</p>'
            f'<ul class="proof-list">{points}</ul>'
            f'</div></section>'
        )
    path_title = "工艺主路径" if t["dir"] == "zh" else "Process path"
    path_body = (
        "从 SMT / 插件到线束与整机，测试嵌在路径中。下面按模块展开关键参数与现场图。"
        if t["dir"] == "zh"
        else "From SMT and THT to harness and box-build, with test embedded in the path. Key parameters and floor photos below."
    )
    body = f"""
<div class="container">
  <header class="page-hero">
    <span class="mono">{m["kicker"]}</span>
    <h1>{m["h1"]}</h1>
    <p class="lead">{m["lead"]}</p>
  </header>
</div>
<section class="media-band">
  <div class="media"><img src="../assets/tht-line.jpg" alt="Assembly process" /></div>
  <div class="copy">
    <span class="mono">PROCESS PATH</span>
    <h3>{path_title}</h3>
    <p>{path_body}</p>
  </div>
</section>
<div class="container process-stack">
  {''.join(blocks)}
  <section class="content-block">
    <span class="mono">{m["note_title"]}</span>
    <h3>{m["note_title"]}</h3>
    <p>{m["note_body"]}</p>
  </section>
</div>
"""
    return shell(t, m["title"], "manufacturing", body)


def page_about(t):
    a = t["about"]
    blocks = []
    for b in a["blocks"]:
        blocks.append(
            f"""
<section class="content-block">
  <span class="mono">{b["tag"]}</span>
  <h3>{b["title"]}</h3>
  <p>{b["body"]}</p>
</section>"""
        )
    facts = []
    for label, value in a["facts"]:
        facts.append(
            f'<div class="row"><span class="mono">{label}</span><strong>{value}</strong></div>'
        )
    body = f"""
<div class="container">
  <header class="page-hero">
    <span class="mono">{a["kicker"]}</span>
    <h1>{a["h1"]}</h1>
    <p class="lead">{a["lead"]}</p>
  </header>
</div>
<section class="media-band">
  <div class="media"><img src="../assets/lean.jpg" alt="Lean manufacturing" /></div>
  <div class="copy">
    <span class="mono">QUALITY</span>
    <h3>{'质量体系' if t["dir"]=='zh' else 'Quality system'}</h3>
    <ul class="proof-list">
      <li>ISO 9001 / ISO 14000 / IATF 16949</li>
      <li>IPC-A-610 Class 2 &amp; 3 · J-STD-001 · WHMA-A-620</li>
      <li>IPC member</li>
    </ul>
  </div>
</section>
<div class="container">
  <div class="two-col">
    <div>
{''.join(blocks[:2])}
    </div>
    <div>
{''.join(blocks[2:])}
      <section class="content-block" style="border-bottom:none;padding-top:8px">
        <span class="mono">{a["facts_title"]}</span>
        <h3>{a["facts_title"]}</h3>
        <div class="fact-list">{''.join(facts)}</div>
      </section>
    </div>
  </div>
</div>
"""
    return shell(t, a["title"], "about", body)


def page_contact(t):
    c = t["contact"]
    people = []
    for p in c["people"]:
        phone = next((x[3:].strip() for x in p["lines"] if x.startswith("T: ")), "")
        email = next((x[3:].strip() for x in p["lines"] if x.startswith("E: ")), "")
        body_html = []
        if phone:
            tel = phone.replace(" ", "")
            body_html.append(f'<a href="tel:{tel}">{phone}</a>')
        if email:
            body_html.append(f'<a href="mailto:{email}">{email}</a>')
        people.append(
            f"""
<div class="contact-card">
  <div>
    <span class="mono label">{p["role"]}</span>
    <h3>{p["name"]}</h3>
    <p class="role">{p["title"]}</p>
    <p class="body">{"<br>".join(body_html)}</p>
  </div>
</div>"""
        )
    website = c.get("note_body", "www.ts-lihua.com").replace("https://", "")
    body = f"""
<div class="container">
  <header class="page-hero">
    <span class="mono">{c["kicker"]}</span>
    <h1>{c["h1"]}</h1>
    <p class="lead">{c["lead"]}</p>
  </header>
  <div class="contact-grid">
{''.join(people)}
    <div class="contact-card">
      <div>
        <span class="mono label">{'位置' if t["dir"]=='zh' else 'LOCATION'}</span>
        <h3>{c["addr_title"]}</h3>
        <p class="meta">{c["addr_body"]}</p>
      </div>
    </div>
    <div class="contact-card">
      <div>
        <span class="mono label">{'官网' if t["dir"]=='zh' else 'WEBSITE'}</span>
        <h3><a href="https://{website}">{c["note_title"]}</a></h3>
        <p class="meta">{'官方网站' if t["dir"]=='zh' else 'Official website'}</p>
      </div>
    </div>
  </div>
</div>
"""
    return shell(t, c["title"], "contact", body)


def main():
    for locale, t in I18N.items():
        out = ROOT / t["dir"]
        out.mkdir(parents=True, exist_ok=True)
        pages = {
            "index.html": page_home(t),
            "manufacturing.html": page_manufacturing(t),
            "about.html": page_about(t),
            "contact.html": page_contact(t),
        }
        for name, html in pages.items():
            (out / name).write_text(html, encoding="utf-8")
            print("wrote", out / name)
    print("done")


if __name__ == "__main__":
    main()
