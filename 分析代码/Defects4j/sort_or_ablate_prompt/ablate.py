import re
import os

# 示例：在脚本开头定义输入输出目录
input_dir = "/ymy/my_code/generate_prompt/all_bug_info/bug_info"
output_dir = "/ymy/my_code/generate_prompt/all_bug_info/bug_info_for_ablation/bug_info_ablation_4"

def ablate_md_sections(file_path, output_dir, sections_to_remove):
    """根据指定的 sections_to_remove 列表删除 Markdown 文件中的对应小节及其内容。"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 依次删除每个要移除的小节及其内容
    for section in sections_to_remove:
        escaped_section = re.escape(section)
        # 匹配 '## 小节名称' 及其内容，直到下一个 '## ' 或文档末尾
        pattern = re.compile(rf'##\s+{escaped_section}[\s\S]*?(?=(\n##\s+)|$)')
        content = re.sub(pattern, '', content)

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.basename(file_path)
    new_file = os.path.join(output_dir, base_name)
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"生成文件：{new_file}")


def process_directory(directory, sections_to_remove):
    """处理目录下所有以 prompt.md 结尾的文件，删除指定的小节列表。"""
    if not os.path.exists(directory):
        print(f"目录不存在：{directory}")
        return

    print(f"开始处理目录：{directory}，删除小节：{sections_to_remove}")
    for filename in os.listdir(directory):
        if filename.endswith('prompt.md'):
            file_path = os.path.join(directory, filename)
            ablate_md_sections(file_path, output_dir, sections_to_remove)
    print("处理完成")


if __name__ == "__main__":
    # 在此定义要删除的小节列表，例如 ['Error Code Block', 'Buggy code']
    SECTIONS_TO_REMOVE = ['Failed test', 'Test line', 'Error']
    process_directory(input_dir, SECTIONS_TO_REMOVE)
