import streamlit as st
import requests


def download(image_url):
    response = requests.get(image_url)
    with open('image.jpg', 'wb') as file:
        file.write(response.content)
    print('Download Completed')


def page_four():
    st.set_page_config(
        page_title = "Generated Image"
    )
    image_url = st.session_state.url
    download(image_url)
    st.title("Generated Image")
    st.image("image.jpg")
    if st.button("Return to HomePage"):
        st.session_state.page=1