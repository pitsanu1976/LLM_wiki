---
title: "trade_improvement.md"
type: source
status: active
agent: leader
created: 2026-11-06
updated: 2026-11-06
source_mtime: 2026-11-06 15:01 UTC
source_sha256: 62b413756b4fcb58
tags:
  - source/feed
  - domain/trading
related:
  - "[[trading-finance-moc]]"
source: "workspace/ingest/trade_improvement.md"
---

> 🔁 สำเนาอัตโนมัติจาก `workspace/ingest/trade_improvement.md` (mtime 2026-11-06 15:01 UTC) — **ห้ามแก้ด้วยมือ** ระบบเขียนทับจากต้นฉบับ
> บทเรียน/สิ่งที่ต้องแก้ของทีม

# Trade Improvement

- อัปเดต: 2026-11-06 11:40 UTC · รอบวิเคราะห์: **ไม้ปิดไม้แรกของบัญชี `PA3ZME9WF` (MSFT)**
- อินพุต: `ingest/trade_journal_summary.md` (1 closed) + `reports/leader/decisions.md` + Alpaca `GET /v2/orders?status=all` + SIP/IEX bars
- ประวัติเดิม (บัญชี `PA3Z4JM8I` · 3 ไม้ · IMP-20261101-01..03) → `reports/leader/archive/2026-11-01-PA3Z4JM8I-trade_improvement.md`
- KPI คำนวณจาก 1 ไม้ = ยังไม่พอสรุปเชิงสถิติ (ต้อง ≥20 ไม้) — ใช้เพื่อปรับกฎ ไม่ใช่ตัดสินว่ากลยุทธ์ผิด

## ตารางปรับปรุงคะแนน

| improve_id | improve_date | plan_id | journal_id | stock | buy limit | sell limit | sell stop | volume | news score improvement | finance score improvement | technical score improvement |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| IMP-20261106-01 | 2026-11-06 | PLAN-20261105-01 | J-20261105-01 | MSFT | 551.00 | 585.00 (T1) | 535.00 | 0.36 | **−1.0** — N 8 สร้างจากธีม macro (ผลเลือกตั้ง + WSJ 4 พ.ย. "structural winner") ไม่มี event ของบริษัทในกรอบถือ ⇒ เพดาน N = 7 เว้นแต่มี event เฉพาะบริษัทที่มีวันที่ · ถ้าธีมเป็นตัวหลัก ต้องลดน้ำหนักหรือรอ confirmation ราคา | **0.0** — F 7.5 สะท้อนงบจริง (FCF/op margin/net cash) ไม่ใช่สาเหตุขาดทุน | **−2.0** — T 8.5 สูงเกินจริง: (ก) แผนเรียกว่า breakout ATH แต่ entry 551.00 อยู่ **ใต้ pivot 559.15** ⇒ เป็น pullback ที่ใช้ stop ของ breakout (ข) stop 15.91 = **1.08×ATR14** < 1.5× ⇒ อยู่ใน noise ของแท่งเมื่อวาน (range 16.46) (ค) เข้า 14:33Z = 09:33 ET ใน 5 นาทีแรก |

## ผลของการปรับปรุงต่อรอบถัดไป (wiring — 2026-11-06)

Improvement จะไม่มีผลถ้าไม่ถูกอ่าน ⇒ ผูกเข้า 3 จุด:

| ชั้น | ไฟล์/กลไก | ผลที่เกิดขึ้น |
| :--- | :--- | :--- |
| 1. คะแนน desk | `ingest/score_adjustments.json` + `shared/scoring_policy.md` | delta/cap ต่อ ticker หรือต่อ desk · มี `source_improve` และ `expires` บังคับ · desk ต้องรายงานทั้งคะแนนดิบและหลังปรับ |
| 2. การตัดสิน leader | `scripts/apply_adjustments.py` + cron 05:30 ICT ขั้นที่ 4 และ 7 | ใช้คะแนนหลังปรับเท่านั้น · เพิ่ม gate: setup consistency · entry window (ห้าม fill ก่อน 10:00 ET) · broker stop ต้องวางจริง · stop ≥1.5 ATR เมื่อ ATR% >2.5 |
| 3. ไม้ที่เปิด/order ค้าง | `shared/position_policy.md` + `manual_stops.json` ladder | ยก stop ได้อย่างเดียว · trailing (Chandelier) · time stop · ขยาย stop ได้เฉพาะเมื่อลดขนาดให้ $ risk เท่าเดิม |

**ทดสอบย้อนกลับกับไม้นี้:** `.venv/bin/python scripts/apply_adjustments.py --round DAILY-2026-11-05`
→ MSFT N 8→7 · T 8.5→6.5 ⇒ avg **7.00 < 7.5** และ T 6.5 < 7 ⇒ **ตกคัด** (ถ้าใช้กฎวันนี้ ไม้ที่ขาดทุนจะไม่ถูกส่ง)
→ ผลข้างเคียง: AMZN N 8→7 (avg 6.83→6.5) ตกอยู่แล้ว · ตัวอื่นไม่เปลี่ยนผล

## Post-mortem — MSFT `PLAN-20261105-01` / `J-20261105-01`

**Facts (Alpaca API + IEX bars)**
- buy `4ebc3a3d` fill **550.914** 2026-11-05 14:33:09Z · 0.36 หุ้น · notional **$198.33 (19.7% ของ equity)**
- sell `2f819ada` fill **533.70** 2026-11-05 20:30:49Z · สาเหตุ **STOP_HIT** (watchdog เห็น 534.01 < stop 535.00)
- realized **−$6.20 = −3.12% ของ notional · −0.618% ของ equity · −1.08R** (plan risk $5.73)
- slippage ใต้ stop **$1.30/หุ้น = $0.47 = 8.2% ของระยะ stop**
- MFE **0.42R** (high 557.605) · MAE **−1.15R** (low 532.68) · ไม้ไม่เคยขึ้นถึง 1R เลย
- แท่ง 2026-11-05: open **555.31** / high **557.605** / low **532.68** / close **536.29** · แท่งก่อนหน้า 11-04: **+6.78%** (520.84 → 556.07) high **559.12**

**Calc**
- tech desk เสนอ entry **555.80** (breakout) stop 542.30 ⇒ ระยะ 13.50 · leader ใช้ limit **551.00** เพื่อ fill สวย ⇒ ระยะ stop ที่ตั้งจริง 15.91 แต่จุดอ้างอิงกลายเป็น "ใต้ pivot"
- ระยะ stop 15.91 **สั้นกว่า range ของแท่งเมื่อวาน 16.46** ⇒ noise ปกติของวันเดียวก็ชน stop ได้

**View (ความเห็น — ไม่ใช่ตัวเลข)**
- สาเหตุหลัก **ไม่ใช่ข่าวหรือพื้นฐาน** แต่คือ **setup drift**: เปลี่ยน breakout เป็น pullback โดยไม่เปลี่ยน stop/โครงสร้าง — ซื้อใต้ pivot ด้วย stop ที่ออกแบบมาสำหรับ breakout
- สาเหตุรอง: (1) stop 1.08 ATR แน่นเกินสำหรับหุ้น ATR 14.7 (~2.7%/วัน) (2) เข้าใน 5 นาทีแรกซึ่ง spread/ช่วงแกว่งกว้างสุด (3) broker DAY stop ไม่ถูกวางจริง ⇒ พึ่ง watchdog 15 นาที ⇒ slippage 8.2% ของระยะ stop

**ไม่ใช่สาเหตุ:** งบการเงิน (F 7.5 ถูก) · สภาพคล่อง (0.36 หุ้นเล็กมาก) · correlation (MSFT–GDDY +0.061) · risk per trade (0.570% < 1%)

## KPI ฐานของบัญชีนี้ (อัปเดตทุกครั้งที่ปิดไม้)

| metric | ค่า | วิธีคำนวณ |
| :--- | :--- | :--- |
| closed trades | **1** | นับจากตารางใน trade_journal_summary (J-20261105-01) |
| win rate | **0% (0/1)** | ชนะ / ปิดทั้งหมด — ตัวอย่างน้อยเกินสรุป |
| avg win / avg loss | — / **−$6.20** | เฉลี่ยจากไม้ที่ปิด |
| expectancy ต่อไม้ | **−$6.20 (−0.62% equity)** | (win rate × avg win) − (loss rate × avg loss) |
| avg R multiple | **−1.08R** | (exit − entry) / (entry − stop) = −17.214 / 15.914 |
| max drawdown | **−0.36%** | equity peak $1,006.85 (2026-11-05 ก่อน stop) → $1,003.27 |
| fees สะสม | ~$0.00 | regulatory fees จาก Alpaca (ไม่แยกต่อออเดอร์) |
| equity เริ่ม / ปัจจุบัน | $1,000.00 / **$1,003.27** | GET /v2/account 2026-11-06 10:55:56Z |

## Pre-registered review — PLAN-20261101-01 (GDDY)

ตัดสินก่อนเห็นผล เพื่อกัน hindsight bias:
- เข้าได้ตาม limit 115.00 หรือไม่ · slippage กี่ %
- MAE ระหว่างถือ (ถ้าเกิน 1×stop distance = stop แคบเกินไปสำหรับ ATR 4.13%)
- R multiple ที่ได้จริงเทียบ 3.99 · ถ้าถูก stop ให้ดูว่า gap หรือ intrabar
- ตรวจ compliance กับกฎ 6 ข้อ (ตารางล่าง) — ถ้าละเมิดข้อใด ให้ out come ไม่นับเป็น "กลยุทธ์ผิด"

## Checklist การปฏิบัติตามกฎ (ต่อไม้)

| rule | วิธีตรวจ | สถานะ GDDY |
| :--- | :--- | :--- |
| 1. entry confirmation | close > prior day high | ✅ **PASS** — ปิด 30 ต.ค. 117.24 > high 29 ต.ค. 106.685 (+$10.55) · ที่มา: Alpaca SIP bars |
| 2. implied move vs stop | straddle ถ้ามีงบในกรอบ | ✅ ผ่าน — งบ Q3 ออก 29 ต.ค. แล้ว ไม่มีงบในกรอบถือ |
| 3. news ≥8 ต้องมี catalyst มีวันที่ | ตรวจ news detail | ✅ ไม่ trigger (news 7) |
| 4. sector median < −2% หัก 1 คะแนน | 30 ต.ค. tech median −3.87% | ⚠️ **ขัดแย้ง** — ถ้าหักจริง news 7→6, avg 7.33 < 7.5 (ดูหมายเหตุ) |
| 5. finance ใช้คัดคุณภาพ | finance 7 | ✅ ผ่าน |
| 6. risk ≤1%/ไม้ + มี stop ก่อนเข้า | risk $7.30 = 0.73% | ✅ ผ่าน |

**หมายเหตุข้อ 4 (ต้องบันทึก):** กฎ sector filter ประกาศ effective **2026-11-02** แต่แผน GDDY ถูกส่ง **2026-11-01 12:13 UTC** ⇒ ใช้แบบ prospective ไม่หักคะแนนย้อนหลัง ไม้นี้จึงถือเป็น **grandfathered** (ข้อยกเว้นที่บันทึกไว้ ไม่ใช่การเพิกเฉยกฎ) — ไม้ใหม่ตั้งแต่ 2 พ.ย. เป็นต้นไปต้องหักตามกฎเคร่งครัด


### Checklist การปฏิบัติตามกฎ — MSFT (PLAN-20261105-01)

| rule | วิธีตรวจ | สถานะ MSFT |
| :--- | :--- | :--- |
| 1. entry confirmation | close > prior day high | ❌ **FAIL** — prior day high **559.12** แต่ entry **550.914** (ซื้อใต้ pivot ไม่ใช่ breakout) |
| 2. implied move vs stop | straddle ถ้ามีงบในกรอบ | ✅ ไม่มีงบในกรอบ (Q2 FY27 ~ม.ค. 2027) |
| 3. news ≥8 ต้องมี catalyst มีวันที่ | ตรวจ news detail | ⚠️ **ก้ำกึ่ง** — catalyst เป็นธีม (ผลเลือกตั้ง 4 พ.ย. + WSJ) ไม่ใช่ event บริษัท ⇒ ตามกฎใหม่ = เพดาน 7 |
| 4. sector median < −2% หัก 1 | 11-04 tech median | ✅ ไม่เข้าเงื่อนไข (sector บวก) |
| 5. finance ใช้คัดคุณภาพ | F 7.5 | ✅ ผ่าน (FCF/net cash ดี) |
| 6. risk ≤1%/ไม้ + stop ก่อนเข้า | risk $5.73 = 0.570% | ✅ ผ่าน |
| 7. (ใหม่) stop ≥1.5×ATR เมื่อ ATR% >2.5 | ATR14 14.74 | ❌ **FAIL** — stop 15.91 = 1.08×ATR |
| 8. (ใหม่) ห้ามเข้าใน 30 นาทีแรก | fill 14:33:09Z = 09:33 ET | ❌ **FAIL** |

**สรุป compliance: ผ่าน 4 · ไม่ผ่าน 3 (ข้อ 1, 7, 8) · ก้ำกึ่ง 1 (ข้อ 3)** ⇒ ไม้นี้ **ละเมิดกฎของเราเอง** ผลขาดทุนจึงไม่ควรถูกตีความว่า "ระบบคัดหุ้นผิด" แต่เป็น "ขั้น execution ผิด"

## กฎที่ยกมาบังคับใช้ต่อ (บทเรียนจากบัญชีเก่า — ไม่ใช่บันทึกการเทรด)

1. **Technical:** entry ต้องมี confirmation — `close > prior day's high` หรือปิดเหนือแนวที่กำหนด ห้ามใช้ limit ล้วนในขาลง 1D
2. **Technical:** ถ้า implied move > ระยะ stop → ห้ามถือข้ามงบ; ลดขนาด 50% หรือออกก่อนประกาศ
3. **News:** คะแนน ≥8 ต้องมี catalyst ที่มีวันที่ชัดในกรอบถือ; sentiment ล้วนเพดาน 7
4. **News:** sector median ของวัน < −2% → หัก 1 คะแนนทุกตัวใน sector นั้น
5. **Finance:** ใช้คัดคุณภาพ/ตัดหุ้นพัง ไม่ใช่จับจังหวะ — veto ได้เฉพาะกรณีงบดุลพัง
6. **Leader:** คง risk ≤1%/ไม้ · ห้ามเพิ่มขนาดเพื่อเอาคืน · ทุกไม้ต้องมี stop ก่อนเข้า
7. **ห้ามแก้ entry ให้ต่ำกว่า trigger ของ analyst เพื่อให้ fill สวย** — ถ้าจะซื้อใต้ pivot ให้ประกาศว่าเป็น pullback setup และคำนวณ stop จาก swing low + R:R ใหม่ (บทเรียน MSFT: เปลี่ยน breakout เป็น pullback แต่คง stop ของ breakout)
8. **stop ≥1.5×ATR14** เมื่อ ATR% ของหุ้น > 2.5 (เดิม ≥1 ATR) — ระยะ stop ต้องไม่สั้นกว่า range ของแท่งก่อนหน้า
9. **ห้าม entry ใน 30 นาทีแรกหลังเปิด (09:30–10:00 ET)** — ให้ limit ตั้งไว้ล่วงหน้าแล้วปล่อยให้ fill หลัง 10:00 ET หรือรอปิดเหนือ high ของ 30 นาทีแรก
10. **ก่อนถือข้ามวัน ต้องมี broker DAY stop วางจริง** — watchdog 15 นาทีเป็นด่านสองเท่านั้น (ไม้นี้ slippage 8.2% ของระยะ stop เพราะพึ่ง watchdog)

## ข้อจำกัดของข้อมูล
- ค่าธรรมเนียมแยกต่อออเดอร์ดึงไม่ได้จาก Alpaca API — ใช้ยอดกระทบยอดรวมเมื่อมีไม้ปิด

## เครื่องมือตรวจสอบอัตโนมัติ (เพิ่ม 2026-11-01)

- `scripts/reconcile_journal.py` — กระทบยอด journal ↔ Alpaca: ไม้ปิดมีแถวครบ · ราคา fill ตรง · pending ตรงกับ open order · equity
  - `--verbose` ดูรายละเอียด · `--quiet` เงียบเมื่อไม่มีปัญหา · `--journal <path>` ทดสอบกับไฟล์อื่นได้
  - cron `journal-reconcile` (job 49a048301bca) ทุกวัน จ.–ศ. 22:00 UTC = 05:00 ICT · ส่งข้อความเฉพาะเมื่อเจอ mismatch
- `workspace/data/corr-2026-11-01.json` — correlation matrix (Alpaca SIP, ปิด 2026-10-30)
