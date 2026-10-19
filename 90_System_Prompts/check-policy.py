#!/usr/bin/env python3
"""
check-policy.py — ตรวจว่าการเขียนใน vault อยู่ในขอบเขตสิทธิ์ของ agent

อ้างอิง: 90_System_Prompts/agent-access-policy.md

ใช้:
    python3 check-policy.py                 # ตรวจสถานะปัจจุบัน (static)
    python3 check-policy.py --git 30        # ตรวจ 30 commit ล่าสุด
    python3 check-policy.py --quiet

Exit: 0 = ผ่าน, 1 = พบการละเมิด, 2 = หา vault ไม่ได้
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

# ── นโยบาย ────────────────────────────────────────────────────────────────
# โฟลเดอร์ → agent เจ้าของ (None = ใช้ร่วม ไม่ต้องตรวจ agent field)
SCOPES = {
    "20_Knowledge/24_News_Archive": "news",
    "20_Knowledge/25_Tech_Analysis": "tech",
    "20_Knowledge/26_Financial_Data": "finance",
    "50_Watchlist": "leader",
    "10_MOC/stocks": "leader",
}
HUMAN_ONLY = ("90_System_Prompts",)
TICKER_DIRS = ("20_Knowledge/24_News_Archive",
               "20_Knowledge/25_Tech_Analysis",
               "20_Knowledge/26_Financial_Data")
HUB_DIR = "10_MOC/stocks"
HUB_BLOCKS = ("news", "tech", "finance", "leader")

ALLOWED_PREFIX = {
    "news": ["00_Inbox/", "20_Knowledge/24_News_Archive/", "10_MOC/stocks/"],
    "tech": ["00_Inbox/", "20_Knowledge/25_Tech_Analysis/", "10_MOC/stocks/"],
    "finance": ["00_Inbox/", "20_Knowledge/26_Financial_Data/", "10_MOC/stocks/"],
    "leader": ["00_Inbox/", "50_Watchlist/", "10_MOC/stocks/", "40_Journals/"],
    "human": None,  # ทุกที่
}

BLOCK_RE = re.compile(r"<!--\s*agent:(\w+):begin\s*-->(.*?)<!--\s*agent:\1:end\s*-->", re.S)
MARKER_RE = re.compile(r"<!--\s*agent:(\w+):(begin|end)\s*-->")
FM_KEY = re.compile(r"^([A-Za-z_][\w-]*):\s*(.*)$")


def resolve_vault(cli: str | None) -> str:
    if cli:
        return os.path.abspath(os.path.expanduser(cli))
    env = os.environ.get("OBSIDIAN_VAULT_PATH")
    if env:
        return os.path.abspath(os.path.expanduser(env.strip('"').strip("'")))
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[3:end].splitlines():
        m = FM_KEY.match(line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return fm


def blocks(text: str) -> dict[str, str]:
    return {m.group(1): m.group(2).strip() for m in BLOCK_RE.finditer(text)}


def git(vault: str, *args: str) -> str:
    return subprocess.run(["git", "-C", vault, *args],
                          capture_output=True, text=True).stdout


# ── static checks ─────────────────────────────────────────────────────────
def static_check(vault: str) -> list[tuple[str, str, str]]:
    """คืน list ของ (severity, path, message)"""
    out: list[tuple[str, str, str]] = []

    for root, dirs, files in os.walk(vault):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for name in files:
            if not name.endswith(".md"):
                continue
            path = os.path.join(root, name)
            rel = os.path.relpath(path, vault).replace(os.sep, "/")

            owner = None
            for prefix, who in SCOPES.items():
                if rel.startswith(prefix + "/"):
                    owner = who
                    break

            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            fm = frontmatter(text)

            # 1) agent field ต้องตรงกับเจ้าของโฟลเดอร์
            declared = fm.get("agent", "")
            if owner and declared != owner:
                out.append(("ERROR", rel,
                            f"ต้องมี agent: {owner} (พบ '{declared or 'ไม่มี'}')"))

            # 1b) 90_System_Prompts เป็นของมนุษย์ — agent ห้ามเป็นเจ้าของ
            if any(rel.startswith(h + "/") for h in HUMAN_ONLY):
                if declared not in ("", "human"):
                    out.append(("ERROR", rel,
                                f"90_System_Prompts เป็นของมนุษย์ (พบ agent: {declared})"))

            # 2) ไฟล์ข่าว/เทคนิค/งบ ต้องมี ticker + ลิงก์ hub
            if any(rel.startswith(d + "/") for d in TICKER_DIRS):
                ticker = fm.get("ticker", "")
                if not ticker:
                    out.append(("ERROR", rel, "ขาด ticker: ใน frontmatter"))
                elif f"[[{ticker}]]" not in text:
                    out.append(("ERROR", rel, f"ต้องมีลิงก์ [[{ticker}]]"))

            # 3) hub ต้องมี marker ครบและไม่ซ้อน
            if rel.startswith(HUB_DIR + "/") and not name.startswith("_"):
                markers = MARKER_RE.findall(text)
                if not markers:
                    out.append(("ERROR", rel, "ไม่พบ marker block ใด ๆ"))
                else:
                    stack: list[str] = []
                    for agent, kind in markers:
                        if kind == "begin":
                            if stack:
                                out.append(("ERROR", rel,
                                            f"block ซ้อนกัน: {stack[-1]} → {agent}"))
                            stack.append(agent)
                        else:
                            if not stack or stack[-1] != agent:
                                out.append(("ERROR", rel,
                                            f"end ไม่จับคู่กับ begin: {agent}"))
                            else:
                                stack.pop()
                    if stack:
                        out.append(("ERROR", rel, f"block ไม่ปิด: {stack}"))
                    found = {a for a, k in markers if k == "begin"}
                    missing = [b for b in HUB_BLOCKS if b not in found]
                    if missing:
                        out.append(("WARN", rel,
                                    f"ขาด block: {', '.join(missing)}"))
    return out


# ── git checks ────────────────────────────────────────────────────────────
def commit_agent(subject: str) -> str | None:
    m = re.match(r"^\[(\w+)\]", subject.strip())
    return m.group(1) if m else None


def git_check(vault: str, n: int) -> list[tuple[str, str, str]]:
    out: list[tuple[str, str, str]] = []
    log = git(vault, "log", f"-{n}", "--format=%H\x1f%s")
    for line in log.splitlines():
        if "\x1f" not in line:
            continue
        sha, subject = line.split("\x1f", 1)
        agent = commit_agent(subject)
        if not agent:
            continue                      # ไม่มี prefix = มนุษย์
        if agent not in ALLOWED_PREFIX:
            out.append(("WARN", sha[:7], f"ไม่รู้จัก agent '{agent}'"))
            continue

        changed = [p for p in git(vault, "show", "--name-only",
                                  "--format=", sha).splitlines() if p.strip()]
        allowed = ALLOWED_PREFIX[agent]
        if allowed is not None:
            for path in changed:
                if not any(path.startswith(a) for a in allowed):
                    out.append(("ERROR", f"{sha[:7]} {path}",
                                f"'{agent}' ไม่มีสิทธิ์เขียน path นี้"))

        # hub: ตรวจระดับ block
        for path in changed:
            if not path.startswith(HUB_DIR + "/") or not path.endswith(".md"):
                continue
            old = git(vault, "show", f"{sha}^:{path}")
            new = git(vault, "show", f"{sha}:{path}")
            ob, nb = blocks(old), blocks(new)
            for owner, content in nb.items():
                if owner != agent and content != ob.get(owner, ""):
                    out.append(("ERROR", f"{sha[:7]} {path}",
                                f"'{agent}' แก้ block ของ '{owner}'"))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Agent write-scope checker")
    ap.add_argument("--vault")
    ap.add_argument("--git", type=int, metavar="N",
                    help="ตรวจ N commit ล่าสุด (ต้องมี prefix [agent])")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    vault = resolve_vault(args.vault)
    if not os.path.isdir(vault):
        print(f"ERROR: vault not found: {vault}", file=sys.stderr)
        return 2

    problems = static_check(vault)
    if args.git:
        problems += git_check(vault, args.git)

    errors = [p for p in problems if p[0] == "ERROR"]
    warns = [p for p in problems if p[0] == "WARN"]

    if not args.quiet or problems:
        print(f"vault: {vault}")
        if problems:
            for sev, path, msg in sorted(problems):
                print(f"  [{sev}] {path}: {msg}")
        else:
            print("  ไม่พบการละเมิด ✓")

    print(f"\n  errors: {len(errors)}   warnings: {len(warns)}")
    print(f"  status: {'PASS' if not errors else 'FAIL'}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
