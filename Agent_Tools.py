from langchain.tools import tool
from langchain.agents import Tool
from Reterival_QA_Chain import conversation_retriever_chain
from Answer_Chain_for_MySQL import sql_chain

@tool
def handle_out_of_domain_input(user_input):
    """If user asks a question other than customer support domain"""
    return ("I am a customer support chatbot specialized in this domain. I cannot respond to your query. Please let me "
            "know if you have any query related to my domain.")

tools =[
    Tool(
        name="Website Related QA System",
        func=conversation_retriever_chain.invoke,
        description="useful for when you need to answer questions about the e-commerce website (Al-Fatah "
                    "Electronics). Input should be a fully formed question.",
        return_direct=True
    ),
    Tool(
        name="Irrelevant Query Handling System",
        func=handle_out_of_domain_input,
        description="useful for when you need to answer questions irrelevant to customer support domain",
        return_direct=True
    )
]
