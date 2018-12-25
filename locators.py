from selenium.webdriver.common.by import By

# furniture header
class Header:
    # Commercial banner
    HEAD_BANNER = (By.NAME, 'head_banner')
    LANG_SWITCHER = (By.XPATH, '//div[@class="lang-switcher-i"]/a[@class="lang-switcher-link whitelink"]')
    SIGHN_IN = (By.NAME, 'signin')

    FAQ_LINK = (By.XPATH, '//ul[@name="header-top-menu"]/li/a[@href="https://rozetka.com.ua/ua/faq/"]')
    CREDIT_LINK = (By.XPATH, '//ul[@name="header-top-menu"]/li/a[@href="https://rozetka.com.ua/ua/credit/"]')
    DELIVERY_LINK = (By.XPATH, '//ul[@name="header-top-menu"]/li/'
                               'a[@href="https://rozetka.com.ua/ua/payments-and-deliveries/"]')
    GUARANTEE_LINK = (By.XPATH, '//ul[@name="header-top-menu"]/li/a[@href="https://rozetka.com.ua/ua/warranty/"]')
    CONTACTS_LINK = (By.XPATH, '//ul[@name="header-top-menu"]/li/a[@href="https://rozetka.com.ua/ua/contacts/"]')
    TRACK_THE_ORDER_LINK = (By.XPATH, '//ul[@name="header-top-menu"]/li/'
                                      'a[@href="https://my.rozetka.com.ua/ua/profile/account/#details"]')
    SELL_ON_ROZETKA_LINK = (By.XPATH, '//ul[@name="header-top-menu"]/li/a[@href="https://rozetka.com.ua/ua/newseller/"]')

    LOGO_LINK = (By.CLASS_NAME, 'logo-link')
    CITY_CHOOSER = (By.ID, 'city-chooser')
    SEARCH_FILD = (By.CLASS_NAME, 'rz-header-search-input-text')
    SEARCH_VOICE_BTN = (By.CLASS_NAME, 'rz-header-search-voice-link')
    SEARCH_BTN = (By.CLASS_NAME, 'js-rz-search-button')

    TRY_PREMIUM_BTN = (By.CLASS_NAME, 'hub-i-premium')
    COMPARE_BTN = (By.CLASS_NAME, 'hub-i-comparison-link')
    WISH_BTN = (By.CLASS_NAME, 'hub-i-wishlist-link')
    CART_BTN = (By.CLASS_NAME, 'hub-i-cart-link')
    # Choose city popup
    CHANGE_REGION = (By.NAME, 'city')


class SideBarMenu:
    FRAMELESS_FURNITURE = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                     'a[@href="https://rozetka.com.ua/ua/beskarkasnaya-mebel/c154006/"]')
    COMPUTER_TABLES = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                 'a[@href="https://rozetka.com.ua/ua/kompyuternye-stoly/c155285/"]')
    DINNER_TABLES = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                               'a[@href="https://rozetka.com.ua/ua/obedennye-stoly/c2796732/"]')
    COFFY_TABLES = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                              'a[@href="https://rozetka.com.ua/ua/jurnalnye-stoly/c2798167/"]')
    OFFICE_CHAIRS = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                               'a[@href="https://rozetka.com.ua/ua/ofisnye-kresla-i-stulya/c154072/"]')
    ERGONOMICS_WORKPLACE = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                      'a[@href="https://rozetka.com.ua/ua/ergonomika-rabochego-mesta/c4630662/"]')
    Chairs_AND_stools = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                   'a[@href="https://rozetka.com.ua/ua/stulya-i-taburety/c154084/"]')
    GARDEN_PAVILIONS = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                  'a[@href="https://rozetka.com.ua/ua/sadovye-pavilony/c91290/"]')
    GARDEN_SWINGS = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                               'a[@href="https://rozetka.com.ua/ua/sadovye-kacheli/c91291/"]')
    Folding_furniture = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                   'a[@href="https://rozetka.com.ua/ua/furniture/c82672/"]')
    GARDEN_FURNITURE = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                  'a[@href="https://rozetka.com.ua/ua/plastikovaya-mebel/c3130405/"]')
    SUNBEDS = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                         'a[@href="https://rozetka.com.ua/ua/shezlongi/c4625403/"]')
    FIXTURE_FOR_TV = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                'a[@href="https://rozetka.com.ua/ua/tv-mounts-stands/c80071/"]')
    TABLES_FOR_LAPTOPS = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                    'a[@href="https://rozetka.com.ua/ua/notebook_stands/c183690/24628=14700/"]')
    MATTRESSES = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                            'a[@href="https://rozetka.com.ua/ua/mattress/c177055/"]')
    BEDS = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                      'a[@href="https://rozetka.com.ua/ua/krovati/c4627785/"]')
    SOFAS = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                       'a[@href="https://rozetka.com.ua/ua/divany/c4627575/"]')
    ARMCHAIRS_AND_POUFFES = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                       'a[@href="https://rozetka.com.ua/ua/kresla-i-pufiki/c4627792/"]')
    SCREENS = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                         'a[@href="https://rozetka.com.ua/ua/shirmy/c4629270/"]')
    STANDS_FOR_FLOWERS = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                    'a[@href="https://rozetka.com.ua/ua/podstavki-dlya-cvetov/c4629031/"]')
    DECOR_FOR_HOME = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                'a[@href="https://rozetka.com.ua/ua/decoration_for_home/c375695/"]')
    FURNITURE_FOR_HALLWAY = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                          'a[@href="https://rozetka.com.ua/ua/mebelj-v-prikhozhuyu/c4628982/"]')
    TABLES_STANDS_FOR_SHOES = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                         'a[@href="https://rozetka.com.ua/ua/podstavki-dlya-obuvi/c4652751/"]')
    MASSAGE_CHAIRS = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                'a[@href="https://rozetka.com.ua/ua/massazhnye-kresla/c4629129/"]')
    NIGHTSTAND = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                            'a[@href="https://rozetka.com.ua/ua/tumbochki/c4629185/"]')
    SHELVES = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                         'a[@href="https://rozetka.com.ua/ua/polki/c4629192/"]')
    SHELVING = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                          'a[@href="https://rozetka.com.ua/ua/stellaji/c4629178/"]')
    TV_HOLDER = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                           'a[@href="https://rozetka.com.ua/ua/tumbochki/c4629185/tip116138=tumbi-pod-televizor/"]')
    BATHROOM_FURNITURE = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                    'a[@href="https://bt.rozetka.com.ua/ua/mebel-dlya-vannoy-komnaty/c155548/"]')
    ETAGERKI = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                          'a[@href="https://rozetka.com.ua/ua/etagerki/c4652744/"]')
    MIRRORS = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                         'a[@href="https://rozetka.com.ua/ua/zerkala4630668/c4630668/"]')
    WARDRODES = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                           'a[@href="https://rozetka.com.ua/ua/shkafi-kupe/c4630461/"]')
    ACCESSORIES_FOR_FURNITURE = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/a[@href="https://'
                                           'rozetka.com.ua/ua/komplektuyushchie-dlya-ofisnih-kresel/c4631397/"]')
    FURNITURE_ACCESSORIES = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/'
                                       'a[@href="https://rozetka.com.ua/ua/mebelnaya-furnitura4630013/c4630013/"]')
    STORAGE_AND_SPACE_ORGANIZATION = (By.XPATH, '//*[@id="menu_categories_left"]/li/p/a[@href="'
                                                'https://rozetka.com.ua/ua/yhod-i-hranenie-odejdy-i-obyvi/c4629263/"]')


class PopularProduct:
    ''


class Feedback:
    ''



class Popup:
    CLOSE_COMMR_POPUP = (By.CLASS_NAME, 'exponea-close-cross')
    CLOSE_LANG_POPUP = (By.CLASS_NAME, 'popup-close')

