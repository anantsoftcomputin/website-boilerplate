# chatbot/api.py

import requests
from django.conf import settings

def chat_with_gpt3(prompt):
    endpoint = "https://api.openai.com/v1/engines/davinci/completions"  # or whichever endpoint you're using
    headers = {
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 1500
    }
    response = requests.post(endpoint, headers=headers, json=data)
    response_data = response.json()

    return response_data.get("choices")[0].get("text").split("Q:")[0]
