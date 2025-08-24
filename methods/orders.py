import requests
from constants import Constants

class Orders:
    @staticmethod
    def create_order(order_data):
        response = requests.post(Constants.BASE_URL + Constants.ORDERS_URL, json=order_data)
        return response

    @staticmethod
    def get_orders_list():
        response = requests.get(Constants.BASE_URL + Constants.ORDERS_URL)
        return response