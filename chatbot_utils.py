# Create general chatbot using cohere API
import cohere
import streamlit as st

co = cohere.ClientV2(st.secrets["cohere_api_key"])

def get_response(question):
    chat = co.chat(
        model="command-r-plus-08-2024",
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
    )
    return chat.message.content[0].text
