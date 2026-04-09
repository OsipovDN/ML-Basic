"""
Доработайте класс `Vehicle`
"""

from abc import ABC
from homework_05 import exceptions


class Vehicle(ABC):
    weight: float = 0
    started: bool = False
    fuel: float = 0
    fuel_consumption : float = 0

    def __init__(
            self, 
            weight: float, 
            fuel: float, 
            fuel_consumption: float):
        super().__init__()

        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError
            
    def move(self, distance: int):
        if not self.started:
            self.started = True
        if self.fuel == 0:
            raise exceptions.LowFuelError
        else:
            fuel = float(distance)*self.fuel_consumption/100
            if self.fuel < fuel:
                raise exceptions.NotEnoughFuel
            else:
                self.fuel -= fuel
        
            