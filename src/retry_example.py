import os
from posix import environ
import requests
from src.deco import retry_exception

@retry_exception(
    max_retries=int(os.environ['MAX_RETRIES']),
    backoff=int(os.environ['BACKOFF'])
)
def run_it():
    requests.post('http://example.com')
