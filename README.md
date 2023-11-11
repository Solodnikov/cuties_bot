# cuties_bot

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Static Badge](https://img.shields.io/badge/aiogram-3.1.1.-greene)

### Описание проекта
Телеграм бот. Позволяет получать картинки собачек, кошечек и лисичек при вызове из клавиатуры.

Пример развернутого доступен в телеграме: 
`@FurryFriendsPhotoBot`


### Развертывание проекта

* клонируйте проект

   `https://github.com/Solodnikov/cuties_bot.git`

* установите и запустите виртуальное окружение в папке проекта

    `python -m venv venv`

    `. venv/Scripts/activate`

* установите зависимости проекта

    `pip install -r requirements.txt`

### Запуск проекта

* создайте файл `.env` в корневой директории проекта:
    
    ```
    BOT_TOKEN='<ваш токен для бота>'
    ```
* запустить бота из корневой директории проекта
    
    `python bot.py`