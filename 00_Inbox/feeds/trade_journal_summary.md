---
title: "trade_journal_summary.md"
type: source
status: active
agent: leader
created: 2026-11-03
updated: 2026-11-03
tags:
  - source/feed
  - domain/trading
related:
  - "[[trading-finance-moc]]"
source: "workspace/ingest/trade_journal_summary.md"
---

> 🔁 สำเนาอัตโนมัติจาก `workspace/ingest/trade_journal_summary.md` (sync 2026-11-03) — ต้นฉบับที่ทีมใช้อยู่ใน workspace
> สรุป trade journal (R/win rate)

# Trade Journal Summary

- อัปเดต: 2026-11-02 23:05 UTC · แหล่งข้อมูล: Alpaca paper API (`GET /v2/orders?status=closed`, `GET /v2/account`) — ตรวจซ้ำด้วย `scripts/reconcile_journal.py` 2026-11-02 23:05 UTC: **problems=0**
- **บัญชีปัจจุบัน: `PA3ZME9WF` · เริ่มต้น $1,000.00 (2026-11-01)**
- ประวัติบัญชีเก่า `PA3Z4JM8I` (เริ่ม $100,000 → ปิด $98,741.89 · 3 ไม้ขาดทุน −$1,258.11) ถูกย้ายไป `reports/leader/archive/2026-11-01-PA3Z4JM8I-trade_journal_summary.md` — ไม่ได้ลบ
- สถิติบัญชีนี้: **ปิด 0 ไม้ · realized $0.00** · equity $1,000.00 · positions 0

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
| PLAN-20261102-01 | GDDY | SENT (armed · session 2026-11-03 · re-arm #2) | 9d3c7071-0d15-4f9e-81c1-fc6c3998699a | 1.35 | 0 | 113.60 (limit, DAY, expires 2026-11-03 21:00 UTC) | 106.35 (manual) | 131.74 (manual) | 2026-11-02 22:32:46 UTC |

- order ก่อนหน้า `858c1f0a` = **EXPIRED 2026-11-02 21:00 UTC · filled 0** (low ของ session 2 พ.ย. 115.93 > limit 113.60) — ไม่ใช่การยกเลิก และไม่ถูกนับเป็น position
- plan เดิม `PLAN-20261101-01` (1.739 @115.00 · stop 110.80) ถูก **ยกเลิก 2026-11-01 22:33:02 UTC** ก่อน fill — แทนด้วย plan ข้างบน (stop 106.35 = 1.50×ATR) ไม่นับเป็น position

- positions 0 · equity $1,000.00 · cash $1,000.00 · open orders 1 (GDDY DAY)
- เมื่อ fill: เปลี่ยนสถานะในตารางนี้เป็น **OPEN** (ไม่ย้าย) · ย้ายไปตารางหลักเฉพาะเมื่อ **ปิดไม้แล้ว**
