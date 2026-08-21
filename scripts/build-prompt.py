#!/usr/bin/env python3
"""从 SKILL.md + references/ 生成元宝/豆包可粘贴的提示词版。"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "prompt" / "yuer-triage.txt"


def build() -> str:
    parts: list[str] = []
    skill = ROOT / "SKILL.md"
    parts.append(skill.read_text(encoding="utf-8"))
    for ref in sorted((ROOT / "references").glob("*.md")):
        parts.append(f"\n\n---\n\n# 知识文件：{ref.name}\n\n")
        parts.append(ref.read_text(encoding="utf-8"))
    return "\n".join(parts)


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    content = build()
    OUT.write_text(content, encoding="utf-8")
    print(f"已生成: {OUT} ({len(content)} 字符)")


if __name__ == "__main__":
    main()
