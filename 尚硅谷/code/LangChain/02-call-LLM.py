from langchain_core.language_models import LanguageModelInput
from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam
from dotenv import load_dotenv
import os

from openai.types.responses import WebSearchToolParam

load_dotenv()
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')

openAiClient = OpenAI(
    api_key=api_key,
    base_url=base_url
)

def call_llm_withChatCompletionAPI():
    call_response=openAiClient.chat.completions.create(
        model="gpt-5.6-sol",
        messages=[
            ChatCompletionUserMessageParam(
                content="你好，请问你是谁？今天的北京有新闻呢？？？",
                role="user",
                name="user-zsh"
            ),
            ChatCompletionSystemMessageParam(
                content="你是一个高级全栈开发工程师",
                role="system",
                name="system-zsh"
            )
        ]
    )
    print(call_response)
    print(call_response.choices[0].message.content)


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


def call_llm_withLangChainAPI():
    from langchain.chat_models import init_chat_model
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
    # call_llm_withChatCompletionAPI()
    # call_llm_withResonseAPI()
    call_llm_withLangChainAPI()