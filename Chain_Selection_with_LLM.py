import warnings
warnings.filterwarnings("ignore")
from Mixtral_LLM import mixtral_llm
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from Test_Data import test_questions, test_questions_2, documents_test_queries, other_domain_queries, jibrish_queries
from Response_Cleaning import clean_response

memory = [("What products are available here?", "You can purchase a wide range of home appliances from Al-Fatah "
                                                "Electronics, including LEDs, Air Conditioners, Refrigerators, "
                                                "Washing Machines, Microwave Ovens, Small Electronics, "
                                                "Water Dispensers, Cooking Range, Kitchen Hobs, Kitchen Hoods, "
                                                "Dishwashers, Geysers, Heaters, Deep Freezers, Water Cooler, "
                                                "Kitchen Sinks, Kitchen Taps, Warming Drawers, Dryers and Air "
                                                "Curtains."),
          ("Give me some details of the first one.", "LEDs are one of the products available at Al-Fatah Electronics. "
                                                     "The features of LEDs available at Al-Fatah Electronics are not "
                                                     "explicitly mentioned in the given context. However, "
                                                     "we can infer that the LEDs available at Al-Fatah Electronics "
                                                     "are 100% genuine products with quality after-sale services. The "
                                                     "warranty policy for LEDs may vary from product to product. If "
                                                     "you want to know more about the features of LEDs available at "
                                                     "Al-Fatah Electronics, you may need to contact the company or "
                                                     "visit their website. I don't know."),
          ("How can I purchase it?", "You can purchase the LEDs available at Al-Fatah Electronics by logging into "
                                     "your account as explained in Section – 1 and then clicking the “Add to Cart” "
                                     "button appearing at the end of each product as displayed below.")]

# Define the categories
categories = ["SQL", "FAQ", "OTHER"]


template = """
    Take a deep breath and solve the problem carefully.
    You are a classifier for an e-commerce customer support chatbot. Your task is to classify user input into one of three categories: 
    1. "SQL" for questions related to customer data, order history, products available, product prices, product description, etc., which are stored in a MySQL database.
    2. "FAQ" for questions related to website content like FAQs, processes, rules, policies, etc. How to purchase a product, what is return/refund policy, etc.
    3. "OTHER" for any input that is gibberish, irrelevant, or unrelated to customer support and the available products or documents (e-commerce).
    Give one word response.
    
    Text: "{user_input}

    Category:"""

type_prompt = PromptTemplate.from_template(template)

query_type_selector = LLMChain(
    llm=mixtral_llm,
    prompt=type_prompt
)


# for user_input in documents_test_queries:
#     print(user_input)
#     response = query_type_selector(user_input)
#     print(response['text'])
#     print(" ")

# print(query_type_selector("What can I get from here?")['text'])