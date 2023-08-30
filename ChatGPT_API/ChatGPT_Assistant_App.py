import sys
sys.path.append("/Users/silinmeng/Python_Projects/ChatBot")

import openai
import gradio
import constants

openai.api_key = constants.API_KEY

messages = [{"role": "system", "content": "You are a financial experts that specializes in stock and long_term investment"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Stock Investment Pro")

demo.launch(share=True)