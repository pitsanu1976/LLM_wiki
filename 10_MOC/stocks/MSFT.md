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
**2026-11-02 (ปิด 507.12, −2.83%, SIP consolidated 21:00 UTC ดึง 22:36Z)** · 1W −4.78% · 1M −2.01% · ATR14 **2.52%** (ต่ำสุดในธีม)
**ไม่มี earnings ในกรอบถือ** (งบถัดไป ~ก.พ. 2027) · **XD ปันผล 2026-11-19 $0.98** (declared 2026-09-15, pay 12/10, Nasdaq dividends API) = หักราคา ~0.19% แบบกลไก ไม่ใช่ sentiment
**คะแนนแคทาทิสต์ N = 4/10** — ต่ำเป็นอันดับสองในลิสต์ เพราะไม่มีวันนัดในกรอบ + เป็นฝ่ายจ่าย capex ที่ตลาดกำลังลงโทษ (1D −2.83% แรงกว่าดัชนี)
**Sentiment: Bearish ระดับธีม / Neutral-narrow เฉพาะตัว** — งบ 28 ต.ค. แข็ง (Azure +48%, RPO $677B) แต่การก่อหนี้ $25B + capex 2H FY27 กด multiple
ที่มา: Alpaca SIP bars 2026-11-02 · Nasdaq dividends API 2026-11-02 — รายงานเต็ม `workspace/reports/news/2026-11-03-DAILY.md` · คะแนน `workspace/reports/news/2026-11-03-DAILY-scores.md`
<!-- agent:news:end -->

## 📈 Technical
<!-- agent:tech:begin -->
## เทคนิคัล (อัปเดต 2026-11-04, ข้อมูลถึงปิด 2026-11-03)
- Trend 1D: **ออกข้าง ไม่ชัด / 1W ขาขึ้นชัด** — ปิด 520.99 เหนือ MA50 514.06 (+1.35%) และ MA200 +18.82%, ใต้ MA20 −1.64%
- RSI14 49.4 · MACD hist −3.193 · vol 0.89x MA20 · wRSI 63.1 wHist +5.29
- แนวรับ 507.82 / 504.96 (20d low) · แนวต้าน 529.66 (MA20) / 541.29 / 551.15 (52w)
- ไฟล์เต็ม (ภาพรวมธีม): [[DAILY_tech_2026-11-04]]
<!-- agent:tech:end -->

## 💰 Financial
<!-- agent:finance:begin -->
- งวด: TTM ถึง 2026-09-30 (10-Q Q1 FY27, unaudited) · รายได้ 346,445M · NI 142,631M · FCF 59,957M (17.3%)
- Valuation: P/E 27.23 (520.99 ÷ 19.13) vs median ตัวเอง 35.65 · EV/EBITDA 19.15 vs 24.18
- จับตา: capex TTM 135,921M = 39.3% ของรายได้ (P/FCF 64.5) · net debt 69,422M · XD 2026-11-19 $0.98
- เต็ม: [[DAILY_2026-11-04_fin]]
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
