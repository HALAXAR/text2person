import streamlit as st
import torch
from torch.cuda.amp import autocast
from diffusers import StableDiffusionPipeline
from auth_key import AUTHORIZATION_KEY
from PIL import Image

# Prompt Generator using Streamlit
# Inputs for avatar description
facial = st.text_input("Explain facial features of your avatar:")
hair = st.text_input("Hair description:")
body_type = st.text_input("Explain the body type:")
clothing = st.text_input("Explain the clothing:")
age = st.text_input("Enter the age/age-group:")
complexion = st.text_input("Describe the complexion of your character:")
ethnicity = st.text_input("Enter the ethnicity:")

# Create the prompt for the image generation
prompt = f"Generate an anime character based on the following description. Facial Description: {facial}, Hair Description: {hair}, Body-type: {body_type}, Clothing Description: {clothing}, Age: {age}, Complexion: {complexion}, Ethnicity: {ethnicity}"

# Function to generate the image using Stable Diffusion
def generate_image(pipe, device):
    # Use autocast only if device is cuda
    if device == "cuda":
        with autocast():
            image = pipe(prompt, guidance_scale=8.5).images[0]
    else:
        # No autocast for CPU, just run the pipeline
        image = pipe(prompt, guidance_scale=8.5).images[0]
    return image

if st.button("Generate Image"):
    st.title("Generated Image")
    try:
        # Setup model for Stable Diffusion
        modelid = "CompVis/stable-diffusion-v1-4"
        device = "cuda" if torch.cuda.is_available() else "cpu"  # Check if CUDA is available
        # Load the model with half-precision if using CUDA
        pipe = StableDiffusionPipeline.from_pretrained(
            modelid, 
            revision="fp16" if device == "cuda" else None, 
            torch_dtype=torch.float16 if device == "cuda" else torch.float32, 
            use_auth_token=AUTHORIZATION_KEY
        )
        pipe.to(device)  # Move model to device

        # Generate the image
        image = generate_image(pipe, device)

        # Display the image using Streamlit
        st.image(image)
    except Exception as e:
        st.write("Error:", e)
        print(e)
