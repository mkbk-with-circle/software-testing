#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件名：extract_bug_info.py
用途：提取 Defects4J 某个 bug 的关键信息，包括具体出错的源代码行，并写入 info.md
请在以下变量中配置 Defects4J 安装根路径：

具体出错的test源代码行## Error test Block
"""

# 用户请在此处设置 Defects4J 根路径，例如 "/home/user/defects4j"
DEFECTS4J_HOME = "/ymy/defects4j"

import argparse
import os
import shutil
import subprocess
import sys
import re

# 导入之前实现的函数模块，请确保 get_error_code.py 和本脚本在同一目录
from get_error_test_code import get_failing_line, find_source_file, extract_method_block

def run(cmd, **kwargs):
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True, **kwargs)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {cmd}\nstderr: {result.stderr}")
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description="Extract bug info from Defects4J project.")
    parser.add_argument('project', help='Defects4J project name, e.g. Lang')
    parser.add_argument('bug_id', help='Bug identifier, integer')
    parser.add_argument("if_delete",help="if you want to delete the workspace,choose 1",type=bool,default=False)
    args = parser.parse_args()

    PROJECT = args.project
    BUG_ID = args.bug_id
    VERSION = f"{BUG_ID}b"
    WORKSPACE = os.path.join(os.getcwd(), 'bug_info', f"{PROJECT}_{BUG_ID}")
    print("workspace",WORKSPACE)


    # 1. Prepare workspace
    print(f"==> Preparing workspace {WORKSPACE}")
    if os.path.exists(WORKSPACE):
        shutil.rmtree(WORKSPACE)
    os.makedirs(WORKSPACE)
    os.chdir(WORKSPACE)

    # 2. Checkout buggy version
    #print(f"==> Checking out {PROJECT} bug {BUG_ID} ({VERSION})...")
    run(f"defects4j checkout -p {PROJECT} -v {VERSION} -w .")

    # 2.5 Compile the project so tests are available on the classpath
    #print("==> Compiling project ...")
    run(f"defects4j compile -w .")

    INFO_FILE = '../my_info/info.md'
    print(f"==> Generating {INFO_FILE}")
    # … 以下就写 header、classes.modified、tests.trigger …

    # 5. Triggering Tests
    tests_output = run(f"defects4j export -p tests.trigger -w .")
    tests = [line.strip() for line in tests_output.splitlines() if line.strip()]


    # 8. 错误方法代码块
    # 使用 get_error_code_annotated 中的函数提取实际失败位置的代码块
    if tests:
        test_id = tests[0]
        try:
            java_file, line_no = get_failing_line('.', test_id)
            src_path = find_source_file('.', java_file)
            block = extract_method_block(src_path, line_no)
            with open(INFO_FILE, 'a', encoding='utf-8') as f:
                f.write('\n## Error Code Block\n')
                f.write('```java\n')
                f.write(block if block else '未能提取到代码块')
                f.write('\n```\n')
        except Exception as e:
            with open(INFO_FILE, 'a', encoding='utf-8') as f:
                f.write('\n## Error Code Block\n')
                f.write(f'解析失败: {e}\n')

    print(f"==> Done! See {os.path.join(os.getcwd(), INFO_FILE)}")
    
    if args.if_delete:
        shutil.rmtree(WORKSPACE)
        print(f"==> Deleted workspace {WORKSPACE}")


if __name__ == '__main__':
    main()
