import os
import google.generativeai as genai
import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

st.title("Image reader using Gemini-1.5-flash")

genai.configure(api_key='AIzaSyCU770U3gz6l73BEac8B79XhrSvqVj9fyQ')
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 200
}

model = genai.GenerativeModel('gemini-1.5-flash', generation_config=generation_config)
uploaded_file = st.file_uploader("Upload an image to read the content of it...", type=["jpeg"])

if uploaded_file is not None:
    image_data = uploaded_file.read()

    image_part = {
        "mime_type": "image/jpeg",
        "data": image_data
    }

    prompt_part = [
        "Describe the image\n",
        image_part
    ]

    if st.button("Submit"):
        generated_content = model.generate_content(prompt_part)
        st.write(generated_content.text)











