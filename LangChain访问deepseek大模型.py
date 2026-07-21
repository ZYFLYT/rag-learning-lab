import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

#加载.env里面的密钥
load_dotenv()

llm=ChatDeepSeek(
    model="deepseek-v4-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    temperature=0.7,  #随机性 0严谨1创意
    max_tokens=1024  #单次最大输出长度
)

res=llm.invoke("给我说个笑话")

print(res.content)