---
title: Decision Log
type: moc
status: active
agent: leader
created: 2026-10-19
updated: 2026-10-19
tags:
  - moc
  - domain/finance
  - topic/decisions
aliases:
  - decisions
  - Watchlist
  - บันทึกการตัดสินใจ
---

# 👑 Decision Log

บันทึกการตัดสินใจของ Leader — **append-only** ห้ามแก้ย้อนหลัง
ถ้าจะเปลี่ยนใจ ให้เพิ่มบรรทัดใหม่พร้อมวันที่ ไม่ใช่แก้ของเดิม

← กลับ [[main-hub]]

## รูปแบบรายการ

```markdown
## [YYYY-MM-DD] <TICKER> — <BUY | HOLD | SELL | WATCH>
- **ราคาอ้างอิง:** <ราคา> (ณ วันที่)
- **เหตุผลหลัก:** <1–3 ข้อ>
- **ความเสี่ยงที่เห็น:** <1–3 ข้อ>
- **เงื่อนไขที่ทำให้คิดใหม่:** <อะไรจะทำให้เปลี่ยนใจ>
- **แหล่งข้อมูล:** [[AAPL]] · [[ข่าวที่ใช้]] · [[วิเคราะห์เทคนิค]]
```

> [!warning] กฎส่วนตัว
> ทุกตัวเลขต้องมีแหล่งและวันที่กำกับ ห้ามอ้างราคาจากความจำ
> หุ้นพลังงาน = conflict of interest — ระบุทุกครั้ง

## บันทึก

_ยังไม่มีการตัดสินใจ_

## Watchlist ปัจจุบัน

| Ticker | สถานะ | อัปเดตล่าสุด | หน้า |
|---|---|---|---|
| AAPL | ตัวอย่าง | 2026-10-19 | [[AAPL]] |

## เกี่ยวข้อง

- [[agent-access-policy]]
- [[trading-finance-moc]]
