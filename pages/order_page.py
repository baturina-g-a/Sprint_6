import allure

import data
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Открываем страницу оформления заказа')
    def get_to_order_page(self):
        self.get_to_url(data.ORDER_PAGE_URL)

    @allure.step('Принимаем файлы cookie на странице оформления заказа')
    def accept_cookies_on_order_page(self):
        self.click_to_element(OrderPageLocators.COOKIE_BUTTON)

    @allure.step('Создаем заказ')
    def make_order(self, firstname, lastname, address, station, phone,
                   delivery_date, rental_time, color, comment):
        self.get_to_order_page()
        self.accept_cookies_on_order_page()
        self.add_text_to_field(OrderPageLocators.FIRSTNAME_FIELD, firstname)
        self.add_text_to_field(OrderPageLocators.LASTNAME_FIELD, lastname)
        self.add_text_to_field(OrderPageLocators.ADDRESS_FIELD, address)
        self.click_to_element(OrderPageLocators.STATION_FIELD)
        locator_station_formatted = self.format_locator(OrderPageLocators.STATION_NAME, station)
        self.click_to_element(locator_station_formatted)
        self.add_text_to_field(OrderPageLocators.PHONE_FIELD, phone)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
        self.add_text_to_field(OrderPageLocators.DELIVERY_DATE_FIELD, delivery_date)
        self.click_to_element(OrderPageLocators.TITLE_FORM)
        self.click_to_element(OrderPageLocators.RENTAL_TIME_FIELD)
        locator_rental_time_formatted = self.format_locator(OrderPageLocators.RENTAL_TIME_LIST, rental_time)
        self.click_to_element(locator_rental_time_formatted)
        locator_color_formatted = self.format_locator(OrderPageLocators.COLOR_CHECKBOX, color)
        self.click_to_element(locator_color_formatted)
        self.add_text_to_field(OrderPageLocators.COMMENT_FIELD, comment)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_UNDER_FORM)
        self.click_to_element(OrderPageLocators.ORDER_CONFIRMATION_BUTTON)
        self.click_to_element(OrderPageLocators.VIEW_STATUS_BUTTON)

    @allure.step('Проверяем, что заказ был создан')
    def check_order(self):
        return self.get_text_from_element(OrderPageLocators.CANCEL_ORDER_BUTTON)
