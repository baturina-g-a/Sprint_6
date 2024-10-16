from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def scroll_page_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def add_text_to_field(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locator(self, locator_num, num):
        method, locator = locator_num
        locator = locator.format(num)
        return method, locator
