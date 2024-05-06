import requests
import matplotlib.pyplot as plt

from io import BytesIO
from openai import OpenAI, OpenAIError
from PIL import Image, ImageDraw

API_KEY = "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"
CLIENT = OpenAI(
    api_key=API_KEY
)


def create_empty_image(error_msg):
    empty_img = Image.new("RGB", (300, 300))
    Im = ImageDraw.Draw(empty_img)
    Im.text((15, 15), error_msg, (255, 0, 0))
    return empty_img


def generate_image(prompt):

    try:
        response = CLIENT.images.generate(
            prompt=prompt,
            n=1,
            size="256x256"
        )
        image_url = response.data[0].url

        img_response = requests.get(image_url)
        img = Image.open(BytesIO(img_response.content))
        return img
    except OpenAIError as e:
        print(e)
        empty_img = create_empty_image(error_msg="Error en OpenAI")
        return empty_img
    except Exception as e:
        print(e)
        empty_img = create_empty_image(error_msg="Error en el proceso")
        return empty_img


generate_prompt = "Mono celebrando su cumpleaños"
image = generate_image(prompt=generate_prompt)

plt.imshow(image)
plt.show()
