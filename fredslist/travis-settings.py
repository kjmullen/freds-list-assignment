from .settings import *


DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fredslist',
        'USER': 'postgres',  # travis sets up postgres user
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
