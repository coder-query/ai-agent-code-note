from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model

load_dotenv()
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')

def call_llm_withLangChainAPI():
    llm = init_chat_model(
        model="gpt-5.6-sol",
        api_key=api_key,
        base_url=base_url,
        model_provider="openai",
    )
    call_response = llm.invoke(
        [
            {
                "role": "user",
                "content": "你好，请问你是谁？今天的北京有新闻呢？？？"
            }
        ]
    )
    print(call_response)
    print(type(call_response))

if __name__ == '__main__':
    call_llm_withLangChainAPI()