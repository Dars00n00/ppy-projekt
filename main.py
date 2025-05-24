from book import Book
from person import Person


print("============System zarządzania biblioteką============")

print("  1) wpisz 1 aby dodać nową książkę")
print("  2) wpisz 2 aby usunąć książkę")
print("  3) wpisz 3 aby edytować książkę")
print("  4) wpisz 4 aby wyświetlić informacje o książkach")

print("  5) wpisz 5 aby dodać nowego czytelnika")
print("  6) wpisz 6 aby usunąć czytelnika")
print("  7) wpisz 7 aby edytować czytelnika")
print("  8) wpisz 8 aby wyświetlić informacje o czytelnikach")

print("  9) wpisz 9 aby dodać nowe wypożyczenie")
print(" 10) wpisz 10 aby usunąć wypożyczenie")
print(" 11) wpisz 11 aby edytować wypożyczenie")
print(" 12) wpisz 12 aby wyświetlić informacje o wypożyczeniach")

print(" 13) wpisz 13 aby dodać nową rezerwację")
print(" 14) wpisz 14 aby usunąć rezerwację")
print(" 15) wpisz 15 aby edytować rezerwację")
print(" 16) wpisz 16 aby wyświetlić informacje o rezerwacjach")

print()


def menu1():
    options = ["tytuł", "autora", "numer isbn", "wydawcę", "liczbę stron"]
    kwargs = []
    for opt in options:
        arg = input("podaj " + opt + " = ")
        kwargs.append(arg.strip())
    print(kwargs)
    try:
        Book.add_book(title=kwargs[0],
                      author=kwargs[1],
                      isbn=kwargs[2],
                      publisher=kwargs[3],
                      pages=kwargs[4])
    except Exception as e:
        print(f"Błąd przy dodawaniu książki: {e}")


def menu2():
    title = input("podaj tytuł książki = ")
    if Book.remove_book(title):
        print("usunięto książkę z bazy")


def menu3():
    title = input("podaj tytuł książki = ")
    Book.edit_book(title)


def menu4():
    Book.display_books()


people = Person.load()
def menu5():
    fname = input("Podaj imie: ")
    lname = input("Podaj nazwisko: ")
    address = input("Podaj adres: ")
    phone = input("Podaj numer telefonu: ")
    people.append(Person(fname=fname, lname=lname, address=address, phone=phone))
    Person.save(people)
def menu6():
    count = 1
    for person in people:
        print(count,  ". ",person.fname, person.lname, person.address, person.phone)
        count += 1
    nr = int(input("Usuń czytelnika o numerze: "))
    del people[nr-1]
    Person.save(people)
def menu7():
    count = 1
    for person in people:
        print(count, ". ", person.fname, person.lname, person.address, person.phone)
        count += 1
    nr = int(input("Edytuj czytelnika o numerze: "))
    fname = input("Podaj imie: ")
    people[nr - 1].fname = fname
    lname = input("Podaj nazwisko: ")
    people[nr - 1].lname = lname
    address = input("Podaj adres: ")
    people[nr - 1].address = address
    phone = input("Podaj numer telefonu: ")
    people[nr-1].phone = phone
    Person.save(people)
def menu8(): print("Wyświetlanie informacji o czytelniku...")


def menu9(): print("Dodawanie nowego wypożyczenia...")
def menu10(): print("Usuwanie wypożyczenia...")
def menu11(): print("Wyszukiwanie wypożyczenia...")
def menu12(): print("Wyświetlanie informacji o wypożyczeniu...")


def menu13(): print("Dodawanie nowej rezerwacji...")
def menu14(): print("Usuwanie rezerwacji...")
def menu15(): print("Wyszukiwanie rezerwacji...")
def menu16(): print("Wyświetlanie informacji o rezerwacji...")


while True:
    try:
        option = int(input("wybierz menu = "))
    except ValueError:
        print(f"Niepoprawna opcja –> wpisz liczbę całkowitą od 1 do 12")
    else:
        match option:
            case 1: menu1()
            case 2: menu2()
            case 3: menu3()
            case 4: menu4()
            case 5: menu5()
            case 6: menu6()
            case 7: menu7()
            case 8: menu8()
            case 9: menu9()
            case 10: menu10()
            case 11: menu11()
            case 12: menu12()
            case _: print(f"Niepoprawna opcja {option} –> wpisz liczbę całkowitą od 1 do 12")

