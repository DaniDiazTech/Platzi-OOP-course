from python.base import BaseClass


class Payment(BaseClass):
    def __init__(self, id_: int, amount: float):
        super().__init__(id_) 

        self.amount = amount


class Card(Payment):
    def __init__(self, id_: int, amount: float, number: int, cvv: int, date: str):
        super().__init__(id_, amount)

        self.number = number
        self.cvv = cvv
        self.date = date

class PayPal(Payment):
    def __init__(self, id_: int, amount: float, email: str):
        super().__init__(id_, amount)
        self.email = email


class Cash(Payment):
    pass
