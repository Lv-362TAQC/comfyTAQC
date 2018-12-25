from selenium import webdriver
from locators import *
from os import path


class BasePage:
    def __init__(self, driver=None):
        self.driver = driver if driver else webdriver.Chrome(path.abspath('chromedriver'))


class FunniturePage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)
        self.driver.get('https://rozetka.com.ua/ua/mebel/c152458/')
        self.driver.find_element(*Popup.CLOSE_COMMR_POPUP).click()
        self.driver.find_element(*Popup.CLOSE_LANG_POPUP).click()

if __name__ == '__main__':
    driver = webdriver.Chrome(path.abspath('chromedriver'))
    FunniturePage(driver)