'''
获取
1. 源代码
2. 失败的测试名
3. 对应的错误的测试行
4. 显示的错误及其正确/错误的输出
'''

import re

# Function to extract the relevant sections from the txt file
def extract_bug_details(txt_file_path, output_md_path):
    with open(txt_file_path, 'r') as file:
        content = file.read()

    # Remove the "Example" part from the content using regex (between "Example start" and "Example end")
    content = re.sub(r"<Example start>.*?<Example end>", "", content, flags=re.DOTALL)

    # Remove the last sentence: "Please provide an analysis of the problem..."
    content = re.sub(r"Please provide an analysis of the problem and the expected behaviour of the correct fix, and the correct version of the function in the form of Java Markdown code block\.", "", content)

    # Extract each section using regex
    buggy_code_match = re.search(r"(?<=The following code contains a bug:)(.*?)(?=The code fails on this test:)", content, re.DOTALL)
    failed_test_match = re.search(r"(?<=The code fails on this test:)(.*?)(?=on this test line:)", content, re.DOTALL)
    test_line_match = re.search(r"(?<=on this test line:)(.*?)(?=with the following test error:)", content, re.DOTALL)
    error_match = re.search(r"(?<=with the following test error:)(.*)", content, re.DOTALL)

    # Open the output markdown file to write the results
    with open(output_md_path, 'w') as md_file:
        if buggy_code_match:
            md_file.write("## Buggy code\n")
            md_file.write(f"```java\n{buggy_code_match.group(0).strip()}\n```\n\n")
        
        if failed_test_match:
            md_file.write("## Failed test\n")
            md_file.write(f"{failed_test_match.group(0).strip()}\n\n")

        if test_line_match:
            md_file.write("## Test line\n")
            md_file.write(f"{test_line_match.group(0).strip()}\n\n")

        if error_match:
            md_file.write("## Error\n")
            md_file.write(f"{error_match.group(0).strip()}\n")

# Example usage
txt_file_path = '/ymy/an-implementation-of-chatrepair/initial/Lang/10.txt'  # Replace with your txt file path
output_md_path = '/ymy/my_code/generate_prompt/bug_info/my_info/info.md'  # The output markdown file path

extract_bug_details(txt_file_path, output_md_path)
