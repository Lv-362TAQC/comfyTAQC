from selenium import webdriver
from pages.furniture_page import FurniturePage
import logging

logging.basicConfig(level=logging.INFO,
                    format=f'# %(levelname)-8s [%(asctime)s] %(filename)-20s %(funcName)-15s [LINE:%(lineno)s] %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename="logs.log")

if __name__ == "__main__":

    page = FurniturePage()
    page.header.language.get_language()
    page.header.language.switch_language().switch_language()
    page.header.search.search('leptop')
    page.driver.close()
    #


