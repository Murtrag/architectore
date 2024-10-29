import copy

class Prototype:
    def copy(self):
        return copy.deepcopy(self)

class Light(Prototype):
    def turn_on(self):
        print("turn on")

    def turn_off(self):
        print("turn off")


a = Light()

a.turn_on()
a.turn_off()

b = a.copy()

b.turn_on()
b.turn_off()
