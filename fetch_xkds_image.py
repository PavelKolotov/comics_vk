import os
import requests
import random
import urllib.parse


from pathlib import Path


def download_img(img_url, images_path):
    Path('images').mkdir(parents=True, exist_ok=True)
    response = requests.get(img_url)
    response.raise_for_status()

    with open(f'{images_path}', 'wb') as file:
        file.write(response.content)


def separate_extension(link):
    url_encoding = urllib.parse.unquote(link)
    url_parse = urllib.parse.urlsplit(url_encoding)
    filename = os.path.split(url_parse.path)[1]
    return filename


def fetch_xkds_comics():
    num = random.randint(1, 2739)
    if num == 404:
        num = 405
    url = f'https://xkcd.com/{num}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()

    comic_link = response.json()
    img_link = comic_link['img']
    comment_comic = comic_link['alt']
    filename = separate_extension(img_link)
    img_path = f'./images/{filename}'
    download_img(img_link, img_path)
    return comment_comic

