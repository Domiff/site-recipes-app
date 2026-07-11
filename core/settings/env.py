"""
Environment variables (django-environ).
https://django-environ.readthedocs.io/
"""

from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, ""),
    ALLOWED_HOSTS=(list, ["127.0.0.1", "0.0.0.0"]),
    POSTGRES_DB=(str, ""),
    POSTGRES_USER=(str, ""),
    POSTGRES_PASSWORD=(str, ""),
    POSTGRES_HOST=(str, "localhost"),
    POSTGRES_PORT=(str, "5432"),
    CSRF_TRUSTED_ORIGIN=(str, "http://127.0.0.1:8080"),
)

environ.Env.read_env(BASE_DIR / ".env")
