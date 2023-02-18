# Comics VK

## Описание работы скрипта:
Скачивает с ресурса XKDS произвольный комикс и публикует его с комментарием в группе VK.


## Зависимости
Python3 должен быть уже установлен. Затем используйте pip 
(или pip3, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt

```
## Окружение

.env

```
GROUP_ID= 
ACCESS_TOKEN=

```
GROUP_ID - ID вашей группы VK

ACCESS_TOKEN - воспользуйтесь процедурой [Implicit Flow](https://vk.com/dev/implicit_flow_user) для 
получения ключа доступа пользователя

## Запуск скрипта в консоли
```
python main.py

```
