from openai import OpenAI, api_key
from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam
from dotenv import load_dotenv
import os


def call_llm_withChatCompletion(api_key,base_url):
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )
    call_response=client.chat.completions.create(
        model="gpt-5.6-sol",
        messages=[
            ChatCompletionUserMessageParam(
                content="你好，请问你是谁？今天的北京天气怎么样",
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

if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('API_KEY')
    base_url = os.getenv('BASE_URL')
    call_llm_withChatCompletion(api_key,base_url)