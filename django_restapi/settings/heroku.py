"""
Production Settings for Heroku
"""

import environ

# If using in your own project, update the project namespace below
from django_restapi.settings.base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# False if not in os.environ
DEBUG = env('DEBUG')

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

SQLITE_URL = env('SQLITE_URL')

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}