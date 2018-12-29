from selenium.webdriver import Chrome


class BasePage:
    def __init__(self, browser=None):
        self.browser = browser if browser else Chrome()
