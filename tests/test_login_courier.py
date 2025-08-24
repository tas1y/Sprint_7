import allure
from constants import Message
from methods.courier import Courier
from methods.login import Login


class TestLoginCourier:
    @allure.title("Успешная авторизация курьера")
    @allure.description("Тест проверяет успешный логин курьера")
    def test_login_courier_success(self):
        courier = Login.register_new_courier()
        
        with allure.step("Выполнить авторизацию"):
            response = Login.login_courier(courier["login"], courier["password"])
        
        with allure.step("Проверить успешную авторизацию"):
            assert response.status_code == 200
            assert "id" in response.json()
            courier_id = response.json()["id"]

        delete_response = Courier.delete_courier(courier_id)

        with allure.step("Проверить успешное удаление"):
            assert delete_response.status_code == 200

    @allure.title("Авторизация с неверным паролем")
    @allure.description("Тест проверяет ошибку при авторизации с неверным паролем")
    def test_login_courier_wrong_password(self):
        courier = Login.register_new_courier()
        
        with allure.step("Попытаться авторизоваться с неверным паролем"):
            response = Login.login_courier(courier["login"], "wrong_password")
        
        with allure.step("Проверить ошибку авторизации"):
            assert response.status_code == 404
            assert Message.ACCOUNT_NOT_FOUND in response.json()["message"]

        with allure.step("Выполнить авторизацию"):
            response = Login.login_courier(courier["login"], courier["password"])
        
        with allure.step("Проверить успешную авторизацию"):
            assert response.status_code == 200
            assert "id" in response.json()
            courier_id = response.json()["id"]

        delete_response = Courier.delete_courier(courier_id)

        with allure.step("Проверить успешное удаление"):
            assert delete_response.status_code == 200

    @allure.title("Авторизация с неверным логином")
    @allure.description("Тест проверяет ошибку при авторизации с неверным логином")
    def test_login_courier_wrong_login(self):
        courier = Login.register_new_courier()
        
        with allure.step("Попытаться авторизоваться с неверным логином"):
            response = Login.login_courier("wrong_login", courier["password"])
        
        with allure.step("Проверить ошибку авторизации"):
            assert response.status_code == 404
            assert Message.ACCOUNT_NOT_FOUND in response.json()["message"]

        with allure.step("Выполнить авторизацию"):
            response = Login.login_courier(courier["login"], courier["password"])
        
        with allure.step("Проверить успешную авторизацию"):
            assert response.status_code == 200
            assert "id" in response.json()
            courier_id = response.json()["id"]

        delete_response = Courier.delete_courier(courier_id)

        with allure.step("Проверить успешное удаление"):
            assert delete_response.status_code == 200

    @allure.title("Авторизация без логина")
    @allure.description("Тест проверяет ошибку при авторизации без логина")
    def test_login_courier_missing_login(self):
        with allure.step("Попытаться авторизоваться без логина"):
            response = Login.login_courier("", "password")
        
        with allure.step("Проверить ошибку недостатка данных"):
            assert response.status_code == 400
            assert Message.MISSING_VALUE_AUTHORIZATION in response.json()["message"]

    @allure.title("Авторизация без пароля")
    @allure.description("Тест проверяет ошибку при авторизации без пароля")
    def test_login_courier_missing_password(self):
        with allure.step("Попытаться авторизоваться без пароля"):
            response = Login.login_courier("login", "")
        
        with allure.step("Проверить ошибку недостатка данных"):
            assert response.status_code == 400
            assert Message.MISSING_VALUE_AUTHORIZATION in response.json()["message"]

    @allure.title("Авторизация несуществующего курьера")
    @allure.description("Тест проверяет ошибку при авторизации несуществующего курьера")
    def test_login_nonexistent_courier(self):
        with allure.step("Попытаться авторизоваться несуществующего курьера"):
            response = Login.login_courier("nonexistent", "password")
        
        with allure.step("Проверить ошибку авторизации"):
            assert response.status_code == 404
            assert Message.ACCOUNT_NOT_FOUND in response.json()["message"]