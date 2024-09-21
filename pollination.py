import streamlit as st
import requests

# Prompt Generator using Streamlit
# Inputs for avatar description
gender = st.text_input("Enter the gender of your character: ")
facial = st.text_input("Explain facial features of your avatar:")
hair = st.text_input("Hair description:")
body_type = st.text_input("Explain the body type:")
clothing = st.text_input("Explain the clothing:")
age = st.text_input("Enter the age/age-group:")
complexion = st.text_input("Describe the complexion of your character:")
ethnicity = st.text_input("Enter the ethnicity:")

# Create the prompt for the image generation
prompt = f"Generate an anime character based on the following description. Facial Description: {facial}, Hair Description: {hair}, Body-type: {body_type}, Clothing Description: {clothing}, Age: {age}, Complexion: {complexion}, Ethnicity: {ethnicity}"

def download_image(prompt):
    url = f"https://pollinations.ai/p/{prompt}"
    response = requests.get(url)
    with open('generated_image.jpg', 'wb') as file:
        file.write(response.content)
    print('Image downloaded!')

if st.button("Generate Image"):
    st.title("Generated Image")
    download_image(prompt)
    st.image('generated_image.jpg')