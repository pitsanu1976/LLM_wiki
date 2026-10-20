---
title: "CRYPTO — Technical 2026-10-20 (round 8, 11 pairs)"
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
  - ticker/XRP
  - ticker/PAXG
  - ticker/AAVE
  - ticker/SOL
  - ticker/LINK
  - ticker/UNI
  - ticker/BCH
  - ticker/DOT
  - ticker/ARB
---

# CRYPTO — Technical read 2026-10-20 (round 8)

รอบ 8 แทน [[CRYPTO_tech_2026-10-20-r7]] (r7 = 7 คู่, quote 07:17Z) · รอบนี้ **11 คู่** ตาม work order: BTC, ETH, XRP, PAXG, AAVE, SOL, LINK, UNI, BCH, DOT, ARB
แท่ง 1D ปิดล่าสุด = **2026-10-19** (crypto 24/7 ⇒ แท่ง 20 ต.ค. ไม่ปิด ใช้เป็น reference เท่านั้น)

## แหล่งข้อมูล (ทุกตัวเลขดึงจริงรอบนี้)
- **Alpaca crypto v1beta3** bars 1Day/1Hour/15Min + snapshots/latest quotes/trades — ดึง **2026-10-20T13:21:04Z**
- **Coinbase Exchange** ticker 11/11 (13:22:48–13:23:18Z) · L2 book walk $3,000 (13:23:28–13:23:35Z) · 1D candles 17–21 ต.ค. (cross-check แท่งปิด)
- **CoinGecko** 11/11 (last_updated_at 13:22:57–13:23:06Z)
- cross-check แท่งปิด 19 ต.ค.: close ต่าง Alpaca−CB **−0.21% ถึง +0.036%** ⇒ ใช้ชุด Alpaca คำนวณ indicator ได้

## Trend + ความชัด
- **ออกข้างถึงขาลง — ชัดว่าไม่ใช่ขาขึ้น**: ราคาใต้ **EMA20(1D) ครบ 11/11 ที่ราคาปัจจุบัน** (แท่งปิด 19 ต.ค. ใต้ 10/11 · ARB ที่ปิดเหนือ +3.24% วันนี้หลุดลงมาแล้ว −1.57%)
- **ไม่มีคู่ไหน up_aligned ที่ราคาปัจจุบัน** · EMA20 slope ติดลบ 10/11 (แบนสุด DOT −0.02%, ชันสุด UNI −7.59%)
- MACD hist ติดลบ 9/11 แต่หดตัวขึ้นจาก 5 แท่งก่อน ⇒ ฟื้นของแรงลบ ไม่ใช่ reversal · RSI14 36.7–53.3 ไม่มี oversold/overbought
- ทุกคู่อยู่ครึ่งล่างของ range 24 ชม. (14.0%–44.4%) ⇒ ไม่มีใครเบรกเอาท์

## Indicator (แท่งปิดถึง 2026-10-19)
- **ATR(1D)**: BTC 2.54% · ETH 3.85% · PAXG 3.99% · XRP 4.78% · SOL 4.80% · LINK 5.84% · BCH 5.86% · AAVE 6.88% · DOT 7.84% · UNI 8.49% · ARB 8.76%
- **ATR > 5% ถึง 6 คู่** ⇒ stop ≥1×ATR ชนเพดาน 5% ทันที (LINK, BCH, AAVE, DOT, UNI, ARB)
- vs EMA20/50/200 (1D): BTC −0.80/+1.62/+7.78 · ETH −3.90/−3.09/+3.99 · XRP −5.34/−5.43/−5.26 · PAXG −1.11/−2.49/−0.17 · AAVE −5.68/+1.09/+19.40 · SOL −3.69/−1.69/+7.30 · LINK −5.63/−2.99/+10.26 · UNI −4.85/+0.01/+34.59 · BCH −1.22/+1.25/−8.40 · DOT −0.74/+4.11/−3.08 · ARB +3.24/+12.23/+50.76
- RSI14: BTC 48.00 · ETH 37.84 · XRP 36.68 · PAXG 39.92 · AAVE 43.66 · SOL 41.06 · LINK 40.99 · UNI 44.86 · BCH 48.25 · DOT 49.99 · ARB 53.30

## สรุปคำตัดสิน (stop ≥1×ATR · stop ≤5.0% · R2 ≥1.25)
- **ผ่าน 2 คู่ (แบบ limit ที่ 24h low): ETH** entry 2,371.37 / stop 2,278.81 (3.90%, 1.00×ATR) / T1 2,406.16 (R1 0.38) / T2 2,502.76 (EMA20 1D, **R2 1.42**) · **XRP** entry 1.28475 / stop 1.22254 (4.84%) / T1 1.32047 (R1 0.57) / T2 1.37618 (**R2 1.47**)
- **ETH~XRP corr 0.865 (30d) / 0.883 (7d)** ⇒ ถือได้ไม้เดียว
- **ที่ราคาตลาด 13:23Z เหลือคู่เดียวที่ยังผ่าน: XRP (stop 4.80%, R2 1.27 เฉียด)** — ETH ที่ตลาด R2 1.19 ตก
- **ไม่มีตั๋ว 9 คู่**: AAVE/LINK/UNI/BCH/DOT/ARB (stop เกินเพดานเพราะ ATR>5%) · BTC (R2 0.67) · PAXG (R2 0.48) · SOL (R2 1.10 + event 21 ต.ค.)
- **ตั๋วใช้ได้ถึง 2026-10-20 20:00Z** (ระดับอิง 24h window 19 ต.ค. 14:00Z→20 ต.ค. 12:00Z · drift 6.5 ชม. ≈ 0.3–0.5×ATR · T1 จะถูกคำนวณใหม่ที่ 4H close)

## Correlation
- **คู่ที่ corr <0.5 ทั้งสองหน้าต่างมี 10 คู่ และทุกคู่มี PAXG เป็นขาเดียว** — ไม่มีคู่ที่ไม่ใช่ PAXG เลย
- corr กับ BTC: 30d ต่ำสุด BCH 0.320 · 7d ต่ำสุด PAXG 0.413 (ไม่นับ PAXG = DOT 0.611)
- UNI~ARB 0.851/0.793 · UNI~BCH 0.809/0.813 ⇒ กลุ่มเดียวกัน

## ข้อควรระวังข้อมูล
- **ARB print 0.183134 (Alpaca 20 ต.ค. 04:00Z) เป็น feed artifact** — CB ต่ำสุด 0.18731 ⇒ ไม่ใช้เป็นแนวรับ
- **PAXG Alpaca ask bias +0.369%** (L1 ask depth $2) ⇒ ใช้ Coinbase สำหรับระดับราคา
- **ARB EMA200(1D) มีแค่ 246 แท่ง (ตั้งแต่ 2026-02-16)** = 8 เดือน ไม่ใช่ 1 ปี · 1H/4H history เริ่ม 2026-08-15
- เทปบาง: AAVE มี print แค่ 8/23 ชม. · ARB 12/23 · BCH 14/23 · UNI 15/23 · LINK 19/23
- ไม่มี notional/วัน จาก Coinbase candles ในรอบนี้ (ตัดออกเพื่อทันกำหนด 14:20Z)

รายงานฉบับเต็ม: `/opt/data/home/hermes-stock-team/workspace/reports/tech/2026-10-20-CRYPTO-r8.md`

[[trading-finance-moc]]
