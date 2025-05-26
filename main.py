from datetime import datetime, timedelta
from book import Book
from borrowing import Borrowing
from person import Person
from reservation import Reservation


def menu1():  # dodaj książkę
    options = ["tytuł", "autora", "numer isbn", "wydawcę", "liczbę stron"]
    kwargs = []
    for opt in options:
        arg = input("podaj " + opt + " = ")
        kwargs.append(arg.strip())
    try:
        Book.add_book(title=kwargs[0], author=kwargs[1], isbn=kwargs[2],
                      publisher=kwargs[3], pages=kwargs[4])
    except Exception as e:
        print(f"Błąd przy dodawaniu książki: {e}")


def menu2():  # usuń książkę
    books = Book.load_books()
    for book in books:
        print(book)
    arg_id = int(input("wybierz numer książki do usunięcia = "))
    Book.remove_book(arg_id)


def menu3():  # edytuj książkę
    books = Book.load_books()
    for book in books:
        print(book)

    try:
        arg_id = int(input("wybierz numer książki do edycji = "))
        options = ["tytuł", "autor", "numer isbn", "wydawca", "numer stron"]
        kwargs = []
        for opt in options:
            arg = input("nowy " + opt + " = ")
            kwargs.append(arg.strip())

        b = Book(title=kwargs[0],
                 author=kwargs[1],
                 isbn=kwargs[2],
                 publisher=kwargs[3],
                 pages=kwargs[4])
        Book.edit_book(arg_id, b)
    except ValueError:
        print("podaj liczbę")


def menu4():  # wyświetl książki
    Book.display_books()
    Book.display_stats()


def menu5():
    people = Person.load()
    fname = input("Podaj imie: ").strip()
    lname = input("Podaj nazwisko: ").strip()
    address = input("Podaj adres: ").strip()
    phone = input("Podaj numer telefonu: ").strip()
    people.append(Person(fname=fname, lname=lname, address=address, phone=phone))
    Person.save(people)


def menu6():
    people = Person.load()
    #count = 1
    for count, person in enumerate(people, start=1):
        print(count,  ". ", person.id, person.fname, person.lname, person.address, person.phone)
        #count += 1
    nr = int(input("Usuń czytelnika o numerze: "))
    del people[nr-1]
    Person.save(people)


def menu7():
    people = Person.load()
    #count = 1
    for count, person in enumerate(people, start=1):
        print(count, ". ", person.id, person.fname, person.lname, person.address, person.phone)
        #count += 1
    nr = int(input("Edytuj czytelnika o numerze: "))
    fname = input("Podaj imie: ").strip()
    people[nr - 1].fname = fname
    lname = input("Podaj nazwisko: ").strip()
    people[nr - 1].lname = lname
    address = input("Podaj adres: ").strip()
    people[nr - 1].address = address
    phone = input("Podaj numer telefonu: ").strip()
    people[nr-1].phone = phone
    Person.save(people)


def menu8():
    people = Person.load()
    books = Book.load_books()
    borrowings = Borrowing.load()
    revervations = Reservation.load_reservations()

    count = 1
    for count, person in enumerate(people, start=1):
        print(count, ". ", person.id, person.fname, person.lname, person.address, person.phone)
        #count += 1
    Person.display_stats()
    nr = int(input("Wyświetl informacjie o czytelniku o numerze: "))
    print("=========Rezerwacje=========")
    for reservation in revervations:
        if people[nr - 1].id == reservation.person_id:
            for book in books:
                if book.id == reservation.book_id:
                    print(book.title, "od" , reservation.begin_date, "do", reservation.end_date)
    print("=========Wypożyczenia=========")
    for borrowing in borrowings:
        if people[nr - 1].id == borrowing.id_person:
            for book in books:
                if book.id == borrowing.id_book:
                    print(book.title, "od" , borrowing.date_from, "do", borrowing.date_to, end="")
                    if borrowing.returned == True:
                        print(" | zwrócona")
                    else:
                        print("| niezwrócona")
    Person.display_person_stats(people[nr-1])


def menu9():
    people = Person.load()
    books = Book.load_books()
    borrowings = Borrowing.load()

    count = 1
    for person in people:
        print(count, ". ", person.id, person.fname, person.lname, person.address, person.phone)
        count += 1
    nr_czytelnika = int(input("Wypożycza czytelnik o numerze: "))

    borrowed_book_ids = {b.id_book for b in borrowings if not b.returned}
    available_books = [book for book in books if book.id not in borrowed_book_ids]

    #count = 1
    for count, book in enumerate(available_books, start=1):
        print(count, ". ", book.title)
        #count += 1
    nr_ksiazki = int(input("Wypożycza książkę o numerze: "))
    date_to = input("Wypożycza do (YYYY-MM-DD): ").strip()

    borrowings.append(Borrowing(id_person=people[nr_czytelnika-1].id, id_book=available_books[nr_ksiazki-1].id, date_to=date_to))
    Borrowing.save(borrowings)


def menu10():  # dodaj rezerwację
    people = Person.load()
    people_ids = [person.id for person in people]
    for p in people:
        print(p)
    person_id = int(input("Podaj id osoby dokonującej rezerwację = ").strip())
    if person_id not in people_ids:
        print("brak osoby o takim id -> powrót do menu")
        return

    books = Book.load_books()
    borrowings = Borrowing.load()
    borrowed_book_ids = {b.id_book for b in borrowings if not b.returned}
    borrowed_books = [book for book in books if book.id in borrowed_book_ids]
    books_ids = [book.id for book in borrowed_books]
    for b in borrowed_books:
        print(b, end="")
        for borrowing in borrowings:
            if b.id == borrowing.id_book and borrowing.returned == False:
                print(" |||| Dostępna od", borrowing.date_to)
    book_id = int(input("Podaj id książki do rezerwacji = ").strip())
    if book_id not in books_ids:
        print("brak książki o takim id -> powrót do menu")
        return

    begin_date = ""
    for borrowing in borrowings:
        if book_id == borrowing.id_book and borrowing.returned == False:
            begin_date = borrowing.date_to

    parsedBegin = datetime.strptime(begin_date, '%Y-%m-%d').date()
    pasrsedEnd = parsedBegin + timedelta(days=3)

    Reservation.add_reservation(
        person_id=person_id,
        book_id=book_id,
        begin_date=parsedBegin.strftime("%Y-%m-%d"),
        end_date=pasrsedEnd.strftime("%Y-%m-%d"),)


def menu14():  # usuń rezerwację
    reservations = Reservation.load_reservations()
    for r in reservations:
        print(r)
    reservation_id = int(input("wybierz numer rezerwacji do usunięcia = "))
    removed = Reservation.remove_reservation(reservation_id - 1)
    print(f"usunięto rezerwację {removed}")


def menu15():  # znajdź rezerwację
    print("Wyszukiwanie rezerwacji...")


def menu16():  # wyświetl rezerwacje
    Reservation.display_reservations()


while True:
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

    print(" 10) wpisz 10 aby dodać nową rezerwację")
    #print(" 14) wpisz 14 aby usunąć rezerwację")
    #print(" 15) wpisz 15 aby edytować rezerwację")
    #print(" 16) wpisz 10 aby wyświetlić informacje o rezerwacjach")

    print()
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
            #case 14: menu14()
            #case 15: menu15()
            #case 16: menu16()
            case _: print(f"Niepoprawna opcja {option} –> wpisz liczbę całkowitą od 1 do 10")

    nest = input("\nWciśnij ENTER aby przejść dalej").strip()
