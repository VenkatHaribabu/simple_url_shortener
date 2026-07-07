import random
import string
from urllib.parse import urlparse
from models import get_url

def generate_short_code(length=6):
    while True:                  # To genereate unique code
        short_code = ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=length
            )
        )
        if get_url(short_code) is None:
            return short_code


def is_valid_url(url):
    try:                      # To check urls
        parsed = urlparse(url)
        return all([
            parsed.scheme in ("http", "https"),
            parsed.netloc
        ])
    except Exception:
        return False


        