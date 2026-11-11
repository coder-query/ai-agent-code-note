from langchain_community.document_loaders import UnstructuredMarkdownLoader

def markdown_loader_demo():

    loader = UnstructuredMarkdownLoader("./assets/sample.md",encoding="utf-8",mode="elements")
    docs = loader.load()
    print(docs)
    for doc in docs:
        print(doc.page_content,end="\n============\n")


if __name__ == '__main__':
    markdown_loader_demo()