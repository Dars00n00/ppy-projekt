from datetime import datetime

class Borowing:

    late_return_fee_per_day = 1

    def __init__(self,**kwargs):
        self.id_person = kwargs.get("id_person")
        self.id_book = kwargs.get("id_book")
        self.date_from = datetime.today().date()
        self.date_to = kwargs.get("date_to")

    def calculate_fee(self):
        due_date = datetime.strptime(self.date_to, '%Y-%m-%d').date()
        today = datetime.today().date()
        days_late = (today - due_date).days
        return self.late_return_fee_per_day * max(days_late, 0)

b= Borowing(id_person=1, id_book=5, date_to="2025-02-25")
print(b.calculate_fee())
