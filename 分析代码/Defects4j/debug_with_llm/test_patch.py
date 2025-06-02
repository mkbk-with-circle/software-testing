# 输入中有两个个参数，第一个为数字n，表示是第几个bug，然后在相对路径为../../test/下执行，
# 第二个是project，表示是哪个项目，然后执行
# defects4j checkout -p Lang -v {n}b -w ../../test/Lang_{n}_buggy
# 然后在../../an-implementation-of-chatrepair/patches/{project}找到{n}.json文件，
# json文件如下所示：
"""
{
    "num_of_hunks": 1,
    "0": {
        "file_name": "/ymy/test/patch/src/main/java/org/apache/commons/lang3/time/FastDateParser.java",
        "patch_type": "insert",
        "replaced_with": "        if (patternMatcher.regionStart() != patternMatcher.regionEnd()) {\n            throw new IllegalArgumentException(\"Failed to parse \\\"\"+pattern+\"\\\" ; gave up at index \"+patternMatcher.regionStart());\n        }\n",
        "next_line_no": 144
    }
}
"""
# 可能有很多个hunks但是只需要提取第一个块中的file_name即可
# 然后把/ymy/test/ptach替换为../../test/{project}_{n}_buggy,得到了file_name_buggy
# 然后找到../generate_prompt/bug_info/{project}_{n}_reply.md文件，
# 提取其中被"```java"和"```"包裹的代码,赋值给变量ds_patch，
# 例如：
"""
```java
public int translate(final CharSequence input, final int index, final Writer out) throws IOException {
    int max = longest;
    if (index + longest > input.length()) {
        max = input.length() - index;
    }
    // descend so as to get a greedy algorithm
    for (int i = max; i >= shortest; i--) {
        final CharSequence subSeq = input.subSequence(index, index + i);
        final CharSequence result = lookupMap.get(subSeq.toString());
        if (result != null) {
            out.write(result.toString());
            return i;
        }
    }
    return 0;
}
```
"""

# 然后找到file_name_buggy对应的文件，利用utils中的函数找到刚刚提取的de_patch对应的代码行是哪些（这一段我自己写）
# 然后进行替换，将de_patch替换到file_name_buggy中，但是暂时存储好原来的代码行，因为后续还要恢复回去，此时刷新一下文件并且加个breakpoint（确保已经进行替换）
# 然后进行测试，进入../../test/{project}_{n}_buggy，运行defects4j test，
# 并且获取其返回的信息，输入到统一的log文件中：. ./../logs.txt(注意同时标明是第几个bug)
# 然后恢复原来的代码行，并且刷新文件，加个breakpoint（确保已经恢复）


import os
import json
import subprocess
import argparse
import re
import shutil
import utils
import constants


import re

def extract_sections(md_text):
    # 定义我们关注的五个小节名
    section_names = {
        'Failed test',
        'Error',
        'Error Code Block',
        'Test line',
        'Buggy code'
    }

    # 使用正则表达式匹配所有标题及其内容
    pattern = re.compile(r'##\s+(.*?)\n(.*?)(?=(\n##\s+|$))', re.DOTALL)
    matches = pattern.findall(md_text)

    # 保存为字典，确保乱序也能提取
    section_dict = {name: '' for name in section_names}  # 初始化字典，所有小节名默认值为空字符串
    for title, content, _ in matches:
        title = title.strip()
        if title in section_names:
            section_dict[title] = content.strip()

    return section_dict



def find_patch_lines(prompt_path, buggy_path):
    public_line_num = None
    end_line_num = None
    public_line = None
    with open(prompt_path, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()

    # 根据markdown中的小节进行分类，
    sections = extract_sections(content)
    # 依次打印sections中的内容
    # 示例输出：查看 Error Code Block 内容
    #print("Error Code Block:\n", sections.get("Error Code Block", "[未找到]"))
    #breakpoint()

    # 提取section中对应“## Buggy code”的部分
    buggy_section = sections["Buggy code"]
    # 找到buggy_code中第一个以“/*”为开头的行所在行数
    start_line = None
    for i, line in enumerate(buggy_section.splitlines()):
        if line.startswith("/*"):
            start_line = i
            break
    if start_line is None:
        start_line = 0
    print("start_line", start_line)
    print(buggy_section.splitlines()[start_line+1])
    # 找到buggy_code中第二个以“```”为开头的行所在行数
    end_line = None
    for i, line in enumerate(buggy_section.splitlines()):
        if line.startswith("```"):
            if end_line is None:
                end_line = i
            else:
                end_line = i
                break
    print("end_line", end_line)
    print(buggy_section.splitlines()[end_line-1])
    # 计算end_line-start_line的值，赋值给function_length
    function_length = end_line - start_line
    #breakpoint()
    with open(buggy_path, 'r', encoding='utf-8') as f:
        buggy_code = f.readlines()
    # 将buggy_code中的行与buggy_section.splitlines()[start_line+1]进行匹配,需要忽略开头的空格
    buggy_start = None
    for i, line in enumerate(buggy_code):
        if i>66 and i<70:
            print("i", i)
            print(line.lstrip(), buggy_section.splitlines()[start_line+1].lstrip())
        # 改为是否某一句为另一句的子串  
        if line.lstrip().startswith(buggy_section.splitlines()[start_line+1].lstrip()) or line.lstrip().endswith(buggy_section.splitlines()[start_line+1].lstrip()):
            buggy_start = i-1
            break
    if buggy_start is None:
        print("🚩 Breakpoint: patch not found")
        exit(0)
    print("buggy_start, buggy_end", buggy_start, buggy_start+function_length)
    #breakpoint()
    return buggy_start, buggy_start+function_length

    






def main():
    parser = argparse.ArgumentParser(description="Automatically apply and test LLM patch for a Defects4J bug")
    parser.add_argument('n', type=int, help='Bug number (e.g., 1 for Lang_1)')
    parser.add_argument('project', help='Project name (e.g., Lang)')
    args = parser.parse_args()

    n = args.n
    proj = args.project
    ####################################################################################
    # 1. Checkout buggy version，获取文件夹
    workdir = f"../../test/{proj}_{n}_buggy"
    prompt_workdir = f"../generate_prompt/all_bug_info/bug_info_for_ablation/bug_info_ablation_4"
    # 如果文件夹不存在，则checkout
    if not os.path.isdir(workdir):
        cmd = [
            'defects4j', 'checkout',
            '-p', proj,
            '-v', f'{n}b',
            '-w', workdir
        ]
        print(f"⏳ Checking out {proj} bug {n} into {workdir}...")
        subprocess.run(cmd, check=True)
    else:
        print(f"📂 Working dir already exists: {workdir}")
    ####################################################################################
    # 2. 加载patch_json文件,获取buggy代码的文件路径
    patch_json = f"../../an-implementation-of-chatrepair/patches/{proj}/{n}.json"
    with open(patch_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    first_hunk = data.get('0')
    # 获取第一个hunk的file_name，找到文件路径
    original_path = first_hunk['file_name']
    # 更换为真实的路径
    buggy_path = original_path.replace('/ymy/test/patch', workdir)
    print(f"✅ Target buggy file: {buggy_path}")
    ####################################################################################
    # 3. 从reply.md中提取patch代码
    md_file = f"{prompt_workdir}/{proj}_{n}_reply.md"
    # print("md_file", md_file)
    with open(md_file, 'r', encoding='utf-8') as f:
        md = f.read()
    # 提取被```java和```包裹的代码
    match = re.search(r'```java\s*(.*?)```', md, re.S)
    if not match:
        raise ValueError('No Java code block found in reply markdown')
    ds_patch = match.group(1).rstrip('\n') + '\n'# 去除末尾的换行符
    #print("ds_patch", ds_patch)
    ####################################################################################
    # 4. 定位patch代码，获得其起始行和
    prompt_path = f"{prompt_workdir}/{proj}_{n}_prompt.md"
    start_line, end_line = find_patch_lines(prompt_path,buggy_path)
    if start_line == -1:
        print("🚩 Breakpoint: patch not found")
        return
    print(f"🔍 Patch applies to lines {start_line} to {end_line}")
    ####################################################################################
    # 5. 定位buggy代码
    with open(buggy_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Backup original lines
    orig_lines = lines[start_line:end_line]
    pre_lines = lines[:start_line]
    post_lines = lines[end_line:]

    # Apply patch
    patch_lines = [line + '\n' for line in ds_patch.splitlines()]
    # 以比较易读的方式打印patch_lines和orig_lines
    print("patch_lines:\n", "".join(patch_lines))
    print("\n\n\n\n")
    print("orig_lines:\n", "".join(orig_lines))
    #breakpoint()
    new_lines = pre_lines + patch_lines + post_lines
    with open(buggy_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("🚩 Breakpoint: patch applied, file written.")
    #breakpoint()



    # 5. Run Defects4J test
    print("🧪 Running defects4j test...")
    test_proc = subprocess.run(
        ['defects4j', 'test'],
        cwd=workdir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    output = test_proc.stdout

    # Append to logs
    log_line = f"{proj}_{n}: {output}\n"
    with open(f'{prompt_workdir}/logs.md', 'a', encoding='utf-8') as logf:
        #先写上“## Lang{n}”
        logf.write(f"## Lang_{n}\n")
        logf.write(log_line)
    print(f"📓 Log appended to {prompt_workdir}/logs.md")

    # 6. Restore original file
    restore_lines = pre_lines + orig_lines + post_lines
    with open(buggy_path, 'w', encoding='utf-8') as f:
        f.writelines(restore_lines)
    print("🚩 Breakpoint: original code restored.")

    # 把defects4j checkout的文件夹删除
    shutil.rmtree(workdir)

if __name__ == '__main__':
    main()
