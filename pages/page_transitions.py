import allure

import data
from locators.page_transitions_locators import PageTransitionsLocators
from pages.base_page import BasePage


class PageTransitions(BasePage):

    @allure.step('Открываем главную страницу')
    def get_to_main_page(self):
        self.get_to_url(data.MAIN_PAGE_URL)

    @allure.step('Принимаем файлы cookie')
    def accept_cookies(self):
        self.click_to_element(PageTransitionsLocators.COOKIE_BUTTON)

    @allure.step('Нажимаем на кнопку "Заказать" в хедере')
    def click_to_order_button_in_header(self):
        self.get_to_main_page()
        self.accept_cookies()
        self.click_to_element(PageTransitionsLocators.ORDER_BUTTON_IN_HEADER)
        return self.get_text_from_element(PageTransitionsLocators.TITLE_ORDER_FORM)

    @allure.step('Нажимаем на логотип "Самокат" в хедере')
    def click_to_logo_scooter(self):
        self.click_to_element(PageTransitionsLocators.LOGO_SCOOTER)
        return self.find_element_with_wait(PageTransitionsLocators.HOME_PAGE_DESCRIPTION)

    @allure.step('Нажимаем на кнопку "Заказать" на странице')
    def click_to_order_button_on_page(self):
        self.get_to_main_page()
        self.accept_cookies()
        self.scroll_page_to_element(PageTransitionsLocators.INSTRUCTION)
        self.click_to_element(PageTransitionsLocators.ORDER_BUTTON_ON_PAGE)
        return self.get_text_from_element(PageTransitionsLocators.TITLE_ORDER_FORM)

    @allure.step('Переключаемся на новую вкладку в браузере')
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Нажимаем на логотип "Яндекс" в хедере')
    def click_to_logo_yandex(self):
        self.click_to_element(PageTransitionsLocators.LOGO_YANDEX)
        self.switch_to_new_tab()
        return self.get_text_from_element(PageTransitionsLocators.DOWNLOAD_BUTTON)
