from langchain_core.language_models import LanguageModelInput
from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam
from dotenv import load_dotenv
import os
import asyncio
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

async def async_call_llm_withLangChainAPI(msg):
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(
        model="gpt-5.6-sol",
        temperature=0.0,
        base_url=base_url,
        api_key=api_key
    )
    resp = await llm.ainvoke(msg)
    print(type(resp))
    print(resp.content)
    return resp

async def async_call_llm_main():
    import time
    start_time = time.time()
    msg = [
        [
            {
                "role": "system",
                "content": "你是一个高级算法工程师"
            },
            {
                "role": "user",
                "content": "你好,你是谁？你知道机器学习是什么吗？"
            }
        ],
        [
            {
                "role": "system",
                "content": "你是一个高级算法工程师"
            },
            {
                "role": "user",
                "content": "你好,你是谁？你知道深度学习是什么吗？"
            }
        ],
        [
            {
                "role": "system",
                "content": "你是一个高级算法工程师"
            },
            {
                "role": "user",
                "content": "你好,你是谁？你知道强化学习是什么吗？"
            }
        ]
    ]
    asyncio_task = [async_call_llm_withLangChainAPI(msg) for msg in msg]
    res = await asyncio.gather(*asyncio_task)
    print(f"async_call_llm_main: -----> {res}")
    end_time = time.time()
    print(f"async_call_llm_main异步执行总耗时: -----> {end_time - start_time}")

def sync_call_llm_main():
    import time
    start_time = time.time()
    msg = [
        [
            {
                "role": "system",
                "content": "你是一个高级算法工程师"
            },
            {
                "role": "user",
                "content": "你好,你是谁？你知道机器学习是什么吗？"
            }
        ],
        [
            {
                "role": "system",
                "content": "你是一个高级算法工程师"
            },
            {
                "role": "user",
                "content": "你好,你是谁？你知道深度学习是什么吗？"
            }
        ],
        [
            {
                "role": "system",
                "content": "你是一个高级算法工程师"
            },
            {
                "role": "user",
                "content": "你好,你是谁？你知道强化学习是什么吗？"
            }
        ]
    ]
    for msg in msg:
        sync_call_llm_withLangChainAPI(msg)
    end_time = time.time()
    print(f"sync_call_llm_main同步执行总耗时: -----> {end_time - start_time}")

def sync_call_llm_withLangChainAPI(msg):
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(
        model="gpt-5.6-sol",
        temperature=0.0,
        base_url=base_url,
        api_key=api_key
    )
    resp = llm.invoke(msg)
    print(type(resp))
    print(resp.content)
    return resp



if __name__ == '__main__':

    # 1. 使用openai的chat.completions.create接口调用LLM
    #            call_llm_withChatCompletionAPI()
    #2. 使用openai的responses.create接口调用LLM
    #            call_llm_withResonseAPI()
    #3. 使用langchain的chat_models.init_chat_model接口调用LLM
    #            call_llm_withLangChainAPI()
    #4. 使用langchain_openai的ChatOpenAI接口调用LLM
    #             get_model_from_openai_package()
    #5. 异步调用LLM
    asyncio.run(async_call_llm_main())
    #6. 同步调用LLM
    sync_call_llm_main()