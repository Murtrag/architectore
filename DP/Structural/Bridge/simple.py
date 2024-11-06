from abc import ABC, abstractmethod
# Composition between Abstraction and implementation makes the bridge
# tv = TV()
# radio = Radio()

# tv_remote = Remote(tv)
# radio_remote = Remote(radio)

# tv_remote.toggle_power()  # Toggling power... TV is now ON
# radio_remote.toggle_power()
# Separates related objects 

class Abstraction(ABC):
    def __init__(self, implementation: Implementation):
        self._implementation = implementation
    
    @abstractmethod
    def operation(self):
        pass


class Implementation(ABC):
    @abstractmethod
    def method1(self):
        pass

class ConcreteImplementation1(ABC):
    def method1(self):
        pass
class ConcreteImplementation2(ABC):
    def method1(self):
        pass
class ConcreteImplementation3(ABC):
    def method1(self):
        pass

class RefinedAbstraction(Abstraction):
    def method5(self):
        pass

