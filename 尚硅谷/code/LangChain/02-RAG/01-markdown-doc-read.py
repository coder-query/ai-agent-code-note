from langchain_community.document_loaders import UnstructuredMarkdownLoader
import os


def get_markdown_file_path():
    # 获取当前脚本所在目录的绝对路径（不受运行时工作目录影响）
    abspath = os.path.abspath(__file__)
    print(f"abspath = {abspath}")
    current_dir = os.path.dirname(abspath)
    print(f"current_dir = {current_dir}")
    f_path = os.path.dirname(current_dir)
    print(f"f_path = {f_path}")
    # 用 os.path.join 拼接出 markdown 文件的绝对路径
    return os.path.join(f_path, "assets", "sample.md")

def markdown_loader_demo():
    file_path = get_markdown_file_path()
    print(f"加载文件：{file_path}")
    loader = UnstructuredMarkdownLoader(file_path, encoding="utf-8", mode="elements")
    docs = loader.load()
    print(docs)
    for doc in docs:
        print(doc.page_content,end="\n============\n")


if __name__ == '__main__':
    get_markdown_file_path()

    # markdown_loader_demo()