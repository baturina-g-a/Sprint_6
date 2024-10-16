import allure

import data
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Открываем главную страницу')
    def get_to_main_page(self):
        self.get_to_url(data.MAIN_PAGE_URL)

    @allure.step('Принимаем файлы cookie')
    def accept_cookies(self):
        self.click_to_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Получаем текст ответа на вопрос')
    def get_text_answer_to_question(self, num):
        self.get_to_main_page()
        self.accept_cookies()
        locator_q_formatted = self.format_locator(MainPageLocators.QUESTION, num)
        locator_a_formatted = self.format_locator(MainPageLocators.ANSWER, num)
        self.scroll_page_to_element(MainPageLocators.LAST_QUESTION)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

