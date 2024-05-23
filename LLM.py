from langchain_community.llms import HuggingFaceEndpoint
import os

# HUGGINGFACEHUB_API_TOKEN = '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'
HUGGINGFACEHUB_API_TOKEN = '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'
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.01
    )