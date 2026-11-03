---
title: GDDY
type: moc
status: active
ticker: GDDY
agent: leader
created: 2026-11-02
updated: 2026-11-04
tags:
  - moc
  - ticker/GDDY
related:
  - "[[2026-11-02]]"
  - "[[2026-11-03]]"
  - "[[2026-11-04]]"
  - "[[decisions]]"
  - "[[trading-finance-moc]]"
aliases:
  - GDDY
  - GoDaddy
---

# GDDY — GoDaddy

## Snapshot
| | |
|---|---|
| Sector | Internet infrastructure — domain registry / hosting / SMB tools |
| Watchlist status | **ถือจริง (OPEN)** 1.35 หุ้น @ 113.08 · fill 2026-11-03 14:37Z |
| ความเห็นล่าสุด | ไม้เดียวในบัญชี `PA3ZME9WF` ($1,000.50) · risk $9.09 (0.909%) · R:R 2.77 · stop 106.35 = 1.32×ATR14 5.08 · mark 113.45 (+$0.50) |

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
### 2026-11-02 — BUY rev3: 1.35 @113.60 · stop 106.35 · target 131.74
- ยกเลิก rev2 `67e075ae` (1.739 @115.00) เพราะ stop 110.80 = **0.87×ATR** = แคบกว่า noise (ผิดเกต ≥1 ATR) และ R:R 3.99 มาจาก stop ที่บีบ
- rev3 ใช้ stop โครงสร้างของ tech **106.35** (ใต้ cluster 94.02–110.90) = 1.50×ATR · entry ปรับลงมาอยู่ในโซน ≤114.81 เพื่อให้ R:R ≥2
- ขนาด: 10.00 / 7.25 = 1.379 → **1.35 หุ้น** (เผื่อ slippage) = notional **$153.36 (15.3%)** · risk **$9.79 (0.979%)** · **R:R 2.50**
- fractional ทำ bracket ไม่ได้ ⇒ stop/target เป็น **manual** (`ingest/manual_stops.json`) + watchdog ทุก 15 นาที
- บันทึก: [[2026-11-02]]

### 2026-11-03 — RE-ARM #2 (order หมดอายุ ไม่ใช่ถูก invalidate)
- `858c1f0a` = **EXPIRED 2 พ.ย. 21:00Z filled 0** · low วันนั้น 115.93 ไม่แตะ limit 113.60 · ปิด 116.61 > stop 106.35
- ส่งใหม่ **`9d3c7071`** 1.35 @113.60 · **DAY (หมดอายุ 3 พ.ย. 21:00Z)** · stop 106.35 = **1.48×ATR 4.892** · target 131.74
- บันทึก: [[2026-11-03]]

### 2026-11-03 — ✅ FILLED: 1.35 @ 113.08 (ไม้เปิดจริงไม้แรกของบัญชี)
- order `9d3c7071` (1.35 @113.60 · DAY · simple) **fill 2026-11-03 14:37:25Z ที่ 113.08** — ดีกว่า limit $0.52 · mv $153.16 · mark 113.45 (**+$0.50**)
- **ไม่มี legs ที่ broker** (fractional บังคับ simple+DAY) ⇒ stop **106.35** / target **131.74** เป็น manual ใน `ingest/manual_stops.json` + watchdog `fractional-stop-watchdog` (`*/15 13-21 จ.-ศ.`) — `--status` ยืนยัน `held=1.35 stop=106.35 target=131.74`
- ตัวเลขจริงหลัง fill: stop 6.73 = **1.32×ATR14 5.08** · risk **$9.09 (0.909% ของ $1,000.50)** · **R:R 2.77** · weight **15.31%** ≤20% · cash เหลือ $847.34 ≥ reserve $200
- รอบ DAILY 2026-11-04: คัด 10 ชื่อ AI/semis ใหม่ — **ไม่มีชื่อใดผ่านเกตคะแนน** ⇒ **ไม่เพิ่มไม้** (GDDY ยังเป็นไม้เดียว, 2 ช่องว่าง)
- **invalidation:** ปิด 1D < **106.35** → watchdog ขาย market ทั้งจำนวน · ทบทวนถึง **2026-12-15**
- หมายเหตุ: block `agent:news` / `agent:tech` / `agent:finance` ของหน้านี้ยังว่าง — รอบนี้ใช้รายงานต้นทาง `reports/{news,tech,finance}/2026-11-04-DAILY.md` แทน (ไม่เดาแทน block ที่ว่าง)
- บันทึก: [[2026-11-04]]

### สถานะปัจจุบัน (2026-11-04)
- **ถือ GDDY 1.35 @113.08** · stop 106.35 · target 131.74 · **1/3 ไม้**
- ความเสี่ยงค้าง: ไม่มี broker-side stop — พึ่ง watchdog ทุก 15 นาที · gap เปิดต่ำกว่า 106.35 จะขายที่ tick ถัดไป (ยอมรับ slippage)
<!-- agent:leader:end -->

## แหล่งข้อมูล

- ข่าว: `20_Knowledge/24_News_Archive/`
- เทคนิค: `20_Knowledge/25_Tech_Analysis/`
- งบการเงิน: `20_Knowledge/26_Financial_Data/`
- บันทึกการตัดสินใจ: [[decisions]]

## เกี่ยวข้อง

- [[2026-11-02]] · [[2026-11-03]] · [[2026-11-04]] — วันที่ตัดสิน/ส่งคำสั่ง/fill
- [[trading-finance-moc]] · [[journals-moc]]
