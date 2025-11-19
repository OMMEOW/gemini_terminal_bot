import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat()

print("Chat started")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("Gemini: ", response.text)
    response = chat.send_message(user_input)
    print("Gemini: ", response.text)