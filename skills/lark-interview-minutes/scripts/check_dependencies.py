#!/usr/bin/env python3
import json
import os
import shutil
from pathlib import Path


def find_skill(root: Path, name: str) -> bool:
    return (root / name / "SKILL.md").is_file()


def main() -> None:
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    skills_root = codex_home / "skills"

    required_official = ["lark-shared", "lark-doc", "lark-whiteboard"]
    official_status = {name: find_skill(skills_root, name) for name in required_official}
    chart_status = find_skill(skills_root, "design-lark-chart")
    cli_path = shutil.which("lark-cli")
    if not cli_path:
        candidates = [
            Path.home() / "bin" / "lark-cli",
            Path.home() / ".local" / "bin" / "lark-cli",
            Path("/usr/local/bin/lark-cli"),
            Path("/opt/homebrew/bin/lark-cli"),
        ]
        cli_path = next((str(path) for path in candidates if path.is_file()), None)

    missing = []
    if not cli_path:
        missing.append("lark-cli")
    missing.extend(name for name, installed in official_status.items() if not installed)
    if not chart_status:
        missing.append("design-lark-chart")

    result = {
        "ready": not missing,
        "codex_home": str(codex_home),
        "skills_root": str(skills_root),
        "lark_cli": {"installed": bool(cli_path), "path": cli_path},
        "official_lark_skills": official_status,
        "design_lark_chart": chart_status,
        "missing": missing,
        "sources": {
            "official": "https://github.com/larksuite/cli",
            "chart": "https://github.com/fuxiaoai/lark-chart-skill",
        },
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
