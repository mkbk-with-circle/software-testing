#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件名：get_all_patch.py
使用方法: python get_all_patch.py {project}
用途：对 Defects4J 某个项目的所有有效 Bug ID，依次调用
    python get_diff.py {project} {bug_id}
    python diff2json.py {project} {bug_id}
"""

import subprocess
import argparse
import sys
import time
def run_cmd(cmd):
    """运行 shell 命令，出错则打印并退出。"""
    print(f"Running: {cmd}")
    proc = subprocess.run(cmd, shell=True, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        print(f"Error executing command: {cmd}", file=sys.stderr)
        print(proc.stderr, file=sys.stderr)
        sys.exit(proc.returncode)
    return proc.stdout

def get_valid_bug_ids(project):
    """调用 `defects4j bids -p project`，返回按数值排序的 bug_id 列表（跳过 deprecated）。"""
    out = run_cmd(f"defects4j bids -p {project}")
    # bids 会逐行输出各个 ID，例如：
    # 1
    # 3
    # 4
    # ...
    ids = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            ids.append(int(line))
        except ValueError:
            # 如果有奇怪的输出，直接跳过
            pass
    return sorted(ids)

def main():
    parser = argparse.ArgumentParser(description="为 Defects4J 项目批量生成补丁")
    parser.add_argument("project", help="项目名，比如 Lang")
    args = parser.parse_args()

    project = args.project
    # 1) 拿到所有有效 bug IDs
    print(f"==> 获取 {project} 所有非废弃的 Bug ID 列表 …")
    bug_ids = get_valid_bug_ids(project)
    print(f"找到了 {len(bug_ids)} 个 Bug ID: {bug_ids}")

    bug_ids = bug_ids[1:]
    # 2) 依次调用脚本
    for bug_id in bug_ids:
        print(f"\n==> 处理 {project}#{bug_id} …")
        run_cmd(f"python3 get_diff.py {project} {bug_id}")
        run_cmd(f"python3 diff2json.py {project} {bug_id}")
        # 等待 0.1 秒
        time.sleep(0.1)

    print("\n==> 全部处理完成！")

if __name__ == "__main__":
    main()
