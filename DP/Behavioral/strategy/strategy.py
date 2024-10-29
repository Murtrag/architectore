from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> int:
        pass
    
class AddStrategy(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a + b
        
class SubtractStrategy(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a - b

class MultiplyStrategy(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a * b        

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
        
    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy
        
    def execute_strategy(self, a:int, b:int):
        return self._strategy.execute(a, b)
        

context = Context(AddStrategy())
print(context.execute_strategy(1,2))
context.set_strategy(SubtractStrategy())
print(context.execute_strategy(1,2))
context.set_strategy(MultiplyStrategy())
print(context.execute_strategy(1,2))