import streamlit as st
from about import page_one
from prompt import page_two
from image_settings import page_three
from endpoint import page_four


def main():
    if 'page' not in st.session_state:
        st.session_state.page = 1
    if 'prompt' not in st.session_state:
        st.session_state.prompt = "Confused person"
    if 'url' not in st.session_state:
        st.session_state.url = f"https://image.pollinations.ai/prompt/{st.session_state.prompt}?model=flux&width=1024&height=1024&nologo=true&enhance=True"

    if st.session_state.page == 1:
        page_one()
    elif st.session_state.page == 2:
        page_two()
    elif st.session_state.page == 3:
        page_three()
    elif st.session_state.page == 4:
        page_four()

if __name__ == '__main__':
    main()