from book import Book
from exceptions import WrongReservationParameterException
from datetime import date, datetime
from person import Person


class Reservation:

    @staticmethod
    def load_reservations():
        reservations = []
        with open("reservationData.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.split(";")
                r = Reservation(id=int(parts[0]),
                                person_id=int(parts[1]),
                                book_id=int(parts[2]),
                                begin_date=parts[3],
                                end_date=parts[4])
                reservations.append(r)
        return reservations

    @staticmethod
    def save_changes(reservations):
        with open("reservationData.txt", "w", encoding="utf-8") as f:
            for r in reservations:
                f.write(f"{r.id};{r.person_id};{r.book_id};{r.begin_date};{r.end_date}\n")

    @staticmethod
    def add_reservation(**kwargs):
        reservations = Reservation.load_reservations()
        new_reservation = Reservation(id=Reservation.next_id(), **kwargs)
        reservations.append(new_reservation)
        Reservation.save_changes(reservations)
        print("dodano rezerwację: " + str(new_reservation))

    @staticmethod
    def remove_reservation(id_rmv):
        reservations = Reservation.load_reservations()
        removed = reservations.pop(id_rmv)
        Reservation.save_changes(reservations)
        return removed

    @staticmethod
    def edit_reservation(id_edit, reservation):
        reservations = Reservation.load_reservations()
        reservations[id_edit] = reservation
        Reservation.save_changes(reservations)

    @staticmethod
    def display_reservations():
        reservations = Reservation.load_reservations()
        books = Book.load_books()
        people = Person.load()

        if len(reservations) == 0:
            print("brak rezerwacji")
        else:
            for r in reservations:
                person = people[r.person_id]
                book = books[r.book_id]

                print(f"{r}\n{person}\n{book}\n")

    @staticmethod
    def next_id() -> int:
        ids = []
        for r in Reservation.load_reservations():
            ids.append(r.id)
        if len(ids) == 0:
            return 0
        else:
            return int(sorted(ids)[-1])+1

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.person_id = kwargs.get("person_id")
        self.book_id = kwargs.get("book_id")
        self.begin_date = kwargs.get("begin_date")
        self.end_date = kwargs.get("end_date")

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int):
        if id is None or not isinstance(id, int):
            raise WrongReservationParameterException("id", str(id))
        self._id = id

    @property
    def person_id(self) -> int:
        return self._person_id

    @person_id.setter
    def person_id(self, person_id: int):
        if person_id is None or not isinstance(person_id, int):
            raise WrongReservationParameterException("person_id", str(person_id))
        self._person_id = person_id

    @property
    def book_id(self) -> int:
        return self._book_id

    @book_id.setter
    def book_id(self, book_id: int):
        if book_id is None or not isinstance(book_id, int):
            raise WrongReservationParameterException("book_id", str(book_id))
        self._book_id = book_id

    @property
    def begin_date(self) -> date:
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date: str):
        if begin_date is None:
            raise WrongReservationParameterException("begin_date", str(begin_date))
        if isinstance(begin_date, str):
            try:
                begin_date = datetime.strptime(begin_date.strip(), "%Y-%m-%d").date()
            except ValueError:
                raise WrongReservationParameterException("begin_date (invalid format) (correct format='YYYY-MM-DD')", str(begin_date))
        elif not isinstance(begin_date, date):
            raise WrongReservationParameterException("begin_date", str(begin_date))
        self._begin_date = begin_date

    @property
    def end_date(self) -> date:
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: str):
        if end_date is None:
            raise WrongReservationParameterException("end_date")
        if isinstance(end_date, str):
            try:
                end_date = datetime.strptime(end_date.strip(), "%Y-%m-%d").date()
            except ValueError:
                raise WrongReservationParameterException("end_date (invalid format) (correct format='YYYY-MM-DD')", str(end_date))
        elif not isinstance(end_date, date):
            raise WrongReservationParameterException("end_date", str(end_date))
        self._end_date = end_date

    def __str__(self):
        return (f"Reservation id={self.id}, Person id={self.person_id}, Book id={self.book_id}, "
                f"From={self.begin_date}, To={self.end_date}")
