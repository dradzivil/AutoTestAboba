from selenium.webdriver.common.by import By
import random

class AuthenticationPageLocators:

    LOGIN = (By.CSS_SELECTOR, '#UserName')
    PASSWORD = (By.CSS_SELECTOR, '#Password')
    SIGN_IN_BUTTON = (By.XPATH, '//input[@value="Войти"]')

class CreateWindowLocators:
    # buttons:
    MINUS_GUEST = (By.CSS_SELECTOR, '[viewBox="0 0 14 2"]')
    PLUS_GUEST = (By.CSS_SELECTOR, '[viewBox="0 0 14 14"]')
    NO_PHONE_BUTTON = (By.XPATH, '//div[@class="generic-phone-input__container"]/div')
    SAVE_BUTTON = (By.XPATH, '//div[@class="popup__buttons"]/div')

    # time slots:
    DATE_VISIT = (By.XPATH, '//input[@class="generic-date-input__content no-select"]')
    TIME_VISIT = (By.XPATH, '//input[@class="generic-time-input__input no-select"][0]')
    DURATION_BOOK = (By.XPATH, '//input[@class="generic-time-input__input no-select"][1]')

    # text fields:
    NAME = (By.CSS_SELECTOR, '[name="Имя гостя"]')
    COMMENTS = (By.CSS_SELECTOR, '[name="Комментарий"]')

    # numbers fields:
    COUNT_GUESTS = (By.XPATH, 'input[class="no-select"]')
    PHONE = (By.CSS_SELECTOR, '[name="Номер телефона"]')

    # others:
    HALLS = (By.XPATH, '//div[@class="popup-reserve__selectors"]/select[1]')
    TABLES = (By.XPATH, '//div[@class="popup-reserve__selectors"]/select[2]')


class PanelLocators:

    MAIN_BUTTON = (By.XPATH, '//div[@class="tab-panel__container"]/div[1]')
    RESERVES_BUTTON = (By.XPATH, '//div[@class="tab-panel__container"]/div[2]')
    GUESTS_BUTTON = (By.XPATH, '//div[@class="tab-panel__container"]/div[3]')
    SETTINGS_BUTTON = (By.XPATH, '//div[@class="tab-panel__container"]/div[4]')
    CREATE_BOOK = (By.CSS_SELECTOR, '[class="header__create-reserve-button"]')

class ReserveLocators:

    TIMES = (By.CSS_SELECTOR, '[class="reserve-line__time"]')
