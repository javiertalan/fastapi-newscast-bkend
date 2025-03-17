from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Verify the API key is loaded (optional)
if openai.api_key is None:
    raise ValueError("OpenAI API key not found in environment variables") 