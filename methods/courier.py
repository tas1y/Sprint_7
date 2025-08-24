import allure
import requests
from constants import Constants

class Courier:
    @staticmethod
    def create_courier(login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(Constants.BASE_URL + Constants.CREATE_COURIER_URL, data=payload)
        return response

    @allure.step("Удалить созданного курьера")
    def delete_courier(courier_id):
        response = requests.delete(Constants.BASE_URL + Constants.DELETE_COURIER_URL + str(courier_id))
        return response
