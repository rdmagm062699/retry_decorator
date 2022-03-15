from functools import wraps
from textwrap import wrap

def retry_exception(max_retries):
    def retry_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            tries = 0
            while True:
                try:
                    print('blah')
                    func(*args, **kwargs)
                except Exception:
                    tries += 1
                    if tries > max_retries:
                        break
            
        return wrapper
    return retry_decorator
