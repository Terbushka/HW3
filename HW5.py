# 1.
class Laptop:
    """
    Make the class with composition.
    """

    def __init__(self, name, battery_type, battery_capacity):
        self.name = name
        self.battery = Battery(battery_type, battery_capacity)

    def __str__(self):
        return f'{self.name} with battery {self.battery}'


class Battery:
    """
    Make the class with composition.
    """

    def __init__(self, battery_type, battery_capacity):
        self.battery_type = battery_type
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f'{self.battery_type} {self.battery_capacity}'


laptop = Laptop('Xiaomi Mi Notebook Pro', 'Li-ion polymer battery', '8000mAh')
print(laptop)


# 2.
class Guitar:
    """
    Make the class with aggregation
    """

    def __init__(self, name, strings):
        self.name = name
        self.strings = strings

    def __str__(self):
        return f'{self.name} has {len(self.strings)} strings'


class GuitarString:
    """
    Make the class with aggregation
    """

    def __init__(self, length):
        self.length = length

    def __str__(self):
        return f'string with length {self.length}'


string1 = GuitarString(10)
string2 = GuitarString(10)
string3 = GuitarString(10)
string4 = GuitarString(10)
string5 = GuitarString(10)
my_strings = [string1, string2, string3, string4, string5]
guitar = Guitar('Guitar', my_strings)
print(guitar)


# 3
class Calc:
    """
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """

    @staticmethod
    def add_nums(num1, num2, num3):
        return num1 + num2 + num3


print(Calc.add_nums(1, 2, 3))


# 4*.
class Pasta:
    """
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """

    def __init__(self, ingredients):
        self.ingridients = ingredients

    @classmethod
    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(["tomato", "cucumber"])
pasta_2 = Pasta.bolognaise()
print(pasta_1.ingridients)
print(pasta_2.ingridients)


# 5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    max_visitor_num = 0

    def __init__(self, visitors_count=0):
        self._visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, x):
        self._visitors_count = min(self.max_visitor_num, x)


Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)


# 6.
import dataclasses

@dataclasses.dataclass
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
    """
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


ab1 = AddressBookDataClass(1, 'Anton', '+380985424561', 'Lviv', 'Anton@i.ua', '01-08-1995', 26)
print(ab1)


# 7. Create the same class (6) but using NamedTuple
import collections

AddressBookDataClass = collections.namedtuple('AddressBookDataClass',
                                              ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])
ab2 = AddressBookDataClass(1, 'Anton', '+380985424561', 'Lviv', 'Anton@i.ua', '01-08-1995', 26)
print(ab2)


# 8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """

    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"{__class__.__name__}(key={self.key}, name='{self.name}', phone_number='{self.phone_number}', address='{self.address}', email='{self.email}', birthday='{self.birthday}', age={self.age})"


ab3 = AddressBook(1, 'Anton', '+380985424561', 'Lviv', 'Anton@i.ua', '01-08-1995', 26)
print(ab3)


# 9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


person = Person()
person.age = 40
print(person.age)


# 10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(123, "John")
student.email = 'john@gmail.com'
setattr(student, 'student_email', 'john@yahoo.com')
print(getattr(student, 'student_email'))


# 11*.
class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return (self._temperature * 1.8) + 32


temp = Celsius(36.6)
print(temp.temperature)
