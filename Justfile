set dotenv-load

install:
    uv sync

run:
    uv run python manage.py runserver

migrate:
    uv run python manage.py migrate

makemigrations:
    uv run python manage.py makemigrations
