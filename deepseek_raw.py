import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)

try:
    resp = client.embeddings.create(
        model="deepseek-embedding",
        input="测试"
    )
    print("✅ 原生调用成功，向量长度:", len(resp.data[0].embedding))
except Exception as e:
    print("❌ 原生调用失败:", e)
    # 如果这里也 404，说明问题不在 LangChain，而在 DeepSeek 账号/模型名/网络