# QA API Service

## Запуск проекта

1. Клонируйте репозиторий из GitHub c помощью команды:

    git clone <ссылка на репозиторий>

2. Убедитесь, что у Вас установлен Docker и Docker Compose.
3. Установите зависимости из файла requirements.txt с помощью команды:

    pip install -r requirements.txt

4. Создайте базу данных в PostgreSQL, внесите данные по ней в файлы settings.py 
и docker-compose.yml, а потом сделайте миграции и подключите их к созданной вами в PostgreSQL 
базе данных с помощью следующих команд:

    docker-compose run web python3 manage.py makemigrations
    docker-compose run web python3 manage.py migrate

5. Запустите проект:
   docker-compose up

    API будет доступен по адресу: http://localhost:8000/api/