import os
from dotenv import load_dotenv
from llama_index.llms.gemini import Gemini
import google.generativeai as genai


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key = GOOGLE_API_KEY)

def load_model():
    
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
    try:
        model = Gemini(models='gemini-pro',api_key=GOOGLE_API_KEY)
        return model
    except Exception as e:
        print(e)
        