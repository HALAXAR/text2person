import streamlit as st

def page_one():
    st.write("# Welcome to Character Generation WebApp")
    st.markdown("""
        This is a personalized character generation app backed by [pollinations.ai].
        You can create a character based on your imagination by providing a description.
    """)
    if st.button("Next"):
        st.session_state.page = 2