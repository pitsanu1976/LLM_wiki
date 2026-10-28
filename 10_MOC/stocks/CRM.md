---
title: CRM
type: moc
status: active
ticker: CRM
agent: leader
created: 2026-10-19
updated: 2026-10-25
tags:
  - moc
  - ticker/CRM
related:
  - "[[2026-10-19]]"
  - "[[2026-10-22]]"
  - "[[2026-10-25-week1-trade-journal]]"
  - "[[decisions]]"
aliases:
  - CRM
---

# CRM

> สร้างจาก [[stock-hub-template]] — Leader เติม Snapshot และ Decision block
> block ข่าว/เทคนิค/งบ จะถูกเติมโดย agent เจ้าของในรอบถัดไป

## Snapshot

| | |
|---|---|
| Sector | Software — SaaS / enterprise CRM |
| Watchlist status | **ยกเลิกคำสั่งแล้ว** (71 @235 ไม่เคย fill) |
| ความเห็นล่าสุด | news + finance ตรงกันว่าไม่มี catalyst มีวันจนถึง 2 ธ.ค. ⇒ ยกเลิก 2026-10-22 · P/E 22.5 + FCF yield 7.6% ยังน่าสนใจแต่ต้องมีตัวกระตุ้น |

## 📰 News
<!-- agent:news:begin -->
- **2026-10-12 (ข่าว, เก่า 8 วัน)**: BofA double upgrade Underperform→Buy PT $160→$285 (Benzinga/Barchart) — ยังใช้เป็นบริบท ไม่ใช่ catalyst ใหม่
- **งบถัดไป**: Q3 FY27 ~**2026-12-02** หลังปิด (TipRanks "confirmed" / MarketBeat "estimated") ⇒ ไม่มี binary จนท้ายกรอบ
- **Sentiment**: Neutral (แรงหนุนข่าวหมดอายุ, หุ้นขึ้น >50% จากปลาย มิ.ย.) — [[DAILY-US_news_2026-10-20]]
<!-- agent:news:end -->

## 📈 Technical
<!-- agent:tech:begin -->
**ปิด 2026-10-28 $242.11** (Alpaca SIP 1Day) · trend 1D **ขึ้น (ไม่ชัด) — ทรงตัว 236–252 ตั้งแต่ 15 ต.ค.**: MA20 237.96 +1.75% / MA50 237.93 +1.76% / MA200 198.41 +22.02%
RSI14 **53.57** · MACD hist **+0.31** (ลดจาก 0.66) · ATR14 8.54 (3.53%) · vol 0.91× · 1D +0.51% · 1W +0.14%
แนวรับ 237.01 (10-28) / 235.60 (10-20) / **220.29 (10-08)** · แนวต้าน 244.64 (10-28) / **252.42 (10-22)** / 262.33 (09-15)
ถ้าซื้อ: entry 226.00–230.00 (**−5.8% ต้องย่อลึก ถ้าไม่ย่อไม่มีไม้**) · stop **215.00** (5.70% = 1.52×ATR) · T1 252.42 / T2 262.33 · **R:R net 2.29** · 76 หุ้น (86.8% เพดาน) · งบ 2 ธ.ค.
เต็ม: [[DAILY-US_tech_2026-10-28]]
<!-- agent:tech:end -->

## 💰 Financial
<!-- agent:finance:begin -->
**งบล่าสุด:** **Q2 FY27 (31 ก.ค. 26, 10-Q ยื่น 2026-08-27)** — รายได้ $11,345M (**+10.8% yoy ช้าสุด**) · GM 76.65% · OM 21.38% · OCF/NI 1.63 (stockanalysis, ดึง 2026-10-27)
**Valuation (ปิด 2026-10-27 $240.91):** P/E **22.32** · fwd 16.42 · median P/E 5y 47.7 ⇒ **−53%** · FCF yield **7.61%** · D/E **1.10** · net debt **$30.97B** · current ratio 0.84 · **P/E หักกำไรเงินลงทุน $4,245M (43.9% ของ NI) = ~36.6x**
**จับตา:** total debt 11,635→17,711→42,548 $M (**+$30.9B ใน 2 ไตรมาส**) · AR yoy +15.5% บนรายได้ +10.8% · consensus 2 ธ.ค. **EPS −9.4% yoy** · finance: **VETO** (ถูกเพราะ one-off ไม่ใช่เพราะตลาดพลาด)
เต็ม: [[DAILY_2026-10-28_fin]] · [[CRM_fin_2027-Q2]]
<!-- agent:finance:end -->

## 👑 Decision
<!-- agent:leader:begin -->
### 2026-10-19 — BUY limit 71 @235.00 (stop 221.00 / TP 263.60)
- เหตุผล: valuation reset — P/E 22.5 (−37% vs ประวัติ) + FCF yield 7.6%
- บันทึก: [[2026-10-19]]

### 2026-10-22 — ยกเลิกคำสั่ง (`d04b3af7` → canceled)
- news + finance ตรงกัน: **ไม่มี catalyst ที่มีวันชัดเจนจนถึง 2 ธ.ค.** ⇒ ถือ limit ที่ไม่ fill ต่อไปไม่ก่อประโยชน์
- ปลด notional $16,685 / risk $994
- บันทึก: [[2026-10-22]]

### สถานะปัจจุบัน (2026-10-25)
- **ไม่มี position** · ไม่มีออเดอร์ค้าง
- กลับเข้าได้เมื่อ: มี catalyst ที่มีวัน (เช่น งบ/คำประกาศ) + ราคายังไม่หลุดโครงสร้างขาขึ้น
<!-- agent:leader:end -->

## แหล่งข้อมูล

- [[DAILY-US_tech_2026-10-19]] — technical (รวมหลาย ticker)
- [[CRM_fin_2027-Q2]] — งบการเงิน

## เกี่ยวข้อง

- [[trading-finance-moc]]
- [[agent-access-policy]]
