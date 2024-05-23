from langchain.agents import AgentType, initialize_agent
from LLM import llm
from Test_Data import documents_test_queries, jibrish_queries, other_domain_queries
from Response_Cleaning import response_formatting
from Agent_Tools import tools


document_RAG_agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False, handle_parsing_errors=True,
    max_iterations=3,
)

# ---------------------------------TESTING----------------------------------#

# response = document_RAG_agent.run(
#     "What products are available here?"
# )
# print(response['answer'])

# for query in documents_test_queries:
#     response = document_RAG_agent.run(query)
#     formatted_response = response_formatting(response)
#     print(formatted_response)
# --------------------------------------------------------------------------#
