from sentence_transformers import SentenceTransformer, util
from Test_Data import test_questions, test_questions_2, documents_test_queries, other_domain_queries, jibrish_queries

sql_description = ("Manage customer existing orders, products, and inventory. Retrieve order history, "
                   "product details, and stock quantities, product availability. Update customer information and "
                   "verify changes.")
web_description = ("Get help with online shopping. Find answers to questions about what is offered for purchase, "
                   "placing orders, canceling"
                   "orders, return policies, refunds, how to get a product (process for order).")
other_domains_description = "Incomplete sentence, nonsensical phrase, fruit."

other = ("Unrelated queries (irrelevant to customer support), gibberish, or unclear english sentences. "
         "This includes nonsensical phrases, irrelevant questions, or statements that don't require a response. "
         "Non-electronic products like animals, fruits, books, etc.")

model = SentenceTransformer("all-MiniLM-L6-v2")

embedding_sql = model.encode(sql_description)
embedding_web = model.encode(web_description)
embedding_garbage = model.encode(other_domains_description)


def route_query(query):
    query_embd = model.encode(query)
    similarity_sql = util.cos_sim(query_embd, embedding_sql)
    similarity_web = util.cos_sim(query_embd, embedding_web)
    similarity_other = util.cos_sim(query_embd, embedding_garbage)
    similarites = [similarity_sql, similarity_web, similarity_other]
    chains = ["SQL", "Web", "Other"]
    chain_idx = similarites.index(max(similarites))
    return chains[chain_idx]


#-------------------------TESTING---------------------------#
# for query in documents_test_queries:
#     chain_type = route_query(query)
#     print(query)
#     print(chain_type)
#     print(" ")

# print(route_query("Tell me order cancellation process."))
#-----------------------------------------------------------#
