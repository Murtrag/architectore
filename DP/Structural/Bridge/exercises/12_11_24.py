from abc import ABC, abstractmethod

class Abstraction(ABC):
    def __init__(self, implementation: 'Implementation'):
        self.implementation = implementation
    
    @abstractmethod
    def method(self):
        pass 

class ConreteAbstraction(Abstraction):
    def method(self):
        self.implementation.method1()
        self.implementation.method2()
        self.implementation.method3()

class Implementation(ABC):
    @abstractmethod
    def method1(self) -> None:
        pass
    @abstractmethod
    def method2(self) -> None:
        pass
    @abstractmethod
    def method3(self) -> None:
        pass

class ConcreteImplementation(Implementation):
    def method1(self) -> None:
        print("Mehtod1")
    def method2(self) -> None:
        print("Mehtod2")
    def method3(self) -> None:
        print("Mehtod3")

a = ConreteAbstraction(ConcreteImplementation())
a.method()

