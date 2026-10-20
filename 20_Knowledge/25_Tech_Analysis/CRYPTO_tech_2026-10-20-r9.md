---
title: "CRYPTO — Technical 2026-10-20 (round 9, 10 pairs)"
type: source
status: active
created: 2026-10-20
updated: 2026-10-20
agent: tech
ticker: CRYPTO
scope: market
tags:
  - tech/indicators
  - ticker/CRYPTO
  - ticker/BTC
  - ticker/ETH
  - ticker/LINK
  - ticker/SOL
  - ticker/XRP
  - ticker/PAXG
  - ticker/AAVE
  - ticker/LTC
  - ticker/DOGE
  - ticker/ADA
---

# CRYPTO — Technical read 2026-10-20 (round 9)

รอบ 9 แทน [[CRYPTO_tech_2026-10-20]] (r8 = 11 คู่, quote 13:23Z) · รอบนี้ **10 คู่** ตาม work order: BTC, ETH, LINK, SOL, XRP, PAXG, AAVE, LTC, DOGE, ADA
แท่ง 1D ปิดล่าสุด = **2026-10-19** (crypto 24/7 ⇒ แท่ง 20 ต.ค. ไม่ปิด ใช้เป็น reference เท่านั้น)
Quote ที่ใช้ตัดสิน = **Coinbase 16:49:20–16:50:59Z** (Alpaca เป็น feed บาง ใช้เทียบเท่านั้น)

## แหล่งข้อมูล (ทุกตัวเลขดึงจริงรอบนี้)
- **Alpaca crypto v1beta3** bars 1Day/1Hour/15Min + snapshots/latest quotes/trades — ดึง **2026-10-20T16:48:41Z**
- **Coinbase Exchange** ticker 10/10 · L2 book walk $3,000 · 1D candles 14–20 ต.ค. (cross-check แท่งปิด 19 ต.ค.)
- **CoinGecko** 10/10 (≈16:50:42–16:51:02Z) — ต่างจาก CB −0.15% ถึง +0.05%
- cross-check แท่งปิด 19 ต.ค.: close ต่าง Alpaca−CB **−0.06% ถึง +0.019%** ⇒ ใช้ชุด Alpaca คำนวณ indicator ได้

## Trend + ความชัด
- **ออกข้าง (ไม่ชัด) 9 คู่ + ขาลงชัด 1 คู่ (DOGE)** — ไม่มีคู่ไหนเป็นขาขึ้น 1D
- แท่งปิด 19 ต.ค. ปิดใต้ EMA20(1D) **ครบ 10/10** (−0.80% BTC ถึง −7.00% ADA)
- ที่ราคา 16:50Z มีคู่เดียวที่ยืนเหนือ EMA20(1D) = **BTC +0.29%** (EMA20 slope ยัง −0.90% ⇒ ยังไม่ยืนยัน) · ที่เหลือใต้ EMA20 −1.18% ถึง −4.68%
- MACD hist ติดลบ 8/10 (บวกแค่ PAXG) · RSI14 ต่ำกว่า 50 ทุกคู่ (ต่ำสุด DOGE 36.38) ⇒ เป็นการเด้งจาก oversold ไม่ใช่ trend ใหม่

## Indicator (แท่งปิดถึง 2026-10-19)
- **ATR(1D)**: BTC 2.54% · ETH 3.85% · PAXG 3.99% · XRP 4.78% · SOL 4.80% · DOGE 5.40% · LINK 5.84% · LTC 5.86% · AAVE 6.88% · ADA 6.90%
- **ATR > 5% 5 คู่** (DOGE, LINK, LTC, AAVE, ADA) ⇒ stop ≥1×ATR ชนเพดาน 5% ทันที = ไม่ผ่านเกต leader
- **EMA20(1D) อยู่เหนือราคา = แนวต้าน:** ETH 2,502.76 · LINK 12.7631 · SOL 108.9618 · XRP 1.3762 · PAXG 4,173.76 · AAVE 158.34 · LTC 62.2559 · DOGE 0.0850 · ADA 0.2343
- **EMA20(1D) อยู่ใต้ราคา = ฐานเดียวที่มี: BTC 82,494.78** (ราคา 82,731.78 ⇒ +0.29%)

## ระดับสำคัญ
- **BTC**: ต้าน 83,343.65 (20 ต.ค. high) → 84,060.20 → 84,265.37 · รับ 82,246.75 → 81,103.41 → 80,583.66
- **ETH**: ต้าน 2,474.08 → 2,502.76 (EMA20) → 2,526.78 · รับ 2,429.29 → 2,371.37 → 2,326.28
- **SOL**: ต้าน 108.15 → 108.96 (EMA20) → 111.95 · รับ 105.19 → 103.54 → 100.34
- **XRP**: ต้าน 1.34535 → แถบ EMA 1.375–1.377 → 1.42536 · รับ 1.31495 → 1.28475 → 1.25520
- คู่ที่เหลือไม่มีตั๋วผ่านเกต (ATR กว้าง หรือ R2 < 1.25)

## ผลต่อเกต `stop% ≤5.0` + `R2 ≥1.25`
- **ผ่าน 3 คู่ — ทั้งหมดเป็น limit ใต้ตลาด ไม่ใช่ราคาที่ซื้อได้เดี๋ยวนี้:** ETH 2,380 (stop 2,287.44 = 3.89%, R2 1.33) · SOL 104.60 (stop 99.57 = 4.81%, R2 1.46) · XRP 1.29 (stop 1.22778 = 4.82%, R2 1.39)
- **แผน breakout (A) ผ่าน 0/10** — เป้าเหนือตลาดห่างแค่ 0.8–1.6% แต่ stop 1×ATR 2.5–7.0% ⇒ R2 0.32–1.21
- **corr กับ BTC (7d hourly): ETH 0.912 · SOL 0.905 · XRP 0.895** ⇒ ถือพร้อมกันไม่ได้ = เลือก 1 ไม้
- **corr < 0.5 กับ BTC ทั้งสองหน้าต่าง: PAXG คู่เดียว** (0.370 daily / 0.456 hourly) แต่ PAXG ไม่ผ่านเกต (R2 0.32–0.37)

## ข้อควรระวังเรื่องข้อมูล
- **LTC print 53.6153 (20 ต.ค. 06:00Z) เป็น feed artifact** (v=0, n=0) — CB ต่ำสุด 58.219 · range 24 ชม. จริง 4.68% ไม่ใช่ 13.65%
- **PAXG print 4,173.2 (14:00Z) ไม่ถูก CB ยืนยัน** (CB high 4,153.34) และ spike 4,25x–4,736 ใน 12–15 ต.ค. เป็นของปลอม
- **spread Alpaca กว้างเกินจริง** (XRP 41 bps vs CB 1.5 · PAXG 103.54 vs 1.41) ⇒ ใช้ CB เป็นต้นทุน · walk book $3,000 slip 0.53–7.19 bps ทุกคู่
- **ADA มี 1D เพียง 249 แท่ง (เริ่ม 2026-02-13)** ⇒ EMA200 ครอบ ~8 เดือน

รายงานเต็ม: `workspace/reports/tech/2026-10-20-CRYPTO-r9.md`

[[trading-finance-moc]]
