from typing import Union


# =======================  wrong parameter exceptions =======================
class WrongBookParameterException(Exception):
    def __init__(self, param_name: str, param_value):
        self.param_name = param_name
        self.param_value = param_value

    def __str__(self):
        if self.param_value is None or str(self.param_value).strip() == "":
            value_str = '""'
        else:
            value_str = str(self.param_value)
        return f"błędne lub puste pole ({self.param_name}) = {value_str}"


class WrongPersonParameterException(Exception):
    def __init__(self, field_name: str, field_value: str):
        super().__init__(f"błędne lub puste pole ({field_name}) = {field_value}")


class WrongReservationParameterException(Exception):
    def __init__(self, field_name: str, field_value: str):
        super().__init__(f"błędne lub puste pole ({field_name}) = {field_value}")


class WrongBorrowingParameterException(Exception):
    def __init__(self, field_name: str, field_value: str):
        super().__init__(f"błędne lub puste pole ({field_name}) = {field_value}")


class MultipleErrorsException(Exception):
    def __init__(self, errors: list):
        message = "\n".join(str(e) for e in errors)
        super().__init__(message)
        self.errors = errors


# class EmptyBookParameterException(Exception):
#     def __init__(self, book_field):
#         super().__init__(f"puste pole {book_field}")
#
#
# # reservation exceptions
# class EmptyReservationParameterException(Exception):
#     def __init__(self, reservation_field):
#         super().__init__(f"puste pole {reservation_field}")


# =======================  not found exceptions =======================
class NoPersonFoundException(Exception):
    def __init__(self, id_person: Union[int, str]):
        super().__init__(f"nie znaleziono osoby o id {str(id_person)}")


class NoBookFoundException(Exception):
    def __init__(self, id_book: Union[int, str]):
        super().__init__(f"nie znaleziono książki o id {str(id_book)}")


class NoReservationFoundException(Exception):
    def __init__(self, id_reservation: Union[int, str]):
        super().__init__(f"nie znaleziono rezerwacji o id {str(id_reservation)}")


class NoBorrowingFoundException(Exception):
    def __init__(self, id_borrowing: Union[int, str]):
        super().__init__(f"nie znaleziono wypożyczenia o id {str(id_borrowing)}")

class EmptyCollectionException(Exception):
    def __init__(self, msg):
        super().__init__(msg)