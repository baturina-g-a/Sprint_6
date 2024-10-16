import allure
import pytest

from data import FIRSTNAME, LASTNAME, ADDRESS, STATION, PHONE, DELIVERY_DATE, RENTAL_TIME, COLOR, COMMENT
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка успешного создания заказа')
    @allure.description(
        'Проверяем, что заказ был создан, на странице отслеживания заказа есть кнопка "Отменить заказ"')
    @pytest.mark.parametrize(
        'firstname, lastname, address, station, phone, delivery_date, rental_time, color, comment',
        [
            (FIRSTNAME[0], LASTNAME[0], ADDRESS[0], STATION[0], PHONE[0], DELIVERY_DATE[0], RENTAL_TIME[0], COLOR[0],
             COMMENT[0]),
            (FIRSTNAME[1], LASTNAME[1], ADDRESS[1], STATION[1], PHONE[1], DELIVERY_DATE[1], RENTAL_TIME[1], COLOR[1],
             COMMENT[1])
        ]
    )
    def test_order_successfully_created(self, driver, firstname, lastname, address, station, phone,
                                        delivery_date, rental_time, color, comment):
        order_page = OrderPage(driver)
        order_page.make_order(firstname, lastname, address, station, phone,
                              delivery_date, rental_time, color, comment)
        assert order_page.check_order() == 'Отменить заказ'
