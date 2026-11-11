
from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam
from dotenv import load_dotenv
import os

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


if __name__ == '__main__':
  call_llm_withChatCompletionAPI()
