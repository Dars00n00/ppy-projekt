from datetime import datetime, timedelta
from book import Book
from borrowing import Borrowing
from exceptions import WrongPersonParameterException, MultipleErrorsException, WrongBookParameterException
from person import Person
from reservation import Reservation


def menu1():  # dodaj książkę
    options = ["tytuł", "autora", "numer isbn", "wydawcę", "liczbę stron"]
    kwargs = []
    for opt in options:
        arg = input("podaj " + opt + " = ")
        kwargs.append(arg.strip())
    try:
        b = Book(id=Book.next_id(), title=kwargs[0], author=kwargs[1], isbn=kwargs[2],
                 publisher=kwargs[3], pages=kwargs[4])
        books = Book.load_books()
        books.append(b)
        Book.save_changes(books)
        print("dodano nową książkę: " + str(b))
    except MultipleErrorsException as e:
        print("błąd podczas dodawania nowej książki:\n" + str(e))
    except WrongBookParameterException as e:
        print("błąd podczas dodawania nowej książki -> " + str(e))


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

        b = Book(id=arg_id, title=kwargs[0],
                 author=kwargs[1],
                 isbn=kwargs[2],
                 publisher=kwargs[3],
                 pages=kwargs[4])
        Book.edit_book(arg_id, b)
        print("książka po edycji: " + str(b))
    except MultipleErrorsException as e:
        print("błąd podczas edycji książki:\n" + str(e))
    except WrongBookParameterException as e:
        print("błąd podczas edycji książki -> " + str(e))
    except Exception:
        pass


def menu4():  # wyświetl książki
    Book.display_books()
    Book.display_stats()


def menu5():
    people = Person.load()
    fname = input("Podaj imie: ").strip()
    lname = input("Podaj nazwisko: ").strip()
    address = input("Podaj adres: ").strip()
    phone = input("Podaj numer telefonu: ").strip()
    try:
        p = Person(fname=fname, lname=lname, address=address, phone=phone)
        people.append(p)
        Person.save(people)
        print("dodano nowego czytelnika: " + str(p))
    except MultipleErrorsException as e:
        print(str(e))
    except WrongPersonParameterException as e:
        print("błąd podczas dodawania nowego czytelnika -> " + str(e))
    except Exception as e:
        pass


def menu6():
    people = Person.load()
    for count, person in enumerate(people, start=1):
        print(count,  ". ", person.id, person.fname, person.lname, person.address, person.phone)

    nr = int(input("Usuń czytelnika o numerze: "))
    del people[nr-1]
    Person.save(people)


def menu7():
    people = Person.load()
    for count, person in enumerate(people, start=1):
        print(count, ". ", person.id, person.fname, person.lname, person.address, person.phone)
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
    reservations = Reservation.load_reservations()
    for count, person in enumerate(people, start=1):
        print(count, ". ", person.id, person.fname, person.lname, person.address, person.phone)
    Person.display_stats()
    nr = int(input("Wyświetl informacjie o czytelniku o numerze: "))
    Person.display_person_stats(people[nr-1]) ######################## wazne nie usuwaj shdas
    print("=========Rezerwacje=========")
    for reservation in reservations:
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
                        print(" | niezwrócona")


def menu9():
    people = Person.load()
    books = Book.load_books()
    borrowings = Borrowing.load()

    count = 1
    for person in people:
        print(count, ". ", person.id, person.fname, person.lname, person.address, person.phone)
        count += 1
    nr_czytelnika = int(input("Wypożycza czytelnik o numerze: ").strip())

    borrowed_book_ids = [b.id_book for b in borrowings if not b.returned]
    available_books = [book for book in books if book.id not in borrowed_book_ids]

    count = 1
    for book in available_books:
        print(count, ". ", book.title)
        count += 1
    nr_ksiazki = int(input("Wypożycza książkę o numerze: ").strip())
    date_to = input("Wypożycza do (YYYY-MM-DD): ").strip()

    borrowings.append(Borrowing(id_person=people[nr_czytelnika-1].id, id_book=available_books[nr_ksiazki-1].id, date_to=date_to))
    Borrowing.save(borrowings)


def menu10():
    people = Person.load()
    borrowings = Borrowing.load()
    reservations = Reservation.load_reservations()
    books = Book.load_books()
    people_ids = [person.id for person in people]
    for p in people:
        print(p)
    person_id = int(input("Podaj id osoby przedłużającej wypożyczenie = ").strip())
    if person_id not in people_ids:
        print("brak osoby o takim id -> powrót do menu")
        return
    persons_borrowings = [b for b in borrowings if b.id_person == person_id]
    persons_avaliable_borrowings = []
    for persons_borrowing in persons_borrowings:
        if not persons_borrowing.returned:
            decision = True
            for reservation in reservations:
                if reservation.book_id == persons_borrowing.id_book:
                    decision = False
            if decision:
                persons_avaliable_borrowings.append(persons_borrowing)
    avaliable_books = []
    for persons_borrowing in persons_avaliable_borrowings:
        for book in books:
            if book.id == persons_borrowing.id_book and datetime.strptime(persons_borrowing.date_to, '%Y-%m-%d').date() >= datetime.today().date():
                print(book, "||| aktualne wypozyczenie do", persons_borrowing.date_to)
                avaliable_books.append(book)
    if len(avaliable_books) == 0:
        print("Brak wypożyczonych książek lub są już zarezerwowane")
        return
    books_ids = [book.id for book in avaliable_books]
    book_id = int(input("Podaj id książki której wypożyczenie chcesz przedłużyć = ").strip())
    if book_id not in books_ids:
        print("brak dostępnej książki o takim id -> powrót do menu")
        return
    new_date_to = input("Podaj nową datę zwrotu książki (YYYY-MM-DD) = ").strip()
    for borrowing in borrowings:
        if borrowing.id_book == book_id and not borrowing.returned:
            if datetime.strptime(new_date_to, '%Y-%m-%d').date() <= datetime.strptime(borrowing.date_to, '%Y-%m-%d').date():
                print("nowa date zwrotu nie może być wcześniejsza niż poprzednia data zwrotu -> powrót do menu")
                return
            borrowing.date_to = new_date_to
    Borrowing.save(borrowings)


def menu11():
    people = Person.load()
    people_ids = [person.id for person in people]
    for p in people:
        print(p)
    person_id = int(input("Podaj id osoby zwracającej = ").strip())
    if person_id not in people_ids:
        print("brak osoby o takim id -> powrót do menu")
        return
    borrowings = Borrowing.load()
    books = Book.load_books()
    books_ids = []
    persons_borrowings = [b for b in borrowings if b.id_person == person_id]
    for persons_borrowing in persons_borrowings:
        for book in books:
            if book.id == persons_borrowing.id_book and not persons_borrowing.returned:
                books_ids.append(book.id)
                print(book, "||| Opłata: ", Borrowing.calculate_fee(persons_borrowing))
    if not books_ids:
        print("brak książek do zwrotu -> powrót do menu")
        return
    book_id = int(input("Podaj id ksiązki do zwrotu = ").strip())
    if book_id not in books_ids:
        print("brak książki o takim id -> powrót do menu")
        return
    for borrowing in borrowings:
        if borrowing.id_book == book_id and not borrowing.returned:
            borrowing.returned = True
    Borrowing.save(borrowings)

def menu12():  # dodaj rezerwację
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
    borrowed_book_ids = [b.id_book for b in borrowings if not b.returned and datetime.strptime(b.date_to, '%Y-%m-%d').date() > datetime.today().date()]
    borrowed_books = [book for book in books if book.id in borrowed_book_ids]
    books_ids = [book.id for book in borrowed_books]
    for borrowed_book in borrowed_books:
        print(borrowed_book, end="")
        for borrowing in borrowings:
            if borrowed_book.id == borrowing.id_book and borrowing.returned == False:
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
    print("  10) wpisz 10 aby przedłużyć wypożyczenie")
    print("  11) wpisz 11 aby zwrócić książkę")

    print("  12) wpisz 12 aby dodać nową rezerwację")

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
            case 11: menu11()
            case 12: menu12()
            #case 14: menu14()
            #case 15: menu15()
            #case 16: menu16()
            case _: print(f"Niepoprawna opcja {option} –> wpisz liczbę całkowitą od 1 do 10")

    nest = input("\nWciśnij ENTER aby przejść dalej").strip()
