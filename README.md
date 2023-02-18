# Space

## Описание работы скрипта:
Скачивает с ресурса NASA и SpaceX фотографии, связанные с космической тематикой, 
а также загружает скаченные фото (в произвольном порядке) в Telegram канал с установленным интервалом времени.

## Получение ID для скачивания фото с ресурса SpaceX

[Документация: получить фотографии запуска по id](https://github.com/r-spacex/SpaceX-API/blob/master/docs/launches/v5/one.md)


## Зависимости
Python3 должен быть уже установлен. Затем используйте pip 
(или pip3, есть есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```
## Окружение
.env

[API key авторизации NASA](https://api.nasa.gov) 
```
NASA_TOKEN=BqnssG5NGr0h61pd0zCkeLQJIBJgd5cX9rAtHMDt
TELEGRAM_TOKEN= (токен телеграм bot)
TELEGRAM_CHAT_ID= (ID канала)
```
## Запуск скрипта в консоли
```
python3 fetch_spacex_images.py 5eb87d47ffd86e000604b38a
# (номер ID, по умолчанию 5eb87d19ffd86e000604b366)

python3 fetch_nasa_apod_images.py 13
# (количество случайных фото, по умолчанию 10)

python3 fetch_nasa_epic_images.py

python3 telegram_bot.py 60
# (время задержки в секундах, по умолчанию 4 часа) 
Запускается бесконечный цикл, выход из цикла: Control + C
```
