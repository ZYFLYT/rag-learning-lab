from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_deepseek import ChatDeepSeek
import os

model = ChatDeepSeek(model="deepseek-v4-flash", api_key=os.getenv("DEEPSEEK_API_KEY"))
str_parser = StrOutputParser()

prompt = PromptTemplate.from_template(
    "我的姓氏是{lastname},我最喜欢的食物是{foot},给我的对象起一个昵称，用我的姓氏和食物关联,只给我返回昵称就行"
)

chain = prompt | model | str_parser | model
res = chain.stream({"lastname": "周", "foot": "西瓜"})
for chunk in res:
    print(chunk.content, end="", flush=True)
