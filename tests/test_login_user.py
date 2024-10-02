import allure
import requests
from data import API_data
class TestLoginUser:
    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, create_user):
        response, data = create_user
        resp = requests.post(API_data.LOGIN_USER, data=data)
        assert resp.status_code == 200 and API_data.SUCCESS_TRUE in resp.text

    @allure.title("Логин с неверным email и паролем")
    def test_login_with_incorrect_data(self, create_user):
        response, data = create_user
        data['email'] = ''
        data['password'] = ''
        resp = requests.post(API_data.LOGIN_USER, data=data)
        assert resp.status_code == 401 and API_data.INCORRECT_DATA

    @allure.title("Проверка логина с неверным email")
    def test_login_with_incorrect_email(self, create_user):
        response, data = create_user
        data['email'] = ''
        resp = requests.post(API_data.LOGIN_USER, data=data)
        assert resp.status_code == 401 and API_data.INCORRECT_DATA

    @allure.title("Проверка логина с неверным паролем")
    def test_login_with_incorrect_password(self, create_user):
        response, data = create_user
        data['password'] = ''
        resp = requests.post(API_data.LOGIN_USER, data=data)
        assert resp.status_code == 401 and API_data.INCORRECT_DATA
