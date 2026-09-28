set dotenv-load

install:
    uv sync

run:
    uv run python backend/manage.py runserver

migrate:
    uv run python backend/manage.py migrate

makemigrations:
    uv run python backend/manage.py makemigrations

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
    cd backend && uv run python manage.py test
