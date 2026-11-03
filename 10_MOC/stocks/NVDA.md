---
title: NVDA
type: moc
status: active
ticker: NVDA
agent: leader
created: 2026-10-25
updated: 2026-10-25
tags:
  - moc
  - ticker/NVDA
aliases:
  - NVDA
  - NVIDIA
related:
  - "[[MSFT]]"
  - "[[2026-10-22]]"
  - "[[2026-10-23]]"
  - "[[2026-10-29]]"
  - "[[2026-10-25-week1-trade-journal]]"
  - "[[decisions]]"
  - "[[trading-finance-moc]]"
---

# NVDA — NVIDIA

## Snapshot
| | |
|---|---|
| Sector | Semiconductors — AI accelerators / datacenter GPU |
| Watchlist status | **มีคำสั่งค้าง** buy 94 @211.00 (stop 201.00 · TP 243.37) · filled 0/94 |
| ความเห็นล่าสุด | รอบ 29 ต.ค.: finance PASS ตัวเดียวใน 10 ชื่อ (P/E 27.2 vs median 51.6) · net R:R 2.76 · stop 1.70×ATR — ไม้ที่แก้ข้อผิดพลาดของรอบก่อน (stop แคบ) |

*(ส่วนนี้เป็นของ Leader)*

## 📰 News
<!-- agent:news:begin -->
**2026-11-02 (ปิด 202.06, −1.26%, SIP consolidated 21:00 UTC ดึง 22:36Z)** · 1W −6.45% · 1M −13.63% · ATR14 **3.15%** (ต่ำสุดพอใส่ไม้เต็มเพดาน)
**งบ Q3 FY27 = 2026-11-17 ยืนยันจากบริษัท** (ผล ~20:20 UTC, call 22:00 UTC) — primary = NVIDIA PR 2026-10-28 · guide Q3 $108B ±2%, outlook ไม่นับ China data-center
**ไม่มี XD ในกรอบ** (ล่าสุด 2026-09-10 $0.25) · **คะแนนแคทาทิสต์ N = 6/10** (สูงสุดในลิสต์ 10 ชื่อ — แคทาทิสต์มีวัน+primary เดียว; ถูกจำกัดที่ 6 เพราะ sentiment ธีม Bearish)
**Sentiment: Bearish-narrow ระดับธีม / demand ยังไม่พัง** — งบ 17 พ.ย. = binary ที่อยู่ในกรอบถือ (gap ไม่ใช่ trend)
ที่มา: Alpaca SIP bars 2026-11-02 · NVIDIA PR 2026-10-28 — รายงานเต็ม `workspace/reports/news/2026-11-03-DAILY.md` · คะแนน `workspace/reports/news/2026-11-03-DAILY-scores.md`
<!-- agent:news:end -->

## 📈 Technical
<!-- agent:tech:begin -->
## เทคนิคัล (อัปเดต 2026-11-04, ข้อมูลถึงปิด 2026-11-03)
- Trend 1D: **ขาลง ไม่ชัด** — ดีด +2.29% ปิด 206.69 แต่ยังใต้ MA20 217.99 / MA50 221.46 (เหนือ MA200 204.56 +1.04%)
- RSI14 39.2 · MACD hist −1.628 (ติดลบ 10/10 ชื่อในลิสต์) · vol 0.91x MA20
- แนวรับ 205.93 / 200.92 (20d low) · แนวต้าน 209.98 / 212.15 / 222.19
- ไฟล์เต็ม (ภาพรวมธีม): [[DAILY_tech_2026-11-04]]
<!-- agent:tech:end -->

## 💰 Financial
<!-- agent:finance:begin -->
- งวด: TTM ถึง 2026-07-26 (10-Q Q2 FY27, unaudited) · รายได้ 302,970M · NI 192,880M · FCF 127,006M (41.9%)
- Valuation: P/E 26.14 (206.69 ÷ 7.91) = ต่ำกว่า median ตัวเอง 54.60 ถึง −52% · EV/EBITDA 24.68 vs 46.88
- จับตา: GM FY2026 71.1% ต่ำสุดใน 3 ปี (TTM ฟื้น 74.7%) · OCF/NI 0.70 · งบ 2026-11-17 หลังปิด
- เต็ม: [[DAILY_2026-11-04_fin]]
<!-- agent:finance:end -->

## 👑 Decision
<!-- agent:leader:begin -->
### 2026-10-22 — BUY 91 @217.08 (stop 211.00 / TP 234.76)
- เหตุผล: tech #1 ของรอบ (R:R T2 2.39 · stop 1.19×ATR · เหนือ MA200) + finance #2 (P/E 28.06 = −33% vs median 41.8) + news ผ่านเกณฑ์
- ขนาด: 91 หุ้น = $19,838 (19.8%) — **ติดเพดาน 20%** จึงใช้ risk เพียง 0.64% ไม่เต็ม 1%
- บันทึก: [[2026-10-22]]

### 2026-10-23 — STOPPED OUT 91 @212.20 → **−$444.08 = −0.80R**
- stop leg ทำงาน 13:32:50Z หลัง SOXX −6.79% · TP leg ถูกยกเลิกอัตโนมัติ (OCO)
- บทเรียน: stop ต้อง ≥1.5×ATR และ ≥ implied gap ถ้าถือข้ามงบ — ทำได้โดยลดขนาดไม้ ไม่ใช่ยืด stop
- บันทึก: [[2026-10-23]] · สรุปสัปดาห์: [[2026-10-25-week1-trade-journal]]

### 2026-10-29 — BUY อีกครั้ง 94 @211.00 (stop 201.00 / TP 243.37)
- เหตุผล: finance **PASS ตัวเดียว** ใน 10 ชื่อ (P/E 27.2 vs median 5 ปี 51.6 · net cash $23.6B) · net R:R **2.76** · stop 10.00 = **1.70×ATR** (ผ่านกติกาใหม่ ≥1.5×ATR) · corr MSFT 0.47
- ขนาด 94 หุ้น = $19,834 (19.87%) · risk **$940 (0.94%)** · order `3fac49b1` accepted GTC · legs TP 243.37 (94) + stop 201.00 (94) `held`
- ตัด TSM ออกจากรอบนี้เพราะ corr NVDA–TSM **0.858** (ไม้เดียวกัน)
- บันทึก: [[2026-10-29]]

### สถานะปัจจุบัน (2026-10-29 00:27 UTC)
- **มีคำสั่งค้าง: buy 94 @211.00** (filled 0 — ตลาดปิด) · invalidated ถ้าปิด < 204.14 ก่อนเข้า
- ไม่มี position (ไม้เดิม 91 @217.08 ถูก stop 212.20 ไปแล้ว 23 ต.ค.)
- งบ **18 พ.ย.** ต้องตัดสินก่อน 17 พ.ย.
<!-- agent:leader:end -->

## แหล่งข้อมูล

- ข่าว/include ในรอบวิเคราะห์: [[DAILY_news_2026-10-22]]
- เทคนิค: [[DAILY-US_tech_2026-10-22]]
- งบการเงิน: [[DAILY_2026-10-22_fin]]
- บันทึกการตัดสินใจ: [[decisions]]

## เกี่ยวข้อง

- [[MSFT]] — ไม้ที่ถืออยู่ตัวเดียว · corr c30 0.20
- [[TSM]] — corr c60 0.651 (ใช้ตัดสินขนาดไม้)
- [[trading-finance-moc]]
- [[journals-moc]]
