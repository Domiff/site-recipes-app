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
- [uv](https://docs.astral.sh/uv/)
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
├── uv.lock
└── .env                  # environment variables (create from .env.template)
```

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- PostgreSQL (production / Docker; SQLite when `DEBUG=True`)

The database driver (`psycopg`) is listed in `pyproject.toml`.

## Setup and run

1. Clone the repository and go to the project directory.

2. Install dependencies:

   ```bash
   uv sync
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
   uv run python manage.py migrate
   ```

5. (Optional) Create a superuser:

   ```bash
   uv run python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   uv run python manage.py runserver
   ```

   Or with [just](https://github.com/casey/just): `just install`, `just migrate`, `just run`.

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

Copy `.env.template` to `.env` and set `SECRET_KEY`. All services read variables from `.env` (`POSTGRES_HOST=db`, `DEBUG=False` for PostgreSQL in containers).

```bash
docker compose up --build
```

App: http://127.0.0.1:8000/main/

The image uses a multi-stage build (`builder` with `uv sync` → `runtime`). Migrations run when the `web` container starts.

For local development without Docker, use `DEBUG=True` (SQLite) and `POSTGRES_HOST=localhost` in `.env`.

## App rename note

If the database already had tables from the old app labels (`site_recipes_app`, `auth_user_app`), you may need to update rows in `django_migrations` or recreate the database in a dev environment. Fresh installs use migrations from `site_recipes/` and `auth_user/` as-is.
