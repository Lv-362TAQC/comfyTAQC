from selenium.webdriver import Chrome


class BasePageElement:
    def __init__(self, driver=None):
        self.driver = driver if driver else Chrome()

    def _reload(self):
        self.__init__(self.driver)
