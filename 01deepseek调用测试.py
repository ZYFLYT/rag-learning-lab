# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
from dotenv import load_dotenv

#自动读取当前目录下的.env文件，把里面的变量加到环境变量中
load_dotenv()
#创建与AI大模型交互的客户端(DEEPSEEK_API_KEY环境变量的名字，值就是deepseek的API_KEY的值)
client = OpenAI(
    api_key=os.getenv('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#与AI大模型进行交互
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你好，给我介绍下RAG和Agent"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

#输出大模型返回的结果
print(response.choices[0].message.content)