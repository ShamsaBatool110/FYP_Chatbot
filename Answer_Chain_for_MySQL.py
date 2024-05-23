from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from Response_Cleaning import clean_response

from MySQL_Query_Chain import write_query, execute_query
from LLM import llm
from Mixtral_LLM import mixtral_llm
from Test_Data import test_questions, test_questions_2

# Google Magic Prompt
magic_prompt = "Take a deep breadth and work on this problem step by step."

answer_prompt = PromptTemplate.from_template(
    """
    Take a deep breadth and work on this problem step by step.
    You are a helpful customer support assistant. Given the following user question and SQL result, answer the user question in a polite, professional and helpful way (as an efficient human customer support assistant).
    If the SQL query execution gives nothing in sql result (an empty string), just say 'I could not find any records against your question.'.
    If the SQL query execution gives any error, just say 'Apologies for inconvenience, I cannot respond to it.'.
    Give precise and relevant answer.
    Format the answer in Standard English Language format and remove any irrelevant text, strings, or symbols.
    Strictly AVOID TO include explanation, SQL query, function calls, intermediate steps or repetitions in your answer.
    
Question: {question}
SQL Query: {query}    
SQL Result: {result}

Answer: """
)

sql_chain = (
        RunnablePassthrough.assign(query=write_query).assign(
            result=itemgetter("query") | execute_query
        )
        | answer_prompt
        | mixtral_llm
        | StrOutputParser()
)

# for query in test_questions:
#     print(query)
#     response = sql_chain.invoke({"question": query})
#     print(clean_response(response))
#     print(" ")

# print(sql_chain.invoke({"question": "My name is Ali. What orders are there for me?"}))