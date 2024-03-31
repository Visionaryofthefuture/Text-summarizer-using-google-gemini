
import streamlit as st
import PIL
from ai import Ai

Gemini = Ai()
st.title("Image Summarizer App")

text_input = st.text_input("Enter your prompt:")


image_file = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])


def print_response():
    if image_file is not None:
        img = PIL.Image.open(image_file)
        st.image(image_file, width=400)

    if image_file and text_input: 
        response = Gemini.get_summary(image=img, input=text_input)
        if response:  
            st.markdown("**Text Summary:**")
            st.write(response)  
        else:
            st.write("Error: Could not generate summary.") 
    else:
        st.write("Please upload an image and enter some text to proceed.")

if st.button("Click Me to get response"):
    print_response()