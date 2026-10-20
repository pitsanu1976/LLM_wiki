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

**รอบล่าสุด: r8 · ข้อมูล 2026-10-20 13:21:02Z** (orderbook 13:21:11Z · quotes 3 ชม. ถึง 13:21Z · CoinGecko 13:23–13:25Z · Farside 13:26Z · DefiLlama unlocks 13:30–13:34Z · Alpaca fee docs 13:27Z)
**แหล่ง:** Alpaca Data API `/v1beta3/crypto/us/{trades,quotes,latest/trades,latest/quotes,latest/orderbooks,bars}` · CoinGecko `/coins/markets` + `/coins/{id}` · Farside `/btc /eth /sol` · DefiLlama `/unlocks/*` · docs.alpaca.markets `crypto-fees`, `crypto-trading`
**ข้อจำกัดสำคัญ:** สินทรัพย์กลุ่มนี้ **ไม่มีงบการเงิน/ไม่มี audited statements** ⇒ P/E · P/BV · D/E · ROE · gross margin · dividend yield = **หาไม่ได้/n/a ทุกตัว** · ตัวเลขที่บันทึกคือ (ก) สภาพคล่องจากเทปจริง (ข) ต้นทุนไป-กลับ (ค) supply/vesting (ง) โครงสร้างตลาดของ venue
**รายงานฉบับเต็มของรอบ:** `workspace/reports/finance/2026-10-20-CRYPTO-r8.md`

## ตัวเลขหลัก (2026-10-20 13:21Z · 11 คู่ตามลิสต์ Leader · taker tier 1)

| symbol | notional 24 ชม. | 24 ชม. ex-top-2 ชม. | 6 ชม. | **6 ชม. ex-top-hour** | print ≥$1k 6ชม./24ชม. | last age | L1 spread | **eff spread @$3k** | **RT @$1k / @$3k** | % ของ $150 (@$1k/@$3k) | mcap · circ/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BTC/USD | $180,728 | $48,804 | $17,854 | **$4,505** | 2 / 20 | 4.0 น. | 2.91 bps | 8.52 bps | **0.576% / 0.585%** | 3.8% / 11.7% | $1.636T · 100% |
| ETH/USD | $37,651 | $16,267 | $25,322 | **$13,486** | 3 / 5 | 4.0 น. | 2.88 | 9.94 | **0.589% / 0.599%** | 3.9% / 12.0% | $292.3B · 100% |
| XRP/USD | $9,389 | $7,031 | $1,736 | $873 | 0 / 1 | 1.0 น. | 33.16 | 33.16 | 0.832% / 0.832% | 5.5% / 16.6% | $81.9B · 63.1% |
| SOL/USD | $109,935 | $6,634 | $571 | $376 | 0 / 33 | 11.1 น. | 9.10 | 46.73 | 0.792% / 0.967% | 5.3% / 19.3% | $61.5B · 92.7% |
| LINK/USD | $3,845 | $1,861 | $604 | $157 | 0 / 1 | 26.0 น. | 19.40 | 19.40 | 0.694% / 0.694% | 4.6% / 13.9% | $9.17B · 76.7% |
| BCH/USD | $5,835 | $253 | $412 | $26 | 0 / 1 | 0.7 น. | 60.88 | 60.88 | 1.109% / 1.109% | 7.4% / 22.2% | $5.49B · 100% |
| UNI/USD | $2,990 | $917 | $1,375 | $400 | 0 / 0 | 13.0 น. | 17.82 | 17.82 | 0.678% / 0.678% | 4.5% / 13.6% | $4.47B · 70.4% |
| AAVE/USD | $2,025 | $396 | $47 | **$5** | 0 / 0 | 21.0 น. | 15.43 | 15.43 | 0.654% / 0.654% | 4.4% / 13.1% | $2.30B · 96.5% |
| DOT/USD | $1,367 | $751 | $220 | $114 | 0 / 0 | 7.5 น. | 18.29 | 32.30 | 0.712% / 0.823% | 4.7% / 16.5% | $1.94B · 100% |
| PAXG/USD | $3,928 | $2,809 | $826 | $331 | 0 / 0 | 3.9 น. | 81.22 | 115.23 | 1.650% / 1.652% | 11.0% / 33.0% | $1.82B · 100% (441,809 oz) |
| ARB/USD | $17,110 | $3,825 | $567 | $20 | 0 / 3 | 20.7 น. | 30.32 | 30.32 | 0.803% / 0.803% | 5.4% / 16.1% | $1.30B · 68.9% |

`[calc]` RT = 2×0.25% taker (tier 1, docs 2026-10-20) + eff spread = (buy VWAP − sell VWAP)/mid ที่ขนาดนั้น (walk book จริง 2–4 ระดับ) ⇒ **ไม่นับซ้ำ** spread/slippage (แก้ข้อผิดของ r7 ที่นับซ้ำ 2–4 bps)
`[calc]` ค่าธรรมเนียมเป็นก้อนใหญ่สุดที่ขนาดเล็ก: ที่ $1,000 fee $5.00 = 87% ของ RT BTC · 85% ETH · 60% XRP · 30% PAXG
`[key]` **ต้นทุนเป็น % ไม่ลดตามขนาด** (BTC 0.585→0.576% เมื่อ $3,000→$1,000 = 0.9 bps) แต่ **% ของ risk budget ลดเป็นเส้นตรง** (11.7%→3.8%) — "ลดขนาด" แก้เรื่องเงินที่จ่าย ไม่ได้แก้เรื่องความแพงต่อหน่วย

## เพดานขนาดที่วัดได้ (เกต: N ≤ 6h ex-top-hour AND N ≤ 20% bid depth AND last age ≤ 30 น.)

BTC **$4,505** · ETH **$13,486** · XRP $873 · UNI $400 · SOL $376 · PAXG $331 · LINK $157 · DOT $114 · BCH $26 · ARB $20 · AAVE $5
`[view]` เกตที่ผูกจริงคือเทป (6h ex-top) ไม่ใช่ depth — bid depth ต่ำสุด DOT $26,696 = 26.7× ของไม้ $1,000 ⇒ **"ไม่มีของใน book" ไม่ใช่ปัญหา; ปัญหาคือ book อาจถูก pull และเทปไม่เคยพิสูจน์ว่ามีคนเทรดขนาดนั้น**

## ข้อเท็จจริงเชิงโครงสร้างที่วัดซ้ำได้ (สะสมหลายรอบ)

1. **L1 ไม่ใช่ต้นทุน:** BTC/ETH L1 spread 2.9 bps แต่ L1 มีของข้างละ **$80–$81** ⇒ ไม้ $3,000 ไต่ 3 ระดับ จ่ายจริง 8.5–9.9 bps (3.0–3.4×) · PAXG L1 ask **$2** · SOL $99–100
2. **"notional 24 ชม. สูง" แทบไม่มีความหมาย:** r8 — BTC 73% ของวันอยู่ใน 2 ชั่วโมง (19 ต.ค. 14Z + 20 ต.ค. 02Z) · SOL **92.8% อยู่ในชั่วโมง 03Z** (33 print ≥$1,000 ทั้งหมดอยู่ในชั่วโมงเดียว) · ETH 6 ชม. = 3 print (89.6%) · BCH 88.8% = print เดียว · ARB 77.6% = 2 ชั่วโมง
3. **Venue ไม่มี stop-market:** Alpaca crypto รองรับ **Market / Limit / Stop Limit** (tif `gtc`, `ioc`) เท่านั้น (docs, 13:27Z) ⇒ "ออกที่ stop ด้วย market order" เป็นคำสั่งเดียวบน venue ไม่ได้; stop_limit ที่ราคา gap ผ่านจะ **ไม่ fill เลย** ไม่ใช่ fill แย่ลง — คนละความเสี่ยงกับ slippage
4. **เทปขาดเป็นปกติของ small cap:** r8 hours-with-tape (25 ชม.) — AAVE **11/26** (gap 519.8 น.) · ARB 14/26 (299 น.) · BCH 16/26 (179 น.) · UNI 17/26 (303 น.) · LINK 21/26 (170 น.) · DOT 22/26 (179 น.) ส่วน BTC/ETH/XRP/PAXG/SOL มี print ทุกชั่วโมง
5. **basis last-vs-mid ต้องตรวจทุกครั้ง:** r6 ARB −2.80% · r7 ทุกคู่ ±0.6% · **r8 UNI −0.345% (เกินครึ่ง spread 8.9 bps ⇒ ต้นทุนจริง ~0.94% ไม่ใช่ 0.678%)**, XRP −0.220%, BCH −0.296%, PAXG +0.406%, LINK +0.148%
6. **การลดขนาดไม่ได้ช่วยคู่ที่เทปตาย:** 9 ใน 11 คู่มีเพดานต่ำกว่า $1,000 อยู่แล้ว ⇒ ที่ $1,000 ยังผ่านแค่ BTC/ETH (2/11) เท่ากับที่ $3,000

## Supply / overhang (2026-10-20)

- **BTC** circ 20,098,843 = total · ไม่มี unlock · **BCH** circ 20,105,203 = total · ไม่มี vesting
- **ETH** circ = total 122,151,332 · net issuance หาไม่ได้ (ultrasound API คืนว่าง)
- **SOL** circ 589.55M / total 636.09M (92.7%) · **unlock ถัดไป 11 พ.ย. 2026 03:24Z** (linear 397,300 SOL/สัปดาห์ = $41.23M/สัปดาห์ = 0.055% ของ circ / 0.067% ของ float, DefiLlama 13:31Z)
- **XRP** circ 63.13B / 99.99B (63.1%) · escrow 1B XRP/เดือน (ต้นเดือนถัดไป = 1 พ.ย.) — ยังไม่ยืนยันตัวเลข net รอบนี้
- **ARB** circ 6.892B / 10B (68.9%) · **unlock 15/16 พ.ย. 2026 ~92.65M ARB ≈ $17–18M = 1.34% ของ float** (จาก r7; หน้า unlocks/arbitrum วันนี้ stale — ราคาหน้า $0.099 vs จริง $0.1878)
- **LINK** circ 766.85M / 1B · **ไม่มี unlock ที่จะถึง**; cliff ล่าสุด 9 ต.ค. 2026 = $224.81M / 18.75M LINK (1.88% ของ circ)
- **UNI** circ 624.70M / 886.94M · ไม่มี unlock ตามกำหนด; vesting ทีม/investor $13.65M/สัปดาห์
- **AAVE** circ 15.44M / 16M · ไม่มี unlock (DefiLlama 13:34Z)
- **DOT** circ 1.708B = total · **unlock ไม่ทราบ** (defillama.com/unlocks/polkadot = CRAWL_NOT_FOUND)
- **PAXG** 441,809 oz = total · ไม่มี vesting (ค้ำทอง)

## ETF flow (Farside, ดึง 13:26Z)

BTC **−$228.4M** (12–16 ต.ค.) → **19 ต.ค. +$526.7M** · ETH **−$320.1M** (12–16 ต.ค.) → 19 ต.ค. −$103.3M (session ที่ 10 ติดลบ) · SOL **−$25.5M** (12–16 ต.ค.) → 19 ต.ค. −$6.7M · 20 ต.ค. ทุกคู่ $0.0M (ยังไม่รายงาน)
`[cross-check]` ผลรวม 12–16 ต.ค. ตรงกับที่ news รายงาน (BTC −228.4 / ETH −320.1) ⇒ parser Total-column ใช้ได้ · **DefiLlama `/etfs` เป็นหน้า stale "May 15, 2026" — ห้ามใช้** · XRP/PAXG/ARB/BCH ไม่มีหน้าใน Farside ⇒ ดึงไม่ได้ (farside.co.uk/xrp/ = HTTP 404)

## Event 72 ชม.

- **SOL Alpenglow epoch 1064** — solana.com ระบุ ~13:20Z 21 ต.ค. · Vortex ~13:45Z · r7 วัด slot rate 217.5 ms/slot ⇒ ~13:43Z handoff ~14:01Z ⇒ **ใช้กรอบ 13:20–15:30Z ห้ามอ้างวินาทีเดียว**
- XRP amendment `fixCleanup3_4_0` คาด activate 23 ต.ค. ~09:34Z (ทุติยภูมิ มีเงื่อนไข 30/36 validator)
- ไม่พบ event 72 ชม. ของ BTC/ETH/BCH/PAXG/ARB/LINK/UNI/AAVE/DOT

## จุดที่ต้องจับตา (สำหรับรอบถัดไป)

1. **ETH เพิ่งกลายเป็นคู่ที่เทปหนาสุดบนกระดาน (6h ex-top $13,486)** — แต่มาจาก 3 print; รอบหน้าต้องวัดซ้ำว่ามี print ≥$1,000 ต่อเนื่องหรือกลับไปเป็น 0 เหมือน r7 (ซึ่ง ETH 6h = $667, 0 print ≥$1k)
2. **ขอ Leader ยืนยัน fee tier 30 วัน** — ทั้งตารางคิดบน tier 1 (0.25% taker); tier 2 = 0.22% จะลดทุกช่อง ~6 bps
3. **ห้ามใช้ DefiLlama `/etfs`** (stale "May 15, 2026") และ `/emissions` (402); **หน้า `/unlocks/<slug>` บางหน้าคืน snapshot เก่า** (ARB) — ต้องเทียบราคาในหน้ากับ CoinGecko ก่อนใช้ทุกครั้ง
4. **stop_limit ไม่ใช่ stop-market** — ถ้า Leader จะใช้ stop ต้องตัดสินใจเรื่อง limit price + ยอมรับความเสี่ยง "ไม่ fill เลย"

---
ลิงก์: [[CRYPTO]] · [[trading-finance-moc]]
