import os
import argparse
import requests

API_URL = "https://api.deepseek.com/v1/chat/completions"

def chat_with_deepseek(file_path, prompt_prefix="", model="deepseek-chat"):

    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("❌ 请设置环境变量 DEEPSEEK_API_KEY。")

    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()

    # 拼接输入内容
    prompt = f"{prompt_prefix.strip()}\n\n{file_content.strip()}"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "你是一个精通编程的助手。"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    print(f"⏳ 正在调用 {model} ...")
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise RuntimeError(f"❌ 请求失败: {response.status_code} - {response.text}")

    # 获取回复内容
    reply = response.json()['choices'][0]['message']['content']
    print("✅ DeepSeek 回复：\n")
    # 将回复内容写入文件,若文件不存在则创建。文件名是文件名去掉最后的prompt.md改为reply.md
    file_name = file_path.replace(".md", "_reply.md")
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(reply)
            # 刷新缓冲区
            f.flush()
    else:
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(reply)
            # 刷新缓冲区
            f.flush()
    print(reply)
    print(f"✅ 回复已保存到 {file_name}")
    return reply

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="将文件内容输入 DeepSeek 并获取回复")
    parser.add_argument("--filepath", help="要读取的文件路径")
    parser.add_argument("--folder", help="文件夹路径", default="")
    parser.add_argument("--prefix", help="提问前缀，例如：请分析以下代码：", default="请你根据信息帮我对Buggy code进行debug并且只返回修复后的代码")
    parser.add_argument("--model", help="模型名称（默认 deepseek-chat）", default="deepseek-chat")

    args = parser.parse_args()
    if args.folder:
        # 对文件夹排序
        files = os.listdir(args.folder)
        files.sort()
        for file in files:
            # 只选择文件名前缀为Bear的文件,且不以reply.md结尾的文件
            chat_with_deepseek(os.path.join(args.folder, file), args.prefix, args.model)
    else:
        chat_with_deepseek(args.filepath, args.prefix, args.model)
