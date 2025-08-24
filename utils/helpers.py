import requests
import allure
from constants import Constants
from utils.data_generator import generate_courier_data

@allure.step("Регистрация нового курьера")
def register_new_courier():
    courier_data = generate_courier_data()
    response = requests.post(Constants.BASE_URL + Constants.CREATE_COURIER_URL, data=courier_data)
    
    if response.status_code == 201:
        return {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        }
    return None
