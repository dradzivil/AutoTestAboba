from pages.book_page import BookPage


class TestBookPage:

    def test_book(self, browser):
        url = 'https://ui.aboba.studio/main'
        book_page = BookPage(browser, url)
        book_page.open()
        book_page.sign_in()
        book_page.fill_name_and_save('das_ha')


