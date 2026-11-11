---
title: "DAILY — Technical 2026-11-11"
type: source
status: active
created: 2026-11-11
updated: 2026-11-11
agent: tech
ticker: DAILY
scope: market
tags:
  - tech/indicators
  - ticker/DAILY
  - ticker/TJX
  - ticker/KO
  - ticker/TGT
  - ticker/LVS
  - ticker/WMT
  - ticker/PEP
  - ticker/MDLZ
  - ticker/VZ
  - ticker/KR
  - ticker/DIS
---

# DAILY — Technical 2026-11-11 (10 ชื่อ shortlist ของ news)

แท่ง 1D ปิดล่าสุด **2026-11-10** ทุกชื่อ · OHLCV จาก **Alpaca v2/stocks/bars feed=sip** (`timeframe=1Day`, `adjustment=all`, 718 แท่ง/ชื่อ) ดึง 2026-11-11 10:19Z · indicator คำนวณด้วย Python ทั้งหมด · cross-check ปิดล่าสุดกับ **Nasdaq `secondaryData` ("Closed at Nov 10, 2026 4:00 PM ET")** ตรงกันทุกชื่อ ผลต่าง ≤ $0.03 · Yahoo ตอบ 429 ทั้ง 10 ชื่อ (ไม่มี second source daily bars)

รายงานฉบับเต็ม: `workspace/reports/tech/2026-11-11-DAILY.md`
ข้อมูลดิบ: `workspace/data/2026-11-11-DAILY-tech-{fetch,calc,extra,plans}.json`

## Trend + ความชัด (1D)

| ticker | Trend | px vs MA20/50/200 | EMA20 slope 10d | RSI14 | MACD hist | volR | ATR14 (SMA) | ATR% |
|---|---|---|---|---|---|---|---|---|
| TJX | ขาลง (ชัด) | ใต้ MA20 −3.7% / เหนือ MA50 +0.7% / ใต้ MA200 −8.8% | −1.12% | 45.5 | −0.385 | 1.03 | 3.88 | 2.83% |
| KO | ขาขึ้น (ชัด) | +3.2% / +7.5% / +17.8% | +3.01% | 68.0 | +0.311 | 0.91 | 1.98 | 2.04% |
| TGT | ขาขึ้น (ไม่ชัด) | +4.8% / +4.1% / +20.9% | +2.14% | 57.8 | +0.841 | 1.06 | 6.00 | 3.71% |
| LVS | ขาขึ้น (ไม่ชัด) | +7.7% / +5.1% / −14.2% | +3.87% | 64.8 | +0.667 (MACD ยังลบ) | 0.71 | 1.28 | 3.13% |
| WMT | ขาขึ้น (ชัด) | +3.0% / +10.8% / +6.0% | +5.62% | 63.5 | +0.761 | 0.77 | 3.19 | 2.54% |
| PEP | ขาขึ้น (ชัด) | +5.3% / +7.7% / ติด MA200 −0.06% | +3.90% | 65.8 | +1.258 | 0.72 | 3.56 | 2.48% |
| MDLZ | ขาขึ้น (ชัด) | +3.3% / +7.3% / +11.1% | +3.59% | 61.2 | +0.369 | 0.81 | 1.70 | 2.55% |
| VZ | ออกข้าง (ชัด) | +3.5% / ใต้ MA50 +0.5% / +1.2% | +1.17% | 57.0 | +0.269 | 0.57 | 1.30 | 2.81% |
| KR | ขาขึ้น (ชัด) | +3.8% / +10.5% / +8.3% | +4.65% | 62.4 | +0.303 | 0.59 | 2.02 | 2.95% |
| DIS | ขาขึ้น (ชัด) | +5.5% / +9.9% / +15.5% | +3.92% | 70.6 | +0.744 | 0.98 | 2.57 | 2.15% |

## ระดับสำคัญ (swing จริง, 1D)

- **TJX**: R 139.83 EMA20 / 142.17 MA20 / 148.57 (2026-10-20 high) · S 135.91 MA50 / 134.69 (2026-11-06 low) / 122.78 (2026-09-16 low)
- **KO**: R 97.39 (2026-11-05 = 52w high) · S 93.71 EMA20 / 93.00 (2026-11-06 low) / 90.58 (2026-10-28 low)
- **TGT**: R 166.43 (2026-11-09 high) / 169.56 (2026-08-24 high) · S 157.92 (2026-11-10 low) / 152.48 (2026-09-16 low)
- **LVS**: R 41.73 (2026-11-09 high) / 43.57 (2026-07-23 high) / 47.11 (2026-08-25 high) · S 40.17 (2026-11-09 low) / 39.67 (2026-11-06 low) / 34.75 (2026-10-22 low)
- **WMT**: R 130.94 (2026-11-04 high) / 134.83 (52w high) · S 123.58 (2026-11-09 low) / 121.66 EMA20
- **PEP**: R 143.70 MA200 / 145.55 (2026-11-05 high) / 147.46 (2026-07-07 high) · S 139.00 (2026-10-22 high) / 131.85 (2026-10-28 low)
- **MDLZ**: R 68.75 (2026-11-05 = 52w high) · S 65.34 (2026-11-09 low) / 64.46 EMA20
- **VZ**: R 46.98 (2026-11-05 high) / 48.26 (2026-07-28 high) / 50.88 (2026-09-15 high) · S 45.51 EMA50 / 44.03 (2026-11-02 low) / 42.47 (2026-10-26 low)
- **KR**: R 68.56 (2026-10-23 high, เบรกแล้ว) / 71.64 (2026-11-05 high) / 75.66 (52w high) · S 66.82 (2026-11-09 low) / 66.11 EMA20
- **DIS**: R 120.80 (2026-11-05 = 52w high) · S 117.42 (2026-11-10 low) / 113.39 EMA20 / 110.75 (2026-10-30 low)

## scenario / plan สรุป

**ผ่าน gate ครบ 6 ชื่อ (stop ≥1.5×ATR, stop% ≤5.00%, R:R T2 net ≥2.0):**

| ticker | setup | entry | stop | T1 | T2 | R:R net T2 | T score |
|---|---|---|---|---|---|---|---|
| DIS | pullback EMA20 | 113.90–115.00 | 110.55 (1.52×ATR) | 120.80 | 130.85 (measured) | 3.99 | 7 |
| KO | pullback EMA20 | 93.60–94.80 | 90.40 (1.92×ATR) | 97.39 | 104.20 (measured) | 2.50 | 6 |
| KR | pullback MA20 | 67.40–68.00 | 64.65 (1.51×ATR) | 71.64 | 75.66 | 2.49 | 6 |
| PEP | breakout MA200 | 144.50–145.10 | 138.90 (1.66×ATR) | 147.46 | 159.25 (measured) | 2.33 | 5 |
| LVS | breakout 41.73 | 41.85–42.10 | 39.60 (1.86×ATR) | 43.57 | 47.11 | 2.08 | 6 |
| MDLZ | breakout 52w high | 68.85–69.00 | 65.60 (1.96×ATR) | 71.00 | 76.00 (measured) | 2.03 | 6 |

LVS: stop 5.66% > เพดาน 5.00% ⇒ full cap ทำไม่ได้ ขนาดสูงสุด ≈ $175.6 notional

**NO PLAN 4 ชื่อ:** TJX (ขาลง + gap งบ p95 4.29% ≥ stop 4.25%) · TGT (ATR 3.71% ⇒ stop 5.56% > เพดาน + gap p95 5.16% + R:R T2 net 1.21) · WMT (gap งบ p95 6.63% >> stop 3.81%) · VZ (R:R net 1.28)

## Earnings-gap check (SIP 1D, |open−prev close|/prev close, 4 ครั้งล่าสุด)

- **TJX** (2026-08-19, 05-20, 02-25, 2025-11-19): −4.45% / +1.46% / −0.07% / +3.38% → median **2.42%**, p95 **4.29%**, max 4.45%
- **TGT** (2026-08-19, 05-20, 03-03, 2025-11-19): −3.06% / −5.53% / +2.51% / −2.37% → median **2.79%**, p95 **5.16%**, max 5.53%
- **WMT** (2026-08-20, 05-21, 02-19, 2025-11-20): −6.93% / −4.93% / +1.49% / +3.31% → median **4.12%**, p95 **6.63%**, max 6.93%
- วันที่รายงานจาก Nasdaq `company/<SYM>/earnings-surprise` (ดึง 2026-11-11 10:24Z)

## Correlation (daily returns, SIP)

- **60d ≥0.5 (8/45 คู่):** PEP/MDLZ 0.752 · KO/PEP 0.708 · KO/MDLZ 0.671 · PEP/KR 0.560 · TGT/MDLZ 0.558 · KO/KR 0.554 · LVS/DIS 0.545 · TGT/PEP 0.542
- **20d ≥0.5 (32/45 คู่):** PEP/MDLZ 0.838 · WMT/KR 0.832 · WMT/MDLZ 0.824 · KO/MDLZ 0.821 · PEP/KR 0.821 · KO/PEP 0.802 · WMT/PEP 0.782 · MDLZ/VZ 0.781 (ที่เหลือ ≥0.70: KO/KR 0.759, TGT/DIS 0.757, MDLZ/KR 0.757, TGT/MDLZ 0.755, TJX/TGT 0.750, TJX/DIS 0.747, TJX/WMT 0.743, KO/WMT 0.740, TGT/WMT 0.701)
- ข้อสรุป: defensive/staples ทั้งลิสต์เคลื่อนไปทางเดียวกันใน 20 วัน ⇒ ถือ 2 ชื่อพร้อมกันแทบไม่ได้ diversification

## ข้อมูลที่ดึงไม่ได้

- Yahoo daily bars: HTTP 429 ทั้ง 10 ชื่อ (retry 4 ครั้ง) ⇒ ใช้ Nasdaq เป็นตัวตรวจซ้ำแทน
- NBBO/spread จริง: ตลาดปิด/pre-market ⇒ bid/ask indicative กว้างผิดปกติ (TJX 135.00/140.00) ใช้คำนวณ slippage ไม่ได้; slippage 0.15% ใน R:R เป็นสมมติฐาน (V)
- futures/pre-market จาก Yahoo: ไม่มี (429) — pre-market ใช้ Nasdaq `primaryData` (ET 04:00–05:19)
- VZ 52w low: SIP มี bad print 9.933 (2026-01-08) — ตัดออก, ใช้ 36.88 (2026-01-20)

## ลิงก์

[[trading-finance-moc]]
