# Exercise #1)
# 1. We have provided you with a source code (shipping.py) which needs to be refactored to use the Strategy Pattern.
#     a. Your task is to identify the main issue.
#     b. Correct it by refactoring the bad code into a number of Strategies.
# 2. We have provided you with simple console code to test your code.
#     a. you will need to test the following:
#         i. When the user switches the shipping method you should be able to dynamically switch which algorithm is being used.
# 3. After that, add a new Handler/Strategy for another shipping carrier:
#     a. Amazon Delivery
#     b. With the cost of delivery being 3.25
#     c. And add it as a new input option.       

# def calculate_shipping_cost(weight, carrier):
#     cost = 0
#     if carrier == "FedEx":
#         cost = weight * 2.5
#     elif carrier == "UPS":
#         cost = weight * 3
#     elif carrier == "DHL":
#         cost = weight * 4
#     return cost

# print("Select a carrier for shipping:")
# print("1. FedEx")
# print("2. UPS")
# print("3. DHL")

# choice = int(input("Enter the number corresponding to your choice: "))
# weight = float(input("Enter the weight of the package (in pounds): "))

# if choice == 1:
#     carrier = "FedEx"
# elif choice == 2:
#     carrier = "UPS"
# elif choice == 3:
#     carrier = "DHL"
# else:
#     print("Invalid choice!")
#     exit(1)

# shipping_cost = calculate_shipping_cost(weight, carrier)
# print(f"The shipping cost for {carrier} is ${shipping_cost:.2f}")
from abc import ABC, abstractmethod
from enum import Enum


class BaseStrategy(ABC):
    def __init__(self):
        self._weight = 0.0
    
    def set_weight(self, weight: float) -> None:
        self._weight = weight

    @abstractmethod
    def get_cost(self) -> float:
        pass

class FedExStrategy(BaseStrategy):
    def get_cost(self):
        return self._weight * 2.5

class UPSStrategy(BaseStrategy):
    def get_cost(self):
        return self._weight * 3

class DHLStrategy(BaseStrategy):
    def get_cost(self):
        return self._weight * 4

class AmazonStrategy(BaseStrategy):
    def get_cost(self):
        return self._weight * 3.25

class CarrierStrategies(Enum):
    FedEx = 1
    UPS = 2
    DHL = 3
    Amazon = 4

class ShippingCost:
    def set_strategy(self, strategy: BaseStrategy):
        self._strategy = strategy

    def set_weight(self, weight: float) -> None:
        self._strategy.set_weight(weight)

    def get_cost(self):
        return self._strategy.get_cost()

class PriceFactory:
    @staticmethod
    def get_cost(carrier: int, weight: float) -> float:
        shipping_cost = ShippingCost()
        if carrier == CarrierStrategies.FedEx.value:
            shipping_cost.set_strategy(FedExStrategy())
            shipping_cost.set_weight(weight)
            return shipping_cost.get_cost()
        elif carrier == CarrierStrategies.UPS.value:
            shipping_cost.set_strategy(UPSStrategy())
            shipping_cost.set_weight(weight)
            return shipping_cost.get_cost()
        elif carrier == CarrierStrategies.DHL.value:
            shipping_cost.set_strategy(DHLStrategy())
            shipping_cost.set_weight(weight)
            return shipping_cost.get_cost()
        elif carrier == CarrierStrategies.Amazon.value:
            shipping_cost.set_strategy(AmazonStrategy())
            shipping_cost.set_weight(weight)
            return shipping_cost.get_cost()
        else:
            raise NotImplemented("Carrier not recognized")

print("Select a carrier for shipping:")
print("1. FedEx")
print("2. UPS")
print("3. DHL")
print("4. Amazon")
while True:
    choice = int(input("Enter the number corresponding to your choice: "))
    weight = float(input("Enter the weight of the package (in pounds): "))
    result = PriceFactory.get_cost(
        choice, weight
    )
    print(result)

# Exercise #2)
# 1. You have a simple application that processes text data. The application can perform three different text transformations: uppercase, lowercase, and capitalize.
# 2. Currently, the code (which is in text_processing.py) is written without the strategy pattern, and you need to refactor it to use the strategy pattern.
# 3. This code does not have any testing or input capabilities, so please go back to exercise #1 and reuse that code structure to create the ability 
# to provide input text and which transformation is required and test it in your console.

# def process_text(text, operation):
#     if operation == "uppercase":
#         return text.upper()
#     elif operation == "lowercase":
#         return text.lower()
#     elif operation == "capitalize":
#         return text.capitalize()
#     else:
#         return text

# input_text = "This is an example text."
# operation = "uppercase"

# output_text = process_text(input_text, operation)
# print(output_text)
class BaseStrategy(ABC):
    @abstractmethod
    def transform(self, text: str) -> str:
        pass

class UppercaseStrategy(BaseStrategy):
    def transform(self, text: str) -> str:
        return text.upper()
class LowercaseStrategy(BaseStrategy):
    def transform(self, text: str) -> str:
        return text.lower()
class CapitalizeStrategy(BaseStrategy):
    def transform(self, text: str) -> str:
        return text.capitalize()
class TransformStrategies(Enum):
    uppercase = 1
    lowercase = 2
    capitalize = 3

class TransformText:
    def set_strategy(self, strategy: BaseStrategy):
        self._strategy = strategy
    
    def transform(self, text: str) -> str:
        return self._strategy.transform(text)

class TransformTextSimpleFactory:
    @staticmethod
    def transform(type: int, text: str) -> str:
        tt = TransformText()
        if type == TransformStrategies.uppercase.value:
            tt.set_strategy(UppercaseStrategy())
            return tt.transform(text)
        elif type == TransformStrategies.lowercase.value:
            tt.set_strategy(LowercaseStrategy())
            return tt.transform(text)
        elif type == TransformStrategies.capitalize.value:
            tt.set_strategy(CapitalizeStrategy())
            return tt.transform(text)



print("Types of transformation:")
print("1. Uppercase")
print("2. Lowercase")
print("3. Capitalize")
while True:
    raw_text = input("Put text to transorm: \n")
    choice = int(input("Put type of  transformation you want to perform: "))
    transformed = TransformTextSimpleFactory.transform(choice, raw_text)
    print(transformed)
