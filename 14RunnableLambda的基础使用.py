from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek
from langchain_core.runnables import RunnableLambda
import os

model = ChatDeepSeek(model="deepseek-v4-flash", api_key=os.getenv("DEEPSEEK_API_KEY"))
str_parser = StrOutputParser()

first_prompt = PromptTemplate.from_template(
    "我的姓氏是{lastname},我最喜欢的食物是{foot},给我的对象起一个昵称，用我的姓氏和食物关联,只给我返回昵称就行"
)

second_prompt = PromptTemplate.from_template(
    "昵称{nickname},帮我解析含义"
)

my_func = RunnableLambda(lambda ai_msg: {"nickname": ai_msg.content})

chain = first_prompt | model | my_func | second_prompt | model | str_parser

res = chain.stream({"lastname": "周", "foot": "西瓜"})
for chunk in res:
    print(chunk, end="", flush=True)
