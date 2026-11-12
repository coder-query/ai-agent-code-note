from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')



def get_model_from_openai_package():
  from langchain_openai import ChatOpenAI
  llm = ChatOpenAI(
    model="gpt-5.6-sol",
    temperature=0.0,
    base_url=base_url,
    api_key=api_key
  )
  resp = llm.invoke("你好,你是谁？")
  print(type(resp))
  print(resp.content)


if __name__ == '__main__':
    get_model_from_openai_package()