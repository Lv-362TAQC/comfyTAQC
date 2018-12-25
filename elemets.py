from selenium import webdriver
from os import path
from locators import *


class BasePageElement:
    def __init__(self, driver=None):
        self.driver = driver if driver else webdriver.Chrome(path.abspath('chromedriver'))


class HeaderElement(BasePageElement):
    def __init__(self, driver=None):
        super().__init__(driver)

    def switch_lang(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element(*Header.LANG_SWITCHER).click()

class Link(BasePageElement):
    def __init__(self, locator, driver=None):
        super().__init__(driver)
        self.locator = self.driver.find_element(locator)
    def click(self):
        self.locator.click()