import allure
from constants import Message
from methods.courier import Courier
from utils.data_generator import generate_courier_data

class TestCreateCourier:
    @allure.title("Успешное создание курьера")
    @allure.description("Тест проверяет успешное создание нового курьера")
    def test_create_courier_success(self):
        courier_data = generate_courier_data()
        
        with allure.step("Создать нового курьера"):
            response = Courier.create_courier(courier_data["login"], courier_data["password"], courier_data["firstName"])
        
        with allure.step("Проверить код ответа и тело ответа"):
            assert response.status_code == 201
            assert response.json() == {"ok": True}

    @allure.title("Создание дубликата курьера")
    @allure.description("Тест проверяет ошибку при создании курьера с существующим логином")
    def test_create_duplicate_courier(self):
        courier_data = generate_courier_data()
        
        with allure.step("Создать первого курьера"):
            Courier.create_courier(courier_data["login"], courier_data["password"], courier_data["firstName"])
        
        with allure.step("Попытаться создать курьера с тем же логином"):
            response = Courier.create_courier(courier_data["login"], courier_data["password"], courier_data["firstName"])
        
        with allure.step("Проверить ошибку конфликта"):
            assert response.status_code == 409
            assert Message.LOGIN_OCCUPIED in response.json()["message"]

    @allure.title("Создание курьера без логина")
    @allure.description("Тест проверяет ошибку при создании курьера без логина")
    def test_create_courier_missing_login(self):
        courier_data = generate_courier_data()
        
        with allure.step("Создать курьера с пустым логином"):
            response = Courier.create_courier("", courier_data["password"], courier_data["firstName"])
        
        with allure.step("Проверить ошибку недостатка данных"):
            assert response.status_code == 400
            assert Message.MISSING_VALUE_REGISTRATION in response.json()["message"]

    @allure.title("Создание курьера без пароля")
    @allure.description("Тест проверяет ошибку при создании курьера без пароля")
    def test_create_courier_missing_password(self):
        courier_data = generate_courier_data()
        
        with allure.step("Создать курьера с пустым паролем"):
            response = Courier.create_courier(courier_data["login"], "", courier_data["firstName"])
        
        with allure.step("Проверить ошибку недостатка данных"):
            assert response.status_code == 400
            assert Message.MISSING_VALUE_REGISTRATION in response.json()["message"]

    @allure.title("Создание курьера без имени")
    @allure.description("Тест проверяет, что имя не является обязательным полем")
    def test_create_courier_missing_first_name(self):
        courier_data = generate_courier_data()
        
        with allure.step("Создать курьера с пустым именем"):
            response = Courier.create_courier(courier_data["login"], courier_data["password"], "")
        
        with allure.step("Проверить успешное создание (имя необязательно)"):
            assert response.status_code == 201
            assert response.json() == {"ok": True}
