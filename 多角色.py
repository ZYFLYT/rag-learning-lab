import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

llm=ChatDeepSeek(
    model="deepseek-v4-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    temperature=0.7
)

messages_full=[
    SystemMessage(content="你是一个十分有经验且专业的科技英语的英语老师"),
    HumanMessage(content="给我简洁介绍一下科技论文"),
    AIMessage(content="科技论文是**记录原创科学研究成果、经过同行评议并发表在学术期刊上的正式文献**"),
    HumanMessage(content="给我介绍一下科技论文，包括期刊分类、影响因子、论文构成、第一作者、通讯作者等，"
                         "以及所相关的专业内容，我要考试了，给我详细介绍下，以及所有我需要的内容")
]

print("=====完整消息对象流式输出=====\n")
for chunk in llm.stream(input=messages_full):
    print(chunk.content,end="",flush=True)

print("\n\n=====二元组简写流式输出=====\n")
messages_short=[
    ("system","你是一个十分有经验且专业的科技英语的英语老师"),
    ("human","给我简洁介绍一下科技论文"),
    ("ai","科技论文是**记录原创科学研究成果、经过同行评议并发表在学术期刊上的正式文献**"),
    ("human","现在简洁的告诉我怎么学习这些内容")
]
for chunk in llm.stream(input=messages_short):
    print(chunk.content,end="",flush=True)