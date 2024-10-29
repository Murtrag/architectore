class CSingleton:
    _instance = None
    
    def __init__(self):
        raise RuntimeError('Call instance( instead')
    
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        return cls._instance

a = CSingleton.get_instance()
b = CSingleton.get_instance()
print(a is b)
