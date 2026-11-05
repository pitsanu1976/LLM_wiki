---
title: Forex Experiment Journal — Exness MT5 Demo
type: journal
status: active
created: 2026-11-05
updated: 2026-11-05
tags:
  - trading/forex
  - trading/experiment-log
  - trading/grid
aliases:
  - forex_journal
  - บันทึกการทดลอง Forex
related:
  - trading-finance-moc
  - journals-moc
---

# Forex Experiment Journal — Exness MT5 Demo

บัญชีทดลอง: **464166782 · Exness-MT5Trial17** · leverage 1:2000 · เริ่มที่ $300
รันบน VPS 187.53.129.196 (MT5 ใต้ Wine) → bridge `mt5_webhook.py` → SSH tunnel → Hermes
ทุกตัวเลขผลลัพธ์มาจาก broker (`/positions`, `/rates`, `deal` history) ไม่ใช่ความจำ

## ตารางสรุปการทดลอง

| วันที่เริ่ม | วันที่สิ้นสุด | ชื่อกลยุทธ์ | คู่เงิน | รายละเอียดกลยุทธ์ | ผลลัพธ์ | สิ่งที่ต้องปรับปรุง |
|---|---|---|---|---|---|---|
| 2026-11-05 | 2026-11-05 | Order-flow smoke test | EURUSD | ทดสอบเส้นทางส่งคำสั่งครบวงจร: BUY/SELL market, แนบ SL/TP, อ่าน position, ปิดด้วย ticket | retcode 10009 ทุกเส้นทาง · 4 รอบเปิด-ปิด · ต้นทุน ~0.8 pip/รอบ (−$0.37 จาก $299.87) | ต้องเปิด AutoTrading ใน MT5 ก่อนทุกครั้งที่ terminal รีสตาร์ท · คีย์ API ต้อง rotate |
| 2024-11-03 | 2026-11-03 | Plan A — Trend pullback (H1) | EURUSD | เข้าตามเทรนด์ EMA + pullback, SL/TP 30 pips, 0.01 lot, backtest 2 ปี (Yahoo H1) | **ปฏิเสธ** · 129 ไม้ · win 35.7% · PF 0.80 · expectancy −$0.40/ไม้ · สุทธิ −$51.03 (−17.0%) · maxDD 19.8% · แพ้ติด 11 ไม้ | break-even winrate 40.9% แต่ทำได้แค่ 35.7% → แพ้เชิงโครงสร้าง ไม่ใช่เรื่องพารามิเตอร์ |
| 2026-11-03 | 2026-11-05 (หยุด) | Mean-reversion BB+RSI (H1) | EURUSD | RSI14 + Bollinger band mean-reversion, SL/TP 30 pips, ≤2 ไม้/วัน, max 20 ไม้, 0.01 lot | หยุดก่อนเทรดจริง · backtest 251 ไม้ win 53.4% PF 1.09 (+10.2%) แต่**ครึ่งแรก PF 0.95 ขาดทุน** → ไม่ผ่านเกณฑ์ "กำไรทั้งสองครึ่ง" · เทรดจริง 0 ไม้ | ต้องมีข้อมูล M1 จาก broker และทดสอบแบบ walk-forward ก่อน · ห้ามใช้ข้อมูล Yahoo M1 (ปลอม 100% flat) |
| 2026-11-05 | **กำลังทดลอง** | Grid + EMA200 filter (H1) | EURUSD | grid 8 ระดับ ห่าง 20 pips · 0.01 lot คงที่ (ไม่มี martingale) · TP ตะกร้า +$1.00 · hard stop −$20 · ทิศเดียวตาม EMA200 · 1 ตะกร้า/ครั้ง | Backtest 50,000 แท่ง H1 จริง (2018-10→2026-11): 7,599 ตะกร้า · win 97.4% · PF 1.88 · maxDD $109 · 4/4 ไตรมาสบวก · **live เริ่ม 2026-11-05**: BUY 0.01 @ 1.12315 | maxDD = 36% ของพอร์ต (สูงเกิน) · stop เป็นฝั่งบอท ไม่ใช่ broker → gap ทำ loss เกิน −$20 ได้ · ต้องทดสอบคู่เงินอื่นและช่วง regime ต่าง ๆ |

## รายละเอียด: Grid + EMA200 (การทดลองที่กำลังวิ่ง)

**ไฟล์**
- `scripts/grid_bot_h1.py` — บอท (state: `cache/grid_state.json`, log: `cache/grid_trades.jsonl`, halt: `cache/grid_STOP`)
- `scripts/backtest_grid_h1.py` — backtester (worst-case intrabar: adverse extreme ก่อน favourable)
- `scripts/fetch_h1.py` — ดึง H1 จาก broker ผ่าน `/rates`
- cron `grid-h1-demo-test` (`6bf1fa36ffde`) — ทุก 2 นาที

**กฎที่ล็อกไว้ (ห้ามเปลี่ยนกลางการทดลอง)**
```
filter      : H1 close > EMA200 → BUY grid · ต่ำกว่า → SELL grid
grid        : 8 ระดับ × 20 pips · 0.01 lot/ระดับ (fixed, no martingale)
basket TP   : กำไรรวม ≥ +$1.00 → ปิดทั้งตะกร้า
hard stop   : ขาดทุนรวม ≤ −$20.00 → ปิดทั้งตะกร้า
limits      : 1 ตะกร้า/ครั้ง · max 0.08 lot · หยุดบอทถ้า equity < $270
execution   : H1 bar close ตัดสินทิศ · ราคาแตะระดับ → เพิ่มไม้ market order
```

**ผล backtest (ข้อมูลจริง Exness H1, 50,000 แท่ง)**

| TP | ตะกร้า | win rate | net | PF | maxDD | stops |
|---|---|---|---|---|---|---|
| $0.50 | 11,157 | 98.8% | +$2,750 | 2.00 | $56 | 138 |
| **$1.00** | **7,599** | **97.4%** | **+$3,461** | **1.88** | **$109** | **197** |
| $2.00 | 4,666 | 94.4% | +$3,568 | 1.68 | $166 | 262 |
| $3.00 | 3,227 | 90.8% | +$2,825 | 1.47 | $172 | 298 |

walk-forward 4 ไตรมาส (TP $1): +$685 / +$1,038 / +$814 / +$878 — บวกทุกช่วง
stress สเปรด 1.2 pip (จริง 0.8): PF 1.83 · maxDD $132

**สถานะ live ล่าสุด (2026-11-05)**
- balance $299.08 · equity $299.08 · ไม่มี position ค้างก่อนเริ่ม
- เปิดตะกร้าแรก: **BUY EURUSDm 0.01 @ 1.12315** · ticket `2808035229`

**สิ่งที่ต้องปรับปรุง (เรียงตามความสำคัญ)**
1. **ขนาดไม้ใหญ่เกินความเสี่ยงที่รับได้** — maxDD ใน backtest = $109 = 36% ของพอร์ต → ลดเป็น 0.005 lot/ระดับ หรือเพิ่มเงินเป็น ≥$1,000 ก่อนขยับเป็นเงินจริง
2. **stop ไม่ได้อยู่ที่ broker** — ทั้ง TP และ stop คำนวณฝั่งบอทและปิดด้วย market order ⇒ ช่วง gap/weekend ราคากระโดดข้ามได้ ควรทดสอบวาง SL ที่ broker ต่อไม้ หรือ hedge ด้วย pending stop
3. **ข้อมูล intrabar** — backtest สมมติ worst-case ordering แต่ยังไม่จำลอง slippage ตอน stop และ spread ที่กว้างขึ้นช่วงข่าว/rollover
4. **ไม่มี compounding** — ทดสอบที่ 0.01 lot คงที่ ผลเป็น absolute ไม่ใช่ % ของพอร์ตที่โตขึ้น
5. **คู่เงินเดียว ช่วงเวลาเดียว** — ต้องทดสอบ USDJPY/GBPUSD และช่วง 2018–2020 (trend แรง) แยก
6. **AutoTrading หลุดทุกครั้งที่ terminal รีสตาร์ท** — ต้องมี health check ที่เตือนทันทีที่ `trade_allowed=false`

## บทเรียนที่ใช้ซ้ำได้

- **Grid ที่ไม่มี hard stop = ruin guarantee** บนบัญชี $300: martingale ×2 ที่ 8 ระดับล้างพอร์ตด้วยเทรนด์ 160 pips (คำนวณจาก 0.01 lot, $0.10/pip)
- **ดู floating drawdown ไม่ใช่แค่ realized** — backtest รอบแรกที่คิดเฉพาะ P/L ที่ปิดแล้วรายงาน +5,126% ซึ่งผิดมหันต์; พอรวม floating DD เข้าไปเหลือ +1,154%
- **ห้ามใช้ข้อมูล M1 จาก Yahoo** — 9,573 แท่งที่ได้มา high=low=open=close 100% (มีราคาไม่ซ้ำแค่ 101 ค่า) ใช้ตัดสินใจไม่ได้
- **ตัวเลข win rate สูง (>95%) ไม่ได้แปลว่าดี** — ต้องดู PF, maxDD และ worst-case พร้อมกัน
