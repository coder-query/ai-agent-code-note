import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')

def call_llm_streaming_mode():
  from langchain_openai import ChatOpenAI
  llm = ChatOpenAI(
    model="gpt-5.6-sol",
    temperature=0.0,
    base_url=base_url,
    api_key=api_key
  )
  response = llm.stream("Hello, 你是什么模型")
  # 遍历迭代器对象，打印每个chunk的内容
  for chunk in response:
    print(chunk.content,end="")

if __name__ == '__main__':
    call_llm_streaming_mode()