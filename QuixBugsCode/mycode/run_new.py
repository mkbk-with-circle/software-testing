import os
import subprocess
from glob import glob

def get_impl_filename(test_file):
    """从测试文件名提取对应的实现文件名"""
    base = os.path.basename(test_file)
    if base.startswith("test_") and base.endswith(".py"):
        return base[5:]  # 移除'test_'前缀
    return None

def run_pytest_test(test_file, impl_dir):
    """运行单个测试文件并返回是否全部通过"""
    try:
        # 获取对应的实现文件路径
        impl_file = get_impl_filename(test_file)
        impl_path = os.path.join(impl_dir, impl_file)
        
        # 确保实现文件存在
        if not os.path.exists(impl_path):
            print(f"⚠️ 实现文件缺失: {impl_file}")
            return False

        # 运行测试（使用绝对路径确保测试文件可定位）
        result = subprocess.run(
            ["pytest", "--timeout=5", test_file],  # 移除非标准参数--correct
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print(f"🕒 测试超时: {os.path.basename(test_file)}")
        return False
    except Exception as e:
        print(f"❌ 执行异常: {os.path.basename(test_file)} - {str(e)}")
        return False

def process_tests(test_dir, impl_dir):
    """处理所有匹配的测试文件并统计正确率"""
    correct_files = 0
    incorrect_files = 0
    
    # 获取所有测试文件（使用绝对路径）
    test_files = glob(os.path.join(test_dir, "test_*.py"))
    cnt = 0
    for test_file in test_files:
        # 获取对应的实现文件名
        impl_file = get_impl_filename(test_file)
        if not impl_file:
            cnt -= 1
            print(f"⏭️ 跳过非法测试文件: {os.path.basename(test_file)}")
            continue
            
        print(f"\n🔍 正在测试: {os.path.basename(test_file)} → {impl_file}")
        is_passed = run_pytest_test(test_file, impl_dir)
        
        if is_passed:
            correct_files += 1
            cnt += 1
            print("✅ 测试结果: 全部通过")
        else:
            incorrect_files += 1
            cnt += 1
            print("❌ 测试结果: 存在失败用例")

    # 打印统计结果
    total_files = correct_files + incorrect_files
    if total_files > 0:
        accuracy = correct_files / 31 * 100
        print(f"\n{'='*40}")
        print(f"📊 总测试文件: {31}")
        print(f"🎯 正确率: {accuracy:.2f}%")
        print(f"📈 分布: ✅ {correct_files} | ❌ {31 - correct_files}")
    else:
        print("\n⚠️ 没有找到匹配的测试文件")

if __name__ == "__main__":
    # 路径配置（根据实际情况修改）
    test_dir = "../QuixBugs-master/python_testcases"       # 原测试文件目录
    new_code_dir = "../QuixBugs-master/python_programs"  # 修复后的代码目录
    process_tests(test_dir, new_code_dir)  # 直接传入目录路径