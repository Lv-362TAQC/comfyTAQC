from selenium.webdriver.common.by import By


class Header:
    # Commercial banner
    TOP_BANNER = (By.NAME, 'head_banner')
    LANG_SWITCHER = (By.XPATH, '//div[@class="lang-switcher-i"]/a[@class="lang-switcher-link whitelink"]')
    LOG_IN_LINK = (By.XPATH, '//span[@id="header_user_menu_parent"]/a')
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
    PRODUCTS_FOR_HOME = (By.CLASS_NAME, '//ul[@class="clearfix breadcrumbs-catalog"]/li/'
                                       'a[@href="https://rozetka.com.ua/ua/tovary-dlya-doma/c2394287/"]')
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


class Footer:
    SCHEDULE_CALL_CENTER_LINK = (By.XPATH, '//ul[@class="schedule-l"]/li/'
                                      'a[@href="https://rozetka.com.ua/ua/contacts/"]')
    #
    BONUS_ACCOUNT = (By.XPATH, '//li[@name="page_loyalty"/a')
    GIFT_CERTIFICATES_LINK = (By.XPATH, '//li[@name="page_gift"]/a')
    RETURNING_GOODS_LINK = (By.XPATH, '//a[@href="https://service.rozetka.com.ua/"]')
    SERVISE_CENTERS_LINK = (By.XPATH, '//a[@href="https://rozetka.com.ua/ua/service-centers/"]')
    FAQ_LINK = (By.XPATH, '//a[@href="https://rozetka.com.ua/ua/faq/"]')
    TERMS_LINK = (By.XPATH, '//a[@href="https://rozetka.com.ua/ua/terms/"]')
    #
    ABOUT_US_LINK = (By.XPATH, '//a[@href="https://rozetka.com.ua/ua/about/"]')
    CONTACTS_LINK = (By.XPATH, '//a[@href="https://rozetka.com.ua/ua/contacts/"]')
    PARTNERSHIP_LINK = (By.XPATH, '//a[@href="https://rozetka.com.ua/ua/partnership/"]')
    SELL_ON_ROZETKA_LINK = (By.XPATH, '//a[@href="https://rozetka.com.ua/ua/newseller/"]')
    VACANCY_LINK = (By.XPATH, '//a[@href="https://rozetka.com.ua/ua/jobs/"]')
    TRANSFER_CARD_TO_CARD_LINK = (By.XPATH, '//a[@href="https://rozetka.com.ua/ua/jobs/"]')
    #
    EMAIL_FIELD = (By.NAME, 'email')
    SUBSCRIBE_BTN = (By.XPATH, '//span[@class="newsletter-subscription-btn"/button')
    #OWOX
    OWOX_LINK = (By.CLASS_NAME, 'logo-owox-link')
    #Social media
    FACEBOOK_LINK = (By.XPATH, '//a[@title="Facebook"]')
    TWITTER_LINK = (By.XPATH, '//a[@title="Twitter"]')
    GOOGLE_PLUS_LINK = (By.XPATH, '//a[@title="Google+"]')
    YOUTUBE_LINK = (By.XPATH, '//a[@title="YouTube"]')
    INSTAGRAM_LINK = (By.XPATH, '//a[@title="Instagram"]')
    VIBER_LINK = (By.XPATH, '//a[@title="Vider"]')
    #mobile
    APP_STORE_LINK = (By.XPATH, '//a[href="https://rozetka.com.ua/go/https:/itunes.apple.com/app/apple-store/'
                                'id740469631/?pt=3132803&ct=fullversion&at=1000l3MB&mt=8"]/img')
    GOOGLE_PLAY_LINK = (By.XPATH, '//a[href="https://rozetka.com.ua/go/https:/play.google.com/store/apps/'
                                'details/?id=ua.com.rozetka.shop&referrer=utm_source%3Dfullversion%26utm_medium%3Dsite'
                                '%26utm_campaign%3Dfullversion"]/img')
    MOBILE_VERSION_LINK = (By.ID, 'footer-mobile-link')
    #
    VERIFIED_VISA = (By.ID, 'visa_elem')
    MASTERCARD = (By.ID, 'mastercard_elem')


class Popup:
    CLOSE_COMMR_POPUP = (By.CLASS_NAME, 'exponea-close-cross')
    CLOSE_LANG_POPUP = (By.CLASS_NAME, 'popup-close')
