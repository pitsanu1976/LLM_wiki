---
title: Agent Access & Workflow Policy
type: system
status: active
created: 2026-10-19
updated: 2026-10-19
tags:
  - system/policy
  - meta/access
  - domain/finance
aliases:
  - สิทธิ์ของ Agent
  - RBAC
  - Agent Policy
---

# Agent Access & Workflow Policy

> สัญญาระหว่าง agent ทั้ง 4 ตัวกับ vault — ใครอ่านอะไรได้ ใครเขียนอะไรได้
> และเมื่อหลายตัวเขียนพร้อมกันจะไม่ทับกันอย่างไร

## 0. หลักการ 4 ข้อ

| # | หลักการ | เพราะอะไร |
|---|---|---|
| 1 | **Single writer** — หนึ่งไฟล์มีเจ้าของคนเดียว | Hermes เขียนไฟล์ทั้งไฟล์ (ไม่ใช่ patch) ถ้าสองตัวเขียนไฟล์เดียวกัน ตัวหลังจะทับตัวแรก |
| 2 | **Append-only สำหรับหลักฐาน** | ข้อมูลที่ใช้ตัดสินใจต้องย้อนดูได้ ถ้าแก้ย้อนหลังจะตรวจสอบไม่ได้ |
| 3 | **Hub เป็นมุมมอง ไม่ใช่สมุดร่าง** | `<TICKER>.md` ทำหน้าที่รวมลิงก์ ไม่ใช่ที่ลองเขียนอะไรก็ได้ |
| 4 | **ทุกอย่างอยู่ใน git** | ใครเขียนอะไรเมื่อไร ตรวจย้อนหลังได้เสมอ |

> **หมายเหตุเรื่องเลขโฟลเดอร์:** ใช้ `24/25/26` แทน `23/24/25` ที่ระบุในโจทย์
> เพราะ `23_Trading_Finance` มีอยู่แล้ว และ `30_Projects` ก็จองเลข 30 ไปแล้ว
> จึงใช้ `50_Watchlist` แทน `30_Watchlist`

---

## 1. Agent ทั้ง 4 ตัว

| Agent | profile | หน้าที่ | เขียนที่ | Output หลัก |
|---|---|---|---|---|
| 🤖 **News** | `news` | กวาดข่าวจาก RSS/เว็บ สรุปเป็น bullet | `00_Inbox/` · `20_Knowledge/24_News_Archive/` | `<TICKER>_news_YYYY-MM-DD.md` |
| 📊 **Tech** | `tech` | คำนวณ indicator (RSI, MACD, MA) สรุปภาวะเทคนิค | `00_Inbox/` · `20_Knowledge/25_Tech_Analysis/` | `<TICKER>_tech_YYYY-MM-DD.md` |
| 💰 **Finance** | `finance` | วิเคราะห์งบ ดุล อัตราส่วน (P/E, ROE, D/E) | `00_Inbox/` · `20_Knowledge/26_Financial_Data/` | `<TICKER>_fin_YYYY-QN.md` |
| 👑 **Leader** | `leader` | รวมข้อมูล 3 ด้าน ตัดสินใจ Buy/Sell/Hold | `00_Inbox/` · `50_Watchlist/` · `10_MOC/stocks/` | `<TICKER>.md` (Decision) |

**มนุษย์ (นุ)** — สิทธิ์เต็มทุกที่ รวม `90_System_Prompts/` ที่ agent ห้ามแตะ

---

## 2. ตารางสิทธิ์ (RBAC)

`W` = สร้าง/แก้ได้ · `R` = อ่านอย่างเดียว · `—` = ไม่มีสิทธิ์

| Path | News | Tech | Finance | Leader | มนุษย์ |
|---|:--:|:--:|:--:|:--:|:--:|
| `00_Inbox/` | W | W | W | W | W |
| `10_MOC/main-hub.md` | R | R | R | R | W |
| `10_MOC/stocks/<T>.md` | *block* | *block* | *block* | W | W |
| `20_Knowledge/21_Tech_AI/` | R | R | R | R | W |
| `20_Knowledge/22_Offshore_Ops/` | R | R | R | R | W |
| `20_Knowledge/23_Trading_Finance/` | R | R | R | R | W |
| `20_Knowledge/24_News_Archive/` | **W** | R | R | R | W |
| `20_Knowledge/25_Tech_Analysis/` | R | **W** | R | R | W |
| `20_Knowledge/26_Financial_Data/` | R | R | **W** | R | W |
| `30_Projects/` | R | R | R | R | W |
| `40_Journals/` | — | — | — | W | W |
| `50_Watchlist/` | R | R | R | **W** | W |
| `90_System_Prompts/` | R | R | R | R | **W** |

`*block*` = เขียนได้เฉพาะ block ของตัวเองในหน้านั้น (ดู §4)

**อ่านข้ามโดเมนได้หมด** — นี่คือจุดแข็งของ wiki: Tech อ่านข่าวได้ Finance อ่านกราฟได้
แต่ **เขียนได้เฉพาะบ้านตัวเอง**

---

## 3. กติกาการเขียนไฟล์

### 3.1 ชื่อไฟล์

```
24_News_Archive/AAPL_news_2026-10-19.md
25_Tech_Analysis/AAPL_tech_2026-10-19.md
26_Financial_Data/AAPL_fin_2026-Q3.md
```

- `<TICKER>` ตัวพิมพ์ใหญ่
- วันที่ ISO `YYYY-MM-DD` / ไตรมาส `YYYY-QN`
- **ห้ามใส่คำอธิบายยาวในชื่อไฟล์** — ใส่ใน `title:` แทน

### 3.2 Frontmatter บังคับ

```yaml
---
title: "AAPL — ข่าว 19 ต.ค. 2026"
type: source          # source | concept | howto | reference
status: active
created: 2026-10-19
updated: 2026-10-19
agent: news           # news | tech | finance | leader | human
ticker: AAPL
tags:
  - news/earnings
  - ticker/AAPL
---
```

- **`agent:` คือฟิลด์ที่ใช้บังคับสิทธิ์** — checker ตรวจว่าไฟล์ในโฟลเดอร์ของใคร ต้องประกาศ `agent:` ตรงกับเจ้าของ
- `ticker:` จำเป็นสำหรับไฟล์ใน `24/25/26` และ `10_MOC/stocks/`

### 3.3 Append-only

| สถานการณ์ | ทำอะไร |
|---|---|
| ข้อมูลวันใหม่ | สร้างไฟล์ใหม่ตามวันที่ |
| ข้อมูลเดิมผิด | สร้างไฟล์ใหม่ `..._correction.md` ระบุว่าอะไรผิด |
| ไฟล์ซ้ำหัวข้อ | รวมเป็นไฟล์เดียว แต่ต้องแจ้ง Leader ก่อน |

**ห้ามลบไฟล์** — ถ้าไม่ใช้แล้วให้ตั้ง `status: archived`

### 3.4 ลิงก์บังคับ

ทุกไฟล์ใน `24/25/26` ต้องมีอย่างน้อย:
- `[[AAPL]]` — ลิงก์ไป hub ของหุ้นตัวนั้น
- 1 MOC ที่เกี่ยวข้อง

---

## 4. Hub Contract — `10_MOC/stocks/<TICKER>.md`

หน้า hub คือ**จุดเดียว**ที่ข้อมูล 3 ด้านมาบรรจบกัน Leader อ่านหน้านี้เป็นหลัก

### 4.1 โครงสร้าง block

```markdown
## 📰 News
<!-- agent:news:begin -->
(News agent เขียนเฉพาะในบล็อกนี้)
<!-- agent:news:end -->

## 📈 Technical
<!-- agent:tech:begin -->
...
<!-- agent:tech:end -->

## 💰 Financial
<!-- agent:finance:begin -->
...
<!-- agent:finance:end -->

## 👑 Decision
<!-- agent:leader:begin -->
...
<!-- agent:leader:end -->
```

- เนื้อหา **นอก** block ทั้งหมดเป็นของ **Leader** (เจ้าของหน้า)
- block หนึ่งมีเจ้าของเดียว ห้ามซ้อน block
- ห้ามลบ marker — ถ้าลบ checker จะจับได้ทันที

### 4.2 ขั้นตอนเขียน hub (สำคัญ)

```
1. flock  ไฟล์ .lock ของ ticker
2. อ่านไฟล์ทั้งไฟล์
3. หา block ของตัวเองด้วย marker
4. แทนที่เฉพาะเนื้อหาระหว่าง marker ของตัวเอง
5. เขียนกลับทั้งไฟล์
6. ปลด lock
```

> **ทำไมต้อง lock:** Hermes เขียนไฟล์ทั้งไฟล์ ถ้า Tech กับ Finance เขียนพร้อมกัน
> ตัวที่เขียนทีหลังจะทับการแก้ของตัวแรกในบล็อกอื่นด้วย — lock + read-modify-write แก้ปัญหานี้

### 4.3 กติกาความขัดแย้ง

- ถ้าพบว่า block ของตัวเองถูกแก้โดยคนอื่น → **หยุด เขียนใน `00_Inbox/` แทน แล้วแจ้ง Leader**
- Leader เป็นผู้ตัดสินสุดท้ายเรื่องเนื้อหาในหน้า hub

---

## 5. Workflow รายวัน

```mermaid
flowchart LR
    subgraph ดึงข้อมูล
        N[🤖 News<br/>06:00] --> N1[24_News_Archive/AAPL_news_*.md]
        T[📊 Tech<br/>06:15] --> T1[25_Tech_Analysis/AAPL_tech_*.md]
        F[💰 Finance<br/>06:30<br/>รายไตรมาส] --> F1[26_Financial_Data/AAPL_fin_*.md]
    end

    N1 --> H[📄 10_MOC/stocks/AAPL.md]
    T1 --> H
    F1 --> H

    H --> L[👑 Leader<br/>07:00]
    L --> D[50_Watchlist/decisions.md]
    L --> H2[Decision block ใน AAPL.md]
```

### ลำดับเวลา (กันชนกัน)

| เวลา | Agent | ทำอะไร |
|---|---|---|
| 06:00 | News | เขียนไฟล์ข่าว + อัปเดต block News ใน hub |
| 06:15 | Tech | คำนวณ indicator + เขียนไฟล์ + block Technical |
| 06:30 | Finance | (รายไตรมาส) เขียนไฟล์ + block Financial |
| 07:00 | Leader | อ่าน hub ทั้งหน้า → ตัดสินใจ → เขียน block Decision + `50_Watchlist/decisions.md` |

**เว้น 15 นาทีระหว่าง agent** — ลดโอกาสเขียน hub พร้อมกัน
ถ้า agent ตัวไหนช้ากว่า window ให้ข้าม block ของ hub แล้วเขียนแค่ไฟล์ของตัวเอง (Leader จะ merge ให้)

### ตัวอย่างจริง: AAPL

1. **News** เจอข่าวผลิตภัณฑ์ใหม่ → `24_News_Archive/AAPL_news_2026-10-19.md`
   พร้อม `[[AAPL]]` + `#news/product`
2. **Tech** กราฟทะลุ resistance → `25_Tech_Analysis/AAPL_tech_2026-10-19.md`
   (RSI 68, MACD ตัดขึ้น, ปริมาณ 1.8× ค่าเฉลี่ย 20 วัน)
3. **Finance** กำไรโตต่อเนื่อง → `26_Financial_Data/AAPL_fin_2026-Q3.md`
   (P/E, ROE, D/E พร้อมวันที่ของงบ)
4. **Leader** อ่าน `[[AAPL]]` ทั้งหน้า → ประเมินความเสี่ยง → เขียน Decision
   ลง block ของตัวเอง + `50_Watchlist/decisions.md`

---

## 6. ข้อยกเว้น

| สถานการณ์ | วิธีทำ |
|---|---|
| ต้องเขียนนอก scope | เขียนใน `00_Inbox/` ชื่อ `<agent>-<เรื่อง>.md` แล้วแจ้ง Leader |
| พบข้อมูลผิดของ agent อื่น | **ห้ามแก้เอง** — เขียน correction ใน `00_Inbox/` + ลิงก์ไฟล์ที่ผิด |
| ต้องแก้ `90_System_Prompts/` | ห้ามทุกกรณี — แจ้งมนุษย์ |
| ไฟล์ชนกัน (conflict) | หยุด เขียนใน `00_Inbox/` แจ้ง Leader |

---

## 7. การบังคับใช้

### 7.1 ตัวตรวจ

```bash
cd "~/Documents/Obsidian Vault/90_System_Prompts"
python3 check-policy.py            # ตรวจสถานะปัจจุบัน
python3 check-policy.py --git 30   # ตรวจ 30 commit ล่าสุด (ต้องมี prefix [agent])
```

ตรวจ 4 อย่าง:
1. ไฟล์ในโฟลเดอร์ของ agent ต้องมี `agent:` ตรงกับเจ้าของ
2. ไฟล์ใน `24/25/26` ต้องมี `ticker:` และลิงก์ `[[<TICKER>]]`
3. Hub ต้องมี marker ครบ 4 block และไม่ซ้อนกัน
4. (`--git`) commit ที่ขึ้นต้นด้วย `[news]`/`[tech]`/`[finance]`/`[leader]` ต้องแตะเฉพาะ path ที่อนุญาต

### 7.2 Commit convention

ถ้า agent commit เอง ให้ขึ้นต้นข้อความด้วย:

```
[news] AAPL: ข่าวผลิตภัณฑ์ใหม่
[tech] AAPL: RSI 68, MACD ตัดขึ้น
[finance] AAPL: Q3 กำไรโต 12%
[leader] AAPL: HOLD — รอ confirm ปริมาณ
```

ไม่มี prefix = ถือว่าเป็นมนุษย์ (อนุญาตทุก path)

### 7.3 เมื่อพบการละเมิด

1. checker รายงาน path + agent + เหตุผล
2. Leader แจ้งเตือนในรอบถัดไป
3. ถ้าซ้ำ → มนุษย์แก้ที่ SOUL.md ของ agent นั้น

> การบังคับใช้เป็น **การตรวจสอบย้อนหลัง** ไม่ใช่การบล็อกแบบ real-time
> เพราะทุก agent รันด้วย user เดียวกัน ระบบไฟล์แยกสิทธิ์ไม่ได้จริง —
> สิ่งที่แยกได้คือ *วินัยที่เขียนไว้ใน SOUL* + *ตัวตรวจที่จับได้*

---

## 8. ความสัมพันธ์กับระบบ file-queue เดิม

ทีมหุ้นปัจจุบันใช้ `/opt/data/home/hermes-stock-team/workspace` เป็นคิวไฟล์
(`inbox/<line>/` → `reports/<line>/` → `done/`)

| ชั้น | ใช้ทำอะไร | อายุข้อมูล |
|---|---|---|
| **file-queue** | handoff ระหว่าง agent ต่อรอบ | ชั่วคราว — ใช้แล้วทิ้ง |
| **wiki (vault นี้)** | ความรู้สะสมที่มนุษย์อ่านและค้นได้ | ถาวร + มี git history |

**กติกา:** queue คือท่อ, wiki คือคลัง — agent เขียนผลลง wiki *หลัง* ส่งงานใน queue สำเร็จ
ไม่ใช่เขียน wiki แทน queue

---

## เกี่ยวข้อง

- [[main-hub]]
- [[system-moc]]
- [[wiki-formatting-guide]]
- [[hermes-wiki-persona]]
- [[trading-finance-moc]]
