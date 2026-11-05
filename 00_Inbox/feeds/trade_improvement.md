---
title: "trade_improvement.md"
type: source
status: active
agent: leader
created: 2026-11-05
updated: 2026-11-05
source_mtime: 2026-11-01 13:52 UTC
source_sha256: 49ea51f231745013
tags:
  - source/feed
  - domain/trading
related:
  - "[[trading-finance-moc]]"
source: "workspace/ingest/trade_improvement.md"
---

> 🔁 สำเนาอัตโนมัติจาก `workspace/ingest/trade_improvement.md` (mtime 2026-11-01 13:52 UTC) — **ห้ามแก้ด้วยมือ** ระบบเขียนทับจากต้นฉบับ
> บทเรียน/สิ่งที่ต้องแก้ของทีม

# Trade Improvement

- อัปเดต: 2026-11-01 12:55 UTC · รอบวิเคราะห์: **ยังไม่มีไม้ปิดในบัญชี `PA3ZME9WF`**
- อินพุต: `ingest/trade_journal_summary.md` (0 closed trades) + `reports/leader/decisions.md`
- ประวัติเดิม (บัญชี `PA3Z4JM8I` · 3 ไม้ · IMP-20261101-01..03) → `reports/leader/archive/2026-11-01-PA3Z4JM8I-trade_improvement.md`
- improve_id ใหม่จะถูกสร้างเมื่อมีไม้ปิดไม้แรกของบัญชีนี้

## ตารางปรับปรุงคะแนน

| improve_id | improve_date | plan_id | journal_id | stock | buy limit | sell limit | sell stop | volume | news score improvement | finance score improvement | technical score improvement |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| — | — | — | — | — | — | — | — | — | — | — | — |

## KPI ฐานของบัญชีนี้ (อัปเดตทุกครั้งที่ปิดไม้)

| metric | ค่า | วิธีคำนวณ |
| :--- | :--- | :--- |
| closed trades | 0 | นับจากตารางใน trade_journal_summary |
| win rate | — | ชนะ / ปิดทั้งหมด |
| expectancy ต่อไม้ | — | (win rate × avg win) − (loss rate × avg loss) เป็น USD และ %equity |
| avg R multiple | — | (exit − entry) / (entry − stop) |
| max drawdown | 0.00% | จาก equity peak ถึง trough |
| fees สะสม | $0.00 | regulatory fees จาก Alpaca |
| equity เริ่ม / ปัจจุบัน | $1,000.00 / $1,000.00 | GET /v2/account |

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

## กฎที่ยกมาบังคับใช้ต่อ (บทเรียนจากบัญชีเก่า — ไม่ใช่บันทึกการเทรด)

1. **Technical:** entry ต้องมี confirmation — `close > prior day's high` หรือปิดเหนือแนวที่กำหนด ห้ามใช้ limit ล้วนในขาลง 1D
2. **Technical:** ถ้า implied move > ระยะ stop → ห้ามถือข้ามงบ; ลดขนาด 50% หรือออกก่อนประกาศ
3. **News:** คะแนน ≥8 ต้องมี catalyst ที่มีวันที่ชัดในกรอบถือ; sentiment ล้วนเพดาน 7
4. **News:** sector median ของวัน < −2% → หัก 1 คะแนนทุกตัวใน sector นั้น
5. **Finance:** ใช้คัดคุณภาพ/ตัดหุ้นพัง ไม่ใช่จับจังหวะ — veto ได้เฉพาะกรณีงบดุลพัง
6. **Leader:** คง risk ≤1%/ไม้ · ห้ามเพิ่มขนาดเพื่อเอาคืน · ทุกไม้ต้องมี stop ก่อนเข้า

## ข้อจำกัดของข้อมูล
- ค่าธรรมเนียมแยกต่อออเดอร์ดึงไม่ได้จาก Alpaca API — ใช้ยอดกระทบยอดรวมเมื่อมีไม้ปิด

## เครื่องมือตรวจสอบอัตโนมัติ (เพิ่ม 2026-11-01)

- `scripts/reconcile_journal.py` — กระทบยอด journal ↔ Alpaca: ไม้ปิดมีแถวครบ · ราคา fill ตรง · pending ตรงกับ open order · equity
  - `--verbose` ดูรายละเอียด · `--quiet` เงียบเมื่อไม่มีปัญหา · `--journal <path>` ทดสอบกับไฟล์อื่นได้
  - cron `journal-reconcile` (job 49a048301bca) ทุกวัน จ.–ศ. 22:00 UTC = 05:00 ICT · ส่งข้อความเฉพาะเมื่อเจอ mismatch
- `workspace/data/corr-2026-11-01.json` — correlation matrix (Alpaca SIP, ปิด 2026-10-30)
