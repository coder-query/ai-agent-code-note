from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

load_dotenv()
import os
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')

def json_output_parser():
    from langchain_core.messages import SystemMessage
    from langchain.chat_models import  init_chat_model
    from langchain_core.output_parsers import JsonOutputParser
    from pydantic import BaseModel, Field

    llm = init_chat_model(
        model="gpt-5.6-sol",
        api_key=api_key,
        base_url=base_url,
        model_provider="openai",
        temperature=0.0,
    )

    class Prime(BaseModel):
        prime: list[int] = Field(description="素数")


    json_parser = JsonOutputParser(pydantic_object=Prime)

    sysMessage = SystemMessage(json_parser.get_format_instructions())
    userMessage = HumanMessage(content="1-100中，100以内的素数有哪些？")

    call_response = llm.invoke([sysMessage, userMessage])
    print(json_parser.get_format_instructions())
    print(call_response.content)
    print(type(call_response.content))
    parsed_res = json_parser.invoke(call_response)
    print(type(parsed_res))
    print(parsed_res)


if __name__ == '__main__':
    print(api_key)
    print(base_url)
    json_output_parser()


