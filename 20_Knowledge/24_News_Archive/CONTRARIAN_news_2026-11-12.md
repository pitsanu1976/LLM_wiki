---
title: "CONTRARIAN — คัดรายชื่อ 2026-11-12"
type: source
status: active
created: 2026-11-12
updated: 2026-11-12
agent: news
scope: market
ticker: MULTI
tags:
  - news/contrarian
  - ticker/NVDA
  - ticker/INTC
  - ticker/MRVL
  - ticker/NOW
  - ticker/SMCI
---

# CONTRARIAN — คัดรายชื่อตามกลยุทธ์ CONTRARIAN-REVERSAL (ดึงข้อมูล 2026-11-12)

## สรุป 3 บรรทัด
- คัดจาก universe 506 ชื่อ (S&P 500 เป็นหลัก) ด้วยราคาปิด **2026-11-11** (Alpaca 1Day, feed=iex): **42 ชื่อ** ตก ≥20% จาก 20-day high แต่ผ่านด่าน ADV20 ≥ $50M + ราคา ≤ $198.74 เพียง **8 ชื่อ**.
- **ไม่มีชื่อผ่านครบทุกเกต** — ชื่อเดียวที่ผ่านข้อ 1–5 คือ [[NVDA]] (เหตุ = วิกฤตผู้บริหาร) และตกข้อ 6 เพราะมีงบ Q3 FY2027 วันที่ **17 พ.ย. 2026**.
- 7 ใน 8 ชื่อที่เหลือมีสาเหตุเป็นพื้นฐาน/AI de-rating ไม่ใช่ภาพลักษณ์ ⇒ 17/21 ของลิสต์มาจากธีม AI-infra เดียว = ตามกติกา **"broad bearish ⇒ ห้ามเข้าไม้ใหม่ทั้งรอบ"** (แต่ breadth ตลาด 11-11 ยังเป็นบวก 323/153)

## ข่าวและแหล่งอ้างอิง

| # | พาดหัว | แหล่ง | วันที่ | ลิงก์ |
|---|---|---|---|---|
| 1 | NVDA: CEO Jensen Huang ลาออก 12 พ.ย. 2026 · CFO Colette Kress เป็น interim CEO (ไทม์ไลน์: NYT 29 ต.ค. → ยอมรับ affair 8 พ.ย. → FBI สอบ 9 พ.ย. → ลาออก 12 พ.ย.) | BBC News live (ไทม์ไลน์ระบุวันที่เอง) | 2026-11-12 15:44 GMT | https://www.bbc.com/news/live/c6zjry11v8w1t |
| 2 | NVDA intraday 12 พ.ย. เปิด −13% (ลบ >$5 แสนล้าน) แล้วฟื้นราว −6% | BBC News live | 2026-11-12 intraday | https://www.bbc.com/news/live/c6zjry11v8w1t |
| 3 | MRVL ซื้อ Lumentum (LITE) all-stock ~$115B · 4.5:1 · ผู้ถือ MRVL เดิมเหลือ 67% = dilution ใหม่ | SEC EDGAR exhibit 99.1 + Motley Fool | 2026-11-02 | https://www.sec.gov/Archives/edgar/data/1835632/000119312526442714/d81187dex991.htm |
| 4 | NOW Q3 (28 ต.ค.) EPS $1.00 พลาด $1.02 · Q4 cRPO guide 18.5% (จาก 21%) ⇒ −26.95% ไป 109.67 | Pomerantz alert + Forbes (อ้าง SEC filing) | 2026-10-29 | https://prnewswire.com/news-releases/investor-alert-pomerantz-law-firm-investigates-claims-on-behalf-of-investors-of-servicenow-inc---now-302937435.html |
| 5 | INTC Q3 (29 ต.ค.) + Q4 guide ต่ำกว่าคาดมาก + เตือน burn cash · −23% after hours | Reuters | 2026-10-29 | https://www.reuters.com/business/intel-signals-slower-growth-pc-market-remains-under-pressure-2026-10-29/ |
| 6 | SMCI Q1 FY27 (3 พ.ย.): GM 12.7% (จาก 17.5%) + ลูกค้ารายเดียว 44% ของรายได้ · คดีส่งออกชิป (contractor สารภาพผิด ต.ค.) | Zacks/Yahoo + Benzinga | 2026-11-03 | https://zacks.com/stock/news/3024554/smci-stock-falls-5-7-after-q1-results:-should-you-hold-or-fold |

## Sentiment
**Bearish (narrow: AI-infra) / Mixed (ภาพตลาด)** — breadth ปิด 11-11: ขึ้น 323 / ลง 153 / median +0.42% (คำนวณเอง จาก 506 ชื่อ)

## ตัวกระตุ้นราคา
- [[NVDA]] งบ Q3 FY2027 **17 พ.ย. 2026 ~21:20Z** (NVIDIA newsroom) = เหตุการณ์ที่จะกลบข่าวผู้บริหารทั้งหมด — อยู่ในกรอบถือ 10 session ⇒ ตกเกตข้อ 6
- MRVL: ปิดดีลคาด H1 2028 ⇒ dilution ยังเป็น overhang ต่อเนื่อง
- ธีม: ราคา memory · export control จีน · crypto (HOOD/COIN)

## ข้อมูลที่ดึงไม่ได้
- Alpaca SIP ถูกปฏิเสธ `403 subscription does not permit querying recent SIP data` ⇒ ใช้ feed=iex (ตรวจ NVDA 173.85 iex vs 173.73 sip = ต่าง 0.07%)
- S&P 400 list: `CRAWL_NOT_FOUND` ⇒ universe ไม่ครอบ mid/small cap
- สาเหตุของ DDOG, NBIS และอีก ~24 ชื่อในลิสต์ 42 ชื่อ ยังไม่ตรวจ

ไฟล์เต็ม: `hermes-stock-team/workspace/reports/news/2026-11-12-CONTRARIAN.md`

## เกี่ยวข้อง
- [[trading-finance-moc]]
- [[NVDA]]
