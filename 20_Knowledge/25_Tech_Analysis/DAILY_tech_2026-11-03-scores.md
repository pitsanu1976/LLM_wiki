---
title: "DAILY — Technical T-scores 2026-11-03 (10 ชื่อ, ADDENDUM)"
type: source
status: active
created: 2026-11-03
updated: 2026-11-03
agent: tech
ticker: DAILY
scope: market
tags:
  - tech/indicators
  - tech/scoring
  - ticker/NVDA
  - ticker/MSFT
  - ticker/AMZN
  - ticker/TSM
  - ticker/AVGO
  - ticker/CEG
  - ticker/ETN
  - ticker/AMAT
  - ticker/PLTR
  - ticker/ANET
---

# DAILY — คะแนน T (คุณภาพ setup ทางเทคนิค) 2026-11-03

ต่อยอดจาก [[DAILY_tech_2026-11-03]] (รายงานฐาน: entry/stop/target + S/R) · ไฟล์นี้เพิ่มเฉพาะ**คะแนน T 0–10** ที่ leader ขอใน ADDENDUM · ไม่ดึงข้อมูลใหม่

**ข้อมูล:** Alpaca SIP `1Day` consolidated · **แท่งปิดล่าสุด = 1D 2026-11-02** (ดึง 2026-11-02 22:47 UTC) · 1W ปิดสัปดาห์ 2026-10-30 · indicator คำนวณด้วยโค้ด (Wilder RSI/ATR, EMA12/26 MACD)

## คะแนน T (median 7, ช่วง 6–8)

- **PLTR 8** — ชื่อเดียวที่ 1W ยังขึ้น (184.11 > wMA20 163.08, wRSI 55.8, wHist +2.92); net R:R 2.23
- **ETN 7** — net R:R 2.95 สูงสุด; 1D ขาลงชัด, งบ 11-03 ก่อนเปิด
- **AMZN 7** — ปิด +2.20% วันเดียวกับ SMH −2.71%, vol 1.36x; entry สูงกว่าแนวรับ 1.28 ATR
- **CEG 7** — ออกข้าง + wHist พลิกบวก; vol 0.81x ต่ำสุด, stop 1.05 ATR บางสุด
- **NVDA 7** — double bottom 200.92/201.66, stop 1.16 ATR; 1D+1W ลงทั้งคู่
- **AMAT 7** — 372.80 ทดสอบ 4 ครั้ง; stop 6.64% ⇒ ไม้แค่ $151
- **AVGO 6** — vol 0.91x, 1W −11.4% ใต้ wMA20, T2 = MA50 ลาดลง
- **MSFT 6 (NO PLAN)** — trend ดีสุดในลิสต์ แต่ net R:R 0.98 → ติดเพดาน cap
- **TSM 6 (NO PLAN)** — structure 7.5 แต่ net R:R 1.21 → ติดเพดาน cap
- **ANET 6** — structure ต่ำสุด 4.5 (แนวรับ 163.25 ทดสอบครั้งเดียว, entry ห่าง 0.93 ATR)

## เกณฑ์

5 มิติ: structure 30% · R:R net 25% · stop safety 20% · trend alignment 15% · volume 10% · cap: `net R:R(T2) < 2.0 → T ≤ 6` และ `stop < 1 ATR → T ≤ 5`
trend ถ่วงแค่ 15% เพราะทั้ง 10 ชื่ออยู่ใต้ MA20 (1D) = เงื่อนไขคงที่ ไม่จำแนกชื่อ

## บทเรียนที่ใช้ซ้ำได้

- ในลิสต์ที่ทั้งกลุ่มเป็น downtrend เดียวกัน **มิติ trend กลายเป็นค่าคงที่** — ต้องลดน้ำหนักและให้ structure/R:R เป็นตัวจำแนก ไม่งั้นทุกชื่อได้คะแนนเท่ากัน
- **structure ของแผนที่ออกแบบให้ entry เกาะแนวรับอยู่แล้วจะแบน** (4.5–7.5) ⇒ ตัวจำแนกจริงคือ **จำนวนครั้งที่แนวรับถูกทดสอบ** และ **ระยะ entry ถึงแนวรับเป็น ATR**
- คะแนนที่ชนเพดานจาก cap (MSFT/TSM) ต้องรายงาน **ค่าดิบคู่กับค่าที่ติดเพดาน** ไม่งั้น leader อ่านผิดว่า trend แย่ ทั้งที่ปัญหาเดียวคือ R:R

รายงานเต็ม: `reports/tech/2026-11-03-DAILY-scores.md` · เกี่ยวข้อง: [[trading-finance-moc]]
