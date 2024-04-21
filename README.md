# Django Notes

## Generating a new secret key

```bash

python -c "import secrets; print(secrets.token_urlsafe())"

```

## static files

```bash

mkdir static
python -m pip install whitenoise

```

## settings.py

```python
INSTALLED_APPS = [
    "whitenoise.runserver_nostatic", # new
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware", # new
    "corsheaders.middleware.CorsMiddleware",
]

#static files settings
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"] # new
STATIC_ROOT = BASE_DIR / "staticfiles" # new
STATICFILES_STORAGE ="whitenoise.storage.CompressedManifestStaticFilesStorage" # new


```

## Gathering all the static files

```bash

python manage.py collectstatic

```

## Pyscopg and Gunicorn

```bash

python -m pip install psycopg2
python -m pip install gunicorn
python -m pip freeze > requirements.txt

```

## Deployment Checklist

1. add environment variables via django-environ
2. set DEBUG to False
3. set ALLOWED_HOSTS
4. use environment variable for SECRET_KEY
5. update DATABASES to use SQLite locally and PostgreSQL in production
6. configure static files and install whitenoise
7. install gunicorn for a production web server
8. create a requirements.txt file
