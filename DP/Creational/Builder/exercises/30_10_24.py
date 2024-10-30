# Exercise #1
# 1. Create a simple User class which holds such data as:
# 	a. fist_name - requred
# 	b. last_name - required
# 	c. age - optional
# 	d. phone_number - optional
# 	e. address - optional
# 	f. email_address - required
# 2. Make all these elements immutable in your User class, provide only getters.
# 3. Create a UserBuilder class that can build a user with the above elements and which then can be used to initialize the User class.
from abc import ABC, abstractmethod

class BaseUser(ABC):
    @abstractmethod
    def get_first_name(self):
        pass
    @abstractmethod
    def get_last_name(self):
        pass
    @abstractmethod
    def get_age(self):
        pass
    @abstractmethod
    def get_phone_number(self):
        pass
    @abstractmethod
    def get_address(self):
        pass
    @abstractmethod
    def get_email_address(self):
        pass
    @abstractmethod
    def present_user(self):
        pass

class User(BaseUser):
    def __init__(self, first_name, last_name, age, phone_number, address, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.address = address
        self.email_address = email_address

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address

    def get_email_address(self):
        return self.email_address

    def present_user(self):
        return (
            f"👤 User Details:\n"
            f"  - Full Name: {self.first_name} {self.last_name}\n"
            f"  - Age: {self.age}\n"
            f"  - Phone Number: {self.phone_number}\n"
            f"  - Address: {self.address}\n"
            f"  - Email Address: {self.email_address}\n"
        )

class BaseBuilder(ABC):
    @abstractmethod
    def build_user(self, **context) -> None:
        pass

    @abstractmethod
    def get_user(self) -> BaseUser:
        pass

class BuildUser(BaseBuilder):
    def build_user(self, **kwargs) -> None:
        self.user = User(**kwargs)

    def get_user(self) -> BaseUser:
        return self.user

class UserBuilder:
    def __init__(self, builder: BaseBuilder):
        self._builder = builder

    def set_builder(self, builder: BaseBuilder) -> None:
        self._builder = builder
    
    def build_user(self, context) -> BaseUser:
        self._builder.build_user(**context)
        return self._builder.get_user()


ub = UserBuilder(BuildUser())
user = ub.build_user({
    'first_name': 'Lukasz',
    'last_name': 'Kowalski',
    'age': '30',
    'phone_number': '12341234',
    'address': 'Sokolska 99',
    'email_address': 'lukasz.kowalski@gmail.com'
})
print(user.present_user())

