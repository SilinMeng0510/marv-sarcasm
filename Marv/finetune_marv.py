import time
import sys
sys.path.append("/Users/silinmeng/Python_Projects/ChatBot")

import openai
import constants
openai.api_key = constants.API_KEY

# Upload the dataset
file_response = openai.File.create(
    file=open("FineTuned_ChatGPT/marv.jsonl", "rb"),
    purpose="fine-tune"
)
file_id = file_response['id']
while file_response['status'] != "processed":
    time.sleep(3)
    file_response = openai.File.retrieve(file_id)
print(f"File ID: {file_id} \n")

# Start fine-tuning
tuning_response = openai.FineTuningJob.create(
    training_file=file_id,
    model="gpt-3.5-turbo", 
    suffix="marv_sacrastic_bot"
)
tuning_id = tuning_response['id']

# Monitor Progress
status_response = openai.FineTuningJob.retrieve(
    tuning_id
)
status = status_response['status']
print(f"Fine-tuning status: {status}")


