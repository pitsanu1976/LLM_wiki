---
title: Obsidian สำหรับ LLM Wiki
type: howto
status: active
created: 2026-10-19
updated: 2026-10-19
tags:
  - domain/tech
  - topic/llm
  - topic/knowledge-base
  - topic/obsidian
aliases:
  - Obsidian + LLM wiki
  - ตั้งค่า Obsidian สำหรับ agent
---

# Obsidian สำหรับ LLM Wiki

**ประโยคเดียว:** Obsidian ไม่ใช่ "เครื่องมือทำ wiki" แต่เป็น **หน้าจออ่าน** ของ wiki
ที่ agent เขียน — รูปแบบไฟล์ที่มันอ่าน (markdown + YAML + `[[wikilink]]`) คือรูปแบบเดียวกับที่ LLM เขียนอยู่แล้ว
จึงไม่ต้อง import/export อะไรเลย

## ทำไมมันเข้ากันได้พอดี

| LLM ต้องการ | Obsidian ให้ |
|---|---|
| ไฟล์ข้อความที่แก้ได้ด้วยเครื่องมือพื้นฐาน | markdown ธรรมดาในโฟลเดอร์ |
| โครงสร้างที่ query ได้ | YAML frontmatter (Dataview) |
| กราฟความสัมพันธ์ | Graph View + Backlinks |
| ประวัติการเปลี่ยนแปลง | ไฟล์อยู่ใน git ได้ตรง ๆ |
| ที่อ่านคำตอบ | เปิดหน้าได้ทันที รวมถึง Marp/รูป |

## setup จริงของ Karpathy

จากโพสต์ X (เม.ย. 2026) — เขาแยกเป็น 3 ส่วน:

**1. Data ingest** — ใช้ **Obsidian Web Clipper** แปลงบทความเว็บเป็น `.md`
แล้วกด hotkey "Download attachments for current file" ให้รูปถูกโหลดมาเก็บในเครื่อง
เพื่อให้ LLM อ้างอิงรูปได้จริง ไม่ใช่พึ่ง URL ที่อาจตาย

**2. IDE** — ใช้ Obsidian เป็น frontend ดู raw data, wiki ที่ compile แล้ว, และ visualization
ที่สร้างเพิ่ม — "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase"

**3. Output** — ให้ LLM สร้าง markdown, สไลด์ Marp, หรือกราฟ matplotlib แล้วกลับมาดูใน Obsidian
แทนที่จะอ่านคำตอบใน terminal

## Plugin stack ที่คนใช้จริงตรงกัน

| Plugin | บทบาท | จำเป็นไหม |
|---|---|:--:|
| **Dataview** | query frontmatter เป็นตาราง (dashboard, หน้าที่ค้างแก้) | แนะนำ |
| **Templater** | สร้างหน้าจาก template ด้วยคีย์ลัด | แนะนำ |
| **Linter** | บังคับลำดับ frontmatter/heading ให้สม่ำเสมอ | แนะนำเมื่อ agent เขียน |
| **Web Clipper** | เก็บแหล่งจากเว็บเข้า vault | ถ้า ingest จากเว็บ |
| **Marp** | สไลด์จาก markdown ใน wiki | ทางเลือก |
| **Git** | version control ในตัว | แนะนำ |
| **Smart Connections / Omnisearch** | ค้นเชิงความหมาย / full-text เร็ว | ทางเลือก |
| **obsidian-mcp-tools** | เปิด vault ให้ agent ผ่าน MCP | ทางเลือก |

มี plugin สำเร็จรูปที่ทำ ingest/query/lint ในตัว (เช่น *Auto LLM Wiki*, *Karpathy LLM Wiki*)
— สะดวก แต่ผูก workflow ไว้กับ plugin ตัวนั้น

## ตั้งค่า Graph View ให้อ่านออก

```
View → Graph View → Display
  Arrows               ✅   เห็นทิศทางลิงก์
  Existing files only  ✅   ซ่อนลิงก์ที่ยังไม่มีหน้า
  Color groups:
    tag:#entities  → ฟ้า
    tag:#concepts  → เขียว
    tag:#sources   → เหลือง
```

"Existing files only" สำคัญมาก — มันแยก **ลิงก์ที่ยังไม่ได้เขียน** (ghost node) ออกจากกราฟจริง

## Sync เมื่อ agent อยู่บน server

ถ้า agent เขียน vault บน VPS แต่คุณเปิด Obsidian บน laptop มี 2 ทาง:

**ก. git (ฟรี, แนะนำสำหรับ vault ที่เป็นข้อความล้วน)**
agent commit + push → เครื่องคุณ `git pull` เป็นระยะ
ข้อดี: ประวัติครบ, ตรวจ diff ได้, ไม่มีค่าใช้จ่าย

**ข. Obsidian Headless (`ob`) — อย่างเป็นทางการ**
เปิดตัว ก.พ. 2026, ต้องมี Node.js 22+ และ **subscription Obsidian Sync**

```bash
npm install -g obsidian-headless
ob login
ob sync-setup --vault "My Vault"
ob sync --continuous          # เฝ้าไฟล์และ sync ตลอด
```

> [!warning] ห้ามใช้สองวิธี sync บนเครื่องเดียวกัน
> เอกสาร Obsidian ระบุชัดว่า **ห้ามใช้ desktop Sync กับ Headless Sync พร้อมกันบนเครื่องเดียว**
> เพราะจะเกิด conflict — เลือกอย่างใดอย่างหนึ่งต่อเครื่อง

## กับดัก 5 ข้อ

1. **Plugin ที่แก้อัตโนมัติตอน save (Linter) แข่งกับ agent** — ถ้า agent เขียนไฟล์แล้ว Linter
   reformat ทันที diff จะรกและ conflict ง่าย ปิด "lint on save" ถ้า agent เป็นคนเขียนหลัก
2. **Graph สวยไม่เท่ากับ wiki ดี** — กราฟที่ดูแน่นอาจเต็มไปด้วยลิงก์ไปหน้าที่ไม่มีจริง
   เช็คด้วย "Existing files only" ก่อนภูมิใจ
3. **Dataview ทำงานตอนเปิดแอป** — ไม่ใช่ตอน agent เขียน agent จึงใช้ Dataview เพื่อ "ตรวจสอบ" ไม่ได้
   ต้องมี script ตรวจฝั่ง filesystem แยก
4. **Sync สองทางพร้อมกัน = conflict** — ดูกฎข้างบน และหลีกเลี่ยงการแก้ไฟล์เดียวกันจากสองเครื่อง
5. **เชื่อ plugin มากเกินไป** — สิ่งที่ทำให้ wiki ทำงานคือ *วินัยของ frontmatter + ลิงก์* ไม่ใช่ plugin
   vault ที่ไม่มี plugin เลยยังใช้ได้ แต่ vault ที่ frontmatter มั่วจะเน่าไม่ว่าติด plugin อะไร

## กรณีของ vault นี้

vault ที่คุณกำลังอ่านอยู่เลือกแบบ **ไม่มี plugin** โดยตั้งใจ:

| เรื่อง | ที่ทำ |
|---|---|
| sync | git + `auto-push.sh` (ไม่ใช้ Obsidian Sync) |
| ตรวจสุขภาพ | `check-vault.py` (ลิงก์/frontmatter) + `check-policy.py` (สิทธิ์ agent) |
| ตรวจซ้ำ | รันบน filesystem ไม่พึ่ง Dataview |
| เจ้าของการเขียน | agent แยกตามโฟลเดอร์ ดู [[agent-access-policy]] |

เหตุผล: ทุกอย่างต้องรันได้บน VPS แบบ headless และตรวจได้ด้วยคำสั่งเดียว
ถ้าจะเพิ่ม Dataview ภายหลัง มันจะเป็น *ชั้นอ่าน* ไม่ใช่ชั้นเขียน

## ที่มา

- Karpathy, ["LLM Knowledge Bases"](https://x.com/karpathy/status/2039805659525644595) (X, เม.ย. 2026)
- Karpathy, [llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — §Tips and tricks
- [Obsidian Headless Sync](https://obsidian.md/help/sync/headless) — เอกสารทางการ
- [obsidianmd/obsidian-headless](https://github.com/obsidianmd/obsidian-headless) — repo
- คู่มือ integration ของ implementation ต่าง ๆ (llmwiki, llm-wiki-blueprint, obsidian-llm-wiki)

## เกี่ยวข้อง

- [[llm-wiki-pattern]] — ตัว pattern ที่ Obsidian มาทำหน้าที่เป็นหน้าจอ
- [[2026-karpathy-llm-wiki]] — ต้นทางแนวคิด
- [[llm-wiki-vs-rag]] — ทำไมต้อง compile ไม่ใช่ retrieve
- [[wiki-formatting-guide]] — กฎการเขียนที่ทำให้ vault นี้ค้นได้
