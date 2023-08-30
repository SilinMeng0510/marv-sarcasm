import sys
sys.path.append("/Users/silinmeng/Python_Projects/ChatBot")

import openai
import constants

openai.api_key = constants.API_KEY

completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)