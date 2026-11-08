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
- **2026-11-08 (news · ดึงข้อมูล 09:26 UTC):** sentiment **Neutral (เอนลบ · narrow)** กรอบ 1–3 สัปดาห์ — ไม่มี guidance cut ในห่วงโซ่ แต่ความเสี่ยง permit data center ระดับรัฐยังไม่คลี่ + ตลาด price chance ขึ้นดอกเบี้ย ธ.ค. **78%** (LSEG ผ่าน Reuters 6 พ.ย.)
- ปิด **2026-11-06 = 186.64** (+5.04 / +2.78%, prev close 181.60 · stockanalysis "At close: Nov 6, 2026, 4:00 PM EST") · −23.31% จาก 52w high 243.37 (calc) ⇒ **ปิดต่ำกว่า invalidation 204.14 ของคำสั่งค้าง buy 94 @211.00 (filled 0) แล้ว** — ต้องตัดสินเรื่องคำสั่งค้างก่อนคิดเรื่องงบ
- วันงบ = **อ. 17 พ.ย. 2026 หลังปิด** (ผล ~16:20 ET · call 17:00 ET / 22:00 UTC) — ยืนยันแล้ว (nvidianews.nvidia.com 28 ต.ค. 2026) ⇒ **ไม่ใช่ 18 พ.ย. ตาม block Decision (บันทึก 29 ต.ค.)**
- วัด thesis งบ 17 พ.ย.: revenue ≥ **$108.0B ±2%** · GM ≥ **74.0% ±50bp** (จาก 75.0% Q2) · Q4 guide โตต่อ · ไม่มีคำว่า "push out" · คำอธิบาย China + permitting
- จีนสองทาง (ยังไม่มีกำหนด): H200 ~**600,000** ชิปค้างฮ่องกงรอผู้อนุมัติ (Reuters 5 พ.ย., กึ่งยืนยัน) = upside ที่ guide **ไม่รวม**; NYT 7 พ.ย. ชี้การอนุมัติบริษัทจีนมีช่องโหว่ ⇒ เสี่ยงถูกทบทวน (= ตัด optionality)
- เสี่ยงหลัก: GM vs ต้นทุน memory (commitments $119B → **$279B "primarily memory"**, 26 ส.ค.) · EO/moratorium ระดับรัฐ · binary งบ 17 พ.ย.
- ปฏิทินใกล้: 10 พ.ย. TSMC Oct sales 05:30 UTC · CPI ต.ค. 13:30 UTC · CoreWeave Q3 22:00 UTC · 12 พ.ย. AMAT + CSCO
- อ้างอิง: [[NVDA_news_2026-11-08]] · [[DAILY_news_2026-11-06]]
<!-- agent:news:end -->

## 📈 Technical
<!-- agent:tech:begin -->
## เทคนิคัล (อัปเดต 2026-11-08, ข้อมูลถึงปิด 2026-11-06 · SIP)
- Trend 1D: **ขาลง ชัด** — ปิด 186.64 ใต้ MA20 211.55 / MA50 219.81 / MA200 204.67 · dd −23.3% จาก high 243.37
- RSI14 **30.8** (จาก 25.4) · MACD hist −3.20 (ลึกขึ้น ไม่มี cross) · vol 181.0M = 1.53× MA20 · ATR14 7.77 (4.16%)
- ต้าน 188.88 (2026-03-16) / 194.90 (2026-11-06) / 206.79 · รับ 185.22 / 181.46 (low 120d) / 179.18 / 176.76
- armed ใหม่: A ปิด ≥188.88 → E 189.00 · S **176.50** (1.61×ATR) · T2 206.79 · 0.80 หุ้น (R:R 1.42) · B E 179.20 · S 167.50 · T2 197.97 · 0.85 หุ้น (1.60R) — ของเดิม stop 0.95×ATR ใช้ไม่ได้
- งบ 2026-11-17: ถ้าเข้าต้องมี time stop ก่อน 2026-11-16 · ไฟล์เต็ม: [[NVDA_tech_2026-11-08]]
<!-- agent:tech:end -->

## 💰 Financial
<!-- agent:finance:begin -->
- งบ Q2 FY27 (ถึง 2026-07-26, unaudited): Revenue 96,221M +105.8% YoY · GM 75.0% · GAAP EPS 2.46 (ตัด equity gains 7.8B → core ~2.19) · FCF 21,341M −56% QoQ · net cash 23.2B
- Valuation @2026-11-06 (186.64): P/E trailing 23.60 · FY27E 20.05 (EPS 9.31) · **core P/E 27.1** · EV/EBITDA 22.3 · PEG 0.25
- จับตางบ 17 พ.ย.: GM guidance 74% (จาก 75.0) · DSO 45.4→59.6 วัน + FCF หายครึ่ง · consensus FY27 9.31 ต่ำกว่า run-rate 9.71
- เต็ม: [[NVDA_fin_2027-Q2]]
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
