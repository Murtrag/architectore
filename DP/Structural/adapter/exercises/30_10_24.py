# Exercise 1)
# 1. Add an additional adapter to the lecture code which will provide a conversion from CSV format to the format we render.
#     a. To do that come up with your own test CSV format that your code will be able to read.
#     b. Parsing the CSV should be relative easy with Python's csv parsing module.
#     c. Test your adapter with the existing code by making sure that your adapter can properly read and convert the CSV Data.
import csv
from abc import ABC, abstractmethod

class CSVParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        data = []
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data

cvpar = CSVParser('DP/Structural/adapter/exercises/data.txt')
print(
    cvpar.read_data()
)

class CSVAdapter:
    def __init__(self, adaptee):
        self._adaptee = adaptee
    def convert(self):
        data = self._adaptee.read_data()
        result = []
        for row in data:
            result.append({
                'full_name': f"{row['first_name']} {row['last_name']}",
                'age': int(row['age']),
                'email': row['email']
            })
        return result
cvadapter = CSVAdapter(CSVParser('DP/Structural/adapter/exercises/data.txt'))
print(cvadapter.convert())
# Exercise 2)
# 1. Consider the Legacy Rectangle provided in the Adapter Pattern lecture.
#     a. Create an Adapter which will take the legacy Rectangle and convert it into the new Rectangle signature.
#     Legacy Rectangle class which uses the following constructor.
#     ``` Rectangle rect = Rectangle(x, y, w, h) ```
#     New version of Rectangle uses the following constructor:
#     ``` Rectangle rect = Rectangle(x1, y1, x2, y2) ```
#     b. Remember: the key point here is that you have a Rectangle already which needs to be adapted to the new signature.

class LegacyRectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def get_position_and_size(self):
        return f"Top-left corner: ({self.x}, {self.y}), Width: {self.width}, Height: {self.height}"

class AdapterRectangle:
    def __init__(self, x1, y1, x2, y2):
        dimensions = { 'x': x1, 'y': y1, 'w': x2 - x1, 'h': y2 - y1 }
        self._adaptee = LegacyRectangle(**dimensions)
    
    def get_position_and_size(self):
        return self._adaptee.get_position_and_size()

adapter = AdapterRectangle(0, 0, 10, 5)
print(adapter.get_position_and_size())