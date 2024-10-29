from abc import ABC

class OldSystem:
    def old_request(self):
        return "Stary system: Specyficzne zadanie"
        
class INewSystem(ABC):
    def request(self):
        pass
    
class Adapter(INewSystem):
    def __init__(self, old_system):
        self.old_system = old_system
        
    def request(self):
        return self.old_system.old_request()
        
os = OldSystem()
adapter = Adapter(os)

print(adapter.request())