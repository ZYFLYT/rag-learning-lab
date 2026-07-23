from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek
import os

# 初始化解析器
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

# DeepSeek模型
model = ChatDeepSeek(model="deepseek-v4-flash", api_key=os.getenv("DEEPSEEK_API_KEY"))

# 第一层模板：生成JSON格式名字
first_prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请起名，并封装到JSON格式返回给我，"
    "要求key是name，value就是起的名字。请严格遵守格式要求"
)

# 第二层模板：解析名字含义
second_prompt = PromptTemplate.from_template(
    "姓名{name}，请帮我解析含义。"
)

# 完整串联链
chain = first_prompt | model | json_parser | second_prompt | model | str_parser

# 执行
res: str = chain.invoke({"lastname": "张", "gender": "女儿"})
print("最终输出：", res)
print("输出类型：", type(res))
