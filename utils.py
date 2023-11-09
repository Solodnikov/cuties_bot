import requests
from constants import CATS_API_URL, DOGS_API_URL, FOXES_API_URL


def get_cat_photo_url(source_url=CATS_API_URL):
    response = requests.get(source_url)
    if response.status_code == 200:
        return response.json()[0]['url']


def get_dog_photo_url(source_url=DOGS_API_URL):
    response = requests.get(source_url)
    if response.status_code == 200:
        return response.json()['url']


def get_fox_photo_url(source_url=FOXES_API_URL):
    response = requests.get(source_url)
    if response.status_code == 200:
        return response.json()['image']