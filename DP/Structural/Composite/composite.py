from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent: int = 0) -> None:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass


class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size

    def display(self, indent: int = 0) -> None:
        print(" " * indent + f"File: {self._name} ({self._size} KB)")

    def get_size(self) -> int:
        return self._size


class Directory(FileSystemComponent):
    def __init__(self, name:str):
        self._name = name
        self._children = []

    def add(self, component: FileSystemComponent) -> None:
        self._children.append(component)
    
    def remove(self, component: FileSystemComponent) -> None:
        self._children.remove(component)
    
    def display(self, indent: int=0) -> None:
        print(" " * indent + f"Directory: {self._name}")
        for child in self._children:
            child.display(indent + 1)
    
    def get_size(self) -> int:
        return sum(child.get_size() for child in self._children)
    
    # Przykład użycia
file1 = File("file1.txt", 10)
file2 = File("file2.txt", 20)
sub_dir = Directory("sub_dir")
sub_dir.add(file1)

root_dir = Directory("root")
root_dir.add(sub_dir)
root_dir.add(file2)

root_dir.display()
print(f"Total size: {root_dir.get_size()} KB")