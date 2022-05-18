DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_testing_examples",
        "ATOMIC_REQUESTS": True,
    }
}

DEBUG = True

INTERNAL_IPS = ("127.0.0.1", "testserver", "localhost")
ALLOWED_HOSTS = INTERNAL_IPS