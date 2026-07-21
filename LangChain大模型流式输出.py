import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

load_dotenv()

llm=ChatDeepSeek(
    model="deepseek-v4-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    temperature=0.7
)

stream_res=llm.stream(input="给我简洁介绍一下科技论文")

#llm.invoke()：一次性等待完整结果返回，无打字动画;  llm.stream()：服务端逐字符分片推送，循环迭代实现实时流式

for chunk in stream_res:
    print(chunk.content,end="",flush=True)
    # chunk.content 取出当前分片文本
    # end=""：打印不自动换行，文字连续输出模拟打字效果
    # flush=True 强制实时输出，不会缓存文字一次性弹出