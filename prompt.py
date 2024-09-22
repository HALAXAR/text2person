import streamlit as st

def page_two():
    st.write("## Character Description")

    # Input fields for character description
    gender = st.text_input("Enter the gender of your character:")
    facial = st.text_input("Explain facial features of your avatar:")
    hair = st.text_input("Hair description:")
    body_type = st.text_input("Explain the body type:")
    clothing = st.text_input("Explain the clothing:")
    age = st.text_input("Enter the age/age-group:")
    complexion = st.text_input("Describe the complexion of your character:")
    ethnicity = st.text_input("Enter the ethnicity:")

    if st.button("Next"):
        if not gender or not facial or not hair or not body_type or not clothing or not age or not complexion or not ethnicity:
            st.warning("Please fill all the fields before proceeding.")
        else:
            st.session_state.prompt = (f"Generate an anime character based on the following description. "
                                       f"Gender: {gender}, Facial Description: {facial}, Hair Description: {hair}, "
                                       f"Body Type: {body_type}, Clothing: {clothing}, Age: {age}, "
                                       f"Complexion: {complexion}, Ethnicity: {ethnicity}")
            st.session_state.page = 3  