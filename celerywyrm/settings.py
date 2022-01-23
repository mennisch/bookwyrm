""" bookwyrm settings and configuration """
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from bookwyrm.settings import *

REDIS_BROKER_URL = env("REDIS_BROKER_URL", "redis://redis_broker:6379/0")

CELERY_BROKER_URL = REDIS_BROKER_URL
CELERY_RESULT_BACKEND = REDIS_BROKER_URL

CELERY_DEFAULT_QUEUE = "low_priority"

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
FLOWER_PORT = env("FLOWER_PORT")

INSTALLED_APPS = INSTALLED_APPS + [
    "celerywyrm",
]

ROOT_URLCONF = "celerywyrm.urls"

WSGI_APPLICATION = "celerywyrm.wsgi.application"
