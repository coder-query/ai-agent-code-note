from dotenv import load_dotenv
import os
from openai import OpenAI
from openai.types.responses import WebSearchToolParam

load_dotenv()
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')

openAiClient = OpenAI(
    api_key=api_key,
    base_url=base_url
)

def  call_llm_withResonseAPI():
   call_response = openAiClient.responses.create(
        model="gpt-5.6-sol",
        input="最近中国发生什么新闻吗？请使用中文回答我",
        tools=[
            WebSearchToolParam(type="web_search",search_context_size="low")
        ]
    )
   print(call_response)
   print(call_response.output_text)


if __name__ == '__main__':
    call_llm_withResonseAPI()