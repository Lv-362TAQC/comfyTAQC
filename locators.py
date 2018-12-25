from selenium.webdriver.common.by import By


class MobilePhonesPage:
    """For maintainability we can separate web objects by page name"""
    # Options
    # Sorting
    DROP_DOWN   = (By.XPATH, '//*[@id="sort_view"]/a')
    CHEAP       = (By.XPATH, '//*[@id="filter_sortcheap')
    EXPENSIVE   = (By.XPATH, '//*[@id="filter_sortexpensive"]/a')
    POPULAR     = (By.XPATH, '//*[@id="filter_sortpopularity"]/a')
    NEW         = (By.XPATH, '//*[@id="filter_sortnovelty"]/a')
    ACTION      = (By.XPATH, '//*[@id="filter_sortaction"]/a')
    RANK        = (By.XPATH, '//*[@id="filter_sortrank"]/a')
    TILE        = (By.XPATH, '//*[@id="filter_viewtile"]/a')
    LIST        = (By.XPATH, '//*[@id="filter_viewlist"]/a')
    # Product list
    # Viewed products
