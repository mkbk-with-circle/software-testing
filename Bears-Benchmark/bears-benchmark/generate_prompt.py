import os
import re
import json

DIFF_PATH = "diff_position"
EXPORT_PATH = "export_bears"
WORKSPACE_PATH = "workspace"
WORKSPACE_TEST_PATH = "workspace_test"
PROMPT_PATH = "prompt"

os.makedirs(PROMPT_PATH, exist_ok=True)

def extract_names_from_diff(diff_file):
    names = set()
    with open(diff_file, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.search(r'@@.*?@@\s*(public\s+)?(class|interface|enum)?\s*(\w+)', line)
            if match:
                names.add(match.group(3))
    return list(names)

def extract_code_elements(code, name_list):
    blocks = {}
    for name in name_list:
        pattern = rf"(public\s+|protected\s+|private\s+)?(class|interface|enum)\s+{re.escape(name)}[^\{{]*\{{"
        match = re.search(pattern, code)
        if match:
            start = match.start()
            brace_count = 0
            for i in range(match.end(), len(code)):
                if code[i] == '{':
                    brace_count += 1
                elif code[i] == '}':
                    if brace_count == 0:
                        blocks[name] = code[start:i+1]
                        break
                    else:
                        brace_count -= 1
    return blocks

def extract_failure_info(json_path):
    if not os.path.exists(json_path):
        return "", "", ""
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    try:
        failure_detail = data["tests"]["failureDetails"][0]
        failure_name = failure_detail.get("failureName", "")
        test_class = failure_detail.get("testClass", "")
        detail = failure_detail.get("detail", "")
        return failure_name, test_class, detail
    except Exception:
        return "", "", ""

def extract_ecb_code(test_class, test_root):
    if not test_class:
        return ""
    rel_path = os.path.join("src", "test", "java", *test_class.split(".")) + ".java"
    abs_path = os.path.join(test_root, rel_path)
    if os.path.exists(abs_path):
        with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    return ""

for bug_folder in os.listdir(DIFF_PATH):
    print(f"Processing {bug_folder}...")

    # step 1
    diff_file = os.path.join(DIFF_PATH, bug_folder, "diff_hunks.txt")
    if not os.path.exists(diff_file):
        continue
    name_list = extract_names_from_diff(diff_file)
    if not name_list:
        continue

    # step 2
    workspace_dir = os.path.join(WORKSPACE_PATH, bug_folder)
    code_blocks = {}
    for root, _, files in os.walk(workspace_dir):
        for file in files:
            if file.endswith(".java"):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    code = f.read()
                    code_blocks.update(extract_code_elements(code, name_list))
    code_str = "\n\n".join(code_blocks.values())

    # step 3
    meta_file = os.path.join(EXPORT_PATH, bug_folder, "meta", "bears.json")
    failure_name, test_class, detail = extract_failure_info(meta_file)

    # step 4 - ECB
    test_dir = os.path.join(WORKSPACE_TEST_PATH, bug_folder)
    ecb_code = extract_ecb_code(test_class, test_dir)

    # step 5 - write
    output_path = os.path.join(PROMPT_PATH, f"{bug_folder}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("## Buggy code\n")
        f.write("```java\n" + code_str + "\n```\n\n")
        f.write("## Failed test\n" + test_class + "\n\n")
        f.write("## Test line\n" + failure_name + "\n\n")
        f.write("## Error\n" + detail + "\n\n")
        f.write("## Error Code Block\n")
        f.write("```java\n" + ecb_code + "\n```\n")

print("all Markdown in prompt")
