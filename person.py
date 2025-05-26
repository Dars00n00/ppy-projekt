import matplotlib.pyplot as plt
from borrowing import Borrowing
from collections import Counter

from reservation import Reservation


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
        borrowings = [brw for brw in Borrowing.load() if person.id == brw.id_person]
        reservations = [rsr for rsr in Reservation.load_reservations() if person.id == rsr.person_id]




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
                if int(parts[0]) > next_id:
                    next_id = int(parts[0]) + 1
        return next_id

    next_id = loadId()

    def __init__(self,**kwargs):
        if kwargs.get("id"):
            self._id = kwargs["id"]
        else:
            self._id = Person.next_id
            Person.next_id += 1
        self.fname = kwargs.get("fname")
        self.lname = kwargs.get("lname")
        self.address = kwargs.get("address")
        self.phone = kwargs.get("phone")

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id):
        raise AttributeError('ID cannot be changed')

    @property
    def fname(self) -> str:
        return self._fname

    @fname.setter
    def fname(self, fname):
        if not fname or not fname.isalpha():
            raise ValueError('First name cannot be empty and can contain only letters')
        self._fname = fname

    @property
    def lname(self) -> str:
        return self._lname

    @lname.setter
    def lname(self, lname):
        if not lname or not lname.isalpha():
            raise ValueError('Last name cannot be empty and can contain only letters')
        self._lname = lname

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, address):
        if not address:
            raise ValueError('Address cannot be empty')
        self._address = address

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, phone):
        if not phone.isdigit() or len(phone) != 9:
            raise ValueError('Phone number has to be 9 digits')
        self._phone = phone

    def __str__(self):
        return (f"Person id={self.id}, firstname={self.fname}, lastname={self.lname},"
                f"address={self.address}, phone={self.phone}")

