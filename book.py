from exceptions import BookParameterException, EmptyBookParameterException


class Book(object):

    @staticmethod
    def load_books():
        books = []
        with open("bookData.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.split(";")
                b = Book(id=parts[0],
                         title=parts[1],
                         author=parts[2],
                         isbn=parts[3],
                         publisher=parts[4],
                         pages=parts[5])
                books.append(b)
        return books

    @staticmethod
    def save_changes(books):
        with open("bookData.txt", "w", encoding="utf-8") as f:
            for book in books:
                f.write(f"{book.id};{book.title};{book.author};{book.isbn};{book.publisher};{book.pages}\n")

    @staticmethod
    def add_book(**kwargs):
        books = Book.load_books()
        new_book = Book(id=Book.__next_id(), **kwargs)
        print(new_book)
        books.append(new_book)
        Book.save_changes(books)

    @staticmethod
    def remove_book(id_rmv):
        books = Book.load_books()
        removed = books.pop(id_rmv)
        Book.save_changes(books)
        return removed

    @staticmethod
    def edit_book(id_edit, book):
        books = Book.load_books()
        books[id_edit] = book
        Book.save_changes(books)

    @staticmethod
    def display_books():
        books = Book.load_books()
        for book in books:
            print(book)

    @staticmethod
    def __next_id() -> int:
        ids = []
        for book in Book.load_books():
            ids.append(book.id)
        return sorted(ids)[-1]

    def __init__(self, **kwargs):
        if kwargs.get("id"):
            self.id = kwargs.get("id")
        else:
            self.id = self.__next_id()

        self.title = kwargs.get("title")
        self.author = kwargs.get("author")
        self.isbn = kwargs.get("isbn")
        self.publisher = kwargs.get("publisher")
        self.pages = kwargs.get("pages")

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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
        try:
            pages = int(pages)
        except (ValueError, TypeError):
            raise BookParameterException(f"wrong number ({pages}) of pages")
        if pages <= 0:
            raise BookParameterException(f"wrong number ({pages}) of pages")
        self._pages = pages

    def __str__(self):
        return (f"[Id: {self.id}, Title: {self.title}, Author: {self.author}, ISBN: {self.isbn},"
                f" Pages: {str(self.pages)}, Publisher: {self.publisher}]")
