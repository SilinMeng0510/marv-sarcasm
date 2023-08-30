import sys
sys.path.append("/Users/silinmeng/Python_Projects/ChatBot")

import openai
import constants
openai.api_key = constants.API_KEY

response = openai.FineTuningJob.list()

for model in response['data']:
    print(model)
    print("------------------------------------------------------------------")
