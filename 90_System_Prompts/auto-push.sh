#!/usr/bin/env bash
# auto-push.sh — commit + push vault ขึ้น GitHub ถ้ามีการเปลี่ยนแปลง
#
# ออกแบบให้รันซ้ำได้บ่อยแค่ไหนก็ได้ (idempotent):
#   - ไม่มีอะไรเปลี่ยน + ไม่มี commit ค้าง  -> เงียบ ออก 0
#   - มีของใหม่                              -> commit แล้ว push
#   - push รอบก่อนล้มเหลว                    -> รอบนี้ลอง push ซ้ำให้
#
# ใช้กับ Hermes cron แบบ no_agent: stdout ว่าง = ไม่ส่งอะไร, มี error = แจ้งเตือน
set -uo pipefail

VAULT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG="$VAULT/.git/autopush.log"
LOCK="${TMPDIR:-/tmp}/llm-wiki-autopush.lock"
BRANCH="master"

exec 9>"$LOCK"
flock -n 9 || exit 0            # มีรอบอื่นกำลังทำงานอยู่ -> ข้าม

cd "$VAULT" || { echo "AUTOPUSH ERROR: vault not found: $VAULT"; exit 1; }
[ -d .git ] || { echo "AUTOPUSH ERROR: not a git repo: $VAULT"; exit 1; }

note() { printf '[%s] %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" >>"$LOG"; }

# ---------- 1) stage + commit ----------
git add -A

if ! git diff --cached --quiet; then
    N=$(git diff --cached --name-only | wc -l | tr -d ' ')
    FILES=$(git diff --cached --name-only | head -5 | tr '\n' ' ')
    if ! git commit -q -m "vault: sync $(date -u +%Y-%m-%dT%H:%MZ) — ${N} file(s)

${FILES}"; then
        echo "AUTOPUSH ERROR: commit failed"
        note "commit failed"
        exit 1
    fi
    note "committed ${N} file(s)"
fi

# ---------- 2) มีอะไรต้อง push ไหม ----------
if git rev-parse --verify --quiet "origin/${BRANCH}" >/dev/null; then
    AHEAD=$(git rev-list --count "origin/${BRANCH}..HEAD" 2>/dev/null || echo 1)
else
    AHEAD=1                      # ยังไม่เคย fetch สำเร็จ -> ต้องลอง push
fi
if [ "$AHEAD" -eq 0 ]; then
    exit 0                       # เงียบ: ไม่มีอะไรต้องทำ
fi

# ---------- 3) push (ถ้าโดน reject ให้ rebase แล้วลองใหม่ 1 ครั้ง) ----------
if git push -q origin "$BRANCH" 2>>"$LOG"; then
    note "pushed ${AHEAD} commit(s) -> $(git rev-parse --short HEAD)"
    exit 0
fi

note "push rejected — trying rebase"
if git pull -q --rebase --autostash origin "$BRANCH" >>"$LOG" 2>&1; then
    if git push -q origin "$BRANCH" 2>>"$LOG"; then
        note "pushed after rebase -> $(git rev-parse --short HEAD)"
        exit 0
    fi
fi

git rebase --abort 2>/dev/null
echo "AUTOPUSH ERROR: push failed — ดู log ที่ $LOG"
note "PUSH FAILED (see log)"
exit 1
