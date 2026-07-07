import os
from pathlib import Path

REDIS_URL = "redis://localhost:6379/0"
BASE_DIR = Path(__file__).parent
DATABASE = os.path.join(BASE_DIR, "instance", "urls.db")
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL