from selenium.webdriver.common.by import By


class PageTransitionsLocators:
    # кнопка принятия cookie:
    COOKIE_BUTTON = By.XPATH, '//button[contains(@class, "App_CookieButton")]'
    # кнопка "Заказать" в хедере:
    ORDER_BUTTON_IN_HEADER = By.XPATH, '//button[@class ="Button_Button__ra12g" and text()="Заказать"]'
    # кнопка "Заказать" на странице:
    ORDER_BUTTON_ON_PAGE = By.XPATH, '//button[contains(@class,"Button_Middle") and text()="Заказать"]'
    # 4-ый пункт инструкции:
    INSTRUCTION = By.XPATH, '//div[text()="4"]'
    # заголовок формы на странице оформления заказа:
    TITLE_ORDER_FORM = By.XPATH, '//div[text()="Для кого самокат"]'
    # лого "Самокат" в хедере:
    LOGO_SCOOTER = By.XPATH, '//a[contains(@class,"Header_LogoScooter")]'
    # описание главной страницы:
    HOME_PAGE_DESCRIPTION = By.XPATH, '//div[contains(@class,"Home_Header")]'
    # лого Яндекса в хедере:
    LOGO_YANDEX = By.XPATH, '//a[contains(@class,"Header_LogoYandex")]'
    # кнопка "Установить" в всплывающем окне с предложением установить Яндекс Браузер:
    DOWNLOAD_BUTTON = By.XPATH, '//a[text()="Установить"]'



