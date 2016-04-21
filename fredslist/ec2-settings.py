from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fredslist',
        'USER': 'postgres',
        'PASSWORD': os.environ["DB_PASSWORD"],
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = False
STATIC_ROOT='staticfiles'

ALLOWED_HOSTS = ['*']
