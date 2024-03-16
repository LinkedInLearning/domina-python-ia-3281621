import openai

API_KEY = "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"


PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"

openai.api_key = API_KEY

response = openai.images.generate(
    prompt=PROMPT,
    n=1,
    size="256x256",
)

print(response["data"][0]["url"])
