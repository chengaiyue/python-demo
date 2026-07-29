import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(   
    # The base URL for model invocation
    base_url="https://ark.cn-beijing.volces.com/api/plan/v3",   
    # Replace with your API Key
    api_key=os.environ.get('ARK_API_KEY'), 
)

completion = client.chat.completions.create(
    # Replace with Model ID
    model="doubao-seed-2.0-lite", 
    messages = [
        {"role": "user", "content": "你是谁"},
    ],
)
print(completion.choices[0].message.content)