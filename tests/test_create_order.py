import allure
import requests
from data import API_data
class TestCreateOrder:
    @allure.title("Cоздание заказа с авторизацией, с ингредиентами")
    def test_create_order_auth_user_ingredients(self, create_user):
        response, data = create_user
        requests.post(API_data.LOGIN_USER, data=data)
        ingredients = {"ingredients": [API_data.FLUOR_BUN, API_data.BIO_CUTLET, API_data.SAUCE_SPICY, API_data.FLUOR_BUN]}
        resp = requests.post(API_data.CREATE_ORDER, data=ingredients)
        assert resp.status_code == 200 and API_data.SUCCESS_TRUE in resp.text

    @allure.title("Создание заказа без авторизации, с ингредиентами")
    def test_create_order_not_auth_user_ingredients(self):
        ingredients = {"ingredients": [API_data.FLUOR_BUN, API_data.BIO_CUTLET, API_data.SAUCE_SPICY, API_data.FLUOR_BUN]}
        resp = requests.post(API_data.CREATE_ORDER, data=ingredients)
        assert resp.status_code == 200 and API_data.SUCCESS_TRUE in resp.text

    @allure.title("Создание заказа с авторизацией, без ингредиентов")
    def test_create_order_auth_user_without_ingredients(self, create_user):
        response, data = create_user
        requests.post(API_data.LOGIN_USER, data=data)
        ingredients = {"ingredients": ['']}
        resp = requests.post(API_data.CREATE_ORDER, data=ingredients)
        assert resp.status_code == 400 and API_data.NOT_INGREDIENT in resp.text

    @allure.title("Создание заказа без авторизации, с невалидным хешем ингредиентов")
    def test_create_order_not_auth_user_incorrect_hash(self):
        ingredients = {"ingredients": [API_data.INVALID_HASH, API_data.FLUOR_BUN, API_data.BIO_CUTLET]}
        resp = requests.post(API_data.CREATE_ORDER, data=ingredients)
        assert resp.status_code == 500 and API_data.ORDER_INCORRECT_INGREDIENTS in resp.text
