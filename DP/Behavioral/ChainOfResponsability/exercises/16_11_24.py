
from abc import abstractmethod, ABC
class AbstractChain(ABC):
    def __init__(self, successor: 'AbstractChain' = None):
        self._successor = successor
    
    def handle(self, request: str):
        handled = self._handle(request)
        if not handled and self._successor:
            self._successor.handle(request)
    
    @abstractmethod
    def _handle(self, request: str) -> bool:
        pass

class ConcreteChain1(AbstractChain):
    def _handle(self, request: str) -> bool:
        if request == "banana":
            print("is a banana")
            return True
        return False
class ConcreteChain2(AbstractChain):
    def _handle(self, request: str) -> bool:
        if request == "apple":
            print("is an apple")
            return True
        return False
class ConcreteChain3(AbstractChain):
    def _handle(self, request: str) -> bool:
        if request == "dog":
            print("is a dog")
            return True
        return False

c = ConcreteChain1(
    ConcreteChain2(
        ConcreteChain3()
    )
)

c.handle("dog")
c.handle("appel")
c.handle("apple")
c.handle("banana")

    