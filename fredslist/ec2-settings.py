from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fredslist',
        'USER': 'postgres',
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}