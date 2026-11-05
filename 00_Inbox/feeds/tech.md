---
title: "tech.md"
type: source
status: active
agent: leader
created: 2026-11-05
updated: 2026-11-05
source_mtime: 2026-11-01 13:20 UTC
source_sha256: 643a7c950ae817f8
tags:
  - source/feed
  - domain/trading
related:
  - "[[trading-finance-moc]]"
source: "workspace/raw/tech.md"
---

> 🔁 สำเนาอัตโนมัติจาก `workspace/raw/tech.md` (mtime 2026-11-01 13:20 UTC) — **ห้ามแก้ด้วยมือ** ระบบเขียนทับจากต้นฉบับ
> Technical feed — setup/entry/stop/target/ATR/corr

# raw/tech.md — Technical Agent Feed

- วิเคราะห์เมื่อ: 2026-11-01 (ตลาดปิด · อาทิตย์) · แท่งล่าสุดที่ปิดแล้ว = **2026-10-30 (Fri)**
- แหล่ง OHLCV: stockanalysis.com history API (`/api/symbol/s/<T>/history?range=5Y&period=Daily`), ดึง 2026-11-01 · SPY ใช้คำนวณ relative strength (ไม่ได้ใส่เป็นคอลัมน์)
- indicator คำนวณด้วยโค้ดทั้งหมด: SMA/EMA, RSI14 Wilder, MACD 12/26/9, OBV, ATR14 Wilder, ADX14 Wilder (+DI/-DI), RVOL, ADV20, swing pivot 5-bar (500 แท่ง)
- จับคู่กับ `raw/news.md` (สแกน 2026-11-01 09:57–10:02 UTC) ตาม news_id
- **เพิ่ม 4 คอลัมน์จาก v1**: `ADX14 (+DI/-DI)` · `volume & liquidity` · `ATR14 / ระยะจาก SMA20` · `S/R · entry/stop/target`

| tech_id | refer improve_id | tech_date | news_id | stock | moving average | ADX14 (+DI/-DI) | candlestick pattern | on balance volume | volume & liquidity (RVOL / ADV20) | RSI | ATR14 / ระยะจาก SMA20 | S/R · entry / stop / target | scoring (1-10)[10 recommend buy, 1 recommend sell, 5 hold] |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TECH-20261101-01 | — | 2026-11-01 | NEWS-20261030-01 | REGN | 1D 2026-10-30: close 927.89 · SMA20 788.89 / SMA50 793.30 / SMA200 737.54 · +17.62% vs SMA20, +16.97% vs SMA50, +25.81% vs SMA200 · SMA20 < SMA50 (-0.56%), SMA50 > SMA200 (+7.56%) | ADX14 26.9 · +DI 46.8 / -DI 8.8 → เทรนด์ชัด · ทิศ ขึ้น | 1D 2026-10-30: O 869.43 H 935.35 L 839.08 C 927.89 · gap up +6.19% · body 61% · close อยู่ 92% ของช่วง · wick บน 8% / ล่าง 32% → แท่งขึ้นชัด ปิดครึ่งบนของช่วง | OBV 8.22M vs OBV MA20 4.00M · 20 วัน +44.9% ของ volume 20 วัน | RVOL 3.85x (vol 2,870,655 / MA20 745,167) · ADV20 $604M | RSI14 79.11 (overbought) · MACD 20.98 / signal 9.54 / hist +11.43 (prev +5.08) | ATR14 27.10 (2.92% ของราคา) · ราคาห่าง SMA20 = 5.13 ATR | S 779.08 (2026-08-31) · R ไม่มี swing เหนือราคา (52w high 935.35) → entry 860.15–887.25 · stop 833.05 · T1 935.35 / T2 975.99 · R:R 1.52 | 7 |
| TECH-20261101-02 | — | 2026-11-01 | NEWS-20261030-02 | GDDY | 1D 2026-10-30: close 117.24 · SMA20 106.08 / SMA50 101.43 / SMA200 91.92 · +10.52% vs SMA20, +15.58% vs SMA50, +27.54% vs SMA200 · SMA20 > SMA50 (+4.58%), SMA50 > SMA200 (+10.35%) | ADX14 30.9 · +DI 38.8 / -DI 20.9 → เทรนด์ชัด · ทิศ ขึ้น | 1D 2026-10-30: O 103.70 H 118.11 L 103.70 C 117.24 · เปิด gap down -2.07% จาก prev close 105.89 · body 94% · close อยู่ 94% ของช่วง · wick บน 6% / ล่าง 0% → bullish marubozu ปิดใกล้ high | OBV 164.51M vs OBV MA20 162.25M · 20 วัน +18.8% ของ volume 20 วัน | RVOL 2.14x (vol 3,574,957 / MA20 1,672,436) · ADV20 $179M | RSI14 66.07 · MACD 3.15 / signal 2.80 / hist +0.35 (prev -0.19) | ATR14 4.84 (4.13% ของราคา) · ราคาห่าง SMA20 = 2.31 ATR | S 94.02 (2026-08-26) · R 131.74 (2025-12-04) → entry 112.40–114.82 · stop 106.35 · T1 131.74 / T2 136.58 · R:R 2.50 | 9 |
| TECH-20261101-03 | — | 2026-11-01 | NEWS-20261030-03 | CROX | 1D 2026-10-30: close 150.52 · SMA20 122.22 / SMA50 120.40 / SMA200 109.92 · +23.16% vs SMA20, +25.01% vs SMA50, +36.94% vs SMA200 · SMA20 > SMA50 (+1.51%), SMA50 > SMA200 (+9.54%) | ADX14 18.9 · +DI 46.2 / -DI 9.4 → ไม่มีเทรนด์ชัด (<20) · ทิศ ขึ้น | 1D 2026-10-30: O 151.73 H 154.05 L 149.00 C 150.52 · ไม่มี gap (+0.98%) · body 24% · close อยู่ 30% ของช่วง · wick บน 46% / ล่าง 30% → spinning top / แรงขายที่ high | OBV -89.16M vs OBV MA20 -97.37M · 20 วัน +50.8% ของ volume 20 วัน | RVOL 1.65x (vol 2,119,755 / MA20 1,287,236) · ADV20 $164M | RSI14 77.75 (overbought) · MACD 4.25 / signal 1.10 / hist +3.16 (prev +2.03) | ATR14 6.02 (4.00% ของราคา) · ราคาห่าง SMA20 = 4.70 ATR | S 119.74 (2026-07-08) · R ไม่มี swing เหนือราคา (52w high 154.05) → entry 135.46–141.48 · stop 129.44 · T1 154.05 / T2 163.09 · R:R 1.72 | 7 |
| TECH-20261101-04 | — | 2026-11-01 | NEWS-20261030-04 | TMUS | 1D 2026-10-30: close 156.44 · SMA20 155.81 / SMA50 167.13 / SMA200 186.96 · +0.41% vs SMA20, -6.39% vs SMA50, -16.32% vs SMA200 · SMA20 < SMA50 (-6.77%), SMA50 < SMA200 (-10.61%) | ADX14 23.4 · +DI 26.5 / -DI 29.3 → เทรนด์กำลังก่อตัว · ทิศ ลง | 1D 2026-10-30: O 150.00 H 158.99 L 149.71 C 156.44 · gap up +1.84% · body 69% · close อยู่ 73% ของช่วง · wick บน 27% / ล่าง 3% → แท่งขึ้นชัด ปิดครึ่งบนของช่วง | OBV 131.27M vs OBV MA20 120.58M · 20 วัน +18.8% ของ volume 20 วัน | RVOL 1.60x (vol 11,498,166 / MA20 7,165,401) · ADV20 $1103M | RSI14 48.52 · MACD -4.79 / signal -5.03 / hist +0.24 (prev -0.46) | ATR14 5.91 (3.77% ของราคา) · ราคาห่าง SMA20 = 0.11 ATR | S 147.90 (2026-10-09) · R 171.80 (2026-10-08) → entry 154.67–157.62 · stop 146.42 · T1 171.80 / T2 177.71 · R:R 1.61 | 6 |
| TECH-20261101-05 | — | 2026-11-01 | NEWS-20261030-05 | FDXF | 1D 2026-10-30: close 126.04 · SMA20 111.73 / SMA50 118.83 / SMA200 n/a (ประวัติ 109 แท่ง) · +12.80% vs SMA20, +6.07% vs SMA50 · SMA20 < SMA50 (-5.97%) | ADX14 31.5 · +DI 35.1 / -DI 19.4 → เทรนด์ชัด · ทิศ ขึ้น | 1D 2026-10-30: O 115.20 H 128.00 L 115.20 C 126.04 · gap up +5.02% · body 85% · close อยู่ 85% ของช่วง · wick บน 15% / ล่าง 0% → bullish marubozu ปิดใกล้ high | OBV -28.03M vs OBV MA20 -28.90M · 20 วัน -1.9% ของ volume 20 วัน | RVOL 2.45x (vol 3,597,309 / MA20 1,468,724) · ADV20 $166M | RSI14 67.09 · MACD -1.40 / signal -3.00 / hist +1.59 (prev +0.50) | ATR14 5.27 (4.18% ของราคา) · ราคาห่าง SMA20 = 2.72 ATR | S 107.67 (2026-10-01) · R 135.70 (2026-09-01) → entry 120.77–123.41 · stop 114.19 · T1 135.70 / T2 140.97 · R:R 1.72 | 6 |

## หมายเหตุประกอบ (ไม่ใช่ส่วนของตาราง)

**สูตรคะแนน (คำนวณด้วยโค้ด — ตรวจย้อนได้ทุกบรรทัด)**
trend 4 (px>MA20, MA20>MA50, px>MA200, MA50>MA200) + momentum 2 (MACD hist>0 และ hist เพิ่ม) + volume/OBV 2 (RVOL≥1.5x, OBV>MA20 และ OBV 20 วันเพิ่ม) + entry 2 (ระยะจาก SMA20 เป็น ATR) - หัก 0.5 ถ้า RSI>75 หรือเหลือ <1 ATR ถึงแนวต้าน - **หัก ADX**: ADX<20 = -1.0, ADX 20–25 = -0.25, ADX≥25 = 0 · **cap 6** ถ้า px<MA50 · **cap 7** ถ้า ext>4 ATR

- REGN **7** (base 7.00 - ADX 0.00 = 7.00, cap7 ext>4ATR) — trend 3/4 · mom 2/2 · vol 2/2 · entry 0/2 · ext 5.13 ATR · R:R 1.52 · หัก: RSI>75
- GDDY **9** (base 9.00 - ADX 0.00 = 9.00) — trend 4/4 · mom 2/2 · vol 2/2 · entry 1/2 · ext 2.31 ATR · R:R 2.50
- CROX **7** (base 8.00 - ADX 1.00 = 7.00, cap7 ext>4ATR) — trend 4/4 · mom 2/2 · vol 2/2 · entry 0/2 · ext 4.70 ATR · R:R 1.72 · หัก: RSI>75
- TMUS **6** (base 6.00 - ADX 0.25 = 5.75, cap6 px<MA50) — trend 1/4 · mom 1/2 · vol 2/2 · entry 2/2 · ext 0.11 ATR · R:R 1.61
- FDXF **6** (base 6.00 - ADX 0.00 = 6.00) — trend 2.0/4 · mom 2/2 · vol 1/2 · entry 1/2 · ext 2.72 ATR · R:R 1.72

**ระดับสำคัญและแผน (1D · swing pivot 5-bar/500 แท่ง · ATR-based)**
- REGN: entry 860.15–887.25 · stop 833.05 · T1 935.35 / T2 975.99 · R:R 1.52 (รอย่อ เพราะ ext 5.13 ATR)
- GDDY: entry 112.40–114.82 · stop 106.35 · T1 131.74 / T2 136.58 · R:R 2.50
- CROX: entry 135.46–141.48 · stop 129.44 · T1 154.05 / T2 163.09 · R:R 1.72 (ADX 18.9 = ยังไม่มีเทรนด์จริง)
- TMUS: entry 154.67–157.62 · stop 146.42 · T1 171.80 / T2 177.71 · R:R 1.61
- FDXF: entry 120.77–123.41 · stop 114.19 · T1 135.70 / T2 140.97 · R:R 1.72

**สภาพคล่อง/ความผันผวน (คำนวณ)**
- ADV20 (มูลค่าซื้อขายเฉลี่ย): REGN $604M · GDDY $179M · CROX $164M · TMUS $1103M · FDXF $166M
- ATR14: REGN 27.10 (2.92% ของราคา) · GDDY 4.84 (4.13% ของราคา) · CROX 6.02 (4.00% ของราคา) · TMUS 5.91 (3.77% ของราคา) · FDXF 5.27 (4.18% ของราคา)
- stop ทุกตัวอิง 1.5 ATR จาก mid ของ entry และไม่เกิน 2.5 ATR — แคบกว่านั้นถือว่าโดน noise

**ข้อมูลที่ดึงไม่ได้**
- Yahoo Finance chart API คืน HTTP 429 ทุก ticker (2026-11-01 10:06 UTC) → ใช้ stockanalysis.com แทน; ตรวจแล้วราคาปิด 30 ต.ค. ตรงกับ `news.md` ทั้ง 5 ตัว
- FDXF ไม่มี MA200 (ประวัติ 109 แท่งตั้งแต่ spin-off 28 พ.ค. 2026) → trend คิดจาก 2 เงื่อนไขที่วัดได้ ปรับสเกลเป็น 4
