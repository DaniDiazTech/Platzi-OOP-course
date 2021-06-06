from python.base import BaseClass

from python.accounts import Driver

from python.defaults import default_seat_materials, default_car_types

class UberCar(BaseClass):

    def __init__(self, id_: int, license_: str, driver: Driver, passengers: int):
        super().__init__(id_)

        self.license = license_
        self.driver = driver
        self.passengers = passengers


class UberBasic(UberCar):
    def __init__(self, id_: int, license_: str, driver: Driver, passengers: int, brand: str, model: str):
        super().__init__(id_, license_, driver, passengers)

        self.brand = brand.lower()
        self.model = model.lower()

class UberPremium(UberCar):
    def __init__(self, id_: int, license_: str, driver: Driver, passengers: int, car_type: str, seat_material: str):
        super().__init__(id_, license_, driver, passengers)

        self.car_type = car_type.lower()
        self.seat_material = seat_material.lower()

        if not self.check_requirements:
            raise ValueError('Sorry, this cars doesn\'t meet the requirements')
            
    def check_requirements(self):
        return self.check_car_type and self.check_seat_materials
    
    def check_car_type(self, car_types: list = default_car_types):
        return self.car_type in car_types

    def check_seat_materials(self, seat_material: list = default_seat_materials):
        return self.seat_material in seat_material

    
class UberX(UberBasic):
    pass

class UberPoll(UberBasic):
    pass

class UberBlack(UberPremium):
    pass

class UberVan(UberPremium):
    pass

            
    