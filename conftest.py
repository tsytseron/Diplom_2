import random
import string
import pytest
import requests
from data import API_data

@pytest.fixture(scope='function')
def create_user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string

    def generate_user_data():
        email = generate_random_string(6) + '@yandex.ru'
        password = generate_random_string(10)
        name = generate_random_string(10)
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload

    data = generate_user_data()
    response = requests.post(API_data.CREATE_USER, data=data)
    token = response.json()['accessToken']
    headers = {"Content-type": "application/json", "Authorization": f'{token}'}
    yield response, data
    requests.delete(API_data.DELETE_USER, headers=headers)
