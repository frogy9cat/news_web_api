# News web API
Этот проект разработан на Python с использованием Django REST Framework.

## Описание
Проект поддерживает методы API:
  - **GET**: получение данных
  - **POST**: создание записей
  - **RETRIEVE**: получение одной записи
  - **UPDATE**: обновление записи
  - **DELETE**: удаление записи

Для работы с новостями предусмотрена фильтрация по дате. Чтобы отфильтровать новости по диапазону дат, укажите начальную и конечную дату в URL (в формате `.../YYYYMMDD-YYYYMMDD`).

---
## Использование
#### 1. Клонирование репозитория:
  ```bash
  git clone https://github.com/frogy9cat/news_web_api.git
  ```
#### 2. Создание виртуального окружения и установка зависимостей:
  ```bash
  python -m venv venv
  source env/bin/activate  # Для Linux/Mac
  .\venv\Scripts\activate  # Для Windows
  pip install -r requirements.txt
  ```
#### 3. Настройка переменных окружения:
  - **Заполните `.env` файл необходимыми значениями переменных окружения, включая (`BOT_TOKEN`) для интеграции с [Telegram-ботом](https://github.com/frogy9cat/news-bot).**
#### 4. Запуск сервера:
  ```bash
  python manage.py runserver 0.0.0.0:8000
  ```
API будет доступно по адресу `http://127.0.0.1:8000/`.

## Интеграция с Telegram ботом
В `.env` файле укажите токен вашего Telegram-бота (`BOT_TOKEN`). Этот бот будет отправлять уведомления при создании новой новости. Telegram-юзеров можно добавлять в базу данных через API. Также, [Telegram-бот](https://github.com/frogy9cat/news-bot) автоматически отправляет `post` запрос в базу данных через API для создания нового пользователя после того, как пользователь Телеграм отправит боту команду `/start`.

---
## Дальнейшие планы
  - **Расширение функционала**: Добавление новых возможностей для взаимодействия с базой данных через API.
  - **Авторизация**: Введение системы авторизации для обеспечения безопасности доступа к данным.
  - **Оптимизация**: Улучшение производительности приложения и снижение нагрузки на базу данных.
