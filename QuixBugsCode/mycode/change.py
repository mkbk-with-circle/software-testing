import os
import shutil

def sync_py_files(folder_a, folder_b):
    """
    同步文件夹B中的.py文件，使其与文件夹A中的文件保持一致
    - 同名文件：用A中的内容覆盖B中的文件
    - B中存在但A中没有的.py文件：删除
    """
    # 获取A和B中的所有.py文件（仅文件名，不包含路径）
    files_a = {f for f in os.listdir(folder_a) if f.endswith('.py')}
    files_b = {f for f in os.listdir(folder_b) if f.endswith('.py')}

    # 处理B中的文件
    for file_b in files_b:
        src_path = os.path.join(folder_a, file_b)
        dst_path = os.path.join(folder_b, file_b)
        
        if file_b in files_a:
            # 覆盖B中的文件
            shutil.copy2(src_path, dst_path)
            print(f"✅ 覆盖文件: {file_b}")
        else:
            # 删除B中的文件
            os.remove(dst_path)
            print(f"🗑️ 删除文件: {file_b}")

if __name__ == "__main__":
    folder_a = "/home/jky/software-testing/QuixBugs-master/new_code_104"  # 替换为实际路径
    folder_b = "/home/jky/software-testing/QuixBugs-master/python_programs"  # 替换为实际路径
    
    # 验证路径是否存在
    if not os.path.isdir(folder_a):
        raise FileNotFoundError(f"文件夹A不存在: {folder_a}")
    if not os.path.isdir(folder_b):
        raise FileNotFoundError(f"文件夹B不存在: {folder_b}")
    
    sync_py_files(folder_a, folder_b)
    print("\n同步完成！")