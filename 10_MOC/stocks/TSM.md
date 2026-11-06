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
- **2026-11-06 (news):** **ยืนยันวันแล้ว** = รายได้เดือน ต.ค. 2026 ออก **อ. 10 พ.ย. 2026 13:30 Taipei (05:30 UTC)** — แหล่ง primary: investor.tsmc.com/english/financial-calendar (เดิมรายงาน 2026-11-05 ระบุ "ต้องยืนยัน")
- ปิด 2026-11-05 = **353.10** (−10.78% 1D, −18.23% 5D, −25.22% 21D), ATR% 4.53 (calc), ห่าง high 52w −27.56%, ปริมาณ 3.39× MA20
- วัด thesis ด้วย: MoM/YoY ของรายได้รายเดือน = datapoint เร็วที่สุดของ demand จริง (เร็วกว่าทุกงบในลิสต์)
- เสี่ยง: เป็น datapoint ไม่มี guidance · ไต้หวัน −4.5% ในสัปดาห์ = แย่สุดในรอบ 2 ทศวรรษ (Reuters 2026-11-06)
- อ้างอิง: [[DAILY_news_2026-11-06]]
<!-- agent:news:end -->

## 📈 Technical
<!-- agent:tech:begin -->
## เทคนิคัล (อัปเดต 2026-11-06, ข้อมูลถึงปิด 2026-11-05)
- Trend 1D: **ขาลง ชัด** — ปิด 353.10 ใต้ MA200 401.24 / MA20 420.33 / MA50 432.68 · MA20 slope −6.01% (10 แท่ง)
- RSI14 **26.4** (48.1) · MACD hist −6.37 (จาก −0.49) · vol 42.6M = **3.04× MA20** · ATR14 16.01 (4.53%)
- แนวรับ 351.19 (2026-11-05 low) / 331.92 (2026-03-09) / 319.07 · แนวต้าน 380.78 (2026-11-05 high) / 401.24 (MA200)
- ระดับ: pullback E 332.20 · S 316.10 (1.01×ATR) · T2 380.00 (2.88R net) — รายได้เดือน 11-10 gap proxy max 7.23% = 1.49× stop (borderline)
- ไฟล์เต็ม: [[DAILY_tech_2026-11-06]]
<!-- agent:tech:end -->

## 💰 Financial
<!-- agent:finance:begin -->
- งวด: TTM ถึง 2026-09-30 (Q3-2026, TWD ล้าน, unaudited) · รายได้ 4,944,816 · NI 2,527,571 · FCF 1,480,739 (29.9%)
- Valuation: P/E 23.88 (353.10 ÷ 14.79 ADR) vs median ตัวเอง 22.37 (+6.8%) · EV/EBITDA 14.66 · net cash 3.20T TWD · D/E 0.12
- จับตา: GM 66.4% / OM 58.7%, ICov 324, dilution +0.01% · รายได้เดือน ต.ค. 2026-11-10 · XD 2026-12-10 $1.08544/ADS
- เต็ม: [[DAILY_fin_2026-11-06]]
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
