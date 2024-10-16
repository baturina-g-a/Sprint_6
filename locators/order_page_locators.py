from selenium.webdriver.common.by import By


class OrderPageLocators:
    # поле имя:
    FIRSTNAME_FIELD = By.XPATH, '//input[@placeholder="* Имя"]'
    # поле фамилия:
    LASTNAME_FIELD = By.XPATH, '//input[@placeholder="* Фамилия"]'
    # поле адрес:
    ADDRESS_FIELD = By.XPATH, '//input[contains(@placeholder,"* Адрес")]'
    # поле станции метро:
    STATION_FIELD = By.XPATH, '//input[@placeholder="* Станция метро"]'
    # название станции метро:
    STATION_NAME = By.XPATH, '//div[text()="{}"]'
    # поле номер телефона:
    PHONE_FIELD = By.XPATH, '//input[contains(@placeholder,"* Телефон")]'
    # кнопка "Далее":
    NEXT_BUTTON = By.XPATH, '//button[text()="Далее"]'
    # поле выбора даты доставки:
    DELIVERY_DATE_FIELD = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    # поле срок аренды:
    RENTAL_TIME_FIELD = By.XPATH, '//div[text()="* Срок аренды"]'
    # список возможных сроков аренды:
    RENTAL_TIME_LIST = By.XPATH, '//div[@class = "Dropdown-menu"]/div[text() = "{}"]'
    # чек-бокс выбора цвета:
    COLOR_CHECKBOX = By.XPATH, '//input[@id="{}"]'
    # поле для комментария:
    COMMENT_FIELD = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    # кнопка "Заказать" под формой:
    ORDER_BUTTON_UNDER_FORM = By.XPATH, '//button[contains(@class,"Button_Middle") and text()="Заказать"]'
    # кнопка "Да" в модальном окне подтверждения заказа:
    ORDER_CONFIRMATION_BUTTON = By.XPATH, '//button[contains(@class,"Button_Middle") and text()="Да"]'
    # кнопка "Посмотреть статус" в модальном окне подтверждения заказа:
    VIEW_STATUS_BUTTON = By.XPATH, '//button[contains(@class,"Button_Middle") and text()="Посмотреть статус"]'
    # кнопка "Отменить заказ" на странице отслеживания заказа:
    CANCEL_ORDER_BUTTON = By.XPATH, '//button[contains(@class,"Button_Middle") and text()="Отменить заказ"]'
    # кнопка принятия cookie:
    COOKIE_BUTTON = By.XPATH, '//button[contains(@class, "App_CookieButton")]'
    # заголовок формы:
    TITLE_FORM = By.XPATH, '//div[text()="Про аренду"]'
