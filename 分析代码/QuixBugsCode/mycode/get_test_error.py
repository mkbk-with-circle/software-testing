import os
import re
import subprocess
from glob import glob
def clean_markdown_file(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 使用正则表达式删除summary部分
    cleaned_content = re.sub(
        r'=+\s*(?:short test summary info|\d+ failed.*?)\s*=+.*?=+\s*\d+.*?s\s*=+',
        '',
        content,
        flags=re.DOTALL
    )
    
    # 清理多余空行
    cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content.strip())



def process_test_file(test_file, bug_info_dir):
    # 运行 pytest 并捕获输出
    result = subprocess.run(
        ["pytest", "--timeout=5", test_file],
        capture_output=True,
        text=True
    )
    raw_output = result.stdout + result.stderr

    # 解析详细错误块
    detailed_blocks = re.findall(
        r'_{5,} (test_\w+\[[\w-]+\]) _{5,}\n'
        r'([\s\S]*?)\n'
        r'>\s+(assert .*?)\n'
        r'([\s\S]*?)\n'
        r'(E\s+.*?)\n(?=_{5,} test_|\Z)',
        raw_output,
        re.DOTALL
    )

    # 解析 short test summary 中的失败条目
    summary_failures = re.findall(
        r'FAILED (\S+::test_\w+\[[\w-]+\])',
        raw_output
    )

    # 合并两种错误来源
    all_failures = []
    
    # 处理详细错误块
    for match in detailed_blocks:
        all_failures.append({
            "test_name": match[0],
            "test_line": match[2].strip(),
            "error_msg": re.sub(r'\n\s*', ' ', match[4]).strip()
        })
    
    # 处理summary中的条目（去重）
    for entry in summary_failures:
        if not any(f["test_name"] in entry for f in all_failures):
            all_failures.append({
                "test_name": entry.split("::")[-1],
                "test_line": "Assertion not captured",
                "error_msg": "Failure recorded in summary only"
            })

    if not all_failures:
        print(f"No failed tests found in {test_file}")
        return

    # 生成目标文件名
    base_name = os.path.basename(test_file)
    md_filename = base_name.replace("test_", "").replace(".py", "_prompt.md")
    md_path = os.path.join(bug_info_dir, md_filename)

    # 构建Markdown内容
    content = "\n\n"
    # 失败测试列表
    content += "## Failed test\n"
    content += "\n".join([f"{i+1}.{f['test_name']}" for i, f in enumerate(all_failures)]) + "\n\n"
    
    # 断言代码行
    content += "## Test line\n" 
    content += "\n".join([f"{i+1}.{f['test_line']}" for i, f in enumerate(all_failures)]) + "\n\n"
    
    # 错误信息
    content += "## Error\n"
    error_lines = []
    for i, failure in enumerate(all_failures, 1):
        # 清理错误信息中的换行和缩进
        clean_error = re.sub(r'\n\s*', ' ', failure['error_msg']).strip()
        error_lines.append(f"{i}.{clean_error}")
    content += "\n".join(error_lines)

    # 追加写入文件
    with open(md_path, "a", encoding="utf-8") as f:
        f.write(content + "\n\n")
    
    clean_markdown_file(md_path)

def main():
    # 确保输出目录存在
    bug_info_dir = "/home/jky/software-testing/Q_code/bug_info"
    os.makedirs(bug_info_dir, exist_ok=True)
    
    # 获取所有测试文件
    test_files = glob(os.path.join("../QuixBugs-master/python_testcases", "test_*.py"))
    
    # 处理每个测试文件
    for test_file in test_files:
        print(f"Processing: {test_file}")
        process_test_file(test_file, bug_info_dir)

if __name__ == "__main__":
    main()