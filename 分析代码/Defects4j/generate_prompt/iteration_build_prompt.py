import re
import os
from all_in_one import run
from run_all_in_one_script import get_valid_bug_ids

def extract_lang_blocks(logs_text):
    """
    从 Markdown 文本中提取每个以 ## Lang_{n} 开头的块，并组成字典
    """
    # 正则匹配所有标题及其位置
    headers = [(m.group(), m.start()) for m in re.finditer(r'## Lang_\d+', logs_text)]
    
    result = {}
    for i in range(len(headers)):
        title, start = headers[i]
        end = headers[i + 1][1] if i + 1 < len(headers) else len(logs_text)
        block = logs_text[start:end].strip()
        
        # 去掉标题行，作为内容存储
        content = block.split("\n", 1)[1].strip() if "\n" in block else ""
        result[title] = content

    return result

target_dir = "/ymy/my_code/generate_prompt/all_bug_info/bug_info_for_shuffled/bug_info_shuffled_6"
logs_file = os.path.join(target_dir, "logs.md")
save_dir= "/ymy/my_code/generate_prompt/all_bug_info/bug_info_for_iteration/bug_info_for_shuffled/bug_info_shuffled_6"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

with open(logs_file, "r", encoding="utf-8") as f:
    logs_text = f.read()

#提取的bug
logs_blocks = extract_lang_blocks(logs_text)
#获取某个项目的所有bug id,并且排序
bug_ids = get_valid_bug_ids("Lang")
bug_ids.sort()

# 遍历每个bug id
for bug_id in bug_ids:
    # 构造对应的bug id字符串，形如:"## Lang_{n}"
    bug_id_title = f"## Lang_{bug_id}"
    # 获取对应的bug info
    bug_info = ""
    # 尝试获取bug_info,如果没有，则跳过
    if bug_id_title not in logs_blocks:
        continue
    bug_info = logs_blocks[bug_id_title]
        # 检查bug_info里是否有某一行包含子串"Failing tests: 0"
    if "Failing tests: 0" not in bug_info:
        # 说明需要进行迭代更新，先读取target_dir目录下的prompt文件
        prompt_file = os.path.join(target_dir, f"Lang_{bug_id}_prompt.md")
        with open(prompt_file, "r", encoding="utf-8") as f:
            prompt_text = f.read()
        # 然后读取target_dir目录下的reply文件
        reply_file = os.path.join(target_dir, f"Lang_{bug_id}_reply.md")
        with open(reply_file, "r", encoding="utf-8") as f:
            reply_text = f.read()
        # 提取reply_text里用```java和```包裹的代码块,把```java和```也保留 
        reply_text = re.findall(r'```java(.*)```', reply_text, re.DOTALL)
        
        # 将提取的代码块写入到prompt_text里
        prompt_text += f"\n## mistake patch"
        prompt_text += f"\n以下之前你给出的错误的修正代码"
        prompt_text += f"\n```java\n"
        prompt_text += f"\n{reply_text[0]}"
        prompt_text += f"\n```"
        # 匹配bug_info里是否包含"BUILD FAILED",如果有加上一句“之前编译失败了”
        if "BUILD FAILED" in bug_info:
            prompt_text += f"\n运用你给出的修复代码后，编译失败了"
        prompt_text += f"\n请你继续修正"
        # 将prompt_text写入到prompt_file里
        new_prompt_file = os.path.join(save_dir, f"Lang_{bug_id}_iteration_prompt.md")
        with open(new_prompt_file, "w", encoding="utf-8") as f:
            f.write(prompt_text)
        # 调用run函数，进行迭代更新
        


