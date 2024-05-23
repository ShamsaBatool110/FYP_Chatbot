import warnings
warnings.filterwarnings("ignore")
from langchain_community.llms import HuggingFaceEndpoint
import os
from langchain import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from Test_Data import test_questions, test_questions_2, documents_test_queries, jibrish_queries, other_domain_queries

# HUGGINGFACEHUB_API_TOKEN = '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'
HUGGINGFACEHUB_API_TOKEN = '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'
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

mixtral_llm=HuggingFaceEndpoint(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
                                temperature=0.9, top_p=0.95, max_new_tokens=250,
                                repetition_penalty=1.1)

# template = """
# Act as a highly intelligent customer support chatbot for an e-commerce website and classify the given user text into one of the following categories only 1. SQL Database Query 2.Website FAQ, Processes, Policies 4. Other
# Do not code. Return only one word answer with only the category name that the given user text belongs to
# User text: {query}
#
# """
# prompt = PromptTemplate(input_variables=["query"],template=template)
#
# chain = LLMChain(llm=mixtral_llm,prompt=prompt)
#
# categories = ['SQL Database Query', 'Website FAQ', 'Processes', 'Policies', 'Other']
# def process_llm_output(answer):
#     for category in categories:
#         if category.lower() in answer.lower():
#             return category
#
# for query in test_questions:
#     print(query)
#     print(chain.run(query))
