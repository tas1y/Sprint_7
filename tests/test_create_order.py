import pytest
import allure
from methods.orders import Orders
from utils.data_generator import generate_order_data


class TestCreateOrder:
    @allure.title("Создание заказа с разными вариантами цветов")
    @allure.description("Параметризованный тест создания заказа с различными комбинациями цветов")
    @pytest.mark.parametrize("color", [
        (["BLACK"], "с черным цветом"),
        (["GREY"], "с серым цветом"), 
        (["BLACK", "GREY"], "с обоими цветами"),
        ([], "без указания цвета")
    ], ids=["black_color", "grey_color", "both_colors", "no_color"])
    def test_create_order_with_different_colors(self, color):
        color_value, color_description = color
        
        allure.dynamic.title(f"Создание заказа {color_description}")
        
        with allure.step(f"Создать заказ {color_description}"):
            order_data = generate_order_data(color_value)
            response = Orders.create_order(order_data)
        
        with allure.step("Проверить успешное создание заказа"):
            assert response.status_code == 201
        
        with allure.step("Проверить наличие track номера в ответе"):
            assert "track" in response.json()