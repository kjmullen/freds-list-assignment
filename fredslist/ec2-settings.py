from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fredslist',
        'USER': 'postgres',
        'PASSWORD': os.environ["DB_PASSWORD"],
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

DEBUG = False
STATIC_ROOT = 'staticfiles'

ALLOWED_HOSTS = ['*']
