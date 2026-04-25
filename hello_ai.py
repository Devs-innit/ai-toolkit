import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI(base_url="https://openrouter.ai/api/v1",api_key=os.getenv("OPENROUTER_API_KEY"))
question = input("Ask me anything: ")
response = client.chat.completions.create(model="mistralai/mistral-small-3.1-24b-instruct",messages=[{"role": "system", "content": "You are a helpful codig assistantfor beginner developers.Keep answers simple, friendly and easy to understand."},{"role":"user","content": question}])
print(response.choices[0].message.content)

