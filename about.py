import streamlit as st

def page_one():
    st.set_page_config(
        page_title = "Welcome"
    )

    st.write("# Welcome to Character Generation WebApp")

    st.markdown(
        """
        This is a personalized character generation app which is backed by [pollinations.ai].
        By the means of this app users can create a character based purely on imagination.
        This requires the user to provide a description of the character in the text fields provided.    
    """
    )
    if st.button("Next"):
        st.session_state.page=2