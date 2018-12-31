from pages.base_page import BasePage
from elements.header import HeaderElement, Language
import logging
class FurniturePage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)
        self.PAGE = 'https://rozetka.com.ua/ua/mebel/c152458/'
        self.driver.get(self.PAGE)
        logging.info(f'# Opened {self.PAGE}')
        self.header = HeaderElement(self.driver)

