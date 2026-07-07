from celery_worker import celery
from models import update_status
from utils import is_valid_url


@celery.task(name="tasks.validate_url_task")
def validate_url_task(message):
    """
    Background task to validate URL
    """

    url = message["url"]
    url_id = message["id"]

    print(f"\nProcessing URL: {url}")

    if is_valid_url(url):
        update_status(url_id, "active")
        print("Status Updated → ACTIVE")

    else:
        update_status(url_id, "invalid")
        print("Status Updated → INVALID")