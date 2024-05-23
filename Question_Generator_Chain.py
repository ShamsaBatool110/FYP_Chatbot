from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain

from LLM import llm
from Mixtral_LLM import mixtral_llm
from Response_Cleaning import clean_response

template = """Given the following chat history and a follow up question, rephrase the follow up input question to be a standalone question.
Or end the conversation if it seems like it's done. If the follow up question is incomplete phrase, non-sensical question, or gibberish keys, return it as standalone question.

Chat History:\"""
{chat_history}
\"""
Follow Up Input: \"""
{question}
\"""
Standalone question:"""

condense_question_prompt = PromptTemplate.from_template(template)

question_generator = LLMChain(
    llm=mixtral_llm,
    prompt=condense_question_prompt
)

memory = [("What products are available here?", "You can purchase a wide range of home appliances from Al-Fatah Electronics, including LEDs, Air Conditioners, Refrigerators, Washing Machines, Microwave Ovens, Small Electronics, Water Dispensers, Cooking Range, Kitchen Hobs, Kitchen Hoods, Dishwashers, Geysers, Heaters, Deep Freezers, Water Cooler, Kitchen Sinks, Kitchen Taps, Warming Drawers, Dryers and Air Curtains."),
          ("Give me some details of the first one.", "LEDs are one of the products available at Al-Fatah Electronics. The features of LEDs available at Al-Fatah Electronics are not explicitly mentioned in the given context. However, we can infer that the LEDs available at Al-Fatah Electronics are 100% genuine products with quality after-sale services. The warranty policy for LEDs may vary from product to product. If you want to know more about the features of LEDs available at Al-Fatah Electronics, you may need to contact the company or visit their website. I don't know."),
          ("How can I purchase it?", "You can purchase the LEDs available at Al-Fatah Electronics by logging into your account as explained in Section – 1 and then clicking the “Add to Cart” button appearing at the end of each product as displayed below."),
          ("My name is Ali. What orders are there for me?", "Hi Ali, according to our records, you have two orders: Order 1 and Order 2. Please let me know if you need any further assistance.")]

# generated_question = question_generator.invoke({"chat_history": memory, "question": "two love"})
# cleaned_generated_question = clean_response(generated_question['text'])
# print(cleaned_generated_question)
