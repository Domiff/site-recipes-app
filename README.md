# BestRecipes — your favorite recipes site

BestRecipes is a Django web app for storing, browsing, and editing cooking recipes. Users can sign up, add their own dishes, and manage a personal recipe collection.

## Features

- **Browse recipes** — recipe list and a random selection on the home page
- **Add a recipe** — description, ingredients, steps, photo (authenticated users only)
- **Edit and delete** — recipe author only
- **Sign up and sign in** — dedicated authentication app

## Stack

- Python 3.13
- Django 5.2
- PostgreSQL
- Poetry
- Pillow (images)
- Gunicorn (production)

## Project structure

```
site-recipes-app/
├── core/                 # Django settings (settings, urls, wsgi)
├── site_recipes/         # recipes, categories, templates
│   └── templates/site_recipes/
├── auth_user/            # registration, login, logout
│   └── templates/auth/
├── manage.py
├── pyproject.toml
└── .env                  # environment variables (create from .env.template)
```

## Requirements

- Python 3.13+
- [Poetry](https://python-poetry.org/)
- PostgreSQL

The database driver (`psycopg2-binary`) is already listed in `pyproject.toml`.

## Setup and run

1. Clone the repository and go to the project directory.

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Create a PostgreSQL database and copy the environment template:

   ```bash
   cp .env.template .env
   ```

   Fill in `.env`:

   | Variable            | Description                        |
   |---------------------|------------------------------------|
   | `SECRET_KEY`        | Django secret key                  |
   | `DEBUG`             | `True` for local development       |
   | `POSTGRES_DB`       | database name                      |
   | `POSTGRES_USER`     | PostgreSQL user                    |
   | `POSTGRES_PASSWORD` | password                           |
   | `POSTGRES_HOST`     | host (default `localhost`)         |
   | `POSTGRES_PORT`     | port (default `5432`)              |

4. Apply migrations:

   ```bash
   poetry run python manage.py migrate
   ```

5. (Optional) Create a superuser:

   ```bash
   poetry run python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   poetry run python manage.py runserver
   ```

   App URL: http://127.0.0.1:8000/main/

## Routes

| URL               | Purpose                              |
|-------------------|--------------------------------------|
| `/main/`          | home, recipe list, and CRUD          |
| `/auth/register/` | registration                         |
| `/auth/login/`    | login                                |
| `/auth/logout/`   | logout                               |
| `/admin/`         | Django admin                           |

Template URL names: `site_recipes:*`, `auth_user:*`.

## Docker

Copy `.env.template` to `.env` and set `SECRET_KEY` and PostgreSQL credentials (defaults in `docker-compose.yml` work for local dev).

```bash
docker compose up --build
```

App: http://127.0.0.1:8000/main/

Migrations run automatically when the `web` container starts.

## App rename note

If the database already had tables from the old app labels (`site_recipes_app`, `auth_user_app`), you may need to update rows in `django_migrations` or recreate the database in a dev environment. Fresh installs use migrations from `site_recipes/` and `auth_user/` as-is.
