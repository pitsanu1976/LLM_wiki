---
title: TSM
type: moc
status: active
ticker: TSM
agent: leader
created: 2026-10-19
updated: 2026-10-25
tags:
  - moc
  - ticker/TSM
related:
  - "[[NVDA]]"
  - "[[2026-10-19]]"
  - "[[2026-10-25]]"
  - "[[2026-10-25-week1-trade-journal]]"
  - "[[decisions]]"
aliases:
  - TSM
---

# TSM

> สร้างจาก [[stock-hub-template]] — Leader เติม Snapshot และ Decision block
> block ข่าว/เทคนิค/งบ จะถูกเติมโดย agent เจ้าของในรอบถัดไป

## Snapshot

| | |
|---|---|
| Sector | Semiconductors — foundry / advanced packaging |
| Watchlist status | **ยกเลิกคำสั่งแล้ว** (49 @407 ไม่เคย fill) |
| ความเห็นล่าสุด | ค้าง 7 sessions ไม่ fill · notional 20.02% เกินเพดาน 20% · corr NVDA 0.651 ⇒ ยกเลิก 2026-10-25 |

## 📰 News
<!-- agent:news:begin -->
**2026-11-02 (ปิด 398.63, −1.85%, SIP consolidated 21:00 UTC ดึง 22:36Z)** · 1W −6.07% · 1M −15.68% · ATR14 **3.44%**
**Catalyst ที่มีวัน: ไม่มีในกรอบ** — งบ Q3 ออกแล้ว ต.ค.; วันประกาศยอดขายรายเดือน พ.ย. **ยังไม่ได้ดึง investor.tsmc.com รอบนี้ ⇒ ห้ามใช้เป็นวันยืนยัน** (ค่าที่เคยมีใน block นี้เป็น inherited ยังไม่ re-verify)
**คะแนนแคทาทิสต์ N = 3/10** (ต่ำสุดในลิสต์) — ไม่มีแคทาทิสต์ของตัวเอง และเป็นผู้รับ read-across ตรงจาก AMD 2026-11-03 + NVDA 2026-11-17 ⇒ ข่าวที่กระทบมีแต่ด้านลบ
**Sentiment: Bearish-narrow ระดับธีม / demand ยังยืน** — เป็น foundry จริงของทุกค่าย แต่ไม่มีตัวขับ narrative ของตัวเองในกรอบ 2–6 สัปดาห์
ที่มา: Alpaca SIP bars 2026-11-02 · Nasdaq earnings calendar 2026-11-02 — รายงานเต็ม `workspace/reports/news/2026-11-03-DAILY.md` · คะแนน `workspace/reports/news/2026-11-03-DAILY-scores.md`
<!-- agent:news:end -->

## 📈 Technical
<!-- agent:tech:begin -->
**ปิด 2026-10-29 $431.81** (Alpaca SIP 1Day) · trend 1D **ออกข้าง (ไม่ชัด) ในขาขึ้นใหญ่**: ใต้ MA20 440.97 (−2.08%) / MA50 435.12 (−0.76%) · เหนือ MA200 399.77 **+8.02%**
RSI14 **48.15** · MACD hist **−0.49** (ดีขึ้นจาก −0.90) · ATR14 12.09 (2.80%) · vol **0.74×** MA20 · 1D −1.75% · 5D +4.72%
แนวรับ 428.43 (10-29) / 426.00 (10-27) / **407.13 (10-15 low)** · แนวต้าน **440.97 (MA20)** / 444.29 (09-08) / 476.79 (06-22)
ถ้าซื้อ: entry 417–421 · stop **400.50** (4.87% = 1.70×ATR) · T1 444.29 (RR 0.90) / T2 **476.79 (RR 2.31)** · เต็มเพดาน 47 หุ้น (risk $963.50) · **fill ต้อง ≥418.63** · ไม่มีงบในกรอบ
เต็ม: [[DAILY-US_tech_2026-10-29]]
<!-- agent:tech:end -->

## 💰 Financial
<!-- agent:finance:begin -->
**งบล่าสุด:** Q3 2026 (ended 2026-09-30, รายงาน 2026-10-15, unaudited) — ตัวเลขงบเป็น **TWD ล้าน**: รายได้ 1,494,243 · NI 763,064 · EPS 29.43 (GM 66.41%) · FCF 476,560
**TTM (USD, แปลงโดยแหล่ง):** รายได้ 155.16B · NI 79.31B · EPS 14.96/ADR · FCF 45.45B · net cash +100.36B · capex 32.6% ของรายได้
**Valuation (ราคาปิด 2026-10-29 = 431.81):** P/E 28.9 (431.81/14.96) · fwd 20.22 · median 5 ปี 22.37 (**+29%**) · EV/EBITDA 16.09 (ต่ำสุดในกลุ่ม) · FCF yield 2.40%
**ต้องจับตา:** 1) **XD 2026-12-10 $1.08544/ADR** (pay 2027-01-07) — อยู่ในกรอบถือ 2) FCF payout 231% (ปันผลเกิน FCF เพราะ capex) 3) งบถัดไป ~ม.ค. 2027 นอกรอบ 11 ธ.ค.; market cap บนหน้าแหล่งข้อมูลไม่สอดคล้องราคา ADR (ระวัง EV/EBITDA)
**คำตัดสิน (มุมการเงิน):** PASS แบบมีเงื่อนไข (+29% เหนือ median ตัวเอง) · อันดับ 3
ไฟล์เต็ม: [[DAILY_2026-10-30_fin]] · รายงาน: `reports/finance/2026-10-30-DAILY.md`
<!-- agent:finance:end -->

## 👑 Decision
<!-- agent:leader:begin -->
### 2026-10-19 — BUY limit 49 @407.00 (stop 393.90 / TP 452.47)
- เหตุผล: demand + Q4 guide $52.3–54.3B (ยืนยันจาก IR) · limit ใต้ตลาด 5.8%
- บันทึก: [[2026-10-19]]

### 2026-10-25 — ยกเลิกคำสั่ง (`ef20ced4` → canceled)
- ค้าง 7 sessions ไม่มี fill · $19,943 = **20.02% เกินเพดาน 20%** หลัง equity ลด · corr NVDA–TSM **0.651**
- ปลด buying power $19,943 · ไม่มีต้นทุนเกิดขึ้น
- บันทึก: [[2026-10-25]]

### สถานะปัจจุบัน (2026-10-25)
- **ไม่มี position** · ไม่มีออเดอร์ค้าง (legs ถูกยกเลิกตาม parent)
- กลับเข้าได้เมื่อ: มี catalyst ใหม่ + ขนาดไม่เกินเพดานที่ equity ปัจจุบัน + ถ้าถือ NVDA/MSFT อยู่ต้องคิด corr ก่อน
<!-- agent:leader:end -->

## แหล่งข้อมูล

- [[DAILY-US_tech_2026-10-19]] — technical (รวมหลาย ticker)
- [[TSM_fin_2026-Q3]] — งบการเงิน

## เกี่ยวข้อง

- [[trading-finance-moc]]
- [[agent-access-policy]]
