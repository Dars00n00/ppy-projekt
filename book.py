from exceptions import WrongBookParameterException, MultipleErrorsException
from borrowing import Borrowing
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from collections import Counter


class Book(object):

    @staticmethod
    def display_stats():
        books = Book.load_books()
        borrowing = Borrowing.load()

        counter = Counter()

        for brw in borrowing:
            if brw.returned:
                counter[brw.id_book] += 1

        id_to_title = {book.id: book.title for book in books}
        books_ids = list(counter.keys())
        titles = [id_to_title.get(b) for b in books_ids]
        counts = [counter[b] for b in books_ids]

        plt.bar(titles, counts, color='blue')
        plt.xlabel("Tytuł książki")
        plt.ylabel("liczba wypożyczeń")
        plt.title("Częstotliwość wypożyczeń książek")
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def load_books():
        books = []
        with open("bookData.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.split(";")
                book = Book(id=int(parts[0]), title=parts[1], author=parts[2],
                            isbn=parts[3], publisher=parts[4], pages=parts[5])
                books.append(book)
        return books

    @staticmethod
    def save_changes(books):
        with open("bookData.txt", "w", encoding="utf-8") as file:
            for book in books:
                file.write(f"{book.id};{book.title};{book.author};{book.isbn};{book.publisher};{book.pages}\n")

    @staticmethod
    def add_book(**kwargs):
        books = Book.load_books()
        print(books)
        new_book = Book(id=Book.next_id(), **kwargs)
        books.append(new_book)
        Book.save_changes(books)
        print("Dodano nową książkę: " + str(new_book))

    @staticmethod
    def remove_book(id_rmv):
        books = Book.load_books()
        for list_index, book in enumerate(books):
            if id_rmv == book.id:
                removed = books.pop(list_index)
                print("Usunięto książkę " + str(removed))
                break
        Book.save_changes(books)

    @staticmethod
    def edit_book(id_edit, edited_book):
        books = Book.load_books()
        for list_index, book in enumerate(books):
            if id_edit == book.id:
                books[list_index] = edited_book
                break
        Book.save_changes(books)

    @staticmethod
    def display_books():
        books = Book.load_books()
        for book in books:
            print(book)

    @staticmethod
    def next_id() -> int:
        books = Book.load_books()
        if not books:
            return 1
        ids = [book.id for book in books]
        return max(ids) + 1

    def __init__(self, **kwargs):
        self.errors = []
        self.id = kwargs.get("id")
        self.title = kwargs.get("title")
        self.author = kwargs.get("author")
        self.isbn = kwargs.get("isbn")
        self.publisher = kwargs.get("publisher")
        self.pages = kwargs.get("pages")

        if len(self.errors) > 0:
            raise MultipleErrorsException(self.errors)

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id):
        try:
            self._id = int(id)
        except (ValueError, TypeError):
            self.errors.append(WrongBookParameterException("id", id))
            self._id = id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str):
        if title is None or not isinstance(title, str) or title.strip() == "":
            self.errors.append(WrongBookParameterException("title", title))
            self._title = title
        else:
            self._title = title.strip()

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author: str):
        if author is None or not isinstance(author, str) or author.strip() == "":
            self.errors.append(WrongBookParameterException("author", author))
            self._author = author
        else:
            self._author = author.strip()

    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, isbn: str):
        if isbn is None or not isinstance(isbn, str) or isbn.strip() == "":
            self.errors.append(WrongBookParameterException("author", isbn))
            self._author = isbn
        else:
            self._isbn = isbn.strip()

    @property
    def publisher(self) -> str:
        return self._publisher

    @publisher.setter
    def publisher(self, publisher: str):
        if not publisher or not isinstance(publisher, str) or publisher.isspace():
            self.errors.append(WrongBookParameterException("publisher", publisher))
        self._publisher = publisher.strip()

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages):
        try:
            pages = int(pages)
            if pages <= 0:
                self.errors.append(WrongBookParameterException("pages", str(pages)))
        except (ValueError, TypeError):
            self.errors.append(WrongBookParameterException("pages", pages))
        self._pages = pages

    def __str__(self):
        return (f"Book id={self.id}, Title={self.title}, Author={self.author}, ISBN={self.isbn},"
                f" Pages={str(self.pages)}, Publisher={self.publisher}")
