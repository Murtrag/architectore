from abc import ABC, abstractmethod

class Car:
    def __init__(self):
        self.parts = []
        
    def add_part(self, part):
        self.parts.append(part)
        
    def __str__(self):
        return f"{self.parts}"


class CarBuilder(ABC):
    @abstractmethod
    def build_engine(self):
        pass
    
    @abstractmethod
    def build_wheels(self):
        pass
    
    @abstractmethod
    def build_body(self):
        pass
    
    @abstractmethod
    def get_car(self):
        pass
    
class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()
    def build_engine(self):
        self.car.add_part("Sports engine")
    def build_wheels(self):
        self.car.add_part("Sports wheels")
    def build_body(self):
        self.car.add_part("Sports body")
    def get_car(self):
        return self.car
    
class Director:
    def __init__(self, builder: CarBuilder):
        self._builder = builder
        
    def construct_car(self):
        self._builder.build_engine()
        self._builder.build_wheels()
        self._builder.build_body()
        
    def get_car(self):
        return self._builder.get_car()
    
director = Director(SportsCarBuilder())
director.construct_car()
sport_car = director.get_car()

print(sport_car)
