import datetime
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.book_page_locators import CreateWindowLocators as cwLocators
from locators.book_page_locators import PanelLocators as pLocators
from locators.book_page_locators import AuthenticationPageLocators as aLocators


class BookPage(BasePage):

    def sign_in(self):
        self.element_is_visible(aLocators.LOGIN).send_keys("aboba@horeca.com")
        self.element_is_visible(aLocators.PASSWORD).send_keys("12345")
        self.element_is_visible(aLocators.SIGN_IN_BUTTON).click()

    def fill_name_and_save(self, name):
        self.element_is_visible(pLocators.CREATE_BOOK).click()
        self.element_is_visible(cwLocators.NAME).send_keys(name)
        self.element_is_visible(cwLocators.NO_PHONE_BUTTON).click()
        self.element_is_visible(cwLocators.SAVE_BUTTON).click()
        time.sleep(2)

