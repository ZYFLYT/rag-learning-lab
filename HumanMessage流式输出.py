import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage

load_dotenv()

chat=ChatDeepSeek(
    model="deepseek-v4-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

#构造消息列表
messages=[
    HumanMessage(content="给我介绍一下科技论文，包括期刊分类、影响因子、论文构成、第一作者、通讯作者等，"
                         "以及所相关的专业内容，我要考试了，给我详细介绍下，以及所有我需要的内容")
]

print("AI输出:")
for chunk in chat.stream(input=messages):
    print(chunk.content,end="",flush=True)