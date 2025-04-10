📷 Image Uploader (Django + Vue.js)
Проект для загрузки и управления изображениями 
с API на Django и фронтендом на Vue.js.

Работа выполнена в ОС Windows 
в редакторе кода VS Code и команды написаны под них.

🚀 Запуск проекта.
1. Клонируйте репозиторий GIT командой:
git clone git@github.com:AlexandrShmidt/push_images.git

2. Перейдите  в директорию проекта в папку бэкенда:
cd ... push_images/backend_image

⚙️ Настройка бэкенда (Django)
1. Создайте виртуальное окружение (Windows):
cd applications/image_api
python -m venv venv
2. Активируйте окружение:
.\venv\Scripts\activate
либо
source/venv/Scripts/activate
3. Установите зависимости:
pip install -r requirements.txt
4. Примените миграции:
python manage.py migrate
5. Запустите сервер:
python manage.py runserver

💻 Настройка фронтенда (Vue.js)
1. Установите Node.js
Скачайте с официального сайта (версия LTS)

2. Установите зависимости
cd ../image_frontend
npm install
3. Запустите сервер разработки
npm run serve
Фронтенд будет доступен по адресу: http://localhost:8080

🌐 Использование
Откройте http://localhost:8080 в браузере

Загружайте изображения через форму

Просматривайте и удаляйте их из списка

📁 Структура проекта
Copy
.
├── image_api/          # Django-проект
│   ├── venv/          # Виртуальное окружение (игнорируется)
│   ├── requirements.txt # Зависимости Python
│   └── ...
├── image_frontend/     # Vue-проект
│   ├── node_modules/  # Зависимости JS (игнорируются)
│   └── ...
└── README.md          # Этот файл

📦 Зависимости
Бэкенд: Django 4.2+, DRF 3.14+

Фронтенд: Vue 3, Axios

База данных: SQLite (по умолчанию)