import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  
api_key = os.getenv("OPENAI_API_KEY")
openai_model = 'gpt-4o-mini' 
client = OpenAI(api_key = api_key)

job_id = "ftjob-Me8Bu7jvOSIMuhkuCJFyYAYz" # <----------- Copy your Job ID here

job = client.fine_tuning.jobs.retrieve(job_id)

print("Status:", job.status)
# Status Results:
# - validating_files: The dataset is being checked for format and content issues.
# - queued: The job is waiting in line to start fine-tuning.
# - running: The fine-tuning job is actively in progress.
# - succeeded: The job completed successfully, and your model is ready to use!
# - failed: The job encountered an error and did not complete.
# - cancelled: The job was cancelled (manually or automatically).

print("Fine-tuned model:", job.fine_tuned_model) # <------- Find your Model ID here