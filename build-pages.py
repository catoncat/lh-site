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
        "status": "LIHUA ELECTRONICS · SINCE 1993",
        "location": "TAISHAN · GUANGDONG · CHINA",
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
            "title": "利华电子 | PCBA、线束与机电装配制造服务",
            "description": "台山市利华电子厂有限公司提供 PCBA、插件组装、定制线束、机电装配与测试服务，拥有 30+ 年电子制造服务经验。",
            "hero_kicker": "ELECTRONICS MANUFACTURING SERVICES · SINCE 1993",
            "hero_title": "高质量电子产品的\n一站式制造伙伴",
            "hero_lead": "从 PCBA、插件组装、定制线束到整机装配与测试，利华为工业、交通、航空与检测设备客户提供稳定、灵活、可追溯的电子制造服务。",
            "hero_primary": "提交项目需求",
            "hero_secondary": "查看制造能力",
            "hero_note": "广东台山 · 工程支持 · 灵活批量 · 全球项目经验",
            "hero_image_alt": "利华电子台山生产厂区",
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
                ("成立于", "1993"),
                ("EMS 经验", "30+ 年"),
                ("生产车间", "7,000㎡"),
                ("贴片产能", "350K/h"),
            ],
            "cap_kicker": "WHAT WE BUILD",
            "cap_intro": "四条制造能力主线覆盖板卡、线束与整机，测试和质量控制嵌入每个关键工序。",
            "capabilities": [
                {
                    "no": "01",
                    "name": "PCBA · SMT",
                    "desc": "锡膏印刷、高速贴片、回流焊、在线 AOI 与 X-Ray 检查。",
                    "metric": "0201+ · 510×510mm · 350K pcs/h",
                    "image": "smt-line-single.png",
                },
                {
                    "no": "02",
                    "name": "插件组装",
                    "desc": "元件成型、自动/手工插装、波峰焊、DI 清洗与过程检验。",
                    "metric": "THT · Wave Soldering · AOI",
                    "image": "tht-line.jpg",
                },
                {
                    "no": "03",
                    "name": "定制线缆与线束",
                    "desc": "压接、焊接与 IDC，覆盖工业、汽车及航空类复杂线束。",
                    "metric": "0–500kg 拉力 · 32,000 测试点",
                    "image": "harness.png",
                },
                {
                    "no": "04",
                    "name": "机电装配与测试",
                    "desc": "Box-build、ICT/FCT、固件烧录、老化、环境试验与定制包装。",
                    "metric": "ICT · FCT · Burn-in · Hi-Pot",
                    "image": "box-build.png",
                },
            ],
            "mes_kicker": "DIGITAL PROCESS CONTROL",
            "mes_title": "MES 连接每一道工序，\n让质量过程可追溯",
            "mes_body": "利华通过 MES 将生产任务、物料批次、工序执行、检验测试与异常处置串联起来，让质量要求落实到制造过程并形成可查询的生产履历。",
            "mes_items": [
                ("01", "工单与物料", "关联生产任务、BOM 与物料批次。"),
                ("02", "工序执行", "记录关键工序的人员、设备与时间。"),
                ("03", "检验与测试", "汇集制程检验、测试结果与不良信息。"),
                ("04", "追溯与闭环", "建立生产履历并记录异常处置与改进。"),
            ],
            "quality_kicker": "QUALITY BUILT INTO THE PROCESS",
            "quality_title": "不是交付前检查，\n而是全过程质量控制",
            "quality_body": "从来料、制程到功能与环境测试，利华按项目要求配置质量关卡和追溯方式。",
            "quality_items": [
                "ISO 9001 / IATF 16949",
                "IPC-A-610 Class 2 & 3",
                "IPC J-STD-001 / WHMA-A-620",
                "AOI / X-Ray / ICT / FCT",
                "温循 -70°C 至 +200°C",
                "敷形涂覆、老化与耐压测试",
            ],
            "process_kicker": "PROJECT PATH",
            "process_title": "从资料评审到稳定量产",
            "process_items": [
                ("01", "工程评审", "确认 BOM、图纸、测试与质量要求。"),
                ("02", "NPI 与打样", "完成 DFM、工艺设计、治具和样品验证。"),
                ("03", "过程控制", "按工序设置检验、测试和追溯节点。"),
                ("04", "量产交付", "以灵活排产、质量一致性和准时交付支撑长期合作。"),
            ],
            "industry_kicker": "INDUSTRIES & APPLICATIONS",
            "industry_intro": "制造能力服务于高可靠、复杂装配和多品种项目。",
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
            "cta_body": "有新项目、样品或工艺问题？直接把需求发给工厂团队。",
            "cta_btn": "联系项目团队",
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
            "campus_kicker": "THE FACTORY",
            "campus_title": "真实现场，稳定制造",
            "campus_body": "利华位于广东台山，厂区占地 50 亩并预留 30 亩扩展用地，生产车间约 7,000 平方米。团队以工程支持、灵活响应和长期合作为核心。",
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
        "status": "LIHUA ELECTRONICS · SINCE 1993",
        "location": "TAISHAN · GUANGDONG · CHINA",
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
            "title": "LIHUA ELECTRONICS | PCBA, Cable Harness & Box-Build EMS",
            "description": "Taishan City Lihua Electric Factory provides PCBA, THT assembly, custom cable harness, box-build and testing backed by 30+ years of EMS experience.",
            "hero_kicker": "ELECTRONICS MANUFACTURING SERVICES · SINCE 1993",
            "hero_title": "One manufacturing partner\nfor high-quality electronics",
            "hero_lead": "From PCBA and THT assembly to custom cable harnesses, box-build and test, Lihua delivers flexible, traceable electronics manufacturing for demanding industrial products.",
            "hero_primary": "Start a project",
            "hero_secondary": "Explore capabilities",
            "hero_note": "Taishan, China · Engineering support · Flexible volume · Global project experience",
            "hero_image_alt": "Lihua Electronics manufacturing campus in Taishan",
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
                ("EMS experience", "30+ years"),
                ("Manufacturing floor", "7,000㎡"),
                ("Placement capacity", "350K/h"),
            ],
            "cap_kicker": "WHAT WE BUILD",
            "cap_intro": "Four connected manufacturing capabilities cover boards, harnesses and complete systems, with test and quality control embedded in the process.",
            "capabilities": [
                {
                    "no": "01",
                    "name": "PCBA · SMT",
                    "desc": "Solder paste printing, high-speed placement, reflow, inline AOI and X-Ray inspection.",
                    "metric": "0201+ · 510×510mm · 350K pcs/h",
                    "image": "smt-line-single.png",
                },
                {
                    "no": "02",
                    "name": "THT Assembly",
                    "desc": "Component forming, insertion, wave soldering, DI wash and in-process inspection.",
                    "metric": "THT · Wave Soldering · AOI",
                    "image": "tht-line.jpg",
                },
                {
                    "no": "03",
                    "name": "Custom Cable & Harness",
                    "desc": "Crimp, solder and IDC for complex industrial, automotive and aircraft harness work.",
                    "metric": "0–500kg pull test · 32,000 test points",
                    "image": "harness.png",
                },
                {
                    "no": "04",
                    "name": "Box-Build & Test",
                    "desc": "Electro-mechanical assembly, ICT/FCT, programming, burn-in, environmental test and packaging.",
                    "metric": "ICT · FCT · Burn-in · Hi-Pot",
                    "image": "box-build.png",
                },
            ],
            "mes_kicker": "DIGITAL PROCESS CONTROL",
            "mes_title": "MES connects each production step\nfor traceable quality",
            "mes_body": "Lihua uses MES to connect production tasks, material lots, process execution, inspection, test and exception handling—turning quality requirements into a queryable manufacturing record.",
            "mes_items": [
                ("01", "Work Orders & Materials", "Link production tasks, BOM data and material lots."),
                ("02", "Process Execution", "Record people, equipment and time at key operations."),
                ("03", "Inspection & Test", "Collect in-process checks, test results and defects."),
                ("04", "Traceability & Closure", "Build production history and retain corrective-action records."),
            ],
            "quality_kicker": "QUALITY BUILT INTO THE PROCESS",
            "quality_title": "Quality is controlled throughout,\nnot inspected in at the end",
            "quality_body": "From incoming material to process, functional and environmental test, quality gates and traceability are configured around each program.",
            "quality_items": [
                "ISO 9001 / IATF 16949",
                "IPC-A-610 Class 2 & 3",
                "IPC J-STD-001 / WHMA-A-620",
                "AOI / X-Ray / ICT / FCT",
                "Temperature cycle -70°C to +200°C",
                "Conformal coating, burn-in and hi-pot",
            ],
            "process_kicker": "PROJECT PATH",
            "process_title": "From engineering review to stable production",
            "process_items": [
                ("01", "Engineering review", "Align BOM, drawings, test coverage and quality requirements."),
                ("02", "NPI & prototype", "Complete DFM, process design, fixtures and sample validation."),
                ("03", "Process control", "Place inspection, test and traceability gates along the build path."),
                ("04", "Production delivery", "Support long-term programs with flexible scheduling and consistent output."),
            ],
            "industry_kicker": "INDUSTRIES & APPLICATIONS",
            "industry_intro": "Built for high-reliability, complex assembly and high-mix programs.",
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
            "cta_body": "Have a new build, sample or process question? Send it directly to the plant team.",
            "cta_btn": "Contact the project team",
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
            "campus_kicker": "THE FACTORY",
            "campus_title": "A real factory built for consistent delivery",
            "campus_body": "Lihua is based in Taishan, Guangdong, with a 50-mu campus, 30 mu of reserved expansion land and about 7,000 square meters of manufacturing space. Engineering support, responsiveness and long-term partnership guide the work.",
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
  <div class="mono nav-status"><span class="nav-brand">LIHUA</span><span class="nav-context"> ELECTRONICS · SINCE 1993</span></div>
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
    nav_links = "".join(
        f'<a href="{t["paths"][key]}">{t["nav"][key]}</a>'
        for key in ("home", "manufacturing", "about", "contact")
    )
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand-block">
        <div class="footer-logo">LIHUA®</div>
        <p class="footer-summary">{f["tagline"]}</p>
      </div>
      <div class="footer-nav-block">
        <span class="mono col-title">NAVIGATION</span>
        <nav class="footer-links" aria-label="Footer">{nav_links}</nav>
      </div>
      <div class="footer-contact-block">
        <span class="mono col-title">{f["contact"]}</span>
        <p><a href="tel:+867505625181">+86 750 5625181</a><br><a href="mailto:raylee@ts-lihua.com">raylee@ts-lihua.com</a></p>
      </div>
      <div class="footer-legal-block">
        <span class="mono col-title">{f["legal"]}</span>
        <p>{f["legal_lines"]}</p>
      </div>
    </div>
    <div class="footer-bottom"><span class="mono">{f["copy"]}</span><span class="mono">TAISHAN · GUANGDONG · CHINA</span></div>
  </div>
</footer>
"""


def shell(t, title: str, active: str, body: str, description=None, body_class: str = "") -> str:
    meta_description = description or "Taishan City Lihua Electronics Factory — PCBA, harness, electromechanical manufacturing."
    class_attr = f' class="{body_class}"' if body_class else ""
    skip_text = "跳到主要内容" if t["dir"] == "zh" else "Skip to content"
    skip_link = f'<a class="skip-link" href="#main-content">{skip_text}</a>' if body_class else ""
    return f"""<!doctype html>
<html lang="{t["lang"]}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{meta_description}" />
  <link rel="stylesheet" href="../css/site.css?v=20260715" />
</head>
<body{class_attr}>
{skip_link}
{nav(t, active)}
{body}
{footer(t)}
<script src="../js/site.js"></script>
</body>
</html>
"""



def page_home(t):
    h = t["home"]
    hero_title = h["hero_title"].replace("\n", "<br> ")
    mes_title = h["mes_title"].replace("\n", "<br> ")
    quality_title = h["quality_title"].replace("\n", "<br> ")
    stats = [
        f'<div class="home-stat"><strong>{value}</strong><span>{label}</span></div>'
        for label, value in h["stats"]
    ]
    capabilities = []
    for item in h["capabilities"]:
        capabilities.append(
            '<article class="capability-card">'
            '<div class="capability-photo">'
            f'<img src="../assets/{item["image"]}" alt="{item["name"]}" loading="lazy" decoding="async" />'
            f'<span class="capability-no mono">{item["no"]}</span>'
            '</div>'
            '<div class="capability-copy">'
            f'<h3>{item["name"]}</h3><p>{item["desc"]}</p>'
            f'<span class="capability-metric mono">{item["metric"]}</span>'
            '</div></article>'
        )
    quality_items = [f'<li>{item}</li>' for item in h["quality_items"]]
    mes_items = [
        '<li class="mes-flow-item">'
        f'<span class="mes-flow-no mono">{no}</span><div><h3>{title}</h3><p>{desc}</p></div>'
        '</li>'
        for no, title, desc in h["mes_items"]
    ]
    process_items = [
        '<li class="process-step">'
        f'<span class="process-no mono">{no}</span><div><h3>{title}</h3><p>{desc}</p></div>'
        '</li>'
        for no, title, desc in h["process_items"]
    ]
    applications = []
    for idx, (title, desc, img) in enumerate(h["apps"], 1):
        applications.append(
            '<article class="industry-card">'
            f'<img src="../assets/{img}" alt="{title}" loading="lazy" decoding="async" />'
            '<div class="industry-card-copy">'
            f'<span class="mono">0{idx}</span><h3>{title}</h3><p>{desc}</p>'
            '</div></article>'
        )
    body = f"""
<main id="main-content" class="home-main">
  <section class="home-hero">
    <div class="container home-hero-grid">
      <div class="home-hero-copy">
        <span class="eyebrow mono">{h["hero_kicker"]}</span>
        <h1>{hero_title}</h1>
        <p class="home-hero-lead">{h["hero_lead"]}</p>
        <div class="home-actions">
          <a class="button button-primary" href="{t["paths"]["contact"]}">{h["hero_primary"]}<span aria-hidden="true">→</span></a>
          <a class="button button-secondary" href="{t["paths"]["manufacturing"]}">{h["hero_secondary"]}</a>
        </div>
        <p class="home-hero-note mono">{h["hero_note"]}</p>
      </div>
      <figure class="home-hero-visual">
        <img src="../assets/plant.jpg" alt="{h["hero_image_alt"]}" fetchpriority="high" decoding="async" />
        <figcaption><span>LIHUA</span><strong>TAISHAN<br>CHINA</strong></figcaption>
      </figure>
    </div>
  </section>

  <section class="home-proof" aria-label="Company facts">
    <div class="container home-stats">{''.join(stats)}</div>
  </section>

  <section class="home-section home-capabilities" id="capabilities">
    <div class="container">
      <div class="home-section-head">
        <div><span class="eyebrow mono">{h["cap_kicker"]}</span><h2>{h["cap_title"]}</h2></div>
        <p>{h["cap_intro"]}</p>
      </div>
      <div class="capability-grid">{''.join(capabilities)}</div>
      <a class="section-link" href="{t["paths"]["manufacturing"]}">{h["hero_secondary"]}<span aria-hidden="true">→</span></a>
    </div>
  </section>

  <section class="home-mes">
    <div class="container home-mes-grid">
      <div class="home-mes-copy">
        <span class="eyebrow mono">{h["mes_kicker"]}</span>
        <h2>{mes_title}</h2>
        <p>{h["mes_body"]}</p>
        <span class="mes-system-label mono">MES · PROCESS · QUALITY · TRACEABILITY</span>
      </div>
      <ol class="mes-flow">{''.join(mes_items)}</ol>
    </div>
  </section>

  <section class="home-quality">
    <div class="container home-quality-grid">
      <div class="home-quality-copy">
        <span class="eyebrow mono">{h["quality_kicker"]}</span>
        <h2>{quality_title}</h2>
        <p>{h["quality_body"]}</p>
        <ul class="quality-list">{''.join(quality_items)}</ul>
      </div>
      <div class="home-quality-photo">
        <img src="../assets/testing.png" alt="Testing and quality inspection equipment" loading="lazy" decoding="async" />
        <span class="photo-label mono">AOI · X-RAY · ICT · FCT</span>
      </div>
    </div>
  </section>

  <section class="home-section home-process">
    <div class="container">
      <div class="home-section-head compact">
        <div><span class="eyebrow mono">{h["process_kicker"]}</span><h2>{h["process_title"]}</h2></div>
      </div>
      <ol class="process-list">{''.join(process_items)}</ol>
    </div>
  </section>

  <section class="home-section home-industries">
    <div class="container">
      <div class="home-section-head">
        <div><span class="eyebrow mono">{h["industry_kicker"]}</span><h2>{h["apps_title"]}</h2></div>
        <p>{h["industry_intro"]}</p>
      </div>
      <div class="industry-grid">{''.join(applications)}</div>
    </div>
  </section>

  <section class="home-factory">
    <div class="home-factory-photo"><img src="../assets/lean.jpg" alt="Lihua production floor" loading="lazy" decoding="async" /></div>
    <div class="home-factory-copy">
      <span class="eyebrow mono">{h["campus_kicker"]}</span>
      <h2>{h["campus_title"]}</h2>
      <p>{h["campus_body"]}</p>
      <div class="chip-row"><span class="chip">EMS</span><span class="chip">PCBA</span><span class="chip">HARNESS</span><span class="chip">BOX-BUILD</span></div>
    </div>
  </section>

  <section class="home-final-cta">
    <div class="container home-final-cta-inner">
      <div><span class="eyebrow mono">{h["cta_title"]}</span><h2>{h["cta_body"]}</h2></div>
      <a class="button button-light" href="{t["paths"]["contact"]}">{h["cta_btn"]}<span aria-hidden="true">→</span></a>
    </div>
  </section>
</main>
"""
    return shell(t, h["title"], "home", body, h["description"], "home-page")


def page_manufacturing(t):
    m = t["manufacturing"]
    zh = t["dir"] == "zh"
    images = ["smt-line-single.png", "tht-line.jpg", "harness.png", "box-build.png"]
    blocks = []
    for i, item in enumerate(m["items"]):
        img = images[i % len(images)]
        points = "".join(f"<li>{p}</li>" for p in item["points"])
        reverse = " reverse" if i % 2 else ""
        blocks.append(
            f'<section class="manufacturing-module{reverse}" id="process-{i + 1}">'
            f'<div class="manufacturing-module-photo"><img src="../assets/{img}" alt="{item["name"]}" loading="lazy" decoding="async" /></div>'
            f'<div class="manufacturing-module-copy"><span class="eyebrow mono">{item["no"]}</span>'
            f'<h2>{item["name"]}</h2><p class="module-desc">{item["desc"]}</p>'
            f'<ul class="module-facts">{points}</ul></div></section>'
        )
    page = {
        "eyebrow": "MANUFACTURING CAPABILITIES",
        "title": "从板卡到整机，制造与测试一体化" if zh else "Integrated manufacturing from board to complete system",
        "lead": "工艺、测试与质量控制沿同一条制造路径协同，适合多品种、复杂装配和中高批量项目。" if zh else "Process, test and quality control work along one connected path for high-mix, complex assemblies and medium-to-high volume programs.",
        "primary": "联系工程团队" if zh else "Contact engineering",
        "secondary": "查看工艺模块" if zh else "View process modules",
        "facts": [
            ("贴片总产能" if zh else "Placement capacity", "350K pcs/h"),
            ("最大板尺寸" if zh else "Max board size", "510×510mm"),
            ("线束测试" if zh else "Harness test", "32,000 points"),
            ("温度循环" if zh else "Temperature cycle", "-70°C ~ +200°C"),
        ],
        "nav_label": "能力索引" if zh else "Capability index",
        "quality_kicker": "TEST & QUALITY",
        "quality_title": "测试不是最后一步，\n而是制造路径的一部分" if zh else "Test is part of the build path,\nnot a final afterthought",
        "quality_body": "根据产品和客户要求配置 AOI、X-Ray、ICT、FCT、固件烧录、耐压、老化与环境测试，并将质量节点嵌入生产过程。" if zh else "AOI, X-Ray, ICT, FCT, firmware programming, hi-pot, burn-in and environmental tests are configured around product and customer requirements.",
        "quality_items": ["AOI / AAOI", "BGA X-Ray", "Agilent 3070 ICT", "Functional Test", "Firmware Programming", "Burn-in / Hi-Pot"],
        "mes_kicker": "MES PROCESS CONTROL",
        "mes_title": "用生产数据连接过程与质量" if zh else "Production data connects process and quality",
        "mes_body": "MES 将生产任务、关键工序记录、质量数据与批次追溯纳入同一生产履历，为过程控制、问题定位与持续改进提供依据。" if zh else "MES brings production tasks, key operation records, quality data and lot traceability into one manufacturing history for process control, issue analysis and continual improvement.",
        "mes_items": ["生产任务", "工序记录", "质量数据", "批次追溯"] if zh else ["Production tasks", "Process records", "Quality data", "Lot traceability"],
        "more_kicker": "ADDITIONAL PROCESSES",
        "more_title": "按项目配置的补充工艺" if zh else "Additional processes configured by program",
        "more_items": [
            ("热压焊" if zh else "Hot-bar soldering", "FPC to rigid board"),
            ("自动敷形涂覆" if zh else "Automated conformal coating", "Controlled protection"),
            ("激光标识" if zh else "Laser marking", "Durable traceability"),
            ("老化与温循" if zh else "Burn-in & temperature cycle", "Up to +150°C / -70°C to +200°C"),
        ],
        "cta": "把图纸、BOM 和测试要求发给我们，先确认工艺匹配。" if zh else "Send the drawings, BOM and test requirements for an initial process-fit review.",
        "cta_button": "开始项目沟通" if zh else "Start a project discussion",
    }
    hero_title = page["title"].replace("\n", "<br> ")
    quality_title = page["quality_title"].replace("\n", "<br> ")
    facts = "".join(f'<div class="inner-stat"><strong>{value}</strong><span>{label}</span></div>' for label, value in page["facts"])
    index_links = "".join(f'<a href="#process-{i + 1}"><span>0{i + 1}</span>{item["name"]}</a>' for i, item in enumerate(m["items"]))
    quality_items = "".join(f'<li>{item}</li>' for item in page["quality_items"])
    mes_items = "".join(f'<li>{item}</li>' for item in page["mes_items"])
    more_items = "".join(f'<article><span class="mono">0{i + 1}</span><h3>{title}</h3><p>{desc}</p></article>' for i, (title, desc) in enumerate(page["more_items"]))
    body = f"""
<main id="main-content" class="inner-main">
  <section class="inner-hero manufacturing-hero">
    <div class="container inner-hero-grid">
      <div class="inner-hero-copy">
        <span class="eyebrow mono">{page["eyebrow"]}</span>
        <h1>{hero_title}</h1>
        <p>{page["lead"]}</p>
        <div class="home-actions">
          <a class="button button-primary" href="{t["paths"]["contact"]}">{page["primary"]}<span aria-hidden="true">→</span></a>
          <a class="button button-secondary" href="#process-1">{page["secondary"]}</a>
        </div>
      </div>
      <div class="inner-hero-photo"><img src="../assets/tht-line.jpg" alt="Assembly process" fetchpriority="high" decoding="async" /><span class="photo-label mono">SMT · THT · HARNESS · BOX-BUILD</span></div>
    </div>
  </section>

  <section class="inner-proof"><div class="container inner-stats">{facts}</div></section>

  <nav class="capability-index container" aria-label="{page["nav_label"]}"><span class="mono">{page["nav_label"]}</span><div>{index_links}</div></nav>

  <div class="container manufacturing-modules">{''.join(blocks)}</div>

  <section class="manufacturing-quality">
    <div class="container manufacturing-quality-grid">
      <div class="manufacturing-quality-copy"><span class="eyebrow mono">{page["quality_kicker"]}</span><h2>{quality_title}</h2><p>{page["quality_body"]}</p><ul>{quality_items}</ul></div>
      <div class="manufacturing-quality-photo"><img src="../assets/testing.png" alt="Testing equipment" loading="lazy" decoding="async" /></div>
    </div>
    <div class="container manufacturing-mes">
      <div><span class="eyebrow mono">{page["mes_kicker"]}</span><h3>{page["mes_title"]}</h3><p>{page["mes_body"]}</p></div>
      <ul>{mes_items}</ul>
    </div>
  </section>

  <section class="inner-section additional-processes"><div class="container"><div class="inner-section-head"><span class="eyebrow mono">{page["more_kicker"]}</span><h2>{page["more_title"]}</h2></div><div class="additional-grid">{more_items}</div></div></section>

  <section class="inner-final-cta"><div class="container inner-final-cta-grid"><h2>{page["cta"]}</h2><a class="button button-light" href="{t["paths"]["contact"]}">{page["cta_button"]}<span aria-hidden="true">→</span></a></div></section>
</main>
"""
    description = "利华电子提供 SMT、插件组装、定制线束、机电装配以及 ICT/FCT 测试服务。" if zh else "Lihua provides SMT, THT assembly, custom harness, box-build and ICT/FCT testing services."
    return shell(t, m["title"], "manufacturing", body, description, "inner-page manufacturing-page")


def page_about(t):
    a = t["about"]
    zh = t["dir"] == "zh"
    facts = "".join(f'<div class="inner-stat"><strong>{value}</strong><span>{label}</span></div>' for label, value in a["facts"])
    offers = "".join(
        f'<article class="about-value"><span class="mono">0{i + 1}</span><h3>{title}</h3><p>{desc}</p></article>'
        for i, (title, desc) in enumerate(t["home"]["offers"])
    )
    page = {
        "eyebrow": "TAISHAN CITY LIHUA ELECTRIC FACTORY LTD.",
        "title": "三十余年，专注把高质量电子产品稳定制造出来" if zh else "More than three decades focused on high-quality electronics manufacturing",
        "lead": "利华成立于 1993 年，提供供应链协同、工程支持、完整生产配套与测试服务，长期服务于高可靠和复杂装配项目。" if zh else "Founded in 1993, Lihua combines supply-chain coordination, engineering support, complete manufacturing processes and test for high-reliability, complex assemblies.",
        "story_kicker": "OUR FOUNDATION",
        "story_title": "从台山出发，做长期制造伙伴" if zh else "Built in Taishan for long-term manufacturing partnerships",
        "story_body": "30+ 年的 EMS 经验让团队更关注可制造性、过程一致性与持续交付，而不是一次性的产品展示。厂区与工程团队围绕客户项目长期协作。" if zh else "Over 30 years of EMS experience has shaped a focus on manufacturability, process consistency and sustained delivery rather than one-off builds.",
        "campus_kicker": "CAMPUS & PEOPLE",
        "campus_title": "真实厂区，真实生产现场" if zh else "A real campus and an experienced production team",
        "campus_body": "厂区占地 50 亩，并预留 30 亩扩展用地；生产车间约 7,000 平方米。精益方法用于适合的产品与工序，以提升效率和质量一致性。" if zh else "The 50-mu campus includes 30 mu of reserved expansion land and about 7,000 square meters of manufacturing space. Lean methods are applied where they improve efficiency and consistency.",
        "quality_kicker": "QUALITY SYSTEM",
        "quality_title": "用体系、标准和现场执行建立信任" if zh else "Trust built through systems, standards and floor execution",
        "quality_body": "质量体系与工艺标准覆盖板卡、线束与整机装配，并按项目要求配置检验、测试和追溯。" if zh else "Quality systems and workmanship standards cover board, harness and box-build programs with inspection, test and traceability configured by project.",
        "values_kicker": "HOW WE WORK",
        "values_title": "合作原则" if zh else "Working principles",
        "cta": "需要进一步了解厂区、审核资料或安排项目沟通？" if zh else "Need a deeper capability review, audit information or project discussion?",
        "cta_button": "联系利华" if zh else "Contact Lihua",
    }
    title = page["title"].replace("\n", "<br> ")
    body = f"""
<main id="main-content" class="inner-main">
  <section class="inner-hero about-hero"><div class="container inner-hero-grid"><div class="inner-hero-copy"><span class="eyebrow mono">{page["eyebrow"]}</span><h1>{title}</h1><p>{page["lead"]}</p></div><div class="inner-hero-photo"><img src="../assets/plant.jpg" alt="Lihua campus" fetchpriority="high" decoding="async" /><span class="photo-label mono">FOUNDED 1993 · TAISHAN</span></div></div></section>

  <section class="inner-proof"><div class="container inner-stats">{facts}</div></section>

  <section class="inner-section about-story"><div class="container about-story-grid"><div><span class="eyebrow mono">{page["story_kicker"]}</span><h2>{page["story_title"]}</h2></div><div><p>{page["story_body"]}</p><p>{a["blocks"][1]["body"]}</p></div></div></section>

  <section class="about-campus"><div class="about-campus-gallery"><img src="../assets/lean.jpg" alt="Lihua production floor" loading="lazy" decoding="async" /><img src="../assets/assembly.jpg" alt="Lihua assembly line" loading="lazy" decoding="async" /></div><div class="about-campus-copy"><span class="eyebrow mono">{page["campus_kicker"]}</span><h2>{page["campus_title"]}</h2><p>{page["campus_body"]}</p></div></section>

  <section class="about-quality"><div class="container about-quality-grid"><div><span class="eyebrow mono">{page["quality_kicker"]}</span><h2>{page["quality_title"]}</h2><p>{page["quality_body"]}</p></div><ul><li>ISO 9001</li><li>IATF 16949</li><li>ISO 14000</li><li>IPC-A-610 Class 2 &amp; 3</li><li>IPC J-STD-001</li><li>IPC/WHMA-A-620</li></ul></div></section>

  <section class="inner-section about-values"><div class="container"><div class="inner-section-head"><span class="eyebrow mono">{page["values_kicker"]}</span><h2>{page["values_title"]}</h2></div><div class="about-values-grid">{offers}</div></div></section>

  <section class="inner-final-cta"><div class="container inner-final-cta-grid"><h2>{page["cta"]}</h2><a class="button button-light" href="{t["paths"]["contact"]}">{page["cta_button"]}<span aria-hidden="true">→</span></a></div></section>
</main>
"""
    description = "了解利华电子自 1993 年以来的 EMS 经验、台山厂区、质量体系与合作原则。" if zh else "Learn about Lihua's EMS experience since 1993, Taishan campus, quality systems and working principles."
    return shell(t, a["title"], "about", body, description, "inner-page about-page")


def page_contact(t):
    c = t["contact"]
    zh = t["dir"] == "zh"
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
            f'<article class="contact-person"><span class="eyebrow mono">{p["role"]}</span><h2>{p["name"]}</h2><p class="contact-role">{p["title"]}</p><div class="contact-person-links">{"".join(f"<span>{line}</span>" for line in body_html)}</div></article>'
        )
    website = c.get("note_body", "www.ts-lihua.com").replace("https://", "")
    page = {
        "eyebrow": "START A CONVERSATION",
        "title": "让我们先确认项目是否匹配" if zh else "Let's start by confirming the project fit",
        "lead": "无论是新项目评估、样品、工艺问题还是供应商审核，都可以直接联系工厂团队。" if zh else "For new program review, samples, process questions or supplier audits, contact the plant team directly.",
        "primary": "发送项目邮件" if zh else "Send a project email",
        "secondary": "拨打工厂电话" if zh else "Call the factory",
        "people_kicker": "DIRECT CONTACTS",
        "people_title": "直接联系项目负责人" if zh else "Contact the project team directly",
        "brief_kicker": "PROJECT BRIEF",
        "brief_title": "邮件中建议包含这些资料" if zh else "What to include in the first email",
        "brief_items": [
            "产品类型与应用场景" if zh else "Product type and application",
            "BOM、Gerber、图纸或线束资料" if zh else "BOM, Gerber, drawings or harness data",
            "预计批量与交付节奏" if zh else "Expected volume and delivery cadence",
            "测试、认证与追溯要求" if zh else "Test, certification and traceability requirements",
            "样品或 NPI 时间计划" if zh else "Sample or NPI timeline",
        ],
        "location_kicker": "LOCATION",
        "location_title": "中国 · 广东 · 台山" if zh else "Taishan · Guangdong · China",
        "location_body": "台山市利华电子厂有限公司，生产车间约 7,000 平方米。" if zh else "Taishan City Lihua Electric Factory Ltd., with about 7,000 square meters of manufacturing space.",
    }
    title = page["title"].replace("\n", "<br> ")
    brief_items = "".join(f'<li><span class="mono">0{i + 1}</span>{item}</li>' for i, item in enumerate(page["brief_items"]))
    body = f"""
<main id="main-content" class="inner-main">
  <section class="contact-hero"><div class="container contact-hero-grid"><div><span class="eyebrow mono">{page["eyebrow"]}</span><h1>{title}</h1><p>{page["lead"]}</p><div class="home-actions"><a class="button button-primary" href="mailto:raylee@ts-lihua.com">{page["primary"]}<span aria-hidden="true">→</span></a><a class="button button-secondary" href="tel:+867505625181">{page["secondary"]}</a></div></div><div class="contact-hero-mark"><strong>LIHUA</strong><span>EMS · EST. 1993</span></div></div></section>

  <section class="inner-section contact-people-section"><div class="container"><div class="inner-section-head"><span class="eyebrow mono">{page["people_kicker"]}</span><h2>{page["people_title"]}</h2></div><div class="contact-people-grid">{''.join(people)}</div></div></section>

  <section class="contact-brief"><div class="container contact-brief-grid"><div><span class="eyebrow mono">{page["brief_kicker"]}</span><h2>{page["brief_title"]}</h2></div><ol>{brief_items}</ol></div></section>

  <section class="contact-location"><div class="contact-location-photo"><img src="../assets/plant.jpg" alt="Lihua campus" loading="lazy" decoding="async" /></div><div class="contact-location-copy"><span class="eyebrow mono">{page["location_kicker"]}</span><h2>{page["location_title"]}</h2><p>{page["location_body"]}</p><div class="contact-location-links"><a href="https://{website}">{website}<span aria-hidden="true">↗</span></a><a href="mailto:raylee@ts-lihua.com">raylee@ts-lihua.com<span aria-hidden="true">→</span></a></div></div></section>
</main>
"""
    description = "联系利华电子工厂团队，沟通 PCBA、线束、机电装配、样品及供应商审核需求。" if zh else "Contact Lihua's plant team about PCBA, harness, box-build, samples and supplier audit requirements."
    return shell(t, c["title"], "contact", body, description, "inner-page contact-page")


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
