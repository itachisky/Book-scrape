from bs4 import BeautifulSoup
import re

from locators.all_book_page import AllBookPage
from parsers.parsers import Parsers


class BooksPages:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    @property
    def books(self):
        return [Parsers(e) for e in self.soup.select(AllBookPage.Books)]

    @property
    def page_count(self):
        content = self.soup.select_one(AllBookPage.Pager).string
        pattern = "Page [0-9]+ of ([0-9]+)"
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        return pages
