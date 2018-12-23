import os
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


class RozetkaMP(object):
    WEB_LINK = 'https://rozetka.com.ua/mobile-phones/c80003/'

    def __init__(self):
        # chrome_options = Options()
        # chrome_options.headless = True
        self.browser = Chrome(#executable_path=os.path.abspath('chromedriver'),
                              #chrome_options=chrome_options
                )
        self.browser.maximize_window()
        self.browser.get(self.WEB_LINK)
        #sleep(2)

    def sort(self, sort_type):
        self.browser.find_element_by_xpath('//*[@id="sort_view"]/a').click()
        if sort_type == 'cheap':
            self.browser.find_element_by_xpath('//*[@id="filter_sortcheap"]').click()
        elif sort_type == 'expensive':
            self.browser.find_element_by_xpath('//*[@id="filter_sortexpensive"]/a').click()
        elif sort_type == 'popularity':
            self.browser.find_element_by_xpath('//*[@id="filter_sortpopularity"]/a').click()
        elif sort_type == 'novelty':
            self.browser.find_element_by_xpath('//*[@id="filter_sortnovelty"]/a').click()
        elif sort_type == 'action':
            self.browser.find_element_by_xpath('//*[@id="filter_sortaction"]/a').click()
        elif sort_type == 'rank':
            self.browser.find_element_by_xpath('//*[@id="filter_sortrank"]/a').click()

    def compare(self):
        pass

    # Options
    def state(self):
        pass

    def brand(self, name):
        self.browser.find_element_by_xpath('//*[@id="filter_producer_5964"]/label/a/span').click()

    def series(self, name):
        pass

    def credit(self):
        pass

    def conn_type(self, conn_type):
        if conn_type == '2G':
            self.browser.find_element_by_xpath(
                    '//*[@id="filter_standart-svyazi-83148_406358"]/label/a/span').click()
        elif conn_type == '3G':
            self.browser.find_element_by_xpath(
                    '//*[@id="filter_standart-svyazi-83148_406358"]/label/a/span').click()
        elif conn_type == '4G':
            self.browser.find_element_by_xpath(
                    '//*[@id="filter_standart-svyazi-83148_406363"]/label/a/span').click()
        elif conn_type == 'CDMA':
            self.browser.find_element_by_xpath(
                    '//*[@id="filter_standart-svyazi-83148_790316"]/label/a/span').click()

    def seller(self, name='Rozetka'):
        if name == 'Rozetka':
            self.browser.find_element_by_xpath('//*[@id="filter_seller_1"]/label/a/span').click()
        else:
            self.browser.find_element_by_xpath('//*[@id="filter_seller_2"]/label/a/span').click()

    # display options
    def disp_size(self):
        pass

    def disp_res(self):
        pass

    def disp_type(self):
        pass

    def price(self, p_from='', p_to=''):
        self.browser.find_element_by_xpath('//*[@id="price[min]"]').send_keys(p_from)
        self.browser.find_element_by_xpath('//*[@id="price[max]"]').send_keys(p_to)
        self.browser.find_element_by_id('submitprice').click()

    def battery(self):
        pass

    def rom(self):
        pass

    def int_mem(self):
        pass

    def main_cam(self):
        pass

    def front_cam(self):
        pass

    def popular_opts(self):
        pass

    def os_type(self):
        pass

    def color(self):
        pass

    def phone_class(self):
        self.browser.find_element_by_xpath('//*[@id="filter_presetsmartfon"]/label/a/span').click()

rozetka = RozetkaMP()
#rozetka.brand('Xiaomi')
#rozetka.sort('cheap')
rozetka.phone_class()
rozetka.price('', '5000')

