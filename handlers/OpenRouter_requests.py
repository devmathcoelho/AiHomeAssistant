import os
import httpx
import json
from dotenv import load_dotenv

load_dotenv()

async def AsyncOpenRouter(user_input: str) -> str:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENROUTER_API_KEY}"
    }
    payload = {
        "model": "google/gemma-3-27b-it:free",
        "messages": [
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": "Your response should be concise and informative. Always answer in the language used by the user. If the user greets you, greet them back warmly. If you don't know the answer, say 'I don't know'. Avoid unnecessary elaboration."}
        ],
        "max_tokens": 150
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url, 
            headers=headers, 
            data=json.dumps(payload),
            timeout=30.0
        )

    if response.status_code == 200:
        data = response.json()
        return data['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}"