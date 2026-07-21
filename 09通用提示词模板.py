from os import getenv

from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
import os

load_dotenv()

prompt_template=PromptTemplate.from_template(
    "我的姓氏是{lastname},我最喜欢的食物是{favourite},现在给我的对象起一个和我同姓氏的可爱昵称"
)

model=ChatDeepSeek(
    model="deepseek-v4-flash",
    api_key=getenv("DEEPSEEK_API_KEY"),
    temperature=0.8
)

#调用format方法注入信息
# prompt_text=prompt_template.format(lastname="周",favourite="芒果")
# res=model.invoke(input=prompt_text)
# print(res.content)

chain=prompt_template|model
res=chain.invoke(input={"lastname":"周","favourite":"西瓜"})
print(res.content)