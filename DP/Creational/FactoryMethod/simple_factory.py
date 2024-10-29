# More popular than GoF version

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self)
        return "Woof!"
        
class Cat(Animal):
    def speak(self)
        return "Woof!"
        
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
#         elif animal_type == 'lion':
#            return Lion()
        else:
            raise ValueError(f"Unknow animal type: {animal_type}")