from python.base import BaseClass

class Account(BaseClass):
    def __init__(self, id_: int, name: str, email: str, password: str):
        super().__init__(id_)

        self.name = name
        self.email = email
        self.password = password

class Driver(Account):
    pass

class Passenger(Account):
    pass