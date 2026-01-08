from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

# Load environment variables from .env file (including GEMINI_API_KEY)
load_dotenv()
# gemini_key = os.getenv("GEMINI_API_KEY"))

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", 
    #config=types.GenerateContentConfig(system_instruction="You are a cat. Your name is Neko."),    
    contents="Explain how AI works in a few words",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    )
)
print(response.text)
# Expected output (example):
# "AI works by using algorithms and data to mimic human intelligence, enabling machines to learn, reason, and make decisions."
