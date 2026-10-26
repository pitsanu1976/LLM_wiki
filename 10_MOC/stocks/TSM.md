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
- **2026-10-20 (ข่าว)**: Q3 2026 (15 ต.ค.) รายได้ $46.72B เหนือ high end, GM 66.4%, Q4 guide $52.3–54.3B, FY26 ~+44% USD, capex $60–64B — แต่หุ้นลง 3.4% วันนั้นจาก N2/ต่างประเทศ margin dilution (TSMC IR)
- **Catalyst ถัดไป**: ยอดขายรายเดือน ต.ค. 2026 · 2026-11-10 13:30 Taipei · TSMC IR financial calendar (inherited 2026-10-18) · งบ Q4 ~ม.ค. 2027 ยังไม่ประกาศวัน
- **Sentiment**: Bullish-narrow (demand ยืน, margin เป็นตัวกด) — รายละเอียด [[DAILY-US_news_2026-10-20]]
<!-- agent:news:end -->

## 📈 Technical
<!-- agent:tech:begin -->
_ยังไม่มี block — ข้อมูลล่าสุดอยู่ใน [[DAILY-US_tech_2026-10-19]]_
<!-- agent:tech:end -->

## 💰 Financial
<!-- agent:finance:begin -->
**งบล่าสุด:** **Q3-2026** (Sep-26) — รายได้ 1,494,243M TWD (+50.9% yoy) · GM **66.41%** (จาก 67.72% q/q) · OM 58.66% · FCF 476.6B TWD (+242% yoy)
**Valuation:** P/E **27.8** (median 8 ไตรมาส 23.8 = +17%) · fwd 19.5 · EV/EBITDA 16.0 · FCF yield 2.38% · D/E 0.12 · net cash **$100.4B**
**จับตา:** margin dilution จาก N2/โรงงานต่างประเทศคือความเสี่ยงหลัก (ไม่ใช่รายได้) · ยอดขายรายเดือน ต.ค. 2026-11-10
เต็ม: [[DAILY_2026-10-21_fin]] · [[TSM_fin_2026-Q3]]
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
