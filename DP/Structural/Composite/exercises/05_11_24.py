from abc import ABC, abstractmethod

class FileSystem(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def get_size(self) -> float:
        pass

    @abstractmethod
    def display(self) -> None:
        pass


class File(FileSystem):

    def __init__(self, name: str, size: float):
        super().__init__(name)
        self._size = size

    def display(self) -> None:
        print( f"{self._name} ({self._size})")

    def get_size(self) -> float:
        return self._size

class Directory(FileSystem):
    def __init__(self, name: str):
        super().__init__(name)
        self._children = []

    def add(self, file: FileSystem):
        self._children.append(file)

    def remove(self, file: FileSystem):
        self._children.remove(file)
    
    def get_size(self):
        return sum(
            file.get_size() for file in self._children
        )

    def display(self) -> None:
        print(self._name) 
        for file in self._children:
            file.display()




file1 = File("file1.txt", 10)
file2 = File("file2.txt", 20)
sub_dir = Directory("sub_dir")
sub_dir.add(file1)

root_dir = Directory("root")
root_dir.add(sub_dir)
root_dir.add(file2)

root_dir.display()
print(f"Total size: {root_dir.get_size()} KB")