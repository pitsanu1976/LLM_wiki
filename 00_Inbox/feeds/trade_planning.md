---
title: "trade_planning.md"
type: source
status: active
agent: leader
created: 2026-11-10
updated: 2026-11-10
source_mtime: 2026-11-10 11:14 UTC
source_sha256: c094b21518026b0e
tags:
  - source/feed
  - domain/trading
related:
  - "[[trading-finance-moc]]"
source: "workspace/ingest/trade_planning.md"
---

> 🔁 สำเนาอัตโนมัติจาก `workspace/ingest/trade_planning.md` (mtime 2026-11-10 11:14 UTC) — **ห้ามแก้ด้วยมือ** ระบบเขียนทับจากต้นฉบับ
> แผนเทรด/armed levels/สถานะไม้

# Trade Planning

- สร้าง: 2026-11-01 11:55 UTC (leader) · **rev3: 2026-11-01 22:35 UTC (รอบ DAILY 2026-11-02)** · **rev4: 2026-11-02 23:05 UTC (รอบ DAILY-2026-11-03 · 0 ไม้ใหม่ · arm 8 ระดับรอ trigger)** · **rev5: 2026-11-03 23:05 UTC (รอบ DAILY-2026-11-04 · GDDY FILLED · 0 ไม้ใหม่ · arm 9 ระดับรอ trigger)** · **rev6: 2026-11-05 11:02 UTC (รอบ DAILY-2026-11-05 · MSFT SENT)** · **rev7: 2026-11-06 11:10 UTC (รอบ DAILY-2026-11-06 · MSFT CLOSED by stop · 0 แผนใหม่ · 2 WATCH + 3 armed)** · รอบ: WEEKEND-SCAN-2026-11-01 → DAILY-2026-11-02 → … → DAILY-2026-11-06
- แหล่งข้อมูล: `raw/news.md` (09:57–10:02 UTC) · `raw/finance.md` (10:05 UTC) · `raw/tech.md` (10:08 UTC) — จับคู่ด้วย `news_id`
- ราคาอ้างอิง: ปิด **Fri 2026-10-30 16:00 ET / 20:00 UTC** (SIP) · ไม่มี session ใหม่ระหว่าง 30 ต.ค. → 2 พ.ย. ⇒ ข้อมูลยังเป็นชุดล่าสุด · ตลาดเปิด **Mon 2026-11-02 09:30 ET = 14:30 UTC / 21:30 ICT** (DST สหรัฐสิ้นสุด 1 พ.ย. ⇒ เปิด/ปิดเร็วขึ้น 1 ชม. จากสัปดาห์ก่อน)
- บัญชี: Alpaca paper **`PA3ZME9WF`** — equity **$1,000.00** · cash $1,000.00 · positions 0 · open orders 1 (GET 2026-11-01 22:31:12 UTC)
- **การตัดสินใจต่อหุ้นทุกตัว (score + verdict + เหตุผล): `ingest/stock_decision.md`** — ทุกแถว plan_id ในไฟล์นี้ต้องมีแถว `SELECT` ที่นั่น (ตรวจด้วย `scripts/reconcile_journal.py`)
- กติกา: risk/ไม้ ≤1% = **$10.00** · เพดาน/ตัว ≤20% = **$200.00** · reserve ≥20% = $200 · max 3 ไม้ · R:R ≥2.0 · stop ≥1 ATR · stop ก่อนเข้าเสมอ
- **สถานะ: ✅ FILLED — order `9d3c7071-0d15-4f9e-81c1-fc6c3998699a` · 1.35 หุ้น · fill avg 113.08 (ดีกว่า limit 113.60 $0.52) · session 2026-11-03** · position เปิดจริง mv $153.16 · uPL +$0.50 (GET 2026-11-03 22:30:56Z) · **ไม่มี legs ที่ broker (fractional simple DAY)** ⇒ stop 106.35 / target 131.74 เป็น manual + watchdog
- **re-arm:** ไม่ต้อง — fill แล้วก่อน DAY หมดอายุ · order `858c1f0a` (re-arm #2) = EXPIRED 2026-11-02 21:00Z filled 0 มาก่อนหน้า
- **re-arm #2 (2026-11-02 22:32 UTC):** order ก่อนหน้า `858c1f0a` = **EXPIRED** 2026-11-02 21:00Z · **filled 0** — low 2 พ.ย. **115.93** ไม่แตะ 113.60 (ปิด 2 พ.ย. **116.61**, o 118.87 / h 121.48) ⇒ แผนยังไม่ถูก invalidate (ปิด > stop 106.35) และยังอยู่ก่อน deadline 2026-11-07 · ATR14 อัปเดต **4.892** ⇒ stop 7.25 = **1.48×ATR** (ยัง ≥1 ATR ✓)
- **stop + target เป็น manual ทั้งคู่**: ไม่มี leg ที่ broker · ตั้งใน `ingest/manual_stops.json` — **SL 106.35 / TP 131.74** · watchdog `fractional-stop-watchdog` (cron `*/15 13-21 * * 1-5`) ตรวจทุก 15 นาทีขณะตลาดเปิด: ราคา ≤106.35 หรือ ≥131.74 → ขาย market ทั้งจำนวน
- **rev3 แก้ 2 อย่างจาก rev2** (2026-11-01 22:33 UTC): (1) ยกเลิก order `67e075ae` 1.739 @115.00 (CANCELED, filled 0) (2) ส่งใหม่ 1.35 @113.60 พร้อม **stop 106.35** — เหตุผล: stop 110.80 ของ rev2 = 4.20 USD = **0.87×ATR14 4.84** = แคบกว่า noise 1 วัน (ผิดเกต "stop ≥1 ATR" ของบัญชี และผิดหลักห้ามตั้ง stop ให้แคบเพื่อรีด R:R) · 106.35 คือ stop โครงสร้างที่ tech desk ออกแบบเอง (ใต้ 94.02–110.90 cluster) = 7.25 = **1.50×ATR** · ผลคือ entry ต้องลงมาอยู่ในโซนของ tech (≤114.81 เพื่อให้ R:R ≥2 ที่ stop นี้)
- ยกเลิก order เดิม 1 หุ้น bracket GTC (`112b6e5b…`) เมื่อ 2026-11-01 12:13:55 UTC แล้ว

## ตารางแผน

| plan_id | refer improve_id | plan date | news_id | finance_id | tech_id | stock | buy limit | sell limit | sell stop | volume |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PLAN-20261102-01 | — (IMP ชุดเดิม archived แล้ว) | 2026-11-02 | NEWS-20261030-02 | FIN-20261101-02 | TECH-20261101-02 | GDDY | 113.60 | 131.74 | 106.35 | 1.35 |

## Price / size screen (อัปเดต 2026-11-01 13:39 UTC (rev2) — เปิดใช้เศษหุ้นแล้ว)

เพดาน/ตัว $200 ⇒ ขนาดเศษหุ้นที่ risk ≤$10 และ notional ≤$200 คือเพดานจริง (ไม่ใช่ราคาต่อหุ้นอีกต่อไป)

| stock | ปิด 30 ต.ค. | 1 หุ้น = % equity | ขนาดที่ risk ≤1% | notional | bound | สถานะ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| REGN | 927.89 | 92.79% | 0.196 หุ้น | $174.78 | risk | ซื้อได้ (เดิมติดเพราะหุ้นเต็ม) |
| CROX | 150.52 | 15.05% | 1.365 หุ้น | $200.00 | cap | ซื้อได้ |
| TMUS | 156.44 | 15.64% | 1.303 หุ้น | $200.00 | cap | ซื้อได้ |
| FDXF | 126.04 | 12.60% | 1.667 หุ้น | $200.00 | cap | ซื้อได้ |
| GDDY | 117.24 | 11.72% | 1.379 หุ้น @113.60 (risk-bound) | $156.66 | risk | **armed 1.35 @113.60 (SENT)** |

⚠️ ข้อสรุปที่เปลี่ยน: เมื่อเศษหุ้นใช้ได้ ตัวกรองที่ตัดสินคือ **R:R + คะแนน + ความปลอดภัยของ stop** ไม่ใช่ราคาต่อหุ้น — ตารางเดิมที่เขียนว่า REGN "ซื้อไม่ได้" เป็นข้อมูลก่อนเปิดใช้เศษหุ้น


## สถานะแผน (ใช้แทนการอ่านจาก prose)

| plan_id | status | order id | ส่งเมื่อ | TIF | fill | re-arm | invalidated เมื่อ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PLAN-20261102-01 | **SENT / ARMED (รอ fill อังคาร 3 พ.ย.)** | 9d3c7071-0d15-4f9e-81c1-fc6c3998699a | 2026-11-02 22:32:46 UTC (re-arm #2) | DAY (expires 2026-11-03 21:00 UTC) | 0 / 1.35 | 2 ครั้ง (rev3 + re-arm) | ปิด 1D < 106.35 ก่อน fill = ยกเลิก · ไม่ fill ภายใน 2026-11-07 = ยกเลิก |
| PLAN-20261101-01 | **REVOKED** (ยกเลิก 2026-11-01 22:33:02 UTC · CANCELED filled 0) | 67e075ae-8b48-47b2-9d6e-68433d774e30 | 2026-11-01 12:13:55 UTC | DAY | 0 / 1.739 | — | แทนด้วย PLAN-20261102-01 (stop เดิมแคบ 0.87×ATR) |

- fractional DAY หมดอายุทุก session ⇒ **re-arm ทุกวัน** จนกว่าจะ fill หรือถึง deadline 2026-11-07
- ราคาเปิด/ระหว่างวัน **สูงกว่า entry zone** ไม่ใช่เหตุยกเลิก — limit 113.60 fill ไม่ได้อยู่แล้วถ้าราคาไม่ลงมา (ไม่ไล่ราคาโดยธรรมชาติของ limit)
- ความเสี่ยงที่ต้องรู้: ถ้าเปิดจันทร์ **gap ลงต่ำกว่า 106.35** limit buy จะ fill ที่ราคาเปิด (ต่ำกว่า stop) ⇒ เป็นไม้ที่ผิดเงื่อนไขทันที — watchdog จะขายออกที่ tick ถัดไป (≤15 นาที) ผลขาดทุนจริง ≈ slippage ไม่ใช่ส่วนต่างทั้งช่วง เพราะซื้อและขายที่ราคาตลาดเดียวกัน
- correlation: ยังไม่มี position อื่น ⇒ กฎ ≤0.5 ไม่ผูกพัน · ก่อนเพิ่มไม้ที่ 2 ต้องคำนวณ corr กับ GDDY (ตาราง 2026-11-01 มีแล้ว)

## รายละเอียดแผน PLAN-20261102-01 — GDDY (LONG)

- **คะแนนรวม 7.67** = news 7 · finance 7 · tech 9 (สูงสุดใน 5 ตัว)
- **buy limit 113.60** — กลางโซน tech **112.40–114.82** · ต่ำกว่าปิด 117.24 (30 ต.ค.) อยู่ **3.10%**
- **sell stop 106.35** — ระดับโครงสร้างของ tech (ใต้ cluster low 94.02–110.90) · ระยะ **7.25 USD/หุ้น = 1.50×ATR14 4.84**
- **sell limit 131.74** — แนวต้าน 4 ธ.ค. 2025 (T2 ของ tech = 136.58, 52w high 137.93)
- **R:R = (131.74 − 113.60) / (113.60 − 106.35) = 18.14 / 7.25 = 2.50** ✓ ≥2.0
- เพดาน entry ที่ยังได้ R:R 2.0 กับ stop นี้: `(131.74 + 2×106.35)/3 = 114.81` ⇒ 113.60 อยู่ใต้เพดาน 1.06%
- เหตุผล: reversal day 30 ต.ค. (เปิด −2.07% → ปิด +10.72%, body 94% ของช่วง, wick ล่าง 0%, RVOL 2.14×) · MACD histogram พลิกบวก · ADX14 30.9 (+DI 38.8 / −DI 20.9) · SMA เรียงขึ้น · Airo annualized bookings >$100M (จาก $50M) · FCF Q3 $480.8M หนุน buyback · finance 7 (net debt/EBITDA 1.87×, FCF yield สูง, ROIC 28.66%)
- ความเสี่ยงที่บันทึกไว้: PT consensus $110 **ต่ำกว่าราคา** 117.24 (ตลาด re-rate ไปแล้วรอบหนึ่ง) · equity ติดลบ −$138.8M · current ratio 0.61 · tech ให้ entry 1/2 คะแนนเพราะราคาห่าง SMA20 2.31 ATR (ยืด)
- invalidated: ปิด 1D < **106.35** ก่อน fill = ยกเลิก · ไม่ fill ภายใน **2026-11-07 16:00 ET** = ยกเลิก · ไม่มี earnings/XD ในกรอบ (งบ Q3 ออก 29 ต.ค. แล้ว, GDDY ไม่จ่ายปันผล)

### สูตร sizing (ตัวเลขจริง — rev3)
```
equity = 1,000.00
risk/ไม้ = 1,000 × 1.00% = 10.00 USD
ระยะ stop = |113.60 − 106.35| = 7.25 USD/หุ้น
shares (risk)   = 10.00 / 7.25 = 1.379
shares (weight) = 200.00 / 113.60 = 1.761          ← ไม่ผูกพัน (risk เป็นตัวบังคับ)
⇒ ใช้ 1.35 หุ้น (เผื่อ 0.029 หุ้น = $0.21 สำหรับ slippage ตอน manual stop)
   notional 1.35 × 113.60 = 153.36 (15.34% ของ equity) ≤ เพดาน 200 ✓
   risk     1.35 × 7.25   = 9.79  (0.979% ของ equity) ≤ budget 10.00 ✓
   R:R = 2.50 ≥ 2.0 ✓ · stop = 1.50×ATR ≥ 1×ATR ✓
cash หลัง fill = 1,000 − 153.36 = 846.64 (84.66%) ≥ reserve 200 ✓ · open positions 1/3 ✓
```
- เทียบ rev2 (1.739 @115.00 / stop 110.80): rev2 วาง risk ไว้ 7.30 (0.73%) แต่ **stop อยู่ที่ 0.87×ATR** = อยู่ใน noise รายวัน ⇒ ความน่าจะเป็นถูกเขี่ยออกสูงกว่าที่ตัวเลข R:R 3.99 บอก · rev3 ยอมลดขนาดลง 22% เพื่อให้ stop อยู่ที่ระดับโครงสร้างจริงและ risk ยัง ≤1%
- หมายเหตุ: เศษหุ้นทำ bracket ไม่ได้ (API: `fractional orders must have order_class=simple`) และ TIF ต้องเป็น DAY เท่านั้น ⇒ ใช้ **manual stop** ผ่าน watchdog


## รายชื่อที่พิจารณาแล้วไม่เข้า

| stock | คะแนนเฉลี่ย | news / finance / tech | เหตุผลที่ไม่เข้า |
| :--- | :--- | :--- | :--- |
| REGN | 8.00 | 9 / 8 / 7 | **R:R ไม่ผ่าน** — ที่โซนเข้า 890 / stop 839.08 / target 960 ได้ R:R **1.37** (<2.0) · ปิด 927.89 ยิ่งแย่ (0.36) · ต้องรอย่อ ≤871 จึงจะได้ 2.11 (ดู Watchlist) |
| CROX | 7.67 | 8 / 8 / 7 | R:R ที่เป้า 154.05 = **1.05** (เป้า 160 = 1.88) < 2.0 · RSI 77.75 · CLV 30% (แรงขายที่ high) |
| TMUS | 6.67 | 7 / 7 / 6 | คะแนนเฉลี่ย < 7.5 · tech 6 = rebound ไม่ใช่ trend (ใต้ SMA50 −6.4%, SMA200 −16.3%) · R:R ผ่าน (3.00) แต่ trend ไม่ผ่าน |
| FDXF | 5.33 | 6 / 4 / 6 | finance 4 — equity ติดลบ, Debt/EBITDA 4.91 · OBV 20 วัน −1.9% · ไม่มี MA200 |

**เกณฑ์คัด:** ซื้อได้ภายในเพดาน 20% → avg ≥7.5 → tech ≥7 → finance ≥7 → R:R ≥2.0 · ผ่านครบมีเพียง GDDY

## หมายเหตุ
- ตัวเลขทั้งหมดมาจาก `raw/*.md` (ปิด 30 ต.ค. 2026) หรือคำนวณจากตัวเลขเหล่านั้น
- **การส่งออเดอร์: leader ส่งเองได้** ตาม policy 2026-11-01 — ไฟล์นี้บันทึกสิ่งที่ส่งจริงพร้อม order id
- ได้ fill แล้วให้เพิ่มแถวใน `ingest/trade_journal_summary.md` และเปลี่ยนสถานะเป็น OPEN

## Watchlist — รอหลัง midterm (มติ 2026-11-01 12:45 UTC)
| stock | สถานะ | เงื่อนไขที่จะเข้า | entry | stop | target | R:R | เหตุที่ไม่เข้าเลย |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| REGN | WATCH | ราคาย่อ ≤871 และไม่มี earnings/midterm shock | 870.00 | 839.08 | 935.35 | 2.11 | ปิด 927.89 = 52w high, RSI 79.11, 5.13 ATR จาก MA20 |
| CROX | NO | ต้องย่อหลุด 139.33 ไปหาโซน 117–120 ก่อน | — | — | — | — | stop ปลอด noise ให้ R:R < 1.6 · RSI 77.75 |
| TMUS | NO | ต้องปิดเหนือ SMA50 (167.13) ก่อน | — | — | — | — | tech 6 · โครงสร้างขาลง |
| FDXF | NO | ต้องมี FCF เป็นบวก + MA200 | — | — | — | — | finance 4 · PE 28.78 · ไม่มี MA200 |

- ช่องว่างโพซิชัน: **2/3** (ถือ/รอ fill GDDY 1 ไม้) · cash reserve เป้าหมาย ≥ $200
- ห้ามเข้าไม้ใหม่ก่อน **2026-11-04** (midterm 3 พ.ย. + 755 บริษัทรายงานสัปดาห์ 2–6 พ.ย.)

## Correlation จริง (คำนวณ 2026-11-01 14:20 UTC — Alpaca SIP daily returns)

| pair | n (1Y) | corr 1Y | corr 60 วัน |
| :--- | :--- | :--- | :--- |
| GDDY–REGN | 252 | 0.08 | **0.45** |
| GDDY–CROX | 252 | 0.09 | 0.04 |
| GDDY–TMUS | 252 | 0.19 | 0.30 |
| GDDY–FDXF | 106 | 0.10 | 0.36 |
| REGN–CROX | 252 | 0.11 | 0.10 |
| REGN–TMUS | 252 | 0.05 | 0.30 |
| REGN–FDXF | 106 | 0.22 | 0.44 |
| CROX–TMUS | 252 | 0.09 | 0.01 |
| CROX–FDXF | 106 | 0.22 | 0.17 |
| TMUS–FDXF | 106 | 0.21 | 0.33 |

- **ผ่านกฎ ≤0.5 ทุกคู่** · สูงสุด 1Y = CROX–FDXF 0.22 · สูงสุด 60 วัน = GDDY–REGN 0.45 (ใกล้เพดาน — ต้องเฝ้า)
- ข้อจำกัด: FDXF มีประวัติซื้อขาย ~107 วัน (spin-off 28 พ.ค. 2026) → คู่ที่เกี่ยวกับ FDXF ใช้ n=106
- ไฟล์ดิบ: `workspace/data/corr-2026-11-01.json` (สร้างด้วย Alpaca SIP daily bars, ปิด 2026-10-30)

---

# รอบ DAILY-2026-11-03 (rev4 · 2026-11-02 23:05 UTC)

- ราคาอ้างอิง: ปิด **2026-11-02 (SIP)** · equity $1,000.00 · positions 0 · open orders 1 (GDDY armed) — GET 2026-11-02 23:05:09Z
- **ผล: 0 ไม้ใหม่** — ไม่มีชื่อใดผ่านเกตคะแนน (avg ≥7.5) · WATCH 1 (NVDA 7.33) · REJECT 9 · รายละเอียดต่อชื่อ: `ingest/stock_decision.md` §รอบ DAILY-2026-11-03
- ยังติดมติ **ห้ามเข้าไม้ใหม่ก่อน 2026-11-04** (midterm 3 พ.ย. + งบ 755 บริษัท 2–6 พ.ย.)

## Armed levels 2026-11-04 (ระดับรอ trigger — **ไม่ใช่แผนที่อนุมัติ**)

ทุกแถวมาจาก `reports/tech/2026-11-03-DAILY.md` · ยังไม่ผ่าน score gate ⇒ ห้ามส่งออเดอร์จนกว่าคะแนนจะถึง 7.5 **และ** trigger ทำงาน

| ticker | limit | stop | T1 | T2 | R:R net T2 | qty | notional | risk | trigger ก่อนส่ง | invalidated เมื่อ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| NVDA | 203.00 | 195.60 | 213.13 | 222.19 | 2.57 | 0.98 | $198.94 | $7.25 | ปิด 1D ≥ **206.00** แล้วย่อกลับ ≤203.00 | ปิด 1D < 200.92 |
| AMZN | 254.60 | 241.80 | 265.34 | 287.20 | 2.53 | 0.78 | $198.59 | $9.98 | ปิด 1D ≥ **254.60** | ปิด 1D < 242.28 |
| ETN | 361.00 | 342.00 | 382.24 | 417.43 | 2.95 | 0.52 | $187.72 | $9.88 | ปิด 1D ≥ **366.00** (หลังงบ 3 พ.ย.) | ปิด 1D < 358.51 |
| CEG | 252.00 | 239.50 | 269.00 | 287.00 | 2.78 | 0.79 | $199.08 | $9.88 | limit ทำงานเมื่อย่อเข้าโซน 248–252 | ปิด 1D < 247.20 หรือปิด > 269.02 |
| AMAT | 375.00 | 350.10 | 395.93 | 434.04 | 2.36 | 0.40 | $150.00 | $9.96 | ปิด 1D ≥ **380.00** | ปิด 1D < 372.80 |
| AVGO | 322.30 | 309.00 | 333.56 | 351.88 | 2.20 | 0.62 | $199.83 | $8.25 | เปิด 4 พ.ย. ≥ 321.87 (ถ้าต่ำกว่า: ปิด 1D > 325.00) | ปิด 1D < 319.30 |
| PLTR | 188.00 | 176.90 | 196.69 | 212.94 | 2.23 | 0.90 | $169.20 | $9.99 | ปิด 1D ≥ **186.87** | ปิด 1D < 178.13 |
| ANET | 171.50 | 161.70 | 181.27 | 194.73 | 2.35 | 1.02 | $174.93 | $10.00 | ปิด 1D ≥ **171.00** (หลังงบ 3 พ.ย.) | ปิด 1D < 163.25 |

- **กติกา fill:** ถ้า limit fill ที่ราคาต่ำกว่า `stop + 1.0×ATR` ⇒ **ไม่รับไม้** (stop หดเพราะ gap)
- **ข้อจำกัดพอร์ตถ้าเข้าไม้:** GDDY (ถ้า fill) + 1 ไม้ = 2/3 · cash ≥ reserve $200 ✓ · **ห้ามถือคู่ corr ≥0.5** — NVDA/TSM/ETN/ANET/AMAT/AVGO ต่อกันเกิน 0.5 ทุกคู่ ⇒ เลือกได้เพียง **1 ตัว** จากกลุ่ม semis/electrical; ชุดที่ถือร่วมได้คือ AMZN + CEG + PLTR (max 0.386)

## ตารางรายชื่อที่ตกคัด (แสดงเพื่อตรวจความมีวินัย)

| stock | N | F | T | avg | ตกเพราะ (ตัวเลขแรกที่ fail) | verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MSFT | 4 | 7 | 6 | 5.67 | tech 6 < 7 · R:R T2 net 0.98 | REJECT |
| TSM | 3 | 8 | 6 | 5.67 | news 3 · R:R T2 net 1.21 | REJECT |
| AMZN | 5 | 6 | 7 | 6.00 | finance 6 < 7 (FCF −$46.9B) · avg 6.00 | REJECT |
| ETN | 5 | 6 | 7 | 6.00 | finance 6 (D/E 1.05) · avg 6.00 | REJECT |
| AMAT | 5 | 6 | 7 | 6.00 | finance 6 (EV/EBITDA +81%) · avg 6.00 | REJECT |
| ANET | 4 | 8 | 6 | 6.00 | tech 6 (structure 4.5/10) | REJECT |
| AVGO | 5 | 6 | 6 | 5.67 | tech 6 (vol 0.91x) · finance 6 (SBC 9.5%) | REJECT |
| PLTR | 5 | 4 | 8 | 5.67 | finance VETO (EV/EBITDA 162x) | REJECT |
| CEG | 5 | 3 | 7 | 5.00 | finance VETO (FCF $309M, หุ้น +6.85%) | REJECT |
| NVDA | 6 | 9 | 7 | 7.33 | avg 7.33 < 7.5 (ขาด 0.17) | WATCH |

## Correlation (leader คำนวณเอง · SIP daily returns ถึง 2026-11-02)

- กับ GDDY (armed): d60 NVDA −0.212 · MSFT +0.093 · AMZN −0.029 · TSM −0.405 · AVGO −0.307 · CEG −0.254 · ETN −0.503 · AMAT −0.393 · PLTR +0.074 · ANET −0.440 ⇒ **ไม่มีตัวชนเกต ≥0.5** (ค่าที่ใกล้เส้นเป็นลบ)
- ภายในลิสต์ d60: TSM–ETN 0.744 · TSM–AVGO 0.737 · NVDA–TSM 0.722 · TSM–AMAT 0.721 · ETN–ANET 0.779 · ETN–AMAT 0.719 · AVGO–AMAT 0.621 · AVGO–ETN 0.611 · MSFT–PLTR 0.593 · CEG–ETN 0.571 · NVDA–AVGO 0.569 · AMZN–ANET 0.346 · CEG–PLTR 0.069
- ไฟล์ดิบ: `workspace/data/bars-2026-11-02-leader.json` (15 symbols, SIP daily 2026-06-01→2026-11-02)

---

# รอบ DAILY-2026-11-04 (rev5 · 2026-11-03 23:05 UTC)

- ราคาอ้างอิง: ปิด **2026-11-03 (SIP)** · equity **$1,000.50** · cash $847.34 · **positions 1 (GDDY 1.35 @113.08)** · open orders 0 — GET 2026-11-03 22:30:56Z
- **ผล: 0 ไม้ใหม่ (0 SELECT · REJECT 10)** — ไม่มีชื่อใดผ่านเกตคะแนนทั้ง 3 ข้อพร้อมกัน · **ไม่มีการส่ง/แก้/ยกเลิกออเดอร์ในรอบนี้**
- รายละเอียดต่อชื่อ + leader comments: `ingest/stock_decision.md` §รอบ DAILY-2026-11-04 · memo: `reports/leader/2026-11-04-DAILY.md`
- desk reports วันเดียวกัน (mtime): news **22:42:12Z** · tech **22:53:04Z** · finance **22:52:39Z** · news-scores **22:57:20Z** · tech-scores **22:55:39Z** — pull day 2026-11-03, bar ปิด 3 พ.ย.

## Plan state — ไม้ที่ถืออยู่

| plan_id | stock | สถานะ | order id | TIF / class | qty สั่ง | filled | entry จริง | SL (manual) | TP (manual) | re-arm | invalidated |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PLAN-20261102-01 | GDDY | **OPEN (filled)** | `9d3c7071-0d15-4f9e-81c1-fc6c3998699a` | DAY / simple (fractional) | 1.35 | **1.35 @113.08** | 113.08 | **106.35** (1.32×ATR14 5.08) | **131.74** (R:R 2.77) | 2 (ทั้งคู่ EXPIRED ก่อนหน้า) | ปิด 1D < **106.35** |

- **ไม่มี legs ที่ broker** — fractional บังคับ `simple` + `DAY` ⇒ stop/target อยู่ที่ `ingest/manual_stops.json` และบังคับด้วย watchdog `fractional-stop-watchdog` (`*/15 13-21 * * 1-5`, job `e86652860dbf`)
- risk ที่ใช้ **$9.09 = 0.909%** ของ equity · weight **15.31%** ⩽ 20% · cash เหลือ $847.34 ⩾ $200 · **เหลือ 2 ช่องจาก 3**

## Armed levels 2026-11-05 (ระดับรอ trigger — **ไม่ใช่แผนที่อนุมัติ**)

ทุกแถวมาจาก `reports/tech/2026-11-04-DAILY.md` · **ยังไม่ผ่าน score gate ⇒ ห้ามส่งออเดอร์จนกว่าคะแนนจะถึง 7.5 และ trigger ทำงาน**

| ticker | limit (entry zone) | stop | T1 | T2 | R:R net T2 | qty | notional | risk | trigger ก่อนส่ง | invalidated เมื่อ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| NVDA | 206.51–207.24 | 199.90 | 212.15 | 222.19 | 2.01 | 0.967 | $200 | $6.74 | **ปิด 1D ≥ 212.15 (MA20) + volR >1.0** ⇒ tech 6→7 · **ต้องออกก่อน 17 พ.ย.** | ปิด 1D < 200.92 |
| MSFT | 514.51–517.84 | 501.50 | 533.25 | 551.15 | 2.01 | 0.387 | $200 | $5.69 | news 4→7 ต้องมี catalyst ที่มีวัน+primary | ปิด 1D < 504.96 |
| AMZN | 243.85–245.34 | 235.50 | 254.60 | 265.34 | 2.01 | 0.818 | $200 | $7.44 | news 4→7 (เดิมไม่มี catalyst เลย) | ปิด 1D < 242.28 |
| TSM | 398.49–401.18 | 384.00 | 414.76 | 436.04 | 2.01 | 0.500 | $200 | $7.92 | N 5→7 ต้องมีวันงบ/รายได้ที่ยืนยันได้ | ปิด 1D < 398.29 |
| AMAT | 372.25–376.35 | 351.50 | 395.93 | 426.52 | 2.00 | 0.439 | $164 | $10.00 | tech 6→7 (volR 0.75x) · **ออกก่อน 12 พ.ย.** (gap 11.13% > stop 6.60%) | ปิด 1D < 372.80 |
| ETN | 379.83–383.83 | 362.00 | 399.30 | 427.96 | 2.00 | 0.504 | $193 | $10.00 | F 6.5→7 ต้อง D/E ≤0.80 · XD 10 พ.ย. | ปิด 1D < 363.76 |
| AVGO | 327.45–331.71 | 314.50 | 342.33 | 366.55 | 2.01 | 0.607 | $200 | $9.15 | tech 6→7 · **งบ 10 ธ.ค. = วันสุดท้ายกรอบ** (gap 14.66% > stop 5.19%) | ปิด 1D < 319.30 |
| CEG | 257.16–259.89 | 246.50 | 269.02 | 287.00 | 2.01 | 0.774 | $200 | $9.30 | **ห้ามส่งก่อน 9 พ.ย.** (งบ) + ต้องปลด VETO (FCF TTM >$1.5B) | ปิด 1D < 247.20 |
| AMD | 496.93–502.52 | 464.50 | 523.92 | 579.18 | 2.00 | 0.284 | $142 | $10.00 | ต้องปลด VETO (FCF m ≥15% 2 ไตรมาสติด) | ปิด 1D < 466.07 |
| ANET | — | — | — | — | **NO PLAN** | — | — | — | รอปิด 1D > 200.68 แล้วย่อ ⇒ ต้องออกแบบระดับใหม่ | — |

- **กติกา fill (สองด้าน):** fill **ต่ำกว่า** ปลายล่างของโซน = ระยะ stop หด → ไม่รับไม้ · fill **สูงกว่า** ปลายบน = net R:R <2 → ไม่รับไม้
- **งบในกรอบถือ:** AMAT 12 พ.ย. (gap 11.13% vs stop 6.60%) · NVDA 17 พ.ย. (6.30% vs 3.54%) · CEG 9 พ.ย. · AVGO 10 ธ.ค. (14.66% vs 5.19%) ⇒ **ทุกตัวต้องออกก่อนวันงบ** ถ้าจะถือ

## ตารางรายชื่อที่ตกคัด (แสดงเพื่อตรวจความมีวินัย)

| stock | N | F | T | avg | ตกเพราะ (ตัวเลขแรกที่ fail) | verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| NVDA | 9 | 8.5 | 6 | 7.83 | **tech 6 < 7** (volR 0.91x, trend 4.50) | REJECT |
| AMAT | 7 | 7.0 | 6 | 6.67 | avg 6.67 · volR 0.75x ต่ำสุด · gap งบ 11.13% > stop 6.60% | REJECT |
| TSM | 5 | 8.0 | 6 | 6.33 | avg 6.33 · N 5 ไม่มีวัน catalyst | REJECT |
| MSFT | 4 | 7.5 | 7 | 6.17 | **news 4** — ไม่มี catalyst ในกรอบ (XD 0.19%) | REJECT |
| AVGO | 6 | 6.5 | 6 | 6.17 | avg 6.17 · SBC 9.5% · net debt $35.4B | REJECT |
| ANET | 5 | 7.5 | 5 | 5.83 | tech 5 + NO PLAN (R:R จริง 0.43–1.12) | REJECT |
| ETN | 5 | 6.5 | 6 | 5.83 | avg 5.83 · D/E 99.5% · งบออกแล้ว AH +7.00% | REJECT |
| CEG | 7 | **4.0** | 6 | 5.67 | **finance VETO** (FCF $295M = 0.9%, P/FCF 316) | REJECT |
| AMZN | 4 | 6.0 | 7 | 5.67 | news 4 (ไม่มี catalyst) + F 6.0 (FCF −$46.9B) | REJECT |
| AMD | 5 | **5.5** | 5 | 5.17 | **finance VETO** (P/E 105, EV/EBITDA 75, หนี้ +119%) | REJECT |

## Correlation (leader คำนวณเอง · SIP daily returns ถึง 2026-11-03, n=60/252)

- กับ **GDDY**: ETN **−0.510** · ANET −0.450 · TSM −0.412 · AMD −0.405 · AMAT −0.401 · AVGO −0.322 · CEG −0.263 · NVDA −0.227 · AMZN −0.047 · MSFT **+0.061** ⇒ **ไม่มีตัวใด ≥ +0.5** ⇒ รอบนี้ correlation ไม่ใช่ตัวตัดสิน
- เกตเป็นแบบ **ด้านเดียว (positive ≥ +0.5 = ไม้ซ้ำ)** — ค่าติดลบคือการกระจายความเสี่ยง ไม่ใช่ความเสี่ยงซ้ำ
- ไฟล์ดิบ: `workspace/data/corr-2026-11-03-vsGDDY.json` (20 symbols)


---

# รอบ DAILY-2026-11-05 (rev6 · leader ตัดสิน 2026-11-05 10:55–11:02 UTC · ก่อนเปิด 14:30Z)

- ราคาอ้างอิง: **ปิด 2026-11-04** (Alpaca SIP 1Day, last bar `2026-11-04T05:00:00Z`) · leader ตรวจซ้ำ 11:00Z ด้วย `scripts/px_equity.py` ตรงกับ analyst ทุกหลัก
- บัญชี **`PA3ZME9WF`** — equity **$1,006.85** · cash $847.33 · positions GDDY 1.35 · open orders 0 (GET 10:55:52Z ก่อนส่ง)
- รายงานวันเดียวกันครบ 3 สาย: news 09:52Z · finance 10:19Z · tech 10:21Z
- กติกา rev8: risk/ไม้ ≤$10.07 · เพดาน/ตัว ≤$201.37 · reserve $201.37 · max 3 ไม้ · R:R ≥2 · stop ≥1 ATR

## ตารางแผน (รอบนี้)

| plan_id | refer improve_id | plan date | news_id | finance_id | tech_id | stock | buy limit | sell limit | sell stop | volume |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PLAN-20261105-01 | IMP-20261106-01 | 2026-11-05 | NEWS-20261105-01 | FIN-20261105-01 | TECH-20261105-01 | MSFT | 551.00 | 585.00 | 535.00 | 0.36 |

## Plan state — 2026-11-05

| plan_id | status | order id | TIF | filled qty | re-arms | invalidation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PLAN-20261105-01 | **SENT** (ACCEPTED 10:57:57Z · read-back 10:59Z filled 0) | `4ebc3a3d-c3cd-44be-bc72-f0cc2c4812bb` | DAY | 0 / 0.36 | 0 | ปิด 1D < 542.30 · เปิด < 549.84 · ไม่ fill ถึง 2026-11-10 21:00Z |
| PLAN-20261102-01 | **OPEN** (GDDY 1.35 @113.08) | `9d3c7071-0d15-4f9e-81c1-fc6c3998699a` (FILLED) | DAY→manual | 1.35 / 1.35 | 2 | ปิด 1D < 106.35 · deadline 2026-12-15 |

- **MSFT เป็น fractional ⇒ ไม่มี bracket ที่ broker** (`order_class=simple` + TIF=DAY เท่านั้น) · stop 535.00 / target 585.00 อยู่ใน `ingest/manual_stops.json` (plan PLAN-20261105-01) · broker DAY stop จะถูกวางโดย `scripts/arm_day_stops.py` (cron 13:25/14:25 UTC) เมื่อมี position จริง · watchdog `fractional-stop-watchdog` (*/15 13–21 UTC) เป็นชั้นที่ 2
- **ถ้าไม่ fill ภายใน 2026-11-05 21:00Z** (DAY หมดอายุ): re-arm ที่ 551.00 ตราบที่ยังไม่ปิด 1D < 542.30 และยังไม่เกิน deadline 2026-11-10 · ถ้าเปิดต่ำกว่า 549.84 = ยกเลิก ห้ามรับ fill


## Armed levels 2026-11-05 (ระดับรอ trigger — **ไม่ใช่แผนที่อนุมัติ**)

- **AMZN** — trigger: ปิด 1D ≥ **265.34** (high 2026-10-20) **และ** ย่อไม่หลุด 262 · entry 262.00 · stop 253.00 (1.05×ATR) · T1 271.49 (R 1.06 = ตก) · **T2 280.00 (R 2.00)** ⇒ ถ้า entry ไม่ลงมาถึง 262 R:R ไม่ผ่าน
- **ANET** — trigger: ย่อถึง **171.00** (gap fill ใต้ close 4 พ.ย. 4.2%) · stop 161.30 (1.02×ATR) · T2 191.11 (R 2.07) · ถ้าไม่ย่อใน 2–3 วัน = ไม่มีไม้ (ห้ามไล่)
- **NVDA** — trigger: ปิด 1D ≥ **212.15** (MA20) + volR >1.0 **และต้องออกก่อนงบ 17 พ.ย.** · แผน breakout 206.79/199.50 ให้ R:R 1.28–1.98 (ตกเกต) ⇒ ยังไม่ใช่แผน
- **MSFT T2** — ถ้า fill 551.00 และปิด 1D เหนือ 585 (T1) ⇒ ยก target เป็น 597.00 (measured move) และเลื่อน stop ขึ้นเป็น breakeven 551.00 (ต้องเขียน trigger + วันที่ก่อนทำ)
- **ไม่จับตา:** AMAT 383.65 · MU 853.34 · CEG 250.85 · ETN 378.23 · GEV 879.04 · PWR 627.07 — ปิดเหนือระดับเหล่านี้แล้ว R:R ยัง 0.38–1.61 = ตกเกตทุกตัว

## ตารางรายชื่อที่ตกคัด (แสดงเพื่อตรวจความมีวินัย)

| stock | N | F | T | avg | ตกเพราะ (ตัวเลขแรกที่ fail) | verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ANET | 7 | 8.0 | 6.5 | 7.17 | **T 6.5 < 7** (ปิดใต้ MA20 185.48, แท่ง 11-04 fade) · ต้องรอย่อถึง 171 | REJECT |
| NVDA | 7 | 9.0 | 5.5 | 7.17 | **T 5.5** (ปิดใต้ MA200 204.67 ครั้งแรก, R:R 1.28/1.98) | REJECT |
| AMZN | 8 | 5.5 | 7.0 | 6.83 | **F 5.5** (FCF TTM −$46.9B, net debt $190.6B, D/E 49.7%) | REJECT |
| AMAT | 4 | 7.0 | 4.5 | 5.17 | avg · R:R 1.50/1.61 · MA20 slope −12.91% · งบ 12 พ.ย. | REJECT |
| MU | 3 | 7.5 | 4.5 | 5.00 | N 3 + R:R 0.84/1.86 · ATR% 6.45 · ไม่มี corr | REJECT |
| GEV | 3 | 8.0 | 3.0 | 4.67 | R:R 0.38/0.52 (แย่สุด) | REJECT |
| PWR | 3 | 7.0 | 4.0 | 4.67 | R:R 0.45/1.28 · stop ต้องกว้าง 10.54% | REJECT |
| ETN | 3 | 6.5 | 3.5 | 4.33 | R:R 0.66/1.02 · corr GDDY −0.510 | REJECT |
| CEG | 4 | 4.0 | 4.0 | 4.00 | **F 4.0** (FCF m 0.9%, D/E 76.4%, dilution +13.4%) | REJECT |

## Correlation (leader · SIP daily returns ถึง 2026-11-04, n=60)

- กับ **GDDY**: MSFT **+0.061** · AMZN −0.047 · NVDA −0.227 · CEG −0.263 · AMAT −0.401 · ANET −0.450 · ETN −0.510 ⇒ **ไม่มีตัวใด ≥ +0.5** ⇒ correlation ไม่ใช่ตัวตัดสินรอบนี้ (เกตด้านเดียว: positive ≥ +0.5 = ไม้ซ้ำ)
- MU / GEV / PWR: **ไม่มีค่า corr** ในไฟล์ `data/corr-2026-11-03-vsGDDY.json` ⇒ ถ้าจะเข้า ต้องถือเป็นความเสี่ยงซ้ำซ้อนที่วัดไม่ได้ (ทั้ง 3 ตกเกตอื่นอยู่แล้ว)


---

# รอบ DAILY-2026-11-06 (rev7 · leader ตัดสิน 2026-11-06 10:55–11:10 UTC · ก่อนเปิด 14:30Z)

- ราคาอ้างอิง: **ปิด 2026-11-05** (Alpaca SIP 1Day) · close ของ 6 ชื่อตรงกันทั้ง 3 สายถึง cent
- บัญชี **`PA3ZME9WF`** — equity **$1,003.27** · cash **$841.11** · positions **GDDY 1.35 (mark 120.12 · uPL +$9.50)** · open orders **0** (GET 10:55:56Z · `/v2/clock` is_open=false next_open 14:30Z)
- รายงานวันเดียวกันครบ 3 สาย: news 09:53Z · finance 10:18Z · tech 10:18Z · ใบสั่งงานเข้า `done/` ครบ 3 คิว
- กติกา rev8 @ equity วันนี้: risk/ไม้ ≤**$10.03** · เพดาน/ตัว ≤**$200.65** · reserve ≥**$200.65** · max 3 ไม้ (ว่าง 2) · R:R ≥2 · stop ≥1 ATR · `stop% ≤ risk/cap = 5.00%`
- **ผลรอบ: 0 แผนที่ส่ง** · 2 WATCH (NVDA, TSM) · 4 REJECT · MSFT ปิดโดย stop เมื่อวาน (−$6.20)

## ตารางแผน (รอบนี้)

| plan_id | refer improve_id | plan date | news_id | finance_id | tech_id | stock | buy limit | sell limit | sell stop | volume |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| — | — | 2026-11-06 | — | — | — | **ไม่มีแผนที่ส่งรอบนี้** | — | — | — | — |

> ไม่มี `plan_id` ใหม่เพราะไม่มี `SELECT` — NVDA/TSM เป็น **WATCH** (มี trigger + ขนาดเขียนไว้ครบ แต่ยังไม่ใช่ใบอนุญาตเข้า) ดู "Armed levels" ด้านล่าง · ตามกติกา: ไม่มี `plan_id` = ห้ามเป็น SELECT (ตรวจด้วย `scripts/reconcile_journal.py`)

## Plan state — 2026-11-06

| plan_id | status | order id | TIF | filled qty | re-arms | invalidation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PLAN-20261105-01 (MSFT) | **CLOSED — STOP_HIT 2026-11-05 20:30:49Z** | `4ebc3a3d` (buy fill 550.914 14:33:09Z) → `2f819ada` (sell 533.70) | DAY | 0.36 / 0.36 → **ปิดแล้ว** | 0 | ปิดจบ: realized **−$6.20 (−0.617% ของ equity)** · slippage ใต้ stop 535 = $1.31/หุ้น |
| PLAN-20261102-01 (GDDY) | **OPEN · stop ยกเป็น breakeven 2026-11-06** | `9d3c7071` (FILLED 1.35 @113.08) | DAY→manual | 1.35 / 1.35 | 2 | ปิด 1D < **113.08** (เดิม 106.35) · target 131.74 · deadline 2026-12-15 |
| — (NVDA armed A) | **WATCH** — trigger ปิด 1D ≥ 188.88 | — | — | — | — | ปิด 1D < 174.64 · ไม่เกิดถึง 2026-11-13 |
| — (NVDA armed B) | **WATCH** — ย่อ ≤179.20 หลัง BLS ผ่าน | — | — | — | — | เปิดต่ำกว่า 179.20 = ห้ามรับ fill |
| — (TSM armed) | **WATCH** — หลังรายได้เดือน 10 พ.ย. + ย่อ ≤332.20 | — | — | — | — | ปิด 1D < 325.19 · รายได้เดือนออกแย่ = ยกเลิกทั้งแผน |

- **GDDY:** fractional ⇒ ไม่มี bracket ที่ broker · stop 113.08 / target 131.74 อยู่ใน `ingest/manual_stops.json` · broker DAY stop วางโดย `scripts/arm_day_stops.py` (cron 13:25/14:25 UTC) · watchdog `fractional-stop-watchdog` (*/15 13–21 UTC) เป็นชั้นที่ 2
- **MSFT:** ปิดแล้ว — order `2f819ada` sell market 0.36 @533.70 (watchdog STOP_HIT, log: `price=534.01 stop=535.0`) · แถว journal `J-20261105-01` อยู่ใน `ingest/trade_journal_summary.md`

## Armed levels 2026-11-06 (ระดับรอ trigger — **ไม่ใช่แผนที่อนุมัติ**)

- **NVDA A (breakout — ทางหลัก):** trigger **ปิด 1D ≥ 188.88** (สูงกว่า high 2026-03-16) → buy limit **189.00** · stop **181.60** (7.40 = 1.01×ATR14 7.34) · T1 200.13 (1.44 net = ตก) · **T2 206.79 (2.32 net ✓)** · size **1 หุ้น = $189.00 (18.8%)** · risk **$7.40 (0.74%)** · งบ 17 พ.ย. gap max 2.65% = 0.65× stop ⇒ ถือข้ามได้
- **NVDA B (pullback):** trigger ย่อแตะ **≤179.20** *หลัง* BLS 13:30Z ผ่านและไม่ถูกขายกลับในชั่วโมงแรก → buy limit **179.20** · stop **171.86** (1.00×ATR) · T2 **197.97** (2.47 net ✓) · 1 หุ้น $179.20 หรือเศษ 0.91 หุ้นที่ stop 168.19 (1.5×ATR, risk $10.02) · **fill floor 179.20** = เปิดต่ำกว่านี้ห้ามรับ fill
- **TSM:** trigger = รายได้เดือน ต.ค. ออก **10 พ.ย. 05:30Z** MoM/YoY เร่ง **และ** ราคาย่อ ≤**332.20** → เศษ **0.60 หุ้น = $199.32 (19.9%)** · stop **316.10** (1.01×ATR) · T2 **380.00 (2.88 net ✓)** · risk **$9.66 (0.96%)** · ถ้ารายได้เดือนแย่ = ยกเลิกแผน ไม่รอย่อ
- **NVDA A/B และ TSM ใช้ slot เดียวกัน** — เกิดอันใดอันหนึ่งแล้ว อีกอันเป็นโมฆะ · corr NVDA–TSM 0.80 (d60) / 0.93 (d30) ⇒ **ห้ามถือพร้อมกัน**
- **ไม่จับตา (ตกเกตแล้ว):** CSCO ปิด >102.14 (avg 7.00) · AMAT (tech สั่งไม่เข้า, stop ไม่มีโครงสร้าง) · BABA (F VETO) · CEG (R:R 1.34 + งบ 9 พ.ย.)

## ตารางรายชื่อที่ตกคัด (แสดงเพื่อตรวจความมีวินัย)

| stock | N | F | T | avg | ตกเพราะ (ตัวเลขแรกที่ fail) | verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CSCO | 7 | 7.0 | 7.0 | 7.00 | **avg 7.00 < 7.5** · entry ต้องเบรก +6.8% จากปิด 95.72 · ปิดที่ low วัน | REJECT |
| AMAT | 8 | 7.0 | 4.0 | 6.33 | **T 4.0 (tech สั่งไม่เข้า)** · stop 23.50 ไม่มีโครงสร้าง (311.07→287.49 ว่าง) · ATR 7.21% | REJECT |
| BABA | 6 | 4.0 | 7.5 | 5.83 | **F VETO** · FCF 4 ไตรมาส −175,755 M CNY · OM 7.29% · ROIC 3.08% | REJECT |
| CEG | 6 | 4.0 | 3.0 | 4.33 | **R:R ดีสุด 1.34 < 2** · งบ 9 พ.ย. gap max 9.92% = 1.79× stop | REJECT |

## Correlation (tech · SIP daily returns ถึง 2026-11-05, 546 แท่ง)

- กับ **GDDY**: NVDA **−0.24 (d60) / −0.52 (d30)** · TSM −0.37 / −0.47 · CSCO −0.29 / −0.39 · CEG −0.29 / −0.38 · AMAT −0.39 / −0.47 · BABA **+0.06 / +0.12** ⇒ ไม่มีตัวใด ≥ +0.5 (เกตด้านเดียว)
- **ภายในลิสต์:** NVDA–TSM **0.80 / 0.93** · AMAT–TSM 0.79 / 0.83 · AMAT–NVDA 0.60 / 0.76 · CSCO–TSM 0.57 / 0.76 · CSCO–NVDA 0.45 / 0.75 · CSCO–CEG 0.44 / 0.51 ⇒ **semis 4 ตัวเป็น exposure เดียวกัน ⇒ ถือได้ไม่เกิน 1 ตัว** · BABA แยกออกได้ (≤+0.2 กับทุกตัว) แต่ติด F VETO
- **คู่ที่ผมปฏิเสธรอบนี้: NVDA + TSM** (0.80/0.93) — เก็บ NVDA เพราะ entry ห่างราคา 1.3% (ไม่ใช่ 5.9%), gap งบ 0.65× stop (ไม่ใช่ 1.49×), สภาพคล่อง $23.8B/วัน (เทียบ $5.75B)
- หมายเหตุ: ไฟล์ `data/corr-2026-11-03-vsGDDY.json` คำนวณถึง 3 พ.ย. (ก่อน crash) และไม่มี CSCO/BABA ⇒ รอบนี้ใช้ค่าที่คำนวณถึง 5 พ.ย. ของ tech


# รอบตรวจ NVDA-2026-11-08 (rev8 · leader ตรวจกับ desks 2026-11-08 ~09:30 UTC · ตลาดปิด)

- **ผล: 0 SELECT · NVDA คงเป็น WATCH · ไม่มี plan_id ใหม่ · ไม่ส่งออเดอร์**
- รายงาน 3 สายวันเดียวกัน: `reports/news/2026-11-08-NVDA.md` (09:31Z, 122 บรรทัด) · `reports/finance/2026-11-08-NVDA.md` (09:28Z, 130) · `reports/tech/2026-11-08-NVDA.md` (09:28Z, 135)
- ราคาอ้างอิง: ปิด **2026-11-06 = 186.64** (Alpaca SIP, ผ่าน tech) — ตรงกับที่ news/finance ใช้
- **armed levels rev7 ถูกยกเลิกทั้งคู่ (stop ใต้กฎ 1.5×ATR ที่ตั้งหลัง MSFT post-mortem IMP-20261106-01):**
  - NVDA A: stop 181.60 = **0.95×ATR14 7.77** → ต่ำกว่ากฎ · ถ้าขยับเป็น 176.50 (1.61×ATR) ⇒ risk $12.50 · **R:R ที่ T2 206.79 = 1.42 < 2** ⇒ ตกเกต (ต้องมี target ≥ **214.00**)
  - NVDA B: stop 171.86 = **0.94×ATR** → เช่นกัน · stop 167.50 (1.5×ATR) ⇒ risk $11.70 · **R:R ที่ T2 197.97 = 1.60 < 2** ⇒ ตกเกต (ต้องมี target ≥ **202.60**)
- ขนาดที่ fit ถ้าจะเข้า: A 0.80 หุ้น ($151.20 = 15.1%, risk $10.00) · B 0.85 หุ้น ($152.32, risk $9.95) — ใต้เพดาน $200.65 ทั้งคู่ แต่ติด R:R
- งบ Q3 FY27 **2026-11-17** อยู่ในกรอบถือ ⇒ ถ้าเข้า 16 พ.ย. ต้องตัดสินถือ/ลดก่อนงบ
- ทิศทาง 1D ขาลง: ปิดใต้ MA20 211.55 / MA50 219.81 / MA200 204.67 · RSI14 30.76 · MACD hist −3.20 · dd −23.3% จาก high 243.37 (6 ต.ค.)


# รอบ DAILY-2026-11-09 (rev9 · leader ตัดสิน 2026-11-09 10:55–11:10 UTC · ก่อนเปิด 14:30Z)

- ราคาอ้างอิง: **ปิด 2026-11-06** · tech ใช้ consolidated (stockanalysis) · news ใช้ Alpaca IEX — ต่าง ≤$0.06 ทุกชื่อ
- บัญชี **`PA3ZME9WF`** — equity **$995.52** · cash **$841.11** · positions **GDDY 1.35 (mark 114.38 · uPL +$1.76)** · open orders **0** ตอน sync (แล้วมี DAY stop `afb697f6` ที่ผมวาง 10:57:59Z) — GET 10:55:58Z · clock is_open=false next_open 14:30Z
- รายงานวันเดียวกันครบ 3 สาย: news 09:54Z · finance 10:20Z · tech 10:23Z · ใบสั่งงานเข้า `done/` ครบ 3 คิว
- กติกา rev8 @ equity วันนี้: risk/ไม้ ≤**$9.96** · เพดาน/ตัว ≤**$199.10** · reserve ≥**$199.10** · max 3 ไม้ (ว่าง 2) · R:R ≥2 · stop ≥1.5×ATR · `stop% ≤ risk/cap = 5.00%`
- **ธีมรอบ:** post-crash dislocation — non-semis + dated catalyst · TF 3–10 sessions (9–27 พ.ย.)
- **ผลรอบ: 0 แผนที่ส่ง** · 8 REJECT · 0 armed ใหม่ · TSM armed revoked · GDDY HOLD

## ตารางแผน (รอบนี้)

| plan_id | refer improve_id | plan date | news_id | finance_id | tech_id | stock | buy limit | sell limit | sell stop | volume |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| — | — | 2026-11-09 | — | — | — | **ไม่มีแผนที่ส่งรอบนี้** | — | — | — | — |

> ไม่มี `plan_id` ใหม่เพราะไม่มี `SELECT` — ตามกติกา: ไม่มี `plan_id` = ห้ามเป็น SELECT

## Plan state — 2026-11-09

| plan_id | status | order id | TIF | filled qty | re-arms | invalidation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PLAN-20261102-01 (GDDY) | **OPEN · stop 113.08 (breakeven) · broker DAY stop re-armed** | `9d3c7071` (FILLED 1.35 @113.08) · stop `afb697f6` | DAY | 1.35 / 1.35 | 2 | ปิด 1D < **113.08** · target 131.74 · deadline 2026-12-15 |

- **GDDY:** fractional ⇒ ไม่มี bracket · stop 113.08 / target 131.74 ใน `ingest/manual_stops.json` · **broker DAY stop `afb697f6-cae5-4e3d-b151-1a859408d99e` SELL 1.35 @113.08 NEW created 2026-11-09 10:57:59Z** (read-back by id) · watchdog `fractional-stop-watchdog` (*/15 13–21 UTC) = ชั้นที่ 2
- **defect ที่แก้รอบนี้:** cron `arm-day-stops` + `stop-audit` ล้ม 4 ครั้งติด (`ModuleNotFoundError: No module named 'alpaca'`) เพราะ `script` ชี้สำเนา `/opt/data/profiles/leader/scripts/arm_day_stops.py` และถูกรันด้วย python ที่ไม่มี alpaca-py ⇒ **ไม่มี DAY stop ตั้งแต่ 2026-11-04 14:55Z** · แก้เป็น **shim** ที่ exec ตัวจริง (`/opt/data/home/hermes-stock-team/scripts/arm_day_stops.py`) ด้วย `.venv/bin/python` · ทดสอบ `--status` และ path ของ cron (ไม่มี arg → `--quiet`) ผ่านทั้งคู่

## Armed levels — 2026-11-09 (ไม่มี)

| ระดับ | สถานะ | เหตุ |
| :--- | :--- | :--- |
| NVDA A (189.00/181.60) · NVDA B (179.20/171.86) | **revoked 2026-11-08** | stop 0.94–0.95×ATR · ขยับถูกกฎแล้ว R:R 1.42/1.60 < 2 |
| **TSM (332.20/316.10/T2 380.00)** | **revoked 2026-11-09** | stop 16.10 = **1.01×ATR14 16.73** < 1.5×ATR · ที่ 1.5×ATR (stop 307.11) **R2 gross 1.90 < 2** |
| TSM เงื่อนไขปลดล็อก (ราคา) | — | entry **≤328.80** + stop = entry − 25.09 (≈303.71) ⇒ R2 net ≥2.0 + รายได้เดือน ต.ค. 10 พ.ย. 05:30Z ดี + corr GDDY ≤0.5 |
| ระดับใหม่ | **ไม่มี** | ทุกชื่อตกเกต **คะแนน** ⇒ armed level ไม่ช่วย (ราคาไม่ทำให้ avg ผ่าน 7.5) |

## ตารางรายชื่อที่ตกคัด (แสดงเพื่อตรวจความมีวินัย)

| stock | N | F | T | avg | ตกเพราะ (ตัวเลขแรกที่ fail) | verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| NTES | 6 | 8.0 | 7.0 | **7.00** | **avg 7.00 < 7.5** (ใกล้สุด) · ที่เหลือผ่าน: R2 net 2.93 · stop 1.50×ATR · risk ที่เพดาน $7.62 | REJECT |
| JD | 7 | 6.5 | 6.5 | 6.67 | **avg 6.67** · F 6.5 (OM TTM 0.17%) · R2 net 1.55 | REJECT |
| TGT | 8 | 7.0 | 4.0 | 6.33 | **T 4.0** (R2 net 1.07) + stop 6.52% > 5.00% | REJECT |
| DIS | 7 | 7.0 | 5.0 | 6.33 | **T 5.0** · R2 net 1.30 | REJECT |
| WMT | 5 | 5.0 | 7.0 | 5.67 | **F 5.0** — PE 45.48 = pct 89 · FCF yield 1.4% | REJECT |
| BABA | 6 | 4.0 | 6.5 | 5.50 | **F VETO** — FCF TTM −$11.47B · OM 14.13→7.29% | REJECT |
| TJX | 6 | 7.0 | 3.0 | 5.33 | **T 3.0** — ขาลง (ใต้ MA200 10.27%, MACD −0.984) | REJECT |
| BIDU | 5 | 4.0 | 6.0 | 5.00 | **F VETO** (TTM ขาดทุน, FCF −$1.90B) + stop 5.32% > 5.00% | REJECT |

## Correlation (tech, 60 daily returns ถึง 2026-11-06)

- กับ **GDDY**: TGT **+0.31 (20d +0.51)** · DIS +0.35 (+0.32) · JD +0.20 · WMT +0.22 (+0.48) · TJX +0.28 · NTES −0.00 · BABA +0.09 · BIDU +0.03 ⇒ ผ่านเกต ≤0.5 ทุกตัวที่ d60 **ยกเว้น TGT ที่ 20d = +0.51** ⇒ ถ้า TGT เป็น candidate ต้องวัดซ้ำทั้งสองหน้าต่าง
- **ภายในลิสต์:** JD–BABA **+0.52** · WMT–TJX **+0.51** · JD–NTES **+0.50** · TGT–WMT +0.39 · NTES–BIDU +0.24 ⇒ กลุ่ม retail (WMT/TJX/TGT) และกลุ่ม China (JD/BABA/NTES) อย่างละ **เดิมพันเดียว** ไม่ใช่ diversification
- ข้อจำกัด: tech คำนวณเป็น 60 daily returns (ไม่ใช่ 49 hourly แบบที่ news ใช้) ⇒ เทียบข้ามสายไม่ได้ตรงตัว

---

## รอบ DAILY 2026-11-10 — rev10 (**0 ไม้ · ไม่มีแผนส่ง · ไม่มี armed**)

- **บัญชี (GET 2026-11-10 10:55:55Z):** `PA3ZME9WF` · equity **$993.69** · cash **$993.69 (100%)** · **positions 0** · **open orders 0** · trading_blocked false · clock is_open=false, next_open 2026-11-10 14:30Z
- **caps รอบนี้:** risk/ไม้ **$9.94** · เพดาน/ตัว **$198.74** · reserve **$198.74** · deployable **$794.95** · max 3 ไม้ ⇒ ว่าง 3 ช่อง · ไม้เต็มเพดานต้อง **stop ≤ 5.00%**
- **GDDY ปิดไม้:** DAY stop `afb697f6` filled **1.35 @113.04** ที่ 2026-11-09 15:40:26Z · realized **−$0.054 ≈ 0.0R** · journal `J-20261109-01` · registry ล้างแล้ว
- **ผลคัด: 0 SELECT · 8 REJECT** — รายละเอียด + คะแนน: `ingest/stock_decision.md` (DEC-20261110-01..08) · memo `reports/leader/2026-11-10-DAILY.md`

### ตารางรายชื่อที่ตกคัด (แสดงเพื่อตรวจความมีวินัย)

| stock | N | F | T | avg (N เพดานบน 7) | ตกเพราะ (ตัวเลขแรกที่ fail) | verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| LVS | 7* | 7.0 | 6.0 | **6.67** | avg 6.67 < 7.5 + T 6.0 <7 + R2 net 1.78 + stop 5.61% >5% | REJECT |
| MGM | 7* | 7.0 | 4.0 | 6.00 | T 4.0 (ใต้ MA50/MA200, MACD hist ไม่ขยับ) + R2 1.72 + stop 6.70% | REJECT |
| DUK | 7* | 5.0 | 6.0 | 6.00 | F 5.0 (FCF −$3.30B ติดลบ 3/4 ปี) + R2 1.98 | REJECT |
| NEE | 7* | 5.0 | 5.0 | 5.67 | F 5.0 (FCF ตรวจไม่ได้) + R2 1.68 | REJECT |
| SBUX | 7* | 3.0 | 6.0 | 5.33 | **F VETO** (equity −$7.67B · P/E pct 90) | REJECT |
| AEP | 7* | 4.0 | 4.0 | 5.00 | F 4.0 + T 4.0 (R2 2.19 ผ่านตัวเดียวแต่คะแนนตก) | REJECT |
| SO | 7* | 4.0 | 3.0 | 4.67 | F 4.0 (FCF −$3.47B · ออกหุ้น +2.6%) + R2 1.14 | REJECT |
| MRK | 7* | 3.0 | 3.0 | 4.33 | **F VETO** (P/E 151.8 จาก one-off 2 ไตรมาส) | REJECT |

`*` N = เพดานบนตาม rubric (news ไม่ให้คะแนนเพราะไม่มี catalyst เฉพาะบริษัทที่ยืนยันวัน) ⇒ avg เป็น **กรณีดีที่สุด**

### Plan state (ตารางที่สอง — ไม่แตะ schema หลัก)

| plan_id | symbol | status | order id | TIF | filled | re-arms | invalidation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PLAN-20261102-01 | GDDY | **CLOSED (STOP_HIT)** | `afb697f6` (sell stop) | DAY | 1.35 @113.04 | 0 | — (ปิดแล้ว) |
| — | — | ไม่มีแผนใหม่รอบนี้ | — | — | — | — | — |

### Armed levels — 2026-11-10 (**ไม่มี**)

| ระดับ | สถานะ | เหตุ / เงื่อนไขปลดล็อก (ต้องเป็นตัวเลข) |
| :--- | :--- | :--- |
| NVDA A/B (188.88 / 179.20) | revoked 2026-11-08 | stop <1.5×ATR; ที่ถูกกฎ R:R 1.42/1.60 |
| TSM (332.20 / 316.10) | revoked 2026-11-09 | stop 1.01×ATR; ที่ถูกกฎ R:R 1.90 · ปลดล็อก: entry ≤328.80 + stop entry−25.09 |
| LVS | ไม่อาวุธ | ต้อง T→7 (ปิด 1D >41.73 volR≥1.2) **และ** entry ≤39.93 (stop 37.85) เพื่อ R2 ≥2 **และ** N 8 จากวัน DICJ GGR — สองข้อแรกขัดกัน (breakout 41.80 → R:R ~1.0) |
| DUK | ไม่อาวุธ | ต้อง F→7 ⇒ FCF TTM พลิกบวก (ปัจจุบัน −$3.30B) — ไม่ใช่เรื่องราคา |
| อื่น ๆ | ไม่อาวุธ | ตกที่คะแนน ไม่ใช่ที่ราคา ⇒ armed level แก้ไม่ได้ |

### Correlation ที่ใช้ปฏิเสธรอบนี้ (SIP daily ถึง 2026-11-09, leader คำนวณเอง + tech ยืนยัน)

- utility: DUK–SO **0.87/0.84** · DUK–NEE **0.85/0.87** · SO–AEP **0.85/0.84** · DUK–AEP 0.74/0.69 · SO–NEE 0.68/0.57 · NEE–AEP 0.58/0.48 ⇒ **1 ไม้เดียว**
- คาสิโน: **LVS–MGM 0.46 / 0.59 (20d)** ⇒ **ปฏิเสธคู่** · MGM–NEE 0.47/0.56 · MGM–SBUX 0.43/0.52
- ไฟล์: `workspace/data/prices-2026-11-10-pool.json`

