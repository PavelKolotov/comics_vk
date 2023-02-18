import os
import requests
import urllib.error
import urllib.parse

from pathlib import Path


def download_img(img_url, images_path):
    Path('images').mkdir(parents=True, exist_ok=True)
    response = requests.get(img_url)
    response.raise_for_status()

    with open(f'{images_path}', 'wb') as file:
        file.write(response.content)

\
def separate_extension(link):
    url_encoding = urllib.parse.unquote(link)
    url_parse = urllib.parse.urlsplit(url_encoding)
    filename = os.path.split(url_parse.path)[1]
    filename_ext = os.path.splitext(filename)[1]
    return filename_ext


def fetch_xkds_comics():
    num = 1
    while True:
        try:
            url = f'https://xkcd.com/{num}/info.0.json'

            if num == 404:
                num = 405
                continue

            response = requests.get(url)
            response.raise_for_status()
            comic_link = response.json()
            img_link = comic_link['img']
            comment_comic = comic_link['alt']
            filename_ext = separate_extension(img_link)
            img_path = f'./images/comics_{num}{filename_ext}'
            # download_img(img_link, img_path)
            num += 1
            print(comment_comic)

        except urllib.error.HTTPError:
            print('картинки закончились')
            break


fetch_xkds_comics()