import allure

import data
from pages.page_transitions import PageTransitions


class TestPageTransitions:

    @allure.title('Проверка клика на кнопку "Заказать" в хедере')
    @allure.description('Проверяем, что клик на кнопку "Заказать" в хедере ведёт на страницу оформления заказа, '
                        'находим заголовок формы заказа')
    def test_click_on_order_button_in_header_leads_to_order_page(self, driver):
        page_transitions = PageTransitions(driver)
        assert page_transitions.click_to_order_button_in_header() == 'Для кого самокат'

    @allure.title('Проверка клика на логотип "Самокат" в хедере')
    @allure.description('Проверяем, что клик на логотип "Самокат" в хедере ведёт со страницы оформления заказа на '
                        'главную, находим описание главной страницы')
    def test_click_on_logo_scooter_leads_to_main_page(self, driver):
        page_transitions = PageTransitions(driver)
        page_transitions.click_to_order_button_in_header()
        assert page_transitions.click_to_logo_scooter().text == data.DESCRIPTION

    @allure.title('Проверка клика на кнопку "Заказать" на странице')
    @allure.description('Проверяем, что клик на кнопку "Заказать", расположенную в теле страницы, ведёт на страницу '
                        'оформления заказа, находим заголовок формы заказа')
    def test_click_on_order_button_on_page_leads_to_order_page(self, driver):
        page_transitions = PageTransitions(driver)
        assert page_transitions.click_to_order_button_on_page() == 'Для кого самокат'

    @allure.title('Проверка клика на логотип "Яндекс" в хедере')
    @allure.description('Проверяем, что клик на логотип "Яндекс" в хедере ведёт со страницы оформления заказа на '
                        'страницу Дзена, находим кнопку "Установить" в окне с предложением скачать Яндекс браузер')
    def test_click_on_logo_yandex_leads_to_dzen_page(self, driver):
        page_transitions = PageTransitions(driver)
        page_transitions.click_to_order_button_on_page()
        assert page_transitions.click_to_logo_yandex() == 'Установить'
