import os
import re
import shutil

def remove_code_comments(content):
    """删除代码块中的三引号注释"""
    # 匹配Python代码块和三引号注释
    pattern = re.compile(
        r'```python\n(.*?)```',
        re.DOTALL
    )
    
    def _remove_comments(match):
        code = match.group(1)
        # 删除三个双引号包裹的注释块
        code = re.sub(
            r'^(\s*)""".*?"""\n',
            '',
            code,
            flags=re.DOTALL | re.MULTILINE
        )
        return f"```python\n{code}```"
    
    return pattern.sub(_remove_comments, content)

def process_md_files(src_dir, dst_dir):
    """处理所有md文件并保存到新目录"""
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.md'):
                src_path = os.path.join(root, file)
                # 保持目录结构
                rel_path = os.path.relpath(root, src_dir)
                dst_folder = os.path.join(dst_dir, rel_path)
                os.makedirs(dst_folder, exist_ok=True)
                dst_path = os.path.join(dst_folder, file)
                
                # 读取并处理文件内容
                with open(src_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                new_content = remove_code_comments(content)
                
                # 写入新文件
                with open(dst_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == "__main__":
    input_dir = "/home/jky/software-testing/Q_code/bug_info04"  # 替换为源文件夹路径
    output_dir = "/home/jky/software-testing/Q_code/bug_info_104"  # 替换为目标文件夹路径
    process_md_files(input_dir, output_dir)
    print(f"处理完成！清理后的文件已保存至：{output_dir}")