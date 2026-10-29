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
**ปิด 2026-10-28 $439.51** (Alpaca SIP 1Day) · trend 1D **ออกข้าง (ไม่ชัด) ในขาขึ้นใหญ่**: ใต้ MA20 442.34 (−0.64%) · เหนือ MA50 434.72 +1.10% / MA200 399.26 **+10.08%**
RSI14 **51.84** · MACD hist **−0.90** (ดีขึ้นจาก −2.22) · ATR14 12.17 (2.77%) · vol **0.70×** MA20 · 1D +0.60% · 1W +1.76%
แนวรับ **426.00** (10-27) / 417.72 (10-26) / **407.13 (10-15)** · แนวต้าน **442.34 (MA20)** / 444.29 (09-08) / 476.79 (06-22) / 487.47 (10-05)
ถ้าซื้อ: entry 425.00–430.00 · stop **406.50** (4.91% = 1.73×ATR) · T1 476.79 / T2 487.47 · **R:R net 2.43** · ไม้เต็มเพดานได้ 46 หุ้น ($19,665, risk $966) · **ไม่มีงบในกรอบ**
เต็ม: [[DAILY-US_tech_2026-10-28]]
<!-- agent:tech:end -->

## 💰 Financial
<!-- agent:finance:begin -->
**งบล่าสุด:** **Q3 2026 (30 ก.ย. 26, ออก 2026-10-15)** — รายได้ TWD 1,494,243M (**+50.9% yoy**) · GM 66.41% (+696bp) · OM **58.65%** · OCF/NI **1.24** (stockanalysis, ดึง 2026-10-27)
**Valuation (ปิด 2026-10-27 $436.885):** P/E **29.05** · fwd 20.25 · median P/E 5y 22.4 ⇒ **+30%** · EV/EBITDA **16.07 (ต่ำสุดใน 10 ชื่อ)** · net cash **+$100.36B** · D/E 0.12 · DSO 29 วัน
**จับตา:** ไม่มีงบในกรอบ 28 ต.ค.–9 ธ.ค. ⇒ ถือข้ามได้ · AR +9.4% q/q ช้ากว่ารายได้ +17.6% q/q (ดี) · SBC ไตรมาสล่าสุด **หาไม่ได้** · finance: **ผ่าน** (ตัวเดียวที่ผ่านไม่มีเงื่อนไขในรอบนี้)
เต็ม: [[DAILY_2026-10-28_fin]] · [[TSM_fin_2026-Q3]]
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
