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
_ยังไม่มี — ดูแหล่งข่าวในหัวข้อ "แหล่งข้อมูล" ด้านล่าง_
<!-- agent:news:end -->

## 📈 Technical
<!-- agent:tech:begin -->
**1D · close 2026-10-22 = 521.08 (−2.23%, vol 0.99× avg20)** — ใต้ MA20 526.29 **−0.99%**, เหนือ MA50 507.88 **+2.60%**, เหนือ MA200 436.31 +19.43% · RSI14 **50.50** (จาก 58.93) · MACD hist **−1.908** (แย่ลงจาก −0.920) · ATR14 11.37 (2.18%)
**Trend: ขาขึ้น ไม่ชัด** — MA เรียงขึ้นและ slope บวก (MA20 +18.16 / MA50 +9.11 ต่อ 10 แท่ง) แต่ราคาหลุด MA20 ตั้งแต่ 10-16
**ระดับ:** ต้าน 526.29 (MA20) · 533.60 (high 10-22) · 551.15 (swing high 10-13) / รับ 520.30 (low 10-22) · **507.88 (MA50)** · 486.00 (swing low 09-10)
**หมายเหตุ:** stop พอร์ต 515 อยู่ *เหนือ* MA50 507.88 ⇒ stop จะถูกแตะก่อนแนวรับจริง
เต็ม: [[DAILY-US_tech_2026-10-22]]
<!-- agent:tech:end -->

## 💰 Financial
<!-- agent:finance:begin -->
**งบล่าสุด:** TTM ถึง **Q4 FY26 (Jun-26)** — รายได้ $331.84B · NI $133.75B · GM 67.20% (จาก 69.05% เมื่อ 3 ไตรมาสก่อน) · OM 45.11% (stockanalysis, ดึง 2026-10-25)
**Valuation (ปิด 2026-10-23 ราคา $524.51):** P/E **29.2** (524.51 ÷ EPS TTM 17.959) · fwd 26.54 · median P/E 5y **31.6** ⇒ ต่ำกว่า median 7% · EV/EBITDA 20.32 · FCF yield 1.72% · D/E 0.29 · net debt **$51.97B** (จาก $18.36B เมื่อ 3 ไตรมาสก่อน)
**จับตา:** งบ **2026-10-28 หลังปิด** (Nasdaq calendar) — ATM straddle 30 ต.ค. **5.28%** ของ spot, strip event แล้ว **σ 3.90% / expected |move| 3.12%** ⇒ **stop 515 ห่าง spot เพียง 1.81% = 0.43–0.58 เท่าของ move ที่ตลาด price** · one-off gainInvestments +$4,830M = 13.5% ของ NI Q4 FY26 · XD ถัดไป **2026-11-19**
เต็ม: [[DAILY_2026-10-26_fin]] · [[MSFT_fin_2026-Q4]]
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
