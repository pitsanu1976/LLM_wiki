---
title: "LLM Wiki — Karpathy (2026)"
type: source
status: active
created: 2026-10-19
updated: 2026-10-19
source_date: 2026-04-04
source: Andrej Karpathy (GitHub Gist)
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
tags:
  - source/article
  - domain/tech
  - topic/llm
  - topic/knowledge-base
aliases:
  - Karpathy llm-wiki
  - llm-wiki.md
---

# LLM Wiki — Karpathy (2026)

> **แหล่ง:** Andrej Karpathy, "LLM Wiki — A pattern for building personal knowledge bases using LLMs"
> GitHub Gist — สร้าง 4 เมษายน 2026 (5,000+ stars ณ ต.ค. 2026)
> <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>

## สาระสำคัญ

Karpathy เสนอทางเลือกแทน RAG: แทนที่จะให้ LLM ดึง chunk จากเอกสารดิบทุกครั้งที่ถาม
ให้ LLM **ค่อย ๆ สร้างและดูแล wiki ของ markdown ที่เชื่อมกัน** ซึ่งวางอยู่ระหว่างผู้ใช้กับเอกสารต้นทาง

> "The knowledge is compiled once and then kept current, not re-derived on every query."

จุดต่างหลักคือ wiki เป็น **artifact ที่สะสมพอกพูน** (persistent, compounding) —
cross-reference มีอยู่แล้ว, contradiction ถูกตั้งธงไว้แล้ว, synthesis สะท้อนทุกอย่างที่อ่านมาแล้ว

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

## สามชั้นสถาปัตยกรรม

| ชั้น | คืออะไร | ใครowns |
|---|---|---|
| **Raw sources** | เอกสารต้นทาง (บทความ, paper, รูป, data) — **แก้ไม่ได้** | มนุษย์คัดเลือก |
| **The wiki** | หน้า markdown ที่ LLM สร้าง (summary, entity, concept, comparison, synthesis) | LLM |
| **The schema** | เอกสารบอกกติกา เช่น `CLAUDE.md` / `AGENTS.md` — ingest/query/lint อย่างไร | มนุษย์ + LLM ร่วมกัน |

Karpathy เน้นว่า **schema คือไฟล์คอนฟิกที่สำคัญที่สุด** — มันคือสิ่งที่ทำให้ LLM
เป็น "ผู้ดูแล wiki ที่มีวินัย" ไม่ใช่ chatbot ทั่วไป

## สามOperation

- **Ingest** — วางแหล่งใหม่แล้วสั่งประมวลผล: LLM อ่าน → คุยประเด็นสำคัญ → เขียนหน้า summary
  → อัปเดต index → อัปเดตหน้า entity/concept ที่เกี่ยวข้อง → append log
  **หนึ่งแหล่งอาจแตะ 10–15 หน้า**
- **Query** — ถามคำถามกับ wiki, LLM หาหน้าที่เกี่ยวข้อง อ่าน แล้วสังเคราะห์คำตอบพร้อม citation
  คำตอบที่ดี**ถูกเก็บกลับเข้า wiki เป็นหน้าใหม่** (คำถามก็ทำให้ wiki โต)
- **Lint** — ตรวจสุขภาพเป็นระยะ: contradiction, claim ที่ล้าสมัย, orphan page,
  concept ที่ถูกพูดถึงแต่ยังไม่มีหน้า, cross-reference ที่ขาด, ช่องว่างข้อมูล

## ไฟล์นำทาง 2 ตัว

- **`index.md`** — catalog เชิงเนื้อหา ทุกหน้ามีลิงก์ + สรุปหนึ่งบรรทัด จัดกลุ่มตามประเภท
  ใช้ตอนตอบคำถาม: อ่าน index ก่อนแล้วเจาะหน้า
- **`log.md`** — บันทึกตามเวลา append-only ใช้ prefix คงที่ เช่น `## [2026-04-02] ingest | ชื่อ`
  ทำให้ `grep "^## \[" log.md | tail -5` ใช้งานได้

Karpathy ระบุว่า index แบบนี้ **พอใช้ได้ถึงระดับ ~100 แหล่ง / หลายร้อยหน้า**
โดยไม่ต้องมี embedding RAG เลย

## ทำไมมันถึงได้ผล

> "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping."

มนุษย์เลิกทำ wiki เพราะภาระการดูแลโตเร็วกว่าคุณค่า — LLM ไม่เบื่อ ไม่ลืมอัปเดต cross-reference
และแตะ 15 ไฟล์ในรอบเดียวได้ ต้นทุนการดูแลจึงเกือบเป็นศูนย์

เชื่อมโยงเชิงแนวคิดกับ **Memex ของ Vannevar Bush (1945)** — คลังความรู้ส่วนตัว
ที่ "เส้นทางเชื่อมโยง" ระหว่างเอกสารมีค่าเท่ากับตัวเอกสาร สิ่งที่ Bush แก้ไม่ได้คือ "ใครจะดูแลมัน" — LLM ตอบโจทย์นั้น

## ลักษณะของเอกสาร

Karpathy เน้นว่าเอกสารนี้**จงใจเป็นนามธรรม** — เป็น "idea file" ที่เอาไปวางให้ agent
แล้วให้ agent สร้าง implementation ให้เข้ากับโดเมนของผู้ใช้ ไม่ใช่ซอฟต์แวร์สำเร็จรูป
ทุกอย่างเป็น optional และ modular

## คำถามเปิด / ข้อจำกัด (จากความเห็นใน gist, ก.ย.–ต.ค. 2026)

- **"agent จะรู้ได้อย่างไรว่าตัวเองลืมอะไรไว้?"** — การ retrieve ดีไม่ได้แปลว่าจะมีการเปิดดู
  มีการตรวจ 9 session จริงพบว่า agent อ่าน wiki ตอนเริ่มงาน แต่**ไม่เปิดกลางงาน**
  และมี 2 session ที่วินิจฉัยปัญหาใหม่ทั้งที่ wiki มีบทเรียนนั้นอยู่แล้ว
  → ต้องมี *trigger* ที่เป็นรูปธรรมใน schema ไม่ใช่แค่ "เปิดดูเมื่อเกี่ยวข้อง"
- **token ส่วนใหญ่หมดไปกับการตัดสินใจ ไม่ใช่การเขียน** — มีรายงานว่า ~72% ของ token
  ตอน ingest ใช้ไปกับการเลือกว่าจะเก็บโฟลเดอร์ไหน, ซ้ำกับ note เดิมไหม, จะ merge หรือไม่
  การแยกงานตัดสินใจไปให้ classifier เล็ก ๆ ช่วยได้ (รายงานความแม่นยำ 62% → 89% บน 525 เอกสาร)
  — **ตัวเลขนี้มาจากคลังข้อมูลเดียวและโมเดลเดียว ยังไม่ควรถือเป็นข้อสรุปทั่วไป**

## เนื้อหาที่แตกออก

- [[llm-wiki-pattern]] — ตัว pattern ในฐานะแนวคิด
- [[llm-wiki-vs-rag]] — เทียบกับ RAG ตรง ๆ
