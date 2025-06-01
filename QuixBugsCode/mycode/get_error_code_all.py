import os
import re

def process_files(input_dir='../QuixBugs-master/python_programs', output_dir='bug_info'):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 获取所有文件列表
    all_files = os.listdir(input_dir)
    
    # 构建需要排除的文件集合
    exclude_files = set()
    
    # 第一步：收集所有_test.py文件
    test_files = [f for f in all_files if f.endswith('_test.py')]
    
    # 第二步：生成对应的实现文件名并验证存在性
    for test_file in test_files:
        # 提取基础名 (例如: breadth_first_search_test.py -> breadth_first_search.py)
        impl_file = test_file.replace('_test.py', '.py')
        
        # 如果对应的实现文件存在
        if impl_file in all_files:
            exclude_files.add(test_file)
            exclude_files.add(impl_file)
    
    # 遍历处理文件
    for filename in all_files:
        filepath = os.path.join(input_dir, filename)
        
        # 跳过条件：目录文件、在排除列表中、文件名包含_test
        if (os.path.isdir(filepath) or 
            filename in exclude_files or 
            '_test' in filename or 
            'node' in filename):
            continue
        
        # 读取文件内容
        with open(filepath, 'r') as f:
            content = f.read()
        
        # 生成Markdown内容
        md_content = f"## Buggy code\n\n```python\n{content.strip()}\n```"
        
        # 生成输出文件名
        output_filename = os.path.splitext(filename)[0] + '_prompt.md'
        output_path = os.path.join(output_dir, output_filename)
        
        # 写入文件
        with open(output_path, 'a') as f:
            f.write(md_content)

if __name__ == '__main__':
    process_files()