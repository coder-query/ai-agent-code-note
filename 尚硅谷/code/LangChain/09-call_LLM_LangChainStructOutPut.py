
from dotenv import load_dotenv

load_dotenv()
import os
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')

def json_output_use_langchain():
  from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
  from langchain.chat_models import init_chat_model
  from pydantic import BaseModel
  # 定义一个Pydantic模型，用于表示日历事件
  class CalendarEvent(BaseModel):
      name: str
      date: str
      participants: list[str]

  llm = init_chat_model(
      model="gpt-5.6-sol",
      api_key=api_key,
      base_url=base_url,
      model_provider="openai",
      temperature=0.0,
  )
  sysMessage = SystemMessage(content="你是一个导游")
  userMessage = HumanMessage(content="2026年12月3日，小张要去见她的女朋友，约定好去银川玩2天")
  # 返回一个新的LLM模型，该模型将返回一个Pydantic模型
  new_llm = llm.with_structured_output(schema=CalendarEvent)
  res = new_llm.invoke([sysMessage,userMessage])
  print(res)
  print(type(res))

if __name__ == '__main__':
    print(api_key)
    print(base_url)
    json_output_use_langchain()