import subprocess
import sys
import os

def run_cmd(command):
    """执行命令并返回输出"""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    # 如果命令执行失败，则打印错误信息并且继续执行
    if result.returncode != 0:
        print(f"Error executing command: {command}")
        print(f"stderr: {result.stderr}")
    return result.stdout

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

def process_bug_ids(project):
    """根据 bug IDs 运行 `python3 all_in_one.py` 命令"""
    bug_ids = get_valid_bug_ids(project)
    for bug_id in bug_ids:
        INFO_FILE = f'bug_info/{project}_{bug_id}_prompt.md'
        print("INFO_FILE",INFO_FILE)
        if os.path.exists(INFO_FILE):
            print(f"==> {INFO_FILE} already exists, skipping")
            continue
        # 假设 Lang 是项目名或某个已知的常量，这里您可以根据实际情况修改
        command = f"python3 all_in_one.py {project} {bug_id} 1"
        print(f"Running command: {command}")
        run_cmd(command)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    process_bug_ids(project_name)
