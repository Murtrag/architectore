class Handler:
    def __init__(self, successor=None):
        self.successor = successor # Zapisz nastepce

    def handle(self, request):
        handled = self._handle(request) # Sprubuj samemu

        if not handled and self.successor:  # Jak sie nie uda, to przekaz do nastepcy
            self.successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("You must implement _handle method")

class ConcreteHandler1(Handler):
    def _handle(self, request):
        if request == "car":
            print("Great, I like cars")
            return True
        return False

class ConcreteHandler2(Handler):
    def _handle(self, request):
        if request == "bus":
            print("I have no money for a bus!")
            return True
        return False

handler = ConcreteHandler1(ConcreteHandler2())

handler.handle("bus")
