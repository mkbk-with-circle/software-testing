import json
import subprocess
import os

BUG_LIST_FILE = "scripts/data/bug_id_and_branch.json"
CHECKOUT_SCRIPT = "scripts/checkout_bug.py"

# 读取所有 bugId
with open(BUG_LIST_FILE, "r", encoding="utf-8") as f:
    bug_list = json.load(f)

# 依次执行 checkout 脚本
for bug in bug_list:
    bug_id = bug.get("bugId")
    if not bug_id:
        continue
    print(f"\nIn {bug_id}...")
    cmd = f'python {CHECKOUT_SCRIPT} --bugId {bug_id}'
    result = subprocess.call(cmd, shell=True)
    if result != 0:
        print(f"{bug_id} failed\n")
    else:
        print(f"{bug_id} success\n")
