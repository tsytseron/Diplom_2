import allure
import requests
from data import API_data
class TestCreateUser:
    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self, create_user):
        response, data = create_user
        assert response.status_code == 200 and API_data.SUCCESS_TRUE in response.text

    @allure.title("Создание ранее зарегистрированного пользователя")
    def test_cannot_create_duplicate_user(self, create_user):
        response, data = create_user
        resp = requests.post(API_data.CREATE_USER, data=data)
        assert resp.status_code == 403 and API_data.SUCCESS_FALSE in resp.text

    @allure.title("Создание пользователя без обязательного поля 'имя'")
    def test_create_user_without_name(self, create_user):
        response, data = create_user
        data['name'] = ''
        resp = requests.post(API_data.CREATE_USER, data=data)
        assert resp.status_code == 403 and API_data.REQUIRED_FIELDS in resp.text

    @allure.title("Создание пользователя без обязательного поля 'пароль'")
    def test_create_user_without_password(self, create_user):
        response, data = create_user
        data['password'] = ''
        resp = requests.post(API_data.CREATE_USER, data=data)
        assert resp.status_code == 403 and API_data.REQUIRED_FIELDS in resp.text

    @allure.title("Создание пользователя без обязательного поля 'email'")
    def test_create_user_without_email(self, create_user):
        response, data = create_user
        data['email'] = ''
        resp = requests.post(API_data.CREATE_USER, data=data)
        assert resp.status_code == 403 and API_data.REQUIRED_FIELDS in resp.text
