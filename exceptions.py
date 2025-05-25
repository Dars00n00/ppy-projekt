# book exceptions
class BookParameterException(Exception):
    def __init__(self, message):
        super().__init__(message)


class EmptyBookParameterException(Exception):
    def __init__(self, book_field):
        super().__init__(f"empty {book_field} field")



class EmptyReservationParameterException(Exception):
    def __init__(self, reservation_field):
        super().__init__(f"empty {reservation_field} field")
