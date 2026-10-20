---
title: "CRYPTO — สภาพคล่อง/ต้นทุน/valuation (sleeve) 2026 Q4"
type: source
status: active
created: 2026-10-19
updated: 2026-10-20
agent: finance
ticker: CRYPTO
scope: market
period: 2026-Q4
tags:
  - finance/earnings
  - ticker/CRYPTO
  - finance/liquidity
---

# CRYPTO sleeve — สภาพคล่อง / ต้นทุนไป-กลับ / valuation multiples (2026 Q4)

**รอบล่าสุด: r7 · ข้อมูล 2026-10-20 07:16:06Z** (orderbook 07:16:15Z · CoinGecko 07:24Z · Farside 07:29Z · Solana RPC 07:20:43–07:22:43Z · Alpaca fee docs 07:40Z)
**แหล่ง:** Alpaca Data API `/v1beta3/crypto/us/{trades,latest/trades,latest/quotes,latest/orderbooks,bars}` · CoinGecko `/coins/markets` + `/coins/{id}` · Farside `/btc /eth /sol` · DefiLlama `/unlocks/*` · Solana mainnet-beta RPC · mempool.space · blockchair
**ข้อจำกัดสำคัญ:** สินทรัพย์กลุ่มนี้ **ไม่มีงบการเงิน/ไม่มี audited statements** ⇒ P/E · P/BV · D/E · ROE · gross margin · dividend yield = **หาไม่ได้/n/a ทุกตัว** · ตัวเลขที่บันทึกคือ (ก) สภาพคล่องจากเทปจริง (ข) ต้นทุนไป-กลับ (ค) supply/vesting (ง) โครงสร้างตลาดของ venue
**รายงานฉบับเต็มของรอบ:** `workspace/reports/finance/2026-10-20-CRYPTO-r7.md`

## ตัวเลขหลัก (ไม้ $3,000 · 2026-10-20 07:16Z)

| symbol | notional 24 ชม. | notional 6 ชม. | 6 ชม. หักชม.สูงสุด | print ≥$3k 6 ชม./24 ชม. | last trade age | spread @$3k | **RT ไป-กลับ** | % ของ risk $150 | mcap / float |
|---|---|---|---|---|---|---|---|---|---|
| BTC/USD | **$338,702** | $51,658 | $15,024 | **3 / 8** | 16.9 น. | 10.61 bps | **0.682%** ($20.45) | **13.6%** | $1.641T · 100% |
| ETH/USD | $21,529 | $667 | $430 | 0 / 1 | 29.0 น. | 10.79 | **0.681%** ($20.43) | **13.6%** | $292.3B · 100% |
| ARB/USD | $16,543 | $5,018 | $88 | 1 / 2 | 39.5 น. | 33.42 | **0.834%** ($25.03) | 16.7% | $1.35B · 68.9% |
| XRP/USD | $24,921 | $2,340 | $1,059 | **0** / 2 | 11.0 น. | 40.25 | **0.902%** ($27.07) | 18.0% | $82.1B · 63.1% |
| BCH/USD | $5,745 | $5,310 | $114 | 1 / 1 | 31.5 น. | 63.70 | **1.137%** ($34.11) | 22.7% | $5.56B · 100% |
| SOL/USD | $110,209 | $102,851 | **$841** | 11 / 11 | 29.2 น. | 70.28 | **1.634%** ($49.02) | 32.7% | $61.6B · 92.7% |
| PAXG/USD | $3,800 | $839 | $581 | **0 / 0** | 10.4 น. | **121.18** | **1.764%** ($52.91) | **35.3%** | $1.82B · 100% |

`[calc]` RT = taker 0.25%×2 (=0.50%, docs.alpaca.markets/us/docs/crypto-trading tier 1, ยืนยัน 2026-10-20) + spread ระหว่าง level ที่สะสมของได้ ≥$3,000 + slip buy + slip sell · ค่าธรรมเนียมเป็นก้อนใหญ่สุด: $15 = 73% ของ RT BTC, 60% ARB, 55% XRP, 28% PAXG
`[alt measure]` ถ้าวัดด้วย median quote spread 3 ชม. (ไม่ขึ้นกับ book snapshot): BTC 0.606% · ETH 0.605% · ARB 0.891% · XRP 0.945% · SOL 1.027% · BCH 1.293% · PAXG 1.715%

## ข้อเท็จจริงเชิงโครงสร้างที่วัดซ้ำได้ (สะสมหลายรอบ)

1. **L1 ไม่ใช่ต้นทุน:** BTC L1 spread 2.48 bps แต่ไม้ $3,000 จ่าย 10.61 bps เพราะ L1 มีของ $81 (ETH $79, SOL $99, PAXG **$22**) — ต้อง walk book ถึงขนาดไม้เสมอ
2. **"ผ่านเกตเทป" ≠ "ออกที่ stop ได้":** r7 ผ่านเกต 4 คู่ แต่ SOL ผ่านด้วย print 11 ครั้งใน **8 วินาที** (03:53:27–34Z, 92.6% ของชั่วโมง) · ARB/BCH ผ่านด้วย print เดียว · BTC พึ่ง 2 print 19 ต.ค. 07:34Z = 47.9% ของวัน
3. **notional 24 ชม. หลอกได้ทุกคู่:** BTC 8 print ≥$3k = $218,247 (64% ของวัน) · XRP 2 print 07:43:20Z = 58% · BCH 1 print = 90% · PAXG print ใหญ่สุด $486
4. **Venue ไม่มี stop-market:** Alpaca crypto รองรับเฉพาะ Market / Limit / **Stop Limit** (tif gtc, ioc), ไม่มี margin, ไม่มี short, ≤$200k/คำสั่ง ⇒ คำสั่ง stop ทุกใบเป็น limit ที่รอใน book ไม่มีการไล่ราคา — นี่คือเหตุผลเชิงโครงสร้างที่ทำให้ยืนยัน "ออกที่ stop ด้วย market order" ไม่ได้ (r6 พบปัญหาเดียวกัน)
5. **Book ลึกแต่ห่าง ≠ ใช้งานได้:** PAXG cum ask depth $668,450 แต่ L1 ask $22 และ spread 116–121 bps; ARB cum depth $1.67M แต่เทปมี print แค่ 11/26 ชั่วโมง (gap 299 นาที)
6. **basis last-vs-mid ต้องตรวจทุกครั้ง:** r6 เจอ ARB เพี้ยน −2.80%; r7 ราคา last trade ทุกคู่ยังอยู่ในกรอบ ±0.6% ของ mid

## Supply / overhang (2026-10-20)

- **BTC** circ 20,098,843 = total · ไม่มี unlock · halving ถัดไป block 1,050,000 (tip 972,280 ⇒ ~77,720 block ≈ 540 วัน) · **BCH** tip 973,670 ⇒ halving ~529 วัน
- **ETH** circ = total 122,151,332 · **net issuance หาไม่ได้** (ultrasound API คืนว่าง)
- **SOL** circ 589.49M / total 636.09M (92.7%) · **inflation 3.5953%/ปี** (RPC epoch 1062) ≈ 1.76M SOL/เดือน ≈ $184M/เดือน
- **XRP** circ 63.13B / 99.99B (63.1%) · ตาราง escrow รายเดือน **ยังยืนยันไม่ได้** (ไม่มี endpoint ฟรี)
- **ARB** circ 6.892B / 10B (68.9%) · **unlock 15/16 พ.ย. 2026 ~92.65M ARB ≈ $17–18M = 1.34% ของ float** (DefiLlama unlocks + Tokenomist — ตรงกันเรื่องขนาด ต่างกันเรื่องวัน)
- **PAXG** 441,809 oz = total · ไม่มี vesting (ค้ำทอง)

## ETF flow (Farside, 7 session 09–19 ต.ค. 2026)

BTC **+$319.4M** (19 ต.ค. +$526.7M) · ETH **−$479.5M** (19 ต.ค. −$103.3M) · SOL **−$36.0M** (19 ต.ค. −$6.7M) · XRP/PAXG/ARB/BCH = **ไม่มีหน้าใน Farside ⇒ ดึงไม่ได้**
`[cross-check]` BTC 12–16 ต.ค. = −$228.4M ตรงกับที่บันทึกในรอบ r6 ⇒ parser Total-column ใช้ได้ (DefiLlama `/etfs` เป็นหน้า stale "May 15, 2026" — ห้ามใช้)

## Event 72 ชม.

- **SOL Alpenglow epoch 1064** — วัด slot rate จริง 217.5 ms/slot (459,145,196 → 459,145,750 ใน 120 วินาที, 07:20:43–07:22:43Z) ⇒ epoch 1064 เริ่ม **~2026-10-21 13:43Z**, handoff ที่ slot 459,653,000 **~14:01Z**; แหล่งอื่น: solana.com ~13:20Z · Anza ~14:50Z · CoinDesk ~15:00Z ⇒ **ใช้กรอบ 13:20–15:30Z ห้ามอ้างวินาทีเดียว**
- ARB: ไม่มี event ใน 72 ชม. (unlock ถัดไป พ.ย.) · BTC/ETH/XRP/BCH/PAXG: ไม่พบ

## จุดที่ต้องจับตา (สำหรับรอบถัดไป)

1. **ค่าธรรมเนียม = ครึ่งหนึ่งของต้นทุนในคู่ที่ spread กว้าง** — ถ้า volume 30 วันขึ้น tier 2 (taker 22 bps) ตัวเลข RT ทั้งตารางจะขยับ ~6 bps; ต้องถาม Leader ว่าใช้ tier ไหน
2. **SOL ต้องวัด 2 ครั้ง:** book-walk ให้ 1.634% แต่ median quote 1.027% — book snapshot บางเฉียบชั่วขณะ อย่ารายงานตัวเดียว
3. **XRP ยังไม่มี print ≥$3k ใน 6 ชม.** ทั้งที่ 24 ชม. อันดับ 3 — เกต 6 ชม. คือเกตที่ถูก ไม่ใช่ 24 ชม.
4. **ห้ามใช้ DefiLlama `/etfs`** (stale) และ `/emissions` (HTTP 402) — ใช้ Farside และหน้า unlocks แทน

---
ลิงก์: [[CRYPTO]] · [[trading-finance-moc]]
