---
title: Trade Forex — Kanban
type: project
status: active
created: 2026-11-09
updated: 2026-11-09
tags:
  - trading/forex
  - project/kanban
aliases:
  - Forex Kanban
  - trade-forex
related:
  - forex_journal
  - trading-finance-moc
kanban-plugin: board
---

# Trade Forex — Kanban

บอร์ดงานของสายเทรด Forex (บัญชีเดโม Exness MT5 `464166782` · bridge บน VPS)
รายละเอียดผลการทดลองและการวิเคราะห์อยู่ใน [[forex_journal]]

## Backlog

- [ ] รีเซ็ตเงินบัญชีเดโม `464166782` แล้วเริ่ม grid v2 ใหม่ที่ 0.005 lot/ระดับ (ลด maxDD จาก 36% → 18%)
- [ ] ทดสอบ grid กฎเดียวกันบน USDJPY — ระวัง pip value ต่างจาก EURUSD
- [ ] ทดสอบ GBPUSD — สเปรดกว้างกว่า ต้องวัด spread จริงจาก `/rates` ก่อน
- [ ] เพิ่ม health check แจ้งเตือนเข้าห้องเมื่อ `trade_allowed=false` (AutoTrading หลุดทุกครั้งที่ terminal รีสตาร์ท)
- [ ] จำลอง weekend gap ใน backtest — stop ที่ −$20 อาจกลายเป็น −$40 ในความเป็นจริง
- [ ] backtest M1 ด้วยข้อมูล broker จริง (`/rates`) แทน Yahoo ที่เป็นข้อมูลปลอม

## กำลังทำ

- [ ] เฝ้าดูว่า bridge บน VPS + SSH tunnel ยังขึ้นเองหลัง container/VPS restart (ยังไม่มี systemd — ยกเลิกตามคำสั่ง 2026-11-09)

## ติดเงื่อนไข

- [ ] รัน grid รอบใหม่ — **ติด**: บัญชี balance $0.00 จาก stop-out 2026-11-06 ต้องรีเซ็ตเงินก่อน
- [ ] ต่อยอดเป็นเงินจริง — **ติด**: ยังไม่มี edge ที่พิสูจน์นอก backtest + maxDD เกิน 30% ของพอร์ต

## เสร็จแล้ว

- [x] วาง bridge บน VPS (MT5 ใต้ Wine) + SSH tunnel แทน ngrok/โน้ตบุ๊ก
- [x] order-flow smoke test: BUY/SELL, แนบ SL/TP, ปิดด้วย ticket — retcode 10009 ทุกเส้นทาง
- [x] backtest grid H1 บนข้อมูล broker จริง 50,000 แท่ง (7,599 ตะกร้า · PF 1.88)
- [x] แก้บั๊ก v2 หลัง stop-out 46 duplicate orders + เขียนเทสต์ 11 (บอท) + 7 (bridge)
- [x] เขียน [[forex_journal]] + post-mortem และ push ขึ้น GitHub

## Archive

**Complete**
