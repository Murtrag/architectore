from abc import ABC, abstractmethod

class Subject:
    def __init__(self):
        self._subscribers = []
        self._state = None
    
    def subscribe(self, subscriber: 'Subscriber'):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: 'Subscriber'):
        self._subscribers.remove(subscriber)
    
    def notify(self):
        for subscriber in self._subscribers:
            subscriber.update(self._state)
    
    def set_state(self, state):
        self._state = state
        self.notify()


class Subscriber(ABC):
    def update(self, state:list):
        pass

class ConcreteSubscriberA(Subscriber):
    def update(self, state):
        print(f"ConcreteObserverA: Zaktualizowany stan to {state}")

subject = Subject()
a = ConcreteSubscriberA()
subject.subscribe(a)

subject.set_state("stan 1")