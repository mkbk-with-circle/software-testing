import os
import re
import argparse

def extract_code_from_md(md_content):
    """使用正则表达式提取所有python代码块"""
    pattern = r'```python\n(.*?)```'
    matches = re.findall(pattern, md_content, re.DOTALL)
    return [match.strip() for match in matches]

def process_folder(input_dir, output_dir):
    """处理目录中的所有markdown文件"""
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 遍历输入目录
    for filename in os.listdir(input_dir):
        if filename.endswith("_reply.md"):
            input_path = os.path.join(input_dir, filename)
            
            # 生成输出文件名
            base_name = filename.replace("_prompt_reply.md", ".py")
            output_path = os.path.join(output_dir, base_name)
            
            # 读取并处理文件
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
                code_blocks = extract_code_from_md(content)
                
                if code_blocks:
                    # 保存第一个代码块（通常修复后的代码）
                    with open(output_path, 'w', encoding='utf-8') as out_f:
                        out_f.write(code_blocks[0])
                    print(f"已提取 {filename} => {base_name}")
                else:
                    print(f"⚠️ 未找到代码块: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="从Markdown回复文件提取Python代码")
    parser.add_argument("-i", "--input", required=True, help="输入目录路径")
    parser.add_argument("-o", "--output", required=True, help="输出目录路径")
    #python3 reply2pynew.py -i reply_info01 -o ../QuixBugs-master/new_code01
    args = parser.parse_args()
    
    print(f"开始处理目录: {args.input}")
    process_folder(args.input, args.output)
    print(f"处理完成！结果保存在: {args.output}")