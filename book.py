from exceptions import BookParameterException, EmptyBookParameterException


class Book(object):

    @staticmethod
    def add_book(**kwargs):
        book = Book(**kwargs)
        print(book)

    @staticmethod
    def remove_book():
        pass

    @staticmethod
    def search_book(title):
        pass

    @staticmethod
    def display_books():
        pass

    def __init__(self, **kwargs):
        self.title = kwargs.get("title")
        self.author = kwargs.get("author")
        self.isbn = kwargs.get("isbn")
        self.publisher = kwargs.get("publisher")
        self.pages = kwargs.get("pages")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title is None or not isinstance(title, str):
            raise EmptyBookParameterException("title")
        if len(title.strip()) <= 0:
            raise BookParameterException("empty title field")
        self._title = title.strip()

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if author is None or not isinstance(author, str):
            raise EmptyBookParameterException("author")
        if len(author.strip()) <= 0:
            raise BookParameterException("empty author field")
        self._author = author.strip()

    @property
    def isbn(self):
        return self._isbn.strip()

    @isbn.setter
    def isbn(self, isbn):
        if isbn is None or not isinstance(isbn, str):
            raise EmptyBookParameterException("isbn")
        if len(isbn.strip()) <= 0:
            raise BookParameterException("empty isbn field")
        self._isbn = isbn.strip()

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        if publisher is None or not isinstance(publisher, str):
            raise EmptyBookParameterException("publisher")
        if len(publisher.strip()) <= 0:
            raise BookParameterException("empty publisher field")
        self._publisher = publisher.strip()

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        pages = int(pages)
        if pages is None or not isinstance(pages, int):
            raise EmptyBookParameterException("pages")
        if pages <= 0:
            raise BookParameterException(f"wrong number ({pages}) of pages")
        self._pages = pages

    def __str__(self):
        return (f"[Title: {self.title}, Author: {self.author}, ISBN: {self.isbn},"
                f" Pages: {str(self.pages)}, Publisher: {self.publisher}]")

