#!/usr/bin/env python3
import re
import subprocess
import os
import sys
import javalang


def run_cmd(cmd, cwd=None, check=True):
    """
    运行外部命令并打印调试信息。

    参数:
        cmd (list[str]): 命令列表，例如 ["java", "-cp", cp, "org.junit.runner.JUnitCore", class_fqn]。
        cwd (str, optional): 命令执行的工作目录，默认为 None。
        check (bool, optional): 是否在命令非零退出时抛出异常，默认为 True。

    返回:
        subprocess.CompletedProcess: 包含返回码、标准输出和标准错误。
    """
    print(f"[DEBUG] 执行命令: {' '.join(cmd)} (cwd={cwd})")
    proc = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=check
    )
    print(f"[DEBUG] 返回码: {proc.returncode}")
    if proc.stdout:
        print(f"[DEBUG] 标准输出:\n{proc.stdout.strip()}")
    if proc.stderr:
        print(f"[DEBUG] 标准错误:\n{proc.stderr.strip()}", file=sys.stderr)
    return proc


def get_failing_line(work_dir: str, test_id: str):
    """
    使用 JUnitCore 运行整个测试类，并定位指定测试方法的失败行号。

    处理流程：
    1. 从 test_id 提取测试类全限定名和方法名。
    2. 导出测试时的 classpath。
    3. 使用 JUnitCore 执行测试类，即便失败也不抛异常。
    4. 按方法名精确匹配堆栈帧：方法名(File.java:LINE)，优先获取对应方法的错误行号。
    5. 如果未匹配到，再回退至扫描所有 (File.java:LINE)，依次查找项目源码中存在的文件。

    参数:
        work_dir (str): 已检出并编译项目的工作目录。
        test_id (str): 测试标识，格式为 类全限定名::方法名。

    返回:
        tuple(str, int): 失败的文件名和行号。

    抛出:
        RuntimeError: 如果无法从任何输出中提取到行号。
    """
    # 1) 提取测试类和方法
    class_fqn, test_method = test_id.split("::", 1)

    # 2) 导出测试 classpath
    cp_proc = run_cmd(
        ["defects4j", "export", "-p", "cp.test"], cwd=work_dir
    )
    cp = cp_proc.stdout.strip()

    # 3) 使用 JUnitCore 运行测试类，不抛异常便于捕获输出
    junit_proc = subprocess.run(
        ["java", "-cp", cp, "org.junit.runner.JUnitCore", class_fqn],
        cwd=work_dir, capture_output=True, text=True, check=False
    )
    jout = junit_proc.stdout + junit_proc.stderr
    print(f"[DEBUG] JUnitCore 输出:\n{jout}")

    # 4) 精确匹配 当前测试方法 的堆栈帧：方法名(File.java:LINE)
    specific_pattern = rf"{re.escape(test_method)}\(([^():]+\.java):(\d+)\)"
    m = re.search(specific_pattern, jout)
    if m:
        return m.group(1), int(m.group(2))

    # 5) 回退：扫描所有 (File.java:LINE)，跳过不在项目源码中的
    matches = re.findall(r"\(([^():]+\.java):(\d+)\)", jout)
    for fname, lineno in matches:
        try:
            find_source_file(work_dir, fname)
            return fname, int(lineno)
        except FileNotFoundError:
            continue

    # 均未匹配时抛错
    raise RuntimeError(f"无法从 JUnitCore 输出提取行号，输出如下:\n{jout}")


def find_source_file(work_dir: str, filename: str):
    """
    在工作目录中查找指定的 Java 源文件。

    参数:
        work_dir (str): 搜索根目录。
        filename (str): 文件名，例如 MyClass.java。

    返回:
        str: 找到的文件绝对路径。

    抛出:
        FileNotFoundError: 如果未找到目标文件。
    """
    for root, dirs, files in os.walk(work_dir):
        if filename in files:
            return os.path.join(root, filename)
    raise FileNotFoundError(f"未找到源文件: {filename}")


def extract_method_block(java_path: str, error_line: int):
    """
    提取包含指定行号的 Java 方法代码块。

    参数:
        java_path (str): Java 源文件路径。
        error_line (int): 错误行号。

    返回:
        str: 包含错误行的完整方法源码，或失败提示信息。
    """
    try:
        with open(java_path, encoding="utf-8") as f:
            src = f.read().splitlines()
    except FileNotFoundError:
        print(f"错误：找不到文件 {java_path}")
        return None
    except UnicodeDecodeError:
        print(f"错误：文件编码不是 UTF-8，尝试使用其他编码")
        # 可以尝试其他编码，比如 latin-1
        try:
            with open(java_path, encoding="latin-1") as f:
                src = f.read().splitlines()
        except Exception as e:
            print(f"错误：读取文件失败 - {str(e)}")
            return None
    tree = javalang.parse.parse("\n".join(src))

    for _, node in tree.filter(javalang.tree.MethodDeclaration):
        if not node.position:
            continue
        start = node.position.line
        brace = 0
        for i, ln in enumerate(src[start-1:], start=start):
            brace += ln.count("{") - ln.count("}")
            if brace == 0:
                end = i
                break
        else:
            continue
        if start <= error_line <= end:
            return "\n".join(src[start-1:end])
    return f"未能定位到包含行 {error_line} 的方法。"


def main():
    import argparse
    parser = argparse.ArgumentParser(description="提取 Defects4J BUG 触发测试失败代码块")
    parser.add_argument("-p", "--project", required=True, help="项目 ID，例如 Lang")
    parser.add_argument("-b", "--bug", type=int, required=True, help="Bug 编号，例如 1")
    parser.add_argument("-w", "--workdir", required=True, help="工作目录路径")
    args = parser.parse_args()

    # 1. Checkout 并编译指定版本
    run_cmd(["defects4j", "checkout", "-p", args.project, "-v", f"{args.bug}b", "-w", args.workdir])
    run_cmd(["defects4j", "compile", "-w", args.workdir])

    # 2. 导出触发测试列表
    tests = run_cmd(["defects4j", "export", "-p", "tests.trigger", "-w", args.workdir]).stdout.strip().split()
    if not tests:
        print("没有找到 trigger tests", file=sys.stderr)
        sys.exit(1)

    # 3. 遍历触发测试，定位第一个失败并提取行号
    for t in tests:
        print(f"[*] 测试 {t}")
        try:
            java_file, line_no = get_failing_line(args.workdir, t)
            print(f"  => Failure at {java_file}:{line_no}")
            break
        except Exception as e:
            print(f"[WARN] {t} 解析失败，继续下一个 ({e})", file=sys.stderr)
    else:
        print("所有触发测试均未提取到失败行号", file=sys.stderr)
        sys.exit(1)

    # 4. 查找源文件并提取代码块
    src_path = find_source_file(args.workdir, java_file)
    print(f"Source: {src_path}")
    block = extract_method_block(src_path, line_no)
    print("\n======= 代码块开始 =======\n")
    print(block)
    print("\n======= 代码块结束 =======\n")

if __name__ == "__main__":
    main()
