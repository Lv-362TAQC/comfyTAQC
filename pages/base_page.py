from selenium import webdriver
from os.path import abspath
from selenium.common.exceptions import WebDriverException
import logging
class BasePage:
    def __init__(self, driver=None):
        try:
            logging.debug('# Finding driver ...')
            self.driver = driver if driver else webdriver.Chrome(abspath('chromedriver'))
            logging.info('# found driver|Opened browser')
        except WebDriverException:
            logging.critical(f'# Did not find driver in path {abspath("chromedriver")}')

    def _reload(self):
        self.__init__(self.driver)

    def __del__(self):
        logging.info('# Closed browser ...')