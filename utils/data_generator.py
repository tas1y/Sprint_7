import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }

def generate_order_data(color=None):
    order_data = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "ул. Пушкина, д. 10",
        "metroStation": 4,
        "phone": "+79991112233",
        "rentTime": 5,
        "deliveryDate": "2024-12-31",
        "comment": "Тестовый заказ"
    }
    
    if color is not None:
        order_data["color"] = color
    
    return order_data
