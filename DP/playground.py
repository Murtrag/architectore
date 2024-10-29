from abc import ABC, abstractmethod
from time import sleep

class SystemFile(ABC):
    def __init__(self, name):
        self.name = name

    def display(self):
        pass

    def get_size(self):
        pass
class File(SystemFile):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def display(self):
        print(self.name)
    
    def get_size(self):
        return self.size

class Directory(SystemFile):
    def __init__(self, name):
        super().__init__(name)
        self.children = []
    
    def add(self, file):
        self.children.append(file)

    def remove(self, file):
        self.children.remove(file)

    def display(self):
        print(self.name)
        for f in self.children:
            f.display()

    def get_size(self):
        return sum( f.get_size() for f in self.children)

    # Przykład użycia
# Composite usage
file1 = File("file1.txt", 10)
file2 = File("file2.txt", 20)
sub_dir = Directory("sub_dir")
sub_dir.add(file1)

root_dir = Directory("root")
root_dir.add(sub_dir)
root_dir.add(file2)

root_dir.display()
print(f"Total size: {root_dir.get_size()} KB")