from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

# Try to read the OPENAI_API_KEY
api_key = os.getenv('OPENAI_API_KEY')

print("Environment variables loaded successfully!")
print(f"API Key found: {'Yes' if api_key else 'No'}")
print(f"API Key starts with: {api_key[:7]}..." if api_key else "No API key found") 