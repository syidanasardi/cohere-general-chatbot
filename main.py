import streamlit as st
from chatbot_utils import get_response


st.title('Chatbot with Streamlit')


if 'chats' not in st.session_state:
    st.session_state.chats = []

def submit():
    user_input = st.session_state.input
    if user_input:
        response = get_response(st.session_state.input)
        st.session_state.chats.append({"user": st.session_state.input, "ai": response})
        st.session_state.input = ''

st.text_input('Enter a message:', key='input', on_change=submit)




for chat in reversed(st.session_state.chats):
    st.write(f"You: {chat['user']}")
    st.write(f"AI: {chat['ai']}")
    st.write('---')