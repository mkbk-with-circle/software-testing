import os
import sys
import subprocess
import json
import argparse
import shutil

from config import *

parser = argparse.ArgumentParser(description='Script to check out one bug from Bears')
parser.add_argument('--bugId', help='The ID of the bug to be checked out', required=True, metavar='')
args = parser.parse_args()

BUG_ID = args.bugId
WORKSPACE = ".\workspace"

os.makedirs(WORKSPACE, exist_ok=True)

BUG_FOLDER_PATH = os.path.join(WORKSPACE, BUG_ID)

print("Checking out the bug %s..." % BUG_ID)

# 读取 bugs.json 文件
bugs = None
try:
    with open(os.path.join(BEARS_PATH, BEARS_BUGS), 'r', encoding='utf-8') as f:
        bugs = json.load(f)
except Exception as e:
    print("Error loading bugs.json:", e)
    sys.exit()

# 找到该 bug 对应的分支名
BUG_BRANCH_NAME = None
if bugs:
    for bug in bugs:
        if bug['bugId'].lower() == BUG_ID.lower():
            BUG_BRANCH_NAME = bug['bugBranch']
            break

if BUG_BRANCH_NAME is None:
    print("There is no bug with the ID %s" % BUG_ID)
    sys.exit()

print("Checking out branch:", BUG_BRANCH_NAME)

# 创建 bug 文件夹
os.makedirs(BUG_FOLDER_PATH, exist_ok=True)

# 切换到该分支并找出 buggy commit
subprocess.call(f'cd "{BEARS_PATH}" && git reset . && git checkout -- . && git clean -f', shell=True)
subprocess.call(f'cd "{BEARS_PATH}" && git checkout {BUG_BRANCH_NAME}', shell=True)

# 复制 bears.json 报告
export_meta = os.path.join(BEARS_PATH, 'export_bears', BUG_ID, 'meta')
os.makedirs(export_meta, exist_ok=True)
shutil.copy2("bears.json", export_meta)

# 查找含有"Changes in the tests"的 commit
cmd = f'cd "{BEARS_PATH}" && git log --format=format:%H --grep="Changes in the tests"'
try:
    BUGGY_COMMIT = subprocess.check_output(cmd, shell=True).decode("utf-8").splitlines()[0]
    print("Buggy commit:", BUGGY_COMMIT)
except Exception as e:
    print("Failed to get buggy commit:", e)
    sys.exit()

# 生成 diff 位置信息并保存到文件
diff_output_cmd = f'cd "{BEARS_PATH}" && git diff -U0 {BUGGY_COMMIT} HEAD -- "*.java"'
diff_output = subprocess.check_output(diff_output_cmd, shell=True).decode("utf-8")

# 提取 hunk 信息（以 @@ 开头的行）
hunk_lines = [line for line in diff_output.splitlines() if line.startswith('@@')]

# 组织输出文件路径
diff_position = os.path.join(BEARS_PATH, 'diff_position', BUG_ID)
os.makedirs(diff_position, exist_ok=True)
diff_file_path = os.path.join(diff_position, 'diff_hunks.txt')

# 写入文件
with open(diff_file_path, 'w', encoding='utf-8') as f:
    for line in hunk_lines:
        f.write(line + '\n')

# 复制代码到 BUG_FOLDER_PATH
diff_cmd = f'cd "{BEARS_PATH}" && git diff --name-only {BUGGY_COMMIT} HEAD -- "*.java"'
changed = subprocess.check_output(diff_cmd, shell=True).decode("utf-8").splitlines()

# 切换到 buggy commit
subprocess.call(f'cd "{BEARS_PATH}" && git checkout {BUGGY_COMMIT}', shell=True)

for rel_path in changed:
    # 跳过 workspace 目录自身
    if rel_path.startswith(os.path.basename(WORKSPACE) + os.sep):
        continue

    src = os.path.join(BEARS_PATH, rel_path)
    dst = os.path.join(BUG_FOLDER_PATH, rel_path)

    # 确保目标目录存在
    os.makedirs(os.path.dirname(dst), exist_ok=True)

    if os.path.isdir(src):
        # 若变更的是目录，复制整个目录
        shutil.copytree(src, dst, dirs_exist_ok=True)
    elif os.path.isfile(src):
        # 若变更的是文件，复制单个文件
        shutil.copy2(src, dst)

# 恢复主分支
subprocess.call(f'cd "{BEARS_PATH}" && git reset . && git checkout -- . && git clean -f && git checkout master', shell=True)

print(f"✔️ Done: Bug {BUG_ID} checked out to {BUG_FOLDER_PATH}")
