from .settings import *


# override database settings and use in-memory sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEST_RUNNER = "green.djangorunner.DjangoRunner"
