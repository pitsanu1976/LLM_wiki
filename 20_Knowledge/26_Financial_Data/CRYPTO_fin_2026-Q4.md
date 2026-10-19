---
title: "CRYPTO — สภาพคล่อง/ต้นทุน/valuation (sleeve) 2026 Q4"
type: source
status: active
created: 2026-10-19
updated: 2026-10-19
agent: finance
ticker: CRYPTO
period: 2026-Q4
tags:
  - finance/earnings
  - ticker/CRYPTO
  - finance/liquidity
---

# CRYPTO sleeve — สภาพคล่อง / ต้นทุนไป-กลับ / valuation multiples (2026 Q4)

**รอบล่าสุด: r6 · ข้อมูล 2026-10-19 22:05:57Z** (orderbook 22:06:06Z · CoinGecko+DefiLlama 22:07:32Z · Farside 22:08Z · glif RPC + Solana RPC 22:08:37Z)
**แหล่ง:** Alpaca Data API `/v1beta3/crypto/us/{trades,latest/trades,latest/quotes,latest/orderbooks}` · CoinGecko `/coins/markets` · DefiLlama `/summary/fees` · Farside `/btc /eth /sol /hyp` · Solana RPC · Filecoin glif RPC
**ข้อจำกัดสำคัญ:** สินทรัพย์กลุ่มนี้ **ไม่มีงบการเงิน/ไม่มี audited statements** ⇒ P/E · P/BV · D/E · ROE · gross margin · dividend yield = **หาไม่ได้/n/a ทุกตัว** · ตัวเลขที่บันทึกไว้คือ (ก) สภาพคล่องที่วัดจากเทปจริง (ข) ต้นทุนไป-กลับ (ค) multiple จาก on-chain fees/revenue (ง) supply/vesting
**รายงานฉบับเต็มของรอบ:** `workspace/reports/finance/2026-10-19-CRYPTO-r6.md`

## ตัวเลขหลัก (ไม้ $3,000 · 2026-10-19 22:06Z)

| symbol | notional 24 ชม. | notional 6 ชม. | print ≥$3k 6 ชม./24 ชม. | last trade age | spread @$3k | **RT ไป-กลับ** | % ของ risk $150 | mcap | mcap/fees (ann.) | mcap/revenue (ann.) | FDV/mcap |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BTC/USD | **$1,108,466** | $6,370 | **0 / 15** | 6.8 น. | 8.70 bps | **0.643%** ($19.28) | 12.9% | $1.648T | 18,641× | n/a | 1.00× |
| ETH/USD | $24,999 | $4,803 | **0 / 1** | 33.4 น. | 10.26 | **0.666%** ($19.98) | 13.3% | $293.7B | 1,351× | 3,808.9× | 1.00× |
| XRP/USD | $37,614 | $2,219 | **0 / 4** | 19.7 น. | 41.39 | **0.914%** ($27.42) | 18.3% | $82.3B | n/a (400) | n/a | 1.58× |
| SOL/USD | $14,449 | $3,410 | 0 / 0 | 5.7 น. | 64.76 | **1.534%** ($46.03) | 30.7% | $61.9B | 183.4× | 1,497.0× | 1.08× |
| ARB/USD | $11,558 | $2,233 | 0 / 1 | 103.0 น. | 25.25 | **0.752%** ($22.57) | 15.0% | $1.37B | 162.6× | 163.4× | 1.45× |
| UNI/USD | $6,894 | $209 | 0 / 1 | 179.4 น. | 19.44 | **0.694%** ($20.83) | 13.9% | $4.55B | **3.4×** | 42.1× | 1.42× |
| HYPE/USD | $2,600 | $889 | 0 / 0 | 166.6 น. | 48.81 | **0.988%** ($29.64) | 19.8% | $17.5B | 17.0× | **21.1×** | **4.29×** |
| PAXG/USD | $3,883 | $597 | 0 / 0 | 43.4 น. | **115.07** | **1.797%** ($53.91) | **35.9%** | $1.83B | n/a | n/a | 1.00× |
| BCH/USD | $837 | $88 | 0 / 0 | 11.6 น. | 55.30 | **1.053%** ($31.59) | 21.1% | $5.60B | 200,950× | n/a | 1.00× |
| FIL/USD | $456 | $97 | 0 / 0 | 341.1 น. | 35.60 | **0.856%** ($25.68) | 17.1% | $844M | 1,005× | 1,005× | 2.34× |

`[calc]` RT = fee taker 0.25%×2 + spread ระหว่าง level ที่สะสมของได้ ≥$3,000 (ไม่ใช่ L1) + slip buy + slip sell · ต้นทุนเป็นสัดส่วนคงที่ของ notional (ไม่ใช่ fixed cost) ⇒ ขาดทุนที่ stop 5% = 5% + RT = **$169.28–$203.91 = 112.9%–135.9% ของ risk $150** ทุกคู่

## ข้อเท็จจริงเชิงโครงสร้างที่ต้องจำ (วัดซ้ำได้)

1. **เทปทั้งลิสต์ว่างพร้อมกันเป็นช่วง ๆ:** 6 ชั่วโมงล่าสุด (16:06Z→22:06Z) **ไม่มี print ใด ≥$3,000 เลยทั้ง 10 คู่**; ไม้ใหญ่สุดใน 6 ชม. = ARB $2,116.90 · print ≥$3,000 ครั้งสุดท้าย = BTC 15:21:23Z ⇒ ตัวเลข notional 24 ชม. ของ **ทุกคู่** ขับด้วย burst ไม่กี่ชั่วโมง (BTC: 73.5% ของวันมาจากชั่วโมงเดียว)
2. **L1 spread ไม่ใช่ต้นทุน:** BTC/ETH/SOL post ของที่ L1 เพียง **$81/$80/$101** ⇒ ต้องไล่ book ถึงขนาดไม้ (SOL: L1 7.62 bps → ต้นทุนจริง 1.534%)
3. **Depth บน book ไม่คงที่:** PAXG L1 ask เคย $17,984 (r5 13:01Z) → **$2** (r6 22:06Z) ใน 9 ชม. ขณะที่ depth รวมยัง $672,705 ⇒ quote MM ถอนได้
4. **ราคา last trade อาจไม่ใช่ราคาตลาด:** basis last-vs-mid ถึง **−2.80% (ARB)**, −1.54% (HYPE), −0.83% (UNI), +0.84% (FIL) ⇒ 4/10 คู่ใช้ราคา last trade เป็นราคาอ้างอิงไม่ได้
5. **แท็กซี่ค่าเงิน (economics):** UNI mcap/fees **3.4×** ถูกสุด · HYPE mcap/revenue **21.1×** แต่ **FDV/mcap 4.29×** (circ เพียง 23.3% ของ total) ⇒ บน FDV = ~90× · BCH fees 30 วัน **$2,292** = mcap/fees 200,950× · ARB mcap/revenue 163.4× (take 99.5%)

## Supply / overhang (2026-10-19)

- **BTC** circ 20,098,843 = total · ไม่มี unlock · **BCH** circ 20,105,009 = total · ไม่มี unlock
- **ETH** circ = total 122,148,378 · **net issuance หาไม่ได้** (ไม่มี Etherscan/Beaconcha.in key)
- **SOL** circ 589,493,608 / total 636,090,156 · **inflation 3.595281%/ปี = 22,869,230 SOL/ปี = $2.40B/ปี** (Solana RPC getInflationRate epoch 1062) · issuance ÷ revenue = **58.1×**
- **XRP** circ 63.13B / 99.99B (63.1%) · escrow 1B XRP ต้น พ.ย. (ทุติยภูมิ)
- **UNI** circ 624.72M / 886.96M (70.4%) · **HYPE** circ 222.45M / 955.31M (**23.3%**) · **ARB** circ 6.892B / 10B (68.9%) · **FIL** circ 835.77M / 1.957B (42.7%)
- **vesting รายเดือน:** ARB ~92.65M ARB (~1.36% ของ float) · HYPE ~9.9M HYPE (238M ÷ 24 tranches) — **วันถัดไปขัดกันหลายแหล่ง ไม่รับวันเดียว**
- **event เฉพาะ:** ARB โหวต 100M ARB (=1.451% ของ circ, $19.8M) ปิด 22 ต.ค. · FIL nv29 เสร็จ 13:59Z 19 ต.ค. (หลัง event เทป 2 print, ราคาต่ำกว่า pre-event) · SOL Alpenglow epoch 1064 ETA **2026-10-21 13:28:52Z**

## ETF flow สัปดาห์ 12–16 ต.ค. 2026 (Farside)

BTC **−$228.4M** · ETH **−$320.1M** · SOL **−$25.5M** · HYPE **−$17.5M** · XRP/PAXG/UNI/ARB/BCH/FIL = **ไม่มีหน้าใน Farside ⇒ หาไม่ได้**

## จุดที่ต้องจับตา (สำหรับรอบถัดไป)

1. **ไม่ควรใช้ notional 24 ชม. ตัดสินสภาพคล่อง** — ต้องดู print ≥$3,000 ใน 6 ชม. + ชั่วโมงที่มีเทป + เทปสดของ last trade; ณ r6 ทั้ง 10 คู่ได้ 0 ไม้
2. **ตรวจ basis last-vs-mid ทุกครั้ง** ก่อนอ้างราคา (ARB เพี้ยน 2.8% ขณะที่ mid ตรงกับราคาอ้างอิงของ leader)
3. **CME OI day-1 (BCH/UNI) ยังหาไม่ได้ (HTTP 403 ทุก endpoint)** · **DefiLlama unlocks 404/402** ⇒ ตาราง unlock ต้องใช้ทุติยภูมิและระบุว่าไม่ยืนยันวัน

---
ลิงก์: [[CRYPTO]] · [[trading-finance-moc]]
