---
title: Stock Hub Template
type: system
status: active
created: 2026-10-19
updated: 2026-10-19
tags:
  - system/template
  - domain/finance
aliases:
  - เทมเพลตหน้าหุ้น
---

# Stock Hub Template

คัดลอกโครงนี้เป็น `10_MOC/stocks/<TICKER>.md` แล้วแทนที่ `<TICKER>`

> ห้ามลบ marker `<!-- agent:X:begin -->` / `<!-- agent:X:end -->`
> — checker ใช้ marker นี้ตรวจว่าใครเขียนส่วนไหน

````markdown
---
title: <TICKER>
type: moc
status: active
ticker: <TICKER>
agent: leader
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - moc
  - ticker/<TICKER>
aliases:
  - <TICKER>
  - <ชื่อบริษัท>
---

# <TICKER> — <ชื่อบริษัท>

## Snapshot
| | |
|---|---|
| Sector | |
| Watchlist status | กำลังติดตาม / เฝ้าดู / ถือ |
| ความเห็นล่าสุด | |

*(ส่วนนี้เป็นของ Leader)*

## 📰 News
<!-- agent:news:begin -->
_ยังไม่มีข้อมูล — News agent จะเติมในรอบถัดไป_
<!-- agent:news:end -->

## 📈 Technical
<!-- agent:tech:begin -->
_ยังไม่มีข้อมูล — Tech agent จะเติมในรอบถัดไป_
<!-- agent:tech:end -->

## 💰 Financial
<!-- agent:finance:begin -->
_ยังไม่มีข้อมูล — Finance agent จะเติมในรอบถัดไป_
<!-- agent:finance:end -->

## 👑 Decision
<!-- agent:leader:begin -->
_ยังไม่มีการตัดสินใจ_
<!-- agent:leader:end -->

## แหล่งข้อมูล

- ข่าว: `20_Knowledge/24_News_Archive/`
- เทคนิค: `20_Knowledge/25_Tech_Analysis/`
- งบการเงิน: `20_Knowledge/26_Financial_Data/`
- บันทึกการตัดสินใจ: [[decisions]]
````

## Checklist ก่อนสร้างหน้าใหม่

- [ ] มี `ticker:` ใน frontmatter
- [ ] marker ครบ 4 block และไม่ซ้อนกัน
- [ ] ลิงก์กลับจาก MOC ที่เกี่ยวข้อง (เช่น [[trading-finance-moc]])
- [ ] ตั้ง `agent: leader` (เจ้าของหน้า)

## เกี่ยวข้อง

- [[agent-access-policy]]
- [[system-moc]]
