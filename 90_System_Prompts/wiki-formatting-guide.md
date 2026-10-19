---
title: Wiki Formatting Guide
type: system
status: active
created: 2026-10-19
updated: 2026-10-19
tags:
  - system/guide
  - meta/formatting
aliases:
  - คู่มือการเขียน
  - Formatting Rules
---

# Wiki Formatting Guide

คู่มือนี้คือ "กฎหมาย" ของ vault นี้ — ทุก note ต้องทำตาม เพื่อให้ graph view อ่านได้
ให้ search ทำงาน และให้ Hermes จัดหมวดหมู่ได้อัตโนมัติ

## 1. โครงสร้างโฟลเดอร์

| โฟลเดอร์ | เก็บอะไร | อะไร**ไม่**ควรอยู่ |
|---|---|---|
| `00_Inbox/` | ของดิบที่ยังไม่จัด — paste, voice note, ลิงก์, ความคิดลอย | ของที่จัดแล้ว (ย้ายออกภายใน 7 วัน) |
| `10_MOC/` | Map of Content — note ที่ทำหน้าที่เป็นสารบัญ/แผนที่ | เนื้อหาความรู้จริง (ให้ลิงก์ไปแทน) |
| `20_Knowledge/21_Tech_AI/` | AI, software, infra, automation, LLM | งาน offshore, การเงิน |
| `20_Knowledge/22_Offshore_Ops/` | oil & gas, rotating equipment, CMMS, reliability, HSE | tech ทั่วไป, trading |
| `20_Knowledge/23_Trading_Finance/` | ลงทุน, ตลาด, เศรษฐศาสตร์, พอร์ต | งานวิศวกรรม |
| `30_Projects/` | งานที่มีจุดจบ มี deadline มี deliverable | ความรู้ทั่วไป (ไป `20_Knowledge`) |
| `40_Journals/` | บันทึกรายวัน/รายสัปดาห์, retro, decision log | บทความที่เรียบเรียงแล้ว |
| `90_System_Prompts/` | กฎ, persona, template ของ vault | เนื้อหาความรู้ |

**หลักคิด:** โฟลเดอร์ = *โดเมนกว้าง* / tag = *มุมตัดขวาง* / wikilink = *ความสัมพันธ์*
ถ้าต้องเลือก — ใส่โฟลเดอร์ตามโดเมนหลักก่อน แล้วใช้ tag + link เชื่อมส่วนตัว

## 2. YAML Frontmatter

ทุก note ต้องเริ่มด้วย frontmatter คั่นด้วย `---` บรรทัดแรกของไฟล์

```yaml
---
title: ชื่อ note (อ่านรู้เรื่องโดยไม่ต้องเปิด)
type: concept          # ดูตาราง type ด้านล่าง
status: active         # inbox | active | draft | archived
created: 2026-10-19
updated: 2026-10-19
tags:
  - domain/topic
  - domain/subtopic
aliases:
  - ชื่อเรียกอื่น
  - English Name
---
```

### ฟิลด์ที่บังคับ

| ฟิลด์ | ค่า | กฎ |
|---|---|---|
| `title` | string | ตรงหรือใกล้เคียงชื่อไฟล์ |
| `type` | enum | ดูตาราง type |
| `status` | enum | `inbox` → `active` → `archived` |
| `created` | `YYYY-MM-DD` | วันที่สร้าง ห้ามแก้ |
| `updated` | `YYYY-MM-DD` | แก้ทุกครั้งที่เนื้อหาเปลี่ยน |

### ฟิลด์เสริม (ใส่เมื่อมีประโยชน์)

`aliases` · `tags` · `source` (URL/หนังสือ) · `related` (ลิสต์ wikilink) ·
`project` · `confidence` (`high`/`medium`/`low`) · `review_by` (วันที่ควรทบทวน)

### ค่า `type` ที่อนุญาต

`concept` · `howto` · `reference` · `moc` · `project` · `journal` · `decision` · `source` · `system`

### กฎ YAML

- ใช้ **kebab-case** กับ key ที่มากกว่าหนึ่งคำ (`review_by`)
- วันที่เป็น ISO เสมอ: `2026-10-19` ไม่ใช่ `19/10/2026`
- ห้ามใช้ tab — ใช้ space 2 ตัว
- string ที่มี `:` หรือ `#` ต้องใส่ quote
- ถ้าไม่มีอะไรจะใส่ ปล่อยว่างได้ แต่อย่าลบ key ที่บังคับ

## 3. การตั้งชื่อไฟล์

- **สื่อความหมาย** — `weibull-beta-interpretation.md` ดีกว่า `note-12.md`
- **ตัวพิมพ์เล็ก + ขีดกลาง** สำหรับ note ภาษาอังกฤษ: `cmms-data-quality.md`
- **ภาษาไทยเขียนติดกันได้**: `การอ่านค่า-beta.md` (แต่หลีกเลี่ยงอักขระพิเศษ `: / \ ? * " < > |`)
- **หนึ่ง note = หนึ่งแนวคิด** — ถ้าชื่อต้องมี "และ" แปลว่าควรแยก
- ตั้งชื่อเป็น *ข้อความ assertion* ได้จะดีมาก: `mtbf-ไม่บอกอะไรถ้าไม่ดู-beta.md`

## 4. Wikilinks

Obsidian link ด้วย `[[ชื่อ note]]` — **ไม่ต้องใส่ path** ถ้าชื่อไม่ซ้ำ

```markdown
[[weibull-beta-interpretation]]              ลิงก์เปล่า
[[weibull-beta-interpretation|ค่า β]]         แสดงข้อความอื่น
[[weibull-beta-interpretation#ข้อควรระวัง]]    ลิงก์ไปที่ heading
[[main-hub]]                                  ลิงก์กลับ hub
```

### กฎ

1. **ลิงก์แบบ atomic** — ลิงก์ไป note ที่เล็กที่สุดที่ตรงประเด็น ไม่ใช่ลิงก์ไปโฟลเดอร์
2. **ทุก note ต้องมีอย่างน้อย 1 inbound link** — ถ้าไม่มี แปลว่าเป็น orphan (graph จะลอยแยก)
3. **ลิงก์สองทางเมื่อเป็นแนวคิดเกี่ยวกัน** — ใส่ `related:` ใน frontmatter ด้วย
4. **ลิงก์ไป note ที่ยังไม่มีได้ถ้าตั้งใจ** — Obsidian จะสร้าง ghost node (แสดงจาง ๆ) ซึ่งใช้เป็น "เป้าหมายที่ยังไม่ได้เขียน" ได้ แต่ต้องตามเก็บ
5. **อย่าใช้ full path** ใน wikilink — เปราะเมื่อย้ายโฟลเดอร์

## 5. Atomic Notes

**นิยาม:** note หนึ่งใบ = ความคิดเดียว ที่ยืนได้ด้วยตัวเอง

### เกณฑ์ตัดสิน

- ✅ อ่านใบเดียวแล้วเข้าใจ concept นั้นครบ โดยไม่ต้องเปิดใบอื่น
- ✅ ตั้งชื่อเป็นประโยค/ข้อความได้ เช่น "ทำไม β ระดับระบบถึงหลอกเรา"
- ✅ ยาว 150–600 คำ (เกิน 800 คำ = ควรแยก)
- ✅ มีลิงก์ออกอย่างน้อย 1 และมีลิงก์เข้ามาอย่างน้อย 1
- ❌ ไม่ใช่ไดอารี่ (นั่นคือ `40_Journals`)
- ❌ ไม่ใช่สารบัญ (นั่นคือ `10_MOC`)

### Template — Atomic Note

```markdown
---
title: {{ชื่อที่สื่อความ}}
type: concept
status: active
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
tags:
  - {{domain}}/{{topic}}
---

# {{ชื่อ}}

## สรุปในหนึ่งประโยค
{{ประเด็นหลัก}}

## ทำไมมันสำคัญ
{{ผลต่อการตัดสินใจ/การทำงาน}}

## รายละเอียด
{{เนื้อหา}}

## ข้อควรระวัง / ข้อจำกัด
- {{...}}

## ที่มา
- {{source}}

## เกี่ยวข้อง
- [[{{note อื่น}}]]
```

## 6. Template อื่น ๆ

### MOC (Map of Content)

```markdown
---
title: {{โดเมน}} — MOC
type: moc
status: active
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
tags:
  - moc
---

# {{โดเมน}}

## จุดเริ่มต้น
- [[{{note แกนหลัก}}]]

## หมวดย่อย
- [[{{note}}]] — {{หนึ่งบรรทัดว่าคืออะไร}}

## ยังไม่ได้เขียน
- {{หัวข้อที่อยากได้}}
```

### Project

```markdown
---
title: {{ชื่อโปรเจกต์}}
type: project
status: active
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
project: {{slug}}
deadline: {{YYYY-MM-DD}}
---

# {{ชื่อโปรเจกต์}}

## เป้าหมาย
## สถานะปัจจุบัน
## งานที่ค้าง
- [ ]
## การตัดสินใจ
## บันทึก
```

### Journal

```markdown
---
title: {{YYYY-MM-DD}}
type: journal
status: active
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
tags:
  - journal/daily
---

# {{YYYY-MM-DD}}

## ทำอะไรไป
## อะไรที่ติด
## เรียนรู้อะไร
## พรุ่งนี้
```

## 7. Tags vs Links vs Folders

| กลไก | ใช้เมื่อ | ตัวอย่าง |
|---|---|---|
| โฟลเดอร์ | จัดตามโดเมนหลัก มีที่เดียวเท่านั้น | `22_Offshore_Ops` |
| Tag | มุมตัดขวาง อยู่ได้หลายที่ | `#equipment/gearbox`, `#status/blocked` |
| Wikilink | ความสัมพันธ์แบบเจาะจง | `[[gear]]` → `[[seal-follows-gearbox-failure]]` |

**รูปแบบ tag:** `หมวด/หมวดย่อย` ตัวพิมพ์เล็กทั้งหมด เช่น `reliability/weibull`, `finance/thb`

**อย่าใส่ tag ซ้ำซ้อนกับโฟลเดอร์** — ถ้าอยู่ใน `22_Offshore_Ops` แล้ว ไม่ต้องใส่ `#offshore` อีก

## 8. การจัดรูปแบบในเนื้อหา

- **Callouts** สำหรับของสำคัญ:

  ```markdown
  > [!warning] ข้อควรระวัง
  > เนื้อหา

  > [!note] บริบท
  > เนื้อหา

  > [!question] ยังไม่ชัด
  > เนื้อหา
  ```

- **ตาราง** เมื่อเทียบ 3+ รายการ
- **code block** ต้องระบุภาษา
- **ตัวเลข** ใส่หน่วยและวันที่กำกับเสมอ (เช่น `฿87.7M ณ 2024-10-29`)
- **ห้ามใช้ HTML** — Obsidian อ่าน markdown ได้ตรงกว่า

## 9. Inbox → Filed

1. จับอะไรได้ โยนลง `00_Inbox/` ทันที อย่าคิดตอนจับ
2. ภายใน 7 วัน: อ่าน → แยกเป็น atomic note → ย้ายเข้าโฟลเดอร์ที่ถูก
3. ตั้ง frontmatter ให้ครบ เปลี่ยน `status: inbox` → `active`
4. ลิงก์เข้า MOC ที่เกี่ยวข้อง
5. ลบ (หรือ archive) ต้นฉบับใน Inbox

## 10. Checklist ก่อนบันทึก

- [ ] มี frontmatter ครบ 5 ฟิลด์บังคับ
- [ ] `type` ถูกต้อง
- [ ] ชื่อไฟล์สื่อความ ไม่มีอักขระต้องห้าม
- [ ] หนึ่งแนวคิดต่อหนึ่ง note
- [ ] มีลิงก์ออกอย่างน้อย 1
- [ ] อยู่ในโฟลเดอร์ที่ถูกต้อง
- [ ] `updated` เป็นวันนี้

## เกี่ยวข้อง

- [[hermes-wiki-persona]]
- [[main-hub]]
- [[system-moc]]
