# Lazy loading
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_buisnes_logic(self):
        pass

# Eagar loading
class SingletonMeta(type):
    _instances = {}
    def __init__(cls,name,bases,dct):
        super().__init__(name,bases,dct)
        cls._instances[cls] = super().__call__()
        
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_buisnes_logic(self):
        pass