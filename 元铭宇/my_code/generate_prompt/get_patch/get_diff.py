#!/usr/bin/env python3
import subprocess
import sys
import argparse
import os
# 这里可以设置你需要的变量

buggy_path = "/ymy/test/buggy"      # buggy 版本存放路径
patch_path = "/ymy/test/patch"      # fixed 版本存放路径
diff_path = f"/ymy/patch.diff"  # diff 文件输出路径

def run_command(command):
    """运行命令，并检测错误返回码"""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error executing command: {command}")
        sys.exit(1)

def main():
    parser =  argparse.ArgumentParser(description="get all patch")
    parser.add_argument('project', help='Defects4J project name, e.g. Lang')
    parser.add_argument('bug_id', help='Bug identifier, integer')
    args = parser.parse_args()
    project = args.project
    bug_id = args.bug_id

    output_file = f"/ymy/an-implementation-of-chatrepair/patches/{project}/{bug_id}.json"
    # 如果output_file存在，则直接结束
    #if os.path.exists(output_file):
    #    print(f"==> {output_file} already exists, skipping")
    #    return

    # 1. Checkout buggy 版本
    cmd_buggy = f"defects4j checkout -p {project} -v {bug_id}b -w {buggy_path}"
    run_command(cmd_buggy)

    # 2. Checkout fixed 版本
    cmd_patch = f"defects4j checkout -p {project} -v {bug_id}f -w {patch_path}"
    run_command(cmd_patch)
    

    # 3. 生成 diff 文件，比较 buggy 和 fixed 版本中的 src 目录
    diff_command = "diff -ruN /ymy/test/buggy/src /ymy/test/patch/src "
    try:
        result = subprocess.run(diff_command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        with open("/ymy/patch.diff", "w", encoding="utf-8") as f:
            f.write(result.stdout)
    except Exception as e:
        print(f"Error executing command: {e}")

    # 4. 删除 对应的文件夹/ymy/test/buggy/src和/ymy/test/patch/src 
    cmd_delete = f"rm -rf {buggy_path}/src"
    run_command(cmd_delete)
    cmd_delete = f"rm -rf {patch_path}/src"
    run_command(cmd_delete)

    print(f"Diff generated successfully at {diff_path}")

if __name__ == "__main__":
    main()


