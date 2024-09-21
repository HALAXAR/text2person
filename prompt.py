import streamlit as st

def page_two():
    st.set_page_config(page_title="Character Description")
    
    gender = st.text_input("Enter the gender of your character: ")
    facial = st.text_input("Explain facial features of your avatar:")
    hair = st.text_input("Hair description:")
    body_type = st.text_input("Explain the body type:")
    clothing = st.text_input("Explain the clothing:")
    age = st.text_input("Enter the age/age-group:")
    complexion = st.text_input("Describe the complexion of your character:")
    ethnicity = st.text_input("Enter the ethnicity:")

    # Create the prompt for the image generation
    st.session_state.prompt = f"Generate an anime character based on the following description.Gender Description:{gender}, Facial Description: {facial}, Hair Description: {hair}, Body-type: {body_type}, Clothing Description: {clothing}, Age: {age}, Complexion: {complexion}, Ethnicity: {ethnicity}"
    
    if st.button("Next"):
        st.session_state.page=3
        
        
    