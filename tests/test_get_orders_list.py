import allure
from methods.orders import Orders


class TestGetOrdersList:
    @allure.title("Получение списка заказов")
    @allure.description("Тест проверяет получение списка всех заказов")
    def test_get_orders_list(self):
        with allure.step("Запросить список заказов"):
            response = Orders.get_orders_list()
    
        with allure.step("Проверить успешный ответ"):
            assert response.status_code == 200

        with allure.step("Получение непустого списка заказов"):
            assert response.json()["orders"]