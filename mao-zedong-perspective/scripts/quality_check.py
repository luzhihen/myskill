#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

def check_skill(skill_path):
    print("=" * 60)
    print("毛泽东Skill质量检查")
    print("=" * 60)

    checks = []

    # 检查SKILL.md存在
    skill_file = os.path.join(skill_path, "SKILL.md")
    if os.path.exists(skill_file):
        checks.append(("SKILL.md存在", "PASS"))
    else:
        checks.append(("SKILL.md存在", "FAIL"))

    # 检查调研文件
    research_dir = os.path.join(skill_path, "references", "research")
    if os.path.exists(research_dir):
        checks.append(("调研目录存在", "PASS"))
        files = ["01-writings.md", "02-conversations.md", "03-expression-dna.md",
                 "04-external-views.md", "05-decisions.md", "06-timeline.md"]
        for f in files:
            if os.path.exists(os.path.join(research_dir, f)):
                checks.append((f"调研文件{f}存在", "PASS"))
            else:
                checks.append((f"调研文件{f}存在", "FAIL"))
    else:
        checks.append(("调研目录存在", "FAIL"))

    # 检查心智模型数量
    if os.path.exists(skill_file):
        with open(skill_file, 'r', encoding='utf-8') as f:
            content = f.read()
            model_count = content.count("### ") - 1
            if model_count >= 3:
                checks.append((f"心智模型数量({model_count})", "PASS"))
            else:
                checks.append((f"心智模型数量({model_count})", "WARN"))

    # 检查诚实边界
    if "诚实边界" in content:
        checks.append(("诚实边界存在", "PASS"))
    else:
        checks.append(("诚实边界存在", "WARN"))

    # 检查表达DNA
    if "表达DNA" in content:
        checks.append(("表达DNA存在", "PASS"))
    else:
        checks.append(("表达DNA存在", "FAIL"))

    # 输出结果
    print("\n检查结果：")
    print("-" * 60)
    for check, status in checks:
        print(f"{check:35s} {status}")

    print("\n" + "=" * 60)
    pass_count = sum(1 for _, s in checks if s == "PASS")
    warn_count = sum(1 for _, s in checks if s == "WARN")
    fail_count = sum(1 for _, s in checks if s == "FAIL")
    print(f"总计：{pass_count} PASS, {warn_count} WARN, {fail_count} FAIL")

    if fail_count == 0:
        print("\n✓ Skill质量检查通过！")
        return 0
    else:
        print("\n✗ Skill存在问题，请检查修复")
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法：python quality_check.py <skill_path>")
        sys.exit(1)

    skill_path = sys.argv[1]
    sys.exit(check_skill(skill_path))
