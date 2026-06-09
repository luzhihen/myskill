#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def merge_research(skill_path):
    research_dir = os.path.join(skill_path, "references", "research")
    output_file = os.path.join(skill_path, "references", "research_summary.md")
    
    if not os.path.exists(research_dir):
        print(f"错误：调研目录不存在: {research_dir}")
        return
    
    files = sorted(os.listdir(research_dir))
    md_files = [f for f in files if f.endswith('.md')]
    
    summary = "# 苏东坡Skill调研汇总\n\n"
    summary += "## 调研文件列表\n\n"
    summary += "| 序号 | 文件 |\n"
    summary += "|------|------|\n"
    
    for i, f in enumerate(md_files, 1):
        summary += f"| {i} | {f} |\n"
    
    summary += "\n## 各文件内容摘要\n\n"
    
    for f in md_files:
        filepath = os.path.join(research_dir, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split('\n')
            # 获取前5行作为摘要
            summary += f"### {f}\n\n"
            summary += '\n'.join(lines[:10]) + "\n\n"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    print(f"调研汇总已生成: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法：python merge_research.py <skill_path>")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    merge_research(skill_path)
