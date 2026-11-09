---
title: relia-work — Kanban
type: project
status: active
created: 2026-11-02
updated: 2026-11-02
tags:
  - project/kanban
  - reliability/cmms
aliases:
  - relia-work
  - Reliability Intelligence Platform
related:
  - projects-moc
  - RCM Reliability Centered Maintenance
kanban-plugin: board
---

# relia-work — Kanban

บอร์ดงานของ **Reliability Intelligence Platform** (`/opt/data/projects/reliability-app`) รวมงานวิเคราะห์ CMMS + งาน knowledge ที่ป้อนเข้าไป
WIP limit: **3 ใบใน Doing** · การ์ดที่ค้างเกิน 2 สัปดาห์ให้ย้ายไป Blocked พร้อมระบุสิ่งที่รอ

## Backlog

- [ ] ต่อ Oracle eAM ตรง ๆ แทน Excel — เขียน `etl.load_from_oracle()` คืน DataFrame ชื่อเดียวกับ sheet เดิม (สัญญาตาม README §2) #oracle #app
- [ ] ออกแบบ failure code dictionary 3 แกน: WO type / Activity Type / Activity Cause + รหัส ISO 14224 (อ้าง `brain2nd/data/oracle-eam/*.csv`) #data-quality #cmms
- [ ] บังคับกรอก Failure Code + Activity Cause ตอนปิด WO ใน Oracle (lookup `WIP_EAM_FAILURE_CODE`) #cmms #oracle
- [ ] เพิ่ม confidence band บน Weibull probability plot (ตอนนี้เป็น point estimate; n=20 ทำให้ β ไม่แน่นอน) #weibull #app
- [ ] แยกอ่าน β ระดับชิ้นส่วน (gearbox 2.69, seal) แทนระบบ (≈1) — ทำป้ายเตือนใน UI ไม่ให้อ่าน β ระบบผิด #weibull #app
- [ ] Export ผลเป็น PDF/Excel รายเดือนสำหรับส่งผู้บริหาร #app
- [ ] Deploy จริง: docker/systemd + backup SQLite อัตโนมัติ #app #ops
- [ ] Auth + multi-user (ตอนนี้เปิดโล่งใน LAN) #app #ops
- [ ] สืบสวน common-cause 7 วันที่เสียพร้อมกัน — แยกสาเหตุร่วมจริง vs ปัญหาการบันทึก (FINDINGS §7.4) #analysis
- [ ] แผน condition monitoring gearbox: vibration + oil analysis ตาม P-F interval #analysis #cmms
- [ ] Recalibrate reorder point ด้วย lead time จริงจากจัดซื้อ (ตอนนี้ใช้ค่าประมาณ) #spares
- [ ] Source note + reading notes *Efficacy of Maintenance* 17 บท เข้า brain2nd #vault
- [ ] หน้า wiki `CMMS Failure Coding` จาก `data/oracle-eam/` + mapping ISO 14224 #vault #cmms
- [ ] ถอด ISO 14224 Table B.4/B.5 จาก PETROSYNC sl.100 → ขยาย [[Failure Hierarchy]] จาก 19 modes เป็นรหัส ISO #vault
- [ ] Reading notes PETROSYNC Applied RCM 8 โมดูล (173 สไลด์) #vault
- [ ] ขอ export CMMS ย้อนหลัง 12 เดือน (n=20 events น้อยเกินให้ CI แคบ) #data

## Next — สัปดาห์นี้

- [ ] ล็อก code list 15–25 failure modes สำหรับ Compressor + mapping ลง ISO 14224 (ใช้ `iso14224_map.csv` เป็นฐาน) #data-quality
- [ ] ร่างนโยบาย seal opportunistic replacement (เปลี่ยนทุกครั้งที่เปิด gearbox) — เริ่มจาก FINDINGS §7.1 #analysis
- [ ] ตัดสินใจ hard-time gearbox ~239 วัน vs รอ annual shutdown — เทียบ downtime cost สองทาง #weibull

## Doing

- [ ] ตรวจ data quality รอบใหม่หลังแก้ WO duplicate — เทียบ `/api/quality` ก่อน/หลัง #data-quality

## Blocked

- [ ] ขอสิทธิ์ read-only schema Oracle eAM จาก IT (ต้องมีก่อนเริ่ม `load_from_oracle`) #oracle
- [ ] รอไฟล์ export 12 เดือนจาก CMMS admin #data

## Review — รอตรวจ

- [ ] Weibull dashboard (เสร็จเชิงเทคนิค) — รอผู้ใช้ตรวจว่า flood/percentile ที่แสดงตรงกับที่ planner ใช้จริง

## Done

- [x] ETL: Excel → SQLite + Warehouse + data quality report
- [x] Weibull MLE, MTBF/MTTR, trend test, age-replacement optimisation
- [x] Pareto (equipment/item/mechanism/discipline), cost breakdown (deferred production/labor/material)
- [x] Spares risk + exposure, patterns (lag pair, common cause), `/api/optimize`
- [x] SPA 5 หน้า: dashboard, weibull, patterns, spares, data quality (Plotly offline)
- [x] รายงาน `docs/FINDINGS_TH.md` (8 หัวข้อ + ข้อเสนอ 6 ข้อ)
- [x] brain2nd: Oracle eAM UG 11i + Training Vol.1–2 + PETROSYNC RCM เข้า raw (พร้อม source note)
- [x] brain2nd: `data/oracle-eam/` 48 แถว ตรวจ quote ทุกแถวด้วย `validate.py` (PASS)

### ลิงก์

- แอป: `/opt/data/projects/reliability-app` · `README.md` · `docs/FINDINGS_TH.md`
- Knowledge: [[RCM Reliability Centered Maintenance]] · [[Failure Hierarchy]] · [[ISO 14224 Taxonomy]] · [[CMMS]]
- Raw ที่ ingest ล่าสุด: `raw/oracle-manual.md` · `raw/oracle-eam-user-guide.md` · `raw/applied-rcm.md`
