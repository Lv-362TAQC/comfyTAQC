from page_elements.base_page_element import BasePageElement
from locators.locators import MobPhoneLocators as locs


class Link(BasePageElement):
    def __init__(self, driver, locator):
        super().__init__(driver)
        self.locator = self.driver.find_element_by_xpath(locator)

    def click(self):
        self.locator.click()


class HeaderElement(BasePageElement):
    def __init__(self, driver):
        super().__init__(driver)
        self.switch = Link(self.driver, locs.LANG_SWITCH)

    def switch_lang(self):
        self.switch.click()


class ElementSorting(BasePageElement):
    def __init__(self, driver):
        super().__init__(driver)
        self.sort = Link(self.driver, locs.DROP_DOWN)
        self.cheap = Link(self.driver, locs.CHEAP)
        self.expensive = Link(self.driver, locs.EXPENSIVE)
        self.popular = Link(self.driver, locs.POPULAR)
        self.new = Link(self.driver, locs.NEW)
        self.action = Link(self.driver, locs.ACTION)
        self.rank = Link(self.driver, locs.RANK)

    def switch_sort(self, opt):
        self.sort.click()
        if opt == 'cheap':
            self.cheap.click()
        elif opt == 'expensive':
            self.expensive.click()
        elif opt == 'popular':
            self.popular.click()
        elif opt == 'new':
            self.new.click()
        elif opt == 'action':
            self.action.click()
        # elif opt == 'rank':
        #     self.rank.click()
        return self


class ElementView(BasePageElement):
    def __init__(self, driver):
        super().__init__(driver)
        self.tile = Link(self.driver, locs.TILE)
        self.list = Link(self.driver, locs.LIST)

    def switch_view(self, view_type):
        if view_type == 'tile':
            self.tile.click()
        elif view_type == 'list':
            self.list.click()
        return self


class ElementOptions(BasePageElement):
    def __init__(self, driver):
        super().__init__(driver)
        # add options logic here


class ElementProductList(BasePageElement):
    def __init__(self, driver):
        super().__init__(driver)
        # add ProductList logic here
