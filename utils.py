import time
import random
from functools import wraps

def retry_network_operation(max_retries=3, backoff=1.0, exceptions=(Exception,)):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_retries - 1:
                        raise
                    sleep_time = backoff * (2 ** attempt) + random.uniform(0, 1)
                    time.sleep(sleep_time)
        return wrapper
    return decorator