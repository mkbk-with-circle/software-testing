#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件名：extract_and_generate_bug_info.py
使用方法：python all_in_one.py {project} {bug_id}
用途：提取 Defects4J 某个 bug 的关键信息，包括具体出错的源代码行，并写入 info.md，同时执行 Defects4J 相关操作。
"""

# 用户请在此处设置 Defects4J 根路径，例如 "/home/user/defects4j"
DEFECTS4J_HOME = "/ymy/defects4j"

import argparse
import os
import shutil
import subprocess
import sys
import re
from get_error_test_code import get_failing_line, find_source_file, extract_method_block


def run(cmd, **kwargs):
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True, **kwargs)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {cmd}\nstderr: {result.stderr}")
    return result.stdout


# 读取 bug 详情并写入到 markdown 文件
def extract_bug_details(txt_file_path, output_md_path):
    # Ensure the directory exists, if not, create it
    output_dir = os.path.dirname(output_md_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(txt_file_path, 'r') as file:
        content = file.read()

    # 删除 "Example" 部分
    content = re.sub(r"<Example start>.*?<Example end>", "", content, flags=re.DOTALL)

    # 删除最后一句话
    content = re.sub(r"Please provide an analysis of the problem and the expected behaviour of the correct fix, and the correct version of the function in the form of Java Markdown code block\.", "", content)

    # 提取各部分
    buggy_code_match = re.search(r"(?<=The following code contains a bug:)(.*?)(?=The code fails on this test:)", content, re.DOTALL)
    failed_test_match = re.search(r"(?<=The code fails on this test:)(.*?)(?=on this test line:)", content, re.DOTALL)
    test_line_match = re.search(r"(?<=on this test line:)(.*?)(?=with the following test error:)", content, re.DOTALL)
    error_match = re.search(r"(?<=with the following test error:)(.*)", content, re.DOTALL)

    # 将提取的内容写入 markdown 文件
    with open(output_md_path, 'w', encoding='utf-8') as md_file:
        if buggy_code_match:
            md_file.write("## Buggy code\n")
            md_file.write(f"```java\n{buggy_code_match.group(0).strip()}\n```\n\n")

        if failed_test_match:
            md_file.write("## Failed test\n")
            md_file.write(f"{failed_test_match.group(0).strip()}\n\n")

        if test_line_match:
            md_file.write("## Test line\n")
            md_file.write(f"{test_line_match.group(0).strip()}\n\n")

        if error_match:
            md_file.write("## Error\n")
            md_file.write(f"{error_match.group(0).strip()}\n")


def main():
    # 定义 argparse 参数
    parser = argparse.ArgumentParser(description="Extract bug info from Defects4J project and generate prompt.")
    parser.add_argument('project', help='Defects4J project name, e.g. Lang')
    parser.add_argument('bug_id', help='Bug identifier, integer')
    parser.add_argument("if_delete", help="If you want to delete the workspace, choose 1", type=bool, default=False)
    args = parser.parse_args()

    PROJECT = args.project
    BUG_ID = args.bug_id
    VERSION = f"{BUG_ID}b"
    WORKSPACE = os.path.join(os.getcwd(), 'bug_info', f"{PROJECT}_{BUG_ID}")
    print("workspace", WORKSPACE)

    # 1. 准备工作区
    print(f"==> Preparing workspace {WORKSPACE}")
    if os.path.exists(WORKSPACE):
        shutil.rmtree(WORKSPACE)
    os.makedirs(WORKSPACE)
    os.chdir(WORKSPACE)

    # 2. 检出 buggy 版本
    run(f"defects4j checkout -p {PROJECT} -v {VERSION} -w .")

    # 2.5 编译项目
    run(f"defects4j compile -w .")

    INFO_FILE = f'../{PROJECT}_{BUG_ID}_prompt.md'
    print(f"==> Generating {INFO_FILE}")

    # 如果INFO_FILE存在，则直接结束
    if os.path.exists(INFO_FILE):
        print(f"==> {INFO_FILE} already exists, skipping")
        return

    # 3. 提取 Bug 相关信息并写入 markdown 文件
    txt_file_path = f'/ymy/an-implementation-of-chatrepair/initial/{PROJECT}/{BUG_ID}.txt'  # 动态生成路径
    extract_bug_details(txt_file_path, INFO_FILE)

    # 4. 获取触发测试的相关信息
    tests_output = run(f"defects4j export -p tests.trigger -w .")
    tests = [line.strip() for line in tests_output.splitlines() if line.strip()]

    # 5. 错误方法代码块
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

    # 6. 可选：删除工作区
    if args.if_delete:
        shutil.rmtree(WORKSPACE)
        print(f"==> Deleted workspace {WORKSPACE}")


if __name__ == '__main__':
    main()
