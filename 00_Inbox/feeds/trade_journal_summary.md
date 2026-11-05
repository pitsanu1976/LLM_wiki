---
title: "trade_journal_summary.md"
type: source
status: active
agent: leader
created: 2026-11-05
updated: 2026-11-05
source_mtime: 2026-11-03 22:59 UTC
source_sha256: 510eca43e43e727a
tags:
  - source/feed
  - domain/trading
related:
  - "[[trading-finance-moc]]"
source: "workspace/ingest/trade_journal_summary.md"
---

> 🔁 สำเนาอัตโนมัติจาก `workspace/ingest/trade_journal_summary.md` (mtime 2026-11-03 22:59 UTC) — **ห้ามแก้ด้วยมือ** ระบบเขียนทับจากต้นฉบับ
> สรุป trade journal (R/win rate)

# Trade Journal Summary

- อัปเดต: 2026-11-03 23:05 UTC · แหล่งข้อมูล: Alpaca paper API (`GET /v2/positions`, `GET /v2/orders?status=all`, `GET /v2/account`) — ตรวจด้วย `scripts/reconcile_journal.py` 2026-11-03 23:1x UTC: ดูผลท้ายไฟล์
- **บัญชีปัจจุบัน: `PA3ZME9WF` · เริ่มต้น $1,000.00 (2026-11-01)**
- ประวัติบัญชีเก่า `PA3Z4JM8I` (เริ่ม $100,000 → ปิด $98,741.89 · 3 ไม้ขาดทุน −$1,258.11) ถูกย้ายไป `reports/leader/archive/2026-11-01-PA3Z4JM8I-trade_journal_summary.md` — ไม่ได้ลบ
- สถิติบัญชีนี้: **ปิด 0 ไม้ · realized $0.00** · equity **$1,000.50** · cash $847.34 · **positions 1 (GDDY 1.35 @113.08, uPL +$0.50)**

## ตารางบันทึกการเทรด

| journal_id | plan_id | stock | entry date | entry price | volume | exit date | exit price | profit & loss | net balance | profit reason | loss reason |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| — | — | — | — | — | — | — | — | — | — | — | — |

## คำนิยามคอลัมน์ / convention

- `journal_id` = `J-YYYYMMDD-NN` (วันที่ปิดไม้) · เรียงตามลำดับที่ปิดในวันนั้น
- `plan_id` ต้องตรงกับ `trade_planning.md` เสมอ (ห้ามใช้ `LEGACY` อีก)
- `entry date` / `exit date` = วันที่ที่ fill จริงตามเวลา **ET** · ถ้าต้องระบุเวลาที่แม่นให้ใช้ UTC ในช่อง reason
- `entry price` / `exit price` = ราคา fill เฉลี่ยจาก Alpaca API (ไม่ใช่ราคาที่ตั้ง)
- `net balance` = equity หลังปิดไม้ (กระทบยอดกับ `GET /v2/account` วันเดียวกัน)
- `profit & loss` = gross (ยังไม่หักค่าธรรมเนียม) · ค่าธรรมเนียมใส่ในหมายเหตุกระทบยอด
- ไม้ที่ยังไม่ปิด **ไม่ใส่ในตารางนี้** — ใช้ตาราง "ไม้ที่รอ fill / เปิดอยู่" ด้านล่าง

## สถานะไม้ที่รอ fill / เปิดอยู่

| plan_id | stock | สถานะ | order id | qty สั่ง | fill | entry | SL | TP | ส่งเมื่อ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PLAN-20261102-01 | GDDY | **OPEN (filled 2026-11-03)** | 9d3c7071-0d15-4f9e-81c1-fc6c3998699a | 1.35 | **1.35** | 113.08 (fill avg; limit 113.60) | 106.35 (manual) | 131.74 (manual) | 2026-11-02 22:32:46 UTC |

- **GDDY fill 2026-11-03:** 1.35 หุ้นที่ **113.08** (limit 113.60 ⇒ fill ดีกว่า $0.52) · mv $153.16 · uPL +$0.50 (mark 113.45) · **ไม่มี legs ที่ broker** (fractional = simple + DAY) ⇒ stop/target อยู่ใน `ingest/manual_stops.json` และบังคับด้วย `fractional-stop-watchdog` (*/15 13-21 จ.-ศ.)
- risk ที่ใช้ **$9.09 (0.909%)** · weight **15.31%** · cash เหลือ $847.34 ≥ reserve $200 · **2 ช่องว่างจาก 3**
- order ก่อนหน้า `858c1f0a` = **EXPIRED 2026-11-02 21:00 UTC · filled 0** (low ของ session 2 พ.ย. 115.93 > limit 113.60) — ไม่ใช่การยกเลิก และไม่ถูกนับเป็น position
- plan เดิม `PLAN-20261101-01` (1.739 @115.00 · stop 110.80) ถูก **ยกเลิก 2026-11-01 22:33:02 UTC** ก่อน fill — แทนด้วย plan ข้างบน (stop 106.35 = 1.50×ATR) ไม่นับเป็น position

- positions 0 · equity $1,000.00 · cash $1,000.00 · open orders 1 (GDDY DAY)
- เมื่อ fill: เปลี่ยนสถานะในตารางนี้เป็น **OPEN** (ไม่ย้าย) · ย้ายไปตารางหลักเฉพาะเมื่อ **ปิดไม้แล้ว**
