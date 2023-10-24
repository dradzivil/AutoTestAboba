from pages.book_page import BookPage
import datetime as dt

class TestBookPage:

    def sign_in(self, browser):
        url = 'https://ui.aboba.studio/main'
        book_page = BookPage(browser, url)
        book_page.open()
        book_page.sign_in()
        return book_page

    def test_sign_in(self, browser):
        self.sign_in(browser)
        assert True


    def test_book_1(self, browser):
        book_page = self.sign_in(browser)
        book_page.fill_and_save(name='book_1')
        assert True

    def test_book_2(self, browser):
        book_page = self.sign_in(browser)
        book_page.fill_and_save(name='book_2', date=str(dt.date.today()))
        assert True

    def test_book_3(self, browser):
        book_page = self.sign_in(browser)
        date = (dt.date.today()+dt.timedelta(days=1))
        book_page.fill_and_save(name='book_3', date=date.strftime('%Y-%m-%d'), time_visit='12:00')
        assert True

    def test_book_4(self, browser):
        book_page = self.sign_in(browser)
        book_page.fill_and_save(name='book_4', dur='01:00:00')
        assert True

    def test_book_5(self, browser):
        book_page = self.sign_in(browser)
        book_page.fill_and_save(name='book_5', hall='Терраса')
        assert True

    def test_book_6(self, browser):
        book_page = self.sign_in(browser)
        book_page.fill_and_save(name='book_6', table='K1000')
        assert True

    def test_book_7(self, browser):
        book_page = self.sign_in(browser)
        book_page.fill_and_save(name='book_7', phone='+7(777)-777-77-77')
        assert True


    def test_book_8(self, browser):
        book_page = self.sign_in(browser)
        book_page.fill_and_save(name='book_8', comments='book_8')
        assert True


    def test_book_9(self, browser):
        book_page = self.sign_in(browser)
        date = dt.date.today() + dt.timedelta(days=1)
        book_page.fill_and_save(name='book_9', comments='book_9', phone='+7(777)-777-77-77', table='K1000', hall='Холл',
                                dur='2:00', date=date.strftime('%d.%m.%Y'), time_visit='12:00')
        assert True

    def test_find_book_1(self, browser):
        pass

