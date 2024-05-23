# Document Loader
from langchain_community.document_loaders import TextLoader
import textwrap
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

loader = TextLoader("all_text.txt")
documents = loader.load()
print(len(documents))


def wrap_text_preserve_newlines(text, width=110):
    lines = text.split('\n')
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
    wrapped_text = '\n'.join(wrapped_lines)
    return wrapped_text


print(wrap_text_preserve_newlines(str(documents[0])))

text_splitter = CharacterTextSplitter(chunk_size=600, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Embeddings
embeddings = HuggingFaceEmbeddings()

# save to disk
vector_db = Chroma.from_documents(docs, embeddings, persist_directory="./chroma_db")
