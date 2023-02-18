import os
import requests


def get_wall_upload_server(vk_grup_id, vk_token):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {
        'group_id': vk_grup_id,
        'access_token': vk_token,
        'v': 5.131
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    server_link = response.json()['response']['upload_url']
    return server_link


def upload_image(server_link):
    images = os.walk('images')
    for img in images:
        img_name = img[2][0]

        with open(f'images/{img_name}', 'rb') as file:
            url = server_link
            files = {
                'photo': file
            }
            response = requests.post(url, files=files)
            response.raise_for_status()
            os.remove(f'images/{img_name}')
            return response.json()


def save_wall_photo(vk_grup_id, vk_token, photo_param, server_param, hash_param):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = {
        'group_id': vk_grup_id,
        'access_token': vk_token,
        'photo': photo_param,
        'server': server_param,
        'hash': hash_param,
        'v': 5.131
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json()


def send_wall_post(vk_grup_id, vk_token, owner_id, media_id, message):
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'owner_id': f'-{vk_grup_id}',
        'access_token': vk_token,
        'from_group': 1,
        'attachments': f'photo{owner_id}_{media_id}',
        'message': message,
        'v': 5.131
    }

    response = requests.post(url, params=params)
    response.raise_for_status()
