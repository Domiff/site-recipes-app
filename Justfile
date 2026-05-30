set dotenv-load

install:
    uv sync

run:
    uv run python manage.py runserver

migrate:
    uv run python manage.py migrate

makemigrations:
    uv run python manage.py makemigrations

lint:
    uv run ruff check .

format:
    uv run ruff format .

lint-fix:
    uv run ruff check --fix .

pre-commit:
    uv run pre-commit run --all-files

setup-hooks:
    uv run pre-commit install

test:
    uv run python manage.py test
