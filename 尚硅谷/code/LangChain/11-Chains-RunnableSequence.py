import os
from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")


def runnable_sequence_demo(subject: str = "机器学习") -> str:
    llm = init_chat_model(
        model="gpt-5.6-sol",
        api_key=api_key,
        base_url=base_url,
        model_provider="openai",
        temperature=0.0,
    )

    prompt_template = PromptTemplate.from_template("请给我讲解{subject}是什么？")
    output_parser = StrOutputParser()

    # 关键：把 PromptTemplate（Runnable）直接接进链，而不是它的 format 结果
    chain = prompt_template | llm | output_parser

    res = chain.invoke({"subject": subject})   # 用 dict 传参，配合 PromptTemplate
    print(res)
    return res


if __name__ == "__main__":
    runnable_sequence_demo("机器学习")