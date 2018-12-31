from selenium import webdriver


class BasePageElement:
    def __init__(self, driver):
        self.driver = driver if driver else webdriver.Chrome()

    def _reload(self):
        self.__init__(self.driver)
