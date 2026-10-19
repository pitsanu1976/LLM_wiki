#!/usr/bin/env python3
"""
check-vault.py — ตรวจสุขภาพของ vault (stdlib ล้วน ไม่ต้องติดตั้งอะไร)

ใช้:
    python3 "90_System_Prompts/check-vault.py"
    python3 check-vault.py --vault "/path/to/vault"
    python3 check-vault.py --quiet        # เฉพาะสรุป

ตรวจ:
  * YAML frontmatter ครบ 5 ฟิลด์บังคับ + type/status/date ถูกต้อง
  * broken wikilink (ข้าม link ใน code block/inline code ตามที่ Obsidian ทำ)
  * orphan note (ไม่มี inbound link)
  * link graph + สถิติ

Exit code: 0 = สะอาด, 1 = พบปัญหา
"""
from __future__ import annotations

import argparse
import collections
import os
import re
import sys

REQUIRED = ["title", "type", "status", "created", "updated"]
VALID_TYPES = {"concept", "howto", "reference", "moc", "project",
               "journal", "decision", "source", "system"}
VALID_STATUS = {"inbox", "active", "draft", "archived"}
ROOT_NOTE = "main-hub"

FENCE = re.compile(r"```.*?```", re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")
WIKILINK = re.compile(r"\[\[([^\[\]]+?)\]\]")
LINK_TARGET = re.compile(r"^([^#|]+?)(?:#[^|]*)?(?:\|.*)?$")


def resolve_vault(cli_path: str | None) -> str:
    """CLI flag > OBSIDIAN_VAULT_PATH > สองระดับเหนือตัว script นี้"""
    if cli_path:
        return os.path.abspath(os.path.expanduser(cli_path))
    env = os.environ.get("OBSIDIAN_VAULT_PATH")
    if env:
        return os.path.abspath(os.path.expanduser(env.strip('"').strip("'")))
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(here)  # <vault>/90_System_Prompts/ -> <vault>


def strip_code(text: str) -> str:
    """Obsidian ไม่ resolve wikilink ใน code — checker ก็ต้องไม่นับ"""
    return INLINE_CODE.sub("", FENCE.sub("", text))


def parse_frontmatter(text: str) -> tuple[dict, str | None]:
    if not text.startswith("---"):
        return {}, "no frontmatter"
    end = text.find("\n---", 3)
    if end == -1:
        return {}, "unterminated frontmatter"
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return fm, None


def scan(vault: str) -> dict:
    notes: dict[str, str] = {}
    for root, dirs, files in os.walk(vault):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            if f.endswith(".md"):
                notes[os.path.basename(f)[:-3]] = os.path.join(root, f)

    lower = {k.lower(): k for k in notes}
    problems: dict[str, list[str]] = collections.defaultdict(list)
    inbound: collections.Counter = collections.Counter()
    outbound: dict[str, list[str]] = collections.defaultdict(list)

    for name, path in sorted(notes.items()):
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        body = strip_code(text)

        fm, err = parse_frontmatter(text)
        if err:
            problems[err].append(name)
        for key in REQUIRED:
            if key not in fm or fm[key] in ("", "~"):
                problems[f"missing field '{key}'"].append(name)
        if fm.get("type") and fm["type"] not in VALID_TYPES:
            problems[f"bad type '{fm['type']}'"].append(name)
        if fm.get("status") and fm["status"] not in VALID_STATUS:
            problems[f"bad status '{fm['status']}'"].append(name)
        for key in ("created", "updated"):
            val = fm.get(key, "")
            if val and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", val):
                problems[f"bad date {key}='{val}'"].append(name)

        for raw in WIKILINK.findall(body):
            m = LINK_TARGET.match(raw.strip())
            if not m:
                problems["unparseable link"].append(f"{name}: [[{raw.strip()}]]")
                continue
            target = m.group(1).strip().rstrip("\\").strip()  # table escape \|
            if not target:
                continue
            hit = lower.get(target.lower())
            if hit:
                inbound[hit] += 1
                outbound[name].append(hit)
            else:
                problems["broken link"].append(f"{name}: [[{target}]]")

    return {"notes": notes, "problems": problems,
            "inbound": inbound, "outbound": outbound}


def report(vault: str, data: dict, quiet: bool = False) -> int:
    notes, problems = data["notes"], data["problems"]
    inbound, outbound = data["inbound"], data["outbound"]
    orphans = [n for n in notes if inbound[n] == 0 and n != ROOT_NOTE]

    if not quiet:
        print("=" * 72)
        print(f"VAULT: {vault}")
        print(f"NOTES: {len(notes)}")
        print("=" * 72)

        print("\n--- FILES ---")
        for name, path in sorted(notes.items()):
            print(f"  {name:<26} {os.path.relpath(path, vault)}")

        print("\n--- LINK GRAPH ---")
        for name in sorted(notes):
            flag = "   <-- ORPHAN" if name in orphans else ""
            print(f"  {name:<26} in={inbound[name]:<3} "
                  f"out={len(set(outbound[name]))}{flag}")

        if problems:
            print("\n--- PROBLEMS ---")
            for kind, items in sorted(problems.items()):
                print(f"  [{kind}] {len(items)}")
                for item in items:
                    print(f"      - {item}")
        else:
            print("\n--- PROBLEMS ---\n  none")

    print("\n--- TOTALS ---")
    print(f"  files          : {len(notes)}")
    print(f"  links resolved : {sum(inbound.values())}")
    print(f"  broken links   : {len(problems.get('broken link', []))}")
    print(f"  orphans        : {len(orphans)}")
    print(f"  other problems : {sum(len(v) for k, v in problems.items() if k != 'broken link')}")
    status = "CLEAN" if not problems and not orphans else "NEEDS ATTENTION"
    print(f"  status         : {status}")
    return 0 if (not problems and not orphans) else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Vault health check")
    ap.add_argument("--vault", help="path to vault (default: OBSIDIAN_VAULT_PATH or script's parent)")
    ap.add_argument("--quiet", action="store_true", help="summary only")
    args = ap.parse_args(argv)

    vault = resolve_vault(args.vault)
    if not os.path.isdir(vault):
        print(f"ERROR: vault not found: {vault}", file=sys.stderr)
        return 2
    return report(vault, scan(vault), quiet=args.quiet)


if __name__ == "__main__":
    sys.exit(main())
