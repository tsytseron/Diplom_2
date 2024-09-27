import allure
import requests
from data import API_data
class TestUpdateUser:
    @allure.title("Изменение email авторизованным пользователем")
    def test_update_email_authorized_user(self, create_user):
        response, data = create_user
        token = response.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        new_email_value = 'up' + response.json()["user"]['email']
        new_email = {"email": new_email_value}
        replace = requests.patch(API_data.UPDATE_DATA, json=new_email, headers=headers)
        assert replace.status_code == 200 and replace.json()['user']['email'] == new_email['email']

    @allure.title("Изменение пароля авторизованным пользователем")
    def test_update_password_authorized_user(self, create_user):
        response, data = create_user
        token = response.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        new_password_value = 'up' + data["password"]
        new_password = {"password": new_password_value}
        replace = requests.patch(API_data.UPDATE_DATA, json=new_password, headers=headers)
        assert replace.status_code == 200 and API_data.SUCCESS_TRUE in replace.text

    @allure.title("Изменение имени авторизованным пользователем")
    def test_update_name_authorized_user(self, create_user):
        response, data = create_user
        token = response.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        new_name_value = 'up' + response.json()["user"]["name"]
        new_name = {"name": new_name_value}
        replace = requests.patch(API_data.UPDATE_DATA, json=new_name, headers=headers)
        assert replace.status_code == 200 and replace.json()['user']['name'] == new_name['name']

    @allure.title("Изменение имени неавторизованным пользователем")
    def test_update_name_notauthorized_user(self, create_user):
        response, data = create_user
        requests.post(API_data.CREATE_USER, data=data)
        headers = {"Content-type": "application/json"}
        new_name_value = 'up' + response.json()["user"]["name"]
        new_name = {"name": new_name_value}
        replace = requests.patch(API_data.UPDATE_DATA, json=new_name, headers=headers)
        assert replace.status_code == 401 and API_data.NOT_AUTHORIZED in replace.text
