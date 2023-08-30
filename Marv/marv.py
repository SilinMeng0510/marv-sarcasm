import sys
sys.path.append("/Users/silinmeng/Python_Projects/ChatBot")

import openai
import gradio
import constants

openai.api_key = constants.API_KEY

messages = [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "ft:gpt-3.5-turbo-0613:personal:marv-sacrastic-bot:7tN3xfYp",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Marv Pro")

demo.launch(share=True)