import time
import datetime as dt

from pages.base_page import BasePage
from locators.book_page_locators import CreateWindowLocators as cwLocators
from locators.book_page_locators import PanelLocators as pLocators
from locators.book_page_locators import AuthenticationPageLocators as aLocators


class BookPage(BasePage):

    def sign_in(self):
        self.element_is_visible(aLocators.LOGIN).send_keys("aboba@horeca.com")
        self.element_is_visible(aLocators.PASSWORD).send_keys("12345")
        self.element_is_visible(aLocators.SIGN_IN_BUTTON).click()

    def fill_and_save(self, date='', time_visit='', count='', dur='', hall='', table='', name='Test',
                      phone='', comments=''):
        self.element_is_visible(pLocators.CREATE_BOOK).click()
        if time_visit:
            self.element_is_visible(cwLocators.TIME_VISIT).send_keys(time_visit)
        if count:
            self.element_is_visible(cwLocators.COUNT_GUESTS).send_keys(count)
        if dur:
            self.element_is_visible(cwLocators.DURATION_BOOK).send_keys(dur)
        if hall:
            self.element_is_visible(cwLocators.HALLS).send_keys(hall)
        if table:
            self.element_is_visible(cwLocators.TABLES).send_keys(table)
        self.element_is_visible(cwLocators.NAME).send_keys(name)
        if phone:
            self.element_is_visible(cwLocators.PHONE).send_keys(phone)
        else:
            self.element_is_visible(cwLocators.NO_PHONE_BUTTON).click()
        if comments:
            self.element_is_visible(cwLocators.COMMENTS).send_keys(comments)
        self.element_is_visible(cwLocators.SAVE_BUTTON).click()
        if date:
            self.element_is_visible(cwLocators.DATE_VISIT).send_keys(value=date)
        time.sleep(1)

    def find_book(self, date=str(dt.date.today()),
                  time_visit=(dt.datetime.now() + dt.timedelta(hours=1)).strftime('%H:00'),
                  count=1, dur='04:00', hall='Холл', table='Стол не назначен', name='',
                  phone='Без номера', comments='Без комментария'):
        pass
