from locators import *
from elements.base_page_element import BasePageElement
from selenium.common.exceptions import NoSuchElementException
import logging


class HeaderElement(BasePageElement):
    def __init__(self, driver=None):
        super().__init__(driver)
        self.language = Language(self.driver)
        self.search = SearchProduct(self.driver)


class Language(BasePageElement):
    def __init__(self, driver=None):
        super().__init__(driver)

    def get_language(self):
        try:
            return self.driver.find_element(*Header.LANG_SWITCHER).get_attribute('data-lang')
        except NoSuchElementException:
            logging.warning(f'# NoSuchElementException {Header.LANG_SWITCHER[0]} {Header.LANG_SWITCHER[1]}')

    def switch_language(self):
        try:
            self.driver.find_element(*Header.LANG_SWITCHER).click()
            logging.info(f'# Clicked on {Header.LANG_SWITCHER}')
            self._reload()
        except NoSuchElementException:
            logging.warning(f'# NoSuchElementException {Header.LANG_SWITCHER}')
        finally:
            return self


class SearchProduct(BasePageElement):
    def __init__(self, driver=None):
        super().__init__(driver)

    def search(self, product):
        try:
            self.driver.find_element(*Header.SEARCH_FILD).send_keys(product)
            logging.info(f'# Typed \'{product}\' in {Header.SEARCH_FILD}')
        except NoSuchElementException:
            logging.warning(f'# NoSuchElementException {Header.SEARCH_FILD}')
        else:
            try:
                self.driver.find_element(*Header.SEARCH_BTN).click()
                logging.info(f'# Clicked on {Header.SEARCH_BTN}')
            except NoSuchElementException:
                logging.warning(f'# NoSuchElementException {Header.SEARCH_BTN}')
        finally:
            return self