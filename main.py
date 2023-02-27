import shutil


from fetch_xkds_image import fetch_random_comic, separate_extension, download_img
from send_wall_post_vk import get_wall_upload_server, upload_image, save_wall_photo, send_wall_post
from environs import Env
from pathlib import Path


def main():
    env = Env()
    env.read_env()

    Path('images').mkdir(parents=True, exist_ok=True)

    vk_group_id = env('VK_GROUP_ID')
    vk_token = env('VK_ACCESS_TOKEN')

    comic_link = fetch_random_comic()
    
    img_link = comic_link['img']
    comic_comment = comic_link['alt']
    filename = separate_extension(img_link)
    img_path = f'./images/{filename}'

    download_img(img_link, img_path)

    server_link = get_wall_upload_server(vk_group_id, vk_token)

    img_link = upload_image(server_link, filename)

    photo_param = img_link['photo']
    server_param = img_link['server']
    hash_param = img_link['hash']

    photo_link = save_wall_photo(vk_group_id, vk_token, photo_param, server_param, hash_param)

    owner_id = photo_link['response'][0]['owner_id']
    media_id = photo_link['response'][0]['id']

    send_wall_post(vk_group_id, vk_token, owner_id, media_id, comic_comment)

    shutil.rmtree('images')


if __name__ == '__main__':
    main()
