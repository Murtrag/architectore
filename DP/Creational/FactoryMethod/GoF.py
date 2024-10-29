from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"
        
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass
    
class DogFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Dog()
        
class CatFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cat()
        
# Tworzymy fabrykę psa i kota
dog_factory = DogFactory()
cat_factory = CatFactory()

dog = dog_factory.create_animal()
print(dog.speak())