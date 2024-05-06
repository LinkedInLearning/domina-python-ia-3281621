from openai import OpenAI

API_KEY = ""
CLIENT = OpenAI(
    api_key=API_KEY
)

response = CLIENT.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "How do I output all files in a directory using Python?"}
    ]
)

print(response.choices[0].message.content)
