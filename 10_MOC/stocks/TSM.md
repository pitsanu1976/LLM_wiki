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
**2026-10-29 (ปิด 431.81, −1.75%, SIP, ดึง 22:36Z)** · AH 22:21Z = **420.98** · 1W **+4.72%** · ATR14 2.80% (ผ่านเกตไม้เต็มเพดาน)
**เหตุการณ์ล่าสุด:** −1.75% เมื่อวาน = อ่อนกว่า SMH −1.06% ท่ามกลางการเทขาย semis หลัง INTC guide; **ไม่มีข่าวเฉพาะตัว TSM ใน 29 ต.ค.**
**Catalyst ที่มีวัน:** **ไม่พบงบในปฏิทิน Nasdaq 30 ต.ค.–11 ธ.ค.** (Q3 รายงานไปแล้ว 15 ต.ค.) — วันที่ **2026-11-10 13:30 Taipei (ยอดขายรายเดือน ต.ค.)** ที่ค้างอยู่ใน block นี้เป็น **ข้อมูล inherited จาก TSMC IR calendar ที่ดึง 2026-10-18 ยังไม่ re-verify รอบนี้** ⇒ อย่าใช้เป็นวันยืนยัน
**XD:** Nasdaq dividends API คืนค่า rows ว่างสำหรับ TSM ⇒ **ไม่ยืนยันว่าไม่มี XD** ต้องดู TSMC IR เอง
**Sentiment: Neutral** — demand ยืน (เป็นผู้ผลิตจริงของ GPU ทุกค่าย) แต่ไม่มี catalyst ข้างหน้าในกรอบ
ที่มา: Nasdaq earnings API 2026-10-29 (43 วัน, 0 error) · Alpaca SIP bars — รายงานเต็ม `workspace/reports/news/2026-10-30-DAILY.md`
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
