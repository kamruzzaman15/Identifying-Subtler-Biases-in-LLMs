import requests

def generate_response_local(model: str, query: str) -> str:
    url = "http://localhost:11434/api/chat"
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ],
        "stream": False,
        "options": {
            "temperature": 0,
            "max_tokens": 50
        }
    }

    response = requests.post(url, json=data)
    return response.json()['message']['content']