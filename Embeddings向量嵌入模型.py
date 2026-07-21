import os
from dotenv import load_dotenv
from langchain_community.embeddings import DashScopeEmbeddings

load_dotenv()

embed=DashScopeEmbeddings()

# 1. embed_query：单个文本转为向量，用于用户提问向量化（RAG检索用户问题）
single_vector=embed.embed_query("我喜欢你")
print("单文本向量 embed_query 长度：",len(single_vector))
print("向量前十位:",single_vector[:10])

# 2. embed_documents：批量多个文本转向量，用于知识库文档分块向量化（RAG入库文档）
batch_texts=["我喜欢你","Go语言框架","python语言","罗雨婷"]
batch_vectors=embed.embed_documents(batch_texts)
print("\n【批量文本向量 embed_documents】文本数量：", len(batch_vectors))
print("第4条文档向量前10位：", batch_vectors[3][:10])