import streamlit as st

def page_three():
    st.write("## Image Settings")

    models = ["flux", "flux-realism", "flux-anime", "flux-3d", "any-dark", "turbo"]
    model_selected = st.selectbox("Select a model", options=models)

    width = st.number_input("Enter width", min_value=256, max_value=2048, value=1024)
    height = st.number_input("Enter height", min_value=256, max_value=2048, value=1024)
    
    enhance_options = [True, False]
    enhance = st.selectbox("Do you want to enhance the prompt?", options=enhance_options)
    
    prompt = st.session_state.prompt

    st.session_state.url = (f"https://image.pollinations.ai/prompt/{prompt}?model={model_selected}&width={width}&height={height}&nologo=true&enhance={enhance}")

    if st.button("Next"):
        st.session_state.page = 4