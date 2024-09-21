import requests
import json
import streamlit as st

api_key=st.text_input("Enter your api key: ")

facial = st.text_input("Explain facial features of your avatar:")
hair = st.text_input("Hair description:")
body_type = st.text_input("Explain the body type:")
clothing = st.text_input("Explain the clothing:")
age = st.text_input("Enter the age/age-group:")
complexion = st.text_input("Describe the complexion of your character:")
ethnicity = st.text_input("Enter the ethnicity:")

# Create the prompt for the image generation
prompt = f"Generate an anime character based on the following description. Facial Description: {facial}, Hair Description: {hair}, Body-type: {body_type}, Clothing Description: {clothing}, Age: {age}, Complexion: {complexion}, Ethnicity: {ethnicity}"


url = "https://modelslab.com/api/v6/images/text2img"

payload = json.dumps({
  "key": api_key,
  "model_id": "midjourney",
  "prompt": prompt,
  "negative_prompt": "",
  "width": "512",
  "height": "512",
  "samples": "1",
  "num_inference_steps": "30",
  "safety_checker": "no",
  "enhance_prompt": "yes",
  "seed": None,
  "guidance_scale": 7.5,
  "panorama": "no",
  "self_attention": "no",
  "upscale": "no",
  "embeddings_model": None,
  "lora_model": None,
  "tomesd": "yes",
  "use_karras_sigmas": "yes",
  "vae": None,
  "lora_strength": None,
  "scheduler": "DDPMScheduler",
  "webhook": None,
  "track_id": None
})

headers = {
  'Content-Type': 'application/json'
}
if st.button("Generate Image"):
    st.title("Generated Image")
    response = requests.request("POST", url, headers=headers, data=payload)

    response=response.text
    print(response)
    data = json.loads(response)

    # Access the "output" field
    output_links = data["output"]

    # Check if the "output" array has at least one link
    if output_links:
        first_link = output_links[0]
        print("First Output Link:", first_link)
    else:
        print("No links found in 'output'.")

    def download_image(url, filename):
      response = requests.get(url)

    # Check if the request was successful (status code 200)
      if response.status_code == 200:
      # Open a file in write-binary mode and save the content
        with open(filename, 'wb') as file:
          file.write(response.content)
          print(f"Image successfully downloaded: {filename}")
      else:
        print(f"Failed to retrieve image. Status code: {response.status_code}")

    # Example usage
    filename = "downloaded_image.jpg"  # The name to save the image as

    download_image(first_link, filename)
    st.image('downloaded_image.jpg')