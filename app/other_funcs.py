import random

import requests


def get_random_number():
    return random.randint(1, 100)


def get_data():
    response = requests.get('http://httpbin.org/ip')
    response.raise_for_status()
    return response.json()


def log_message(message: str):
    print(message)


def get_status_code_from_response(response: requests.Response):
    return response.status_code
