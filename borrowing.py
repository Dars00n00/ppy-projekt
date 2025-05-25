from datetime import datetime

class Borrowing:

    @staticmethod
    def load():
        arr = []
        with open("borrowingData.txt", 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(';')
                arr.append(Borrowing(id_person=int(parts[0]), id_book=int(parts[1]), date_from=parts[2], date_to=parts[3], returned=parts[4]))
        return arr

    @staticmethod
    def save(p):
        with open("borrowingData.txt", 'w', encoding='utf-8') as f:
            for i in range(len(p)):
                line = f"{p[i].id_person};{p[i].id_book};{p[i].date_from};{p[i].date_to};{p[i].returned}\n"
                f.write(line)

    late_return_fee_per_day = 1

    def __init__(self,**kwargs):
        self.id_person = kwargs.get("id_person")
        self.id_book = kwargs.get("id_book")
        if kwargs.get("date_from"):
            self._date_from = kwargs.get("date_from")
            if kwargs.get("returned") == "True":
                self._returned = True
            else:
                self._returned = False
        else:
            self._date_from = datetime.today().date().isoformat()
            self.returned = False
        self.date_to = kwargs.get("date_to")

    def calculate_fee(self):
        due_date = datetime.strptime(self.date_to, '%Y-%m-%d').date()
        today = datetime.today().date()
        days_late = (today - due_date).days
        return self.late_return_fee_per_day * max(days_late, 0)

    @property
    def id_person(self):
        return self._id_person

    @id_person.setter
    def id_person(self, id_person):
        if not id_person:
            raise ValueError('Person ID cannot be empty')
        self._id_person = id_person

    @property
    def id_book(self):
        return self._id_book

    @id_book.setter
    def id_book(self, id_book):
        if not id_book:
            raise ValueError('Book ID cannot be empty')
        self._id_book = id_book

    @property
    def date_from(self):
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        raise AttributeError('From date cannot be changed')

    @property
    def date_to(self):
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        if not date_to:
            raise ValueError('To date cannot be empty')
        try:
            parsedFrom = datetime.strptime(self.date_from, '%Y-%m-%d').date()
            parsedTo = datetime.strptime(date_to, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError('To date must in YYYY-MM-DD format')
        if parsedTo < parsedFrom:
            raise ValueError('To date cannot be before From date')
        self._date_to = date_to

    @property
    def returned(self):
        return self._returned

    @returned.setter
    def returned(self, returned):
        if not returned:
            raise ValueError('Returned cannot be empty')
        self._returned = returned
