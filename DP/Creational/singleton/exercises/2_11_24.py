# Exercise #1)
# 1. Create a Singleton implementation which will generate a sequence of numbers to the callers.
#     a. The idea here is that there is only a single number/sequence generator and all the numbers follow a perfect sequence.
#     b. So when we do a call to the generator using something like getNextNumber() we should get the next number in the sequence
#     no matter how we obtained the generator.
# 2. Make that implemenation both with eager-instantiation and with lazy-instantiation.
#     a. Which one would you prefer to use and why?

# Lazy pythonic
class SequenceNumbers:
    _instance = None

    def __init__(self, start: int = 0, stop: int = 10, step = 1):
        self._start = start
        self._stop = stop
        self._step = step
        self._current = start

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def next(self) -> int:
        if self._current >= self._stop:
            return -1
        current = self._current
        self._current += self._step
        return current

sn = SequenceNumbers()
sn2 = SequenceNumbers()

print(sn.next())
print(sn2.next())
print(sn.next())
print(sn2.next())
print(sn.next())
print(sn2.next())
print(sn.next())
print(sn2.next())
print(sn.next())

print("\n\n\n\n\n\n\n\n")

# Eagar loading
class SingletonMeta(type):
    _instances = {}
    def __init__(cls,name,bases,dct):
        super().__init__(name,bases,dct)
        cls._instances[cls] = super().__call__()
        
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

class SequenceNumbers(metaclass=SingletonMeta):
    def __init__(self, start: int = 0, stop: int = 10, step = 1):
        self._start = start
        self._stop = stop
        self._step = step
        self._current = start
    
    def next(self) -> int:
        if self._current >= self._stop:
            return -1
        current = self._current
        self._current += self._step
        return current

sn = SequenceNumbers()
sn2 = SequenceNumbers()
print(sn.next())
print(sn2.next())
print(sn.next())
print(sn2.next())
print(sn.next())
print(sn2.next())
print(sn.next())
print(sn2.next())
print(sn.next())
print(sn2.next())
print(sn.next())
print(sn2.next())
print(sn.next())


# Lazy: saves memory when the instance is not in use, but may slow down the program when the instance needs to be created.
# Eager: makes the program run faster due to pre-instantiation of the Singleton, but uses memory resources immediately.
# Conclusion: if optimizing program speed is a priority and the Singleton will always be needed, the eager approach is recommended.
# However, if the Singleton instance might be optional and saving resources is important, lazy instantiation is the better choice.