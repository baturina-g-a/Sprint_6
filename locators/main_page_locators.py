from selenium.webdriver.common.by import By


class MainPageLocators:
    # кнопка принятия cookie:
    COOKIE_BUTTON = By.XPATH, '//button[contains(@class, "App_CookieButton")]'
    # вопросы в аккордеон-меню:
    QUESTION = By.XPATH, '//*[@id="accordion__heading-{}"]'
    # последний вопрос в аккордеон-меню (восьмой):
    LAST_QUESTION = By.XPATH, '//*[@id="accordion__heading-7"]'
    # ответы на вопросы:
    ANSWER = By.XPATH, '//*[@id="accordion__panel-{}"]'
