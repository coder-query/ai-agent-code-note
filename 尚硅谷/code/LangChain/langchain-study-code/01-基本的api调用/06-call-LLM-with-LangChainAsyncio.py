import asyncio
import os

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')


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
    msgList = [
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
    tasks = [asyncio.create_task(async_call_llm_withLangChainAPI(msg)) for msg in msgList]
    res = await asyncio.gather(*tasks)
    print(f"async_call_llm_main: -----> {res}")
    end_time = time.time()
    print(f"async_call_llm_main异步执行总耗时: -----> {end_time - start_time}")

if __name__ == '__main__':
    asyncio.run(async_call_llm_main())