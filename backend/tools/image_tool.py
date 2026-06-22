import os
import requests
from dotenv import load_dotenv

load_dotenv()
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")


def get_image(query):

    url = "https://api.pexels.com/v1/search"

    headers = {"Authorization": PEXELS_API_KEY}

    params = {"query": query,"per_page": 1}

    response = requests.get(url,headers=headers,params=params)

    data = response.json()
    print(response.status_code)
    photos = data.get("photos", [])

    if photos:
        return photos[0]["src"]["large"]

    return None