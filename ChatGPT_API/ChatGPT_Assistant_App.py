import openai
import gradio

openai.api_key = "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"

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