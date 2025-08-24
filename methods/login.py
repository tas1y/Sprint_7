import requests
from constants import Constants

class Login:
    @staticmethod
    def login_courier(login, password):
        payload = {"login": login, "password": password}
        response = requests.post(Constants.BASE_URL + Constants.LOGIN_COURIER_URL, data=payload)
        return response
