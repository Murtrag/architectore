from abc import ABC, abstractmethod
from time import sleep

    
class ToasterState(ABC):
    @abstractmethod
    def load_toast(self) -> 'ToasterState':
        pass

    @abstractmethod
    def unload_toast(self) -> 'ToasterState':
        pass

    @abstractmethod
    def turn_on(self) -> 'ToasterState':
        pass

class EmptyToaster:
    def load_toast(self) -> 'ToasterState':
        print("Toaster has ben loaded with a raw delicious toast bread!")
        return LoadedToaster()

    @abstractmethod
    def unload_toast(self) -> 'ToasterState':
        print("You can't unload an empty toaster!")
        return EmptyToaster()

    @abstractmethod
    def turn_on(self) -> 'ToasterState':
        print("You try to turn on the empty toaster, but inmediatelly stops")
        return EmptyToaster()

class LoadedToaster:
    def load_toast(self) -> 'ToasterState':
        print("The toaster is already loaded")
        return LoadedToaster()

    def unload_toast(self) -> 'ToasterState':
        print("You take the raw bread out of the toaster")
        return EmptyToaster()

    @abstractmethod
    def turn_on(self) -> 'ToasterState':
        print("The toast is cooking!")
        sleep(1)
        print("pstryk")
        sleep(1)
        print("It smells good...")
        sleep(2)
        print("Almost ready!")
        sleep(1)
        print("Done!")
        return FinishedToaster()

class FinishedToaster:
    def load_toast(self) -> 'ToasterState':
        print("The toaster is still full! pleas unload it!")
        return LoadedToaster()

    def unload_toast(self) -> 'ToasterState':
        print("You take a delicious toast out of the toaster!")
        print("Well done!")
        return EmptyToaster()

    @abstractmethod
    def turn_on(self) -> 'ToasterState':
        print("The toast is already coocked!")
        print("You decide not to do it to avoid a fire")
        return FinishedToaster()

class Context:
    def __init__(self):
        self._state = EmptyToaster()

    def load_toast(self):
        self._state = self._state.load_toast()
    def unload_toast(self):
        self._state = self._state.unload_toast()
    def turn_on(self):
        self._state = self._state.turn_on()

t = Context()
t.load_toast()
t.load_toast()
t.load_toast()
t.load_toast()
t.turn_on()
t.unload_toast()
