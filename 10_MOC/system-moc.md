---
title: System — MOC
type: moc
status: active
created: 2026-10-19
updated: 2026-10-19
tags:
  - moc
  - meta/system
aliases:
  - System MOC
  - 90_System_Prompts
---

# ⚙️ System

กฎและบทบาทที่ทำให้ vault นี้ทำงานได้สม่ำเสมอ

← กลับ [[main-hub]]

## เอกสารหลัก

- [[wiki-formatting-guide]] — กฎการเขียน: frontmatter, wikilinks, atomic notes, template ทุกชนิด
- [[hermes-wiki-persona]] — บทบาทของ Hermes: ตรวจ Inbox, จัดหมวด, อัปเดต MOC, ตรวจ orphan
- [[agent-access-policy]] — สิทธิ์อ่าน/เขียนของ agent 4 ตัว, hub contract, workflow
- [[stock-hub-template]] — เทมเพลตหน้า hub ของหุ้น
- [[main-hub]] — จุดเริ่มต้นของ graph

## เครื่องมือ

- `check-vault.py` — ตรวจสุขภาพ vault: frontmatter ครบไหม, broken link, orphan

```bash
cd "90_System_Prompts"
python3 check-vault.py            # รายละเอียดเต็ม + link graph
python3 check-vault.py --quiet    # เฉพาะสรุป
python3 check-vault.py --vault "/path/to/vault"
```

Exit code `0` = สะอาด, `1` = มีปัญหา ใช้ใน weekly review ตาม [[hermes-wiki-persona]] §6

- `check-policy.py` — ตรวจว่าการเขียนอยู่ในสิทธิ์ของ agent ตาม [[agent-access-policy]]

```bash
python3 check-policy.py            # ตรวจสถานะปัจจุบัน
python3 check-policy.py --git 30   # ตรวจ 30 commit ล่าสุด (ต้องมี prefix [agent])
```

Exit code `0` = PASS, `1` = พบการละเมิด

## Auto-push ขึ้น GitHub

`auto-push.sh` — commit + push ขึ้น `github.com/pitsanu1976/LLM_wiki` อัตโนมัติ
เรียกโดย Hermes cron job `LLM Wiki autopush` ทุก 5 นาที (no_agent — ไม่เปลือง token)

```bash
bash 90_System_Prompts/auto-push.sh       # รันมือได้ถ้าอยาก push เดี๋ยวนี้
tail -5 .git/autopush.log                # ดูประวัติ
```

พฤติกรรม: ไม่มีอะไรเปลี่ยน → เงียบ · มีของใหม่ → commit + push · push ล้ม → แจ้งเตือนใน Telegram
ใช้ SSH deploy key (`~/.ssh/llm_wiki_deploy`) — ไม่มี token เก็บใน vault

## ลำดับชั้นของ vault

```
main-hub
├── tech-ai-moc            → 20_Knowledge/21_Tech_AI/
├── offshore-ops-moc       → 20_Knowledge/22_Offshore_Ops/
├── trading-finance-moc    → 20_Knowledge/23_Trading_Finance/
├── projects-moc           → 30_Projects/
├── journals-moc           → 40_Journals/
├── inbox-moc              → 00_Inbox/
└── system-moc             → 90_System_Prompts/   (หน้านี้)
```

## ค่าคงที่ของ vault

| ค่า | ตั้งไว้ |
|---|---|
| เจ้าของ | นุ |
| ภาษา | ไทยเป็นหลัก + ศัพท์เทคนิคอังกฤษ |
| วันที่ | ISO `YYYY-MM-DD` |
| ชนิด note | 9 ค่า (ดู [[wiki-formatting-guide]] §2) |
| สร้างเมื่อ | 2026-10-19 |

## เมื่อ vault จะขยาย

ถ้า MOC ตัวไหนมีลิงก์เกิน ~30 รายการ ให้แตกเป็น MOC ย่อยแล้วลิงก์กันเป็นชั้น
อย่าให้ `main-hub` มีลิงก์ตรงไปยัง atomic note — มันควรชี้ไป MOC เท่านั้น
