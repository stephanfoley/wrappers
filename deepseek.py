import os
from openai import OpenAI

system = '''
   Keep replies under 400 words unless otherwise needed
   Act professional
   Discuss projects in high level first
   Only provide code when asked
   Do not provide excessive code, start step-by-step
'''

client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

system_prompt = "please keep replies under 400 words"

def d(msg):
    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": msg},
        ],
        stream=False
    )

    print(response.choices[0].message.content)
