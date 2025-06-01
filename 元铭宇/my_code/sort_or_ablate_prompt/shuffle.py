import re
import random
import os
import sys
input_dir = "./prompt"
output_dir = "./prompt_shuffled"

def shuffle_md_sections(file_path, output_dir):
    """处理单个MD文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    preamble = []
    sections = []
    
    pattern = re.compile(r'^(## .+?)(?=^## |\Z)', flags=re.MULTILINE | re.DOTALL)
    matches = list(pattern.finditer(content))
    
    if not matches:
        print(f"{file_path} 未找到##开头的章节")
        return

    preamble = content[:matches[0].start()].rstrip('\n')
    
    for match in matches:
        sections.append(match.group().strip())
#这里保留了第一段，如果要全打乱，也很容易修改
    first_section = sections[0]
    to_shuffle = sections[1:]
    random.shuffle(to_shuffle)
    shuffled = [first_section] + to_shuffle
    
    new_content = preamble + '\n\n'.join(shuffled)

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    # 生成新文件名
    base_name = os.path.basename(file_path)
    new_file = os.path.join(output_dir, base_name.replace('.md', '_shuffled.md'))
    
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"生成文件：{new_file}")

def process_directory(directory):
    """处理目录下的所有MD文件"""
    if not os.path.exists(directory):
        print(f"目录不存在：{directory}")
        return

    print(f"开始处理目录：{directory}")
    
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            shuffle_md_sections(file_path, output_dir)
    
    print("处理完成")

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("使用方法：python shuffle.py")
        sys.exit(1)
    
    process_directory(input_dir)