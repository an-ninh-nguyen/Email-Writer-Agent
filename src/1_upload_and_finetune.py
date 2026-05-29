# Creating and using a fine-tuned model

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  
api_key = os.getenv("OPENAI_API_KEY")
#openai_model = 'gpt-4o-mini' 
openai_model =  "gpt-4o-mini-2024-07-18"
client = OpenAI(api_key = api_key)

fine_tune_data_file = "fine_tuning_facts.jsonl"

with open(fine_tune_data_file, "rb") as f:
    uploaded_file = client.files.create(
        file=f,
        purpose="fine-tune"
    )

print("Uploaded file ID:", uploaded_file.id)


fine_tune_job = client.fine_tuning.jobs.create(
    training_file=uploaded_file.id,
    model=openai_model
)

print("Fine-tuning job ID:", fine_tune_job.id) # <----------- Find your Job ID here
