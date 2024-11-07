from abc import ABC, abstractmethod

class Abstract(ABC):
    def __init__(self, implementation: 'Implementation'):
        self.implementation = implementation
    
    @abstractmethod
    def method(self):
        pass

class ConcreteAbstract(Abstract):
    def method(self):
        return [
            self.implementation.method1(),
            self.implementation.method2()
        ]

class Implementation(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

class ConcreteImplementation(Implementation):
    def method1(self):
        return "method1"
    def method2(self):
        return "method2"

a = ConcreteAbstract(ConcreteImplementation())
print(
    a.method()
)