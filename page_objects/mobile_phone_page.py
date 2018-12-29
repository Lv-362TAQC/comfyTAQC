from selenium.webdriver.common.keys import Keys
from page_objects.base_page import BasePage
from page_elements.page_elements import HeaderElement, ElementSorting, ElementView
from locators.locators import *

BASE_URL = 'https://rozetka.com.ua/'


class MobilePhonesPage(BasePage):
    def __init__(self, driver=None):
        self.locator = MobPhoneLocators
        super().__init__(driver)
        self.driver.get(BASE_URL+'mobile-phones/c80003/')
        self.header = HeaderElement(self.driver)
        self.sort = ElementSorting(self.driver)
        self.switch_view = ElementView(self.driver)

    def search_item(self, item):
        self.find_element(*self.HeaderLocators.SEARCH).send_keys(item)
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        return self.find_element(*self.locator.SEARCH_LIST).text
