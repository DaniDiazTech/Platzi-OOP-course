from python.base import BaseClass

class Route(BaseClass):
    def __init__(self, id_: int, start: tuple, end: tuple):
        super().__init__(id_)

        self.start = start
        self.end = end