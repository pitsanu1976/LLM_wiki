---
title: MSFT
type: moc
status: active
ticker: MSFT
agent: leader
created: 2026-10-19
updated: 2026-10-25
tags:
  - moc
  - ticker/MSFT
related:
  - "[[NVDA]]"
  - "[[2026-10-21]]"
  - "[[2026-10-22]]"
  - "[[2026-10-25-week1-trade-journal]]"
  - "[[decisions]]"
aliases:
  - MSFT
---

# MSFT

> สร้างจาก [[stock-hub-template]] — Leader เติม Snapshot และ Decision block
> block ข่าว/เทคนิค/งบ จะถูกเติมโดย agent เจ้าของในรอบถัดไป

## Snapshot

| | |
|---|---|
| Sector | Software — cloud / AI infrastructure (Azure + Copilot) |
| Watchlist status | **ถือ 16 หุ้น** @526.158125 · stop 8+8 @515 · TP 8@545 / 8@553.72 |
| ความเห็นล่าสุด | ไม้เดียวที่เหลือ · uPL −$26.37 ที่ 524.51 (2026-10-25) · **ต้องเลือกก่อน 27 ต.ค. 20:00 UTC** ว่าจะถือเต็ม 16 หรือลดเหลือ 8 ก่อนงบ 28 ต.ค. |

## 📰 News
<!-- agent:news:begin -->
**2026-10-29 (ปิด 530.14, −0.16%, SIP consolidated, ดึง 22:36Z) — gap 543.56 หลังงบหายหมดระหว่างวัน** · AH 22:21Z = **528.97** (hi 532.91 / lo 524.15)
**เหตุผลที่ระบุได้:** (ก) แผนออกหุ้นกู้ **$25B** มีดีมานด์ล้น (Bloomberg 29 ต.ค.) ⇒ ตลาดเริ่มคิดต้นทุนทุนของ AI buildout กับ MSFT (ข) ตลาดโฟกัส capex เร่งใน **2H FY27** (William Blair: Q2 >$50B + component inflation) (ค) commercial bookings **−11% cc**
**Analyst หลังงบ:** BofA คง Buy ขึ้น TP **$630** (จาก 600) · Jefferies คง Buy TP **$650** (แหล่งทุติยภูมิ = สื่อสรุป brokernote)
**XD ปันผล: 2026-11-19 $0.98/หุ้น** (declared 2026-09-15, record 11/19, pay 12/10 — Nasdaq dividends API) ⇒ อยู่ในกรอบถือ ต้องไม่ตีความราคาที่ถูกหักว่าเป็นขาดทุน
**Sentiment: Neutral (narrow)** — งบแข็ง (Azure +48%, RPO $677B) แต่การก่อหนี้ + capex 2H ทำให้ multiple ไม่ได้ต่อ
ที่มา: Invezz 2026-10-29 · Proactive/Yahoo 2026-10-29 · Bloomberg wrap 29 ต.ค. · Alpaca SIP bars — รายงานเต็ม `workspace/reports/news/2026-10-30-DAILY.md`
<!-- agent:news:end -->

## 📈 Technical
<!-- agent:tech:begin -->
**ปิด 2026-10-28 $531.01** (SIP) · **AH trade 543.64 @ 2026-10-28T20:54:32Z (+2.38%)** — quote 20:08Z (554/556) ขัดกับ trade ⇒ ใช้ไม่ได้ · trend 1D **ขึ้น (ไม่ชัด) sideways 515–551 ตั้งแต่ 13 ต.ค.**: MA20 529.90 +0.21% / MA50 511.18 +3.88% / MA200 437.32 +21.42%
RSI14 **56.06** · MACD hist **−1.78** (ทรงตัวที่ลบ) · ATR14 **10.80 (2.03%, ก่อนงบ)** — หลังงบคำนวณได้ ≈ **11.24–12.17** · vol **1.40×** MA20
**gap ถ้าเปิด ~543.64: 535.00 → 543.64 (1.61%), gap fill = 535.00** · แนวรับ 529.90 (MA20) / **526.13 (10-28)** / 521.69 / 520.30 · แนวต้าน **551.15 (10-13)** / 553.72 / **555.45 (ATH)**
**บันได stop (trigger = แท่งปิด 1D):** ปิด ≥543.64 → ยกเป็น **525.50** (risk $10.53) · ปิด ≥551.15 → ยกเป็น **535.00** (ล็อกกำไร $141.47) · ปิด <526.13 → gap ล้ม คง **515** (ใต้ 515.70 10-23)
**TP:** 8 @545 อยู่เหนือ AH แค่ 0.25% ⇒ จะ fill ที่เปิด — ทางเลือก แยก 4@545 + 4@551.15 (แนะนำ) · TP2 8@553.72 ใต้ ATH 0.31% ⇒ ไม่คุ้มเลื่อน
เต็ม: [[DAILY-US_tech_2026-10-28]]
<!-- agent:tech:end -->

## 💰 Financial
<!-- agent:finance:begin -->
**งบล่าสุด:** **Q1 FY27 (ไตรมาสสิ้นสุด 2026-09-30) — งบออกแล้ว 2026-10-28**, 8-K EX-99.1 + 10-Q ยื่นวันเดียวกัน, unaudited: รายได้ **$92,279M +19%** · OI **$45,900M +21%** · NI **$36,600M +32% (non-GAAP $36,400M +18%)** · EPS **$4.92 / $4.89** · Azure **+48%** · Commercial RPO **$677B +73%** · OCF $58,000M · cash capex **$39,367M** · **FCF $18,633M**
**Valuation (ปิด 2026-10-28 ราคา ~$530.3):** P/E **27.73** (530.3 ÷ EPS TTM 19.15) · fwd 26.03 · core P/E (กำไรดำเนินงานอย่างเดียว สมมติฐานภาษี 21%) **~30.6** · median P/E 5y **31.5** ⇒ ต่ำกว่า 12% · EV/EBITDA 19.13 · **FCF yield 1.5% (P/FCF 65.8)** · net cash **+$7.31B** · D/E 0.12 · interest coverage 53.0
**จับตา:** **capex = 42.7% ของรายได้ ทำให้ FCF TTM $59.96B ต่ำกว่า FY2024 ($74.07B) 19.1%** — นี่คือตัวจำกัด upside มากกว่า P/E · ยังยืนยันไม่ได้: guidance Q2 Azure 49–50% (อยู่ใน call 21:30 UTC ไม่ได้อยู่ใน PR) และ capex $45.2B ที่ news อ้าง (งบแสดง $39.367B) · XD **2026-11-19 $0.98** จ่าย 12-10 (16 หุ้น = $15.68 ก่อนภาษี) · มุมพื้นฐาน: **ถือต่อได้ด้วยเหตุผลกำไรโต ไม่ใช่ความถูก** (core P/E 30.6 ใกล้ median 5y)
เต็ม: [[DAILY_2026-10-29_fin]] · [[MSFT_fin_2026-Q4]]
<!-- agent:finance:end -->

## 👑 Decision
<!-- agent:leader:begin -->
### 2026-10-21 — BUY 16 @526.158125 (limit 527, partial fill 16/18)
- เหตุผล: setup ดีสุดของรอบ — R:R T2 2.23 · stop 1.05×ATR · MA20 > MA50 > MA200 เรียงขึ้น · P/E 29.6 ไม่มี one-off · spread 12.8bp = 2.6% ของ risk
- ขนาด 18 หุ้น = $9,486 (ครึ่งไม้ เพราะงบ 28 ต.ค.) · risk $216
- บันทึก: [[2026-10-21]]

### 2026-10-22 — Rework legs เป็น OCO 2 ชุด
- ปัญหา: legs 18 หุ้น vs position 16 ⇒ oversell 2 หุ้นถ้า stop ทำงาน
- แก้: ยกเลิก bracket เดิม → **OCO A** 8 @553.72 + **OCO B** 8 @545 ทั้งคู่ stop **515** (ครอบ 16 หุ้นพอดี)
- บันทึก: [[2026-10-22]]

### สถานะปัจจุบัน (2026-10-25)
- ถือ **16 หุ้น** @526.158125 · ราคา 524.51 · **uPL −$26.37 (−0.15R)**
- stop **8+8 @515** (`held`) · TP **8 @545** / **8 @553.72** (`new`) · risk $178.53 (0.18% equity)
- **⏰ deadline 27 ต.ค. 20:00 UTC:** A ถือเต็ม 16 / **B ลดเหลือ 8 (leader แนะนำ)** / C ออกหมด — งบ 28 ต.ค.
<!-- agent:leader:end -->

## แหล่งข้อมูล

- [[DAILY-US_tech_2026-10-19]] — technical (รวมหลาย ticker)
- [[MSFT_fin_2026-Q4]] — งบการเงิน

## เกี่ยวข้อง

- [[trading-finance-moc]]
- [[agent-access-policy]]
