"""Locators separated by page's elements"""

class HeaderLocators:
    # Header
    LANG_SWITCH = '//*[@id="language-switcher"]/div[2]/a'

    SEARCH = '//*[@id="rz-search"]/form/div[1]/div[2]/input'

    # Sorting
    DROP_DOWN = '//*[@id="sort_view"]/a'
    CHEAP = '//*[@id="filter_sortcheap"]/a'
    EXPENSIVE = '//*[@id="filter_sortexpensive"]/a'
    POPULAR = '//*[@id="filter_sortpopularity"]/a'
    NEW = '//*[@id="filter_sortnovelty"]/a'
    ACTION = '//*[@id="filter_sortaction"]/a'
    RANK = '//*[@id="filter_sortrank"]/a'

    # Product view
    TILE = '//*[@id="filter_viewtile"]/a'
    LIST = '//*[@id="filter_viewlist"]/a'

class MobPhoneLocators:
    # Options

    # Product list

    # Viewed products
