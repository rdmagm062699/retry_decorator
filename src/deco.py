from functools import wraps
from time import sleep

def retry_exception(max_retries, backoff=0):
    def retry_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            tries = 0
            while True:
                try:
                    func(*args, **kwargs)
                    break
                except Exception:
                    tries += 1
                    if tries > max_retries:
                        raise
                    else:
                        sleep_time = backoff**(tries - 1)
                        sleep(sleep_time)
            
        return wrapper
    return retry_decorator
