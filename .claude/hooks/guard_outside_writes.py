"""PreToolUse hook: zápis mimo repozitář vždy vyžaduje potvrzení ("ask").

- Write / Edit / NotebookEdit: kontroluje cílovou cestu.
- Bash / PowerShell: heuristika - pokud příkaz obsahuje zapisující operaci
  a zároveň odkazuje na cestu mimo repo (nebo běží v cwd mimo repo), vrátí "ask".
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

WRITE_PATTERNS = re.compile(
    r"""(
        (?<![<>\d&])>>?(?!&)                       # přesměrování > >>
      | \b(mv|cp|rm|rmdir|mkdir|touch|tee|ln|install|rsync|unzip|tar|truncate|dd|chmod|chown)\b
      | \bsed\s+(-\w*\s+)*-i
      | \bgit\s+(-C\s+\S+\s+)?(clone|init|worktree)\b
      | \b(Move-Item|Copy-Item|Remove-Item|New-Item|Set-Content|Add-Content|Out-File|
           Rename-Item|Clear-Content|Expand-Archive|Compress-Archive|mi|cpi|ri|ni|del|erase|move|copy|md|rd)\b
      | \bpython[\d.]*\b | \bnode\b | \bpowershell\b | \bpwsh\b | \bcmd(\.exe)?\b
    )""",
    re.IGNORECASE | re.VERBOSE,
)

PATH_TOKEN = re.compile(
    r"""(?<![^\s"'=(,])(                     # token musí začínat na hranici slova

        [A-Za-z]:[\\/][^\s"'|;&<>`]*          # C:\... nebo C:/...
      | /[a-zA-Z]/[^\s"'|;&<>`]*              # /c/... (Git Bash)
      | ~[\\/]?[^\s"'|;&<>`]*                 # ~/...
      | \$HOME[^\s"'|;&<>`]* | \$env:\w+[^\s"'|;&<>`]*
      | (?:\.\.[\\/]?)+[^\s"'|;&<>`]*         # ../...
      | /(?:tmp|etc|usr|var|home|opt|mnt)\b[^\s"'|;&<>`]*
    )""",
    re.VERBOSE,
)


def normalize(raw: str, cwd: Path) -> Path | None:
    p = raw.strip().strip("'\"")
    m = re.match(r"^/([a-zA-Z])(/.*)?$", p)
    if m and not p.startswith(("/tmp", "/etc", "/usr", "/var", "/home", "/opt", "/mnt")):
        p = f"{m.group(1)}:{m.group(2) or '/'}"
    if p.startswith("~") or p.startswith("$HOME"):
        p = str(Path.home()) + p.split("~", 1)[-1] if p.startswith("~") else str(Path.home()) + p[5:]
    if p.lower().startswith("$env:"):
        return None  # nelze spolehlivě rozvinout -> volající bere jako "mimo"
    try:
        path = Path(p)
        if not path.is_absolute():
            path = cwd / path
        return Path(os.path.normpath(str(path)))
    except Exception:
        return None


def inside_repo(path: Path | None) -> bool:
    if path is None:
        return False
    try:
        rp = os.path.normcase(os.path.realpath(path))
        rr = os.path.normcase(os.path.realpath(REPO))
        return rp == rr or rp.startswith(rr + os.sep)
    except Exception:
        return False


def ask(reason: str) -> None:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        ask("Hook nedokázal přečíst vstup - raději se ptám.")
    tool = data.get("tool_name", "")
    ti = data.get("tool_input", {}) or {}
    cwd = Path(data.get("cwd") or os.getcwd())

    if tool in ("Write", "Edit", "NotebookEdit", "MultiEdit"):
        target = ti.get("file_path") or ti.get("notebook_path") or ""
        path = normalize(target, cwd)
        if not inside_repo(path):
            ask(f"Zápis mimo repozitář: {target}")
        return

    if tool in ("Bash", "PowerShell"):
        cmd = ti.get("command", "") or ""
        if not WRITE_PATTERNS.search(cmd):
            return
        if not inside_repo(cwd):
            ask(f"Zapisující příkaz běží mimo repozitář (cwd: {cwd})")
        for m in PATH_TOKEN.finditer(cmd):
            tok = m.group(0)
            p = normalize(tok, cwd)
            if not inside_repo(p):
                ask(f"Příkaz může zapisovat mimo repozitář: {tok}")
        # cd mimo repo a následný zápis
        for m in re.finditer(r"\b(?:cd|Set-Location|pushd)\s+(\S+)", cmd, re.IGNORECASE):
            if not inside_repo(normalize(m.group(1), cwd)):
                ask(f"Příkaz mění adresář mimo repozitář: {m.group(1)}")


if __name__ == "__main__":
    main()
