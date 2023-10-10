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
    NO_PHONE_BUTTON = (By.CSS_SELECTOR, '[style*="background: red;"]')
    SAVE_BUTTON = (By.CSS_SELECTOR, '[style="background: rgb(94, 191, 116); color: rgb(255, 255, 255); border: none; '
                                    'border-radius: 4px; width: 30%; height: 100%; display: flex; justify-content: '
                                    'center; align-items: center; text-align: center;"]')

    # time slots:
    DATE_VISIT = (By.CSS_SELECTOR,
                  '[style*="color: rgb(85, 95, 89); position: relative; font-size: 19px; font-weight: 500; width: 100%;'
                  ' box-sizing: border-box; height: 40px; border: 1px solid rgb(201, 201, 201); border-radius: 4px; '
                  'padding: 10px; background-repeat:"]')
    TIME_VISIT = (By.CSS_SELECTOR, '//div[@style="width: 100%; display: flex; flex-direction: column; '
                                   'gap: 10px;"][2]/input')
    DURATION_BOOK = (By.CSS_SELECTOR, '//div[@style="display: flex; gap: 10px;"][2]/div[2]/input')
    # text fields:
    NAME = (By.CSS_SELECTOR, '[name="Имя гостя"]')
    COMMENTS = (By.CSS_SELECTOR, '[name="Комментарий"]')

    # numbers fields:
    COUNT_GUESTS = (By.CSS_SELECTOR, '[style="height: 35px; width: 50px; text-align: center;"]')
    PHONE = (By.CSS_SELECTOR, '[name="Номер телефона"]')

    # others:
    HALLS = (By.XPATH, '//div[3]/select[1]')
    TABLES = (By.XPATH, '//div[3]/select[2]')


class PanelLocators:
    MAIN_BUTTON = (By.XPATH, '//div[@style="display: flex; flex-direction: row; justify-content: space-around; width: '
                             '100%; height: 100%;"]/div[1]')
    RESERVES_BUTTON = (By.XPATH, '//div[@style="display: flex; flex-direction: row; justify-content: space-around; '
                                 'width: 100%; height: 100%;"]/div[2]')
    GUESTS_BUTTON = (By.XPATH, '//div[@style="display: flex; flex-direction: row; justify-content: space-around; '
                               'width: 100%; height: 100%;"]/div[3]')
    SETTINGS_BUTTON = (By.XPATH, '//div[@style="display: flex; flex-direction: row; justify-content: space-around; '
                                 'width: 100%; height: 100%;"]/div[4]')
    CREATE_BOOK = (By.CSS_SELECTOR, '[style*="display: flex; align-items: center; justify-content: center; '
                                       'background: ')

