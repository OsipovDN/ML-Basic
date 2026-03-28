"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: float
    max_cargo: float

    
    def __init__(self, max_cargo: float):
        super().__init__()


    def load_cargo(self, cargo: float):
        if (self.cargo + cargo) > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo += cargo