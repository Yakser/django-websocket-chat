# Soft -  django websocket chat

# Установка и запуск

Клонируйте репозиторий
```bash
git clone https://github.com/Yakser/django-websocket-chat
```
Перед установкой зависимостей необходимо скачать [C++ Build Tools](https://stackoverflow.com/questions/40504552/how-to-install-visual-c-build-tools) Они нужны для сборки некоторых библиотек.

# Установка зависимостей

В папке проекта (`/django-websocket-chat/`) выполните команду:
```
pip install -r requirements.txt
```

#  Redis

## Linux/Mac OS

Скачайте [Redis](https://redis.io)
И запустите его:
```bash
sudo service redis-server start
```

## Windows
- Установите [WSL2](https://docs.microsoft.com/ru-ru/windows/wsl/install)
- В WSL установите  `redis-server`:

```bash
sudo apt-add-repository ppa:redislabs/redis
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install redis-server
```

Запустите `redis-sever`:
```bash
sudo service redis-server start
```

# Запуск 
Сделайте и заполните файл `.env` в соответствии с `.env.example`

Перейдите в директорию django-проекта:
```shell
cd chat
```

Запустите приложение командой

```shell
python manage.py runserver
```

# Технические детали
- Python 3.10.4 
- Django 3.2.13
- БД: SQLite
- Библиотека для работы с вебсокетами: channels 3.0.4 
- CSS препроцессор: SCSS
