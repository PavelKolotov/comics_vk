import os
import requests
import urllib.error
import urllib.parse

from pathlib import Path
from environs import Env


env = Env()
env.read_env()

grup_id = env('group_id')

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

def get_server():
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {
        'group_id': env('group_id'),
        'access_token': env('access_token'),
        'v': 5.131
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    server = response.json()['response']['upload_url']
    return server

server = get_server()
def get_loading_img():
    with open('images/comics_1.jpg', 'rb') as file:
        url = server
        files = {
            'photo': file
        }
        response = requests.post(url, files=files)
        response.raise_for_status()
        return response.json()

loading_img = get_loading_img()

photo_img = loading_img['photo']
server_img = loading_img['server']
hash_img = loading_img['hash']


def get_save_wall():
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = {
        'group_id': env('group_id'),
        'access_token': env('access_token'),
        'photo': photo_img,
        'server': server_img,
        'hash': hash_img,
        'v': 5.131
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json()

owner_id = get_save_wall()['response'][0]['owner_id']
media_id = get_save_wall()['response'][0]['id']

def get_wall_post():
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'owner_id': f'-{grup_id}',
        'access_token': env('access_token'),
        'from_group': 1,
        'attachments': f'photo{owner_id}_{media_id}',
        'message': "Don't we all.",
        'v': 5.131
    }

    response = requests.post(url, params=params)
    response.raise_for_status()


get_wall_post()


