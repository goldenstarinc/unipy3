# unipy3

Проект **unipy3** — веб-приложение на Django, предназначенное для игры в шахматы

## Содержание

- `chess_site/` — приложение Django, отвечает за веб-интерфейс  
- `chessboard/` — библиотека / модуль для логики шахмат / доски  
- `manage.py` — стандартный скрипт Django  
- `requirements.txt` — список зависимостей  
- `Dockerfile` & `docker-compose.yml` — для запуска в контейнерах Docker  
- `db.sqlite3` — тестовая / dev-база данных (SQLite)  

## Быстрый старт

### Локально (без Docker)

1. Склонируйте репозиторий:  
   ```bash
   git clone https://github.com/goldenstarinc/unipy3.git
   cd unipy3
2. Создайте виртуальное окружение и установите зависимости:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
3. Примените миграции и запустите сервер:
  ```bash    
  python manage.py migrate
  python manage.py runserver
  ```
4. Перейдите в браузере по адресу http://127.0.0.1:8000/

### С Docker
1. Убедитесь, что установлен Docker и docker-compose.
2. Запустите:
  ```bash
  docker-compose up --build
  ```
3. Сервер будет доступен по адресу, указанному в docker-compose.yml

## Зависимости

Список зависимостей указан в requirements.txt. (Добавь сюда несколько ключевых библиотек и версии, если нужно)

## Структура проекта

|Директория|Отвечает за|
|:---------|:----------|
|chess_site/|Django-приложение, веб-интерфейс|
|chessboard/|Модуль логики шахматной доски / шахматной игры|
|Dockerfile|Инструкция для контейнера приложения|
|docker-compose.yml|Определяет сервисы (web / БД / др.)|
|db.sqlite3|Локальная база данных для разработки|

