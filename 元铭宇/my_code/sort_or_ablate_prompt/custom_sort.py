import re
import os
import sys
import yaml

target_dir = "/ymy/my_code/generate_prompt/bug_info"
output_dir = "/ymy/my_code/generate_prompt/bug_info_shuffled_6"

def load_order_config(config_path):
    """加载顺序配置文件"""
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config['order']

def custom_sort_md(file_path, order_rules):
    """根据自定义规则处理单个文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 分割章节
    sections = []
    pattern = re.compile(r'^(## .+?)(?=^## |\Z)', flags=re.MULTILINE | re.DOTALL)
    matches = list(pattern.finditer(content))
    
    if not matches:
        print(f"跳过无章节文件：{file_path}")
        return

    # 提取前言和章节
    preamble = content[:matches[0].start()].rstrip('\n')
    sections = [match.group().strip() for match in matches]

    # 构建排序索引
    ordered_sections = []
    remaining_sections = sections.copy()
    
    # 按配置顺序排序
    for pattern in order_rules:
        matched = [s for s in remaining_sections if re.search(pattern, s, flags=re.IGNORECASE)]
        ordered_sections.extend(matched)
        remaining_sections = [s for s in remaining_sections if s not in matched]

    # 添加未匹配的章节
    ordered_sections += remaining_sections

    # 生成新内容
    new_content = preamble + '\n\n' + '\n\n'.join(ordered_sections)

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 生成新文件名
    base_name = os.path.basename(file_path)
    new_file = os.path.join(output_dir, base_name.replace('.md', '_ordered.md'))
    
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"生成文件：{new_file}")

def process_directory(directory, config_path):
    """处理整个目录"""
    if not os.path.exists(directory):
        print(f"目录不存在：{directory}")
        return

    try:
        order_rules = load_order_config(config_path)
    except Exception as e:
        print(f"配置文件错误：{e}")
        return

    print(f"开始处理目录：{directory}")
    for filename in os.listdir(directory):
        if filename.endswith('.md') and not filename.endswith('_reply.md'):
            file_path = os.path.join(directory, filename)
            custom_sort_md(file_path, order_rules)
    print("处理完成")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法：python custom_sort.py <配置文件路径>")
        print("示例：python custom_sort.py order_config.yaml")
        sys.exit(1)
    
    process_directory(target_dir, sys.argv[1])