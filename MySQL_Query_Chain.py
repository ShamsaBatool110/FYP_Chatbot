from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain.chains import create_sql_query_chain
from LLM import llm
from Database_Connection import db
from Test_Data import test_questions, test_questions_2

execute_query = QuerySQLDataBaseTool(db=db)
write_query = create_sql_query_chain(llm, db)
query_chain = write_query | execute_query


# for test_question in test_questions:
#     print(test_question)
#     test_query = write_query.invoke({"question": test_question})
#     print(test_query)
#
#     test_query_response = execute_query.invoke(test_query)
#     print(test_query_response)
#     print(" ")

# for test_question in test_questions_2:
#     print(test_question)
#     test_query = write_query.invoke({"question": test_question})
#     print(test_query)
#
#     test_query_response = execute_query.invoke(test_query)
#     print(test_query_response)
#     print(" ")

wrong_query_questions = ["My order ID is 1. What product IDS are included in it?"]
alternative_correct_question = ["Get the details of order with ID 5, including customer name and the products ordered.", "Get the details of order id 5 with products included."]

# test_question = "List all customers"
# test_query = write_query.invoke({"question": test_question})
# print(test_query)
# test_query_response = execute_query.invoke({"query": test_query})
# print(test_query_response)

# for test_question in test_questions:
#     print(test_question)
#     test_question_response = query_chain.invoke({"question": test_question})
#     print(test_question_response)

