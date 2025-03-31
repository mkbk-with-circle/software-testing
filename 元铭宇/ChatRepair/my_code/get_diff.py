#!/usr/bin/env python3
import subprocess
import sys

# 这里可以设置你需要的变量
project = "Lang"            # 项目名称，例如 "Lang"
num = "1"                   # 缺陷编号，例如 "1"
buggy_path = "/ymy/test/buggy"      # buggy 版本存放路径
patch_path = "/ymy/test/patch"      # fixed 版本存放路径
diff_path = "/ymy/patch.diff"  # diff 文件输出路径

def run_command(command):
    """运行命令，并检测错误返回码"""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error executing command: {command}")
        sys.exit(1)

def main():
    # 1. Checkout buggy 版本
    cmd_buggy = f"defects4j checkout -p {project} -v {num}b -w {buggy_path}"
    run_command(cmd_buggy)

    # 2. Checkout fixed 版本
    cmd_patch = f"defects4j checkout -p {project} -v {num}f -w {patch_path}"
    run_command(cmd_patch)

    # 3. 生成 diff 文件，比较 buggy 和 fixed 版本中的 src 目录
    cmd_diff = f"diff -ruN {buggy_path}/src {patch_path}/src > {diff_path}"
    run_command(cmd_diff)

    print(f"Diff generated successfully at {diff_path}")

if __name__ == "__main__":
    main()
