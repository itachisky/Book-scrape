import re

from locators.book_info import BookInfo


class Parsers:

    Ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"Book Name: {self.book_name} at {self.book_price} rated {self.book_ratings}"

    @property
    def book_name(self):
        locator = BookInfo.Book_name
        item_link = self.parent.select_one(locator)
        book_name = item_link.attrs["title"]
        return book_name

    @property
    def book_link(self):
        locator = BookInfo.Link_book
        item_link = self.parent.select_one(locator)
        book_link = item_link.attrs["href"]
        return book_link

    @property
    def book_price(self):
        locator = BookInfo.Book_price
        item_price = self.parent.select_one(locator).string

        pattern = "£([0-9]+\.[0-9]+)"
        book_price = re.search(pattern, item_price)
        return float(book_price.group(1))

    @property
    def book_ratings(self):
        locator = BookInfo.book_rating
        item_rating = self.parent.select_one(locator)

        classes = item_rating.attrs["class"]
        book_rating = [r for r in classes if r != "star-rating"]
        ratings = Parsers.Ratings.get(book_rating[0])
        return ratings

