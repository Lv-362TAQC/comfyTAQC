import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class comfy_home():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    def cre_new_p(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
    def setUp(self):
        self.driver.get("https://comfy.ua/")
    def close_p(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    def langtr(self):
        self.cre_new_p()
        self.setUp()
        if str("Каталог товаров") in self.driver.page_source:
            elem = self.driver.find_element_by_xpath('//*[@class="store-switcher__link store-switcher__link_ua js-lang-switch"]')
        elif str("Каталог товарів") in self.driver.page_source:
            elem = self.driver.find_element_by_xpath('//*[@class="store-switcher__link store-switcher__link_ru js-lang-switch"]')
        elem.click()
        time.sleep(5)
        self.close_p()
    def searchtr(self):
        self.cre_new_p()
        self.setUp()
        elem = self.driver.find_element_by_xpath('//*[@class="header-search__input digi-autocomplete jc-ignore"]')
        elem.send_keys("Iphone Xs max")
        elem.send_keys(Keys.RETURN)
        time.sleep(10)
        self.close_p()

if __name__=="__main__":
    a=comfy_home()
    a.langtr()
    a.searchtr()

