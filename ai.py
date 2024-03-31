import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

class Ai:

    def __init__(self):
        self.API_KEY = os.getenv("API_KEY")
        genai.configure(api_key = self.API_KEY)
        self.model = genai.GenerativeModel('gemini-pro-vision')
        self.prompt = """ You are an expert text summarizer, you will be shown an image with a lot of text on it, it will be a clear enough picture to read , you are to read the gtext from the input and tell the user a brief summary of strictly 60 words , you shall be penalised if you exceed 60 and unless any given input allows you to exceed 60, key points in the text , the content and any further trailing questions the user might have regarding the original text"""

    def get_summary(self, image, input):
        response = self.model.generate_content([input, image, self.prompt])
        return response.text


    


        