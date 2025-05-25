class Person:

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
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        raise AttributeError('ID cannot be changed')

    @property
    def fname(self):
        return self._fname

    @fname.setter
    def fname(self, fname):
        if not fname or not fname.isalpha():
            raise ValueError('First name cannot be empty and can contain only letters')
        self._fname = fname

    @property
    def lname(self):
        return self._lname

    @lname.setter
    def lname(self, lname):
        if not lname or not lname.isalpha():
            raise ValueError('Last name cannot be empty and can contain only letters')
        self._lname = lname

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if not address:
            raise ValueError('Address cannot be empty')
        self._address = address

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if not phone.isdigit() or len(phone) != 9:
            raise ValueError('Phone number has to be 9 digits')
        self._phone = phone

    def __str__(self):
        return (f"Person id={self.id}, firstname={self.fname}, lastname={self.lname}, "
                f"address={self.address}, phone={self.phone}")

ps = Person.load()
ps.append(Person(fname="Marek", lname="Szpak", address="wd awafw awf", phone="643623255"))
ps.pop()
for person in ps:
    print(person.id, person.fname, person.lname, person.address, person.phone)
Person.save(ps)