from openai_setup import openai

def test_openai_connection():
    try:
        # Make a simple API call
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Hello, testing!' if you can hear me."}],
            max_tokens=20
        )
        
        # Print the response
        print("API Response:", response.choices[0].message.content)
        print("\nConnection test successful! ✅")
        
    except Exception as e:
        print("Error occurred:", str(e))
        print("\nConnection test failed! ❌")

if __name__ == "__main__":
    print("Testing OpenAI API connection...")
    test_openai_connection() 