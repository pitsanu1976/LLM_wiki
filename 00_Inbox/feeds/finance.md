---
title: "finance.md"
type: source
status: active
agent: leader
created: 2026-11-03
updated: 2026-11-03
tags:
  - source/feed
  - domain/trading
related:
  - "[[trading-finance-moc]]"
source: "workspace/raw/finance.md"
---

> 🔁 สำเนาอัตโนมัติจาก `workspace/raw/finance.md` (sync 2026-11-03) — ต้นฉบับที่ทีมใช้อยู่ใน workspace
> Finance feed — งบ/valuation ของ finance desk

# raw/finance.md — Finance Agent Output (schema v2)

- สร้างเมื่อ: 2026-11-01 10:05 UTC · **ปรับ schema เป็น v2: 2026-11-01 10:20 UTC** · ราคาอ้างอิง: ปิด **Fri 2026-10-30 16:00 ET**
- แหล่งข้อมูล: stockanalysis.com (statistics / balance sheet, ดึง 2026-11-01 10:03–10:25 UTC) — fundamental เป็น **TTM ถึงงวดล่าสุดที่รายงาน**
- อ่านต้นทาง: `raw/news.md` (สแกน 2026-11-01 09:57–10:02 UTC) · news_id ครบ 5 รายการ · improve_id ใน news.md = `—` ทั้งหมด
- หลักการ: ทุกช่องเป็น **ดึงมา (D)** หรือ **คำนวณ (C)** · ไม่มีตัวเลขใดเขียนจากความจำ

| finance_id | refer improve_id | finance_date | news_id | stock | period | D/E | net debt/EBITDA | quick ratio | ROE | ROA | PE | PBV | EV/EBITDA | FCF margin | interest coverage | one-off impact | scoring (1-10)[10 recommend buy, 1 recommend sell, 5 hold] |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FIN-20261101-01 | — | 2026-11-01 | NEWS-20261030-01 | REGN | TTM Q3-2026 (งบ 30 ต.ค. 2026, unaudited) | 0.08 (D) | −2.86x = net cash (C) | 2.72 (D) | 14.95% (D) | 7.59% (D) | 20.54 / fwd 11.87 (D) | 2.78 (D) | 13.63 (D) | 22.65% (D) | 109.93 (D) | +$1.0B Sanofi upfront เข้า Q4'26 — ยังไม่รวมใน TTM | 8 |
| FIN-20261101-02 | — | 2026-11-01 | NEWS-20261030-02 | GDDY | TTM Q3-2026 (งบ 29 ต.ค. 2026, unaudited) | n/a — equity −$138.8M (D) | 1.87x (C) | 0.40 (D) | n/a — equity ติดลบ (D) | 10.62% (D) | 16.11 / fwd 13.30 (D) | n/a — BVPS −$1.13 (D) | 11.84 (D) | 33.66% (D) | 8.99 (D) | ยังแยกไม่ได้จากเอกสารที่ดึงได้ | 7 |
| FIN-20261101-03 | — | 2026-11-01 | NEWS-20261030-03 | CROX | TTM Q3-2026 (งบ 29 ต.ค. 2026, unaudited) | 1.24 (D) | 1.49x (C) | 0.77 (D) | 49.06% (D) | 13.54% (D) | 11.30 / fwd 9.52 (D) | 5.17 (D) | 8.29 (D) | 18.38% (D) | 11.51 (D) | −$64.1M tariff refund (IEEPA) อยู่ใน GM Q3'26 = 60.3% | 8 |
| FIN-20261101-04 | — | 2026-11-01 | NEWS-20261030-04 | TMUS | TTM Q3-2026 (งบ 28 ต.ค. 2026, unaudited) | 2.11 (D) | 3.21x (C) | 0.68 (D) | 19.35% (D) | 6.19% (D) | 15.13 / fwd 11.47 (D) | 2.95 (D) | 7.89 (D) | 19.88% (D) | 5.16 (D) | ไม่พบรายการใหญ่ในเอกสารที่ดึงได้ | 7 |
| FIN-20261101-05 | — | 2026-11-01 | NEWS-20261030-05 | FDXF | TTM ถึง 4 เดือนสิ้นสุด 2026-09-30 (ปน pre-spin, unaudited) | n/a — equity −$497M (D) | 6.18x (C) | 1.41 (D) | 69.09% (D) — บิดเบือนจาก equity ติดลบ | 5.67% (D) | 28.78 / fwd 25.61 (D) | n/a — BVPS −$3.32 (D) | 25.24 (D) | −2.41% (C; แหล่งให้ n/a) | 9.47 (D) | pretax $884M > EBIT $540M ⇒ non-op +$344M ยังไม่ทราบที่มา | 3 |

## หมายเหตุท้ายตาราง (ที่มา / งวด / วิธีคำนวณ / ข้อจำกัด)

**เปลี่ยนจาก v1 → v2 (11 → 18 คอลัมน์)**
- เพิ่ม `period` — v1 ไม่มี ทำให้ FDXF (งวด 4 เดือน) ถูกเทียบกับตัวอื่นแบบผิดงวดโดยไม่มีอะไรเตือน
- เพิ่ม `net debt/EBITDA` วางติดกับ D/E — ใช้ได้แม้ equity ติดลบ (เคส GDDY/FDXF)
- เปลี่ยน `current ratio` → `quick ratio` (current ratio เก็บไว้ในหมายเหตุ) เพราะสต็อกทำให้ภาพเพี้ยน: CROX current 1.44 แต่ quick 0.77
- เพิ่ม `FCF margin` (คุณภาพกำไร), `interest coverage` (ความเสี่ยงหนี้), `one-off impact` (แยกของพิเศษก่อนใช้ PE ตัดสิน)
- คง `EV/EBITDA` เป็นตัวเทียบ valuation หลักเมื่อ PBV ใช้ไม่ได้

**งวดของตัวเลขทุกตัว**
- REGN · GDDY · CROX · TMUS: TTM ถึง **Q3-2026** (REGN 30 ต.ค. · GDDY 29 ต.ค. · CROX 29 ต.ค. · TMUS 28 ต.ค. 2026) — **ยังไม่ตรวจสอบ (unaudited)**
- FDXF: TTM ถึงงวด **4 เดือนสิ้นสุด 2026-09-30** (29 ต.ค. 2026, unaudited) — TTM ปนงวด pre-spin/carve-out ⇒ เทียบปีก่อนไม่ตรงงวด

**วิธีคำนวณ (C)**
- Net debt = EV − mcap: REGN **−16.15B (net cash)** · GDDY +2.68B · CROX +1.50B · TMUS +113.37B · FDXF +6.11B
- Net debt/EBITDA = net debt ÷ EBITDA (EBITDA เป็น D): REGN −16.15/5.65 · GDDY 2.68/1.43 · CROX 1.50/1.01 · TMUS 113.37/35.36 · FDXF 6.11/0.989
- PE = ราคาปิด 2026-10-30 ÷ EPS TTM: 927.89/45.17 · 117.24/7.28 · 150.52/13.32 · 156.44/10.34 · 126.04/4.38
- PBV (D จากแหล่ง; ตรวจกับ mcap÷equity แล้วใกล้เคียง): REGN 33.50B · CROX 1.35B · TMUS 56.31B — ส่วน GDDY/FDXF equity ติดลบ
- FDXF FCF margin = −212 ÷ 8,800 = −2.41% (แหล่งให้ n/a เพราะ FCF ติดลบ) · GDDY ใช้ค่าที่แหล่งรายงาน 33.66% (คำนวณจากเลขปัดได้ 33.59%)

**D/E, ROE, PBV ที่ใช้ไม่ได้ (equity ติดลบ — ไม่ใช่ขาดทุน แต่มาจาก buyback/โครงสร้างทุน)**
- GDDY: equity −$138.8M, BVPS −1.13, working capital −$1.23B (deferred revenue) ⇒ ใช้ net debt/EBITDA 1.87x, FCF $1.74B, ROIC 28.66%, coverage 8.99 แทน
- FDXF: equity −$497M, BVPS −3.32 ⇒ ROE 69.09% เป็นผลหารด้วย equity ติดลบ ไม่ใช่ผลตอบแทนจริง; ใช้ ROA 5.67%, ROIC 7.56%, net debt/EBITDA 6.18x แทน

**current ratio (คงไว้ในหมายเหตุ)**: REGN 3.35 · GDDY 0.61 · CROX 1.44 · TMUS 0.91 · FDXF 1.52

**หนึ่งครั้งพิเศษ (one-off)**
- CROX: adjusted GM +180bp มี tariff refund (IEEPA) **$64.1M** เป็นส่วนหนึ่ง (29 ต.ค. 2026) ⇒ กำไรปกติต่ำกว่า headline; GM ที่ยั่งยืนควรต่ำกว่า 60.3%
- FDXF: pretax $884M > EBIT $540M ⇒ net non-operating **+$344M** ใน TTM (เอกสารที่ดึงได้ไม่ระบุที่มา) ⇒ กำไร TTM อาจพองจากรายการครั้งเดียว — ต้องอ่าน 10-Q ก่อนใช้ PE 28.78 เป็นตัวตัดสิน
- REGN: upfront **$1.0B** เข้า Q4'26 ⇒ fwd PE 11.87 ต่ำกว่า trailing 20.54 เพราะ EPS ที่ยังไม่เกิดจริง
- GDDY / TMUS: ไม่พบรายการมีนัยสำคัญในเอกสารที่ดึงได้ (แปลว่า "ยังไม่พบ" ไม่ใช่ "ยืนยันว่าไม่มี")

**การให้คะแนน (view ไม่ใช่คำสั่งซื้อขาย)**
- เกณฑ์: งบแข็งแรง (net debt/EBITDA, coverage, quick) 40% · คุณภาพกำไร+ผลตอบแทน (FCF margin, ROE/ROA/ROIC หัก one-off) 35% · valuation (PE/PBV/EV-EBITDA) 25%
- REGN 8 · CROX 8 · GDDY 7 · TMUS 7 · **FDXF 3 — ปรับลงจาก v1 (4) เพราะข้อมูลใหม่: net debt/EBITDA 6.18x สูงสุดในกลุ่ม + FCF margin −2.41% + TTM ปนงวด pre-spin** (ถ้าต้องการคงสเกลเดิม ย้อนเป็น 4 ได้)
- valuation ถูกสุดเมื่อหักความเสี่ยง: CROX (PE 11.30, EV/EBITDA 8.29, FCF margin 18.38%) · งบแข็งสุด: REGN (net cash, coverage 109.93)

**ข้อมูลที่ดึงไม่ได้ / ข้อจำกัด**
- peer set ที่ยืนยันตัวเลขได้: **ยังไม่มีในรอบนี้** ⇒ ยังไม่เทียบ peers (ไม่เปรียบกับ "อุตสาหกรรม" ลอย ๆ)
- FDXF: ที่มาของ non-operating +$344M · P/FCF และ EV/FCF = n/a ที่แหล่ง (FCF ติดลบ) · ประวัติซื้อขายสั้น
- GDDY / FDXF: P/TBV ก็ n/a (tangible book ติดลบ) — ใช้ EV/EBITDA แทนการตีความ PBV
