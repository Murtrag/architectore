from abc import ABC, abstractmethod

class State:
    @abstractmethod
    def handle(self):
        pass

class StartState(State):
    def handle(self):
        print("Machine is in start state")
        return StopState()
    
class StopState(State):
    def handle(self):
        print("Machine is in stop state")
        return StartState()
    
class Context:
    def __init__(self):
        self.state = StartState()
    
    def request(self):
        self.state = self.state.handle()

c = Context()
c.request()
c.request()
c.request()