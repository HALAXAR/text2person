import streamlit as st
import requests
from io import BytesIO

def download(image_url):
    response = requests.get(image_url)
    return BytesIO(response.content)

def page_four():
    st.title("Generated Image")
    image_url = st.session_state.url
    image_data = download(image_url)
    st.image(image_data)
    
    if st.button("Return to HomePage"):
        st.session_state.page = 1