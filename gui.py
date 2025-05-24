import tkinter as tk


def open_book_management_menu():
    main_menu.iconify()
    new_menu = tk.Toplevel()
    new_menu.title("Zarządzanie książkami")
    new_menu.geometry("400x300")

    tk.Label(new_menu, text="To jest Menu 1").pack(pady=15)
    tk.Button(new_menu, text="Wróć do menu", command=lambda: [new_menu.destroy(), main_menu.deiconify()]).pack()


def open_reader_management_menu():
    main_menu.iconify()
    new_menu = tk.Toplevel()
    new_menu.title("Zarządzanie czytelnikami")
    new_menu.geometry("400x300")

    tk.Label(new_menu, text="To jest Menu 2").pack(pady=15)
    tk.Button(new_menu, text="Dodaj czytelnika", width=button_width).pack()
    tk.Button(new_menu, text="Usuń czytelnika", width=button_width).pack()
    tk.Button(new_menu, text="Wyświetl czytelników", width=button_width).pack()
    tk.Button(new_menu, text="Wróć do menu", command=lambda: [new_menu.destroy(), main_menu.deiconify()]).pack()


def open_reservation_management_menu():
    main_menu.iconify()
    new_menu = tk.Toplevel()
    new_menu.title("Zarządzanie rezerwacjami")
    new_menu.geometry("400x300")

    tk.Label(new_menu, text="To jest Menu 3").pack(pady=15)
    tk.Button(new_menu, text="Wróć do menu", command=lambda: [new_menu.destroy(), main_menu.deiconify()]).pack()


main_menu = tk.Tk()
main_menu.title("System zarządzania biblioteką")
main_menu.geometry("400x300")

tk.Label(main_menu, text="Witaj!").pack(pady=10)

button_width = 25

tk.Button(main_menu, text="Zarządzania książkami", width=button_width, command=open_book_management_menu).pack(pady=10)
tk.Button(main_menu, text="Zarządzanie czytelnikami", width=button_width, command=open_reader_management_menu).pack(pady=10)
tk.Button(main_menu, text="Zarządzanie wypożyczeniami", width=button_width, command=open_reservation_management_menu).pack(pady=10)

main_menu.mainloop()
