"""
Создайте класс `Car`, наследник `Vehicle`
"""

from homework_05.base import Vehicle
from homework_05.engine import Engine

class Car(Vehicle):
    engine: Engine

    @engine.setter
    def engine(self, engine: Engine) -> None:
        self.engine = self.engine