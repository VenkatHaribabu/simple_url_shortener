from celery import Celery
from config import REDIS_URL

celery = Celery(
    "url_shortener",
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"]
)

import tasks