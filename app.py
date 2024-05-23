import warnings

warnings.filterwarnings("ignore")
import random
import time
import streamlit as st
from Response_Cleaning import response_formatting, clean_response
from Chain_Selection_with_Embeddings import route_query
from Answer_Chain_for_MySQL import sql_chain
from Reterival_QA_Chain import conversation_retriever_chain
from Question_Generator_Chain import question_generator
from Chain_Selection_with_LLM import query_type_selector
from Helper import find_string_in_bigger_string
from Documents_RAG_Agent import document_RAG_agent

def get_response(query, user_query_route):
    sql_present = find_string_in_bigger_string(user_query_route, "SQL")
    if sql_present:
        response = sql_chain.invoke({"question": query})
        return response
    else:
        response = document_RAG_agent.run(query)
        if type(response) is str:
            return response
        else:
            return response['answer']
        # response = conversation_retriever_chain.invoke({"question": query})
        # cleaned_response = clean_response(response['answer'])
        # # print(cleaned_response)
        # return cleaned_response


def response_generator(chain_response):
    for word in chain_response.split():
        yield word + " "
        time.sleep(0.05)


# Streamlit UI
st.title("Customer Support Chatbot")

# Initializing chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

with st.chat_message("AI"):
    st.markdown("Hello! I am Big_O_1ne, your customer support assistant. How can I help you today?")

# Display the chat history
if len(st.session_state['chat_history']) > 0:
    for message in st.session_state['chat_history']:
        question, answer = message
        with st.chat_message("Human"):
            st.markdown(question)
        with st.chat_message("AI"):
            st.markdown(answer)


user_query = st.chat_input("Type your message here...")

if type(user_query) is str:
    with st.chat_message("Human"):
        st.markdown(user_query)
    if len(st.session_state['chat_history']) > 0:
        print("Here")
        original_type_response = query_type_selector(user_query)
        user_query_route = original_type_response['text']
        other_present = find_string_in_bigger_string(user_query_route, "OTHER")
        if other_present is False:
            user_query_standalone_question = question_generator.invoke(
                {"chat_history": st.session_state['chat_history'], "question": user_query})
            user_query_standalone_question = clean_response(user_query_standalone_question['text'])
            print("S_Q: ",user_query_standalone_question)
            # user_query_route = route_query(user_query_standalone_question)
            type_response = query_type_selector(user_query_standalone_question)
            user_query_route = type_response['text']
            print("Route: ", user_query_route, len(user_query_route))
            response = get_response(user_query_standalone_question, user_query_route)
            # print(response)
        else:
            response = get_response(user_query, user_query_route)
    else:
        # user_query_route = route_query(user_query)
        print("There")
        original_type_response = query_type_selector(user_query)
        user_query_route = original_type_response['text']
        if user_query_route != "OTHER":
            type_response = query_type_selector(user_query)
            user_query_route = type_response['text']
            print("Route: ", user_query_route, len(user_query_route))
            response = get_response(user_query, user_query_route)
        else:
            print("Route: ", user_query_route, len(user_query_route))
            response = get_response(user_query, user_query_route)

    with st.chat_message("AI"):
        # print(response)
        st.write_stream(response_generator(response))

    st.session_state['chat_history'].append((user_query, response))

