import os
import requests
import random
import urllib.parse



def download_img(img_url, images_path):
    response = requests.get(img_url)
    response.raise_for_status()

    with open(f'{images_path}', 'wb') as file:
        file.write(response.content)



def separate_extension(link):
    encoded_url = urllib.parse.unquote(link)
    parsed_url = urllib.parse.urlsplit(encoded_url)
    filename = os.path.split(parsed_url.path)[1]
    return filename


def fetch_random_comic():
    total_number_comics = 2739
    num = random.randint(1, total_number_comics)
    if num == 404:
        num = 405
    url = f'https://xkcd.com/{num}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


