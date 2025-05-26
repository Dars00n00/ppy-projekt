import matplotlib.pyplot as plt
from book import Book
from borrowing import Borrowing
from collections import Counter
from exceptions import WrongPersonParameterException, MultipleErrorsException


class Person:

    @staticmethod
    def display_stats():
        people = Person.load()
        borrowing = Borrowing.load()

        counter = Counter()

        for brw in borrowing:
            if brw.returned:
                counter[brw.id_book] += 1

        id_to_fullname = {p.id: p.fname + " " + p.lname for p in people}
        ppl_ids = list(counter.keys())
        names = [id_to_fullname.get(p) for p in ppl_ids]
        counts = [counter[p] for p in ppl_ids]

        plt.bar(names, counts, color='green')
        plt.xlabel("Dane czytelnika")
        plt.ylabel("Częstotliwość wypożyczeń książek")
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def display_person_stats(person):
        from reservation import Reservation  # wywalało błąd z cyklicznymi importami
        books = Book.load_books()
        borrowings = Borrowing.load()
        reservations = Reservation.load_reservations()

        id_book_to_title = {b.id: b.title for b in books}
        person_borrowings = [brw for brw in borrowings if person.id == brw.id_person]
        person_reservations = [rsr for rsr in reservations if person.id == rsr.person_id]

        borrowings_counter = Counter(brw.id_book for brw in person_borrowings)
        reservations_counter = Counter(rsr.book_id for rsr in person_reservations)

        all_books_ids = list(set(borrowings_counter.keys()).union(set(reservations_counter.keys())))

        titles = [id_book_to_title.get(b_id) for b_id in all_books_ids]
        borrowing_counts = [borrowings_counter.get(b_id, 0) for b_id in all_books_ids]
        reservation_counts = [reservations_counter.get(b_id, 0) for b_id in all_books_ids]

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

        ax1.bar(titles, borrowing_counts, color="blue")
        ax1.set_ylabel("Liczba wypożyczeń")
        ax1.set_title("Wypożyczenia czytelnika " + person.fname + " " + person.lname)
        ax1.grid(True, axis="y")

        ax2.bar(titles, reservation_counts, color="green")
        ax2.set_ylabel("Liczba rezerwacji")
        ax2.set_title("Rezerwacje czytelnika " + str(person.fname) + " " + str(person.lname))
        ax2.grid(True, axis="y")

        plt.xticks(rotation=90)
        plt.xlabel("Tytuł książki")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def load():
        arr = []
        with open("personData.txt", 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(';')
                arr.append(Person(id=int(parts[0]), fname=parts[1], lname=parts[2], address=parts[3], phone=parts[4]))
        return arr

    @staticmethod
    def save(p):
        with open("personData.txt", 'w', encoding='utf-8') as f:
            for i in range(len(p)):
                line = f"{p[i].id};{p[i].fname};{p[i].lname};{p[i].address};{p[i].phone}\n"
                f.write(line)

    @staticmethod
    def loadId():
        next_id = 0
        with open("personData.txt", 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(';')
                if int(parts[0]) >= next_id:
                    next_id = int(parts[0]) + 1
        return next_id

    @staticmethod
    def next_id(self):
        people = Person.load()
        if not people:
            return 1
        ids = [book.id for book in people]
        return max(ids) + 1
    next_id = loadId()

    def __init__(self, **kwargs):
        self.errors = []
        if kwargs.get("id"):
            self._id = kwargs.get("id")
        else:
            self._id = Person.next_id
            Person.next_id += 1
        self.fname = kwargs.get("fname")
        self.lname = kwargs.get("lname")
        self.address = kwargs.get("address")
        self.phone = kwargs.get("phone")

        if len(self.errors) > 0:
            raise MultipleErrorsException(self.errors)

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id):
        self.errors.append(WrongPersonParameterException("id", "id cannot be changed"))
        #raise AttributeError('ID cannot be changed')

    @property
    def fname(self) -> str:
        return self._fname

    @fname.setter
    def fname(self, fname):
        if not fname or not fname.isalpha():
            self.errors.append(WrongPersonParameterException("fname", str(fname)))
        self._fname = fname

    @property
    def lname(self) -> str:
        return self._lname

    @lname.setter
    def lname(self, lname):
        if not lname or not lname.isalpha():
            self.errors.append(WrongPersonParameterException("lname", str(lname)))
        self._lname = lname

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, address):
        if not address:
            self.errors.append(WrongPersonParameterException("address", str(address)))
        self._address = address

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, phone):
        if not phone.isdigit() or len(phone) != 9:
            self.errors.append(WrongPersonParameterException("phone", str(phone)))
        self._phone = phone

    def __str__(self):
        return (f"Person id={self.id}, firstname={self.fname}, lastname={self.lname},"
                f"address={self.address}, phone={self.phone}")

