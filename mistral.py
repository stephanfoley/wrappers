t os
import requests
import json

class MistralChat:
    def __init__(self, api_key=None, model="mistral-medium"):
        self.api_key = api_key or os.getenv("MISTRAL_API_KEY")
        if not self.api_key:
            raise ValueError("Please set MISTRAL_API_KEY in your environment variables or pass it to the constructor.")
        self.model = model
        self.history = []

    def chat(self, user_message):
        self.history.append({"role": "user", "content": user_message})

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": self.history
        }

        response = requests.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers=headers,
            data=json.dumps(data)
        )

        if response.status_code != 200:
            raise Exception(f"API request failed: {response.text}")

        response_data = response.json()
        assistant_message = response_data["choices"][0]["message"]["content"]
        self.history.append({"role": "assistant", "content": assistant_message})

        return assistant_message

    def clear_history(self):
        self.history = []

# Example usage in IPython:
# chat = MistralChat()
# print(chat.chat("Hello, who are you?"))
# print(chat.chat("What did I just ask?"))
