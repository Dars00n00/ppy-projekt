class Person:

    @staticmethod
    def loadId():
        next_id = 0
        with open("personData.txt", 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(';')
                next_id = int(parts[0]) + 1
        return next_id

    next_id = loadId()

    def __init__(self, fname, lname, address, phone):
        self._id = Person.next_id
        Person.next_id += 1
        self.fname = fname
        self.lname = lname
        self.address = address
        self.phone = phone
        self.save()

    def save(self):
        with open("personData.txt", 'a', encoding='utf-8') as f:
            line = f"{self.id};{self.fname};{self.lname};{self.address};{self.phone}\n"
            f.write(line)

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


p = Person("Marek", "Szpak", "wd awafw awf", "643623255")

