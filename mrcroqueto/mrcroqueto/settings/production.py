from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["croqueto-3e4467808c40.herokuapp.com"]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "d23s6fll5v19vb",
        "PASSWORD": "d43aea101018c8a4d9d29be5175d0a8937b3953bd3627be22ef22886c6c8bca3",
        "USER": "ulgjagiccredxt",
        "HOST": "ec2-35-169-9-79.compute-1.amazonaws.com",
        "PORT": "5432",
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "core/static/"
