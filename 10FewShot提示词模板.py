from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
import os

load_dotenv()

example_template = PromptTemplate.from_template("单词:{word}, 反义词:{antonym}")
example_data = [{"word": "大", "antonym": "小"}, {"word": "上", "antonym": "下"}]

few_shot_prompt = FewShotPromptTemplate(
    examples=example_data,
    example_prompt=example_template,
    prefix="给出给定词的反义词，有如下示例:",
    suffix="基于示例告诉我：{input_word}的反义词是？",
    input_variables=["input_word"]
)

model = ChatDeepSeek(model="deepseek-v4-flash", api_key=os.getenv("DEEPSEEK_API_KEY"))
chain = few_shot_prompt | model
res = chain.stream({"input_word": "左"})
for chunk in res:
    print(chunk.content, end="", flush=True)
