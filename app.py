import streamlit as st
import requests
from PIL import Image
import io

st.title("Image Captioning and Classification")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Call the FastAPI endpoint
    response = requests.post("https://3c8b-35-201-133-2.ngrok-free.app", files={"file": uploaded_file})

    if response.status_code == 200:
        result = response.json()
        st.write("Predicted Caption: ", result['predicted_caption'])
        st.write("Predicted Category: ", result['predicted_category'])
    else:
        st.write("Error: ", response.text)
