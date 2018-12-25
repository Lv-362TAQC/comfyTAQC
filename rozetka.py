from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from locators import *


class BasePage:
    def __init__(self, browser=None):
        self.browser = browser if browser else Chrome()


class BasePageElement:
    def __init__(self, browser=None):
        self.browser = browser if browser else Chrome()


class Link(BasePageElement):
    def __init__(self, browser, locator):
        super().__init__(browser)
        self.locator = self.browser.find_element(locator)

    def click(self):
        self.locator.click()


class MobilePhonesPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.header = ElementHeader(self.browser)

    def switch_lang(self, language):
        if language == 'RU':
            self.header.switch_to_ru()
        elif language == 'UA':
            self.header.switch_to_ua()
        return self


class ElementHeader(BasePageElement):
    def __init__(self, browser):
        super().__init__(browser)
        self.ru_button = Link(self.browser, 'store-switcher__link_ru')
        self.ua_button = Link(self.browser, 'store-switcher__link_ua')

    def switch_to_ua(self):
        self.ua_button.click()

    def switch_to_ru(self):
        self.ru_button.click()


class ElementOptions(BasePageElement):
    def __init__(self, browser):
        super().__init__(browser)
        # add options logic here


class ElementSorting(BasePageElement):
    def __init__(self, browser):
        super().__init__(browser)
        # add options logic here


class ElementProductList(BasePageElement):
    def __init__(self, browser):
        super().__init__(browser)
        # add ProductList logic here


#print(ElementHeader.__mro__)

rozetka = RozetkaMP()
# rozetka.smartphone_filter()
# rozetka.brand('Xiaomi')
# rozetka.sort('cheap')
rozetka.price('', '5000')

