
from dotenv import load_dotenv

load_dotenv()
import os
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')

def prompt_template_demo():
    from langchain_core.prompts import PromptTemplate
    from langchain.chat_models import init_chat_model
    from langchain_core.messages import HumanMessage,SystemMessage

    llm = init_chat_model(
      model="gpt-5.6-sol",
      api_key=api_key,
      base_url=base_url,
      model_provider="openai",
      temperature=0.0,

    )
    sysMessage = SystemMessage(content="你是一个高级算法工程师")
    prompt_template = PromptTemplate.from_template(template="请给我讲解{subject}是什么？")
    userMessage = HumanMessage(content=prompt_template.format(subject="机器学习"))
    res = llm.invoke([sysMessage,userMessage])
    print(res)



if __name__ == '__main__':
    prompt_template_demo()