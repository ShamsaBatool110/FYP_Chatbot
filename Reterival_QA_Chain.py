from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.memory import ConversationBufferMemory
from Response_Cleaning import clean_response
from Mixtral_LLM import mixtral_llm

from LLM import llm
from Test_Data import documents_test_queries, other_domain_queries, jibrish_queries

embeddings = HuggingFaceEmbeddings()
vector_store_db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
retriever = vector_store_db.as_retriever()

memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True, output_key='answer')
conversation_retriever_chain = ConversationalRetrievalChain.from_llm(
    llm=mixtral_llm,
    chain_type="stuff",
    memory=memory,
    retriever=retriever,
    return_source_documents=False
)

# for query in other_domain_queries:
#     response = conversation_retriever_chain.invoke({"question": query})
#     cleaned_response = clean_response(response['answer'])
#     print(cleaned_response)

# print(conversation_retriever_chain.invoke("hjhjs")['answer'])
