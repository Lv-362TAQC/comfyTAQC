from selenium.webdriver.common.keys import Keys
from page_objects.mobile_phone_page import MobilePhonesPage


a = MobilePhonesPage()
a.header.switch_lang().click()
#a.switch_view.switch_view('list')
