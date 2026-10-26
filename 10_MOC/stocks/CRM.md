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
_ยังไม่มี block — ข้อมูลล่าสุดอยู่ใน [[DAILY-US_tech_2026-10-19]]_
<!-- agent:tech:end -->

## 💰 Financial
<!-- agent:finance:begin -->
**งบล่าสุด:** **Q2 FY27** (Jul-26) — รายได้ $11,345M (**+10.8% yoy** ช้าสุดใน 12 ชื่อ) · GM 76.65% (จาก 78.10%) · OM 21.38%
**Valuation:** P/E **22.5** (242.44 ÷ EPS 10.79; median 8 ไตรมาส 35.7 = −37%) · fwd 16.5 · **FCF yield 7.60%** · D/E **1.10** · IC 9.4x · net debt $31.0B
**จับตา:** NI/OI 1.45 = มี one-off ~$1.1B · หุ้น −7.44% yoy จาก buyback (หนี้เพิ่มตาม) · งบ 2026-12-02 (กึ่งยืนยัน — IR เป็น JS shell)
เต็ม: [[DAILY_2026-10-21_fin]] · [[CRM_fin_2027-Q2]]
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
