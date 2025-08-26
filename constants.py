class Constants:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    CREATE_COURIER_URL = "/api/v1/courier"
    LOGIN_COURIER_URL = "/api/v1/courier/login"
    ORDERS_URL = "/api/v1/orders"
    DELETE_COURIER_URL = "/api/v1/courier/"

class Message:
    MISSING_VALUE_REGISTRATION = "Недостаточно данных для создания учетной записи"
    LOGIN_OCCUPIED = "Этот логин уже используется"
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    MISSING_VALUE_AUTHORIZATION = "Недостаточно данных для входа"