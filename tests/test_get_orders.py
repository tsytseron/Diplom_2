import allure
import requests
from data import API_data
class TestGetOrdersUser:
    @allure.title("Получение заказа авторизованным пользователем")
    def test_get_order_auth_user(self, create_user):
        response, data = create_user
        token = response.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        ingredients = {"ingredients": [API_data.FLUOR_BUN, API_data.BIO_CUTLET, API_data.SAUCE_SPICY, API_data.FLUOR_BUN]}
        requests.post(API_data.CREATE_ORDER, data=ingredients, headers=headers)
        order = requests.get(API_data.GET_ORDER, headers=headers)
        assert order.status_code == 200 and API_data.SUCCESS_TRUE in order.text

    @allure.title("Получение заказа неавторизованным пользователем")
    def test_get_order_not_auth_user(self):
        order = requests.get(API_data.GET_ORDER)
        assert order.status_code == 401 and API_data.ORDER_NOT_AUTHORIZED in order.text
