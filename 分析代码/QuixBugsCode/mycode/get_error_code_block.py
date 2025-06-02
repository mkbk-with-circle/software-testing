import os
import re
import subprocess
from glob import glob
import ast

def run_tests_and_get_errors(test_file):
    """运行pytest并捕获错误信息（增加超时控制）"""
    try:
        result = subprocess.run(
            ["pytest", "--timeout=5", "-v", test_file],
            capture_output=True,
            text=True,
            timeout=60  # 增加整体超时控制
        )
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        print(f"测试执行超时: {test_file}")
        return ""

def parse_failure_line(test_output):
    """改进错误行匹配模式"""
    # 匹配格式：文件路径:行号: 错误描述
    error_line_pattern = r"^(.*?\.py):(\d+):.*"
    matches = []
    for line in test_output.split('\n'):
        match = re.search(error_line_pattern, line)
        if match:
            matches.append((match.group(1), match.group(2)))
    return matches

def find_code_block(file_path, line_number):
    """增强AST解析的健壮性"""
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            source = f.read()
        
        tree = ast.parse(source)
    except Exception as e:
        print(f"解析失败 {file_path}: {str(e)}")
        return None
    
    target_line = int(line_number)
    current_block = None
    
    # 遍历AST树寻找包含目标行的最小代码块
    for node in ast.walk(tree):
        if hasattr(node, 'lineno') and hasattr(node, 'end_lineno'):
            if node.lineno <= target_line <= node.end_lineno:
                if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
                    current_block = node
                    break  # 优先函数/类定义
                elif not current_block:
                    current_block = node
    
    if current_block:
        with open(file_path, "r", encoding='utf-8') as f:
            lines = f.readlines()
        start = current_block.lineno - 1
        end = current_block.end_lineno
        return "".join(lines[start:end])
    
    return None

def process_files(input_dir='../QuixBugs-master/python_programs',
                 test_dir='../QuixBugs-master/python_testcases',
                 output_dir='bug_info'):
    
    os.makedirs(output_dir, exist_ok=True)
    test_files = glob(os.path.join(test_dir, "test_*.py"))
    
    error_map = {}
    for test_file in test_files:
        print(f"正在处理测试文件: {os.path.basename(test_file)}")
        test_output = run_tests_and_get_errors(test_file)
        error_locations = parse_failure_line(test_output)
        
        for file_name, line_no in error_locations:
            impl_file = os.path.join(input_dir, os.path.basename(file_name))
            if os.path.exists(impl_file):
                error_map.setdefault(impl_file, set()).add(int(line_no))

    # 生成错误代码块文件
    for impl_file, lines in error_map.items():
        base_name = os.path.basename(impl_file)
        md_filename = os.path.splitext(base_name)[0] + '_prompt.md'
        md_path = os.path.join(output_dir, md_filename)
        
        if not os.path.exists(md_path):
            continue
        content = "\n\n ## Error code block\n"
        code_blocks = []
        for line_no in sorted(lines):
            block = find_code_block(impl_file, line_no)
            if block:
                code_blocks.append(block)
        
        if code_blocks:
            with open(md_path, 'a', encoding='utf-8') as f:
                f.write(content)
                f.write("\n\n".join(code_blocks))
            print(f"已生成: {md_path}")
        else:
            with open(base_name, 'r') as f:
                content += f"## Buggy code\n\n```python\n{f.read()}\n```"
            with open(md_path, 'a', encoding='utf-8') as f:
                f.write(content)
            print(f"已生成: {md_path}") 

if __name__ == "__main__":
    process_files()