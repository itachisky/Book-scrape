import requests

from pages.pages import BooksPages

page_content = requests.get("http://books.toscrape.com").content
page = BooksPages(page_content)

books = page.books

for page_num in range(1, page.page_count):
    url = f"http://books.toscrape.com/catalogue/page-{page_num+1}.html"
    page_content = requests.get(url).content
    pages_info = BooksPages(page_content)
    books.extend(pages_info.books)



