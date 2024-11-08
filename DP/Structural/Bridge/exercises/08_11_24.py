from abc import ABC, abstractmethod

class Abstraction(ABC):
    def __init__(self, implementation: 'Implementation'):
        self.implementation = implementation
    
    @abstractmethod
    def methods(self):
        pass

class ConcreteAbstraction(Abstraction):
    def methods(self):
        self.implementation.method1()
        self.implementation.method2()
        self.implementation.method3()

class Implementation(ABC):
    @abstractmethod
    def method1(self):
        pass
    @abstractmethod
    def method2(self):
        pass
    @abstractmethod
    def method3(self):
        pass

class ConcreteImplementation(Implementation):
    def method1(self):
        print("mehtod 1")
    def method2(self):
        print("mehtod 2")
    def method3(self):
        print("mehtod 3")
 
a = ConcreteAbstraction(ConcreteImplementation())
a.methods()