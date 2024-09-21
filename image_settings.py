import streamlit as st

def page_three():
    st.set_page_config(
        page_title = "Image Settings"
    )

    prompt = st.session_state.prompt
    models = ["flux","flux-realism","flux-anime","flux-3d","any-dark","turbo"]
    model_selected = st.selectbox("Select a model",options=models)
    width = 1024
    height = 1024
    enhance_options = [True,False]
    enhance = st.selectbox("Do you want to enhance the promot", options=enhance_options)

    st.session_state.url = f"https://image.pollinations.ai/prompt/{prompt}?model={model_selected}&width={width}&height={height}&nologo=true&enhance={enhance}"
    