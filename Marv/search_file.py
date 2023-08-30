import time
import sys
sys.path.append("/Users/silinmeng/Python_Projects/ChatBot")

import openai
import constants
openai.api_key = constants.API_KEY

request = input("What operation do you want to perform? (Search or Delete) \n")

response = openai.File.list()
if request == 'Search':
    print(response.data)
elif request == 'Delete':
    openai.File.delete("file-ujg9a35A4ut7oamIZaE2gI5e")
    # for file in response.data:
    #     openai.File.delete(file.id)