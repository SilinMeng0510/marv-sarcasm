import sys
sys.path.append("/Users/silinmeng/Python_Projects/ChatBot")

import openai
import constants

openai.api_key = constants.API_KEY

messages = []
system_msg = input("What Type Of Chatbot Would You Like To Create?\n")
messages.append({"role": "system", "content": system_msg})

print(f"Your New Assistant {system_msg} Is Ready! \n")
message = ""
while message != "quit()":
    message = input("User: ")
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\nBot: " + reply + "\n")